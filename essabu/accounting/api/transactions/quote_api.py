"""API for quotes in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class QuoteApi(BaseAccountingApi):
    """CRUD operations for quotes."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List quotes with pagination."""
        return self._list(self._path("quotes"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of quotes."""
        return self._list_all(self._path("quotes"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new quote."""
        return self._create(self._path("quotes"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a quote by ID."""
        return self._retrieve(self._path("quotes", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a quote."""
        return self._update(self._path("quotes", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a quote."""
        return self._delete(self._path("quotes", resource_id))
