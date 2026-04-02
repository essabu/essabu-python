"""Pagination model."""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated API response."""

    data: list[Any]
    total: int
    page: int
    per_page: int
    last_page: int
