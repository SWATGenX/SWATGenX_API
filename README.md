# SWATGenX Model Creation API — generate SWAT+ models for +16,000 USGS stations or any HUC8, based on High Resolution National Hydrographical database (NHDPlus HR).

Public **Jupyter notebook** + small **Python** helpers for the SWATGenX API at **`https://www.swatgenx.com`**.

**Fastest path:** open **`notebooks/01_simple_station_model.ipynb`** in JupyterLab — set your **API key** and **USGS station ID** (`site_no`), run all cells, wait until the task shows **SUCCESS**, then use the **email download link** or the **web dashboard** to fetch files. (The API does not stream the ZIP back in one synchronous call; see the notebook intro.)

For **HUC8** (whole basin) or raw `requests` scripts, see **`examples/`** and **`docs/`**.

**Repository:** [github.com/SWATGenX/SWATGenX_API](https://github.com/SWATGenX/SWATGenX_API)

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

## Quick start (JupyterLab — recommended)

```bash
git clone https://github.com/SWATGenX/SWATGenX_API.git
cd SWATGenX_API
python3 -m venv .venv && . .venv/bin/activate
pip install jupyterlab requests
export SWATGENX_API_KEY='sgx_…'
jupyter lab notebooks/01_simple_station_model.ipynb
```

CLI alternative: `pip install -r requirements.txt` then `python examples/create_model_by_usgs_station.py`.

## Layout

| Path | Purpose |
|------|---------|
| **`notebooks/01_simple_station_model.ipynb`** | **Main user story:** station ID + API key → submit → poll → download guidance. |
| `examples/*.py` | Minimal `requests` scripts (no pip package). |
| `docs/` | Authentication, tiers, endpoint table. |
| `example_outputs/` | Screenshots when you publish. |
| `requirements.txt` | `requests` only (add `jupyterlab` locally for the notebook). |
| `.env.example` | Variable names only — **never** commit real keys. |

## Website

Use **[SWATGenX Developer API](https://www.swatgenx.com/developer-api)** for the public website overview: programmatic SWAT+ generation by **USGS station** or **HUC8**, with links back to this GitHub repo and the example-model catalog.

## Security

- Never commit **`.env`**, API keys (`sgx_…`), or GitHub tokens to this public repository.
- Revoke any token that was ever pasted into chat, logs, or a committed file.
