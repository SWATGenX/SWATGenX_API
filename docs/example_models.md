# Example sites (small regression-style cases)

These USGS `site_no` values are used in SWATGenX internal reliability harnesses: they are **small** PRISM-ready stations suitable for demos (always respect your subscription quota).

| `site_no` | Note |
|-----------|------|
| `402913084285400` | Alaska-style id length used in tests |
| `10348850` | CONUS example |
| `14161500` | CONUS example |
| `05580950` | CONUS example |
| `09513860` | CONUS example |

**HUC8 example (Pro):** `04100004` — verify in UI that the watershed is valid for your account before automating.

Resolutions in API examples often use **`ls_resolution=250`** and **`dem_resolution=30`** (meters); product tier rules still apply server-side.
