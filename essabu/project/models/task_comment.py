"""Task comment model."""

from __future__ import annotations

from pydantic import BaseModel


class TaskComment(BaseModel):
    """Represents a comment on a task."""

    id: str
    task_id: str
    author_id: str | None = None
    content: str
    created_at: str | None = None
    updated_at: str | None = None
