#!/usr/bin/env python3
"""Queue a station-centered SWAT+ model: POST /api/model-settings"""
import json
import os
import sys

import requests

API_KEY = (os.environ.get("SWATGENX_API_KEY") or "").strip()
BASE = (os.environ.get("SWATGENX_BASE_URL") or "https://www.swatgenx.com").rstrip("/")
SITE = (os.environ.get("SWATGENX_EXAMPLE_SITE_NO") or "05580950").strip()


def main() -> int:
    if not API_KEY:
        print("Set SWATGENX_API_KEY", file=sys.stderr)
        return 2
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-SWATGenX-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "site_no": SITE,
        "ls_resolution": int(os.environ.get("SWATGENX_LS_RESOLUTION_M", "250")),
        "dem_resolution": int(os.environ.get("SWATGENX_DEM_RESOLUTION_M", "30")),
    }
    r = requests.post(f"{BASE}/api/model-settings", headers=headers, json=payload, timeout=120)
    print(r.status_code, json.dumps(r.json() if r.content else {}, indent=2))
    r.raise_for_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
