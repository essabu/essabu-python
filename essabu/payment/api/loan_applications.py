"""API for loan applications in the payment module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class LoanApplicationApi(BasePaymentApi):
    """CRUD operations for loan applications."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List loan applications with pagination."""
        return self._list(self._path("loan_applications"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of loan applications."""
        return self._list_all(self._path("loan_applications"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new loan application."""
        return self._create(self._path("loan_applications"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a loan application by ID."""
        return self._retrieve(self._path("loan_applications", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a loan application."""
        return self._update(self._path("loan_applications", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a loan application."""
        return self._delete(self._path("loan_applications", resource_id))

    def approve(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Approve a loan application."""
        return self._http.post(self._path("loan_applications", resource_id, "approve"), json=data)

    def reject(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Reject a loan application."""
        return self._http.post(self._path("loan_applications", resource_id, "reject"), json=data)

    def disburse(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Disburse a loan application."""
        return self._http.post(self._path("loan_applications", resource_id, "disburse"), json=data)
