"""API client for managing timesheet resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/timesheets"


class TimesheetApi(BaseApi):
    """Timesheet management operations.

    Base path: /api/hr/timesheets
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new timesheet."""
        return self._http.post(_BASE_PATH, request)

    def get(self, timesheet_id: str) -> dict[str, Any]:
        """Retrieve a timesheet by ID."""
        return self._http.get(f"{_BASE_PATH}/{timesheet_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List timesheets with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def submit(self, timesheet_id: str) -> dict[str, Any]:
        """Submit a timesheet."""
        return self._http.put(f"{_BASE_PATH}/{timesheet_id}/submit")

    def approve(self, timesheet_id: str, approved_by: str) -> dict[str, Any]:
        """Approve a timesheet."""
        return self._http.put(
            f"{_BASE_PATH}/{timesheet_id}/approve",
            {"approvedBy": approved_by},
        )
