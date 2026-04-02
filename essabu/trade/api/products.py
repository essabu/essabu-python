"""API client for products operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class ProductsApi(BaseApi):
    """API client for products operations."""

    _resource_path = "/products"
