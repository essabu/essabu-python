"""API for transactions in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class TransactionApi(BasePaymentApi):
    """CRUD operations for transactions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List transactions with pagination."""
        return self._list(self._path("transactions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of transactions."""
        return self._list_all(self._path("transactions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new transaction."""
        return self._create(self._path("transactions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a transaction by ID."""
        return self._retrieve(self._path("transactions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a transaction."""
        return self._update(self._path("transactions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a transaction."""
        return self._delete(self._path("transactions", resource_id))
