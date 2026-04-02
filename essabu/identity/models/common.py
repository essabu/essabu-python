"""Common identity models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TimestampMixin:
    """Common timestamp fields."""
    created_at: str | None = None
    updated_at: str | None = None
