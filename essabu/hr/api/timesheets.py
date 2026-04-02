"""API for timesheets in the hr module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class TimesheetApi(BaseHrApi):
    """CRUD operations for timesheets."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List timesheets with pagination."""
        return self._list(self._path("timesheets"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of timesheets."""
        return self._list_all(self._path("timesheets"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new timesheet."""
        return self._create(self._path("timesheets"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a timesheet by ID."""
        return self._retrieve(self._path("timesheets", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a timesheet."""
        return self._update(self._path("timesheets", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a timesheet."""
        return self._delete(self._path("timesheets", resource_id))
