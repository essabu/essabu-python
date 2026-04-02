"""API for payment intents in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class PaymentIntentApi(BasePaymentApi):
    """CRUD operations for payment intents."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List payment intents with pagination."""
        return self._list(self._path("payment_intents"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of payment intents."""
        return self._list_all(self._path("payment_intents"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new payment intent."""
        return self._create(self._path("payment_intents"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a payment intent by ID."""
        return self._retrieve(self._path("payment_intents", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a payment intent."""
        return self._update(self._path("payment_intents", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a payment intent."""
        return self._delete(self._path("payment_intents", resource_id))

    def confirm(self, resource_id: str) -> dict[str, Any]:
        """Confirm a payment intent."""
        return self._http.post(self._path("payment_intents", resource_id, "confirm"), json={})

    def cancel(self, resource_id: str) -> dict[str, Any]:
        """Cancel a payment intent."""
        return self._http.post(self._path("payment_intents", resource_id, "cancel"), json={})

    def capture(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Capture a payment intent."""
        return self._http.post(self._path("payment_intents", resource_id, "capture"), json=data)
