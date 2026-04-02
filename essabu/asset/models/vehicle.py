"""Vehicle model."""

from __future__ import annotations

from pydantic import BaseModel


class Vehicle(BaseModel):
    """Represents a vehicle asset."""

    id: str
    asset_id: str | None = None
    registration_number: str | None = None
    make: str | None = None
    model: str | None = None
    year: int | None = None
    vin: str | None = None
    status: str | None = None
    status_label: str | None = None
    status_color: str | None = None
    mileage: float | None = None
    fuel_type: str | None = None
    assigned_driver: str | None = None
    insurance_expiry: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
