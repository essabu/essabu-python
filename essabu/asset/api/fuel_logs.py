"""Fuel Logs API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.fuel_log import FuelLog
from essabu.asset.models.pagination import PaginatedResponse


class FuelLogsApi(BaseApi):
    """API operations for fuel logs."""

    def list(
        self, vehicle_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List fuel logs for a vehicle."""
        data = self._http.get(f"/vehicles/{vehicle_id}/fuel-logs", params=params)
        return PaginatedResponse(**data)

    def get(self, vehicle_id: str, fuel_log_id: str) -> FuelLog:
        """Get a fuel log by ID."""
        data = self._http.get(f"/vehicles/{vehicle_id}/fuel-logs/{fuel_log_id}")
        return FuelLog(**data)

    def create(self, vehicle_id: str, payload: dict[str, Any]) -> FuelLog:
        """Create a new fuel log entry."""
        data = self._http.post(f"/vehicles/{vehicle_id}/fuel-logs", data=payload)
        return FuelLog(**data)

    def update(
        self, vehicle_id: str, fuel_log_id: str, payload: dict[str, Any]
    ) -> FuelLog:
        """Update a fuel log entry."""
        data = self._http.patch(
            f"/vehicles/{vehicle_id}/fuel-logs/{fuel_log_id}", data=payload
        )
        return FuelLog(**data)

    def delete(self, vehicle_id: str, fuel_log_id: str) -> None:
        """Delete a fuel log entry."""
        self._http.delete(f"/vehicles/{vehicle_id}/fuel-logs/{fuel_log_id}")
