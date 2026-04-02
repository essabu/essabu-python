"""API for fiscal years in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class FiscalYearApi(BaseAccountingApi):
    """CRUD operations for fiscal years."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List fiscal years with pagination."""
        return self._list(self._path("fiscal_years"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of fiscal years."""
        return self._list_all(self._path("fiscal_years"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new fiscal year."""
        return self._create(self._path("fiscal_years"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a fiscal year by ID."""
        return self._retrieve(self._path("fiscal_years", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a fiscal year."""
        return self._update(self._path("fiscal_years", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a fiscal year."""
        return self._delete(self._path("fiscal_years", resource_id))
