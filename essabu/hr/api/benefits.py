"""API client for managing benefit resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_PLANS_PATH = "/api/hr/benefit-plans"
_BENEFITS_PATH = "/api/hr/employee-benefits"


class BenefitApi(BaseApi):
    """Benefit management operations."""

    # --- Plans ---

    def create_plan(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new benefit plan."""
        return self._http.post(_PLANS_PATH, request)

    def list_plans(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List benefit plans with pagination."""
        data = self._http.get(self._with_pagination(_PLANS_PATH, page))
        return PageResponse.from_dict(data)

    # --- Employee Benefits ---

    def enroll(self, request: dict[str, Any]) -> dict[str, Any]:
        """Enroll an employee in a benefit plan."""
        return self._http.post(_BENEFITS_PATH, request)

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List benefits for a specific employee."""
        return self._http.get(f"{_BENEFITS_PATH}?employeeId={employee_id}")

    def terminate(self, benefit_id: str) -> dict[str, Any]:
        """Terminate an employee benefit."""
        return self._http.put(f"{_BENEFITS_PATH}/{benefit_id}/terminate")
