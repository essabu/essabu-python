"""API for kyc documents in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class KycDocumentApi(BasePaymentApi):
    """CRUD operations for kyc documents."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List kyc documents with pagination."""
        return self._list(self._path("kyc_documents"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of kyc documents."""
        return self._list_all(self._path("kyc_documents"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new kyc document."""
        return self._create(self._path("kyc_documents"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a kyc document by ID."""
        return self._retrieve(self._path("kyc_documents", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a kyc document."""
        return self._update(self._path("kyc_documents", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a kyc document."""
        return self._delete(self._path("kyc_documents", resource_id))
