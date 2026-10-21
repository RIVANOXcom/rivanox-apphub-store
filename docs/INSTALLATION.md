# Install RIVANOX AppHub on ZimaOS or CasaOS

RIVANOX AppHub is a community application catalog for self-hosted RIVANOX software on home servers and NAS systems. It delivers approved application manifests and container images from GitHub-hosted infrastructure.

## Official community store sources

| Operating system | Catalog format | Source URL |
| --- | --- | --- |
| ZimaOS | App Store v2 | `https://rivanoxcom.github.io/rivanox-apphub-store/store.json` |
| CasaOS | App Store v1 archive | `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip` |

**Verify that each URL returns a real published file before registering the source.** Source definitions in the repository are not equivalent to a live store catalog.

## ZimaOS — add the community store

1. Sign in to your ZimaOS dashboard.
2. Open **App Store** and select **Community Store** (or **App Store Sources**, depending on the installed ZimaOS version).
3. Select the **Add** icon.
4. Paste the full ZimaOS `store.json` URL above.
5. Confirm and refresh the App Store view.
6. Confirm the **RIVANOX AppHub** store appears. Review an individual application's requirements before selecting **Install**.

## CasaOS — add the app store source

1. Sign in to your CasaOS dashboard.
2. Open **App Store**.
3. Select **+ Add Source**.
4. Paste the complete CasaOS `store/main.zip` URL above.
5. Confirm and refresh the App Store view.
6. Confirm the **RIVANOX AppHub** store is registered and displayable. Install only applications with an approved public release.

## Installation principles

- App store subscriptions are separate from paid product entitlements.
- Public downloads use GitHub and GHCR, never the RIVANOX development Gitea as an end-user registry.
- A release is listed only after independent QA, installation, security, license and persistence checks.
- Original media and existing user data must not be modified by a store subscription.
- Updating the catalog does not automatically mean an installed application is upgraded.
- Do not expose local HTTP services to the public internet without the application's documented and supported security configuration.

## Verify an installation

A successful end-to-end acceptance test confirms that (1) the store source is accepted, (2) the approved app listing appears, (3) its pinned GHCR images are anonymously accessible, (4) the application installs without Git, Node.js, npm or local building, (5) its UI opens on the intended LAN address, and (6) data survives reboot, upgrade and recovery tests.

See [Store compatibility and acceptance testing](QA_STORE_TEST_MATRIX.md) for the full test matrix, safety checks and evidence requirements.

## Troubleshooting

**Source cannot be added:** Verify the exact HTTPS URL, HTTP response, TLS validity and client-side source format. ZimaOS requires `store.json`; CasaOS requires a ZIP file. Confirm the corresponding generated artifact exists and is publicly accessible.

**Store appears but no applications are listed:** The catalog may not contain a publicly approved app for the selected platform or architecture. Do not treat a successful source registration as proof of app installation support.

**Docker image pull fails:** Verify the GHCR image is public and the pinned digest supports the device architecture. Never embed personal access tokens inside a public Compose manifest.

**App does not start:** Check platform logs and the application's published requirements, host port availability, volumes, owner initialization and documented memory minimums before retrying.

**Need support?** Open an issue in the [RIVANOX AppHub repository](https://github.com/RIVANOXcom/rivanox-apphub-store/issues), excluding passwords, tokens, private media, device identifiers and other sensitive diagnostics.
