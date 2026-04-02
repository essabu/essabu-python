"""API client for managing disciplinary resources."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/disciplinary-actions"


class DisciplinaryApi(BaseApi):
    """Disciplinary management operations.

    Base path: /api/hr/disciplinary-actions
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new disciplinary action."""
        return self._http.post(_BASE_PATH, request)

    def get(self, action_id: str) -> dict[str, Any]:
        """Retrieve a disciplinary action by ID."""
        return self._http.get(f"{_BASE_PATH}/{action_id}")

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List disciplinary actions for a specific employee."""
        return self._http.get(f"{_BASE_PATH}?employeeId={employee_id}")

    def revoke(self, action_id: str) -> dict[str, Any]:
        """Revoke a disciplinary action."""
        return self._http.put(f"{_BASE_PATH}/{action_id}/revoke")
