# Security and responsible use

The SWATGenX API uses **account-bound API keys** for authenticated model-creation requests. API users should **keep keys private**, store them in **environment variables** or **secret managers**, and **never commit** keys or **tokenized download URLs** to GitHub.

Generated model ZIP files may be delivered through **time-limited token URLs**. Treat those URLs as **secrets**.

If you believe you found a **security issue**, please report it **privately** through the contact channel listed on **[swatgenx.com](https://www.swatgenx.com)**. Do **not** open public GitHub issues containing API keys, download tokens, private model outputs, or vulnerability details.

For using the live service (terms, privacy, and what the example code license covers), see **[`API_TERMS.md`](../API_TERMS.md)** in this repository.
