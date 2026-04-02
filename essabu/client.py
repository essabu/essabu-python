"""Main entry point for the Essabu SDK.

Usage::

    from essabu import Essabu

    client = Essabu(api_key="xxx", tenant_id="xxx")

    # HR
    client.hr.employees.create({"first_name": "Jean", "last_name": "Mukendi"})
    client.hr.payrolls.calculate(payroll_id)

    # Accounting
    client.accounting.invoices.create({...})

    # Identity
    client.identity.auth.login(email="...", password="...")

    # Trade
    client.trade.contacts.create({...})

    # Payment
    client.payment.loan_applications.create({...})
"""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.config import EssabuConfig


class Essabu:
    """Unified client for all Essabu services.

    Provides lazy access to each module (HR, Accounting, Identity, Trade,
    Payment, EInvoice, Project, Asset) through typed property accessors.

    Args:
        api_key: API key for Bearer token authentication.
        tenant_id: Tenant identifier for multi-tenant isolation (optional).
        base_url: Root URL of the Essabu API (overrides per-service URLs).
        timeout: Request timeout in seconds (default 30).
        max_retries: Number of automatic retries on 5xx errors (default 3).
        environment: API environment, 'production' or 'sandbox'.
        service_urls: Per-service base URL overrides.
        config: Pre-built EssabuConfig (overrides all other params).
    """

    def __init__(
        self,
        api_key: str | None = None,
        tenant_id: str | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        environment: str = "production",
        service_urls: dict[str, str] | None = None,
        config: EssabuConfig | None = None,
    ) -> None:
        if config is not None:
            self._config = config
        else:
            if not api_key:
                raise ValueError("api_key is required")
            self._config = EssabuConfig(
                api_key=api_key,
                tenant_id=tenant_id,
                base_url=base_url,
                timeout=timeout,
                max_retries=max_retries,
                environment=environment,
                service_urls=service_urls or {},
            )

    def _make_http(self, service: str) -> HttpClient:
        """Create an HttpClient for a specific service."""
        return HttpClient(
            base_url=self._config.get_base_url(service),
            api_key=self._config.api_key,
            tenant_id=self._config.tenant_id,
            timeout=self._config.timeout,
            max_retries=self._config.max_retries,
        )

    # -- Module accessors (lazy initialization via cached_property) -----------

    @cached_property
    def hr(self) -> HrClient:
        """HR module: employees, departments, payroll, leaves, etc."""
        from essabu.hr.client import HrClient
        return HrClient(self._make_http("hr"))

    @cached_property
    def accounting(self) -> AccountingClient:
        """Accounting module: invoices, journals, accounts, reports, etc."""
        from essabu.accounting.client import AccountingClient
        return AccountingClient(self._make_http("accounting"))

    @cached_property
    def identity(self) -> IdentityClient:
        """Identity module: auth, users, roles, permissions, companies, etc."""
        from essabu.identity.client import IdentityClient
        return IdentityClient(self._make_http("identity"))

    @cached_property
    def trade(self) -> TradeClient:
        """Trade module: customers, products, orders, CRM, etc."""
        from essabu.trade.client import TradeClient
        return TradeClient(self._make_http("trade"))

    @cached_property
    def payment(self) -> PaymentClient:
        """Payment module: intents, subscriptions, loans, KYC, etc."""
        from essabu.payment.client import PaymentClient
        return PaymentClient(self._make_http("payment"))

    @cached_property
    def einvoice(self) -> EInvoiceClient:
        """EInvoice module: invoices, submissions, verification, compliance."""
        from essabu.einvoice.client import EInvoiceClient
        return EInvoiceClient(self._make_http("einvoice"))

    @cached_property
    def project(self) -> ProjectClient:
        """Project module: projects, tasks, milestones, reports."""
        from essabu.project.client import ProjectClient
        return ProjectClient(self._make_http("project"))

    @cached_property
    def asset(self) -> AssetClient:
        """Asset module: assets, vehicles, depreciation, maintenance."""
        from essabu.asset.client import AssetClient
        return AssetClient(self._make_http("asset"))

    def close(self) -> None:
        """Close all initialized HTTP clients."""
        for attr in ("hr", "accounting", "identity", "trade", "payment", "einvoice", "project", "asset"):
            client = self.__dict__.get(attr)
            if client is not None and hasattr(client, "_http"):
                client._http.close()

    def __enter__(self) -> Essabu:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


# Type stubs for lazy imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from essabu.hr.client import HrClient
    from essabu.accounting.client import AccountingClient
    from essabu.identity.client import IdentityClient
    from essabu.trade.client import TradeClient
    from essabu.payment.client import PaymentClient
    from essabu.einvoice.client import EInvoiceClient
    from essabu.project.client import ProjectClient
    from essabu.asset.client import AssetClient
