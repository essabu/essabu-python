"""Trip log model."""

from __future__ import annotations

from pydantic import BaseModel


class TripLog(BaseModel):
    """Represents a trip log entry for a vehicle."""

    id: str
    vehicle_id: str
    driver_id: str | None = None
    purpose: str | None = None
    start_location: str | None = None
    end_location: str | None = None
    start_mileage: float | None = None
    end_mileage: float | None = None
    distance: float | None = None
    start_time: str | None = None
    end_time: str | None = None
    status: str | None = None
    status_label: str | None = None
    status_color: str | None = None
    notes: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
