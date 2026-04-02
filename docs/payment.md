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

All classes share these standard methods for paginated listing, creation, retrieval, update, and deletion. The `list` method returns a `PageResponse` with pagination metadata and supports keyword filter arguments such as `status` or `customer_id`. The `list_all` method returns a generator that fetches every page automatically. All write methods return the created or updated resource as a dictionary.

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## PaymentIntentApi Extra Methods

The `confirm` method finalizes the payment intent and triggers the actual charge or authorization on the payment method. The `cancel` method voids a payment intent that has not yet been captured. The `capture` method captures funds from a previously confirmed intent, accepting an optional `amount` for partial captures. All three methods require the payment intent `resource_id` and return the updated intent with its new status.

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

Create a payment intent and walk through its full lifecycle: creation, confirmation, capture, and cancellation. The `create` method requires `amount`, `currency`, `customer_id`, and `payment_method` (e.g., `"mobile_money"`, `"card"`, `"bank_transfer"`). An optional `description` provides context for the charge. After confirmation, the intent status changes to `"confirmed"`. Capturing settles the funds; cancellation voids the intent.

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

List and retrieve transaction records. Transactions are created automatically when payment intents are confirmed and captured. The `list` method supports filtering by `status` (e.g., `"completed"`, `"pending"`, `"failed"`) and returns paginated results. The `retrieve` method returns full transaction details including amount, currency, payment method, and timestamps.

```python
transactions = client.payment.transactions.list(status="completed", page_size=50)
txn = client.payment.transactions.retrieve("txn-uuid")
```

### Refunds

Create and track refunds against completed transactions. The `create` method requires `transaction_id`, `amount` (supports partial refunds), and `reason`. The refund is processed asynchronously; its status progresses from `"pending"` to `"completed"` or `"failed"`. Use the `list` method with a `transaction_id` filter to see all refunds associated with a specific transaction.

```python
refund = client.payment.refunds.create(
    transaction_id="txn-uuid",
    amount=2500,
    reason="Customer request",
)
refunds = client.payment.refunds.list(transaction_id="txn-uuid")
```

### Subscriptions

Create subscription plans and subscribe customers to recurring billing. The `subscription_plans.create` method defines a plan with `name`, `amount`, `currency`, and `interval` (e.g., `"month"`, `"year"`). The `subscriptions.create` method binds a customer to a plan with an optional `start_date`. Use the `list` method with a `status` filter to query active, paused, or cancelled subscriptions.

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

Define loan products and process loan applications. The `loan_products.create` method defines a product template with `name`, `max_amount`, `interest_rate`, and `term_months`. The `loan_applications.create` method submits a new application referencing a product and customer. Use `loan_repayments.list` with an `application_id` filter to retrieve the repayment schedule for a specific loan.

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

Create Know Your Customer profiles and upload identity documents for compliance verification. The `kyc_profiles.create` method registers a customer for KYC with a specified verification `level` (e.g., `"basic"`, `"enhanced"`). The `kyc_documents.create` method attaches an identity document to a profile, requiring `type` (e.g., `"national_id"`, `"passport"`), `document_number`, and `expiry_date`. Documents are validated asynchronously.

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

List and create financial accounts representing bank accounts, mobile money wallets, or other payment destinations. The `create` method requires `name`, `type` (e.g., `"bank"`, `"mobile_money"`), and account details such as `bank_name` and `account_number`. These accounts serve as targets for disbursements and sources for collections within the payment module.

```python
accounts = client.payment.financial_accounts.list()
account = client.payment.financial_accounts.create(
    name="Main Operating Account",
    type="bank",
    bank_name="Trust Bank",
    account_number="123456789",
)
```
