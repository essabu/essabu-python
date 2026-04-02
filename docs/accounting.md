# Accounting Module

Full accounting suite: chart of accounts, journal entries, invoices, payments, wallets, currencies, fiscal years, and financial reports.

## Available Classes

### Core

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `AccountApi` | `/api/accounting/accounts` | Chart of accounts |
| `BalanceApi` | `/api/accounting/balances` | Account balances |
| `ConfigApi` | `/api/accounting/config` | Accounting configuration |

### Transactions

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `InvoiceApi` | `/api/accounting/invoices` | Sales and purchase invoices |
| `PaymentApi` | `/api/accounting/payments` | Payment records |
| `JournalApi` | `/api/accounting/journals` | Accounting journals |
| `JournalEntryApi` | `/api/accounting/journal_entries` | Journal entries |
| `CreditNoteApi` | `/api/accounting/credit_notes` | Credit notes |
| `QuoteApi` | `/api/accounting/quotes` | Quotations |
| `PaymentTermApi` | `/api/accounting/payment_terms` | Payment terms |

### Finance

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `CurrencyApi` | `/api/accounting/currencies` | Currency management |
| `ExchangeRateApi` | `/api/accounting/exchange_rates` | Exchange rates |
| `ExchangeRateProviderApi` | `/api/accounting/exchange_rate_providers` | Rate providers |
| `FiscalYearApi` | `/api/accounting/fiscal_years` | Fiscal years |
| `PeriodApi` | `/api/accounting/periods` | Accounting periods |
| `TaxRateApi` | `/api/accounting/tax_rates` | Tax rates |
| `WalletApi` | `/api/accounting/wallets` | Digital wallets |
| `WalletTransactionApi` | `/api/accounting/wallet_transactions` | Wallet transactions |
| `ReportApi` | `/api/accounting/reports` | Financial reports |

### Inventory

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `InventoryApi` | `/api/accounting/inventory` | Inventory items |
| `BatchApi` | `/api/accounting/batches` | Inventory batches |
| `PurchaseOrderApi` | `/api/accounting/purchase_orders` | Purchase orders |
| `StockCountApi` | `/api/accounting/stock_counts` | Stock counts |
| `StockLocationApi` | `/api/accounting/stock_locations` | Stock locations |
| `StockMovementApi` | `/api/accounting/stock_movements` | Stock movements |
| `SupplierApi` | `/api/accounting/suppliers` | Supplier management |
| `WebhookApi` | `/api/accounting/webhooks` | Accounting webhooks |

### Commercial

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `InsuranceClaimApi` | `/api/accounting/insurance_claims` | Insurance claims |
| `InsuranceContractApi` | `/api/accounting/insurance_contracts` | Insurance contracts |
| `InsurancePartnerApi` | `/api/accounting/insurance_partners` | Insurance partners |
| `PriceListApi` | `/api/accounting/price_lists` | Price lists |
| `PriceListOverrideApi` | `/api/accounting/price_list_overrides` | Price list overrides |

## Standard CRUD Methods

All resource classes share these methods:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## ReportApi Extra Methods

```python
balance_sheet(**params: Any) -> dict[str, Any]       # GET /api/accounting/reports/balance-sheet
income_statement(**params: Any) -> dict[str, Any]    # GET /api/accounting/reports/income-statement
trial_balance(**params: Any) -> dict[str, Any]       # GET /api/accounting/reports/trial-balance
cash_flow(**params: Any) -> dict[str, Any]           # GET /api/accounting/reports/cash-flow
```

## Code Examples

### Chart of Accounts

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

accounts = client.accounting.accounts.list(page_size=50)
account = client.accounting.accounts.create(
    code="4010",
    name="Ventes de marchandises",
    type="revenue",
    currency="USD",
)
client.accounting.accounts.update("acc-uuid", name="Updated Name")
```

### Journal Entries

```python
entry = client.accounting.journal_entries.create(
    journal_id="journal-uuid",
    date="2026-03-26",
    reference="JV-001",
    lines=[
        {"account_id": "acc-debit", "debit": 1000, "credit": 0},
        {"account_id": "acc-credit", "debit": 0, "credit": 1000},
    ],
)
```

### Invoices and Payments

```python
invoice = client.accounting.invoices.create(
    customer_id="cust-uuid",
    due_date="2026-04-30",
    lines=[{"description": "Service", "quantity": 1, "unit_price": 500}],
)
payment = client.accounting.payments.create(
    invoice_id=invoice["id"],
    amount=500,
    method="bank_transfer",
    date="2026-03-26",
)
```

### Financial Reports

```python
bs = client.accounting.reports.balance_sheet(date="2026-03-31")
pnl = client.accounting.reports.income_statement(start_date="2026-01-01", end_date="2026-03-31")
tb = client.accounting.reports.trial_balance(date="2026-03-31")
cf = client.accounting.reports.cash_flow(start_date="2026-01-01", end_date="2026-03-31")
```

### Wallets

```python
wallets = client.accounting.wallets.list()
wallet = client.accounting.wallets.create(name="Main Wallet", currency="USD")
txns = client.accounting.wallet_transactions.list(wallet_id="wallet-uuid")
```

### Fiscal Years

```python
fy = client.accounting.fiscal_years.create(
    name="FY 2026",
    start_date="2026-01-01",
    end_date="2026-12-31",
)
```
