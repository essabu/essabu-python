"""Branch models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Branch:
    id: str
    name: str
    code: str | None = None
    address: str | None = None
    tenant_id: str | None = None
