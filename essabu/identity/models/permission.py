"""Permission models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Permission:
    id: str
    name: str
    codename: str
    module: str | None = None
