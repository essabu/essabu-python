"""Authentication utilities for the Essabu SDK."""

from __future__ import annotations


class AuthInterceptor:
    """Applies authentication headers to every API request.

    Headers added:
    - Authorization: Bearer <api_key>
    - X-Tenant-Id: <tenant_id>  (if provided)
    - Accept: application/json
    """

    def __init__(self, api_key: str, tenant_id: str | None = None) -> None:
        self._api_key = api_key
        self._tenant_id = tenant_id

    def get_headers(self) -> dict[str, str]:
        """Return the authentication headers as a dictionary."""
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Accept": "application/json",
        }
        if self._tenant_id:
            headers["X-Tenant-Id"] = self._tenant_id
        return headers
