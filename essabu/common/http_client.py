"""HTTP client with retry logic, authentication, and error mapping."""

from __future__ import annotations

import time
from collections.abc import Generator
from typing import Any

import httpx

from essabu.common.auth import build_auth_headers
from essabu.common.exceptions import (
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    ConflictError,
    EssabuError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from essabu.common.models import PageRequest, PageResponse
from essabu.config import EssabuConfig

_STATUS_MAP: dict[int, type[EssabuError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: AuthorizationError,
    404: NotFoundError,
    409: ConflictError,
    422: ValidationError,
    429: RateLimitError,
}


class HttpClient:
    """Low-level HTTP client wrapping httpx with retry and error mapping."""

    def __init__(self, config: EssabuConfig) -> None:
        self._config = config
        self._client: httpx.Client | None = None

    @property
    def client(self) -> httpx.Client:
        if self._client is None or self._client.is_closed:
            self._client = httpx.Client(
                base_url=self._config.base_url,
                headers=build_auth_headers(self._config),
                timeout=httpx.Timeout(
                    timeout=self._config.timeout,
                    connect=self._config.connect_timeout or self._config.timeout,
                    read=self._config.read_timeout or self._config.timeout,
                ),
            )
        return self._client

    def close(self) -> None:
        """Close the underlying HTTP client."""
        if self._client is not None and not self._client.is_closed:
            self._client.close()

    # -- Core request method -------------------------------------------------

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: Any = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Execute an HTTP request with retry logic and error mapping.

        Returns the parsed JSON response body.
        """
        last_exc: Exception | None = None
        attempts = self._config.max_retries + 1

        for attempt in range(attempts):
            try:
                response = self.client.request(
                    method,
                    path,
                    params=params,
                    json=json,
                    content=data,
                    headers=headers,
                )
                return self._handle_response(response)
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout) as exc:
                last_exc = exc
                if attempt < attempts - 1:
                    time.sleep(min(2**attempt * 0.5, 8.0))
                    continue
            except EssabuError:
                raise
            except Exception as exc:
                last_exc = exc
                break

        raise EssabuError(f"Request failed after {attempts} attempts: {last_exc}")

    # -- Convenience methods --------------------------------------------------

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.request("GET", path, params=params)

    def post(self, path: str, *, json: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.request("POST", path, json=json)

    def put(self, path: str, *, json: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.request("PUT", path, json=json)

    def patch(self, path: str, *, json: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.request("PATCH", path, json=json)

    def delete(self, path: str, *, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.request("DELETE", path, params=params)

    # -- Pagination helper ----------------------------------------------------

    def get_paginated(self, path: str, *, params: dict[str, Any] | None = None) -> PageResponse:
        """Fetch a single page and return a PageResponse."""
        body = self.get(path, params=params)
        return PageResponse.from_response(body)

    def iter_pages(
        self,
        path: str,
        *,
        page_size: int = 25,
        params: dict[str, Any] | None = None,
    ) -> Generator[PageResponse, None, None]:
        """Iterate over all pages for a given endpoint."""
        page_params = PageRequest(page=1, page_size=page_size).to_params()
        if params:
            page_params.update(params)

        while True:
            page_resp = self.get_paginated(path, params=page_params)
            yield page_resp
            if not page_resp.has_next:
                break
            page_params["page"] = page_resp.page + 1

    # -- Response handling ----------------------------------------------------

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Parse response, raising mapped exceptions for error status codes."""
        if response.status_code == 204:
            return {}

        try:
            body = response.json()
        except Exception:
            body = {"detail": response.text}

        if response.is_success:
            return body

        status = response.status_code
        message = body.get("message", body.get("detail", f"HTTP {status} error"))
        headers = dict(response.headers)

        # Rate limit
        if status == 429:
            retry_after = response.headers.get("Retry-After")
            raise RateLimitError(
                message=message,
                retry_after=float(retry_after) if retry_after else None,
                body=body,
                headers=headers,
            )

        # Validation errors
        if status == 422:
            errors = body.get("errors", body.get("violations", []))
            raise ValidationError(message=message, errors=errors, body=body, headers=headers)

        # Server errors (retry upstream already handled)
        if status >= 500:
            raise ServerError(message=message, status_code=status, body=body, headers=headers)

        # Mapped client errors
        exc_cls = _STATUS_MAP.get(status, EssabuError)
        raise exc_cls(message=message, body=body, headers=headers)
