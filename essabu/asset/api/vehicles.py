"""Vehicles API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.vehicle import Vehicle
from essabu.asset.models.pagination import PaginatedResponse


class VehiclesApi(BaseApi):
    """API operations for vehicles."""

    def list(self, params: dict[str, Any] | None = None) -> PaginatedResponse:
        """List all vehicles."""
        data = self._http.get("/vehicles", params=params)
        return PaginatedResponse(**data)

    def get(self, vehicle_id: str) -> Vehicle:
        """Get a vehicle by ID."""
        data = self._http.get(f"/vehicles/{vehicle_id}")
        return Vehicle(**data)

    def create(self, payload: dict[str, Any]) -> Vehicle:
        """Create a new vehicle."""
        data = self._http.post("/vehicles", data=payload)
        return Vehicle(**data)

    def update(self, vehicle_id: str, payload: dict[str, Any]) -> Vehicle:
        """Update a vehicle."""
        data = self._http.patch(f"/vehicles/{vehicle_id}", data=payload)
        return Vehicle(**data)

    def delete(self, vehicle_id: str) -> None:
        """Delete a vehicle."""
        self._http.delete(f"/vehicles/{vehicle_id}")
