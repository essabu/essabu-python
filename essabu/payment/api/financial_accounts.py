"""API for financial accounts in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class FinancialAccountApi(BasePaymentApi):
    """CRUD operations for financial accounts."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List financial accounts with pagination."""
        return self._list(self._path("financial_accounts"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of financial accounts."""
        return self._list_all(self._path("financial_accounts"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new financial account."""
        return self._create(self._path("financial_accounts"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a financial account by ID."""
        return self._retrieve(self._path("financial_accounts", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a financial account."""
        return self._update(self._path("financial_accounts", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a financial account."""
        return self._delete(self._path("financial_accounts", resource_id))
