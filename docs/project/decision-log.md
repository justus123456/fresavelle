# Decision log

Last reviewed: 2 November 2026. **Approved** = explicit current user direction (or source handoff expressly identifies it as clear user direction); **provisional** = preference subject to evaluation; **carried forward** = earlier source whose approval needs checking; **proposed** = recommendation awaiting review; **open** = no final decision. None means implemented or tested. Source references: [working agreement](../blueprint/working-agreement.md), [revision 2](../design/Fresavelle_Blueprint.md), [pasted revision](../blueprint/source-pasted-revision-2.md).

## Approved or explicit direction

| ID | Decision | Evidence / boundary |
|---|---|---|
| D-01 | Abuja groceries, foodstuffs, fruit and vegetables; same website and listed prices for households, restaurants and companies; no enforced minimum. | User working instructions and source sections A and preserved 1. |
| D-02 | Guest checkout allowed; wishlist requires an account. | User working instructions. |
| D-03 | Fixed units; baskets have independent stock and do not automatically consume ingredients. | User working instructions. |
| D-04 | Reserve inventory **15 minutes when payment starts**. It is not a payment deadline. | User's newer explicit working instructions and Stage 0 message override older source section A uncertainty about whether/duration. Payment verification continues independently; exact late-success mechanics still require review. |
| D-05 | Show a delivery or pickup estimate before payment; no false guarantee. | User working instructions and source A/D. |
| D-06 | Backend Paystack verification; redirect alone is not proof; handle uncertain/late payment, duplicate events, stock concurrency and refunds. | User working instructions; detailed mechanisms and policy require review. |
| D-07 | Customer tracking; restricted staff/rider interfaces; individual staff accounts and role-based permissions; handover codes for delivery and pickup; silent dashboard notifications. | User working instructions. Exact grant matrix and exceptions remain open. |
| D-08 | Protect customer data, complaint photos, payment information and rider location. | User working instructions. Exact retention and consent open. |
| D-09 | Next.js/React; Python/Django/DRF modular monolith; Supabase PostgreSQL and Storage; Paystack; Resend. | User approved starting stack; no account or connection verified. |
| D-10 | Story-led modern, easy-to-use customer frontend with pictures/background imagery and floating icons where useful. | Latest user design direction. No specific brand assets, fonts, colors or page design approved. |
| D-11 | Stage-by-stage browser review, safe test/sandbox use, no live charges/messages or publishing without instruction; no secret values in chat. | User working instructions. |
| D-12 | No redelivery after a returned failed delivery; customer may place a new order. | Source revision 2 section A explicitly identifies user direction. Fee/refund policy details still require review. |
| D-13 | Admin implementation is a later stage; read the dashboard reference and inspect both original videos first. | User's earlier explicit request and root AGENTS.md. |

## Provisional preferences and carried-forward details

| ID | Topic | Status and dependent gate |
|---|---|---|
| D-14 | Render for frontend/backend hosting | Preferred, not provisioned; select plan and review costs before hosting. |
| D-15 | SMS provider | Termii provisional; review current pricing, sender requirements and Nigerian network testing before selection. |
| D-16 | Exact session durations, OTP limits, guest-cart retention/merge, operating hours, 20-unit large-order threshold, location staleness, contact attempts, complaint closure and notification retention | Carried-forward figures; the source itself warns some approvals are missing or conflict. Confirm at the relevant stage. |
| D-17 | One-order-at-a-time guest linking using reference, checkout contact and verification | Proposed direction; bulk discovery is not authorised. Confirm method and recovery before implementation. |
| D-18 | No selected delivery/pickup slots, no automatic inbound email threading, no automated rider assignment/route optimisation or in-app voice at launch | Handoff scope; review if launch scope changes. |
| D-19 | Specific owner/manager/staff grants, advanced CRM, purchasing and financial reporting | Source contains proposed roles and carried-forward scope; exact grants and launch priority remain open. |

## Questions before first build stage

- **Required:** Review the proposed stage plan and request Stage 1 when ready. If the proposed local foundation scope is wrong, state the desired change first.
- **Optional and helpful:** Do you have a logo, brand colors, product photos, or example websites? May clearly labelled sample imagery be used for the first preview? A local mock can proceed without these once Stage 1 is authorised.

## Questions to resolve later, before the affected feature is implemented or enabled

| ID | Open decision | Resolve before |
|---|---|---|
| Q-01 | Customer/team/rider session maximums, inactivity, OTP timing/limits and recovery, including owner recovery; source values conflict. | Identity acceptance, Stage 3. |
| Q-02 | Individual guest-order linking, verification, lost reference and ownership dispute handling. | Guest access, Stage 3. |
| Q-03 | Product categories, options, stock accounting, low-stock thresholds, catalogue content and management permission detail. | Actual catalogue/stock configuration, Stage 2. |
| Q-04 | Guest cart lifetime, consent/duplicate merge, quantity limits and sign-in save continuation. | Persistent cart, Stage 4. |
| Q-05 | Service areas, fees, hours/cut-offs, capacity, pickup and delivery estimate method and fallback. | Real quote/payment, Stages 4–5. |
| Q-06 | Customer edits during pending payment; late-success allocation, multiple successful attempts and provider exception resolution. | Checkout acceptance, Stage 5. The 15-minute hold itself is approved and is not reopened. |
| Q-07 | Refund authority, independence, thresholds, eligibility, cancellation, fee treatment, substitutions, pickup noncollection and disclosure. | Refund/checkout activation, Stages 5–6. |
| Q-08 | Exact team role grants, audit obligations, handover exceptions, rider custody/reassignment and customer-unreachable procedure timings. | Relevant admin/delivery functionality, Stages 3 and 6–8. |
| Q-09 | Map and SMS providers, sender approval, domain, budgets, retention, location update frequency, stale thresholds and real background-device feasibility. | Relevant integration, Stages 3 and 8–9. |
| Q-10 | Complaint closure/reopening and attachment policy; support hours/targets, email reply handling and notification retention. | Support features, Stage 9. |
| Q-11 | Privacy notice, retention/deletion, consent, authorised access, data transfer and incident process. | Data collection/integration design and launch gates; start review before affected features. |
| Q-12 | Backup/restore, recovery objectives, external alerts, incident contacts, service plans and cost limits. | Production readiness and relevant infrastructure stages. |
| Q-13 | Advanced CRM, purchasing, reports, guideline acknowledgements and metrics: priority, scope and owners. | Relevant management stage; launch classification requires owner review. |
| Q-14 | Test coverage goals, exact API/schema, secure auth architecture, workers/scheduler and provider event mappings. | Each technical implementation; proposals require validation against current official documentation. |

Do not interpret an unanswered later question as a blocker for a clearly labelled Stage 1 local prototype. Conversely, a mock preview is not permission to silently implement a later business rule.

## Stage 1 authorisation — 2 November 2026

The owner approved the proposed plan and Stage 1 only. Clarifications: Stage 3 includes logout, session management, recovery and deletion requests; build basic staff controls and email/SMS verification when dependencies require them; Stage 5 includes backend verification, idempotency, duplicate events and uncertain-payment recovery; Stage 7 includes Guidelines and Help Centre publishing, version history and staff acknowledgements. Security, permissions, rate limiting and appropriate tests accompany each relevant stage. Use only references the owner actually supplied. Premium, elegant, phone-friendly, story-led storefront with labelled sample products and placeholder imagery.

