# Downloading a completed model

[![Download](https://img.shields.io/badge/flow-token%20URL-0ea5e9?style=flat-square)](https://www.swatgenx.com)

Completed SWAT+ workspaces are **not** returned in the JSON body of `POST /api/model-settings`. When the Celery job finishes, SWATGenX sends a **completion email** that contains the same **tokenized download URL** the product has always used: a plain **`GET`** that streams a ZIP.

## Same link as the email — use it from scripts

The link looks like:

```text
https://www.swatgenx.com/download_model/<token>
```

- **No API key** headers on this request — the **token** in the path is the secret (do not commit it, log it, or paste it into public tickets).
- Typical limits (check your email footer for the exact wording): link valid on the order of **days**, and only **a handful** of successful downloads per token before it stops working.

### cURL

```bash
export SWATGENX_DOWNLOAD_URL='https://www.swatgenx.com/download_model/<paste-from-email>'
curl -fL --output SWAT_Model.zip "$SWATGENX_DOWNLOAD_URL"
```

### Python (`requests`)

Use the repo helper (streams large ZIPs):

```bash
export SWATGENX_DOWNLOAD_URL='https://www.swatgenx.com/download_model/<token>'
export SWATGENX_OUT_ZIP='./MyModel.zip'   # optional
python examples/download_model_by_token_url.py
```

Or inline:

```python
import os
import requests

url = os.environ["SWATGENX_DOWNLOAD_URL"]
r = requests.get(url, stream=True, timeout=600)
r.raise_for_status()
with open("SWAT_Model.zip", "wb") as f:
    for chunk in r.iter_content(chunk_size=1 << 20):
        if chunk:
            f.write(chunk)
```

### Where do I get the URL today?

1. **Completion email** — copy the **Download model package** target URL (or long `https://www.swatgenx.com/download_model/...` link).
2. **Web app** — signed-in users can use **User dashboard** flows for completed models (labels vary by release).

`GET /api/task_status/<task_id>` tells you when the run reached **SUCCESS**, but it **does not** currently echo the download URL in JSON — treat the **email link** (or dashboard) as the hand-off for the token URL. A future API could return a fresh signed URL in JSON; until then, headless workflows can consume the token URL after it is copied from the completion email or dashboard into a local environment variable or secret store.

## Other flows

- **Example bundles** (not your private run): log in and use **[Example SWAT+ models](https://www.swatgenx.com/example-models)**.
- **Session / cookie downloads** under `/download/...` are browser-oriented; prefer the token URL for headless servers.
