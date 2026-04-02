"""API client for managing payroll resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/payrolls"


class PayrollApi(BaseApi):
    """Payroll management operations.

    Base path: /api/hr/payrolls
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new payroll."""
        return self._http.post(_BASE_PATH, request)

    def get(self, payroll_id: str) -> dict[str, Any]:
        """Retrieve a payroll by ID."""
        return self._http.get(f"{_BASE_PATH}/{payroll_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List payrolls with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def calculate(self, payroll_id: str) -> dict[str, Any]:
        """Calculate a payroll."""
        return self._http.put(f"{_BASE_PATH}/{payroll_id}/calculate")

    def approve(self, payroll_id: str, approved_by: str) -> dict[str, Any]:
        """Approve a payroll."""
        return self._http.put(
            f"{_BASE_PATH}/{payroll_id}/approve",
            {"approvedBy": approved_by},
        )

    def download_pdf(self, payroll_id: str) -> bytes:
        """Download the payroll as a PDF."""
        return self._http.get_bytes(f"{_BASE_PATH}/{payroll_id}/pdf")

    def get_payslips(self, payroll_id: str) -> list[dict[str, Any]]:
        """Get payslips for a payroll."""
        return self._http.get(f"{_BASE_PATH}/{payroll_id}/payslips")

    def download_payslip_pdf(self, payroll_id: str, employee_id: str) -> bytes:
        """Download a specific payslip as a PDF."""
        return self._http.get_bytes(
            f"{_BASE_PATH}/{payroll_id}/payslips/{employee_id}/pdf"
        )

    def get_year_to_date(self, employee_id: str, year: int) -> dict[str, Any]:
        """Get year-to-date payroll summary for an employee."""
        path = self._with_param("/api/hr/payroll-ytd", "employeeId", employee_id)
        path = self._with_param(path, "year", year)
        return self._http.get(path)
