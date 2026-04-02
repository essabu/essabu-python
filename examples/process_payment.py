"""Example: Process payments via the Payment module.

Demonstrates the payment intent lifecycle: creating an intent with amount,
currency, and payment method, confirming it to trigger the charge, and listing
recent transactions. Includes error handling for validation and API errors.
"""

from essabu import Essabu
from essabu.common.exceptions import EssabuError, ValidationError

# Initialize the client for payment processing operations.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create a payment intent representing the intention to collect a payment. Required
    # fields are amount, currency, payment_method (e.g., "mobile_money", "card",
    # "bank_transfer"), and customer_id. Optional fields include description and metadata
    # (a dictionary for storing custom key-value pairs like order_id). The intent is created
    # in "requires_confirmation" status. Raises ValidationError for invalid amounts or methods.
    intent = client.payment.payment_intents.create(
        amount="250.00",
        currency="USD",
        payment_method="mobile_money",
        customer_id="cust-001",
        description="Monthly subscription payment",
        metadata={"order_id": "ord-123"},
    )
    print(f"Payment intent created: {intent['id']} - Status: {intent['status']}")

    # Confirm the payment intent to trigger the actual charge on the payment method.
    # This transitions the intent status from "requires_confirmation" to "confirmed"
    # (or "failed" if the charge is declined). Returns the updated intent with its
    # new status. For mobile money payments, this initiates the USSD prompt on the
    # customer's phone.
    confirmed = client.payment.payment_intents.confirm(intent["id"])
    print(f"Payment confirmed: {confirmed['status']}")

    # List recent transactions with pagination. Transactions are created automatically
    # when payment intents are confirmed. The status filter accepts "completed",
    # "pending", or "failed". Each transaction includes id, amount, currency, status,
    # and payment method details. Returns a PageResponse with total count.
    transactions = client.payment.transactions.list(page=1, page_size=5)
    print(f"\nRecent transactions ({transactions.total} total):")
    for tx in transactions.data:
        print(f"  - {tx['id']}: {tx.get('amount', '?')} {tx.get('currency', '')} - {tx.get('status', '')}")

except ValidationError as e:
    print(f"Validation error: {e.message}")
    for err in e.errors:
        print(f"  - {err}")
except EssabuError as e:
    print(f"API error ({e.status_code}): {e.message}")
finally:
    client.close()
