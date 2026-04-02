"""API for shift schedules in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class ShiftScheduleApi(BaseHrApi):
    """CRUD operations for shift schedules."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List shift schedules with pagination."""
        return self._list(self._path("shift_schedules"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of shift schedules."""
        return self._list_all(self._path("shift_schedules"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new shift schedule."""
        return self._create(self._path("shift_schedules"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a shift schedule by ID."""
        return self._retrieve(self._path("shift_schedules", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a shift schedule."""
        return self._update(self._path("shift_schedules", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a shift schedule."""
        return self._delete(self._path("shift_schedules", resource_id))
