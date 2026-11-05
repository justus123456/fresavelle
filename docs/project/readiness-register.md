# Pre-launch readiness register

Last reviewed: 2 November 2026. **No launch has been authorised.** A decision and the implementation of that decision have separate statuses. No workstream below is verified merely because it appears here.

Decision status: Open / In progress / Decided. Implementation readiness: Not started / Implemented / Testing / Verified / Blocked / Not applicable (with reason). All owners, approvers and target dates are **unassigned** unless named below. No tests or service configurations have been verified. Suggested roles in the older handoff are not appointments. Evidence lists describe required future proof, not existing results.

| ID | Workstream / affected feature | Decision status | Implementation readiness | Required decision, dependencies and evidence to close |
|---|---|---|---|---|
| PLAN-01 | Staging and review | Open | Not started | Owner reviews stage plan; each stage has actual checks, browser instructions and review sign-off. |
| BRAND-01 | Storefront design | In progress | Not started | Story-led visual direction recorded; logo, photos, usage rights, colors and copy remain open. Evidence: reviewed responsive preview and approved assets. |
| CAT-01 | Catalogue / stock | Open | Not started | Categories, selling options, thresholds and staff controls; test unit clarity, accurate availability, stock changes and concurrency. |
| ID-01 | Accounts / sessions / guest | Open | Not started | Session and OTP limits, guest ownership/linking, team roles and recovery; test expiry, revocation, anti-abuse and cross-user access. |
| INV-01 | Checkout reservation | Decided | Not started | 15-minute hold when payment starts is approved and is not a payment deadline. Depends on stock/checkout and safe expiry/late-payment handling. Evidence: last-item concurrency, expiry and late-success tests. |
| QUOTE-01 | Delivery/pickup estimates | Open | Not started | Areas, fee, hours, capacity and fallback; evidence: accurate reviewed quote shown before payment, including unavailable estimate cases. |
| PAY-01 | Refund permissions / balance | Open | Not started | Approval limits, requester independence and eligible balance; evidence: permission, concurrent refund and uncertain-outcome tests. |
| PAY-02 | Paystack / reconciliation | Open | Not started | Provider mappings, duplicate callbacks, late payments, multiple attempts and substitution top-up; evidence: sandbox success/failure, lost-response and retry/reconciliation tests. |
| OPS-02 | Fulfilment / handover | Open | Not started | Preparation, pickup, custody, handover exceptions and role grants; evidence: valid/invalid transitions and code verification, audited exception. |
| DEL-01 | Riders / real tracking | Open | Not started | Select map, location frequency/retention and stale thresholds; real rider device, denied permission, stale/offline behavior and privacy tests. |
| POL-01 | Customer policies | Open | Not started | Noncollection, cancellation, refunds, substitutions, delivery failure, complaint periods and disclosure; evidence: owner-reviewed policies displayed before payment where required. No-redelivery direction is recorded separately. |
| COM-01 | Email / SMS / notifications | Open | Not started | Test provider selection, sender/domain requirements, templates, retry and silent per-user dashboard alerts; evidence: sandbox messages and delivery/failure records. Termii is provisional. |
| SUPPORT-01 | Complaints / contact | Open | Not started | Evidence access, retention, closure/reopening and response procedure; evidence: private cross-user file tests and accurate outbound status. |
| SEC-01 | Access recovery | Open | Not started | Owner/team recovery and identity-review evidence; test recovery, roles and revocation without bypass. |
| PRIV-01 | Data protection | Open | Not started | Retention, privacy notice, deletion, provider/data transfer and location access; evidence: reviewed policy and tested handling of records, files, logs and backups. |
| REC-01 | Backups and recovery | Open | Not started | Recovery-point objective and backup procedure for database and files; evidence: actual restore drills. |
| OPS-01 | Operational continuity | Open | Not started | Named alert contacts, escalation, continuity and retry schedules; evidence: incident simulation and runbook. |
| INF-01 | Hosting and capacity | Open | Not started | Render/Supabase plans, costs, capacity and permitted environment; evidence: cost review and agreed load tests. Production actions require explicit instruction. |
| API-01 | API / schema / jobs | Open | Not started | Constraints, API contracts, rate limits, event mappings and worker/scheduler choice; evidence: integration and concurrency tests. |
| SEC-02 | Security incident | Open | Not started | Compromised-account and data-incident response; evidence: exercise and contact plan. |
| MON-01 | Monitoring | Open | Not started | External alerts, ownership and thresholds; evidence: demonstrated delivery to the responsible person. |
| ADMIN-01 | Admin dashboard | Open | Not started | Read admin reference and inspect both videos before building; agree feature scope and permissions. Evidence: owner review and relevant access/interaction tests. |
| UAT-01 | End-to-end acceptance | Open | Not started | Assign customer, team, rider and financial sign-off owners; evidence: complete rehearsals and explicit sign-off with unresolved gaps recorded. |

## Use

Update owner, approver and target for each workstream when actually assigned. Change readiness to Verified only with a dated link to real test/review evidence. A blocked row must name its dependency and next action. A Not applicable row must state why. Release decisions require feature-by-feature review; a completed project stage alone is not permission to go live.
