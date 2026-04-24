# Downloading a completed model

[![Download](https://img.shields.io/badge/flow-email%20%2B%20token-0ea5e9?style=flat-square)](https://www.swatgenx.com)

Completed SWAT+ workspaces are **not** returned inline from `POST /api/model-settings`. Typical flows:

1. **Email** — completion messages include a time-limited **`GET /download_model/<token>`** link (no API key). Use that URL in a browser or `curl -L -o model.zip "https://www.swatgenx.com/download_model/<token>"`.

2. **Web app** — signed-in users can browse **User dashboard → downloads** (exact UI labels vary).

A future API may expose a signed download URL in JSON; until then, treat downloads as **out-of-band** from the creation POST.
