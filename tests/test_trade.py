"""Tests for the Trade / CRM module."""

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


class TestTradeCustomers:
    @respx.mock
    def test_list_customers(self, client):
        respx.get("https://api.test.com/api/trade/customers").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "c-1", "name": "Acme"}], "total": 1, "page": 1, "pageSize": 25, "totalPages": 1})
        )
        result = client.trade.customers.list()
        assert result.data[0]["name"] == "Acme"

    @respx.mock
    def test_create_customer(self, client):
        respx.post("https://api.test.com/api/trade/customers").mock(
            return_value=httpx.Response(201, json={"id": "c-new", "name": "NewCo"})
        )
        result = client.trade.customers.create(name="NewCo", email="info@newco.com")
        assert result["name"] == "NewCo"


class TestTradeOpportunities:
    @respx.mock
    def test_list_opportunities(self, client):
        respx.get("https://api.test.com/api/trade/opportunities").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "opp-1", "value": "10000"}], "total": 1, "page": 1, "pageSize": 25, "totalPages": 1})
        )
        result = client.trade.opportunities.list()
        assert len(result.data) == 1


class TestTradeProducts:
    @respx.mock
    def test_create_product(self, client):
        respx.post("https://api.test.com/api/trade/products").mock(
            return_value=httpx.Response(201, json={"id": "p-1", "name": "Widget"})
        )
        result = client.trade.products.create(name="Widget", price="25.00")
        assert result["name"] == "Widget"
