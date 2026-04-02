"""API client for managing report resources."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/reports"


class ReportApi(BaseApi):
    """Report management operations.

    Base path: /api/hr/reports
    """

    def headcount(self, group_by: str) -> dict[str, Any]:
        """Get headcount report grouped by the specified field."""
        return self._http.get(f"{_BASE_PATH}/headcount?groupBy={group_by}")

    def turnover(self, year: int) -> dict[str, Any]:
        """Get turnover report for a given year."""
        return self._http.get(f"{_BASE_PATH}/turnover?year={year}")

    def absenteeism(self, month: str) -> dict[str, Any]:
        """Get absenteeism report for a given month."""
        return self._http.get(f"{_BASE_PATH}/absenteeism?month={month}")

    def payroll_cost(self, year: int) -> dict[str, Any]:
        """Get payroll cost report for a given year."""
        return self._http.get(f"{_BASE_PATH}/payroll-cost?year={year}")

    def age_pyramid(self) -> dict[str, Any]:
        """Get the age pyramid report."""
        return self._http.get(f"{_BASE_PATH}/age-pyramid")

    def leave_usage(self) -> dict[str, Any]:
        """Get the leave usage report."""
        return self._http.get(f"{_BASE_PATH}/leave-usage")

    def training_compliance(self) -> dict[str, Any]:
        """Get the training compliance report."""
        return self._http.get(f"{_BASE_PATH}/training-compliance")

    def dashboard(self) -> dict[str, Any]:
        """Get the HR dashboard summary."""
        return self._http.get(f"{_BASE_PATH}/dashboard")
