"""API for price lists in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class PriceListApi(BaseAccountingApi):
    """CRUD operations for price lists."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List price lists with pagination."""
        return self._list(self._path("price_lists"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of price lists."""
        return self._list_all(self._path("price_lists"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new price list."""
        return self._create(self._path("price_lists"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a price list by ID."""
        return self._retrieve(self._path("price_lists", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a price list."""
        return self._update(self._path("price_lists", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a price list."""
        return self._delete(self._path("price_lists", resource_id))
