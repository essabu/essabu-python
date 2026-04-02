"""Project model."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Project(BaseModel):
    """Represents a project."""

    id: str
    name: str
    description: str | None = None
    status: str
    status_label: str | None = None
    status_color: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    budget: float | None = None
    progress: float | None = None
    owner_id: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
