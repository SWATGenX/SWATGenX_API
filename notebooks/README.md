# Jupyter notebooks

## Start here

| Notebook | Purpose |
|----------|---------|
| **`01_simple_station_model.ipynb`** | Minimal flow: set **USGS station ID** + **API key** → submit → poll until **SUCCESS** / failure → notes on **email / dashboard** download. |

## Run locally (JupyterLab)

```bash
cd notebooks   # or repo root
python3 -m venv .venv && . .venv/bin/activate
pip install jupyterlab requests
jupyter lab
```

Open `01_simple_station_model.ipynb`. Set `SWATGENX_API_KEY` in the environment (or edit the cell), then **Run → Run All Cells**.

## Google Colab

Upload the `.ipynb` to Colab, add a **secrets** or first-cell `os.environ["SWATGENX_API_KEY"] = "sgx_…"`, then run all.

## Honest product note

SWATGenX does **not** return the finished model ZIP in the same HTTP response as the submit. The notebook waits until the **task** is **SUCCESS**, then you collect files via **email link** or the **web app** (see the last markdown cell). A future API could add a signed download URL; until then, this is the supported path.
