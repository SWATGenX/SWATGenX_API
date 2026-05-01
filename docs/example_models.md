# Example sites (small regression-style cases)

[![USGS](https://img.shields.io/badge/data-USGS%20stations-004a99?style=flat-square)](https://waterdata.usgs.gov/)
[![Example models](https://img.shields.io/badge/download-Example%20SWAT%2B%20models-0f766e?style=flat-square)](https://www.swatgenx.com/example-models)

To inspect **finished** SWAT+ packages (not just API test IDs), **log in** at [swatgenx.com](https://www.swatgenx.com) and open **[Example SWAT+ models](https://www.swatgenx.com/example-models)** for direct downloads.

These USGS `site_no` values are used in SWATGenX internal reliability harnesses: they are **small** PRISM-ready stations suitable for demos (always respect your subscription quota).

| `site_no` | Note |
|-----------|------|
| `402913084285400` | Alaska-style id length used in tests |
| `10348850` | CONUS example |
| `14161500` | CONUS example |
| `05580950` | CONUS example |
| `09513860` | CONUS example |

**HUC8 example (Pro):** `04100004` — verify in UI that the watershed is valid for your account before automating.

**Outlet HUC12 (Basic/Pro):** pick a **12-digit WBD outlet** from Watershed Explorer, then call **`POST /api/model-settings/explorer-watershed`** with **`outlet_huc12`** (see **`examples/create_model_by_outlet_huc12.py`**). Resolved upstream HUC12 count must fit your tier (see **`docs/subscription_tiers.md`**).

Resolutions in API examples often use **`ls_resolution=250`** and **`dem_resolution=30`** (meters); product tier rules still apply server-side.
