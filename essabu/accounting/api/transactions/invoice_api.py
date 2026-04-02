"""API client for managing invoice resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class InvoiceApi(BaseApi):
    """API client for managing invoice resources. Base path: /api/accounting/invoices"""
    BASE_PATH = "/api/accounting/invoices"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, invoice_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{invoice_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def update(self, invoice_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{invoice_id}", request)
    def delete(self, invoice_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{invoice_id}")
    def finalize(self, invoice_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{invoice_id}/finalize")
    def send(self, invoice_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{invoice_id}/send")
    def mark_as_paid(self, invoice_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{invoice_id}/mark-as-paid")
    def cancel(self, invoice_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{invoice_id}/cancel")
    def download_pdf(self, invoice_id: str) -> bytes:
        return self._http.get_bytes(f"{self.BASE_PATH}/{invoice_id}/pdf")
    def create_recurring(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(f"{self.BASE_PATH}/recurring", request)
    def list_recurring(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}/recurring?companyId={company_id}", page)
        return self._http.get(path)
    def update_recurring(self, recurring_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/recurring/{recurring_id}", request)
    def delete_recurring(self, recurring_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/recurring/{recurring_id}")
    def activate_recurring(self, recurring_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/recurring/{recurring_id}/activate")
    def deactivate_recurring(self, recurring_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/recurring/{recurring_id}/deactivate")
