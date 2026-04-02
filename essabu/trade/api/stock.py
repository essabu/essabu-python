"""API for stock in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class StockApi(BaseTradeApi):
    """CRUD operations for stock."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List stock with pagination."""
        return self._list(self._path("stock"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of stock."""
        return self._list_all(self._path("stock"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new stock."""
        return self._create(self._path("stock"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a stock by ID."""
        return self._retrieve(self._path("stock", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a stock."""
        return self._update(self._path("stock", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a stock."""
        return self._delete(self._path("stock", resource_id))
