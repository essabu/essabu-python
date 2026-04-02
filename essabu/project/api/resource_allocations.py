"""API for resource allocations in the project module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.project.api.base import BaseProjectApi


class ResourceAllocationApi(BaseProjectApi):
    """CRUD operations for resource allocations."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List resource allocations with pagination."""
        return self._list(self._path("resource_allocations"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of resource allocations."""
        return self._list_all(self._path("resource_allocations"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new resource allocation."""
        return self._create(self._path("resource_allocations"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a resource allocation by ID."""
        return self._retrieve(self._path("resource_allocations", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a resource allocation."""
        return self._update(self._path("resource_allocations", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a resource allocation."""
        return self._delete(self._path("resource_allocations", resource_id))
