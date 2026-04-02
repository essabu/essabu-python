"""Tests for the Accounting module."""

from __future__ import annotations

import httpx
import pytest
import respx

from essabu import Essabu


@pytest.fixture
def client():
    c = Essabu(api_key="test-key", tenant_id="t", base_url="https://api.test.com")
    yield c
    c.close()


class TestAccountingInvoices:
    @respx.mock
    def test_list_invoices(self, client):
        respx.get("https://api.test.com/api/accounting/invoices").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "inv-1", "total": "1500.00"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.accounting.invoices.list()
        assert result.data[0]["total"] == "1500.00"

    @respx.mock
    def test_create_invoice(self, client):
        respx.post("https://api.test.com/api/accounting/invoices").mock(
            return_value=httpx.Response(201, json={"id": "inv-new", "status": "draft"})
        )
        result = client.accounting.invoices.create(
            customer_id="cust-1",
            items=[{"description": "Service", "quantity": 1, "unit_price": "100.00"}],
        )
        assert result["status"] == "draft"


class TestAccountingAccounts:
    @respx.mock
    def test_list_accounts(self, client):
        respx.get("https://api.test.com/api/accounting/accounts").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "acc-1", "code": "1000"}], "total": 1, "page": 1, "pageSize": 25, "totalPages": 1})
        )
        result = client.accounting.accounts.list()
        assert result.data[0]["code"] == "1000"


class TestAccountingPayments:
    @respx.mock
    def test_create_payment(self, client):
        respx.post("https://api.test.com/api/accounting/payments").mock(
            return_value=httpx.Response(201, json={"id": "pay-1", "amount": "500.00"})
        )
        result = client.accounting.payments.create(invoice_id="inv-1", amount="500.00")
        assert result["amount"] == "500.00"


class TestAccountingWallets:
    @respx.mock
    def test_list_wallets(self, client):
        respx.get("https://api.test.com/api/accounting/wallets").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "w-1"}], "total": 1, "page": 1, "pageSize": 25, "totalPages": 1})
        )
        result = client.accounting.wallets.list()
        assert len(result.data) == 1
