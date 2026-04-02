"""API client for managing exchange rate provider resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class ExchangeRateProviderApi(BaseApi):
    """API client for managing exchange rate provider resources. Base path: /api/accounting/exchange-rate-providers"""
    BASE_PATH = "/api/accounting/exchange-rate-providers"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, provider_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{provider_id}")
    def list(self, company_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?companyId={company_id}")
    def update(self, provider_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{provider_id}", request)
    def delete(self, provider_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{provider_id}")
