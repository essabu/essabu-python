"""Tests for the E-Invoice module."""

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


class TestEInvoiceSubmissions:
    @respx.mock
    def test_create_submission(self, client):
        respx.post("https://api.test.com/api/einvoice/submissions").mock(
            return_value=httpx.Response(201, json={"id": "sub-1", "status": "pending"})
        )
        result = client.einvoice.submissions.create(invoice_id="inv-1")
        assert result["status"] == "pending"

    @respx.mock
    def test_submit(self, client):
        respx.post("https://api.test.com/api/einvoice/submissions/sub-1/submit").mock(
            return_value=httpx.Response(200, json={"id": "sub-1", "status": "submitted"})
        )
        result = client.einvoice.submissions.submit("sub-1")
        assert result["status"] == "submitted"


class TestEInvoiceVerification:
    @respx.mock
    def test_verify(self, client):
        respx.post("https://api.test.com/api/einvoice/verification/verify").mock(
            return_value=httpx.Response(200, json={"valid": True, "invoice_id": "inv-1"})
        )
        result = client.einvoice.verification.verify(qr_code="ABC123")
        assert result["valid"] is True
