"""Unified HTTP client for all Essabu SDK modules.

Provides a requests-based HTTP client with automatic authentication,
retry logic with exponential backoff, and unified error mapping.
"""

from __future__ import annotations

import time
from typing import Any

import httpx

from essabu.common.exceptions import (
    AuthenticationError,
    AuthorizationError,
    EssabuError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)

_BASE_DELAY_S = 1.0


class HttpClient:
    """HTTP client with automatic auth, retry, and error mapping.

    Supports both ``api_key`` (Bearer) and ``tenant_id`` (multi-tenant)
    authentication patterns used across different Essabu services.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        tenant_id: str | None = None,
        token: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        headers: dict[str, str] | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._max_retries = max_retries

        default_headers: dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "essabu-python/1.0.0",
        }

        if api_key:
            default_headers["Authorization"] = f"Bearer {api_key}"
        elif token:
            default_headers["Authorization"] = f"Bearer {token}"

        if tenant_id:
            default_headers["X-Tenant-Id"] = tenant_id

        if headers:
            default_headers.update(headers)

        transport = httpx.HTTPTransport(retries=0)
        self._client = httpx.Client(
            base_url=self._base_url,
            headers=default_headers,
            timeout=timeout,
            transport=transport,
        )

    def set_token(self, token: str) -> None:
        """Update the bearer token for subsequent requests."""
        self._client.headers["Authorization"] = f"Bearer {token}"

    # -- Public HTTP methods --------------------------------------------------

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        """Perform a GET request and return the parsed JSON response."""
        return self._execute("GET", path, params=params)

    def get_bytes(self, path: str) -> bytes:
        """Perform a GET request and return the raw response bytes."""
        response = self._execute_raw("GET", path)
        return response.content

    def post(self, path: str, data: dict[str, Any] | None = None) -> Any:
        """Perform a POST request with a JSON body and return parsed JSON."""
        return self._execute("POST", path, json_body=data)

    def post_empty(self, path: str) -> Any:
        """Perform a POST request without a body and return parsed JSON."""
        return self._execute("POST", path)

    def put(self, path: str, data: dict[str, Any] | None = None) -> Any:
        """Perform a PUT request with a JSON body and return parsed JSON."""
        return self._execute("PUT", path, json_body=data)

    def patch(self, path: str, data: dict[str, Any] | None = None) -> Any:
        """Perform a PATCH request with a JSON body and return parsed JSON."""
        return self._execute("PATCH", path, json_body=data)

    def delete(self, path: str) -> Any:
        """Perform a DELETE request."""
        return self._execute("DELETE", path)

    def post_multipart(
        self,
        path: str,
        files: dict[str, Any],
        data: dict[str, Any] | None = None,
    ) -> Any:
        """Perform a multipart/form-data POST request for file uploads."""
        response = self._client.post(path, files=files, data=data)
        self._raise_for_status(response)
        if response.status_code == 204 or not response.content:
            return None
        return response.json()

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        """Execute a generic HTTP request (used by trade/payment patterns)."""
        response = self._client.request(method, path, **kwargs)
        return self._handle_response(response)

    # -- Private helpers ------------------------------------------------------

    def _execute(
        self,
        method: str,
        path: str,
        json_body: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        last_exception: Exception | None = None

        for attempt in range(self._max_retries + 1):
            try:
                response = self._client.request(
                    method,
                    path,
                    json=json_body,
                    params=params,
                )

                if response.status_code >= 500 and attempt < self._max_retries:
                    time.sleep(min(_BASE_DELAY_S * (2 ** attempt), 10))
                    continue

                self._raise_for_status(response)

                if response.status_code == 204 or not response.content:
                    return None

                return response.json()

            except (httpx.ConnectError, httpx.TimeoutException) as exc:
                last_exception = exc
                if attempt < self._max_retries:
                    time.sleep(min(_BASE_DELAY_S * (2 ** attempt), 10))
                    continue
                raise ServerError(
                    f"Communication error with the Essabu API: {exc}",
                    details={"cause": str(exc)},
                ) from exc

        if last_exception:
            raise ServerError(
                f"Communication error with the Essabu API: {last_exception}",
                details={"cause": str(last_exception)},
            ) from last_exception
        return None

    def _execute_raw(self, method: str, path: str) -> httpx.Response:
        response = self._client.request(method, path)
        self._raise_for_status(response)
        return response

    def _handle_response(self, response: httpx.Response) -> Any:
        """Parse response and raise appropriate exceptions."""
        if response.status_code in (200, 201):
            if not response.content:
                return None
            return response.json()
        if response.status_code == 204:
            return None

        self._raise_for_status(response)
        return None

    def _raise_for_status(self, response: httpx.Response) -> None:
        status = response.status_code

        if 200 <= status < 300:
            return

        message = self._extract_message(response)
        details = self._extract_details(response)

        if status in (400, 422):
            raise ValidationError(
                message, errors=details, details=details
            )
        if status == 401:
            raise AuthenticationError(message, details=details)
        if status == 403:
            raise AuthorizationError(message, details=details)
        if status == 404:
            raise NotFoundError(message, details=details)
        if status == 429:
            retry_after_header = response.headers.get("Retry-After")
            retry_after = int(retry_after_header) if retry_after_header else None
            raise RateLimitError(message, retry_after=retry_after, details=details)
        if status >= 500:
            raise ServerError(message, details=details)

        raise EssabuError(message, status_code=status, details=details)

    @staticmethod
    def _extract_message(response: httpx.Response) -> str:
        try:
            data = response.json()
            return str(
                data.get("message")
                or data.get("error")
                or response.reason_phrase
                or "Unknown error"
            )
        except Exception:
            return response.reason_phrase or "Unknown error"

    @staticmethod
    def _extract_details(response: httpx.Response) -> dict[str, Any]:
        try:
            data = response.json()
            return (
                data.get("violations")
                or data.get("details")
                or data.get("errors")
                or {}
            )
        except Exception:
            return {}

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> HttpClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
