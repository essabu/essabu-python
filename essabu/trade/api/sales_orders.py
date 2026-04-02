"""API for sales orders in the trade module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class SalesOrderApi(BaseTradeApi):
    """CRUD operations for sales orders."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List sales orders with pagination."""
        return self._list(self._path("sales_orders"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of sales orders."""
        return self._list_all(self._path("sales_orders"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new sales order."""
        return self._create(self._path("sales_orders"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a sales order by ID."""
        return self._retrieve(self._path("sales_orders", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a sales order."""
        return self._update(self._path("sales_orders", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a sales order."""
        return self._delete(self._path("sales_orders", resource_id))
