"""API for wallet transactions in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class WalletTransactionApi(BaseAccountingApi):
    """CRUD operations for wallet transactions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List wallet transactions with pagination."""
        return self._list(self._path("wallet_transactions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of wallet transactions."""
        return self._list_all(self._path("wallet_transactions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new wallet transaction."""
        return self._create(self._path("wallet_transactions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a wallet transaction by ID."""
        return self._retrieve(self._path("wallet_transactions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a wallet transaction."""
        return self._update(self._path("wallet_transactions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a wallet transaction."""
        return self._delete(self._path("wallet_transactions", resource_id))
