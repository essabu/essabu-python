# Modules Reference

The Essabu SDK provides access to 8 platform modules, each accessed via the main client as a lazy-loaded property.

## HR (`client.hr`)

Human Resources management.

| Resource        | Access                      | Description                     |
|-----------------|-----------------------------|---------------------------------|
| employees       | `client.hr.employees`       | Employee records                |
| contracts       | `client.hr.contracts`       | Employment contracts            |
| leaves          | `client.hr.leaves`          | Leave requests and balances     |
| payroll         | `client.hr.payroll`         | Payroll runs and pay slips      |
| shifts          | `client.hr.shifts`          | Shift assignments               |
| shift_schedules | `client.hr.shift_schedules` | Shift schedule templates        |
| recruitment     | `client.hr.recruitment`     | Job postings and applications   |
| performance     | `client.hr.performance`     | Performance reviews             |
| attendance      | `client.hr.attendance`      | Clock-in/out records            |
| benefits        | `client.hr.benefits`        | Employee benefits               |
| departments     | `client.hr.departments`     | Department management           |
| documents       | `client.hr.documents`       | Employee documents              |
| expenses        | `client.hr.expenses`        | Expense claims                  |
| loans           | `client.hr.loans`           | Employee loan advances          |
| onboarding      | `client.hr.onboarding`      | Onboarding workflows            |
| positions       | `client.hr.positions`       | Job positions                   |
| skills          | `client.hr.skills`          | Skill tracking                  |
| timesheets      | `client.hr.timesheets`      | Time tracking                   |
| training        | `client.hr.training`        | Training programs               |
| disciplinary    | `client.hr.disciplinary`    | Disciplinary actions            |
| history         | `client.hr.history`         | Employment history              |
| config          | `client.hr.config`          | HR module configuration         |
| reports         | `client.hr.reports`         | HR reports (headcount, turnover)|
| webhooks        | `client.hr.webhooks`        | Webhook subscriptions           |

## Accounting (`client.accounting`)

Full-featured accounting and financial management.

### Core
| Resource | Access | Description |
|----------|--------|-------------|
| accounts | `client.accounting.accounts` | Chart of accounts |
| balances | `client.accounting.balances` | Account balances |
| config   | `client.accounting.config`   | Accounting settings |

### Transactions
| Resource      | Access | Description |
|---------------|--------|-------------|
| invoices      | `client.accounting.invoices` | Sales invoices |
| payments      | `client.accounting.payments` | Payment records |
| journals      | `client.accounting.journals` | Journals |
| journal_entries | `client.accounting.journal_entries` | Journal entries |
| credit_notes  | `client.accounting.credit_notes` | Credit notes |
| payment_terms | `client.accounting.payment_terms` | Payment terms |
| quotes        | `client.accounting.quotes` | Quotations |

### Finance
| Resource | Access | Description |
|----------|--------|-------------|
| wallets | `client.accounting.wallets` | Digital wallets |
| wallet_transactions | `client.accounting.wallet_transactions` | Wallet transactions |
| currencies | `client.accounting.currencies` | Currency management |
| exchange_rates | `client.accounting.exchange_rates` | Exchange rates |
| exchange_rate_providers | `client.accounting.exchange_rate_providers` | Rate providers |
| fiscal_years | `client.accounting.fiscal_years` | Fiscal year periods |
| periods | `client.accounting.periods` | Accounting periods |
| tax_rates | `client.accounting.tax_rates` | Tax rates |
| reports | `client.accounting.reports` | Financial reports |

### Inventory
| Resource | Access | Description |
|----------|--------|-------------|
| inventory | `client.accounting.inventory` | Inventory items |
| batches | `client.accounting.batches` | Batch/lot tracking |
| purchase_orders | `client.accounting.purchase_orders` | Purchase orders |
| stock_counts | `client.accounting.stock_counts` | Stock counts |
| stock_locations | `client.accounting.stock_locations` | Warehouses/locations |
| stock_movements | `client.accounting.stock_movements` | Stock movements |
| suppliers | `client.accounting.suppliers` | Supplier records |
| webhooks | `client.accounting.webhooks` | Webhook subscriptions |

### Commercial
| Resource | Access | Description |
|----------|--------|-------------|
| insurance_claims | `client.accounting.insurance_claims` | Insurance claims |
| insurance_contracts | `client.accounting.insurance_contracts` | Insurance contracts |
| insurance_partners | `client.accounting.insurance_partners` | Insurance providers |
| price_lists | `client.accounting.price_lists` | Price lists |
| price_list_overrides | `client.accounting.price_list_overrides` | Price overrides |

## Identity (`client.identity`)

Authentication, authorization, and tenant management.

| Resource    | Access | Description |
|-------------|--------|-------------|
| auth        | `client.identity.auth` | Login, register, tokens |
| users       | `client.identity.users` | User accounts |
| roles       | `client.identity.roles` | Role management |
| tenants     | `client.identity.tenants` | Tenant management |
| branches    | `client.identity.branches` | Branch/location management |
| companies   | `client.identity.companies` | Company profiles |
| permissions | `client.identity.permissions` | Permission management |
| profiles    | `client.identity.profiles` | User profiles |
| sessions    | `client.identity.sessions` | Active sessions |
| api_keys    | `client.identity.api_keys` | API key management |

