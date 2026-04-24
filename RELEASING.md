# Publishing updates to GitHub

[![Public repo](https://img.shields.io/badge/GitHub-Vahidr32%2FSWATGenX-181717?style=flat-square&logo=github)](https://github.com/Vahidr32/SWATGenX)

Target remote: **https://github.com/Vahidr32/SWATGenX**

## ⛔ Critical: do **not** push your private monorepo `main` here

If your local repo is **`/data/SWATGenXApp/codes`** (or **VahidMSU/SWATGenX**) and you run:

```bash
git remote add public git@github.com-swatgenx:Vahidr32/SWATGenX.git
git push public main
```

Git sends **every commit on `main`** — thousands of objects, `scripts/google-services/*.json`, etc. GitHub **push protection** will **reject** that (secrets in history, large files). The public repo must contain **only** this folder’s files with a **fresh** history (see below).

## 🛠️ Manual publish with SSH (clean history, recommended)

Use a **new directory** (not inside the monorepo’s `.git`):

```bash
PUB=~/SWATGenX-api-public-only
rm -rf "$PUB"
mkdir -p "$PUB" && cd "$PUB"
git init -b main

rsync -a /data/SWATGenXApp/codes/documents/public_swatgenx_api_examples/ ./
git add -A
git status   # should show only README, examples/, docs/, etc. — no scripts/google-services

git -c user.email="you@example.com" -c user.name="Your Name" commit -m "Initial commit: SWATGenX Model Creation API examples"

git remote add origin git@github.com-swatgenx:Vahidr32/SWATGenX.git
git push -u origin main
```

If GitHub already has a bad partial branch from an earlier attempt, you may need `git push -u origin main --force` once (only for this **small** repo, never force the private monorepo blindly).

## 🔐 Fine-grained personal access token (GitHub)

1. **GitHub → Settings → Developer settings → Fine-grained tokens → Generate**.
2. **Resource owner:** your user (`Vahidr32`).
3. **Repository access:** select **only** `Vahidr32/SWATGenX` (or “All repositories” if you accept broader scope).
4. **Permissions:**
   - **Repository permissions → Contents:** **Read and write** (required for `git push` of files on `main`).  
     This is **not** the same as **Actions** read/write (that only affects workflow YAML / Action runs).
   - **Metadata:** read-only (default) is enough.
5. Save the token and store it **only** on your machine (e.g. `ssl_certificate/public_github_fined_grained_token.json` with key `GITHUB_FINE_GRAINED_TOKEN` — **never** commit that file to the public repo).

If `git push` returns **403 Permission denied**, the token is missing **Contents: Write** or the repo is not included in the token’s repository list.

## 🔗 Permanent link in the monorepo (no rsync)

Keep a **single** working tree: your public clone (e.g. `/data/SWATGenXApp/SWATGenX-api-public-only`) and make the monorepo path a **symlink** into it:

```bash
bash /data/SWATGenXApp/codes/scripts/link_public_swatgenx_api_bundle.sh
```

Then `documents/public_swatgenx_api_examples/` in the private repo resolves to the same files as this directory; edit once, `git add` / `git commit` / `git push` **from the public clone** for GitHub, or use the publish script below (which still works because it follows the symlink).

On a **new machine**, recreate the clone and run the link script again (or `ln -sfn` manually). Relative symlinks assume the usual layout: `SWATGenXApp/codes` next to `SWATGenXApp/SWATGenX-api-public-only`.

## 📤 One-way sync from the private monorepo

From the private checkout (uses `GIT_ASKPASS` so the token is not stored in `git remote`):

```bash
bash /data/SWATGenXApp/codes/scripts/publish_public_swatgenx_api.sh
```

Override token path if needed: `SWATGENX_PUBLIC_GITHUB_TOKEN_JSON=/path/to.json`.

The script clones `Vahidr32/SWATGenX`, copies `documents/public_swatgenx_api_examples/` over the tree (symlink source is resolved), commits if there are changes, and pushes using `GIT_ASKPASS` (token is not embedded in the remote URL).

## 🆕 First-time empty repo

If the GitHub repo is empty, the script creates the first commit on `main` and pushes. Ensure the default branch on GitHub is **main** (GitHub’s default for new repos).
