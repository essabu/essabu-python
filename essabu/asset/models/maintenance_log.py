"""Maintenance log model."""

from __future__ import annotations

from pydantic import BaseModel


class MaintenanceLog(BaseModel):
    """Represents a maintenance log entry for an asset."""

    id: str
    asset_id: str
    schedule_id: str | None = None
    title: str | None = None
    description: str | None = None
    performed_by: str | None = None
    performed_at: str | None = None
    cost: float | None = None
    notes: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
