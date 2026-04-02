"""API client for managing expense resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/expense-reports"


class ExpenseApi(BaseApi):
    """Expense management operations.

    Base path: /api/hr/expense-reports
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new expense report."""
        return self._http.post(_BASE_PATH, request)

    def get(self, expense_id: str) -> dict[str, Any]:
        """Retrieve an expense report by ID."""
        return self._http.get(f"{_BASE_PATH}/{expense_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List expense reports with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def submit(self, expense_id: str) -> dict[str, Any]:
        """Submit an expense report."""
        return self._http.put(f"{_BASE_PATH}/{expense_id}/submit")

    def approve(self, expense_id: str, approved_by: str) -> dict[str, Any]:
        """Approve an expense report."""
        return self._http.put(
            f"{_BASE_PATH}/{expense_id}/approve",
            {"approvedBy": approved_by},
        )

    def reject(self, expense_id: str) -> dict[str, Any]:
        """Reject an expense report."""
        return self._http.put(f"{_BASE_PATH}/{expense_id}/reject")
