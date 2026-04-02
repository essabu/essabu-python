"""API for insurance contracts in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class InsuranceContractApi(BaseAccountingApi):
    """CRUD operations for insurance contracts."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List insurance contracts with pagination."""
        return self._list(self._path("insurance_contracts"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of insurance contracts."""
        return self._list_all(self._path("insurance_contracts"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new insurance contract."""
        return self._create(self._path("insurance_contracts"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a insurance contract by ID."""
        return self._retrieve(self._path("insurance_contracts", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a insurance contract."""
        return self._update(self._path("insurance_contracts", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a insurance contract."""
        return self._delete(self._path("insurance_contracts", resource_id))
