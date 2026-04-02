"""Reports API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.report import Report
from essabu.project.models.pagination import PaginatedResponse


class ReportsApi(BaseApi):
    """API operations for project reports."""

    def list(
        self, project_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List reports for a project."""
        data = self._http.get(f"/projects/{project_id}/reports", params=params)
        return PaginatedResponse(**data)

    def get(self, project_id: str, report_id: str) -> Report:
        """Get a report by ID."""
        data = self._http.get(f"/projects/{project_id}/reports/{report_id}")
        return Report(**data)

    def create(self, project_id: str, payload: dict[str, Any]) -> Report:
        """Generate a new report."""
        data = self._http.post(f"/projects/{project_id}/reports", data=payload)
        return Report(**data)

    def delete(self, project_id: str, report_id: str) -> None:
        """Delete a report."""
        self._http.delete(f"/projects/{project_id}/reports/{report_id}")
