"""API client for managing leave resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/leave-requests"


class LeaveApi(BaseApi):
    """Leave management operations.

    Base path: /api/hr/leave-requests
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new leave request."""
        return self._http.post(_BASE_PATH, request)

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List leave requests with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def approve(self, leave_id: str, approved_by: str) -> dict[str, Any]:
        """Approve a leave request."""
        return self._http.put(
            f"{_BASE_PATH}/{leave_id}/approve",
            {"approvedBy": approved_by},
        )

    def reject(self, leave_id: str) -> dict[str, Any]:
        """Reject a leave request."""
        return self._http.put(f"{_BASE_PATH}/{leave_id}/reject")

    def cancel(self, leave_id: str) -> dict[str, Any]:
        """Cancel a leave request."""
        return self._http.put(f"{_BASE_PATH}/{leave_id}/cancel")

    def get_balances(self, employee_id: str) -> list[dict[str, Any]]:
        """Get leave balances for an employee."""
        return self._http.get(
            self._with_param("/api/hr/leave-balances", "employeeId", employee_id)
        )
