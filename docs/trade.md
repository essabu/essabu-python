# Trade Module

CRM and commerce: customers, contacts, opportunities, sales orders, purchase orders, products, suppliers, deliveries, and more.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `CustomerApi` | `/api/trade/customers` | Customer management |
| `ContactApi` | `/api/trade/contacts` | Contact persons |
| `OpportunityApi` | `/api/trade/opportunities` | Sales opportunities / pipeline |
| `SalesOrderApi` | `/api/trade/sales_orders` | Sales orders |
| `PurchaseOrderApi` | `/api/trade/purchase_orders` | Purchase orders |
| `ProductApi` | `/api/trade/products` | Product catalog |
| `SupplierApi` | `/api/trade/suppliers` | Supplier management |
| `DeliveryApi` | `/api/trade/deliveries` | Delivery tracking |
| `ContractApi` | `/api/trade/contracts` | Trade contracts |
| `CampaignApi` | `/api/trade/campaigns` | Marketing campaigns |
| `ActivityApi` | `/api/trade/activities` | CRM activities |
| `DocumentApi` | `/api/trade/documents` | Trade documents |
| `InventoryApi` | `/api/trade/inventory` | Inventory tracking |
| `StockApi` | `/api/trade/stock` | Stock levels |
| `WarehouseApi` | `/api/trade/warehouses` | Warehouse management |
| `ReceiptApi` | `/api/trade/receipts` | Goods receipts |

## Standard CRUD Methods

Every class provides:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## Code Examples

### Customer Management

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

customers = client.trade.customers.list(page_size=20, status="active")
customer = client.trade.customers.create(
    name="ACME Corp",
    email="contact@acme.com",
    phone="+243 812345678",
    address="Kinshasa, DRC",
)
client.trade.customers.update("cust-uuid", name="ACME Corporation")
client.trade.customers.delete("cust-uuid")
```

### Contacts

```python
contacts = client.trade.contacts.list(customer_id="cust-uuid")
contact = client.trade.contacts.create(
    customer_id="cust-uuid",
    first_name="Jean",
    last_name="Kabila",
    email="jean@acme.com",
    role="Purchasing Manager",
)
```

### Opportunities (Pipeline)

```python
opportunities = client.trade.opportunities.list(stage="negotiation")
deal = client.trade.opportunities.create(
    title="Enterprise License Deal",
    customer_id="cust-uuid",
    value=50000,
    currency="USD",
    stage="qualification",
    expected_close="2026-06-30",
)
client.trade.opportunities.update("opp-uuid", stage="proposal")
```

### Sales Orders

```python
order = client.trade.sales_orders.create(
    customer_id="cust-uuid",
    lines=[
        {"product_id": "prod-uuid", "quantity": 10, "unit_price": 25.00},
    ],
)
orders = client.trade.sales_orders.list(status="pending")
```

### Products and Suppliers

```python
products = client.trade.products.list(category="electronics")
product = client.trade.products.create(
    name="Widget Pro",
    sku="WGT-PRO-001",
    price=29.99,
    currency="USD",
)
suppliers = client.trade.suppliers.list()
supplier = client.trade.suppliers.create(
    name="Parts Inc.",
    email="orders@parts.com",
    country="BE",
)
```

### Purchase Orders and Deliveries

```python
po = client.trade.purchase_orders.create(
    supplier_id="sup-uuid",
    lines=[{"product_id": "prod-uuid", "quantity": 100, "unit_price": 15.00}],
)
delivery = client.trade.deliveries.create(
    order_id=order["id"],
    carrier="DHL",
    tracking_number="DHL123456",
)
```

### Warehouses and Stock

```python
warehouses = client.trade.warehouses.list()
stock = client.trade.stock.list(warehouse_id="wh-uuid", product_id="prod-uuid")
```

### Campaigns and Activities

```python
campaign = client.trade.campaigns.create(
    name="Q2 Outreach",
    type="email",
    start_date="2026-04-01",
    end_date="2026-06-30",
)
activity = client.trade.activities.create(
    type="call",
    customer_id="cust-uuid",
    description="Follow-up call",
    due_date="2026-04-01",
)
```
