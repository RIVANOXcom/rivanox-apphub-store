# Verify RIVANOX AppHub Source Registration on ZimaOS, umbrelOS and CasaOS

This is the permanent acceptance procedure for a community store subscription before and after the first public application release.

Source registration is not the same as a successful app installation. No unlicensed Media Center container is required or published by this procedure.

## Test A: umbrelOS — GitHub repository source

The direct repository source does not require GitHub Pages.

1. Open umbrelOS **App Store**, then the three-dot menu → **Community App Stores**.
2. Add `https://github.com/RIVANOXcom/rivanox-apphub-store`.
3. Record whether RIVANOX AppHub is accepted and shown.
4. Check whether the entry survives refreshing or reopening the App Store.

The root `umbrel-app-store.yml` is the definitive identity metadata. Each released umbrelOS app will additionally need a validated `rivanoxapphub-<app>/umbrel-app.yml` plus `docker-compose.yml`. Some umbrelOS versions may not show an empty community store; record this result accurately rather than claiming the source is broken or inventing an app.

## Test B: ZimaOS — test the correct client protocol (ZIP v1 or JSON v2)

1. In [GitHub Pages settings](https://github.com/RIVANOXcom/rivanox-apphub-store/settings/pages), configure **Build and deployment → GitHub Actions**.
2. Open [Publish AppHub Source Registration Catalog](https://github.com/RIVANOXcom/rivanox-apphub-store/actions/workflows/publish-registration-catalog.yml). Run the workflow on `main` and explicitly confirm the publication of an **empty, non-installable catalog**.
3. The job must pass source validation, generate `store.json` and `index.json` with the official v2 build action, package an empty CasaOS ZIP, and deploy the final English AppHub website.
4. In a private browser window verify these HTTPS files return valid, publicly accessible content:
   - `https://rivanoxcom.github.io/rivanox-apphub-store/`
   - `https://rivanoxcom.github.io/rivanox-apphub-store/store.json`
   - `https://rivanoxcom.github.io/rivanox-apphub-store/index.json`
5. Open ZimaOS **App Store → Community Store / App Store Sources → Add Source**.
6. For ZimaOS clients that expect ZIP input, paste `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip`; for v2-compatible clients, paste `https://rivanoxcom.github.io/rivanox-apphub-store/store.json`.
7. If `store.json` returns `zip: not a valid zip file`, the client is parsing the JSON as ZIP: correct the input URL rather than rebuilding the JSON. Record the operating system version.
8. Record source registration, refresh and persistence results.

The IceWhale builder or a ZimaOS version may reject catalogs without apps. That is an interoperability finding, not permission to invent an unapproved release.

## Test C: CasaOS — v1 ZIP source

After the GitHub Pages publication in Test B, download `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip` anonymously and confirm it is a ZIP archive.

In CasaOS choose **App Store → + Add Source**, paste the ZIP URL, confirm and refresh. Record whether the OS accepts a source with zero app entries. CasaOS implementations may require a non-empty app catalog, in which case the full source-registration and installation gate needs a real approved app.

## Automated endpoint smoke test

Open [Verify Live ZimaOS and CasaOS Store Endpoints](https://github.com/RIVANOXcom/rivanox-apphub-store/actions/workflows/verify-public-store.yml), select **Run workflow** with `allow_empty = true`. The workflow checks HTTPS transport, v2 protocol fields, v1 ZIP integrity and the English homepage.

Select `allow_empty = false` after at least one approved app is published. This is a transport/catalog check only; device installation and recovery are independent tests.

## Full application acceptance

After a product passes the R029 Workbench release gate, repeat registration and confirm an approved app listing, anonymous GHCR image digest pull, one-click installation, secure owner initialization, restart/persistence, backup/restore, and upgrade compatibility. Qualify each CPU architecture separately.

Record date, operating system/version, architecture, source URL, GitHub artifact revision, sanitized screenshots/logs and pass/fail in Workbench R029 #2398. Media Center installation evidence belongs to R032 #2399. No customer Gitea download is permitted.
