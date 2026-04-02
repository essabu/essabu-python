"""Statistics models."""

from typing import Any

from pydantic import BaseModel


class StatisticsRequest(BaseModel):
    """Request for statistics."""

    start_date: str | None = None
    end_date: str | None = None
    group_by: str | None = None
    filters: dict[str, Any] | None = None


class StatisticsResponse(BaseModel):
    """Response from statistics endpoint."""

    total_invoices: int
    total_amount: float
    total_tax: float
    submitted_count: int
    accepted_count: int
    rejected_count: int
    pending_count: int
    currency: str
    period_start: str | None = None
    period_end: str | None = None
    breakdown: list[dict[str, Any]] | None = None
