"""API for attendance in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class AttendanceApi(BaseHrApi):
    """CRUD operations for attendance."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List attendance with pagination."""
        return self._list(self._path("attendance"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of attendance."""
        return self._list_all(self._path("attendance"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new attendance."""
        return self._create(self._path("attendance"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a attendance by ID."""
        return self._retrieve(self._path("attendance", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a attendance."""
        return self._update(self._path("attendance", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a attendance."""
        return self._delete(self._path("attendance", resource_id))
