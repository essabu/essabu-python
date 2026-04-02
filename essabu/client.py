"""Main Essabu SDK client with lazy module accessors."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient
from essabu.config import EssabuConfig

if TYPE_CHECKING:
    from essabu.accounting.client import AccountingClient
    from essabu.asset.client import AssetClient
    from essabu.einvoice.client import EInvoiceClient
    from essabu.hr.client import HRClient
    from essabu.identity.client import IdentityClient
    from essabu.payment.client import PaymentClient
    from essabu.project.client import ProjectClient
    from essabu.trade.client import TradeClient


class Essabu:
    """Unified Essabu API client.

    Provides lazy access to all platform modules via dot notation:

        client = Essabu(api_key="esa_live_xxx", tenant_id="tenant-id")
        client.hr.employees.list()
        client.accounting.invoices.create(...)
    """

    def __init__(
        self,
        api_key: str | None = None,
        tenant_id: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> None:
        kwargs: dict[str, str | float | int] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if tenant_id is not None:
            kwargs["tenant_id"] = tenant_id
        if base_url is not None:
            kwargs["base_url"] = base_url
        if timeout is not None:
            kwargs["timeout"] = timeout
        if max_retries is not None:
            kwargs["max_retries"] = max_retries

        self._config = EssabuConfig(**kwargs)  # type: ignore[arg-type]
        self._config.validate()
        self._http = HttpClient(self._config)

        # Lazy-loaded module instances
        self._hr: HRClient | None = None
        self._accounting: AccountingClient | None = None
        self._identity: IdentityClient | None = None
        self._trade: TradeClient | None = None
        self._payment: PaymentClient | None = None
        self._einvoice: EInvoiceClient | None = None
        self._project: ProjectClient | None = None
        self._asset: AssetClient | None = None

    # -- Module accessors (lazy) ---------------------------------------------

    @property
    def hr(self) -> HRClient:
        if self._hr is None:
            from essabu.hr.client import HRClient

            self._hr = HRClient(self._http)
        return self._hr

    @property
    def accounting(self) -> AccountingClient:
        if self._accounting is None:
            from essabu.accounting.client import AccountingClient

            self._accounting = AccountingClient(self._http)
        return self._accounting

    @property
    def identity(self) -> IdentityClient:
        if self._identity is None:
            from essabu.identity.client import IdentityClient

            self._identity = IdentityClient(self._http)
        return self._identity

    @property
    def trade(self) -> TradeClient:
        if self._trade is None:
            from essabu.trade.client import TradeClient

            self._trade = TradeClient(self._http)
        return self._trade

    @property
    def payment(self) -> PaymentClient:
        if self._payment is None:
            from essabu.payment.client import PaymentClient

            self._payment = PaymentClient(self._http)
        return self._payment

    @property
    def einvoice(self) -> EInvoiceClient:
        if self._einvoice is None:
            from essabu.einvoice.client import EInvoiceClient

            self._einvoice = EInvoiceClient(self._http)
        return self._einvoice

    @property
    def project(self) -> ProjectClient:
        if self._project is None:
            from essabu.project.client import ProjectClient

            self._project = ProjectClient(self._http)
        return self._project

    @property
    def asset(self) -> AssetClient:
        if self._asset is None:
            from essabu.asset.client import AssetClient

            self._asset = AssetClient(self._http)
        return self._asset

    # -- Lifecycle ------------------------------------------------------------

    @property
    def config(self) -> EssabuConfig:
        return self._config

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self) -> Essabu:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"Essabu(base_url={self._config.base_url!r}, tenant_id={self._config.tenant_id!r})"
