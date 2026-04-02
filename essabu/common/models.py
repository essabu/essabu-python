"""Common models shared across all Essabu SDK modules."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class PageRequest:
    """Pagination parameters for list operations.

    Attributes:
        page: Zero-based page number (default 0).
        size: Number of items per page (default 20).
        sort: Field name to sort by (optional).
        direction: Sort direction, "asc" or "desc" (optional).
    """

    page: int = 0
    size: int = 20
    sort: str | None = None
    direction: str | None = None

    @staticmethod
    def of(page: int, size: int) -> PageRequest:
        """Create a PageRequest for a specific page and size."""
        return PageRequest(page=page, size=size)

    @staticmethod
    def first() -> PageRequest:
        """Create a default PageRequest (page 0, size 20)."""
        return PageRequest()

    def to_query_string(self) -> str:
        """Serialize to URL query string fragment."""
        parts = [f"page={self.page}", f"size={self.size}"]
        if self.sort:
            sort_part = self.sort
            if self.direction:
                sort_part += f",{self.direction}"
            parts.append(f"sort={sort_part}")
        return "&".join(parts)


@dataclass
class PageResponse:
    """Generic paginated response wrapper.

    Attributes:
        content: List of items in the current page.
        page: Current page number (zero-based).
        size: Number of items per page.
        total_elements: Total number of items across all pages.
        total_pages: Total number of pages.
        first: Whether this is the first page.
        last: Whether this is the last page.
    """

    content: list[Any] = field(default_factory=list)
    page: int = 0
    size: int = 20
    total_elements: int = 0
    total_pages: int = 0
    first: bool = True
    last: bool = True

    @staticmethod
    def from_dict(data: dict[str, Any]) -> PageResponse:
        """Build a PageResponse from an API JSON dictionary."""
        return PageResponse(
            content=data.get("content", []),
            page=data.get("page", 0),
            size=data.get("size", 20),
            total_elements=data.get("totalElements", 0),
            total_pages=data.get("totalPages", 0),
            first=data.get("first", True),
            last=data.get("last", True),
        )

    @property
    def has_content(self) -> bool:
        """Return True if the page contains at least one item."""
        return len(self.content) > 0

    @property
    def has_next(self) -> bool:
        """Return True if there are more pages after this one."""
        return not self.last

    @property
    def has_previous(self) -> bool:
        """Return True if there are pages before this one."""
        return not self.first
