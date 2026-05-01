# Subscription tiers vs the API

[![Basic](https://img.shields.io/badge/tier-Basic-f59e0b?style=flat-square)](https://www.swatgenx.com/subscription)
[![Pro](https://img.shields.io/badge/tier-Effective%20Pro-ca8a04?style=flat-square)](https://www.swatgenx.com/subscription)

The same **account and subscription rules** apply whether you use the web app or these HTTP APIs with your **SWATGenX API key** (`sgx_…`).

## 🎫 Basic

- **Daily cap:** up to **5** SWAT+ **model creation** orders per **UTC calendar day** (same counter as the web app).
- **USGS station** (`POST /api/model-settings`) builds are allowed when the station’s contributing **HUC12 count** is **≤ 15** (the app computes this server-side from the same station table as the map). Larger watersheds return **403** with codes such as `basic_huc12_limit`. To preview a station’s footprint, call **`GET /api/get_station_characteristics?station=<site_no>`** and read **`Num HUC12 subbasins`** (see `docs/api_reference.md`).
- **Outlet HUC12 catalog watershed** (`POST /api/model-settings/explorer-watershed`) uses the same **Basic** contributing-**HUC12** cap (**≤ 15** after upstream resolution). Larger catalog watersheds return **403** (`basic_huc12_limit` / upgrade messaging). **Pro** allows larger resolved watersheds up to server safety limits.
- **Calibration / validation** options on model creation are **Pro-only**; Basic requests that enable them receive **403** (`calval_pro_only`).
- **HUC8 whole-basin** orders (`POST /api/model-settings-huc8`) are **not** available on Basic — **403** (`tier_limit` / Pro messaging).

## ⭐ Effective Pro

- Higher monthly **model-creation quota** (still enforced — **403** `quota_exceeded` when exhausted).
- **HUC8** whole-basin creation via `/api/model-settings-huc8`.
- **Outlet HUC12** catalog watershed creation via `/api/model-settings/explorer-watershed` (larger resolved HUC12 sets than Basic allows).
- Calibration/validation flags where applicable.

There is no separate “API tier”: the key is tied to your **user account**. Scripts should print server `message` / `code` fields on non-2xx responses for debugging.
