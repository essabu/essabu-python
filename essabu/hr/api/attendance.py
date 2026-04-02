"""API client for managing attendance resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/attendances"


class AttendanceApi(BaseApi):
    """Attendance management operations.

    Base path: /api/hr/attendances
    """

    def record(self, request: dict[str, Any]) -> dict[str, Any]:
        """Record an attendance entry."""
        return self._http.post(_BASE_PATH, request)

    def clock_in(self, request: dict[str, Any]) -> dict[str, Any]:
        """Clock in an employee."""
        return self._http.post(f"{_BASE_PATH}/clock-in", request)

    def clock_out(self, request: dict[str, Any]) -> dict[str, Any]:
        """Clock out an employee."""
        return self._http.post(f"{_BASE_PATH}/clock-out", request)

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List attendance records with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def summary(self, employee_id: str, month: str) -> dict[str, Any]:
        """Get attendance summary for an employee for a given month."""
        path = self._with_param(f"{_BASE_PATH}/summary", "employeeId", employee_id)
        path = self._with_param(path, "month", month)
        return self._http.get(path)
