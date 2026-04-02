"""Asset module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.asset.api.assets import AssetsApi
from essabu.asset.api.depreciations import DepreciationsApi
from essabu.asset.api.fuel_logs import FuelLogsApi
from essabu.asset.api.maintenance_logs import MaintenanceLogsApi
from essabu.asset.api.maintenance_schedules import MaintenanceSchedulesApi
from essabu.asset.api.trip_logs import TripLogsApi
from essabu.asset.api.vehicles import VehiclesApi


class AssetClient:
    """Asset module client providing access to all Asset API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def assets(self) -> AssetsApi:
        return AssetsApi(self._http)

    @cached_property
    def depreciations(self) -> DepreciationsApi:
        return DepreciationsApi(self._http)

    @cached_property
    def maintenance_schedules(self) -> MaintenanceSchedulesApi:
        return MaintenanceSchedulesApi(self._http)

    @cached_property
    def maintenance_logs(self) -> MaintenanceLogsApi:
        return MaintenanceLogsApi(self._http)

    @cached_property
    def vehicles(self) -> VehiclesApi:
        return VehiclesApi(self._http)

    @cached_property
    def fuel_logs(self) -> FuelLogsApi:
        return FuelLogsApi(self._http)

    @cached_property
    def trip_logs(self) -> TripLogsApi:
        return TripLogsApi(self._http)
