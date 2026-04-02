"""API for verification in the einvoice module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.einvoice.api.base import BaseEinvoiceApi


class VerificationApi(BaseEinvoiceApi):
    """CRUD operations for verification."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List verification with pagination."""
        return self._list(self._path("verification"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of verification."""
        return self._list_all(self._path("verification"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new verification."""
        return self._create(self._path("verification"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a verification by ID."""
        return self._retrieve(self._path("verification", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a verification."""
        return self._update(self._path("verification", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a verification."""
        return self._delete(self._path("verification", resource_id))

    def verify(self, **data: Any) -> dict[str, Any]:
        """Verify an e-invoice QR code or reference."""
        return self._http.post(self._path("verification", "verify"), json=data)
