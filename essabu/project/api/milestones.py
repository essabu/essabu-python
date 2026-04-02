"""Milestones API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.milestone import Milestone
from essabu.project.models.pagination import PaginatedResponse


class MilestonesApi(BaseApi):
    """API operations for milestones."""

    def list(
        self, project_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List milestones for a project."""
        data = self._http.get(f"/projects/{project_id}/milestones", params=params)
        return PaginatedResponse(**data)

    def get(self, project_id: str, milestone_id: str) -> Milestone:
        """Get a milestone by ID."""
        data = self._http.get(f"/projects/{project_id}/milestones/{milestone_id}")
        return Milestone(**data)

    def create(self, project_id: str, payload: dict[str, Any]) -> Milestone:
        """Create a new milestone."""
        data = self._http.post(f"/projects/{project_id}/milestones", data=payload)
        return Milestone(**data)

    def update(
        self, project_id: str, milestone_id: str, payload: dict[str, Any]
    ) -> Milestone:
        """Update a milestone."""
        data = self._http.patch(
            f"/projects/{project_id}/milestones/{milestone_id}", data=payload
        )
        return Milestone(**data)

    def delete(self, project_id: str, milestone_id: str) -> None:
        """Delete a milestone."""
        self._http.delete(f"/projects/{project_id}/milestones/{milestone_id}")
