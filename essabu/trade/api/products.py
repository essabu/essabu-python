"""API for products in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class ProductApi(BaseTradeApi):
    """CRUD operations for products."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List products with pagination."""
        return self._list(self._path("products"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of products."""
        return self._list_all(self._path("products"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new product."""
        return self._create(self._path("products"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a product by ID."""
        return self._retrieve(self._path("products", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a product."""
        return self._update(self._path("products", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a product."""
        return self._delete(self._path("products", resource_id))
