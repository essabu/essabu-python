"""API key models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ApiKey:
    id: str
    name: str
    prefix: str
    scopes: list[str] | None = None
    expires_at: str | None = None
    last_used_at: str | None = None
    created_at: str | None = None
