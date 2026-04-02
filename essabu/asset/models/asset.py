"""Asset model."""

from __future__ import annotations

from pydantic import BaseModel


class Asset(BaseModel):
    """Represents an asset."""

    id: str
    name: str
    description: str | None = None
    category: str | None = None
    serial_number: str | None = None
    status: str
    status_label: str | None = None
    status_color: str | None = None
    purchase_date: str | None = None
    purchase_price: float | None = None
    current_value: float | None = None
    location: str | None = None
    assigned_to: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
