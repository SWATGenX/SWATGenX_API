# Authentication

## API keys (recommended for scripts)

1. Sign in at [SWATGenX](https://www.swatgenx.com), open **Subscription / API keys** (wording may vary), and create a key prefixed with `sgx_`.
2. Send the same token in **both** headers on every request:

| Header | Value |
|--------|--------|
| `Authorization` | `Bearer <sgx_…>` |
| `X-SWATGenX-Api-Key` | `<sgx_…>` |

Also set `Content-Type: application/json` and `Accept: application/json` for JSON APIs.

## Session cookies (browsers)

The web UI uses Flask-Login sessions. Script-style clients should prefer **API keys** so they are not tied to browser CSRF flows.

## Account requirements

- **Verified** email / watershed policy may apply for certain stations on Basic plans.
- **HUC8** model creation requires an **Effective Pro** tier (see main README in this bundle).

## Environment variables

Use a `.env` file locally (see `../.env.example`). Load it in Python with `python-dotenv` if you like; the example scripts use plain `os.environ` for fewer dependencies.
