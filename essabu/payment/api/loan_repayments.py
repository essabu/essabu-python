"""API for loan repayments in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class LoanRepaymentApi(BasePaymentApi):
    """CRUD operations for loan repayments."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List loan repayments with pagination."""
        return self._list(self._path("loan_repayments"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of loan repayments."""
        return self._list_all(self._path("loan_repayments"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new loan repayment."""
        return self._create(self._path("loan_repayments"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a loan repayment by ID."""
        return self._retrieve(self._path("loan_repayments", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a loan repayment."""
        return self._update(self._path("loan_repayments", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a loan repayment."""
        return self._delete(self._path("loan_repayments", resource_id))
