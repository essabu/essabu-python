# Changelog

All notable changes to the Essabu Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-01

### Added

- Initial SDK release
- Unified client with lazy module loading
- HR module: employees, contracts, leaves, payroll, shifts, recruitment, performance, attendance, benefits, departments, documents, expenses, loans, onboarding, positions, skills, timesheets, training, webhooks, reports, disciplinary, history, shift_schedules
- Accounting module: accounts, invoices, payments, journals, wallets, balances, configs, credit notes, journal entries, payment terms, quotes, currencies, exchange rates, fiscal years, periods, reports, tax rates, wallet transactions, inventory, batches, purchase orders, stock counts, stock locations, stock movements, suppliers, webhooks, insurance claims, insurance contracts, insurance partners, price lists, price list overrides
- Identity module: auth, users, roles, tenants, branches, companies, permissions, profiles, sessions, api_keys
- Trade module: customers, contacts, opportunities, products, sales orders, purchase orders, deliveries, suppliers, campaigns, activities, contracts, documents, inventory, receipts, stock, warehouses
- Payment module: payment intents, loans, subscriptions, subscription plans, transactions, refunds, financial accounts, payment accounts, collaterals, KYC documents, KYC profiles, loan applications, loan products, loan repayments, reports
- E-Invoice module: invoices, submissions, verification, compliance, statistics
- Project module: projects, tasks, milestones, resource allocations, task comments, reports
- Asset module: assets, vehicles, depreciation, fuel logs, maintenance logs, maintenance schedules, trip logs
- HTTP client with automatic retry, error mapping, and authentication
- Pydantic-based request/response models
- Comprehensive exception hierarchy
- Pagination support with PageRequest/PageResponse
