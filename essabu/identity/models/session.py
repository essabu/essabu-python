"""Session models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Session:
    id: str
    user_id: str
    ip_address: str | None = None
    user_agent: str | None = None
    expires_at: str | None = None
    created_at: str | None = None
