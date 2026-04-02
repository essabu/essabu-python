"""API for invoices in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class InvoiceApi(BaseAccountingApi):
    """CRUD operations for invoices."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List invoices with pagination."""
        return self._list(self._path("invoices"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of invoices."""
        return self._list_all(self._path("invoices"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new invoice."""
        return self._create(self._path("invoices"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a invoice by ID."""
        return self._retrieve(self._path("invoices", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a invoice."""
        return self._update(self._path("invoices", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a invoice."""
        return self._delete(self._path("invoices", resource_id))
