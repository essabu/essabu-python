"""API for leaves in the hr module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class LeaveApi(BaseHrApi):
    """CRUD operations for leaves."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List leaves with pagination."""
        return self._list(self._path("leaves"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of leaves."""
        return self._list_all(self._path("leaves"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new leave."""
        return self._create(self._path("leaves"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a leave by ID."""
        return self._retrieve(self._path("leaves", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a leave."""
        return self._update(self._path("leaves", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a leave."""
        return self._delete(self._path("leaves", resource_id))
