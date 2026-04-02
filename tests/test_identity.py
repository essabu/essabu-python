"""Tests for the Identity module."""

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


class TestIdentityAuth:
    @respx.mock
    def test_login(self, client):
        respx.post("https://api.test.com/api/identity/auth/login").mock(
            return_value=httpx.Response(200, json={"access_token": "tok-123", "refresh_token": "ref-456"})
        )
        result = client.identity.auth.login(email="user@example.com", password="secret")
        assert result["access_token"] == "tok-123"

    @respx.mock
    def test_me(self, client):
        respx.get("https://api.test.com/api/identity/auth/me").mock(
            return_value=httpx.Response(200, json={"id": "u-1", "email": "user@example.com"})
        )
        result = client.identity.auth.me()
        assert result["email"] == "user@example.com"


class TestIdentityUsers:
    @respx.mock
    def test_list_users(self, client):
        respx.get("https://api.test.com/api/identity/users").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "u-1"}], "total": 1, "page": 1, "pageSize": 25, "totalPages": 1})
        )
        result = client.identity.users.list()
        assert len(result.data) == 1


class TestIdentityRoles:
    @respx.mock
    def test_create_role(self, client):
        respx.post("https://api.test.com/api/identity/roles").mock(
            return_value=httpx.Response(201, json={"id": "role-1", "name": "Admin"})
        )
        result = client.identity.roles.create(name="Admin", permissions=["read", "write"])
        assert result["name"] == "Admin"
