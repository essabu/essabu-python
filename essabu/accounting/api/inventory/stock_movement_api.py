"""API client for managing stock movement resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class StockMovementApi(BaseApi):
    """API client for managing stock movement resources. Base path: /api/accounting/stock-movements"""
    BASE_PATH = "/api/accounting/stock-movements"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, movement_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{movement_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def confirm(self, movement_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{movement_id}/confirm")
    def cancel(self, movement_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{movement_id}/cancel")
