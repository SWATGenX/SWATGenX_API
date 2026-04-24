# Example outputs

[![Example models](https://img.shields.io/badge/SWATGenX-Example%20models-0f766e?style=flat-square)](https://www.swatgenx.com/example-models)

## Download real example models (recommended)

**Log in** at [swatgenx.com](https://www.swatgenx.com), then open **[Example SWAT+ models](https://www.swatgenx.com/example-models)**. From there you can browse curated example builds and **download** the packaged outputs directly in the browser — no need to rely on files in this GitHub folder.

That page is the best place to see finished ZIP/layouts that match what the API produces after a successful run.

## Optional: screenshots in this repo

Maintainers may still add **non-sensitive** screenshots under `example_outputs/screenshots/` for documentation, for example:

- `screenshots/model_order_response.png` — JSON from `POST /api/model-settings` showing `order_id` / `task_id`.
- `screenshots/model_orders_list.png` — `GET /api/model-orders` excerpt.
- `screenshots/health_slots.png` — `GET /api/model-orders/health` showing `slots.in_use` vs `limit`.

Do **not** commit API keys, tokens, or full paths under `/Users/...`.
