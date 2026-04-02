"""Trip Logs API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.trip_log import TripLog
from essabu.asset.models.pagination import PaginatedResponse


class TripLogsApi(BaseApi):
    """API operations for trip logs."""

    def list(
        self, vehicle_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List trip logs for a vehicle."""
        data = self._http.get(f"/vehicles/{vehicle_id}/trip-logs", params=params)
        return PaginatedResponse(**data)

    def get(self, vehicle_id: str, trip_log_id: str) -> TripLog:
        """Get a trip log by ID."""
        data = self._http.get(f"/vehicles/{vehicle_id}/trip-logs/{trip_log_id}")
        return TripLog(**data)

    def create(self, vehicle_id: str, payload: dict[str, Any]) -> TripLog:
        """Create a new trip log entry."""
        data = self._http.post(f"/vehicles/{vehicle_id}/trip-logs", data=payload)
        return TripLog(**data)

    def update(
        self, vehicle_id: str, trip_log_id: str, payload: dict[str, Any]
    ) -> TripLog:
        """Update a trip log entry."""
        data = self._http.patch(
            f"/vehicles/{vehicle_id}/trip-logs/{trip_log_id}", data=payload
        )
        return TripLog(**data)

    def delete(self, vehicle_id: str, trip_log_id: str) -> None:
        """Delete a trip log entry."""
        self._http.delete(f"/vehicles/{vehicle_id}/trip-logs/{trip_log_id}")
