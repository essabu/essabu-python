"""API client for managing accounting period resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class PeriodApi(BaseApi):
    """API client for managing accounting period resources. Base path: /api/accounting/periods"""
    BASE_PATH = "/api/accounting/periods"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, period_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{period_id}")
    def list(self, fiscal_year_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}?fiscalYearId={fiscal_year_id}")
    def close(self, period_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{period_id}/close")
    def reopen(self, period_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{period_id}/reopen")
