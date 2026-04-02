"""API for performance in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class PerformanceApi(BaseHrApi):
    """CRUD operations for performance."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List performance with pagination."""
        return self._list(self._path("performance"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of performance."""
        return self._list_all(self._path("performance"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new performance."""
        return self._create(self._path("performance"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a performance by ID."""
        return self._retrieve(self._path("performance", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a performance."""
        return self._update(self._path("performance", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a performance."""
        return self._delete(self._path("performance", resource_id))
