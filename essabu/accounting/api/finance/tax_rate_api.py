"""API for tax rates in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class TaxRateApi(BaseAccountingApi):
    """CRUD operations for tax rates."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List tax rates with pagination."""
        return self._list(self._path("tax_rates"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of tax rates."""
        return self._list_all(self._path("tax_rates"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new tax rate."""
        return self._create(self._path("tax_rates"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a tax rate by ID."""
        return self._retrieve(self._path("tax_rates", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a tax rate."""
        return self._update(self._path("tax_rates", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a tax rate."""
        return self._delete(self._path("tax_rates", resource_id))
