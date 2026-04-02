"""API for stock movements in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class StockMovementApi(BaseAccountingApi):
    """CRUD operations for stock movements."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List stock movements with pagination."""
        return self._list(self._path("stock_movements"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of stock movements."""
        return self._list_all(self._path("stock_movements"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new stock movement."""
        return self._create(self._path("stock_movements"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a stock movement by ID."""
        return self._retrieve(self._path("stock_movements", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a stock movement."""
        return self._update(self._path("stock_movements", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a stock movement."""
        return self._delete(self._path("stock_movements", resource_id))
