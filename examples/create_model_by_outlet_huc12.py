#!/usr/bin/env python3
"""Queue a SWAT+ model for a WBD catalog watershed: POST /api/model-settings/explorer-watershed.

Body requires outlet_huc12 (12 digits). Upstream HUC12s are resolved server-side; Basic uses the
same contributing-HUC12 cap as USGS station builds (see docs/subscription_tiers.md).

Set SWATGENX_EXAMPLE_OUTLET_HUC12 to an outlet from Watershed Explorer if the default is unsuitable.
"""
import json
import os
import sys

import requests

API_KEY = (os.environ.get("SWATGENX_API_KEY") or "").strip()
BASE = (os.environ.get("SWATGENX_BASE_URL") or "https://www.swatgenx.com").rstrip("/")
# Small CONUS outlet used in internal tests — confirm in the UI before burning quota.
OUTLET = (os.environ.get("SWATGENX_EXAMPLE_OUTLET_HUC12") or "071200060102").strip().zfill(12)


def main() -> int:
    if not API_KEY:
        print("Set SWATGENX_API_KEY", file=sys.stderr)
        return 2
    if len(OUTLET) != 12 or not OUTLET.isdigit():
        print("outlet_huc12 must be 12 digits", file=sys.stderr)
        return 2
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-SWATGenX-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "outlet_huc12": OUTLET,
        "ls_resolution": int(os.environ.get("SWATGENX_LS_RESOLUTION_M", "250")),
        "dem_resolution": int(os.environ.get("SWATGENX_DEM_RESOLUTION_M", "30")),
    }
    r = requests.post(f"{BASE}/api/model-settings/explorer-watershed", headers=headers, json=payload, timeout=120)
    print(r.status_code, json.dumps(r.json() if r.content else {}, indent=2))
    r.raise_for_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
