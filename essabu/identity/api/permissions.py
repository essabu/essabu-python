"""API for permissions in the identity module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class PermissionApi(BaseIdentityApi):
    """CRUD operations for permissions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List permissions with pagination."""
        return self._list(self._path("permissions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of permissions."""
        return self._list_all(self._path("permissions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new permission."""
        return self._create(self._path("permissions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a permission by ID."""
        return self._retrieve(self._path("permissions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a permission."""
        return self._update(self._path("permissions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a permission."""
        return self._delete(self._path("permissions", resource_id))
