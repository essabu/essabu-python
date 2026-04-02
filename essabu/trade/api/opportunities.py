"""API for opportunities in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class OpportunityApi(BaseTradeApi):
    """CRUD operations for opportunities."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List opportunities with pagination."""
        return self._list(self._path("opportunities"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of opportunities."""
        return self._list_all(self._path("opportunities"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new opportunity."""
        return self._create(self._path("opportunities"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a opportunity by ID."""
        return self._retrieve(self._path("opportunities", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a opportunity."""
        return self._update(self._path("opportunities", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a opportunity."""
        return self._delete(self._path("opportunities", resource_id))
