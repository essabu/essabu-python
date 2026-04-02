"""Trade module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.trade.api.activities import ActivitiesApi
from essabu.trade.api.campaigns import CampaignsApi
from essabu.trade.api.contacts import ContactsApi
from essabu.trade.api.contracts import ContractsApi
from essabu.trade.api.customers import CustomersApi
from essabu.trade.api.deliveries import DeliveriesApi
from essabu.trade.api.documents import DocumentsApi
from essabu.trade.api.inventory import InventoryApi
from essabu.trade.api.opportunities import OpportunitiesApi
from essabu.trade.api.products import ProductsApi
from essabu.trade.api.purchase_orders import PurchaseOrdersApi
from essabu.trade.api.receipts import ReceiptsApi
from essabu.trade.api.sales_orders import SalesOrdersApi
from essabu.trade.api.stock import StockApi
from essabu.trade.api.suppliers import SuppliersApi
from essabu.trade.api.warehouses import WarehousesApi


class TradeClient:
    """Trade module client providing access to all Trade API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def customers(self) -> CustomersApi:
        return CustomersApi(self._http)

    @cached_property
    def products(self) -> ProductsApi:
        return ProductsApi(self._http)

    @cached_property
    def sales_orders(self) -> SalesOrdersApi:
        return SalesOrdersApi(self._http)

    @cached_property
    def deliveries(self) -> DeliveriesApi:
        return DeliveriesApi(self._http)

    @cached_property
    def receipts(self) -> ReceiptsApi:
        return ReceiptsApi(self._http)

    @cached_property
    def suppliers(self) -> SuppliersApi:
        return SuppliersApi(self._http)

    @cached_property
    def purchase_orders(self) -> PurchaseOrdersApi:
        return PurchaseOrdersApi(self._http)

    @cached_property
    def inventory(self) -> InventoryApi:
        return InventoryApi(self._http)

    @cached_property
    def stock(self) -> StockApi:
        return StockApi(self._http)

    @cached_property
    def warehouses(self) -> WarehousesApi:
        return WarehousesApi(self._http)

    @cached_property
    def contacts(self) -> ContactsApi:
        return ContactsApi(self._http)

    @cached_property
    def opportunities(self) -> OpportunitiesApi:
        return OpportunitiesApi(self._http)

    @cached_property
    def activities(self) -> ActivitiesApi:
        return ActivitiesApi(self._http)

    @cached_property
    def campaigns(self) -> CampaignsApi:
        return CampaignsApi(self._http)

    @cached_property
    def contracts(self) -> ContractsApi:
        return ContractsApi(self._http)

    @cached_property
    def documents(self) -> DocumentsApi:
        return DocumentsApi(self._http)
