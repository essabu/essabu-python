"""Invoice models."""

from pydantic import BaseModel


class InvoiceParty(BaseModel):
    """Represents a party (supplier or customer) on an invoice."""

    tin: str
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None


class InvoiceItem(BaseModel):
    """Represents a line item on an invoice."""

    description: str
    quantity: float
    unit_price: float
    tax_rate: float | None = None
    tax_amount: float | None = None
    total: float | None = None


class NormalizeInvoiceRequest(BaseModel):
    """Request to normalize an invoice."""

    supplier: InvoiceParty
    customer: InvoiceParty
    items: list[InvoiceItem]
    invoice_number: str | None = None
    invoice_date: str | None = None
    currency: str = "BIF"
    notes: str | None = None


class NormalizedInvoiceResponse(BaseModel):
    """Response from invoice normalization."""

    invoice_id: str
    invoice_number: str
    invoice_date: str
    supplier: InvoiceParty
    customer: InvoiceParty
    items: list[InvoiceItem]
    subtotal: float
    tax_total: float
    total: float
    currency: str
    normalized_at: str
    signature: str | None = None
