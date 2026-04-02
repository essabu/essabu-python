"""API client for managing webhook resources."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/webhooks"


class WebhookApi(BaseApi):
    """Webhook management operations.

    Base path: /api/hr/webhooks
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new webhook subscription."""
        return self._http.post(_BASE_PATH, request)

    def get(self, webhook_id: str) -> dict[str, Any]:
        """Retrieve a webhook subscription by ID."""
        return self._http.get(f"{_BASE_PATH}/{webhook_id}")

    def list(self) -> list[dict[str, Any]]:
        """List all webhook subscriptions."""
        return self._http.get(_BASE_PATH)

    def update(self, webhook_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update a webhook subscription."""
        return self._http.put(f"{_BASE_PATH}/{webhook_id}", request)

    def delete(self, webhook_id: str) -> None:
        """Delete a webhook subscription."""
        self._http.delete(f"{_BASE_PATH}/{webhook_id}")

    def get_deliveries(self, webhook_id: str) -> list[dict[str, Any]]:
        """Get delivery logs for a webhook subscription."""
        return self._http.get(f"{_BASE_PATH}/{webhook_id}/deliveries")

    def test(self, webhook_id: str) -> None:
        """Send a test event to a webhook subscription."""
        self._http.post_void(f"{_BASE_PATH}/{webhook_id}/test")
