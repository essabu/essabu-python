"""API client for managing balance resources."""

from __future__ import annotations

from typing import Any

from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient


class BalanceApi(BaseApi):
    """API client for managing balance resources.

    Base path: /api/accounting/balances
    """

    BASE_PATH = "/api/accounting/balances"

    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)

    def get_account_balances(self, company_id: str, period_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}/accounts?companyId={company_id}&periodId={period_id}")

    def get_opening_balances(self, company_id: str, fiscal_year_id: str) -> list[dict[str, Any]]:
        return self._http.get(f"{self.BASE_PATH}/opening?companyId={company_id}&fiscalYearId={fiscal_year_id}")

    def create_opening_balance(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(f"{self.BASE_PATH}/opening", request)

    def carry_forward(self, company_id: str, from_fiscal_year_id: str, to_fiscal_year_id: str) -> None:
        self._http.post_empty(
            f"{self.BASE_PATH}/carry-forward?companyId={company_id}"
            f"&fromFiscalYearId={from_fiscal_year_id}&toFiscalYearId={to_fiscal_year_id}"
        )
