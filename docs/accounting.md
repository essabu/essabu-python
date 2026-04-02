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

All resource classes share these methods. The `list` method returns a `PageResponse` with pagination metadata. The `list_all` method returns a generator that automatically fetches all pages. The `create` and `update` methods accept keyword arguments matching the resource fields. The `delete` method performs a soft delete and returns a confirmation dictionary.

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## ReportApi Extra Methods

The `ReportApi` provides specialized methods for generating standard financial statements. Each method accepts keyword arguments for date ranges and filtering criteria. The `balance_sheet` method requires a `date` parameter. The `income_statement`, `trial_balance`, and `cash_flow` methods accept `start_date` and `end_date` to define the reporting period. All methods return a dictionary containing the structured report data.

```python
balance_sheet(**params: Any) -> dict[str, Any]       # GET /api/accounting/reports/balance-sheet
income_statement(**params: Any) -> dict[str, Any]    # GET /api/accounting/reports/income-statement
trial_balance(**params: Any) -> dict[str, Any]       # GET /api/accounting/reports/trial-balance
cash_flow(**params: Any) -> dict[str, Any]           # GET /api/accounting/reports/cash-flow
```

## Code Examples

### Chart of Accounts

List, create, and update accounts in the chart of accounts. The `create` method requires `code` (unique account number), `name`, `type` (one of `"asset"`, `"liability"`, `"equity"`, `"revenue"`, `"expense"`), and `currency`. Returns the created account with its generated `id`. Throws `ConflictError` if the account code already exists.

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

Create a double-entry journal entry with balanced debit and credit lines. The `journal_id` references the target journal, `date` is the posting date, and `reference` is a human-readable identifier. The `lines` list must contain at least two entries where total debits equal total credits. Throws `ValidationError` if the entry is unbalanced or references invalid account IDs.

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

Create a sales invoice and record a payment against it. The invoice `create` method requires `customer_id`, `due_date`, and a list of line items with `description`, `quantity`, and `unit_price`. The payment `create` method links the payment to the invoice via `invoice_id` and records the `amount`, `method`, and `date`. Partial payments are supported; the invoice status updates automatically based on total payments received.

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

Generate standard financial reports for a given date or period. The `balance_sheet` method provides a snapshot of assets, liabilities, and equity at a specific date. The `income_statement` summarizes revenue and expenses over a date range. The `trial_balance` lists all account balances, and the `cash_flow` report tracks cash inflows and outflows. All methods return structured dictionaries with categorized line items and totals.

```python
bs = client.accounting.reports.balance_sheet(date="2026-03-31")
pnl = client.accounting.reports.income_statement(start_date="2026-01-01", end_date="2026-03-31")
tb = client.accounting.reports.trial_balance(date="2026-03-31")
cf = client.accounting.reports.cash_flow(start_date="2026-01-01", end_date="2026-03-31")
```

### Wallets

List, create, and query digital wallets and their transactions. A wallet is a virtual account used for internal fund tracking. The `create` method requires a `name` and `currency`. Use `wallet_transactions.list` with a `wallet_id` filter to retrieve the transaction history for a specific wallet. Each transaction includes amount, type (credit/debit), and timestamp.

```python
wallets = client.accounting.wallets.list()
wallet = client.accounting.wallets.create(name="Main Wallet", currency="USD")
txns = client.accounting.wallet_transactions.list(wallet_id="wallet-uuid")
```

### Fiscal Years

Create and manage fiscal year periods. The `create` method requires a `name`, `start_date`, and `end_date` defining the fiscal year boundaries. Only one fiscal year can be active at a time. Closing a fiscal year generates closing entries and prevents further postings to that period. Throws `ConflictError` if the date range overlaps with an existing fiscal year.

```python
fy = client.accounting.fiscal_years.create(
    name="FY 2026",
    start_date="2026-01-01",
    end_date="2026-12-31",
)
```
