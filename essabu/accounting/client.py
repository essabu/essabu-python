"""Accounting module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.accounting.api.core.account_api import AccountApi
from essabu.accounting.api.core.balance_api import BalanceApi
from essabu.accounting.api.core.config_api import ConfigApi
from essabu.accounting.api.transactions.journal_api import JournalApi
from essabu.accounting.api.transactions.journal_entry_api import JournalEntryApi
from essabu.accounting.api.transactions.invoice_api import InvoiceApi
from essabu.accounting.api.transactions.quote_api import QuoteApi
from essabu.accounting.api.transactions.credit_note_api import CreditNoteApi
from essabu.accounting.api.transactions.payment_api import PaymentApi
from essabu.accounting.api.transactions.payment_term_api import PaymentTermApi
from essabu.accounting.api.finance.tax_rate_api import TaxRateApi
from essabu.accounting.api.finance.currency_api import CurrencyApi
from essabu.accounting.api.finance.exchange_rate_api import ExchangeRateApi
from essabu.accounting.api.finance.exchange_rate_provider_api import ExchangeRateProviderApi
from essabu.accounting.api.finance.fiscal_year_api import FiscalYearApi
from essabu.accounting.api.finance.period_api import PeriodApi
from essabu.accounting.api.finance.report_api import ReportApi
from essabu.accounting.api.finance.wallet_api import WalletApi
from essabu.accounting.api.finance.wallet_transaction_api import WalletTransactionApi
from essabu.accounting.api.commercial.insurance_partner_api import InsurancePartnerApi
from essabu.accounting.api.commercial.insurance_contract_api import InsuranceContractApi
from essabu.accounting.api.commercial.insurance_claim_api import InsuranceClaimApi
from essabu.accounting.api.commercial.price_list_api import PriceListApi
from essabu.accounting.api.commercial.price_list_override_api import PriceListOverrideApi
from essabu.accounting.api.inventory.supplier_api import SupplierApi
from essabu.accounting.api.inventory.inventory_api import InventoryApi
from essabu.accounting.api.inventory.purchase_order_api import PurchaseOrderApi
from essabu.accounting.api.inventory.batch_api import BatchApi
from essabu.accounting.api.inventory.stock_movement_api import StockMovementApi
from essabu.accounting.api.inventory.stock_count_api import StockCountApi
from essabu.accounting.api.inventory.stock_location_api import StockLocationApi
from essabu.accounting.api.inventory.webhook_api import WebhookApi


class AccountingClient:
    """Accounting module client providing access to all Accounting API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def accounts(self) -> AccountApi:
        return AccountApi(self._http)

    @cached_property
    def balances(self) -> BalanceApi:
        return BalanceApi(self._http)

    @cached_property
    def config(self) -> ConfigApi:
        return ConfigApi(self._http)

    @cached_property
    def journals(self) -> JournalApi:
        return JournalApi(self._http)

    @cached_property
    def journal_entries(self) -> JournalEntryApi:
        return JournalEntryApi(self._http)

    @cached_property
    def invoices(self) -> InvoiceApi:
        return InvoiceApi(self._http)

    @cached_property
    def quotes(self) -> QuoteApi:
        return QuoteApi(self._http)

    @cached_property
    def credit_notes(self) -> CreditNoteApi:
        return CreditNoteApi(self._http)

    @cached_property
    def payments(self) -> PaymentApi:
        return PaymentApi(self._http)

    @cached_property
    def payment_terms(self) -> PaymentTermApi:
        return PaymentTermApi(self._http)

    @cached_property
    def tax_rates(self) -> TaxRateApi:
        return TaxRateApi(self._http)

    @cached_property
    def currencies(self) -> CurrencyApi:
        return CurrencyApi(self._http)

    @cached_property
    def exchange_rates(self) -> ExchangeRateApi:
        return ExchangeRateApi(self._http)

    @cached_property
    def exchange_rate_providers(self) -> ExchangeRateProviderApi:
        return ExchangeRateProviderApi(self._http)

    @cached_property
    def fiscal_years(self) -> FiscalYearApi:
        return FiscalYearApi(self._http)

    @cached_property
    def periods(self) -> PeriodApi:
        return PeriodApi(self._http)

    @cached_property
    def reports(self) -> ReportApi:
        return ReportApi(self._http)

    @cached_property
    def wallets(self) -> WalletApi:
        return WalletApi(self._http)

    @cached_property
    def wallet_transactions(self) -> WalletTransactionApi:
        return WalletTransactionApi(self._http)

    @cached_property
    def insurance_partners(self) -> InsurancePartnerApi:
        return InsurancePartnerApi(self._http)

    @cached_property
    def insurance_contracts(self) -> InsuranceContractApi:
        return InsuranceContractApi(self._http)

    @cached_property
    def insurance_claims(self) -> InsuranceClaimApi:
        return InsuranceClaimApi(self._http)

    @cached_property
    def price_lists(self) -> PriceListApi:
        return PriceListApi(self._http)

    @cached_property
    def price_list_overrides(self) -> PriceListOverrideApi:
        return PriceListOverrideApi(self._http)

    @cached_property
    def suppliers(self) -> SupplierApi:
        return SupplierApi(self._http)

    @cached_property
    def inventory(self) -> InventoryApi:
        return InventoryApi(self._http)

    @cached_property
    def purchase_orders(self) -> PurchaseOrderApi:
        return PurchaseOrderApi(self._http)

    @cached_property
    def batches(self) -> BatchApi:
        return BatchApi(self._http)

    @cached_property
    def stock_movements(self) -> StockMovementApi:
        return StockMovementApi(self._http)

    @cached_property
    def stock_counts(self) -> StockCountApi:
        return StockCountApi(self._http)

    @cached_property
    def stock_locations(self) -> StockLocationApi:
        return StockLocationApi(self._http)

    @cached_property
    def webhooks(self) -> WebhookApi:
        return WebhookApi(self._http)
