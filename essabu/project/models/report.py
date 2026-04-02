"""Report model."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Report(BaseModel):
    """Represents a project report."""

    id: str
    project_id: str
    title: str
    report_type: str | None = None
    status: str | None = None
    status_label: str | None = None
    status_color: str | None = None
    generated_at: str | None = None
    data: dict[str, Any] | None = None
    created_at: str | None = None
    updated_at: str | None = None
