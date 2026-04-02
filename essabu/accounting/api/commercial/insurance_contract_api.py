"""API client for managing insurance contract resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class InsuranceContractApi(BaseApi):
    """API client for managing insurance contract resources. Base path: /api/accounting/insurance-contracts"""
    BASE_PATH = "/api/accounting/insurance-contracts"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, contract_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{contract_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def update(self, contract_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{contract_id}", request)
    def delete(self, contract_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{contract_id}")
    def suspend(self, contract_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{contract_id}/suspend")
    def reactivate(self, contract_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{contract_id}/reactivate")
    def list_by_customer(self, customer_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?customerId={customer_id}")
    def list_by_partner(self, partner_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?partnerId={partner_id}")
    def get_expiring(self, within_days: int) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}/expiring?withinDays={within_days}")
