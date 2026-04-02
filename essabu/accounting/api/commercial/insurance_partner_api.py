"""API for insurance partners in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class InsurancePartnerApi(BaseAccountingApi):
    """CRUD operations for insurance partners."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List insurance partners with pagination."""
        return self._list(self._path("insurance_partners"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of insurance partners."""
        return self._list_all(self._path("insurance_partners"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new insurance partner."""
        return self._create(self._path("insurance_partners"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a insurance partner by ID."""
        return self._retrieve(self._path("insurance_partners", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a insurance partner."""
        return self._update(self._path("insurance_partners", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a insurance partner."""
        return self._delete(self._path("insurance_partners", resource_id))
