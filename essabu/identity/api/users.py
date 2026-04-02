"""API for users in the identity module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class UserApi(BaseIdentityApi):
    """CRUD operations for users."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List users with pagination."""
        return self._list(self._path("users"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of users."""
        return self._list_all(self._path("users"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new user."""
        return self._create(self._path("users"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a user by ID."""
        return self._retrieve(self._path("users", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a user."""
        return self._update(self._path("users", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a user."""
        return self._delete(self._path("users", resource_id))
