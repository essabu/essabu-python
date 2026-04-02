"""API client for managing tax rate resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class TaxRateApi(BaseApi):
    """API client for managing tax rate resources. Base path: /api/accounting/tax-rates"""
    BASE_PATH = "/api/accounting/tax-rates"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, tax_rate_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{tax_rate_id}")
    def list(self, company_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?companyId={company_id}")
    def update(self, tax_rate_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{tax_rate_id}", request)
    def deactivate(self, tax_rate_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{tax_rate_id}/deactivate")
    def delete(self, tax_rate_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{tax_rate_id}")
