# Test RIVANOX AppHub in ZimaOS and CasaOS Before the First App Release

The first compatibility milestone is to prove that a device can subscribe to a genuine RIVANOX AppHub source delivered from GitHub. This is separate from validating an actual application install.

This document provides a real, repeatable source-registration test that **does not publish an unapproved application** or invent an image digest.

## 1. Enable GitHub Pages

An authorized repository administrator opens:

`https://github.com/RIVANOXcom/rivanox-apphub-store/settings/pages`

Under **Build and deployment**, select **GitHub Actions** as the publishing source. Save the setting. Public access and the `github-pages` environment must be available.

## 2. Publish the real empty store source

Open:

`https://github.com/RIVANOXcom/rivanox-apphub-store/actions/workflows/publish-registration-catalog.yml`

Choose **Run workflow** on `main`, explicitly check the confirmation checkbox, then start the workflow. The workflow must:

1. Run the automated catalog safety tests.
2. Confirm no installable `Apps/*/docker-compose.yml` is present.
3. Use the official IceWhale v2 build action to generate `store.json` and `index.json`.
4. Generate a ZIP-based CasaOS store archive containing no installable application.
5. Publish the final English homepage and the generated catalog to GitHub Pages.

If a client or build engine rejects an empty catalog, **record that as an interoperability finding**. Do not insert an unapproved application merely to make the test pass. A later approved diagnostic or Media Center app will allow full acceptance testing.

## 3. Verify public files before opening either OS

Open each URL in a private browser window, without signing in to GitHub:

- `https://rivanoxcom.github.io/rivanox-apphub-store/`
- `https://rivanoxcom.github.io/rivanox-apphub-store/store.json`
- `https://rivanoxcom.github.io/rivanox-apphub-store/index.json`
- `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip`

The homepage must display the final English AppHub marketing copy. The JSON endpoints must return valid JSON, and the ZIP link must download a valid ZIP file. HTTP 404, HTML error pages or GitHub login prompts are failures.

The read-only smoke test can also run from GitHub Actions:

`https://github.com/RIVANOXcom/rivanox-apphub-store/actions/workflows/verify-public-store.yml`

Select **Run workflow** with **allow_empty = true**. This verifies public transport and catalog format only.

## 4. Add the store in ZimaOS

1. Open ZimaOS **App Store**.
2. Select **Community Store** or **App Store Sources**.
3. Select **Add Source**.
4. Paste the `store.json` HTTPS URL above.
5. Confirm and refresh.
6. Capture whether the AppHub name is shown and retained after reloading.

If source registration is rejected because the catalog is empty, record the OS version and sanitized error. Actual app listing and install tests remain unverified.

## 5. Add the store in CasaOS

1. Open CasaOS **App Store**.
2. Select **+ Add Source**.
3. Paste the `store/main.zip` HTTPS URL above.
4. Confirm and refresh.
5. Capture whether the AppHub source is registered and retained after reloading.

CasaOS implementations may require at least one installable app in their ZIP. An empty ZIP catalog therefore proves format delivery and may, but does not necessarily, prove source acceptance.

## 6. Close the final installation gate only with a real approved app

Once Media Center or a separately authorized RIVANOX diagnostic application has passed licensing, first-run, image, platform and recovery checks, promote its digest-pinned app entry through the controlled release path. Then test app listing, one-click install, owner setup, read-only media mounts, restart, backup and restore on both systems.

Do not confuse a successful store subscription with a successful product release. Record results in Workbench R029 requirement #2398 and R032 requirement #2399.

## 7. Test evidence to retain

For each OS: exact operating system version, test date, architecture, source URL, publicly served catalog revision, source subscription result, sanitized error/screenshots, and test operator. Do not upload passwords, private media or installation tokens.
