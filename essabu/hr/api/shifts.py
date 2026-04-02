"""API for shifts in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class ShiftApi(BaseHrApi):
    """CRUD operations for shifts."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List shifts with pagination."""
        return self._list(self._path("shifts"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of shifts."""
        return self._list_all(self._path("shifts"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new shift."""
        return self._create(self._path("shifts"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a shift by ID."""
        return self._retrieve(self._path("shifts", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a shift."""
        return self._update(self._path("shifts", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a shift."""
        return self._delete(self._path("shifts", resource_id))
