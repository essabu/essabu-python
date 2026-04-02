"""Common models shared across modules."""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginationParams(BaseModel):
    page: int = 1
    per_page: int = 25


class PaginatedResponse(BaseModel, Generic[T]):
    data: list[Any]
    total: int
    page: int
    per_page: int
    total_pages: int
