# Fresavelle project plan

Status: **Stage 0 approved; Stage 1 ready for review with setup limitation**, 2 November 2026. All later stages are **planned, not started**. This is a proposal, not authorisation to build, deploy or launch. [Decision log](decision-log.md) · [Readiness register](readiness-register.md) · [Blueprint index](../blueprint/README.md)

## Project conditions

Stage 0 found no application source, package manifest, configured services or running preview in the workspace. The existing project contains the supplied design/reference materials, skills and documentation. No implementation, integration, runtime or browser test has been performed.

At the start of each stage: explain what/why, actions by Codex and owner, and blockers. At the end: report what is real/mocked/disconnected, checks and failures, exact start commands and browser URL once actually known, a click-by-click checklist and expected results. Wait for owner review before the next stage. Do not set up every service at once. No live charges/messages, deployment or publishing without specific instruction.

## Proposed stages

| Stage | Status | Purpose and deliverable | Dependencies and review gate |
|---|---|---|---|
| 0. Blueprint and plan | Completed | Organise source material, decisions, readiness and plan; no code. | Owner reviews plan and open questions. |
| 1. Local foundation and storefront direction | Ready for review | Establish local Next.js/React and Django/DRF foundations, basic health check and responsive customer-facing design preview using clearly labelled sample content. Explore story-led imagery and simple navigation; admin dashboard implementation remains later. | Owner approved this plan and authorised Stage 1 on 2 November 2026. Brand assets/references are useful, not required if labelled samples are acceptable. No external account required for a local mock. Show exact URL and checks when actually running. |
| 2. Catalogue and inventory foundation | Ready for review | Selling options, units, browse/search and inventory model; connect a test database only when required, seed safe sample data and build basic staff controls when inventory needs them; defer the complete admin dashboard to Stage 7. | Approved stage 1; Supabase test setup and catalogue decisions as needed; validate access, prices and stock. |
| 3. Identity, guest access and permissions | Planned | Customer and individual team accounts, guest access, logout, session management, account recovery and deletion requests, and role enforcement; bring necessary email/SMS verification forward with safe test delivery. | Identity/session/recovery rules and role grants resolved before accepting those features; configure relevant test email/SMS only when needed. |
| 4. Cart, wishlist and order quote | Planned | Guest/account cart, account wishlist, price/stock revalidation and delivery/pickup estimates. | Stages 2–3; resolve merge rules, delivery areas/fees, estimates and capacity before real checkout. |
| 5. Checkout, reservations and test payments | Planned | Pending-order snapshots, approved 15-minute stock hold, backend Paystack verification, idempotency, duplicate-event handling and uncertain-payment recovery alongside concurrency protection. | Test provider setup; confirm pending-cart edits, late/uncertain payment and operational exception handling. Run sandbox and concurrency checks. |
| 6. Refunds, reconciliation and order operations | Planned | Safe refund foundation, reconciliation and audited preparation/pickup flows, basic staff controls and permissions, and handover. | Define refund authority and policies before activation. Test refund balance and uncertain outcomes alongside payments; operations review. |
| 7. Admin dashboard and team workflows | Planned | Complete the staff/management dashboard for agreed operations, inventory, alerts and approvals, including Guidelines & Help Centre publishing, version history and staff acknowledgements. | First read admin design reference and inspect both original videos if available. Agree permissions and capability scope; reuse real backend work, label gaps. |
| 8. Riders, delivery and real tracking | Planned | Rider assignments, custody, issues, handover and customer tracking; map integration and honest stale/offline fallback. | Delivery policies, restricted roles, provider selection and real mobile device feasibility tests. |
| 9. Communications and support | Planned | Tested transactional email/SMS, silent team notifications, Contact Us and protected complaints. | Provider/domain setup when needed, privacy and support policies. Identity may need test verification channels earlier; integrate narrowly there rather than blocking on this stage. |
| 10. Management, recovery and launch readiness | Planned | Agreed reports/guidelines and unresolved management functions; restore drills, monitoring, reconciliation, privacy/security, load tests and owner/team acceptance. | Complete per-feature readiness evidence, named owners, policy decisions and sign-offs. Advanced CRM/purchasing/reporting scope requires owner review. |
| 11. Production preparation | Planned | Review provider plans, costs, production configuration and safe launch procedure. | Explicit owner instruction for any deployment or publishing; no automatic launch. |

Ordering rationale: a real catalogue/stock basis precedes order quoting; identity precedes account-specific and team actions; secure checkout and refunds are addressed before fulfilment is treated as launch-ready. Security, permissions, rate limiting, testing, accessibility and error handling accompany every relevant stage. This is a reviewable order, not a rigid promise: thin vertical slices may overlap within an approved stage without bypassing review. No irreversible production work is assumed.

