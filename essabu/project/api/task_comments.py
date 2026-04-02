"""API for task comments in the project module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.project.api.base import BaseProjectApi


class TaskCommentApi(BaseProjectApi):
    """CRUD operations for task comments."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List task comments with pagination."""
        return self._list(self._path("task_comments"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of task comments."""
        return self._list_all(self._path("task_comments"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new task comment."""
        return self._create(self._path("task_comments"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a task comment by ID."""
        return self._retrieve(self._path("task_comments", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a task comment."""
        return self._update(self._path("task_comments", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a task comment."""
        return self._delete(self._path("task_comments", resource_id))
