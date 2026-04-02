"""API client for managing skill resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/skills"


class SkillApi(BaseApi):
    """Skill management operations.

    Base path: /api/hr/skills
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new skill."""
        return self._http.post(_BASE_PATH, request)

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List skills with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def add_to_employee(self, request: dict[str, Any]) -> dict[str, Any]:
        """Add a skill to an employee."""
        return self._http.post("/api/hr/employee-skills", request)

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List skills for a specific employee."""
        return self._http.get(f"/api/hr/employee-skills?employeeId={employee_id}")

    def gap_analysis(self, position_id: str, employee_id: str) -> dict[str, Any]:
        """Perform a gap analysis between a position and an employee."""
        return self._http.get(
            f"{_BASE_PATH}/gap-analysis?positionId={position_id}&employeeId={employee_id}"
        )

    def matrix(self, department_id: str) -> dict[str, Any]:
        """Get the skill matrix for a department."""
        return self._http.get(f"{_BASE_PATH}/matrix?departmentId={department_id}")
