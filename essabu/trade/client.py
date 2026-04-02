"""Trade / CRM module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.trade.api.activities import ActivityApi
    from essabu.trade.api.campaigns import CampaignApi
    from essabu.trade.api.contacts import ContactApi
    from essabu.trade.api.contracts import ContractApi
    from essabu.trade.api.customers import CustomerApi
    from essabu.trade.api.deliveries import DeliveryApi
    from essabu.trade.api.documents import DocumentApi
    from essabu.trade.api.inventory import InventoryApi
    from essabu.trade.api.opportunities import OpportunityApi
    from essabu.trade.api.products import ProductApi
    from essabu.trade.api.purchase_orders import PurchaseOrderApi
    from essabu.trade.api.receipts import ReceiptApi
    from essabu.trade.api.sales_orders import SalesOrderApi
    from essabu.trade.api.stock import StockApi
    from essabu.trade.api.suppliers import SupplierApi
    from essabu.trade.api.warehouses import WarehouseApi


class TradeClient:
    """Client for the Trade / CRM module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._customers: CustomerApi | None = None
        self._contacts: ContactApi | None = None
        self._opportunities: OpportunityApi | None = None
        self._products: ProductApi | None = None
        self._sales_orders: SalesOrderApi | None = None
        self._purchase_orders: PurchaseOrderApi | None = None
        self._deliveries: DeliveryApi | None = None
        self._suppliers: SupplierApi | None = None
        self._campaigns: CampaignApi | None = None
        self._activities: ActivityApi | None = None
        self._contracts: ContractApi | None = None
        self._documents: DocumentApi | None = None
        self._inventory: InventoryApi | None = None
        self._receipts: ReceiptApi | None = None
        self._stock: StockApi | None = None
        self._warehouses: WarehouseApi | None = None

    @property
    def customers(self) -> CustomerApi:
        if self._customers is None:
            from essabu.trade.api.customers import CustomerApi
            self._customers = CustomerApi(self._http)
        return self._customers
    @property
    def contacts(self) -> ContactApi:
        if self._contacts is None:
            from essabu.trade.api.contacts import ContactApi
            self._contacts = ContactApi(self._http)
        return self._contacts
    @property
    def opportunities(self) -> OpportunityApi:
        if self._opportunities is None:
            from essabu.trade.api.opportunities import OpportunityApi
            self._opportunities = OpportunityApi(self._http)
        return self._opportunities
    @property
    def products(self) -> ProductApi:
        if self._products is None:
            from essabu.trade.api.products import ProductApi
            self._products = ProductApi(self._http)
        return self._products
    @property
    def sales_orders(self) -> SalesOrderApi:
        if self._sales_orders is None:
            from essabu.trade.api.sales_orders import SalesOrderApi
            self._sales_orders = SalesOrderApi(self._http)
        return self._sales_orders
    @property
    def purchase_orders(self) -> PurchaseOrderApi:
        if self._purchase_orders is None:
            from essabu.trade.api.purchase_orders import PurchaseOrderApi
            self._purchase_orders = PurchaseOrderApi(self._http)
        return self._purchase_orders
    @property
    def deliveries(self) -> DeliveryApi:
        if self._deliveries is None:
            from essabu.trade.api.deliveries import DeliveryApi
            self._deliveries = DeliveryApi(self._http)
        return self._deliveries
    @property
    def suppliers(self) -> SupplierApi:
        if self._suppliers is None:
            from essabu.trade.api.suppliers import SupplierApi
            self._suppliers = SupplierApi(self._http)
        return self._suppliers
    @property
    def campaigns(self) -> CampaignApi:
        if self._campaigns is None:
            from essabu.trade.api.campaigns import CampaignApi
            self._campaigns = CampaignApi(self._http)
        return self._campaigns
    @property
    def activities(self) -> ActivityApi:
        if self._activities is None:
            from essabu.trade.api.activities import ActivityApi
            self._activities = ActivityApi(self._http)
        return self._activities
    @property
    def contracts(self) -> ContractApi:
        if self._contracts is None:
            from essabu.trade.api.contracts import ContractApi
            self._contracts = ContractApi(self._http)
        return self._contracts
    @property
    def documents(self) -> DocumentApi:
        if self._documents is None:
            from essabu.trade.api.documents import DocumentApi
            self._documents = DocumentApi(self._http)
        return self._documents
    @property
    def inventory(self) -> InventoryApi:
        if self._inventory is None:
            from essabu.trade.api.inventory import InventoryApi
            self._inventory = InventoryApi(self._http)
        return self._inventory
    @property
    def receipts(self) -> ReceiptApi:
        if self._receipts is None:
            from essabu.trade.api.receipts import ReceiptApi
            self._receipts = ReceiptApi(self._http)
        return self._receipts
    @property
    def stock(self) -> StockApi:
        if self._stock is None:
            from essabu.trade.api.stock import StockApi
            self._stock = StockApi(self._http)
        return self._stock
    @property
    def warehouses(self) -> WarehouseApi:
        if self._warehouses is None:
            from essabu.trade.api.warehouses import WarehouseApi
            self._warehouses = WarehouseApi(self._http)
        return self._warehouses
