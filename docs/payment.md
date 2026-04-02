# Payment Module

Payment processing, financial accounts, loans, KYC, subscriptions, refunds, and transaction management.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `PaymentIntentApi` | `/api/payment/payment_intents` | Payment intents (authorize, capture) |
| `PaymentAccountApi` | `/api/payment/payment_accounts` | Payment account configuration |
| `FinancialAccountApi` | `/api/payment/financial_accounts` | Financial account management |
| `TransactionApi` | `/api/payment/transactions` | Transaction records |
| `RefundApi` | `/api/payment/refunds` | Refund processing |
| `SubscriptionApi` | `/api/payment/subscriptions` | Recurring subscriptions |
| `SubscriptionPlanApi` | `/api/payment/subscription_plans` | Subscription plan definitions |
| `LoanApplicationApi` | `/api/payment/loan_applications` | Loan applications |
| `LoanProductApi` | `/api/payment/loan_products` | Loan product catalog |
| `LoanRepaymentApi` | `/api/payment/loan_repayments` | Loan repayment schedules |
| `CollateralApi` | `/api/payment/collaterals` | Loan collaterals |
| `KycProfileApi` | `/api/payment/kyc_profiles` | KYC customer profiles |
| `KycDocumentApi` | `/api/payment/kyc_documents` | KYC identity documents |
| `ReportApi` | `/api/payment/reports` | Payment reports |

## Standard CRUD Methods

All classes share:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## PaymentIntentApi Extra Methods

```python
confirm(resource_id: str) -> dict[str, Any]
    # POST /api/payment/payment_intents/{id}/confirm

cancel(resource_id: str) -> dict[str, Any]
    # POST /api/payment/payment_intents/{id}/cancel

capture(resource_id: str, **data: Any) -> dict[str, Any]
    # POST /api/payment/payment_intents/{id}/capture
```

## Code Examples

### Payment Intents

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

# Create a payment intent
intent = client.payment.payment_intents.create(
    amount=5000,
    currency="USD",
    customer_id="cust-uuid",
    payment_method="mobile_money",
    description="Invoice #INV-001",
)

# Confirm the intent
confirmed = client.payment.payment_intents.confirm(intent["id"])

# Capture funds
captured = client.payment.payment_intents.capture(intent["id"], amount=5000)

# Cancel
client.payment.payment_intents.cancel(intent["id"])
```

### Transactions

```python
transactions = client.payment.transactions.list(status="completed", page_size=50)
txn = client.payment.transactions.retrieve("txn-uuid")
```

### Refunds

```python
refund = client.payment.refunds.create(
    transaction_id="txn-uuid",
    amount=2500,
    reason="Customer request",
)
refunds = client.payment.refunds.list(transaction_id="txn-uuid")
```

### Subscriptions

```python
plan = client.payment.subscription_plans.create(
    name="Pro Monthly",
    amount=29.99,
    currency="USD",
    interval="month",
)
subscription = client.payment.subscriptions.create(
    customer_id="cust-uuid",
    plan_id=plan["id"],
    start_date="2026-04-01",
)
subs = client.payment.subscriptions.list(status="active")
```

### Loans

```python
product = client.payment.loan_products.create(
    name="Micro-credit",
    max_amount=10000,
    interest_rate=5.0,
    term_months=12,
)
application = client.payment.loan_applications.create(
    customer_id="cust-uuid",
    product_id=product["id"],
    amount=5000,
    purpose="Working capital",
)
repayments = client.payment.loan_repayments.list(application_id=application["id"])
```

### KYC

```python
profile = client.payment.kyc_profiles.create(
    customer_id="cust-uuid",
    level="enhanced",
)
doc = client.payment.kyc_documents.create(
    profile_id=profile["id"],
    type="national_id",
    document_number="ID-123456",
    expiry_date="2030-12-31",
)
```

### Financial Accounts

```python
accounts = client.payment.financial_accounts.list()
account = client.payment.financial_accounts.create(
    name="Main Operating Account",
    type="bank",
    bank_name="Trust Bank",
    account_number="123456789",
)
```
