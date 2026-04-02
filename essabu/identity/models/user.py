"""User models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool = True
    created_at: str | None = None
    updated_at: str | None = None
