"""Depreciation model."""

from __future__ import annotations

from pydantic import BaseModel


class Depreciation(BaseModel):
    """Represents an asset depreciation record."""

    id: str
    asset_id: str
    method: str | None = None
    useful_life_years: int | None = None
    residual_value: float | None = None
    annual_rate: float | None = None
    period_start: str | None = None
    period_end: str | None = None
    depreciation_amount: float | None = None
    accumulated_depreciation: float | None = None
    book_value: float | None = None
    created_at: str | None = None
    updated_at: str | None = None
