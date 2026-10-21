# RIVANOX AppHub: Language, Search and Release Publishing Standards

## One canonical language

**English is the canonical language of all public GitHub content.** This includes repository READMEs, product listings, SEO titles and meta descriptions, GitHub Releases, changelogs, workflows, commit messages, issues templates, security instructions, support documentation and public release notes.

Localization of application interfaces can be provided through a separate and explicitly maintained locale system, but repository-facing publishing copy remains final English. Do not commit machine-translated temporary notices, placeholder marketing content, unsupported claims or test-only promotional descriptions.

## Editorial quality standard

Product copy explains the real purpose, supported systems, installation path, security requirements, free vs. paid capabilities and deployment limitations. Use natural search terms including **self-hosted app store**, **ZimaOS**, **CasaOS**, **home server**, **NAS**, **Docker applications** and **GitHub-hosted downloads** only where they are relevant. Avoid repeated keywords, exaggerated performance claims, fabricated screenshots and promises of unattended updates that the client OS does not support.

Every product requires a unique and descriptive final English title, tagline, description, approved icon, documented support URL and version notes before it becomes publicly listed.

## Deployment standard

The public store uses one stable canonical origin:
`https://rivanoxcom.github.io/rivanox-apphub-store/`

Source URLs for ZimaOS and CasaOS are immutable in their *path* and are updated only by controlled publication of generated catalog content. Pages and ZIP content are never hand-edited after release; the repository retains source definitions, and CI performs a reproducible build. Every Docker image in an app manifest is pinned by `@sha256`.

The current licensing and QA authority remains the R029 Workbench. Approval must bind exact source revision, test evidence and public image digests. The existing separate Umbrel Store and internal Gitea preview registry are not customer-facing distribution sources.

## Search and website metadata

The canonical landing page owns `<title>`, description, canonical and OpenGraph metadata, supported-platform copy, WebSite schema, `robots.txt` and `sitemap.xml`. Generated `dist/` includes the same approved landing page alongside ZimaOS/CasaOS catalog artifacts. Broken install links are release-blocking defects.

## Accuracy before publication

Never indicate that an image, App Store source, product tier, target architecture or update channel is live unless a public anonymous fetch, qualified device installation and relevant release checks have succeeded. A successful workflow commit alone is not deployment evidence.
