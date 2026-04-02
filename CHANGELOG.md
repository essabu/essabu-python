# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-26

### Added
- Unified SDK merging all 8 Essabu Python SDKs into a single package
- Modules: HR, Accounting, Identity, Trade, Payment, EInvoice, Project, Asset
- Shared HTTP client with retry logic, error mapping, and authentication
- Unified exception hierarchy (`EssabuError` base class)
- Lazy module initialization for optimal startup performance
- Stripe-like API: `from essabu import Essabu; client = Essabu(api_key="...")`
- Per-service base URL configuration support
- Context manager support for automatic resource cleanup
