"""API for price list overrides in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class PriceListOverrideApi(BaseAccountingApi):
    """CRUD operations for price list overrides."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List price list overrides with pagination."""
        return self._list(self._path("price_list_overrides"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of price list overrides."""
        return self._list_all(self._path("price_list_overrides"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new price list override."""
        return self._create(self._path("price_list_overrides"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a price list override by ID."""
        return self._retrieve(self._path("price_list_overrides", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a price list override."""
        return self._update(self._path("price_list_overrides", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a price list override."""
        return self._delete(self._path("price_list_overrides", resource_id))
