"""Maintenance Logs API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.maintenance_log import MaintenanceLog
from essabu.asset.models.pagination import PaginatedResponse


class MaintenanceLogsApi(BaseApi):
    """API operations for maintenance logs."""

    def list(
        self, asset_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List maintenance logs for an asset."""
        data = self._http.get(
            f"/assets/{asset_id}/maintenance-logs", params=params
        )
        return PaginatedResponse(**data)

    def get(self, asset_id: str, log_id: str) -> MaintenanceLog:
        """Get a maintenance log by ID."""
        data = self._http.get(f"/assets/{asset_id}/maintenance-logs/{log_id}")
        return MaintenanceLog(**data)

    def create(self, asset_id: str, payload: dict[str, Any]) -> MaintenanceLog:
        """Create a new maintenance log entry."""
        data = self._http.post(
            f"/assets/{asset_id}/maintenance-logs", data=payload
        )
        return MaintenanceLog(**data)

    def update(
        self, asset_id: str, log_id: str, payload: dict[str, Any]
    ) -> MaintenanceLog:
        """Update a maintenance log entry."""
        data = self._http.patch(
            f"/assets/{asset_id}/maintenance-logs/{log_id}", data=payload
        )
        return MaintenanceLog(**data)

    def delete(self, asset_id: str, log_id: str) -> None:
        """Delete a maintenance log entry."""
        self._http.delete(f"/assets/{asset_id}/maintenance-logs/{log_id}")
