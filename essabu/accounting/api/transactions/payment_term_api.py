"""API for payment terms in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class PaymentTermApi(BaseAccountingApi):
    """CRUD operations for payment terms."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List payment terms with pagination."""
        return self._list(self._path("payment_terms"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of payment terms."""
        return self._list_all(self._path("payment_terms"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new payment term."""
        return self._create(self._path("payment_terms"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a payment term by ID."""
        return self._retrieve(self._path("payment_terms", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a payment term."""
        return self._update(self._path("payment_terms", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a payment term."""
        return self._delete(self._path("payment_terms", resource_id))
