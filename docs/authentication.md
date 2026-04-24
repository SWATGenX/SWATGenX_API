# Authentication

[![Subscription](https://img.shields.io/badge/get%20keys-Subscription-7c3aed?style=flat-square)](https://www.swatgenx.com/subscription)
[![Site](https://img.shields.io/badge/SWATGenX-www.swatgenx.com-0f766e?style=flat-square)](https://www.swatgenx.com)

## 🔑 API keys (recommended for scripts)

1. **Create an account** at [swatgenx.com](https://www.swatgenx.com) (sign up / log in).
2. Open **[Subscription](https://www.swatgenx.com/subscription)** — scroll to **API keys** and **Generate** a key. Keys look like `sgx_…` (treat them like passwords).
3. Send the same token in **both** headers on every authenticated request:

| Header | Value |
|--------|--------|
| `Authorization` | `Bearer <sgx_…>` |
| `X-SWATGenX-Api-Key` | `<sgx_…>` |

Also set `Content-Type: application/json` and `Accept: application/json` for JSON APIs.

## 🍪 Session cookies (browsers)

The web UI uses Flask-Login sessions. Script-style clients should prefer **API keys** so they are not tied to browser CSRF flows.

## ✅ Account requirements

- **Verified** email / watershed policy may apply for certain stations on Basic plans.
- **HUC8** model creation requires an **Effective Pro** tier (see main README in this bundle).

## 📁 Environment variables

Use a `.env` file locally (see `../.env.example`). Load it in Python with `python-dotenv` if you like; the example scripts use plain `os.environ` for fewer dependencies.
