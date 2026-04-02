"""API for refunds in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class RefundApi(BasePaymentApi):
    """CRUD operations for refunds."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List refunds with pagination."""
        return self._list(self._path("refunds"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of refunds."""
        return self._list_all(self._path("refunds"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new refund."""
        return self._create(self._path("refunds"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a refund by ID."""
        return self._retrieve(self._path("refunds", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a refund."""
        return self._update(self._path("refunds", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a refund."""
        return self._delete(self._path("refunds", resource_id))
