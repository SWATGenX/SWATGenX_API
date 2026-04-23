#!/usr/bin/env python3
"""POST /api/model_task/<task_id>/cancel — in-flight model build (when cancelable)."""
import json
import os
import sys

import requests

API_KEY = (os.environ.get("SWATGENX_API_KEY") or "").strip()
BASE = (os.environ.get("SWATGENX_BASE_URL") or "https://www.swatgenx.com").rstrip("/")
TID = (os.argv[1] if len(sys.argv) > 1 else os.environ.get("SWATGENX_TASK_ID") or "").strip()


def main() -> int:
    if not API_KEY or not TID:
        print("Usage: SWATGENX_API_KEY=… python cancel_running_task.py <celery_task_id>", file=sys.stderr)
        return 2
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "X-SWATGenX-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    r = requests.post(f"{BASE}/api/model_task/{TID}/cancel", headers=headers, json={}, timeout=120)
    print(r.status_code, json.dumps(r.json() if r.content else {}, indent=2))
    r.raise_for_status()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
