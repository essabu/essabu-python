"""Essabu SDK configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass
class EssabuConfig:
    """Configuration for the Essabu SDK client.

    Values can be provided explicitly or via environment variables:
    - ESSABU_API_KEY
    - ESSABU_TENANT_ID
    - ESSABU_BASE_URL
    - ESSABU_TIMEOUT
    - ESSABU_MAX_RETRIES
    """

    api_key: str = field(default_factory=lambda: os.environ.get("ESSABU_API_KEY", ""))
    tenant_id: str = field(default_factory=lambda: os.environ.get("ESSABU_TENANT_ID", ""))
    base_url: str = field(default_factory=lambda: os.environ.get("ESSABU_BASE_URL", "https://api.essabu.com"))
    timeout: float = field(default_factory=lambda: float(os.environ.get("ESSABU_TIMEOUT", "30.0")))
    max_retries: int = field(default_factory=lambda: int(os.environ.get("ESSABU_MAX_RETRIES", "3")))

    def __post_init__(self) -> None:
        self.base_url = self.base_url.rstrip("/")

    def validate(self) -> None:
        """Validate that required configuration values are present."""
        if not self.api_key:
            raise ValueError(
                "API key is required. Provide it via Essabu(api_key=...) or ESSABU_API_KEY environment variable."
            )
        if not self.tenant_id:
            raise ValueError(
                "Tenant ID is required. Provide it via Essabu(tenant_id=...) or ESSABU_TENANT_ID environment variable."
            )
