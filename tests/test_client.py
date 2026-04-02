"""Tests for the unified Essabu client."""

from __future__ import annotations

import pytest

from essabu import Essabu, EssabuConfig, EssabuError, PageRequest, PageResponse


class TestEssabuInit:
    """Tests for Essabu client initialization."""

    def test_init_with_api_key(self) -> None:
        client = Essabu(api_key="test-key", tenant_id="tenant-1")
        assert client._config.api_key == "test-key"
        assert client._config.tenant_id == "tenant-1"

    def test_init_requires_api_key(self) -> None:
        with pytest.raises(ValueError, match="api_key is required"):
            Essabu(api_key="")

    def test_init_with_config(self) -> None:
        config = EssabuConfig(api_key="from-config", tenant_id="t1")
        client = Essabu(config=config)
        assert client._config.api_key == "from-config"

    def test_init_with_service_urls(self) -> None:
        client = Essabu(
            api_key="key",
            service_urls={"hr": "https://hr.custom.com"},
        )
        assert client._config.get_base_url("hr") == "https://hr.custom.com"
        assert client._config.get_base_url("trade") == "https://api.essabu.com"

    def test_init_with_base_url_override(self) -> None:
        client = Essabu(api_key="key", base_url="https://custom.essabu.com")
        assert client._config.get_base_url("hr") == "https://custom.essabu.com"
        assert client._config.get_base_url("trade") == "https://custom.essabu.com"


class TestModuleAccess:
    """Tests for lazy module access."""

    def test_hr_module_access(self) -> None:
        client = Essabu(api_key="key")
        hr = client.hr
        assert hr is not None
        assert hr is client.hr  # cached

    def test_accounting_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.accounting is not None

    def test_identity_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.identity is not None

    def test_trade_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.trade is not None

    def test_payment_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.payment is not None

    def test_einvoice_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.einvoice is not None

    def test_project_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.project is not None

    def test_asset_module_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.asset is not None


class TestSubmoduleAccess:
    """Tests for accessing API resources within modules."""

    def test_hr_employees_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.hr.employees is not None

    def test_hr_payrolls_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.hr.payrolls is not None

    def test_accounting_invoices_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.accounting.invoices is not None

    def test_identity_auth_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.identity.auth is not None

    def test_trade_contacts_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.trade.contacts is not None

    def test_payment_loan_applications_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.payment.loan_applications is not None

    def test_einvoice_submissions_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.einvoice.submissions is not None

    def test_project_tasks_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.project.tasks is not None

    def test_asset_vehicles_access(self) -> None:
        client = Essabu(api_key="key")
        assert client.asset.vehicles is not None


class TestContextManager:
    """Tests for context manager support."""

    def test_context_manager(self) -> None:
        with Essabu(api_key="key") as client:
            assert client is not None


class TestPageRequest:
    """Tests for PageRequest model."""

    def test_default(self) -> None:
        page = PageRequest()
        assert page.page == 0
        assert page.size == 20

    def test_of(self) -> None:
        page = PageRequest.of(2, 50)
        assert page.page == 2
        assert page.size == 50

    def test_to_query_string(self) -> None:
        page = PageRequest(page=1, size=10, sort="name", direction="asc")
        assert page.to_query_string() == "page=1&size=10&sort=name,asc"


class TestPageResponse:
    """Tests for PageResponse model."""

    def test_from_dict(self) -> None:
        data = {
            "content": [{"id": "1"}],
            "page": 0,
            "size": 20,
            "totalElements": 100,
            "totalPages": 5,
            "first": True,
            "last": False,
        }
        page = PageResponse.from_dict(data)
        assert page.total_elements == 100
        assert page.has_next is True
        assert page.has_previous is False
        assert page.has_content is True


class TestExceptions:
    """Tests for exception hierarchy."""

    def test_essabu_error_base(self) -> None:
        err = EssabuError("test error", status_code=500)
        assert str(err) == "[500] test error"
        assert err.status_code == 500
        assert err.details == {}

    def test_exception_hierarchy(self) -> None:
        from essabu import (
            AuthenticationError,
            AuthorizationError,
            NotFoundError,
            RateLimitError,
            ServerError,
            ValidationError,
        )

        assert issubclass(AuthenticationError, EssabuError)
        assert issubclass(AuthorizationError, EssabuError)
        assert issubclass(NotFoundError, EssabuError)
        assert issubclass(ValidationError, EssabuError)
        assert issubclass(RateLimitError, EssabuError)
        assert issubclass(ServerError, EssabuError)

    def test_validation_error_has_errors(self) -> None:
        from essabu import ValidationError

        err = ValidationError("bad input", errors={"name": ["required"]})
        assert err.errors == {"name": ["required"]}

    def test_rate_limit_error_has_retry_after(self) -> None:
        from essabu import RateLimitError

        err = RateLimitError("slow down", retry_after=60)
        assert err.retry_after == 60
