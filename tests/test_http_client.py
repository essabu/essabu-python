"""Tests for the HTTP client."""

from __future__ import annotations

import httpx
import pytest
import respx

from essabu.common.exceptions import (
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from essabu.common.http_client import HttpClient
from essabu.config import EssabuConfig


@pytest.fixture
def config():
    return EssabuConfig(api_key="test-key", tenant_id="tenant-1", base_url="https://api.test.com", max_retries=0)


@pytest.fixture
def http(config):
    client = HttpClient(config)
    yield client
    client.close()


class TestHttpClient:
    @respx.mock
    def test_get_success(self, http):
        respx.get("https://api.test.com/api/hr/employees").mock(
            return_value=httpx.Response(200, json={"data": [{"id": "1"}], "total": 1})
        )
        result = http.get("/api/hr/employees")
        assert result["data"][0]["id"] == "1"

    @respx.mock
    def test_post_success(self, http):
        respx.post("https://api.test.com/api/hr/employees").mock(
            return_value=httpx.Response(201, json={"id": "new-1", "first_name": "Jean"})
        )
        result = http.post("/api/hr/employees", json={"first_name": "Jean"})
        assert result["id"] == "new-1"

    @respx.mock
    def test_delete_no_content(self, http):
        respx.delete("https://api.test.com/api/hr/employees/1").mock(
            return_value=httpx.Response(204)
        )
        result = http.delete("/api/hr/employees/1")
        assert result == {}

    @respx.mock
    def test_401_raises_authentication_error(self, http):
        respx.get("https://api.test.com/api/test").mock(
            return_value=httpx.Response(401, json={"message": "Invalid token"})
        )
        with pytest.raises(AuthenticationError, match="Invalid token"):
            http.get("/api/test")

    @respx.mock
    def test_404_raises_not_found_error(self, http):
        respx.get("https://api.test.com/api/test/999").mock(
            return_value=httpx.Response(404, json={"message": "Not found"})
        )
        with pytest.raises(NotFoundError):
            http.get("/api/test/999")

    @respx.mock
    def test_422_raises_validation_error(self, http):
        respx.post("https://api.test.com/api/test").mock(
            return_value=httpx.Response(422, json={"message": "Validation failed", "errors": [{"field": "email"}]})
        )
        with pytest.raises(ValidationError) as exc_info:
            http.post("/api/test", json={})
        assert len(exc_info.value.errors) == 1

    @respx.mock
    def test_429_raises_rate_limit_error(self, http):
        respx.get("https://api.test.com/api/test").mock(
            return_value=httpx.Response(429, json={"message": "Too many requests"}, headers={"Retry-After": "30"})
        )
        with pytest.raises(RateLimitError) as exc_info:
            http.get("/api/test")
        assert exc_info.value.retry_after == 30.0

    @respx.mock
    def test_500_raises_server_error(self, http):
        respx.get("https://api.test.com/api/test").mock(
            return_value=httpx.Response(500, json={"message": "Internal error"})
        )
        with pytest.raises(ServerError):
            http.get("/api/test")

    @respx.mock
    def test_get_paginated(self, http):
        respx.get("https://api.test.com/api/hr/employees").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "1"}],
                "total": 50,
                "page": 1,
                "pageSize": 25,
                "totalPages": 2,
            })
        )
        page = http.get_paginated("/api/hr/employees", params={"page": 1, "pageSize": 25})
        assert page.total == 50
        assert page.has_next is True

    @respx.mock
    def test_patch_success(self, http):
        respx.patch("https://api.test.com/api/hr/employees/1").mock(
            return_value=httpx.Response(200, json={"id": "1", "first_name": "Updated"})
        )
        result = http.patch("/api/hr/employees/1", json={"first_name": "Updated"})
        assert result["first_name"] == "Updated"

    @respx.mock
    def test_auth_headers_sent(self, http):
        route = respx.get("https://api.test.com/api/test").mock(
            return_value=httpx.Response(200, json={})
        )
        http.get("/api/test")
        request = route.calls[0].request
        assert request.headers["authorization"] == "Bearer test-key"
        assert request.headers["x-tenant-id"] == "tenant-1"
