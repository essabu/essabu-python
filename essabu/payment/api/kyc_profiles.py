"""API for kyc profiles in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class KycProfileApi(BasePaymentApi):
    """CRUD operations for kyc profiles."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List kyc profiles with pagination."""
        return self._list(self._path("kyc_profiles"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of kyc profiles."""
        return self._list_all(self._path("kyc_profiles"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new kyc profile."""
        return self._create(self._path("kyc_profiles"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a kyc profile by ID."""
        return self._retrieve(self._path("kyc_profiles", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a kyc profile."""
        return self._update(self._path("kyc_profiles", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a kyc profile."""
        return self._delete(self._path("kyc_profiles", resource_id))
