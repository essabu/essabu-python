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

All classes share:

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
