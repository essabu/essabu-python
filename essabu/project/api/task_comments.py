"""Task Comments API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.task_comment import TaskComment
from essabu.project.models.pagination import PaginatedResponse


class TaskCommentsApi(BaseApi):
    """API operations for task comments."""

    def list(
        self, task_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List comments for a task."""
        data = self._http.get(f"/tasks/{task_id}/comments", params=params)
        return PaginatedResponse(**data)

    def get(self, task_id: str, comment_id: str) -> TaskComment:
        """Get a comment by ID."""
        data = self._http.get(f"/tasks/{task_id}/comments/{comment_id}")
        return TaskComment(**data)

    def create(self, task_id: str, payload: dict[str, Any]) -> TaskComment:
        """Create a new comment on a task."""
        data = self._http.post(f"/tasks/{task_id}/comments", data=payload)
        return TaskComment(**data)

    def update(
        self, task_id: str, comment_id: str, payload: dict[str, Any]
    ) -> TaskComment:
        """Update a comment."""
        data = self._http.patch(
            f"/tasks/{task_id}/comments/{comment_id}", data=payload
        )
        return TaskComment(**data)

    def delete(self, task_id: str, comment_id: str) -> None:
        """Delete a comment."""
        self._http.delete(f"/tasks/{task_id}/comments/{comment_id}")
