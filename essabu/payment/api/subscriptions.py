"""API for subscriptions in the payment module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class SubscriptionApi(BasePaymentApi):
    """CRUD operations for subscriptions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List subscriptions with pagination."""
        return self._list(self._path("subscriptions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of subscriptions."""
        return self._list_all(self._path("subscriptions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new subscription."""
        return self._create(self._path("subscriptions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a subscription by ID."""
        return self._retrieve(self._path("subscriptions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a subscription."""
        return self._update(self._path("subscriptions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a subscription."""
        return self._delete(self._path("subscriptions", resource_id))

    def pause(self, resource_id: str) -> dict[str, Any]:
        """Pause a subscription."""
        return self._http.post(self._path("subscriptions", resource_id, "pause"), json={})

    def resume(self, resource_id: str) -> dict[str, Any]:
        """Resume a subscription."""
        return self._http.post(self._path("subscriptions", resource_id, "resume"), json={})

    def cancel_subscription(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Cancel a subscription."""
        return self._http.post(self._path("subscriptions", resource_id, "cancel"), json=data)
