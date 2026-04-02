"""Essabu Python SDK - Unified client for all Essabu services.

Usage::

    from essabu import Essabu

    client = Essabu(api_key="xxx", tenant_id="xxx")
    client.hr.employees.create({"first_name": "Jean", "last_name": "Mukendi"})
"""

from essabu.client import Essabu
from essabu.config import EssabuConfig
from essabu.common.exceptions import (
    AuthenticationError,
    AuthorizationError,
    EssabuError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from essabu.common.models import PageRequest, PageResponse

__version__ = "1.0.0"

__all__ = [
    "Essabu",
    "EssabuConfig",
    "EssabuError",
    "AuthenticationError",
    "AuthorizationError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
    "ServerError",
    "PageRequest",
    "PageResponse",
]
