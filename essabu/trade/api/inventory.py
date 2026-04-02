"""API for inventory in the trade module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class InventoryApi(BaseTradeApi):
    """CRUD operations for inventory."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List inventory with pagination."""
        return self._list(self._path("inventory"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of inventory."""
        return self._list_all(self._path("inventory"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new inventory."""
        return self._create(self._path("inventory"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a inventory by ID."""
        return self._retrieve(self._path("inventory", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a inventory."""
        return self._update(self._path("inventory", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a inventory."""
        return self._delete(self._path("inventory", resource_id))
