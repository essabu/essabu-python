"""API client for managing stock count resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class StockCountApi(BaseApi):
    """API client for managing stock count resources. Base path: /api/accounting/stock-counts"""
    BASE_PATH = "/api/accounting/stock-counts"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, count_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{count_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def finalize(self, count_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{count_id}/finalize")
    def apply_adjustments(self, count_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{count_id}/apply-adjustments")
