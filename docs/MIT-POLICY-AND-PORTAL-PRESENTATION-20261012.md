# GNU6 — MIT policy and documentation presentation brief

Status: proposed, source-qualified; not a production deployment.

## Licensing rule

MIT is the preferred license for first-party material where GNU6 owns sufficient rights. Do not rewrite third-party copyright, notices, vendored code, or existing historical commit attribution. Every repository requires its own license provenance review before changing LICENSE or package metadata.

## Initial local inventory (2026-10-12)

| Repository | Observed state | Next gate |
| --- | --- | --- |
| gnosix | MIT LICENSE, Cargo metadata and README | Synced into federation PR #20; update stale upstream STATUS separately |
| gnostral.rs | MIT LICENSE | Verify package metadata and notices before any change |
| in.gnu6 | No root LICENSE in local checkout | Review ownership, dependency licenses, then consider MIT; federation disabled |
| shelly-gpui | GPL root LICENSE and README | Legal provenance/ownership review; no blanket rewrite |
| blob.in-showcase | Cargo LicenseRef-Proprietary | Separate authorization and ownership review before relicensing |
| system-one-rust | MIT OR Apache-2.0 Cargo metadata | Review third-party and dual-license commitments |

Other repositories and worktrees are outside this first inventory. Existing dirty worktrees are not to be overwritten.

## Presentation direction — docs.gnu6.live

1. Clear FR/EN landing page and persistent source-aware navigation: Start, Projects, Guides, API/SDK, Evidence, Corpus.
2. Project pages with a consistent information architecture: purpose, installation, current capability, status, source revision, license, reproducibility, evidence, limitations.
3. Separate human-readable editorial summaries from pinned upstream Markdown and immutable SHA-256 provenance.
4. Search, responsive navigation, keyboard and screen-reader paths; reduced-motion support and contrast qualification.
5. Build using existing GNU6 design tokens and native static-site toolchain; no ornamental mockups or invented runtime claims.
6. Keep product-site domains separate from documentation and do not link unavailable endpoints as live products.

## Qualification gates

- Source inventory and ownership/license verification per repository.
- Content model and route map; French and English content parity.
- Desktop/mobile light/dark browser review and accessibility audit.
- Build, link, privacy, source pin, and regression checks.
- Independent review and explicit approval before production promotion.

This brief authorizes no DNS, TLS, Coolify, runtime, or production change.
