"""API client for managing webhook resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class WebhookApi(BaseApi):
    """API client for managing webhook resources. Base path: /api/accounting/webhooks"""
    BASE_PATH = "/api/accounting/webhooks"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, webhook_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{webhook_id}")
    def list(self) -> list[dict[str, Any]]:
        return self._http.get(self.BASE_PATH)
    def update(self, webhook_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{webhook_id}", request)
    def delete(self, webhook_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{webhook_id}")
    def get_deliveries(self, webhook_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}/{webhook_id}/deliveries")
    def test(self, webhook_id: str) -> None:
        self._http.post_empty(f"{self.BASE_PATH}/{webhook_id}/test")
