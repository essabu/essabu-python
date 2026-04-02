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

Every class provides these standard methods for paginated listing, full-page iteration, creation, retrieval by ID, update, and soft deletion. The `list` method accepts optional keyword filters such as `status`, `customer_id`, or `category`. The `list_all` method returns a generator that automatically fetches every page. All write methods return the created or updated resource as a dictionary.

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

Create, list, update, and delete customer records. The `create` method requires `name` and `email`, with optional fields like `phone`, `address`, and `industry`. The `list` method supports filtering by `status` (e.g., `"active"`, `"inactive"`) and returns paginated results. The `delete` method performs a soft delete, preserving the customer record for historical reference while hiding it from active lists.

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

Manage contact persons associated with customer organizations. The `create` method requires `customer_id`, `first_name`, `last_name`, and `email`, with optional `phone` and `role` fields. Use the `list` method with a `customer_id` filter to retrieve all contacts for a specific customer. Each contact can be linked to opportunities and activities for CRM tracking.

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

Create and manage sales opportunities through the CRM pipeline. The `create` method requires `title`, `customer_id`, `value`, `currency`, and `stage` (e.g., `"qualification"`, `"proposal"`, `"negotiation"`, `"closed_won"`, `"closed_lost"`). The optional `expected_close` date helps with forecasting. Use `update` to advance opportunities through pipeline stages. The `list` method filters by `stage` to view opportunities at each pipeline phase.

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

Create sales orders with line items for fulfillment. The `create` method requires `customer_id` and a `lines` list where each line specifies `product_id`, `quantity`, and `unit_price`. The order total is calculated automatically from the line items. Use the `list` method with a `status` filter (e.g., `"pending"`, `"confirmed"`, `"shipped"`, `"delivered"`) to track orders through the fulfillment pipeline.

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

Manage the product catalog and supplier directory. The `products.create` method requires `name`, `sku` (unique stock-keeping unit), `price`, and `currency`, with optional `category` for filtering. The `suppliers.create` method registers a new supplier with `name`, `email`, and `country`. Both resources support standard CRUD operations and can be linked to purchase orders and inventory records.

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

Create purchase orders for suppliers and track deliveries. The `purchase_orders.create` method requires `supplier_id` and a `lines` list with `product_id`, `quantity`, and `unit_price`. The `deliveries.create` method links a delivery to an order with `carrier` and `tracking_number` for shipment tracking. Delivery status updates automatically as tracking events are received from the carrier.

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

Query warehouse locations and check stock levels for products. The `warehouses.list` method returns all configured warehouse locations. The `stock.list` method accepts `warehouse_id` and `product_id` filters to check current inventory levels at specific locations. Stock levels are updated automatically when sales orders are fulfilled, purchase orders are received, or stock adjustments are made.

```python
warehouses = client.trade.warehouses.list()
stock = client.trade.stock.list(warehouse_id="wh-uuid", product_id="prod-uuid")
```

### Campaigns and Activities

Create marketing campaigns and log CRM activities for customer engagement tracking. The `campaigns.create` method requires `name`, `type` (e.g., `"email"`, `"phone"`, `"event"`), `start_date`, and `end_date`. The `activities.create` method logs customer interactions with `type` (e.g., `"call"`, `"meeting"`, `"email"`), `customer_id`, `description`, and `due_date`. Activities can be linked to opportunities for pipeline tracking.

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
