# Asset Module

Fixed asset management: assets, vehicles, depreciation, maintenance schedules, fuel logs, and trip tracking.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `AssetApi` | `/api/asset/assets` | Fixed asset registry |
| `VehicleApi` | `/api/asset/vehicles` | Vehicle fleet management |
| `DepreciationApi` | `/api/asset/depreciations` | Asset depreciation records |
| `MaintenanceLogApi` | `/api/asset/maintenance_logs` | Maintenance history |
| `MaintenanceScheduleApi` | `/api/asset/maintenance_schedules` | Preventive maintenance schedules |
| `FuelLogApi` | `/api/asset/fuel_logs` | Fuel consumption tracking |
| `TripLogApi` | `/api/asset/trip_logs` | Vehicle trip records |

## Standard CRUD Methods

All classes share these standard methods for paginated listing, full-page iteration, creation, retrieval by ID, update, and soft deletion. The `list` method accepts optional keyword filters such as `category`, `status`, or `asset_id`. The `list_all` method returns a generator that fetches every page automatically. All write methods return the created or updated resource as a dictionary.

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## Code Examples

### Asset Registry

Create, list, iterate, update, and delete fixed assets. The `create` method requires `name`, `category`, `purchase_price`, `currency`, and `depreciation_method` (e.g., `"straight_line"`, `"declining_balance"`), with optional fields like `purchase_date`, `useful_life_months`, `location`, and `serial_number`. The `list` method supports filtering by `category` and `status` (e.g., `"active"`, `"disposed"`, `"under_maintenance"`). Use `list_all` to iterate through the complete asset inventory.

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

# Create an asset
asset = client.asset.assets.create(
    name="Dell PowerEdge R750",
    category="IT Equipment",
    purchase_date="2026-01-15",
    purchase_price=8500.00,
    currency="USD",
    useful_life_months=60,
    depreciation_method="straight_line",
    location="Server Room A",
    serial_number="SRV-2026-001",
)

# List assets with filters
assets = client.asset.assets.list(category="IT Equipment", status="active")

# Iterate all assets
for page in client.asset.assets.list_all():
    for a in page.data:
        print(f"{a['name']}: {a['current_value']}")

# Update and delete
client.asset.assets.update(asset["id"], location="Server Room B")
client.asset.assets.delete(asset["id"])
```

### Vehicles

Register and manage vehicles in the fleet. The `create` method requires `make`, `model`, `year`, `license_plate`, and purchase details (`purchase_date`, `purchase_price`, `currency`), with optional `vin` (Vehicle Identification Number) and `assigned_to` (driver user ID). The `list` method supports filtering by `status` (e.g., `"active"`, `"in_maintenance"`, `"decommissioned"`). Use `update` to reassign vehicles to different drivers.

```python
vehicle = client.asset.vehicles.create(
    make="Toyota",
    model="Hilux",
    year=2025,
    license_plate="KIN-1234-AB",
    vin="JTFSS22P600123456",
    purchase_date="2025-06-01",
    purchase_price=35000.00,
    currency="USD",
    assigned_to="driver-uuid",
)
vehicles = client.asset.vehicles.list(status="active")
client.asset.vehicles.update(vehicle["id"], assigned_to="new-driver-uuid")
```

### Depreciation

Record and track depreciation entries for fixed assets. The `create` method requires `asset_id`, `period` (in `"YYYY-MM"` format), `amount`, and `method`. Use the `list` method with an `asset_id` filter to retrieve the full depreciation history for a specific asset. The `retrieve` method returns detailed information including the remaining book value after the depreciation entry.

```python
depreciations = client.asset.depreciations.list(asset_id=asset["id"])
record = client.asset.depreciations.create(
    asset_id=asset["id"],
    period="2026-03",
    amount=141.67,
    method="straight_line",
)
details = client.asset.depreciations.retrieve(record["id"])
```

### Maintenance

Create preventive maintenance schedules and log completed maintenance work. The `maintenance_schedules.create` method defines recurring maintenance with `asset_id`, `type` (e.g., `"oil_change"`, `"inspection"`), `interval_km`, `interval_days`, and `description`. The `maintenance_logs.create` method records a completed maintenance event with `date`, `cost`, `odometer` reading, and `technician` name. Link logs to schedules via `schedule_id` for tracking adherence.

```python
# Scheduled maintenance
schedule = client.asset.maintenance_schedules.create(
    asset_id=vehicle["id"],
    type="oil_change",
    interval_km=5000,
    interval_days=90,
    description="Regular oil change and filter replacement",
)
schedules = client.asset.maintenance_schedules.list(asset_id=vehicle["id"])

# Log completed maintenance
log = client.asset.maintenance_logs.create(
    asset_id=vehicle["id"],
    schedule_id=schedule["id"],
    date="2026-03-15",
    description="Oil change completed",
    cost=150.00,
    odometer=45230,
    technician="Mechanic name",
)
logs = client.asset.maintenance_logs.list(asset_id=vehicle["id"])
```

### Fuel Logs

Record fuel consumption for vehicles. The `create` method requires `vehicle_id`, `date`, `liters`, `cost_per_liter`, `total_cost`, and `odometer` reading, with optional `fuel_type` (e.g., `"diesel"`, `"petrol"`) and `station` name. Use the `list` method with a `vehicle_id` filter to retrieve the fuel history for a specific vehicle. This data enables fuel efficiency analysis and cost tracking per vehicle.

```python
fuel = client.asset.fuel_logs.create(
    vehicle_id=vehicle["id"],
    date="2026-03-26",
    liters=60.5,
    cost_per_liter=1.85,
    total_cost=111.93,
    odometer=45500,
    fuel_type="diesel",
    station="Total Gombe",
)
fuel_logs = client.asset.fuel_logs.list(vehicle_id=vehicle["id"])
```

### Trip Logs

Record vehicle trips with origin, destination, and odometer readings. The `create` method requires `vehicle_id`, `driver_id`, `start_date`, `end_date`, `start_odometer`, `end_odometer`, `origin`, `destination`, and `purpose`. The distance is computed automatically from the odometer readings. Use the `list` method with a `vehicle_id` filter to retrieve the trip history and analyze vehicle utilization patterns.

```python
trip = client.asset.trip_logs.create(
    vehicle_id=vehicle["id"],
    driver_id="driver-uuid",
    start_date="2026-03-26T08:00:00",
    end_date="2026-03-26T17:00:00",
    start_odometer=45500,
    end_odometer=45680,
    origin="Kinshasa",
    destination="Matadi",
    purpose="Client delivery",
)
trips = client.asset.trip_logs.list(vehicle_id=vehicle["id"])
```
