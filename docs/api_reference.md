# API reference (model creation subset)

Base URL: `https://www.swatgenx.com` (use `www` so `/api/*` hits the app, not the marketing apex).

All paths below require authentication (API key headers unless noted).

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

## Downloads

- **Token link** (from email): `GET /download_model/<token>` — no API key; token is time-limited.
- **Authenticated path**: browser or session-based `GET /download/...` under the user tree — see product docs when exposing zip layout.

Errors return JSON with `status: error`, a `message`, and sometimes a machine `code` (e.g. `quota_exceeded`, `csrf_failed` without API key).
