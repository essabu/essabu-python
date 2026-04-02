"""Profile models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Profile:
    id: str
    user_id: str
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    avatar_url: str | None = None
