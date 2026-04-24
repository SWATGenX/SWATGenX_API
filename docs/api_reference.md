# API reference (model creation subset)

[![Base URL](https://img.shields.io/badge/base-www.swatgenx.com-0f766e?style=flat-square)](https://www.swatgenx.com)
[![Auth doc](https://img.shields.io/badge/auth-see%20authentication.md-7c3aed?style=flat-square)](authentication.md)

Base URL: `https://www.swatgenx.com` (use `www` so `/api/*` hits the app, not the marketing apex).

## 🗺️ Discovery (same data the map uses — no API key)

These **GET** routes power the Watershed Explorer UI: pick a USGS site or an HUC8, then draw contributing **HUC12** subbasins. They return JSON the SPA uses for outlines and counts. **You do not need to send API keys** for these read-only calls (rate limits and infrastructure still apply).

| Method | Path | Query | Returns (high level) |
|--------|------|-------|----------------------|
| GET | `/api/get_station_characteristics` | `station=<USGS site_no>` | Station metadata plus **`Num HUC12 subbasins`** and `geometries` / stream / lake layers for those HUC12s. |
| GET | `/api/get_huc8_characteristics` | `huc8=<8-digit code>` | HUC8 label, **`Num HUC12 subbasins`**, and the same style of geometry payloads for all HUC12s in the basin. |
| GET | `/api/huc8-basin-summary` | `huc8=<8-digit code>` | Lightweight JSON: name, **`Num HUC12 subbasins`**, `watershed_area_sqkm` — no heavy geometry arrays. |

Use **`Num HUC12 subbasins`** (or count parsed HUC12 IDs) before calling **`POST /api/model-settings`**: on **Basic**, the server rejects stations above the HUC12 cap (see `docs/subscription_tiers.md`).

---

## 🔐 Model creation & task APIs (API key required)

Send headers from `docs/authentication.md` on every request below.

## `POST /api/model-settings`

Queue or start a **station-centered** (USGS / PRISM site) SWAT+ model.

**Body (common fields):**

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| `site_no` | string | yes | USGS station ID (e.g. eight-digit `05580950`). |
| `ls_resolution` | number | no | landuse/soil resolution |
| `dem_resolution` | number | no | DEM resolution in **meters** (tiers apply). |

**Success:** JSON includes `status`, `order_id` (durable queue id when enqueue is used), and often `task_id` when dispatched immediately.

## `POST /api/model-settings-huc8`

Whole-basin HUC8 build. Body includes `huc8` or `huc8_code` (eight digits). **Pro-only** in production.

## `GET /api/model-orders?limit=50`

List recent model orders for the authenticated user.

## `GET /api/model-orders/health`

Operational snapshot: pending/dispatching queue lengths and Redis **`slots.in_use`** vs **`slots.limit`** (global model-creation concurrency).

## `POST /api/model-orders/<order_id>/cancel`

Cancel a **queued** durable order (`QUEUED_APP`). Other states return an error (use task cancel when `RUNNING`).

## `GET /api/task_status/<task_id>`

JSON `task_info` with `status`, `progress`, nested `info` (phase, message, etc.).

## `POST /api/model_task/<task_id>/cancel`

Stop an in-flight model build when the task is still in an active dashboard phase.

## `GET /api/user_tasks?limit=120`

User’s Celery-tracked tasks plus `model_creation_broker` snapshot (slots, queue depth).

## 📦 Downloads

- **Token link** (from email): `GET /download_model/<token>` — no API key; token is time-limited.
- **Authenticated path**: browser or session-based `GET /download/...` under the user tree — see product docs when exposing zip layout.

Errors return JSON with `status: error`, a `message`, and sometimes a machine `code` (e.g. `quota_exceeded`, `csrf_failed` without API key).
