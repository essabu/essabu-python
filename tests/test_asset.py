"""Tests for the Asset module."""

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


class TestAssets:
    @respx.mock
    def test_list_assets(self, client):
        respx.get("https://api.test.com/api/asset/assets").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "a-1", "name": "Laptop"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.asset.assets.list()
        assert result.data[0]["name"] == "Laptop"


class TestVehicles:
    @respx.mock
    def test_create_vehicle(self, client):
        respx.post("https://api.test.com/api/asset/vehicles").mock(
            return_value=httpx.Response(201, json={"id": "v-1", "plate": "ABC-123"})
        )
        result = client.asset.vehicles.create(plate="ABC-123", model="Toyota Hilux")
        assert result["plate"] == "ABC-123"
