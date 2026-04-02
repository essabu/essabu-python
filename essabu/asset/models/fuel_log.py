"""Fuel log model."""

from __future__ import annotations

from pydantic import BaseModel


class FuelLog(BaseModel):
    """Represents a fuel log entry for a vehicle."""

    id: str
    vehicle_id: str
    date: str | None = None
    quantity_liters: float | None = None
    cost_per_liter: float | None = None
    total_cost: float | None = None
    mileage_at_fill: float | None = None
    fuel_type: str | None = None
    station: str | None = None
    filled_by: str | None = None
    notes: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
