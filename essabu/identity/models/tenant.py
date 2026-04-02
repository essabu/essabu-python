"""Tenant models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Tenant:
    id: str
    name: str
    slug: str
    is_active: bool = True
