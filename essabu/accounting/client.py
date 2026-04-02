"""Accounting module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.accounting.api.commercial.insurance_claim_api import InsuranceClaimApi
    from essabu.accounting.api.commercial.insurance_contract_api import InsuranceContractApi
    from essabu.accounting.api.commercial.insurance_partner_api import InsurancePartnerApi
    from essabu.accounting.api.commercial.price_list_api import PriceListApi
    from essabu.accounting.api.commercial.price_list_override_api import PriceListOverrideApi
    from essabu.accounting.api.core.account_api import AccountApi
    from essabu.accounting.api.core.balance_api import BalanceApi
    from essabu.accounting.api.core.config_api import ConfigApi
    from essabu.accounting.api.finance.currency_api import CurrencyApi
    from essabu.accounting.api.finance.exchange_rate_api import ExchangeRateApi
    from essabu.accounting.api.finance.exchange_rate_provider_api import ExchangeRateProviderApi
    from essabu.accounting.api.finance.fiscal_year_api import FiscalYearApi
    from essabu.accounting.api.finance.period_api import PeriodApi
    from essabu.accounting.api.finance.report_api import ReportApi
    from essabu.accounting.api.finance.tax_rate_api import TaxRateApi
    from essabu.accounting.api.finance.wallet_api import WalletApi
    from essabu.accounting.api.finance.wallet_transaction_api import WalletTransactionApi
    from essabu.accounting.api.inventory.batch_api import BatchApi
    from essabu.accounting.api.inventory.inventory_api import InventoryApi
    from essabu.accounting.api.inventory.purchase_order_api import PurchaseOrderApi
    from essabu.accounting.api.inventory.stock_count_api import StockCountApi
    from essabu.accounting.api.inventory.stock_location_api import StockLocationApi
    from essabu.accounting.api.inventory.stock_movement_api import StockMovementApi
    from essabu.accounting.api.inventory.supplier_api import SupplierApi
    from essabu.accounting.api.inventory.webhook_api import WebhookApi
    from essabu.accounting.api.transactions.credit_note_api import CreditNoteApi
    from essabu.accounting.api.transactions.invoice_api import InvoiceApi
    from essabu.accounting.api.transactions.journal_api import JournalApi
    from essabu.accounting.api.transactions.journal_entry_api import JournalEntryApi
    from essabu.accounting.api.transactions.payment_api import PaymentApi
    from essabu.accounting.api.transactions.payment_term_api import PaymentTermApi
    from essabu.accounting.api.transactions.quote_api import QuoteApi


class AccountingClient:
    """Client for the Accounting module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._accounts: AccountApi | None = None
        self._balances: BalanceApi | None = None
        self._config: ConfigApi | None = None
        self._invoices: InvoiceApi | None = None
        self._payments: PaymentApi | None = None
        self._journals: JournalApi | None = None
        self._journal_entries: JournalEntryApi | None = None
        self._credit_notes: CreditNoteApi | None = None
        self._payment_terms: PaymentTermApi | None = None
        self._quotes: QuoteApi | None = None
        self._wallets: WalletApi | None = None
        self._wallet_transactions: WalletTransactionApi | None = None
        self._currencies: CurrencyApi | None = None
        self._exchange_rates: ExchangeRateApi | None = None
        self._exchange_rate_providers: ExchangeRateProviderApi | None = None
        self._fiscal_years: FiscalYearApi | None = None
        self._periods: PeriodApi | None = None
        self._tax_rates: TaxRateApi | None = None
        self._reports: ReportApi | None = None
        self._inventory: InventoryApi | None = None
        self._batches: BatchApi | None = None
        self._purchase_orders: PurchaseOrderApi | None = None
        self._stock_counts: StockCountApi | None = None
        self._stock_locations: StockLocationApi | None = None
        self._stock_movements: StockMovementApi | None = None
        self._suppliers: SupplierApi | None = None
        self._webhooks: WebhookApi | None = None
        self._insurance_claims: InsuranceClaimApi | None = None
        self._insurance_contracts: InsuranceContractApi | None = None
        self._insurance_partners: InsurancePartnerApi | None = None
        self._price_lists: PriceListApi | None = None
        self._price_list_overrides: PriceListOverrideApi | None = None

    @property
    def accounts(self) -> AccountApi:
        if self._accounts is None:
            from essabu.accounting.api.core.account_api import AccountApi
            self._accounts = AccountApi(self._http)
        return self._accounts
    @property
    def balances(self) -> BalanceApi:
        if self._balances is None:
            from essabu.accounting.api.core.balance_api import BalanceApi
            self._balances = BalanceApi(self._http)
        return self._balances
    @property
    def config(self) -> ConfigApi:
        if self._config is None:
            from essabu.accounting.api.core.config_api import ConfigApi
            self._config = ConfigApi(self._http)
        return self._config
    @property
    def invoices(self) -> InvoiceApi:
        if self._invoices is None:
            from essabu.accounting.api.transactions.invoice_api import InvoiceApi
            self._invoices = InvoiceApi(self._http)
        return self._invoices
    @property
    def payments(self) -> PaymentApi:
        if self._payments is None:
            from essabu.accounting.api.transactions.payment_api import PaymentApi
            self._payments = PaymentApi(self._http)
        return self._payments
    @property
    def journals(self) -> JournalApi:
        if self._journals is None:
            from essabu.accounting.api.transactions.journal_api import JournalApi
            self._journals = JournalApi(self._http)
        return self._journals
    @property
    def journal_entries(self) -> JournalEntryApi:
        if self._journal_entries is None:
            from essabu.accounting.api.transactions.journal_entry_api import JournalEntryApi
            self._journal_entries = JournalEntryApi(self._http)
        return self._journal_entries
    @property
    def credit_notes(self) -> CreditNoteApi:
        if self._credit_notes is None:
            from essabu.accounting.api.transactions.credit_note_api import CreditNoteApi
            self._credit_notes = CreditNoteApi(self._http)
        return self._credit_notes
    @property
    def payment_terms(self) -> PaymentTermApi:
        if self._payment_terms is None:
            from essabu.accounting.api.transactions.payment_term_api import PaymentTermApi
            self._payment_terms = PaymentTermApi(self._http)
        return self._payment_terms
    @property
    def quotes(self) -> QuoteApi:
        if self._quotes is None:
            from essabu.accounting.api.transactions.quote_api import QuoteApi
            self._quotes = QuoteApi(self._http)
        return self._quotes
    @property
    def wallets(self) -> WalletApi:
        if self._wallets is None:
            from essabu.accounting.api.finance.wallet_api import WalletApi
            self._wallets = WalletApi(self._http)
        return self._wallets
    @property
    def wallet_transactions(self) -> WalletTransactionApi:
        if self._wallet_transactions is None:
            from essabu.accounting.api.finance.wallet_transaction_api import WalletTransactionApi
            self._wallet_transactions = WalletTransactionApi(self._http)
        return self._wallet_transactions
    @property
    def currencies(self) -> CurrencyApi:
        if self._currencies is None:
            from essabu.accounting.api.finance.currency_api import CurrencyApi
            self._currencies = CurrencyApi(self._http)
        return self._currencies
    @property
    def exchange_rates(self) -> ExchangeRateApi:
        if self._exchange_rates is None:
            from essabu.accounting.api.finance.exchange_rate_api import ExchangeRateApi
            self._exchange_rates = ExchangeRateApi(self._http)
        return self._exchange_rates
    @property
    def exchange_rate_providers(self) -> ExchangeRateProviderApi:
        if self._exchange_rate_providers is None:
            from essabu.accounting.api.finance.exchange_rate_provider_api import ExchangeRateProviderApi
            self._exchange_rate_providers = ExchangeRateProviderApi(self._http)
        return self._exchange_rate_providers
    @property
    def fiscal_years(self) -> FiscalYearApi:
        if self._fiscal_years is None:
            from essabu.accounting.api.finance.fiscal_year_api import FiscalYearApi
            self._fiscal_years = FiscalYearApi(self._http)
        return self._fiscal_years
    @property
    def periods(self) -> PeriodApi:
        if self._periods is None:
            from essabu.accounting.api.finance.period_api import PeriodApi
            self._periods = PeriodApi(self._http)
        return self._periods
    @property
    def tax_rates(self) -> TaxRateApi:
        if self._tax_rates is None:
            from essabu.accounting.api.finance.tax_rate_api import TaxRateApi
            self._tax_rates = TaxRateApi(self._http)
        return self._tax_rates
    @property
    def reports(self) -> ReportApi:
        if self._reports is None:
            from essabu.accounting.api.finance.report_api import ReportApi
            self._reports = ReportApi(self._http)
        return self._reports
    @property
    def inventory(self) -> InventoryApi:
        if self._inventory is None:
            from essabu.accounting.api.inventory.inventory_api import InventoryApi
            self._inventory = InventoryApi(self._http)
        return self._inventory
    @property
    def batches(self) -> BatchApi:
        if self._batches is None:
            from essabu.accounting.api.inventory.batch_api import BatchApi
            self._batches = BatchApi(self._http)
        return self._batches
    @property
    def purchase_orders(self) -> PurchaseOrderApi:
        if self._purchase_orders is None:
            from essabu.accounting.api.inventory.purchase_order_api import PurchaseOrderApi
            self._purchase_orders = PurchaseOrderApi(self._http)
        return self._purchase_orders
    @property
    def stock_counts(self) -> StockCountApi:
        if self._stock_counts is None:
            from essabu.accounting.api.inventory.stock_count_api import StockCountApi
            self._stock_counts = StockCountApi(self._http)
        return self._stock_counts
    @property
    def stock_locations(self) -> StockLocationApi:
        if self._stock_locations is None:
            from essabu.accounting.api.inventory.stock_location_api import StockLocationApi
            self._stock_locations = StockLocationApi(self._http)
        return self._stock_locations
    @property
    def stock_movements(self) -> StockMovementApi:
        if self._stock_movements is None:
            from essabu.accounting.api.inventory.stock_movement_api import StockMovementApi
            self._stock_movements = StockMovementApi(self._http)
        return self._stock_movements
    @property
    def suppliers(self) -> SupplierApi:
        if self._suppliers is None:
            from essabu.accounting.api.inventory.supplier_api import SupplierApi
            self._suppliers = SupplierApi(self._http)
        return self._suppliers
    @property
    def webhooks(self) -> WebhookApi:
        if self._webhooks is None:
            from essabu.accounting.api.inventory.webhook_api import WebhookApi
            self._webhooks = WebhookApi(self._http)
        return self._webhooks
    @property
    def insurance_claims(self) -> InsuranceClaimApi:
        if self._insurance_claims is None:
            from essabu.accounting.api.commercial.insurance_claim_api import InsuranceClaimApi
            self._insurance_claims = InsuranceClaimApi(self._http)
        return self._insurance_claims
    @property
    def insurance_contracts(self) -> InsuranceContractApi:
        if self._insurance_contracts is None:
            from essabu.accounting.api.commercial.insurance_contract_api import InsuranceContractApi
            self._insurance_contracts = InsuranceContractApi(self._http)
        return self._insurance_contracts
    @property
    def insurance_partners(self) -> InsurancePartnerApi:
        if self._insurance_partners is None:
            from essabu.accounting.api.commercial.insurance_partner_api import InsurancePartnerApi
            self._insurance_partners = InsurancePartnerApi(self._http)
        return self._insurance_partners
    @property
    def price_lists(self) -> PriceListApi:
        if self._price_lists is None:
            from essabu.accounting.api.commercial.price_list_api import PriceListApi
            self._price_lists = PriceListApi(self._http)
        return self._price_lists
    @property
    def price_list_overrides(self) -> PriceListOverrideApi:
        if self._price_list_overrides is None:
            from essabu.accounting.api.commercial.price_list_override_api import PriceListOverrideApi
            self._price_list_overrides = PriceListOverrideApi(self._http)
        return self._price_list_overrides
