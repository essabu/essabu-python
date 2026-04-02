"""API client for managing currency resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class CurrencyApi(BaseApi):
    """API client for managing currency resources. Base path: /api/accounting/currencies"""
    BASE_PATH = "/api/accounting/currencies"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, currency_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{currency_id}")
    def list(self) -> list[dict[str, Any]]:
        return self._http.get(self.BASE_PATH)
    def update(self, currency_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{currency_id}", request)
    def delete(self, currency_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{currency_id}")
    def set_default(self, currency_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{currency_id}/set-default")
