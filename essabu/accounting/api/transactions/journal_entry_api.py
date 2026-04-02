"""API client for managing journal entry resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class JournalEntryApi(BaseApi):
    """API client for managing journal entry resources. Base path: /api/accounting/journal-entries"""
    BASE_PATH = "/api/accounting/journal-entries"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, entry_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{entry_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def update(self, entry_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{entry_id}", request)
    def delete(self, entry_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{entry_id}")
    def validate(self, entry_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{entry_id}/post")
    def reverse(self, entry_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{entry_id}/reverse")
