"""API for customers in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class CustomerApi(BaseTradeApi):
    """CRUD operations for customers."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List customers with pagination."""
        return self._list(self._path("customers"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of customers."""
        return self._list_all(self._path("customers"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new customer."""
        return self._create(self._path("customers"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a customer by ID."""
        return self._retrieve(self._path("customers", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a customer."""
        return self._update(self._path("customers", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a customer."""
        return self._delete(self._path("customers", resource_id))
