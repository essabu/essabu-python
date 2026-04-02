"""Asset module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.asset.api.assets import AssetApi
    from essabu.asset.api.depreciations import DepreciationApi
    from essabu.asset.api.fuel_logs import FuelLogApi
    from essabu.asset.api.maintenance_logs import MaintenanceLogApi
    from essabu.asset.api.maintenance_schedules import MaintenanceScheduleApi
    from essabu.asset.api.trip_logs import TripLogApi
    from essabu.asset.api.vehicles import VehicleApi


class AssetClient:
    """Client for the Asset module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._assets: AssetApi | None = None
        self._vehicles: VehicleApi | None = None
        self._depreciations: DepreciationApi | None = None
        self._fuel_logs: FuelLogApi | None = None
        self._maintenance_logs: MaintenanceLogApi | None = None
        self._maintenance_schedules: MaintenanceScheduleApi | None = None
        self._trip_logs: TripLogApi | None = None

    @property
    def assets(self) -> AssetApi:
        if self._assets is None:
            from essabu.asset.api.assets import AssetApi
            self._assets = AssetApi(self._http)
        return self._assets
    @property
    def vehicles(self) -> VehicleApi:
        if self._vehicles is None:
            from essabu.asset.api.vehicles import VehicleApi
            self._vehicles = VehicleApi(self._http)
        return self._vehicles
    @property
    def depreciations(self) -> DepreciationApi:
        if self._depreciations is None:
            from essabu.asset.api.depreciations import DepreciationApi
            self._depreciations = DepreciationApi(self._http)
        return self._depreciations
    @property
    def fuel_logs(self) -> FuelLogApi:
        if self._fuel_logs is None:
            from essabu.asset.api.fuel_logs import FuelLogApi
            self._fuel_logs = FuelLogApi(self._http)
        return self._fuel_logs
    @property
    def maintenance_logs(self) -> MaintenanceLogApi:
        if self._maintenance_logs is None:
            from essabu.asset.api.maintenance_logs import MaintenanceLogApi
            self._maintenance_logs = MaintenanceLogApi(self._http)
        return self._maintenance_logs
    @property
    def maintenance_schedules(self) -> MaintenanceScheduleApi:
        if self._maintenance_schedules is None:
            from essabu.asset.api.maintenance_schedules import MaintenanceScheduleApi
            self._maintenance_schedules = MaintenanceScheduleApi(self._http)
        return self._maintenance_schedules
    @property
    def trip_logs(self) -> TripLogApi:
        if self._trip_logs is None:
            from essabu.asset.api.trip_logs import TripLogApi
            self._trip_logs = TripLogApi(self._http)
        return self._trip_logs
