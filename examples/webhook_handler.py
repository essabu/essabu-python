"""Example: Handle webhooks from Essabu platform.

This example uses Flask, but you can adapt it to any web framework.
It demonstrates signature verification using HMAC-SHA256 and routing
of different event types to appropriate handlers.
"""

import hashlib
import hmac
import json

# pip install flask
from flask import Flask, jsonify, request

app = Flask(__name__)
WEBHOOK_SECRET = "whsec_your_webhook_secret"


# Verify the webhook payload signature against the shared secret. Essabu signs
# every webhook payload with HMAC-SHA256 using your webhook secret. The signature
# is sent in the X-Essabu-Signature header as "sha256={hex_digest}". This function
# computes the expected signature and compares it in constant time to prevent
# timing attacks. Returns True if the signature is valid, False otherwise.
def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Verify the webhook signature."""
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)


# Handle incoming webhook events from the Essabu platform. The endpoint extracts
# the raw payload and signature header, verifies the signature, then routes the
# event based on its type field. Supported event types include "invoice.created",
# "payment.succeeded", "employee.created", and "loan.approved". Always returns
# a 200 response promptly to acknowledge receipt; process events asynchronously
# for long-running operations to avoid webhook timeouts.
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
