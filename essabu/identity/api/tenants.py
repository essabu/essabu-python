"""API for tenants in the identity module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class TenantApi(BaseIdentityApi):
    """CRUD operations for tenants."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List tenants with pagination."""
        return self._list(self._path("tenants"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of tenants."""
        return self._list_all(self._path("tenants"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new tenant."""
        return self._create(self._path("tenants"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a tenant by ID."""
        return self._retrieve(self._path("tenants", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a tenant."""
        return self._update(self._path("tenants", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a tenant."""
        return self._delete(self._path("tenants", resource_id))
