"""API for roles in the identity module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class RoleApi(BaseIdentityApi):
    """CRUD operations for roles."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List roles with pagination."""
        return self._list(self._path("roles"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of roles."""
        return self._list_all(self._path("roles"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new role."""
        return self._create(self._path("roles"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a role by ID."""
        return self._retrieve(self._path("roles", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a role."""
        return self._update(self._path("roles", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a role."""
        return self._delete(self._path("roles", resource_id))
