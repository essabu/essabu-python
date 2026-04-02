"""API client for managing report resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient

class ReportApi(BaseApi):
    """API client for managing report resources. Base path: /api/accounting/reports"""
    BASE_PATH = "/api/accounting/reports"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def trial_balance(self, company_id: str, period_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/trial-balance?companyId={company_id}&periodId={period_id}")
    def balance_sheet(self, company_id: str, period_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/balance-sheet?companyId={company_id}&periodId={period_id}")
    def income_statement(self, company_id: str, period_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/income-statement?companyId={company_id}&periodId={period_id}")
    def general_ledger(self, company_id: str, period_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/general-ledger?companyId={company_id}&periodId={period_id}")
