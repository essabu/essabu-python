"""API client for loan products operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class LoanProductsApi(BaseApi):
    """API client for loan products operations."""

    _resource_path = "/loan-products"
