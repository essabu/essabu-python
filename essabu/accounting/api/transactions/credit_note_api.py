"""API for credit notes in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class CreditNoteApi(BaseAccountingApi):
    """CRUD operations for credit notes."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List credit notes with pagination."""
        return self._list(self._path("credit_notes"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of credit notes."""
        return self._list_all(self._path("credit_notes"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new credit note."""
        return self._create(self._path("credit_notes"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a credit note by ID."""
        return self._retrieve(self._path("credit_notes", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a credit note."""
        return self._update(self._path("credit_notes", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a credit note."""
        return self._delete(self._path("credit_notes", resource_id))
