# DOCS-SPLIT-01 — Canonical Docs domain and repository separation

Status: architecture contract; migration NOT executed. Owner decision: 2026-10-12.

## Authority

- `https://docs.gnu6.live/` is the only canonical documentation host. `https://gnu6.live/docs` is legacy debt, not a second documentation product.
- `gnu6.live` owns the main portal, its navigation and domain-level handoff; `docs.gnu6.live` owns the Docs experience. Preserve the ratified responsive animated global navigation and reduced-motion fallback. Seamlessness across native origins requires browser evidence; do not claim persistent cross-origin DOM.
- `engineering-corpus` becomes **content and methodology only**, not a deployable site or frontend repository.
- A separate frontend repository (working name `gnu6-docs-portal`, subject to repo availability/ownership check) owns routes, navigation, animation adapters, rendering, static assets, accessibility and deployment image.

## Export and consumption contract

`engineering-corpus` publishes an immutable, versioned content bundle containing `docs/fr`, `docs/en`, evidence/citation metadata, federation manifests, SHA-256 checksums, SPDX/license attribution and a machine-readable route inventory. Exclude credentials, private evidence and raw workstation paths. The portal pins a Git commit and bundle digest; fail closed on missing/changed content. No runtime mutable GitHub fetch and no automatic source promotion.

The portal renders `/fr/...` and `/en/...` on `docs.gnu6.live`; internal links use the canonical Docs host and relative paths. Cross-site links to `gnu6.live` are explicit navigations. Historical `/docs/...` links require a separately owned redirect/retirement plan and link telemetry before removal; no speculative production rewrite.

## Bounded migration phases

1. **S0 inventory:** enumerate existing routes, assets, nav/Motion contracts, consumers, deploy image, public entrypoints and redirect dependencies. Capture baseline screenshots and regression receipts.
2. **S1 content API:** introduce schema, deterministic bundle exporter, integrity tests and a frozen golden fixture inside `engineering-corpus`; do not delete current frontend yet.
3. **S2 portal:** create/qualify separate frontend repository; import existing approved shell, responsive navigation and Motion identity tokens with provenance; consume S1 offline. Preserve FR/EN parity and source provenance.
4. **S3 parity:** compare legacy/new route maps, metadata, links, CSP, performance, keyboard/screen-reader behavior, reduced motion and browser screenshot matrix. Include native cross-domain transition tests and fallback behavior.
5. **S4 cutover:** after explicit approval, switch Docs deployment ownership to portal artifact, keep rollback and redirect legacy `gnu6.live/docs` only from the `gnu6.live` owner; avoid DNS/TLS/Coolify changes without a separate release gate.
6. **S5 corpus cleanup:** remove generated frontend/dist/site assets and frontend-specific tests only after the portal reproduces all qualified routes and the rollback window closes. Keep content schema and producer tests.

## Invariants

No deletion of the current site before parity; no forced relicensing of third-party code; no rebranding `gnu6.live/docs` as canonical; no changes to Gnosix product-site ownership; no claim that Motion is seamless across origins until observed; no auto-deploy or auto-merge.

## Acceptance evidence

Deterministic content bundle hash, pinned consumer lockfile, route diff, FR/EN link/metadata checks, keyboard and reduced-motion qualification, real desktop/mobile light/dark screenshots, CSP/privacy validation, independent review, production rollback artifact and explicit promotion authorization.
