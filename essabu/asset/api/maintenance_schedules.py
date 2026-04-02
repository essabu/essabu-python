"""API for maintenance schedules in the asset module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.asset.api.base import BaseAssetApi


class MaintenanceScheduleApi(BaseAssetApi):
    """CRUD operations for maintenance schedules."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List maintenance schedules with pagination."""
        return self._list(self._path("maintenance_schedules"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of maintenance schedules."""
        return self._list_all(self._path("maintenance_schedules"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new maintenance schedule."""
        return self._create(self._path("maintenance_schedules"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a maintenance schedule by ID."""
        return self._retrieve(self._path("maintenance_schedules", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a maintenance schedule."""
        return self._update(self._path("maintenance_schedules", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a maintenance schedule."""
        return self._delete(self._path("maintenance_schedules", resource_id))
