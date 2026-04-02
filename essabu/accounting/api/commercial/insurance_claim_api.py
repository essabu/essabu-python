"""API client for managing insurance claim resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class InsuranceClaimApi(BaseApi):
    """API client for managing insurance claim resources. Base path: /api/accounting/insurance-claims"""
    BASE_PATH = "/api/accounting/insurance-claims"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, claim_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{claim_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def submit(self, claim_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{claim_id}/submit")
    def approve(self, claim_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(f"{self.BASE_PATH}/{claim_id}/approve", request)
    def deny(self, claim_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(f"{self.BASE_PATH}/{claim_id}/deny", request)
    def appeal(self, claim_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{claim_id}/appeal")
    def close(self, claim_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{claim_id}/close")
    def list_by_contract(self, contract_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?contractId={contract_id}")
    def list_by_invoice(self, invoice_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?invoiceId={invoice_id}")
