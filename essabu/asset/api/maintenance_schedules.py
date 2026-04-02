"""Maintenance Schedules API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.maintenance_schedule import MaintenanceSchedule
from essabu.asset.models.pagination import PaginatedResponse


class MaintenanceSchedulesApi(BaseApi):
    """API operations for maintenance schedules."""

    def list(
        self, asset_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List maintenance schedules for an asset."""
        data = self._http.get(
            f"/assets/{asset_id}/maintenance-schedules", params=params
        )
        return PaginatedResponse(**data)

    def get(self, asset_id: str, schedule_id: str) -> MaintenanceSchedule:
        """Get a maintenance schedule by ID."""
        data = self._http.get(
            f"/assets/{asset_id}/maintenance-schedules/{schedule_id}"
        )
        return MaintenanceSchedule(**data)

    def create(
        self, asset_id: str, payload: dict[str, Any]
    ) -> MaintenanceSchedule:
        """Create a new maintenance schedule."""
        data = self._http.post(
            f"/assets/{asset_id}/maintenance-schedules", data=payload
        )
        return MaintenanceSchedule(**data)

    def update(
        self, asset_id: str, schedule_id: str, payload: dict[str, Any]
    ) -> MaintenanceSchedule:
        """Update a maintenance schedule."""
        data = self._http.patch(
            f"/assets/{asset_id}/maintenance-schedules/{schedule_id}", data=payload
        )
        return MaintenanceSchedule(**data)

    def delete(self, asset_id: str, schedule_id: str) -> None:
        """Delete a maintenance schedule."""
        self._http.delete(
            f"/assets/{asset_id}/maintenance-schedules/{schedule_id}"
        )
