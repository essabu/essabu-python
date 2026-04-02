"""API client for managing loan resources."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/loans"


class LoanApi(BaseApi):
    """Loan management operations.

    Base path: /api/hr/loans
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new loan."""
        return self._http.post(_BASE_PATH, request)

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List loans for a specific employee."""
        return self._http.get(f"{_BASE_PATH}?employeeId={employee_id}")

    def approve(self, loan_id: str, approved_by: str) -> dict[str, Any]:
        """Approve a loan."""
        return self._http.put(
            f"{_BASE_PATH}/{loan_id}/approve",
            {"approvedBy": approved_by},
        )

    def get_repayments(self, loan_id: str) -> list[dict[str, Any]]:
        """Get repayments for a loan."""
        return self._http.get(f"{_BASE_PATH}/{loan_id}/repayments")

    def add_repayment(self, loan_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Add a repayment to a loan."""
        return self._http.post(f"{_BASE_PATH}/{loan_id}/repayments", request)