## Inputs for Stage 1

**Needed:** review this proposed plan and explicitly request the first build stage. Confirm any change to its scope if desired.

**Helpful, not blocking a labelled local prototype:** logo/brand assets, product photos and permission to use them, preferred colors or examples, any existing domain/branding, and whether temporary sample imagery is acceptable. No service account, secret, pricing or operational policy is required simply to view a local design foundation.

**Resolve later at the dependent feature:** session and OTP policy; guest-order linking; product stock thresholds; operating hours/areas/fees/capacity; cart merging and pending changes; payment exception and refund policies; SMS/maps selection; privacy, retention, recovery and alert ownership. Full list is in the decision log.

## Review and evidence

Stage 0 checks: reviewed both available revision-2 sources and the later working instructions; preserved both sources; inspected workspace; documented decisions, ambiguities, staging and readiness. Documentation and source-copy integrity checks are recorded in the current response. No browser preview exists at this stage. Completion of this preparation does not mean owner approval or launch readiness.

## Stage 1 review record — 2 November 2026

Storefront foundation and local-only Django/DRF health endpoint created; generated placeholder photos and sample products are labelled. No commerce, account, storage, database, payment or message services are connected. Next.js production build passed; local homepage returned HTTP 200 and contained the sample notice and mobile navigation. Two Django health endpoint tests passed using downloaded wheel archives because the local Python installation is missing Windows virtual-environment and pip launcher files. Python source syntax check passed. Desktop and 390px browser screenshots were captured; visual inspection and a readability/crop refinement followed. No real purchase, payment, phone device or external integration was tested. Owner review remains pending; stop before Stage 2. Standard Python environment setup requires repairing the local Python installation.

Final design-inspector result: 6 rule failures and 8 warnings remained on the automated style rubric, including small text, motion and style conventions. The preview was captured at 1440px and 390px; a real phone and full accessibility audit were not tested. Treat these as review items, not a clean automated design audit.


## Stage 1 homepage revision — 3 November 2026

Awaiting owner review; Stage 2 has not started. Reworked the customer homepage with an ivory/forest-green/lavender palette, brighter hero, individual generated sample product images, category tiles and labelled non-transactional preview controls. Account, search, wishlist, cart and add-to-cart remain disabled; section links navigate within the page.

Verification: Next.js production build passed; local preview returned HTTP 200. Browser checks at 320, 390 and 1440 CSS pixels found no page-level horizontal overflow, four product cards and no broken product images; the preview buttons were disabled. At 390px, 14 successive keyboard-focus targets had visible outlines; first Tab reaches the skip link. The simulated reduced-motion setting and glass backdrop/fallback CSS are present. Automated inspection reported no low-contrast text, but retained style/rubric findings; no full accessibility audit or physical-device test was performed. The earlier Python launcher limitation remains outside this visual revision.

## Stage 1 color refinement — 3 November 2026

Owner requested richer colors, food-photo backgrounds where useful and soft 3D. Increased lavender, coral, sage and warm-grain accents, added subtle category/product depth and used an existing generated sample photo behind the closing panel. Next.js build passed; browser screenshots at 1440px and 390px loaded images and showed no page-level horizontal overflow. No physical-device or full accessibility audit was performed. Stage 1 remains in review.

## Stage 1 reference-led redesign — 3 November 2026

Awaiting owner review. Applied the supplied visual reference's centred sans-serif introduction, large grocery photograph and restrained overlapping category links. On phones the links sit along the bottom of the photograph. The category section uses two distinct photographic panels; products use a simpler grid. The single page notice explains sample data, and the out-of-stock action and other unconnected shopping controls are disabled. Hero and pantry photographs are generated illustrative assets.

Verification: Next.js production build passed. Browser checks at 320, 390 and 1440 CSS pixels found no document horizontal overflow, no broken images, one notice and disabled product controls. The first 12 keyboard focus targets had visible outlines; reduced-motion emulation shortened transition duration. Sample checks measured the hero text at 13.99:1 and lavender panel text at 8.97:1. These are targeted checks, not a complete accessibility audit or physical-device test. Stage 2 remains unstarted.

## Stage 1 motion refinement — 4 November 2026

Added a gentle entrance sequence for the headline, supporting text, main action and hero photo, plus subtle floating category panels that pause on hover or keyboard focus. The production build passed. A phone-width browser check confirmed that a panel's position changes over time and that reduced-motion settings leave the layout still and readable. Stage 1 remains in review.

