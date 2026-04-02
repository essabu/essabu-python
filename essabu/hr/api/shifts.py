"""API client for managing shift resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/shifts"


class ShiftApi(BaseApi):
    """Shift management operations.

    Base path: /api/hr/shifts
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new shift."""
        return self._http.post(_BASE_PATH, request)

    def get(self, shift_id: str) -> dict[str, Any]:
        """Retrieve a shift by ID."""
        return self._http.get(f"{_BASE_PATH}/{shift_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List shifts with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def update(self, shift_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing shift."""
        return self._http.put(f"{_BASE_PATH}/{shift_id}", request)

    def delete(self, shift_id: str) -> None:
        """Delete a shift."""
        self._http.delete(f"{_BASE_PATH}/{shift_id}")

    def get_my_week(self, employee_id: str, week: str) -> list[dict[str, Any]]:
        """Get shifts for an employee for a given week."""
        return self._http.get(
            f"{_BASE_PATH}/my-week?employeeId={employee_id}&week={week}"
        )
