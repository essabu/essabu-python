"""API for payments in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class PaymentApi(BaseAccountingApi):
    """CRUD operations for payments."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List payments with pagination."""
        return self._list(self._path("payments"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of payments."""
        return self._list_all(self._path("payments"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new payment."""
        return self._create(self._path("payments"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a payment by ID."""
        return self._retrieve(self._path("payments", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a payment."""
        return self._update(self._path("payments", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a payment."""
        return self._delete(self._path("payments", resource_id))
