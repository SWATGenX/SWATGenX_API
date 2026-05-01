# Python examples (`requests` only)

[![requests](https://img.shields.io/badge/HTTP-requests-3775A9?style=flat-square&logo=python&logoColor=white)](https://requests.readthedocs.io/)
[![SWATGenX](https://img.shields.io/badge/API-www.swatgenx.com-0f766e?style=flat-square)](https://www.swatgenx.com)

Run from the bundle root so `os.environ` loads from your shell after `export` or from a tool that reads `.env`.

```bash
export SWATGENX_API_KEY='sgx_…'
export SWATGENX_BASE_URL='https://www.swatgenx.com'
python examples/create_model_by_usgs_station.py
python examples/create_model_by_outlet_huc12.py
```

| Script | Purpose |
|--------|---------|
| `create_model_by_usgs_station.py` | `POST /api/model-settings` |
| `create_model_by_outlet_huc12.py` | `POST /api/model-settings/explorer-watershed` (WBD outlet HUC12) |
| `create_model_by_huc8.py` | `POST /api/model-settings-huc8` (Pro) |
| `list_model_orders.py` | `GET /api/model-orders` (order status / queue rows) |
| `list_user_tasks.py` | `GET /api/user_tasks` (Celery rows + `model_creation_broker`) |
| `model_orders_health.py` | `GET /api/model-orders/health` |
| `task_status.py` | `GET /api/task_status/<task_id>` (pass id on CLI) |
| `cancel_queued_order.py` | `POST /api/model-orders/<order_id>/cancel` |
| `cancel_running_task.py` | `POST /api/model_task/<task_id>/cancel` |
| `download_model.md` | Token URL from email → `curl` / Python streaming download |
| `download_model_by_token_url.py` | `SWATGENX_DOWNLOAD_URL=…` → writes `SWAT_Model.zip` (or `SWATGENX_OUT_ZIP`) |
