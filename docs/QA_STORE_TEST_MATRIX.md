# RIVANOX AppHub — ZimaOS, CasaOS and umbrelOS Store Acceptance Matrix

This is the permanent acceptance standard for store-format interoperability and installation reliability. A source-level build or an HTTP 200 response is not equivalent to a successfully installed app.

## Test environments

Test ZimaOS and CasaOS separately on real amd64 hardware or a qualified VM. Repeat on arm64 only after image multi-arch support and appropriate device evidence have been confirmed. Document operating system version, Docker/Compose version, CPU architecture, free disk space, RAM and a non-sensitive identifier for the test run.

## Gate 1: public catalog and transport

| ID | Check | Expected result |
| --- | --- | --- |
| HTTP-001 | Fetch ZimaOS `store.json` without GitHub login | HTTPS 200, JSON with supported protocol fields |
| HTTP-002 | Fetch ZimaOS `index.json` without GitHub login | HTTPS 200, valid app index |
| HTTP-003 | Fetch CasaOS `store/main.zip` without GitHub login | HTTPS 200, valid ZIP with approved `Apps/` entries |
| HTTP-004 | Examine every Compose image reference | Immutable `@sha256` digest; no Gitea Registry reference |
| HTTP-005 | Check manifest sources for setup secrets and `:latest` | None present |
| HTTP-006 | Validate public website links and metadata | No HTTP 404; English descriptions are accurate |

## Gate 2: ZimaOS

| ID | Action | Expected result |
| --- | --- | --- |
| ZIMA-001 | Add the `store.json` source through Community Store | Source accepted and visible |
| ZIMA-002 | Refresh and reopen App Store | Store subscription persists |
| ZIMA-003 | Open approved app listing | Name, description, icon, architecture and version displayed correctly |
| ZIMA-004 | Install approved app with GUI | Image pull succeeds without manual build/login |
| ZIMA-005 | Restart or reboot host | Persistent app data remains intact |
| ZIMA-006 | Update by supported user action | Version and data migration remain consistent |
| ZIMA-007 | Uninstall | Application-owned data retention follows published policy |

## Gate 3: CasaOS

| ID | Action | Expected result |
| --- | --- | --- |
| CASA-001 | Add the `main.zip` source through **+ Add Source** | Source accepted and visible |
| CASA-002 | Refresh and reopen App Store | Store subscription persists |
| CASA-003 | Open approved app listing | Display data and Compose mappings correct |
| CASA-004 | Install approved app with GUI | Image pull succeeds without manual build/login |
| CASA-005 | Restart or reboot host | Persistent app data remains intact |
| CASA-006 | Update by supported user action | No unapproved schema or persistent data loss |
| CASA-007 | Uninstall | No deletion of user-owned media or unrelated folders |

## Gate 4: umbrelOS

| ID | Action | Expected result |
| --- | --- | --- |
| UMBREL-001 | Add the GitHub repository URL in Community App Stores | The source is accepted, or its empty-catalog limitation is recorded |
| UMBREL-002 | Refresh and reopen App Store | The subscribed source persists |
| UMBREL-003 | Inspect an approved app entry | Prefixed app ID, metadata and architecture match the release |
| UMBREL-004 | Install the app through the umbrelOS GUI | Pinned public GHCR images are downloaded without manual building |
| UMBREL-005 | Restart or reboot host | User data remains intact |
| UMBREL-006 | Apply a supported update | Persistent data and migration policy are respected |
| UMBREL-007 | Uninstall | No deletion of unrelated user data |

## Security and commercial verification

- Initial owner enrollment cannot be claimed by the first unauthenticated network visitor.
- Installation secrets are unique per instance, are not embedded in published catalog files, and survive restart.
- Product entitlements distinguish free core and paid functions; downloading an image does not grant an unauthorized subscription.
- HTTPS/TLS requirements, LAN-only ports and read-only media mounts are checked against the actual product's security contract.
- Logs and screenshots used as evidence contain no private files, credentials, user email addresses or setup tokens.
- Store listing remains blocked until the release is explicitly approved and proven by a device-level test.

## Evidence for Workbench

For each test, record date, OS and architecture, image digest, catalog commit or build identifier, pass/fail, non-sensitive screenshots or sanitized logs, and the corresponding R029/R032 Workbench requirement. Failures must remain open until corrected and retested. An empty catalog allows transport and subscription checks only; it cannot close installation acceptance tests.
