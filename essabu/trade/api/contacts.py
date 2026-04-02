"""API for contacts in the trade module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class ContactApi(BaseTradeApi):
    """CRUD operations for contacts."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List contacts with pagination."""
        return self._list(self._path("contacts"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of contacts."""
        return self._list_all(self._path("contacts"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new contact."""
        return self._create(self._path("contacts"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a contact by ID."""
        return self._retrieve(self._path("contacts", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a contact."""
        return self._update(self._path("contacts", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a contact."""
        return self._delete(self._path("contacts", resource_id))
