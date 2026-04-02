"""Tasks API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.task import Task
from essabu.project.models.pagination import PaginatedResponse


class TasksApi(BaseApi):
    """API operations for tasks."""

    def list(
        self, project_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List tasks for a project."""
        data = self._http.get(f"/projects/{project_id}/tasks", params=params)
        return PaginatedResponse(**data)

    def get(self, project_id: str, task_id: str) -> Task:
        """Get a task by ID."""
        data = self._http.get(f"/projects/{project_id}/tasks/{task_id}")
        return Task(**data)

    def create(self, project_id: str, payload: dict[str, Any]) -> Task:
        """Create a new task."""
        data = self._http.post(f"/projects/{project_id}/tasks", data=payload)
        return Task(**data)

    def update(
        self, project_id: str, task_id: str, payload: dict[str, Any]
    ) -> Task:
        """Update a task."""
        data = self._http.patch(
            f"/projects/{project_id}/tasks/{task_id}", data=payload
        )
        return Task(**data)

    def delete(self, project_id: str, task_id: str) -> None:
        """Delete a task."""
        self._http.delete(f"/projects/{project_id}/tasks/{task_id}")
