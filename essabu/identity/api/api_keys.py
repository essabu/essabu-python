"""API for api keys in the identity module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class ApiKeyApi(BaseIdentityApi):
    """CRUD operations for api keys."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List api keys with pagination."""
        return self._list(self._path("api_keys"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of api keys."""
        return self._list_all(self._path("api_keys"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new api key."""
        return self._create(self._path("api_keys"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a api key by ID."""
        return self._retrieve(self._path("api_keys", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a api key."""
        return self._update(self._path("api_keys", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a api key."""
        return self._delete(self._path("api_keys", resource_id))
