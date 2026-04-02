"""API client for opportunities operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class OpportunitiesApi(BaseApi):
    """API client for opportunities operations."""

    _resource_path = "/opportunities"
