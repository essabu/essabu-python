"""API client for managing department resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/departments"


class DepartmentApi(BaseApi):
    """Department management operations.

    Base path: /api/hr/departments
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new department."""
        return self._http.post(_BASE_PATH, request)

    def get(self, department_id: str) -> dict[str, Any]:
        """Retrieve a department by ID."""
        return self._http.get(f"{_BASE_PATH}/{department_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List departments with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def update(self, department_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing department."""
        return self._http.put(f"{_BASE_PATH}/{department_id}", request)

    def delete(self, department_id: str) -> None:
        """Delete a department."""
        self._http.delete(f"{_BASE_PATH}/{department_id}")
