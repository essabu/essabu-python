"""Example: Manage a CRM sales pipeline with the Trade module."""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create a customer
    customer = client.trade.customers.create(
        name="Acme Corporation",
        email="info@acme.com",
        phone="+243 999 123 456",
        industry="Technology",
        address="123 Business Ave, Kinshasa",
    )
    print(f"Customer created: {customer['id']} - {customer['name']}")

    # Add a contact
    contact = client.trade.contacts.create(
        customer_id=customer["id"],
        first_name="Marie",
        last_name="Kabila",
        email="marie@acme.com",
        phone="+243 999 654 321",
        role="CTO",
    )
    print(f"Contact added: {contact.get('first_name')} {contact.get('last_name')}")

    # Create an opportunity
    opportunity = client.trade.opportunities.create(
        customer_id=customer["id"],
        title="Enterprise License Deal",
        value="50000.00",
        currency="USD",
        stage="qualification",
        expected_close_date="2024-06-30",
    )
    print(f"Opportunity created: {opportunity['id']} - ${opportunity.get('value', '?')}")

    # Log an activity
    activity = client.trade.activities.create(
        customer_id=customer["id"],
        opportunity_id=opportunity["id"],
        type="meeting",
        subject="Initial product demo",
        notes="Positive reception. Follow-up scheduled.",
        date="2024-01-20",
    )
    print(f"Activity logged: {activity.get('subject')}")

    # Create a sales order
    order = client.trade.sales_orders.create(
        customer_id=customer["id"],
        opportunity_id=opportunity["id"],
        items=[
            {"product_id": "prod-001", "quantity": 10, "unit_price": "5000.00"},
        ],
        currency="USD",
    )
    print(f"\nSales order created: {order['id']}")

    # List pipeline by stage
    pipeline = client.trade.opportunities.list(stage="qualification")
    print(f"\nQualification stage: {pipeline.total} opportunities")
    for opp in pipeline.data:
        print(f"  - {opp.get('title')}: ${opp.get('value', '?')}")

except EssabuError as e:
    print(f"Error ({e.status_code}): {e.message}")
finally:
    client.close()
