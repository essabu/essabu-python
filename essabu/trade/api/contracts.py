"""API client for contracts operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class ContractsApi(BaseApi):
    """API client for contracts operations."""

    _resource_path = "/contracts"
