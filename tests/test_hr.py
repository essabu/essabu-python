"""Tests for the HR module."""

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


class TestHREmployees:
    @respx.mock
    def test_list_employees(self, client):
        respx.get("https://api.test.com/api/hr/employees").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "1", "first_name": "Jean"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.hr.employees.list()
        assert len(result.data) == 1
        assert result.data[0]["first_name"] == "Jean"

    @respx.mock
    def test_create_employee(self, client):
        respx.post("https://api.test.com/api/hr/employees").mock(
            return_value=httpx.Response(201, json={"id": "new-1", "first_name": "Jean", "last_name": "Mukendi"})
        )
        result = client.hr.employees.create(first_name="Jean", last_name="Mukendi")
        assert result["id"] == "new-1"

    @respx.mock
    def test_retrieve_employee(self, client):
        respx.get("https://api.test.com/api/hr/employees/emp-1").mock(
            return_value=httpx.Response(200, json={"id": "emp-1", "first_name": "Jean"})
        )
        result = client.hr.employees.retrieve("emp-1")
        assert result["id"] == "emp-1"

    @respx.mock
    def test_update_employee(self, client):
        respx.patch("https://api.test.com/api/hr/employees/emp-1").mock(
            return_value=httpx.Response(200, json={"id": "emp-1", "first_name": "Updated"})
        )
        result = client.hr.employees.update("emp-1", first_name="Updated")
        assert result["first_name"] == "Updated"

    @respx.mock
    def test_delete_employee(self, client):
        respx.delete("https://api.test.com/api/hr/employees/emp-1").mock(
            return_value=httpx.Response(204)
        )
        result = client.hr.employees.delete("emp-1")
        assert result == {}


class TestHRContracts:
    @respx.mock
    def test_list_contracts(self, client):
        respx.get("https://api.test.com/api/hr/contracts").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "pageSize": 25, "totalPages": 0})
        )
        result = client.hr.contracts.list()
        assert result.total == 0


class TestHRLeaves:
    @respx.mock
    def test_create_leave(self, client):
        respx.post("https://api.test.com/api/hr/leaves").mock(
            return_value=httpx.Response(201, json={"id": "leave-1", "type": "annual"})
        )
        result = client.hr.leaves.create(employee_id="emp-1", type="annual", start_date="2024-01-15")
        assert result["id"] == "leave-1"


class TestHRPayroll:
    @respx.mock
    def test_list_payroll(self, client):
        respx.get("https://api.test.com/api/hr/payroll").mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "p1"}],
                "total": 1, "page": 1, "pageSize": 25, "totalPages": 1,
            })
        )
        result = client.hr.payroll.list()
        assert len(result.data) == 1
