"""Example: Process payments via the Payment module."""

from essabu import Essabu
from essabu.common.exceptions import EssabuError, ValidationError

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create a payment intent
    intent = client.payment.payment_intents.create(
        amount="250.00",
        currency="USD",
        payment_method="mobile_money",
        customer_id="cust-001",
        description="Monthly subscription payment",
        metadata={"order_id": "ord-123"},
    )
    print(f"Payment intent created: {intent['id']} - Status: {intent['status']}")

    # Confirm the payment
    confirmed = client.payment.payment_intents.confirm(intent["id"])
    print(f"Payment confirmed: {confirmed['status']}")

    # List transactions
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
