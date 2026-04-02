"""API for collaterals in the payment module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class CollateralApi(BasePaymentApi):
    """CRUD operations for collaterals."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List collaterals with pagination."""
        return self._list(self._path("collaterals"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of collaterals."""
        return self._list_all(self._path("collaterals"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new collateral."""
        return self._create(self._path("collaterals"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a collateral by ID."""
        return self._retrieve(self._path("collaterals", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a collateral."""
        return self._update(self._path("collaterals", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a collateral."""
        return self._delete(self._path("collaterals", resource_id))
