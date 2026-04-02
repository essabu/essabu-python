"""API client for managing payment term resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class PaymentTermApi(BaseApi):
    """API client for managing payment term resources. Base path: /api/accounting/payment-terms"""
    BASE_PATH = "/api/accounting/payment-terms"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, term_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{term_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def update(self, term_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{term_id}", request)
    def delete(self, term_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{term_id}")
