"""API for stock counts in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class StockCountApi(BaseAccountingApi):
    """CRUD operations for stock counts."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List stock counts with pagination."""
        return self._list(self._path("stock_counts"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of stock counts."""
        return self._list_all(self._path("stock_counts"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new stock count."""
        return self._create(self._path("stock_counts"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a stock count by ID."""
        return self._retrieve(self._path("stock_counts", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a stock count."""
        return self._update(self._path("stock_counts", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a stock count."""
        return self._delete(self._path("stock_counts", resource_id))
