"""Milestone model."""

from __future__ import annotations

from pydantic import BaseModel


class Milestone(BaseModel):
    """Represents a project milestone."""

    id: str
    project_id: str
    name: str
    description: str | None = None
    status: str
    status_label: str | None = None
    status_color: str | None = None
    due_date: str | None = None
    completed_at: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
