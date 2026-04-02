"""Configuration for the Essabu SDK client."""

from __future__ import annotations

from dataclasses import dataclass, field


# Default base URLs for each service
DEFAULT_BASE_URLS: dict[str, str] = {
    "hr": "https://api.essabu.com",
    "accounting": "https://api.essabu.com",
    "identity": "https://api.essabu.com",
    "trade": "https://api.essabu.com",
    "payment": "https://api.essabu.com",
    "einvoice": "https://api.essabu.com",
    "project": "https://api.essabu.com",
    "asset": "https://api.essabu.com",
}


@dataclass(frozen=True)
class EssabuConfig:
    """Immutable configuration for the Essabu SDK.

    Attributes:
        api_key: API key for Bearer token authentication.
        tenant_id: Tenant identifier for multi-tenant isolation (optional).
        base_url: Root URL of the Essabu API (overrides per-service URLs).
        timeout: Request timeout in seconds (default 30).
        max_retries: Number of automatic retries on 5xx errors (default 3).
        environment: API environment, 'production' or 'sandbox' (default 'production').
        service_urls: Per-service base URL overrides (optional).
    """

    api_key: str
    tenant_id: str | None = None
    base_url: str | None = None
    timeout: float = 30.0
    max_retries: int = 3
    environment: str = "production"
    service_urls: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("api_key is required")

    def get_base_url(self, service: str) -> str:
        """Get the base URL for a specific service."""
        if service in self.service_urls:
            return self.service_urls[service]
        if self.base_url:
            return self.base_url
        return DEFAULT_BASE_URLS.get(service, "https://api.essabu.com")
