"""API for milestones in the project module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.project.api.base import BaseProjectApi


class MilestoneApi(BaseProjectApi):
    """CRUD operations for milestones."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List milestones with pagination."""
        return self._list(self._path("milestones"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of milestones."""
        return self._list_all(self._path("milestones"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new milestone."""
        return self._create(self._path("milestones"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a milestone by ID."""
        return self._retrieve(self._path("milestones", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a milestone."""
        return self._update(self._path("milestones", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a milestone."""
        return self._delete(self._path("milestones", resource_id))
