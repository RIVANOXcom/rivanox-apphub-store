# RIVANOX AppHub — Self-Hosted App Store for ZimaOS, CasaOS and umbrelOS

**Discover and install RIVANOX self-hosted applications on your home server, private cloud or NAS.** RIVANOX AppHub is an independently maintained community app store designed for streamlined Docker application installation, predictable updates and transparent release information across supported home-server platforms.

RIVANOX AppHub is the public distribution catalog for RIVANOX software. The developer's Gitea instance is the private build source of truth; approved release packages and container images are delivered to users through GitHub and GitHub Container Registry (GHCR). This store is independent of the separately maintained RIVANOX Umbrel Store.

## Supported platforms

| Platform | Store integration | Source |
| --- | --- | --- |
| **ZimaOS** | Community Store, v2 catalog | `https://rivanoxcom.github.io/rivanox-apphub-store/store.json` |
| **CasaOS** | App Store → Add Source, v1 ZIP | `https://rivanoxcom.github.io/rivanox-apphub-store/store/main.zip` |
| **umbrelOS** | Community App Store repository | `https://github.com/RIVANOXcom/rivanox-apphub-store` |

These are the canonical deployment destinations. **Only use a platform source URL after its artifact has been published and verified**; a GitHub repository containing source files alone is not an installable store.

[Installation instructions](docs/INSTALLATION.md) · [Release and security policy](docs/RELEASE_CONTRACT.md)

## Built for self-hosted software

- **Simple app discovery:** one independent source for supported RIVANOX apps on ZimaOS, CasaOS and umbrelOS.
- **GitHub-hosted downloads:** public distribution uses GitHub and GHCR rather than routing customer container pulls through a private office connection.
- **Traceable release versions:** approved application versions, deployment files and supported architectures are documented together.
- **Security-focused packaging:** public Compose manifests use immutable container image digests, reject shared setup secrets and undergo checks before publication.
- **Persistent self-hosted data:** each application's storage, backup and update behavior is described in its own approved installation documentation.
- **Clear licensing:** free features and optional paid services are documented by the individual product, rather than inferred from download access.

## Add RIVANOX AppHub

### ZimaOS
1. Open **App Store**.
2. Open **Community Store** or **App Store Sources**, then choose **Add Source**.
3. Enter the ZimaOS catalog URL shown above.
4. Confirm, refresh the store, and review the available approved app entries.

### CasaOS
1. Open **App Store**.
2. Select **+ Add Source**.
3. Paste the CasaOS store ZIP URL shown above.
4. Confirm, refresh the store, and review the available approved app entries.

**Platform availability:** An empty catalog or an unpublished endpoint is not a usable app installation channel. A listed app should be installed only after its own security, licensing, device and recovery checks have passed.

## How releases reach the store

```text
RIVANOX Gitea source repository
   → RIVANOX Workbench release approval
   → private GitHub Release Factory
   → GitHub Container Registry (versioned image digests)
   → validated RIVANOX AppHub catalog
   → ZimaOS / CasaOS / umbrelOS
```

The store is a **distribution destination**, not the system that approves or builds products. An upstream tag alone cannot authorize publication. Automatically updated catalog listings do not imply automatically upgraded running containers.

## Project links

- **Public app store:** https://github.com/RIVANOXcom/rivanox-apphub-store
- **Publisher:** https://github.com/RIVANOXcom
- **Issues and support:** https://github.com/RIVANOXcom/rivanox-apphub-store/issues
- **Security and publication checks:** [Release Contract](docs/RELEASE_CONTRACT.md)

**RIVANOX AppHub** — a dedicated self-hosted app distribution catalog for home servers and NAS platforms.
