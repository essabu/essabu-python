"""Task model."""

from __future__ import annotations

from pydantic import BaseModel


class Task(BaseModel):
    """Represents a project task."""

    id: str
    project_id: str
    milestone_id: str | None = None
    title: str
    description: str | None = None
    status: str
    status_label: str | None = None
    status_color: str | None = None
    priority: str | None = None
    assignee_id: str | None = None
    due_date: str | None = None
    estimated_hours: float | None = None
    actual_hours: float | None = None
    created_at: str | None = None
    updated_at: str | None = None
