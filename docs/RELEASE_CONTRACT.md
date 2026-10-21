# Public AppHub release contract

The public repository is an output channel, not the approval authority. The authoritative Gitea source and R029 Workbench must specify a product ID, immutable source commit and tag, approved version, QA/security/legal/restore results, authorized approver, and publication time.

## Publishing gates
1. Explicit Product Owner approval is present and can be independently verified against the immutable commit.
2. License and distribution rights (including third-party components) are cleared; **UNLICENSED media-center preview must not be listed**.
3. OCI images exist publicly in GHCR at immutable digests, match the approved source, and include SBOM/provenance.
4. Both target platform installers work without a local Git/npm/build step or embedded shared/default credentials.
5. Backups, database migrations, update/rollback policy, persistence and media read-only boundaries have passed device-level tests.
6. The release has a versioned, immutable manifest for each platform; catalog publication happens only after complete verification.

## Planned output adapters
- ZimaOS: `store.json` plus catalog metadata and `Apps/<Product>/docker-compose.yml`.
- CasaOS: generated `store/main.zip` from approved app entries.
- umbrelOS: `umbrel-app-store.yml`, `rivanoxapphub-<app>/umbrel-app.yml`, its compose manifest.

No public application listings are present yet. Publishing an approved catalog entry is **not** the same as automatically upgrading installations.
