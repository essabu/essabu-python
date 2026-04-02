"""Tests for the Payment module."""

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


class TestPaymentIntents:
    @respx.mock
    def test_create_intent(self, client):
        respx.post("https://api.test.com/api/payment/payment_intents").mock(
            return_value=httpx.Response(201, json={"id": "pi-1", "status": "requires_confirmation"})
        )
        result = client.payment.payment_intents.create(amount="100.00", currency="USD")
        assert result["status"] == "requires_confirmation"

    @respx.mock
    def test_confirm_intent(self, client):
        respx.post("https://api.test.com/api/payment/payment_intents/pi-1/confirm").mock(
            return_value=httpx.Response(200, json={"id": "pi-1", "status": "succeeded"})
        )
        result = client.payment.payment_intents.confirm("pi-1")
        assert result["status"] == "succeeded"


class TestLoanApplications:
    @respx.mock
    def test_create_loan_application(self, client):
        respx.post("https://api.test.com/api/payment/loan_applications").mock(
            return_value=httpx.Response(201, json={"id": "la-1", "status": "pending"})
        )
        result = client.payment.loan_applications.create(amount="5000.00", product_id="lp-1")
        assert result["status"] == "pending"

    @respx.mock
    def test_approve_loan(self, client):
        respx.post("https://api.test.com/api/payment/loan_applications/la-1/approve").mock(
            return_value=httpx.Response(200, json={"id": "la-1", "status": "approved"})
        )
        result = client.payment.loan_applications.approve("la-1")
        assert result["status"] == "approved"


class TestSubscriptions:
    @respx.mock
    def test_list_subscriptions(self, client):
        respx.get("https://api.test.com/api/payment/subscriptions").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "sub-1"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.payment.subscriptions.list()
        assert len(result.data) == 1
