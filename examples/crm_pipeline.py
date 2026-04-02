"""Example: Manage a CRM sales pipeline with the Trade module.

Demonstrates the full CRM workflow: creating a customer, adding a contact person,
creating a sales opportunity, logging a meeting activity, creating a sales order,
and listing the pipeline by stage. Uses the client.trade resource.
"""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

# Initialize the client. All Trade module resources are accessed via client.trade.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create a new customer record. Required fields are name and email. Optional fields
    # include phone, industry, and address. Returns the created customer with a generated
    # UUID. Raises ValidationError if the email is already registered for another customer.
    customer = client.trade.customers.create(
        name="Acme Corporation",
        email="info@acme.com",
        phone="+243 999 123 456",
        industry="Technology",
        address="123 Business Ave, Kinshasa",
    )
    print(f"Customer created: {customer['id']} - {customer['name']}")

    # Add a contact person linked to the customer. Required fields are customer_id,
    # first_name, last_name, and email. The role field describes the contact's position
    # within the customer organization (e.g., "CTO", "Purchasing Manager"). Contacts can
    # be linked to opportunities and activities for CRM tracking.
    contact = client.trade.contacts.create(
        customer_id=customer["id"],
        first_name="Marie",
        last_name="Kabila",
        email="marie@acme.com",
        phone="+243 999 654 321",
        role="CTO",
    )
    print(f"Contact added: {contact.get('first_name')} {contact.get('last_name')}")

    # Create a sales opportunity in the pipeline. Required fields are customer_id, title,
    # value, currency, and stage. The stage tracks where the deal is in the sales process
    # (e.g., "qualification", "proposal", "negotiation", "closed_won"). The expected_close_date
    # helps with revenue forecasting. Raises ValidationError for invalid stage values.
    opportunity = client.trade.opportunities.create(
        customer_id=customer["id"],
        title="Enterprise License Deal",
        value="50000.00",
        currency="USD",
        stage="qualification",
        expected_close_date="2024-06-30",
    )
    print(f"Opportunity created: {opportunity['id']} - ${opportunity.get('value', '?')}")

    # Log a CRM activity linked to the customer and opportunity. Activities track
    # interactions like meetings, calls, and emails. Required fields are customer_id,
    # type (e.g., "meeting", "call", "email"), and subject. Optional fields include
    # opportunity_id for pipeline tracking, notes for details, and date.
    activity = client.trade.activities.create(
        customer_id=customer["id"],
        opportunity_id=opportunity["id"],
        type="meeting",
        subject="Initial product demo",
        notes="Positive reception. Follow-up scheduled.",
        date="2024-01-20",
    )
    print(f"Activity logged: {activity.get('subject')}")

    # Create a sales order with line items. Required fields are customer_id and items
    # (a list with product_id, quantity, and unit_price per line). The optional
    # opportunity_id links the order to a pipeline deal. The order total is calculated
    # automatically from the line items. Returns the order with its generated ID and status.
    order = client.trade.sales_orders.create(
        customer_id=customer["id"],
        opportunity_id=opportunity["id"],
        items=[
            {"product_id": "prod-001", "quantity": 10, "unit_price": "5000.00"},
        ],
        currency="USD",
    )
    print(f"\nSales order created: {order['id']}")

    # List opportunities filtered by pipeline stage. Returns a PageResponse with the
    # total count and opportunity data. Use this to view the pipeline at each stage
    # and calculate forecasted revenue. Each opportunity includes title, value, and
    # expected close date.
    pipeline = client.trade.opportunities.list(stage="qualification")
    print(f"\nQualification stage: {pipeline.total} opportunities")
    for opp in pipeline.data:
        print(f"  - {opp.get('title')}: ${opp.get('value', '?')}")

except EssabuError as e:
    print(f"Error ({e.status_code}): {e.message}")
finally:
    client.close()
