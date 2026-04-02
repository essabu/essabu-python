"""API for subscription plans in the payment module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.payment.api.base import BasePaymentApi


class SubscriptionPlanApi(BasePaymentApi):
    """CRUD operations for subscription plans."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List subscription plans with pagination."""
        return self._list(self._path("subscription_plans"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of subscription plans."""
        return self._list_all(self._path("subscription_plans"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new subscription plan."""
        return self._create(self._path("subscription_plans"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a subscription plan by ID."""
        return self._retrieve(self._path("subscription_plans", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a subscription plan."""
        return self._update(self._path("subscription_plans", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a subscription plan."""
        return self._delete(self._path("subscription_plans", resource_id))
