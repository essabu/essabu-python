"""API for exchange rate providers in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class ExchangeRateProviderApi(BaseAccountingApi):
    """CRUD operations for exchange rate providers."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List exchange rate providers with pagination."""
        return self._list(self._path("exchange_rate_providers"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of exchange rate providers."""
        return self._list_all(self._path("exchange_rate_providers"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new exchange rate provider."""
        return self._create(self._path("exchange_rate_providers"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a exchange rate provider by ID."""
        return self._retrieve(self._path("exchange_rate_providers", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a exchange rate provider."""
        return self._update(self._path("exchange_rate_providers", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a exchange rate provider."""
        return self._delete(self._path("exchange_rate_providers", resource_id))
