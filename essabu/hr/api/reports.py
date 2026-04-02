"""API for reports in the hr module."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseHrApi


class ReportApi(BaseHrApi):
    """Operations for reports."""

    def headcount(self, **params: Any) -> dict[str, Any]:
        """Get headcount report."""
        return self._http.get(self._path("reports", "headcount"), params=params or None)

    def turnover(self, **params: Any) -> dict[str, Any]:
        """Get turnover report."""
        return self._http.get(self._path("reports", "turnover"), params=params or None)

    def payroll_summary(self, **params: Any) -> dict[str, Any]:
        """Get payroll summary report."""
        return self._http.get(self._path("reports", "payroll-summary"), params=params or None)

    def leave_balance(self, **params: Any) -> dict[str, Any]:
        """Get leave balance report."""
        return self._http.get(self._path("reports", "leave-balance"), params=params or None)

    def attendance_summary(self, **params: Any) -> dict[str, Any]:
        """Get attendance summary report."""
        return self._http.get(self._path("reports", "attendance-summary"), params=params or None)
