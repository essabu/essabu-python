"""API for warehouses in the trade module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class WarehouseApi(BaseTradeApi):
    """CRUD operations for warehouses."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List warehouses with pagination."""
        return self._list(self._path("warehouses"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of warehouses."""
        return self._list_all(self._path("warehouses"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new warehouse."""
        return self._create(self._path("warehouses"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a warehouse by ID."""
        return self._retrieve(self._path("warehouses", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a warehouse."""
        return self._update(self._path("warehouses", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a warehouse."""
        return self._delete(self._path("warehouses", resource_id))
