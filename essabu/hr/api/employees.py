"""API client for managing employee resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/employees"


class EmployeeApi(BaseApi):
    """Employee management operations.

    Base path: /api/hr/employees
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new employee."""
        return self._http.post(_BASE_PATH, request)

    def get(self, employee_id: str) -> dict[str, Any]:
        """Retrieve an employee by ID."""
        return self._http.get(f"{_BASE_PATH}/{employee_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List employees with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def update(self, employee_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing employee."""
        return self._http.put(f"{_BASE_PATH}/{employee_id}", request)

    def delete(self, employee_id: str) -> None:
        """Delete an employee."""
        self._http.delete(f"{_BASE_PATH}/{employee_id}")

    def get_leave_balances(self, employee_id: str) -> list[dict[str, Any]]:
        """Get leave balances for an employee."""
        return self._http.get(f"{_BASE_PATH}/{employee_id}/leave-balance")

    def get_history(self, employee_id: str) -> list[dict[str, Any]]:
        """Get audit history for an employee."""
        return self._http.get(f"{_BASE_PATH}/{employee_id}/history")

    def get_documents(self, employee_id: str) -> list[dict[str, Any]]:
        """Get documents for an employee."""
        return self._http.get(f"{_BASE_PATH}/{employee_id}/documents")

    def get_org_tree(self, employee_id: str) -> list[dict[str, Any]]:
        """Get the organizational tree for an employee."""
        return self._http.get(f"{_BASE_PATH}/{employee_id}/org-tree")

    def get_org_chart(self) -> dict[str, Any]:
        """Get the full organizational chart."""
        return self._http.get(f"{_BASE_PATH}/org-chart")
