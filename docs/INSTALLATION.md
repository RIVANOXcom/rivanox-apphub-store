# Install RIVANOX AppHub on ZimaOS, CasaOS or umbrelOS

RIVANOX AppHub is a community application catalog for self-hosted RIVANOX software on home servers and NAS systems. It delivers approved application manifests and container images from GitHub-hosted infrastructure.

## Official community store sources

| Operating system | Catalog format | Source URL |
| --- | --- | --- |
| ZimaOS (ZIP-based clients) | App Store legacy v1 ZIP | `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip` |
| ZimaOS (v2-compatible clients) | App Store v2 static JSON | `https://rivanoxcom.github.io/rivanox-apphub-store/store.json` |
| CasaOS | App Store v1 archive | `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip` |
| umbrelOS | GitHub Community App Store repository | `https://github.com/RIVANOXcom/rivanox-apphub-store` |

**For ZimaOS and CasaOS, verify that the corresponding generated URL returns a published file before registering the source.** A GitHub repository containing source definitions is not automatically a live v2 or v1 catalog.

## ZimaOS — add the community store

1. Sign in to the ZimaOS dashboard and open **App Store**.
2. Open **Community Store** or **App Store Sources**, depending on your ZimaOS version.
3. Choose **Add Source**. For ZIP-based ZimaOS clients, paste the `store/main.zip` HTTPS URL; for v2-compatible clients, use `store.json`.
4. Confirm and refresh the App Store view.
5. Review the store entry and any approved apps displayed by your OS version.

## CasaOS — add the app store source

1. Sign in to CasaOS and open **App Store**.
2. Choose **+ Add Source**.
3. Paste the CasaOS `store/main.zip` HTTPS URL.
4. Confirm and refresh the store.
5. Review the source and any approved apps listed by your OS version.

## umbrelOS — add the community app store

1. Open the umbrelOS **App Store**.
2. Open the menu in the top-right corner (**•••**), then choose **Community App Stores**.
3. Paste `https://github.com/RIVANOXcom/rivanox-apphub-store` into the community source field.
4. Select **Add** and, if accepted, open the RIVANOX AppHub catalog.

umbrelOS reads the GitHub repository directly. It expects `umbrel-app-store.yml` at the root and a compatible prefixed folder for every installable app. An otherwise valid empty source might be rejected by a particular client version; source acceptance without an app does not prove installation success.

## Installation principles

- A public app store source does not grant paid product entitlements.
- Public downloads use GitHub and GHCR, never the RIVANOX development Gitea as an end-user registry.
- Each app requires security, licensing, architecture, installation and recovery approval.
- Data retention, backups, restart behavior and update guarantees are defined per application.
- Updating the catalog does not automatically update installed application containers.
- Local HTTP apps must not be exposed directly to the internet unless that configuration is officially supported.

## Verify the complete application experience

A full acceptance test proves that the OS accepts the source, displays a real approved application, downloads pinned public GHCR images without login, installs it through the GUI without a local build, starts it successfully and retains data through restart and tested upgrades. See the [QA store test matrix](QA_STORE_TEST_MATRIX.md).

## Troubleshooting

**Store source cannot be added:** Match the source to the client protocol, not just the OS name. ZimaOS versions that report `zip: not a valid zip file` while reading `store.json` expect a ZIP; retry with `store/main.zip`. Use `store.json` only with v2-compatible ZimaOS. CasaOS uses `store/main.zip`, and umbrelOS uses the GitHub repository URL. Verify the public URL and inspect sanitized client logs.

**Source registers but no applications appear:** The catalog may legitimately have no published application for the selected platform or CPU architecture. Record the registration result and wait for a separately approved product listing.

**Image download is unauthorized:** Verify that the exact GHCR image digest is publicly downloadable without credentials. Never publish tokens in Compose files.

**Need help?** Create a sanitized report in [RIVANOX AppHub Issues](https://github.com/RIVANOXcom/rivanox-apphub-store/issues). Do not share passwords, setup tokens, private files or personal identifiers.