## Stage 1 storefront refinement — 4 November 2026

Tightened the hero and section spacing, reduced the category overlays, clarified section headings and aligned product details. The production build passed; desktop and mobile browser checks showed no horizontal overflow or broken images. Stage 1 remains open for review.

## Stage 1 approval — 4 November 2026

The user approved the Stage 1 storefront after reviewing the homepage refinements. Stage 2 has not been started.

## Stage 2 implementation — 4 November 2026

Stage 2 uses a local development SQLite catalogue with sample records, fixed units, integer-kobo prices, independent basket stock and Django permission-controlled development management. Search and category filters read from the local Django API. This is not Supabase/PostgreSQL integration; production configuration, role policy and authentication hardening remain open. Customer accounts, cart, payment and the custom dashboard remain later stages.

Stage 2 verification: ten Django tests passed, including public search and category filters, inactive products, non-negative values, staff permission checks, staff creation and stock updates, and independent basket stock. The Next.js production build passed. Local HTTP checks verified filtered storefront responses, the staff login screen, and an honest catalogue-unavailable message when the API was stopped. An automated mobile browser check timed out twice while starting; the Stage 2 layout and complete staff workflow still need manual browser review. PostgreSQL/Supabase has not been tested. Awaiting user review before Stage 3.

## Stage 2 review decisions — 5 November 2026

Status: **Ready for review**, not approved. SQLite is temporary development storage; Supabase PostgreSQL remains the approved database. SQLite checks do not verify PostgreSQL. Connect a separate Supabase test project before Stage 3 and rerun migrations and database-dependent catalogue, validation, permissions and stock tests against PostgreSQL; report results for review. Do not use production credentials or data.

In the future custom dashboard, staff enter prices in naira; the backend stores integer kobo. The current local development management interface asks for kobo. The requested search, catalogue, product details and staff access changes remain part of Stage 2. The user has not approved Stage 3.

## Stage 2 shopping navigation review — 5 November 2026

Stage 2 remains **Ready for review**; do not begin Stage 3 without the owner's approval. The home page retains its hero. Dedicated search and catalogue pages use URL-based search, category and sorting; product details display stored descriptions or a clear placeholder when none exists. The footer links to the existing authenticated, development-only staff interface. Checkout, cart and wishlist remain unavailable.

Review checklist:

- [ ] Search from the header; check the result count, no-results message, clear action, filter/sort controls, URL, refresh and browser Back.
- [ ] Open Shop groceries and a category, then open a product and inspect its unit, price, availability and description or placeholder.
- [ ] Follow Staff sign in; use the local Django superuser or an individually authorised local staff account, then create and update an example product and stock. Basket stock remains independent.
- [ ] Review desktop and phone layouts. Customer account, wishlist, cart and checkout remain later stages.
- [ ] Connect a separate Supabase PostgreSQL test project before Stage 3 and rerun migrations and database-dependent catalogue, validation, permissions and stock tests. SQLite results are not PostgreSQL verification.

Verification: 13 Django tests passed against SQLite, including an isolated staff login/create/update workflow. The Next.js production build passed. HTTP checks covered homepage, search, filtered catalogue, product detail, no results and redirect to staff login. Automated browser checks at 390 and 1366 CSS pixels verified search and filtering without a document reload, URL state, Back navigation and no page-level horizontal overflow. Physical devices and a real staff account workflow were not tested. The database and product records are local examples; Supabase is not connected.
Stage 2 loading refinement — 5 November 2026: catalogue, search and product-detail routes now have accessible skeleton placeholders, with motion disabled when reduced motion is requested. Stage 2 remains Ready for review.

Stage 2 PostgreSQL preparation — 5 November 2026: an opt-in Supabase test configuration and local PostgreSQL driver were prepared; SQLite remains the default and was not reset. The separate project has not yet been connected or tested. Keep the Data API disabled for the test project before migrations, and report PostgreSQL results separately. Django tests request a uniquely named temporary database; provider permissions remain to be verified.

Stage 2 review checks — 5 November 2026: automated browser checks at 390 and 1366 CSS pixels verified header search without a hero or document reload, category and price-sort URL state, refresh, Back and Forward, product detail, no page-level overflow, and the footer link reaching the staff login. The isolated Django staff login/create/update test and all 13 SQLite tests passed. No physical phone or real staff-account workflow was tested. Supabase test settings were validated with a fictional URL only; no Supabase connection, migration, or PostgreSQL test has yet run. SQLite remains untouched and Stage 2 remains Ready for review.
