"""Resource allocation model."""

from __future__ import annotations

from pydantic import BaseModel


class ResourceAllocation(BaseModel):
    """Represents a resource allocation within a project."""

    id: str
    project_id: str
    resource_id: str | None = None
    resource_type: str | None = None
    role: str | None = None
    allocation_percentage: float | None = None
    start_date: str | None = None
    end_date: str | None = None
    hourly_rate: float | None = None
    created_at: str | None = None
    updated_at: str | None = None
