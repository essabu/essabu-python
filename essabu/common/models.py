"""Common models for pagination and shared data structures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PageRequest:
    """Pagination request parameters."""

    page: int = 1
    page_size: int = 25

    def to_params(self) -> dict[str, int]:
        return {"page": self.page, "pageSize": self.page_size}


@dataclass
class PageResponse:
    """Paginated API response."""

    data: list[dict[str, Any]] = field(default_factory=list)
    total: int = 0
    page: int = 1
    page_size: int = 25
    total_pages: int = 0

    @classmethod
    def from_response(cls, body: dict[str, Any]) -> PageResponse:
        """Build a PageResponse from a raw API response body."""
        data = body.get("data", body.get("items", []))
        total = body.get("total", body.get("totalItems", len(data)))
        page = body.get("page", body.get("currentPage", 1))
        page_size = body.get("pageSize", body.get("itemsPerPage", 25))
        total_pages = body.get("totalPages", 0)
        if total_pages == 0 and page_size > 0:
            total_pages = (total + page_size - 1) // page_size
        return cls(data=data, total=total, page=page, page_size=page_size, total_pages=total_pages)

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 1
