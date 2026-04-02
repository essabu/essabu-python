"""API client for managing fiscal year resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class FiscalYearApi(BaseApi):
    """API client for managing fiscal year resources. Base path: /api/accounting/fiscal-years"""
    BASE_PATH = "/api/accounting/fiscal-years"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, fiscal_year_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{fiscal_year_id}")
    def list(self, company_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?companyId={company_id}")
    def update(self, fiscal_year_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{fiscal_year_id}", request)
    def close(self, fiscal_year_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{fiscal_year_id}/close")
    def reopen(self, fiscal_year_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{fiscal_year_id}/reopen")
    def get_current(self, company_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/current?companyId={company_id}")
