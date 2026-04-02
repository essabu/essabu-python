"""Example: Handle webhooks from Essabu platform.

This example uses Flask, but you can adapt it to any web framework.
"""

import hashlib
import hmac
import json

# pip install flask
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = "whsec_your_webhook_secret"


def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Verify the webhook signature."""
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)


@app.route("/webhooks/essabu", methods=["POST"])
def handle_webhook():
    payload = request.get_data()
    signature = request.headers.get("X-Essabu-Signature", "")

    if not verify_signature(payload, signature, WEBHOOK_SECRET):
        return jsonify({"error": "Invalid signature"}), 401

    event = json.loads(payload)
    event_type = event.get("type", "")
    data = event.get("data", {})

    print(f"Received event: {event_type}")

    if event_type == "invoice.created":
        print(f"New invoice: {data.get('id')} - {data.get('total')}")
    elif event_type == "payment.succeeded":
        print(f"Payment succeeded: {data.get('id')} - {data.get('amount')}")
    elif event_type == "employee.created":
        print(f"New employee: {data.get('first_name')} {data.get('last_name')}")
    elif event_type == "loan.approved":
        print(f"Loan approved: {data.get('id')} - {data.get('amount')}")
    else:
        print(f"Unhandled event type: {event_type}")

    return jsonify({"received": True}), 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
