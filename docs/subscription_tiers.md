# Subscription tiers vs the API

The same **account and subscription rules** apply whether you use the web app or these HTTP APIs with your **SWATGenX API key** (`sgx_…`).

## Basic

- **Daily cap:** up to **5** SWAT+ **model creation** orders per **UTC calendar day** (same counter as the web app).
- **USGS station** (`POST /api/model-settings`) builds are allowed when the station’s contributing **HUC12 count** is **≤ 15** (the app computes this server-side from the same station table as the map). Larger watersheds return **403** with codes such as `basic_huc12_limit`. To preview a station’s footprint, call **`GET /api/get_station_characteristics?station=<site_no>`** and read **`Num HUC12 subbasins`** (see `docs/api_reference.md`).
- **Calibration / validation** options on model creation are **Pro-only**; Basic requests that enable them receive **403** (`calval_pro_only`).
- **HUC8 whole-basin** orders (`POST /api/model-settings-huc8`) are **not** available on Basic — **403** (`tier_limit` / Pro messaging).

## Effective Pro

- Higher monthly **model-creation quota** (still enforced — **403** `quota_exceeded` when exhausted).
- **HUC8** whole-basin creation via `/api/model-settings-huc8`.
- Calibration/validation flags where applicable.

There is no separate “API tier”: the key is tied to your **user account**. Scripts should print server `message` / `code` fields on non-2xx responses for debugging.
