"""Company models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Company:
    id: str
    name: str
    tax_id: str | None = None
    address: str | None = None
    phone: str | None = None
    email: str | None = None
