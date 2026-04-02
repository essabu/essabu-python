"""API for loan products in the payment module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class LoanProductApi(BasePaymentApi):
    """CRUD operations for loan products."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List loan products with pagination."""
        return self._list(self._path("loan_products"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of loan products."""
        return self._list_all(self._path("loan_products"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new loan product."""
        return self._create(self._path("loan_products"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a loan product by ID."""
        return self._retrieve(self._path("loan_products", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a loan product."""
        return self._update(self._path("loan_products", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a loan product."""
        return self._delete(self._path("loan_products", resource_id))
