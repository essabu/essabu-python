"""API for currencies in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class CurrencyApi(BaseAccountingApi):
    """CRUD operations for currencies."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List currencies with pagination."""
        return self._list(self._path("currencies"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of currencies."""
        return self._list_all(self._path("currencies"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new currency."""
        return self._create(self._path("currencies"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a currency by ID."""
        return self._retrieve(self._path("currencies", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a currency."""
        return self._update(self._path("currencies", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a currency."""
        return self._delete(self._path("currencies", resource_id))
