"""Projects API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.project import Project
from essabu.project.models.pagination import PaginatedResponse


class ProjectsApi(BaseApi):
    """API operations for projects."""

    def list(self, params: dict[str, Any] | None = None) -> PaginatedResponse:
        """List all projects."""
        data = self._http.get("/projects", params=params)
        return PaginatedResponse(**data)

    def get(self, project_id: str) -> Project:
        """Get a project by ID."""
        data = self._http.get(f"/projects/{project_id}")
        return Project(**data)

    def create(self, payload: dict[str, Any]) -> Project:
        """Create a new project."""
        data = self._http.post("/projects", data=payload)
        return Project(**data)

    def update(self, project_id: str, payload: dict[str, Any]) -> Project:
        """Update an existing project."""
        data = self._http.patch(f"/projects/{project_id}", data=payload)
        return Project(**data)

    def delete(self, project_id: str) -> None:
        """Delete a project."""
        self._http.delete(f"/projects/{project_id}")
