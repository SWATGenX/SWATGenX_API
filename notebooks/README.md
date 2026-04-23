# Notebooks

For v1 this bundle uses **plain Python scripts** under `examples/` so users can copy a single file into **Jupyter**, **VS Code**, or **Google Colab** without packaging.

**Colab / Jupyter:** paste the contents of e.g. `examples/create_model_by_usgs_station.py` into a cell, set `os.environ["SWATGENX_API_KEY"]` via Colab secrets, and run.

Optional later: add `01_create_swatplus_model_by_station.ipynb` that `%run` the script or inlines the same `requests` calls.
