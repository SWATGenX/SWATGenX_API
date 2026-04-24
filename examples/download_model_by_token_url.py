#!/usr/bin/env python3
"""
Download the SWAT+ ZIP using the same token URL as the completion email.

  export SWATGENX_DOWNLOAD_URL='https://www.swatgenx.com/download_model/<token>'
  python examples/download_model_by_token_url.py

Optional: SWATGENX_OUT_ZIP=./MyModel.zip  (default: SWAT_Model.zip)
No API key header — the long token in the path is the credential.
"""
from __future__ import annotations

import os
import sys

import requests


def main() -> int:
    url = os.environ.get("SWATGENX_DOWNLOAD_URL", "").strip()
    if not url or "download_model/" not in url:
        print(
            "Set SWATGENX_DOWNLOAD_URL to the full link from your completion email, e.g.\n"
            "  https://www.swatgenx.com/download_model/<token>",
            file=sys.stderr,
        )
        return 1
    out = (os.environ.get("SWATGENX_OUT_ZIP") or "SWAT_Model.zip").strip() or "SWAT_Model.zip"
    with requests.get(url, stream=True, timeout=600) as r:
        r.raise_for_status()
        with open(out, "wb") as f:
            for chunk in r.iter_content(chunk_size=1 << 20):
                if chunk:
                    f.write(chunk)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
