# SWATGenX Model Creation API — generate SWAT+ models by USGS station or HUC8

[![SWATGenX](https://img.shields.io/badge/SWATGenX-www.swatgenx.com-0f766e?style=flat-square)](https://www.swatgenx.com)
[![Subscription / API keys](https://img.shields.io/badge/API%20keys-Subscription-7c3aed?style=flat-square)](https://www.swatgenx.com/subscription)
[![Python](https://img.shields.io/badge/stack-Python%20%2B%20requests-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-see%20repo-6b7280?style=flat-square)](LICENSE)

Public **Jupyter notebook** + small **Python** helpers for the SWATGenX API at **`https://www.swatgenx.com`**.

> **Note:** GitHub Markdown does not support custom text colors; **badges** (above) and **emoji** in headings are the portable way to add color on the default theme.

## 🔑 Get an API key (required for model orders)

1. **Sign up** (or log in) at **[swatgenx.com](https://www.swatgenx.com)**.
2. Open **[Subscription](https://www.swatgenx.com/subscription)**.
3. In the **API keys** section, **generate** a key. It will start with **`sgx_`**. Store it in a password manager or `.env` — never commit it to git.

Send that key on every authenticated request using **both** headers (see **`docs/authentication.md`**): `Authorization: Bearer <sgx_…>` and `X-SWATGenX-Api-Key: <sgx_…>`.

## 🎫 Basic plan — what API users should expect

**Basic** is the default free tier. For **USGS station** SWAT+ orders (`POST /api/model-settings`), the same rules as the web app apply:

- **Up to 5 SWAT+ model orders per UTC calendar day** (rolling reset on the server).
- Each station order is allowed only if the contributing watershed has **at most 15 HUC12 subbasins** (the app counts them server-side). Larger stations return **403** with codes such as `basic_huc12_limit`.

**Pro (effective)** removes those Basic caps for station builds, unlocks **HUC8 whole-basin** creation, and raises monthly quotas — see **`docs/subscription_tiers.md`** and live numbers on the Subscription page.

## 🗺️ Discover HUC12 counts the same way the map does

The web map loads a USGS site (or an HUC8), then the **server** returns the contributing **HUC12** set and draws it. Your scripts can use the **same HTTP endpoints** (no API key needed for these read-only GETs):

| Goal | Endpoint |
|------|----------|
| Station: metadata + HUC12 outlines + **`Num HUC12 subbasins`** | `GET https://www.swatgenx.com/api/get_station_characteristics?station=<site_no>` |
| HUC8: full basin geometry stack + **`Num HUC12 subbasins`** | `GET https://www.swatgenx.com/api/get_huc8_characteristics?huc8=<8-digit>` |
| HUC8: **lightweight** name, HUC12 count, area (km²) only | `GET https://www.swatgenx.com/api/huc8-basin-summary?huc8=<8-digit>` |

Parse **`Num HUC12 subbasins`** (or derive a count from returned HUC12 lists) **before** you `POST /api/model-settings`, so Basic users avoid a predictable 403. For **HUC8** builds, use the characteristics or summary response to understand basin size; the actual **`POST /api/model-settings-huc8`** call still requires **Pro** in production.

Details and the authenticated route table: **`docs/api_reference.md`**.

## 📥 Get the ZIP (same token URL as the email)

When the build finishes, SWATGenX emails a **time-limited** link of the form:

`https://www.swatgenx.com/download_model/<token>`

That is a normal **`GET`** that returns the ZIP attachment — **the same URL** whether you click it in the email or pass it to automation. **Do not** send `Authorization` / `X-SWATGenX-Api-Key` on that request; the token path is the credential.

**Programmatic download** (once the token URL is available from the completion email or dashboard):

```bash
export SWATGENX_DOWNLOAD_URL='https://www.swatgenx.com/download_model/<token-from-email>'
curl -fL --output SWAT_Model.zip "$SWATGENX_DOWNLOAD_URL"
```

Or Python: see **`examples/download_model_by_token_url.py`** and **`examples/download_model.md`** (streaming `requests`, expiry / re-download limits).

`GET /api/task_status/<task_id>` is for **progress**; it does **not** currently return the download URL in JSON — for headless workflows, consume the token URL after it is copied from the completion email or dashboard into a local environment variable or secret store (e.g. `SWATGENX_DOWNLOAD_URL`).

---

**Fastest path:** open **`notebooks/01_simple_station_model.ipynb`** in JupyterLab — set your **API key** and **USGS station ID** (`site_no`), run all cells, wait until the task shows **SUCCESS**, then use the **email download link** (or the same URL in `curl` / Python above) or the **web dashboard**. (The API does not stream the ZIP back in one synchronous call; see the notebook intro.)

For **HUC8** (whole basin) or raw `requests` scripts, see **`examples/`** and **`docs/`**.

**Repository:** [github.com/Vahidr32/SWATGenX](https://github.com/Vahidr32/SWATGenX)  
This tree is also reachable from the private SWATGenX monorepo as **`documents/public_swatgenx_api_examples/`** (usually a **symlink** to this clone — see **`RELEASING.md`**) so there is one copy to edit, not a manual `rsync` (no backend code, no private paths).

## ⚖️ Subscription = same limits as the web app

API keys are tied to your **user account**. **Basic** accounts hit the same **HUC12 / daily order / HUC8** restrictions as in the UI; **Pro** unlocks HUC8 and cal/val where documented. See **`docs/subscription_tiers.md`**.

## 📡 What SWATGenX exposes

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

## 🚀 Quick start (JupyterLab — recommended)

```bash
cd documents/public_swatgenx_api_examples   # path inside private monorepo; or clone the public GitHub repo
python3 -m venv .venv && . .venv/bin/activate
pip install jupyterlab requests
export SWATGENX_API_KEY='sgx_…'
jupyter lab notebooks/01_simple_station_model.ipynb
```

CLI alternative: `pip install -r requirements.txt` then `python examples/create_model_by_usgs_station.py`.

## 📂 Layout

| Path | Purpose |
|------|---------|
| **`notebooks/01_simple_station_model.ipynb`** | **Main user story:** station ID + API key → submit → poll → download guidance. |
| `examples/*.py` | Minimal `requests` scripts (no pip package). |
| `docs/` | Authentication, tiers, endpoint table. |
| `example_outputs/` | Pointers + optional screenshots; **download real examples** from [Example SWAT+ models](https://www.swatgenx.com/example-models) (log in on the site). |
| `requirements.txt` | `requests` only (add `jupyterlab` locally for the notebook). |
| `.env.example` | Variable names only — **never** commit real keys. |

## 🌐 Website

- **Example outputs:** signed-in users can download curated SWAT+ packages from **[Example SWAT+ models](https://www.swatgenx.com/example-models)** — same idea as what you get after a successful API build (log in on the site).
- **Product / API page:** host a short page on **www.swatgenx.com** (e.g. `/developer-api` or `/api-access`) that states programmatic generation by **USGS station** or **HUC8** and links to this **public GitHub repo**.
- **Optional repo assets:** use non-sensitive **screenshots** in `example_outputs/screenshots/` (order JSON, dashboard or email “ready” state) if you publish visuals alongside the docs.

## 🔒 Security

- Never commit **`.env`**, API keys (`sgx_…`), or GitHub tokens to this public repository.
- Revoke any token that was ever pasted into chat, logs, or a committed file.

## 🧪 Relationship to internal QA

The private application codebase includes HTTP reliability harnesses used before releases. Those scripts are **not** part of this public repo; this repo stays **client-only** (`requests` + docs).
