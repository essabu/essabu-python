# Essabu Python SDK

[![PyPI Version](https://img.shields.io/pypi/v/essabu?style=flat-square)](https://pypi.org/project/essabu/)
[![Python Versions](https://img.shields.io/pypi/pyversions/essabu?style=flat-square)](https://pypi.org/project/essabu/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/essabu/essabu-python/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/essabu/essabu-python/actions)

The official Python SDK for the [Essabu](https://essabu.com) platform -- a unified SaaS solution for billing, accounting, HR, CRM, payments, project management, asset tracking, and electronic invoicing. This SDK gives you a single, consistent Pythonic interface to all eight platform modules, complete with pagination helpers, a rich exception hierarchy, automatic retries, and environment-variable-based configuration.

---

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Modules](#modules)
  - [HR](#hr)
  - [Accounting](#accounting)
  - [Identity](#identity)
  - [Trade / CRM](#trade--crm)
  - [Payment](#payment)
  - [E-Invoice](#e-invoice)
  - [Project](#project)
  - [Asset](#asset)
- [Pagination](#pagination)
- [Error Handling](#error-handling)
- [Async Support](#async-support)
- [Webhooks](#webhooks)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

```bash
# pip
pip install essabu

# poetry
poetry add essabu

# pipenv
pipenv install essabu
```

**Requirements:** Python 3.10+ | Dependencies: `httpx`, `pydantic`

---

## Quick Start

```python
from essabu import Essabu

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# HR -- Create an employee
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Mukendi",
    email="jean.mukendi@example.com",
    department_id="dept-001",
)
print(employee)

# Accounting -- Create an invoice
invoice = client.accounting.invoices.create(
    customer_id="cust-001",
    items=[{"description": "Consulting", "quantity": 10, "unit_price": "150.00"}],
    currency="USD",
)

# Trade / CRM -- List customers with pagination
customers = client.trade.customers.list(page=1, page_size=25)
for c in customers.data:
    print(c["name"])

# Payments -- Create a payment intent
intent = client.payment.payment_intents.create(
    amount="500.00",
    currency="USD",
    payment_method="mobile_money",
)

# E-Invoice -- Submit to tax authority
einvoice = client.einvoice.invoices.create(
    invoice_id="inv-uuid",
    customer_tin="123456789",
    customer_name="ACME Corp",
    items=[{"description": "Service", "quantity": 1, "unit_price": 500, "tax_rate": 16}],
    currency="CDF",
)

# Project -- Create a project
project = client.project.projects.create(
    name="Website Redesign",
    start_date="2026-04-01",
    end_date="2026-09-30",
    budget=50000,
    currency="USD",
)

# Asset -- Register a fixed asset
asset = client.asset.assets.create(
    name="Dell PowerEdge R750",
    category="IT Equipment",
    purchase_price=8500,
    currency="USD",
    depreciation_method="straight_line",
)

# Identity -- Manage users and roles
users = client.identity.users.list(page_size=20)

# Always close when done (or use a context manager)
client.close()
```

### Context Manager

```python
with Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id") as client:
    employees = client.hr.employees.list()
    # client is automatically closed when the block exits
```

---

## Configuration

### Explicit Parameters

```python
from essabu import Essabu

client = Essabu(
    api_key="esa_live_xxx",
    tenant_id="your-tenant-id",
    base_url="https://api.essabu.com",
    timeout=30.0,
    max_retries=3,
)
```

### Environment Variables

```bash
export ESSABU_API_KEY=esa_live_your_api_key
export ESSABU_TENANT_ID=your-tenant-id
export ESSABU_BASE_URL=https://api.essabu.com   # optional
export ESSABU_TIMEOUT=30.0                       # optional
export ESSABU_MAX_RETRIES=3                      # optional
```

```python
client = Essabu()  # reads all values from environment
```

### Configuration Reference

| Parameter     | Env Variable         | Default                  | Description               |
|---------------|----------------------|--------------------------|---------------------------|
| `api_key`     | `ESSABU_API_KEY`     | --                       | API key (required)        |
| `tenant_id`   | `ESSABU_TENANT_ID`   | --                       | Tenant ID (required)      |
| `base_url`    | `ESSABU_BASE_URL`    | `https://api.essabu.com` | API base URL              |
| `timeout`     | `ESSABU_TIMEOUT`     | `30.0`                   | Request timeout (seconds) |
| `max_retries` | `ESSABU_MAX_RETRIES` | `3`                      | Max retry attempts        |

---

## Modules

All modules are accessible via dot notation on the client. They are lazy-loaded -- only initialized when first accessed.

### HR

Employees, departments, contracts, payroll, attendance, leaves, benefits, loans, expenses, performance reviews, recruitment, training, onboarding, shifts, timesheets, and more.

```python
# Employee management
employees = client.hr.employees.list(page_size=50, department="engineering")
employee = client.hr.employees.create(first_name="Jean", last_name="Dupont", email="jean@co.com")
client.hr.employees.update("emp-id", salary=55000)

# Payroll
run = client.hr.payroll.create(period="2026-03", department_id="dept-uuid")

# Leave management
leave = client.hr.leaves.create(employee_id="emp-id", type="annual", start_date="2026-04-01", end_date="2026-04-05")

# Reports
headcount = client.hr.reports.headcount(year=2026)
```

> **Full reference:** [HR Module Wiki](https://github.com/essabu/essabu-python/wiki/HR-Module)

### Accounting

Chart of accounts, journal entries, invoices, payments, credit notes, quotes, fiscal years, currencies, exchange rates, tax rates, wallets, inventory, insurance, price lists, and financial reports.

```python
# Chart of accounts
account = client.accounting.accounts.create(code="4010", name="Sales", type="revenue")

# Journal entries
entry = client.accounting.journal_entries.create(
    journal_id="jnl-uuid", date="2026-03-26", reference="JV-001",
    lines=[{"account_id": "acc-1", "debit": 1000, "credit": 0}, {"account_id": "acc-2", "debit": 0, "credit": 1000}],
)

# Financial reports
bs = client.accounting.reports.balance_sheet(date="2026-03-31")
pnl = client.accounting.reports.income_statement(start_date="2026-01-01", end_date="2026-03-31")
```

> **Full reference:** [Accounting Module Wiki](https://github.com/essabu/essabu-python/wiki/Accounting-Module)

### Identity

Authentication, users, roles, permissions, tenants, companies, branches, profiles, sessions, and API key management.

```python
# Login
tokens = client.identity.auth.login(email="admin@co.com", password="secret")

# User management
user = client.identity.users.create(email="new@co.com", first_name="Alice", last_name="Martin")

# Roles
role = client.identity.roles.create(name="Accountant", permissions=["accounting.read", "accounting.write"])
```

> **Full reference:** [Identity Module Wiki](https://github.com/essabu/essabu-python/wiki/Identity-Module)

### Trade / CRM

Customers, contacts, opportunities, sales orders, purchase orders, products, suppliers, deliveries, contracts, campaigns, activities, warehouses, stock, and receipts.

```python
# Customers
customer = client.trade.customers.create(name="ACME Corp", email="contact@acme.com")

# Sales pipeline
deal = client.trade.opportunities.create(
    title="Enterprise Deal", customer_id="cust-uuid", value=50000, stage="qualification",
)

# Orders
order = client.trade.sales_orders.create(
    customer_id="cust-uuid",
    lines=[{"product_id": "prod-uuid", "quantity": 10, "unit_price": 25}],
)
```

> **Full reference:** [Trade Module Wiki](https://github.com/essabu/essabu-python/wiki/Trade-Module)

### Payment

Payment intents, transactions, refunds, subscriptions, loan applications and products, KYC, financial accounts, and payment reports.

```python
# Payment intent lifecycle
intent = client.payment.payment_intents.create(amount=5000, currency="USD", payment_method="mobile_money")
client.payment.payment_intents.confirm(intent["id"])
client.payment.payment_intents.capture(intent["id"], amount=5000)

# Subscriptions
plan = client.payment.subscription_plans.create(name="Pro", amount=29.99, interval="month")
sub = client.payment.subscriptions.create(customer_id="cust-uuid", plan_id=plan["id"])

# Loans
app = client.payment.loan_applications.create(customer_id="cust-uuid", amount=5000, purpose="Working capital")
```

> **Full reference:** [Payment Module Wiki](https://github.com/essabu/essabu-python/wiki/Payment-Module)

### E-Invoice

Electronic invoices, tax authority submissions, verification, compliance records, and statistics.

```python
# Create and submit
einvoice = client.einvoice.invoices.create(invoice_id="inv-uuid", customer_tin="123456789", ...)
submission = client.einvoice.submissions.create(invoice_id=einvoice["id"], authority="OBR")
result = client.einvoice.submissions.submit(submission["id"])
status = client.einvoice.submissions.check_status(submission["id"])

# Verify
verification = client.einvoice.verification.verify(qr_code="https://tax.gov/verify/ABC123")
```

> **Full reference:** [E-Invoice Module Wiki](https://github.com/essabu/essabu-python/wiki/EInvoice-Module)

### Project

Projects, tasks, milestones, resource allocations, task comments, and project reports.

```python
project = client.project.projects.create(name="Website Redesign", start_date="2026-04-01", end_date="2026-09-30")
task = client.project.tasks.create(project_id=project["id"], title="Design mockups", priority="high")
milestone = client.project.milestones.create(project_id=project["id"], name="Phase 1 Complete", due_date="2026-05-01")
```

> **Full reference:** [Project Module Wiki](https://github.com/essabu/essabu-python/wiki/Project-Module)

### Asset

Fixed assets, vehicles, depreciation, maintenance schedules and logs, fuel logs, and trip logs.

```python
asset = client.asset.assets.create(name="Server", category="IT", purchase_price=8500, depreciation_method="straight_line")
vehicle = client.asset.vehicles.create(make="Toyota", model="Hilux", year=2025, license_plate="KIN-1234-AB")
fuel = client.asset.fuel_logs.create(vehicle_id=vehicle["id"], liters=60.5, cost_per_liter=1.85)
trip = client.asset.trip_logs.create(vehicle_id=vehicle["id"], origin="Kinshasa", destination="Matadi")
```

> **Full reference:** [Asset Module Wiki](https://github.com/essabu/essabu-python/wiki/Asset-Module)

---

## Pagination

All `list()` methods return a `PageResponse` object with pagination metadata.

### Manual Pagination

```python
page = client.hr.employees.list(page=1, page_size=50)

print(f"Page {page.page}/{page.total_pages} | Total: {page.total}")

for employee in page.data:
    print(employee["first_name"])

# Check for next page
if page.has_next:
    next_page = client.hr.employees.list(page=page.page + 1, page_size=50)
```

### Automatic Iteration

```python
for page in client.hr.employees.list_all(page_size=100):
    for employee in page.data:
        print(employee["email"])
```

### Collecting All Results

```python
all_employees = []
for page in client.hr.employees.list_all(page_size=100):
    all_employees.extend(page.data)
```

### PageResponse Properties

| Property       | Type         | Description                   |
|----------------|-------------|-------------------------------|
| `data`         | `list[dict]` | Items on the current page     |
| `total`        | `int`        | Total number of items         |
| `page`         | `int`        | Current page number           |
| `page_size`    | `int`        | Items per page                |
| `total_pages`  | `int`        | Total number of pages         |
| `has_next`     | `bool`       | Whether a next page exists    |
| `has_previous` | `bool`       | Whether a previous page exists|

---

## Error Handling

The SDK provides a rich exception hierarchy. All exceptions inherit from `EssabuError`.

```python
from essabu.common.exceptions import (
    EssabuError,
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    ConflictError,
    ValidationError,
    RateLimitError,
    ServerError,
)

try:
    employee = client.hr.employees.retrieve("nonexistent-id")
except NotFoundError as e:
    print(f"Not found: {e.message}")
except ValidationError as e:
    for err in e.errors:
        print(f"Field error: {err}")
except AuthenticationError:
    print("Invalid API key")
except AuthorizationError:
    print("Insufficient permissions")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
except ServerError as e:
    print(f"Server error ({e.status_code})")
except EssabuError as e:
    print(f"API error: {e.status_code} - {e.message}")
```

### Exception Hierarchy

| Exception             | HTTP Status | Description                  |
|-----------------------|-------------|------------------------------|
| `EssabuError`         | any         | Base exception               |
| `AuthenticationError` | 401         | Invalid API key / token      |
| `AuthorizationError`  | 403         | Insufficient permissions     |
| `NotFoundError`       | 404         | Resource not found           |
| `ConflictError`       | 409         | Resource conflict            |
| `ValidationError`     | 422         | Request validation failed    |
| `RateLimitError`      | 429         | Rate limit exceeded          |
| `ServerError`         | 5xx         | Server-side error            |

---

## Async Support

The SDK is built on `httpx`, which provides both sync and async HTTP clients. The default client uses synchronous operations. For async usage, the underlying `httpx.AsyncClient` can be leveraged:

```python
import asyncio
from essabu import Essabu

async def main():
    client = Essabu(api_key="esa_live_xxx", tenant_id="tenant-id")
    employees = client.hr.employees.list(page_size=10)
    print(f"Found {employees.total} employees")
    client.close()

asyncio.run(main())
```

---

## Webhooks

Essabu sends webhook events signed with HMAC-SHA256. Verify the `X-Essabu-Signature` header before processing.

```python
import hashlib
import hmac
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = "whsec_your_webhook_secret"

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)

@app.route("/webhooks/essabu", methods=["POST"])
def handle_webhook():
    payload = request.get_data()
    signature = request.headers.get("X-Essabu-Signature", "")

    if not verify_signature(payload, signature, WEBHOOK_SECRET):
        return jsonify({"error": "Invalid signature"}), 401

    event = json.loads(payload)

    if event["type"] == "invoice.created":
        print(f"New invoice: {event['data']['id']}")
    elif event["type"] == "payment.succeeded":
        print(f"Payment: {event['data']['amount']}")

    return jsonify({"received": True}), 200
```

> **Full reference:** [Webhooks Wiki](https://github.com/essabu/essabu-python/wiki/Webhooks)

---

## Examples

Complete examples are in the [`examples/`](examples/) directory.

| Example | Description | Module |
|---------|-------------|--------|
| [`authentication.py`](examples/authentication.py) | Login, token refresh, password reset | Identity |
| [`create_employee.py`](examples/create_employee.py) | Employee creation and management | HR |
| [`create_invoice.py`](examples/create_invoice.py) | Invoice creation and payment | Accounting |
| [`crm_pipeline.py`](examples/crm_pipeline.py) | CRM pipeline workflow | Trade |
| [`einvoice_submit.py`](examples/einvoice_submit.py) | E-invoice submission | E-Invoice |
| [`loan_application.py`](examples/loan_application.py) | Loan application workflow | Payment |
| [`process_payment.py`](examples/process_payment.py) | Payment intent lifecycle | Payment |
| [`webhook_handler.py`](examples/webhook_handler.py) | Webhook handler with Flask | Webhooks |

```bash
# Run an example
export ESSABU_API_KEY=esa_test_xxx
export ESSABU_TENANT_ID=your-tenant-id
python examples/create_employee.py
```

---

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`pytest`)
5. Ensure type checks pass (`mypy essabu/`)
6. Ensure linting passes (`ruff check essabu/`)
7. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
8. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/essabu/essabu-python.git
cd essabu-python

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Type checking
mypy essabu/

# Linting
ruff check essabu/

# Formatting
black essabu/
```

---

## License

This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.

---

**[Wiki](https://github.com/essabu/essabu-python/wiki)** | **[API Docs](https://docs.essabu.com/sdk/python)** | **[Changelog](CHANGELOG.md)** | **[Issues](https://github.com/essabu/essabu-python/issues)**
