# SWATGenX Model Creation API — generate SWAT+ models by USGS station or HUC8

Public **Python examples** and **documentation** for the SWATGenX HTTPS API at **`https://www.swatgenx.com`**.  
You provide a **USGS station ID** or **HUC8** (Pro); the API queues a model-creation **order**, returns **`order_id`** / **`task_id`**, and you poll status until the workspace is ready (downloads are usually via **email link** or the web dashboard).

**Repository:** [github.com/Vahidr32/SWATGenX](https://github.com/Vahidr32/SWATGenX)  
This tree is also maintained inside the private SWATGenX monorepo as **`documents/public_swatgenx_api_examples/`** for drift control — publish by syncing that folder here (no backend code, no private paths).

## Subscription = same limits as the web app

API keys are tied to your **user account**. **Basic** accounts hit the same **HUC12 / cal-val / HUC8** restrictions as in the UI; **Pro** unlocks HUC8 and cal/val where documented. See **`docs/subscription_tiers.md`**.

## What SWATGenX exposes

SWATGenX offers authenticated HTTP APIs to queue **SWAT+** model builds from national datasets:

| Entry | HTTP | Notes |
|-------|------|--------|
| USGS streamgage / station | `POST /api/model-settings` | JSON body includes `site_no` (and optional resolutions). |
| HUC8 watershed | `POST /api/model-settings-huc8` | **Effective Pro** subscription required for HUC8 whole-basin orders. |
| Durable orders | `GET /api/model-orders` | Active `QUEUED_APP` / `DISPATCHING` / `RUNNING` rows. |
| Queue health | `GET /api/model-orders/health` | Redis-backed slot snapshot (`slots.in_use`, `slots.limit`). |
| Celery task row | `GET /api/task_status/<task_id>` | Progress while a build runs. |
| Cancel queued order | `POST /api/model-orders/<order_id>/cancel` | Queued durable orders only. |
| Stop in-flight build | `POST /api/model_task/<task_id>/cancel` | Revokes the Celery task when still cancelable. |

Downloads of completed workspaces are typically issued via **email links** (token-based `GET /download_model/<token>`) or the signed-in web app (`/download/...`). See `docs/api_reference.md`.

## Quick start (local copy of this bundle)

```bash
cd documents/public_swatgenx_api_examples
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # edit: set SWATGENX_API_KEY
python examples/create_model_by_usgs_station.py
```

## Layout

| Path | Purpose |
|------|---------|
| `examples/*.py` | Minimal `requests` scripts (no pip package). |
| `docs/` | Authentication summary + endpoint table + example station list. |
| `example_outputs/` | Placeholder for screenshots when you publish the public repo. |
| `notebooks/README.md` | How to paste examples into Jupyter / Colab. |
| `requirements.txt` | `requests` only for v1. |
| `.env.example` | Variable names only — **never** commit real keys. |

## Website

Host a short product page on **www.swatgenx.com** (e.g. `/developer-api` or `/api-access`) that:

- States the capability: programmatic SWAT+ generation by **USGS station** or **HUC8**.
- Links to the **public GitHub repo** once published.
- Uses **screenshots** from `example_outputs/screenshots/` (order JSON, dashboard or email “ready” state).

## Security

- Never commit **`.env`**, API keys (`sgx_…`), or GitHub tokens to this public repository.
- Revoke any token that was ever pasted into chat, logs, or a committed file.

## Relationship to internal QA

The private application codebase includes HTTP reliability harnesses used before releases. Those scripts are **not** part of this public repo; this repo stays **client-only** (`requests` + docs).
