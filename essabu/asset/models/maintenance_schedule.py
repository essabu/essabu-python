"""Maintenance schedule model."""

from __future__ import annotations

from pydantic import BaseModel


class MaintenanceSchedule(BaseModel):
    """Represents a scheduled maintenance for an asset."""

    id: str
    asset_id: str
    title: str
    description: str | None = None
    frequency: str | None = None
    status: str | None = None
    status_label: str | None = None
    status_color: str | None = None
    next_due_date: str | None = None
    last_performed_date: str | None = None
    estimated_cost: float | None = None
    assigned_to: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
