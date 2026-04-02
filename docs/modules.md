# Module Reference

## HR (`client.hr`)

| Resource | Access | Operations |
|----------|--------|------------|
| Employees | `client.hr.employees` | create, get, list, update, delete, get_leave_balances, get_history, get_documents, get_org_tree, get_org_chart |
| Departments | `client.hr.departments` | create, get, list, update, delete |
| Positions | `client.hr.positions` | create, get, list, update, delete |
| Contracts | `client.hr.contracts` | create, get, list, update, delete, terminate |
| Attendance | `client.hr.attendances` | record, clock_in, clock_out, list, summary |
| Leaves | `client.hr.leaves` | create, get, list, approve, reject, cancel, types, balances |
| Shifts | `client.hr.shifts` | create, get, list, update, delete |
| Shift Schedules | `client.hr.shift_schedules` | create, get, list, update, delete, assign |
| Training | `client.hr.trainings` | create, get, list, update, delete |
| Payroll | `client.hr.payrolls` | create, get, list, calculate, finalize |
| Expenses | `client.hr.expenses` | create, get, list, approve, reject |
| Recruitment | `client.hr.recruitment` | create, get, list, update, delete |
| Performance | `client.hr.performance` | create, get, list, update, delete |
| Onboarding | `client.hr.onboarding` | create, get, list, update, delete |
| Documents | `client.hr.documents` | create, get, list, update, delete, download |
| Disciplinary | `client.hr.disciplinary` | create, get, list, update, delete |
| Benefits | `client.hr.benefits` | create, get, list, update, delete |
| Loans | `client.hr.loans` | create, get, list, update, delete, approve, reject |
| Timesheets | `client.hr.timesheets` | create, get, list, update, delete, approve |
| Skills | `client.hr.skills` | create, get, list, update, delete |
| Reports | `client.hr.reports` | generate, get, list |
| Webhooks | `client.hr.webhooks` | create, get, list, update, delete |
| Config | `client.hr.config` | get, update |
| History | `client.hr.history` | list |

## Accounting (`client.accounting`)

| Resource | Access |
|----------|--------|
| Accounts | `client.accounting.accounts` |
| Balances | `client.accounting.balances` |
| Config | `client.accounting.config` |
| Journals | `client.accounting.journals` |
| Journal Entries | `client.accounting.journal_entries` |
| Invoices | `client.accounting.invoices` |
| Quotes | `client.accounting.quotes` |
| Credit Notes | `client.accounting.credit_notes` |
| Payments | `client.accounting.payments` |
| Payment Terms | `client.accounting.payment_terms` |
| Tax Rates | `client.accounting.tax_rates` |
| Currencies | `client.accounting.currencies` |
| Exchange Rates | `client.accounting.exchange_rates` |
| Exchange Rate Providers | `client.accounting.exchange_rate_providers` |
| Fiscal Years | `client.accounting.fiscal_years` |
| Periods | `client.accounting.periods` |
| Reports | `client.accounting.reports` |
| Wallets | `client.accounting.wallets` |
| Wallet Transactions | `client.accounting.wallet_transactions` |
| Insurance Partners | `client.accounting.insurance_partners` |
| Insurance Contracts | `client.accounting.insurance_contracts` |
| Insurance Claims | `client.accounting.insurance_claims` |
| Price Lists | `client.accounting.price_lists` |
| Price List Overrides | `client.accounting.price_list_overrides` |
| Suppliers | `client.accounting.suppliers` |
| Inventory | `client.accounting.inventory` |
| Purchase Orders | `client.accounting.purchase_orders` |
| Batches | `client.accounting.batches` |
| Stock Movements | `client.accounting.stock_movements` |
| Stock Counts | `client.accounting.stock_counts` |
| Stock Locations | `client.accounting.stock_locations` |
| Webhooks | `client.accounting.webhooks` |

## Identity (`client.identity`)

| Resource | Access |
|----------|--------|
| Auth | `client.identity.auth` |
| Users | `client.identity.users` |
| Profiles | `client.identity.profiles` |
| Companies | `client.identity.companies` |
| Tenants | `client.identity.tenants` |
| Roles | `client.identity.roles` |
| Permissions | `client.identity.permissions` |
| Branches | `client.identity.branches` |
| API Keys | `client.identity.api_keys` |
| Sessions | `client.identity.sessions` |

## Trade (`client.trade`)

| Resource | Access |
|----------|--------|
| Customers | `client.trade.customers` |
| Products | `client.trade.products` |
| Sales Orders | `client.trade.sales_orders` |
| Purchase Orders | `client.trade.purchase_orders` |
| Deliveries | `client.trade.deliveries` |
| Receipts | `client.trade.receipts` |
| Suppliers | `client.trade.suppliers` |
| Inventory | `client.trade.inventory` |
| Stock | `client.trade.stock` |
| Warehouses | `client.trade.warehouses` |
| Contacts | `client.trade.contacts` |
| Opportunities | `client.trade.opportunities` |
| Activities | `client.trade.activities` |
| Campaigns | `client.trade.campaigns` |
| Contracts | `client.trade.contracts` |
| Documents | `client.trade.documents` |

## Payment (`client.payment`)

| Resource | Access |
|----------|--------|
| Payment Intents | `client.payment.payment_intents` |
| Payment Accounts | `client.payment.payment_accounts` |
| Transactions | `client.payment.transactions` |
| Refunds | `client.payment.refunds` |
| Subscriptions | `client.payment.subscriptions` |
| Subscription Plans | `client.payment.subscription_plans` |
| Financial Accounts | `client.payment.financial_accounts` |
| Loan Products | `client.payment.loan_products` |
| Loan Applications | `client.payment.loan_applications` |
| Loan Repayments | `client.payment.loan_repayments` |
| Collaterals | `client.payment.collaterals` |
| KYC Profiles | `client.payment.kyc_profiles` |
| KYC Documents | `client.payment.kyc_documents` |
| Reports | `client.payment.reports` |

## EInvoice (`client.einvoice`)

| Resource | Access |
|----------|--------|
| Invoices | `client.einvoice.invoices` |
| Submissions | `client.einvoice.submissions` |
| Verification | `client.einvoice.verification` |
| Compliance | `client.einvoice.compliance` |
| Statistics | `client.einvoice.statistics` |

## Project (`client.project`)

| Resource | Access |
|----------|--------|
| Projects | `client.project.projects` |
| Milestones | `client.project.milestones` |
| Tasks | `client.project.tasks` |
| Task Comments | `client.project.task_comments` |
| Resource Allocations | `client.project.resource_allocations` |
| Reports | `client.project.reports` |

## Asset (`client.asset`)

| Resource | Access |
|----------|--------|
| Assets | `client.asset.assets` |
| Depreciations | `client.asset.depreciations` |
| Maintenance Schedules | `client.asset.maintenance_schedules` |
| Maintenance Logs | `client.asset.maintenance_logs` |
| Vehicles | `client.asset.vehicles` |
| Fuel Logs | `client.asset.fuel_logs` |
| Trip Logs | `client.asset.trip_logs` |
