"""API client for managing shift schedule resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/shift-schedules"


class ShiftScheduleApi(BaseApi):
    """Shift schedule management operations.

    Base path: /api/hr/shift-schedules
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new shift schedule."""
        return self._http.post(_BASE_PATH, request)

    def get(self, schedule_id: str) -> dict[str, Any]:
        """Retrieve a shift schedule by ID."""
        return self._http.get(f"{_BASE_PATH}/{schedule_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List shift schedules with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def approve(self, schedule_id: str, approved_by: str) -> dict[str, Any]:
        """Approve a shift schedule."""
        return self._http.put(
            f"{_BASE_PATH}/{schedule_id}/approve",
            {"approvedBy": approved_by},
        )

    def publish(self, schedule_id: str) -> dict[str, Any]:
        """Publish a shift schedule."""
        return self._http.put(f"{_BASE_PATH}/{schedule_id}/publish")

    def request_swap(self, request: dict[str, Any]) -> dict[str, Any]:
        """Request a shift swap."""
        return self._http.post("/api/hr/shift-swap-requests", request)

    def approve_swap(self, swap_id: str) -> dict[str, Any]:
        """Approve a shift swap request."""
        return self._http.put(f"/api/hr/shift-swap-requests/{swap_id}/approve")
