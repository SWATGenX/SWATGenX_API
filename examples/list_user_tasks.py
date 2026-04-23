#!/usr/bin/env python3
"""GET /api/user_tasks — tasks plus model_creation_broker snapshot (slots, queue)."""
import json
import os
import sys

import requests

API_KEY = (os.environ.get("SWATGENX_API_KEY") or "").strip()
BASE = (os.environ.get("SWATGENX_BASE_URL") or "https://www.swatgenx.com").rstrip("/")


def main() -> int:
    if not API_KEY:
        print("Set SWATGENX_API_KEY", file=sys.stderr)
        return 2
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-SWATGenX-Api-Key": API_KEY,
        "Accept": "application/json",
    }
    lim = int(os.environ.get("SWATGENX_USER_TASKS_LIMIT", "120"))
    r = requests.get(f"{BASE}/api/user_tasks", headers=headers, params={"limit": lim}, timeout=60)
    print(r.status_code, json.dumps(r.json() if r.content else {}, indent=2))
    r.raise_for_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
