# Subscription tiers vs the API

The same **account and subscription rules** apply whether you use the web app or these HTTP APIs with your **SWATGenX API key** (`sgx_…`).

## Basic

- **USGS station** (`POST /api/model-settings`) builds are allowed when the station’s contributing **HUC12 count** is within the Basic cap (the app computes this server-side). Larger watersheds return **403** with codes such as `basic_huc12_limit`.
- **Calibration / validation** options on model creation are **Pro-only**; Basic requests that enable them receive **403** (`calval_pro_only`).
- **HUC8 whole-basin** orders (`POST /api/model-settings-huc8`) are **not** available on Basic — **403** (`tier_limit` / Pro messaging).

## Effective Pro

- Higher monthly **model-creation quota** (still enforced — **403** `quota_exceeded` when exhausted).
- **HUC8** whole-basin creation via `/api/model-settings-huc8`.
- Calibration/validation flags where applicable.

There is no separate “API tier”: the key is tied to your **user account**. Scripts should print server `message` / `code` fields on non-2xx responses for debugging.
