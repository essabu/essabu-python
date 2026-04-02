"""Tests for the main Essabu client."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from essabu import Essabu, EssabuConfig
from essabu.accounting.client import AccountingClient
from essabu.asset.client import AssetClient
from essabu.einvoice.client import EInvoiceClient
from essabu.hr.client import HRClient
from essabu.identity.client import IdentityClient
from essabu.payment.client import PaymentClient
from essabu.project.client import ProjectClient
from essabu.trade.client import TradeClient


class TestEssabuConfig:
    def test_config_from_explicit_values(self):
        config = EssabuConfig(api_key="test-key", tenant_id="tenant-1")
        assert config.api_key == "test-key"
        assert config.tenant_id == "tenant-1"
        assert config.base_url == "https://api.essabu.com"
        assert config.timeout == 30.0
        assert config.max_retries == 3

    def test_config_from_env(self):
        with patch.dict(os.environ, {"ESSABU_API_KEY": "env-key", "ESSABU_TENANT_ID": "env-tenant"}):
            config = EssabuConfig()
            assert config.api_key == "env-key"
            assert config.tenant_id == "env-tenant"

    def test_config_strips_trailing_slash(self):
        config = EssabuConfig(api_key="k", tenant_id="t", base_url="https://api.essabu.com/")
        assert config.base_url == "https://api.essabu.com"

    def test_validate_missing_api_key(self):
        config = EssabuConfig(api_key="", tenant_id="t")
        with pytest.raises(ValueError, match="API key is required"):
            config.validate()

    def test_validate_missing_tenant_id(self):
        config = EssabuConfig(api_key="k", tenant_id="")
        with pytest.raises(ValueError, match="Tenant ID is required"):
            config.validate()


class TestEssabuClient:
    def test_client_creation(self):
        client = Essabu(api_key="test-key", tenant_id="tenant-1")
        assert client.config.api_key == "test-key"
        assert client.config.tenant_id == "tenant-1"

    def test_client_repr(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert "Essabu(" in repr(client)
        assert "tenant_id='t'" in repr(client)

    def test_lazy_hr_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert client._hr is None
        hr = client.hr
        assert isinstance(hr, HRClient)
        assert client._hr is hr  # cached

    def test_lazy_accounting_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.accounting, AccountingClient)

    def test_lazy_identity_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.identity, IdentityClient)

    def test_lazy_trade_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.trade, TradeClient)

    def test_lazy_payment_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.payment, PaymentClient)

    def test_lazy_einvoice_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.einvoice, EInvoiceClient)

    def test_lazy_project_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.project, ProjectClient)

    def test_lazy_asset_module(self):
        client = Essabu(api_key="k", tenant_id="t")
        assert isinstance(client.asset, AssetClient)

    def test_context_manager(self):
        with Essabu(api_key="k", tenant_id="t") as client:
            assert client.config.api_key == "k"

    def test_missing_credentials_raises(self):
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("ESSABU_API_KEY", None)
            os.environ.pop("ESSABU_TENANT_ID", None)
            with pytest.raises(ValueError):
                Essabu()