## Trade (`client.trade`)

CRM, sales, and supply chain management.

| Resource        | Access | Description |
|-----------------|--------|-------------|
| customers       | `client.trade.customers` | Customer records |
| contacts        | `client.trade.contacts` | Contact persons |
| opportunities   | `client.trade.opportunities` | Sales opportunities |
| products        | `client.trade.products` | Product catalog |
| sales_orders    | `client.trade.sales_orders` | Sales orders |
| purchase_orders | `client.trade.purchase_orders` | Purchase orders |
| deliveries      | `client.trade.deliveries` | Delivery tracking |
| suppliers       | `client.trade.suppliers` | Supplier management |
| campaigns       | `client.trade.campaigns` | Marketing campaigns |
| activities      | `client.trade.activities` | CRM activities |
| contracts       | `client.trade.contracts` | Trade contracts |
| documents       | `client.trade.documents` | Trade documents |
| inventory       | `client.trade.inventory` | Trade inventory |
| receipts        | `client.trade.receipts` | Goods receipts |
| stock           | `client.trade.stock` | Stock levels |
| warehouses      | `client.trade.warehouses` | Warehouse management |

## Payment (`client.payment`)

Payment processing, lending, and subscriptions.

| Resource           | Access | Description |
|--------------------|--------|-------------|
| payment_intents    | `client.payment.payment_intents` | Payment intents (confirm, cancel, capture) |
| payment_accounts   | `client.payment.payment_accounts` | Payment accounts |
| transactions       | `client.payment.transactions` | Transaction history |
| refunds            | `client.payment.refunds` | Refund management |
| subscriptions      | `client.payment.subscriptions` | Subscriptions (pause, resume, cancel) |
| subscription_plans | `client.payment.subscription_plans` | Subscription plans |
| loan_applications  | `client.payment.loan_applications` | Loan applications (approve, reject, disburse) |
| loan_products      | `client.payment.loan_products` | Loan product catalog |
| loan_repayments    | `client.payment.loan_repayments` | Loan repayments |
| collaterals        | `client.payment.collaterals` | Loan collaterals |
| financial_accounts | `client.payment.financial_accounts` | Financial accounts |
| kyc_documents      | `client.payment.kyc_documents` | KYC documents |
| kyc_profiles       | `client.payment.kyc_profiles` | KYC profiles |
| reports            | `client.payment.reports` | Payment reports |

## E-Invoice (`client.einvoice`)

Electronic invoicing and tax compliance.

| Resource     | Access | Description |
|--------------|--------|-------------|
| invoices     | `client.einvoice.invoices` | E-invoice records |
| submissions  | `client.einvoice.submissions` | Tax authority submissions (submit, check_status) |
| verification | `client.einvoice.verification` | Invoice verification (verify) |
| compliance   | `client.einvoice.compliance` | Compliance checks |
| statistics   | `client.einvoice.statistics` | E-invoicing statistics |

## Project (`client.project`)

Project and task management.

| Resource             | Access | Description |
|----------------------|--------|-------------|
| projects             | `client.project.projects` | Project records |
| tasks                | `client.project.tasks` | Task management |
| milestones           | `client.project.milestones` | Project milestones |
| resource_allocations | `client.project.resource_allocations` | Resource planning |
| task_comments        | `client.project.task_comments` | Task discussions |
| reports              | `client.project.reports` | Project reports |

## Asset (`client.asset`)

Fixed asset and fleet management.

| Resource              | Access | Description |
|-----------------------|--------|-------------|
| assets                | `client.asset.assets` | Fixed assets |
| vehicles              | `client.asset.vehicles` | Vehicle fleet |
| depreciations         | `client.asset.depreciations` | Depreciation schedules |
| fuel_logs             | `client.asset.fuel_logs` | Fuel consumption logs |
| maintenance_logs      | `client.asset.maintenance_logs` | Maintenance records |
| maintenance_schedules | `client.asset.maintenance_schedules` | Scheduled maintenance |
| trip_logs             | `client.asset.trip_logs` | Vehicle trip logs |

## Common API Pattern

Every resource supports the standard CRUD operations. The `list` method returns a paginated `PageResponse` with `data`, `total`, `page`, and navigation helpers. The `list_all` method returns a generator that fetches every page automatically. The `create` and `update` methods accept keyword arguments matching the API resource fields. The `delete` method performs a soft delete and returns a confirmation dictionary.

```python
# List (paginated)
page = client.module.resource.list(page=1, page_size=25, status="active")

# List all (iterator)
for page in client.module.resource.list_all(page_size=100):
    for item in page.data:
        process(item)

# Create
item = client.module.resource.create(field1="value1", field2="value2")

# Retrieve
item = client.module.resource.retrieve("resource-id")

# Update
item = client.module.resource.update("resource-id", field1="new-value")

# Delete
client.module.resource.delete("resource-id")
```
