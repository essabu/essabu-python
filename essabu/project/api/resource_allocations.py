"""Resource Allocations API."""

from __future__ import annotations

from typing import Any

from essabu.project.api.base import BaseApi
from essabu.project.models.resource_allocation import ResourceAllocation
from essabu.project.models.pagination import PaginatedResponse


class ResourceAllocationsApi(BaseApi):
    """API operations for resource allocations."""

    def list(
        self, project_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List resource allocations for a project."""
        data = self._http.get(
            f"/projects/{project_id}/resource-allocations", params=params
        )
        return PaginatedResponse(**data)

    def get(self, project_id: str, allocation_id: str) -> ResourceAllocation:
        """Get a resource allocation by ID."""
        data = self._http.get(
            f"/projects/{project_id}/resource-allocations/{allocation_id}"
        )
        return ResourceAllocation(**data)

    def create(
        self, project_id: str, payload: dict[str, Any]
    ) -> ResourceAllocation:
        """Create a new resource allocation."""
        data = self._http.post(
            f"/projects/{project_id}/resource-allocations", data=payload
        )
        return ResourceAllocation(**data)

    def update(
        self, project_id: str, allocation_id: str, payload: dict[str, Any]
    ) -> ResourceAllocation:
        """Update a resource allocation."""
        data = self._http.patch(
            f"/projects/{project_id}/resource-allocations/{allocation_id}",
            data=payload,
        )
        return ResourceAllocation(**data)

    def delete(self, project_id: str, allocation_id: str) -> None:
        """Delete a resource allocation."""
        self._http.delete(
            f"/projects/{project_id}/resource-allocations/{allocation_id}"
        )
