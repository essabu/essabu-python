"""Role models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Role:
    id: str
    name: str
    description: str | None = None
    permissions: list[str] | None = None
