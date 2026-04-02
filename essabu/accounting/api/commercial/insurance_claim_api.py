"""API for insurance claims in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class InsuranceClaimApi(BaseAccountingApi):
    """CRUD operations for insurance claims."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List insurance claims with pagination."""
        return self._list(self._path("insurance_claims"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of insurance claims."""
        return self._list_all(self._path("insurance_claims"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new insurance claim."""
        return self._create(self._path("insurance_claims"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a insurance claim by ID."""
        return self._retrieve(self._path("insurance_claims", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a insurance claim."""
        return self._update(self._path("insurance_claims", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a insurance claim."""
        return self._delete(self._path("insurance_claims", resource_id))
