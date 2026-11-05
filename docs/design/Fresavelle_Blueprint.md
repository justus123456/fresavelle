Fresavelle — expanded blueprint, pathways and implementation guide

Revision 2 • 31 October 2026 • Design handoff, not an implemented system

Reading guide and evidence limits

This revision adds explanations, diagrams, relationships, proposed API contracts, setup responsibilities and browser acceptance gates to the earlier summary. The earlier summary is preserved at the end for traceability. This document consolidates available conversation and the existing handoff; it cannot certify that every detail from unavailable earlier messages has been recovered.

Status legend: Confirmed direction = explicit user direction in the available conversation; carried-forward = a detail in the earlier handoff whose original approval should be checked; proposed implementation = an engineering recommendation, not an additional business approval; open = unresolved or conflicting. Nothing here means built, connected, tested or launched.

Read in this order:

Decision conflicts and scope.

Technology responsibilities and architecture.

Customer, team and rider sections.

Operational pathways and exceptions.

Data ownership, relationships and API contracts.

Security, reliability and setup responsibilities.

Staged implementation and launch gates.

Preserved earlier requirements and readiness register.

Diagrams use Mermaid, an editable text diagram format. Open in a Mermaid-capable Markdown viewer to render them. Every diagram also has a prose explanation. This is intentionally suitable for Codex to maintain beside the code.

A. Reconcile these decisions before their dependent features

The following table overrides any implication that all values in the preserved summary are final. Do not silently choose a value because it appears most often.

Topic

Evidence and ambiguity

Implementation boundary

Stock reservations

Early user said “not to reserve”; later repeated proposals use a 15-minute stock hold. “15 minutes is too much” appears during delivery discussion, without an unambiguous replacement stock-hold duration. Delivery slots and inventory reservations are different.

Build configurable inventory controls; confirm whether checkout holds are approved and their duration before enabling checkout. Diagrams show the proposed reservation model conditionally.

Session limits

Visible discussion contains 30-day/14-day limits and a security objection; earlier handoff carries 7-day/24-hour customer limits and shorter team limits.

Do not treat all of these as simultaneously approved. Resolve and record final limits before authentication acceptance.

Historical guest-order linking

Earlier advice alternated between automatic retrieval after extra checks and individual order verification. Later handoff uses individual linking.

Individual reference plus ownership verification is the proposed default; no bulk discovery until policy explicitly settles it.

SMS supplier

SMS required for key events; Termii appears as provisional in the existing handoff.

Evaluate delivery, sender requirements and costs before final selection. Do not mark supplier configured.

Delivery timing

User correctly rejected guaranteed duration because of rain and traffic. Existing handoff carries hours, cut-offs and delay thresholds.

Verify operational hours; show estimates, actual updates and delays rather than a guaranteed arrival.

Detailed operational settings

Original approvals for 20-unit large orders, cart merge max quantity, support-hour targets, 90-day alerts and several pickup rules are not present in full here.

Preserve these as carried-forward settings for review, not invented confirmations.

No redelivery

User explicitly required a new order after failed delivery, with refund. Some earlier copied advice suggested redelivery.

Apply no-redelivery rule. Never revive the contradictory earlier suggestion.

Clear user directions include Next.js/React, Django/DRF, Supabase database and storage, Resend, Paystack, optional customer accounts, wishlist for signed-in customers, individual team accounts, protected complaint images, rider management, silent notifications, editable operational guidelines, no authenticator-app requirement, no enforced purchase minimum, and browser review between build stages.

B. What each technology does

Technology/service

Plain-language purpose

Fresavelle responsibility

Boundary

React

Builds interactive screen components.

Product cards, forms, cart controls, dashboard tables and tracking panels.

Used through Next.js; no separate competing frontend is required.

Next.js

Organises the React website, pages and rendering.

Storefront, customer account, staff dashboard and rider web pages.

May render data or proxy requests, but must not duplicate authoritative payment/stock rules.

Python

Programming language used for backend logic.

Implements Django business services and background work.

Not a hosting service.

Django

Backend application framework.

Accounts, permissions, order workflows, transactions and domain rules.

Primary authority for business actions.

Django REST Framework

Exposes Django functionality through structured HTTP APIs.

Validated requests, authentication, permissions and responses consumed by Next.js.

Hiding a button is not an access-control check.

Supabase PostgreSQL

Hosted relational database.

Stores accounts, inventory, orders, financial records and operational history.

Django migrations own application schema. Proposed design does not require Supabase Auth alongside Django accounts.

Supabase Storage

Stores uploaded files.

Product images and private complaint evidence.

Database stores metadata and access relationships; protected files require backend-authorised access.

Render

Proposed hosting destination for application processes.

Runs Next.js, Django and, when chosen, background workers/scheduled work.

Supabase remains the selected database/file service; “host applications on Render” does not relocate those services. Plans and configuration remain open.

Paystack

Payment provider.

Customer payment interface and authoritative payment/refund results.

Backend verifies result and amount; redirect alone never confirms payment.

Resend

Email delivery service.

Branded confirmation, support replies and operational customer email.

Accepted, delivered and failed are distinct; inbound email threading needs its own design.

SMS provider, selection open

Sends text messages and verification codes.

Transactional SMS and OTP delivery.

Provider delivery conditions and Nigerian network tests must be checked. Termii is only a candidate.

Map provider, selection open

Displays maps and may offer routing/geocoding.

Customer/rider map, location display and destination context.

Does not supply live rider positions; rider device supplies coordinates with permission.

Background worker and scheduler, implementation open

Runs work outside a web request and at scheduled times.

Reconciliation, notification retries, reservation expiry and complaint closure.

Jobs must survive retries and be safe when more than one worker runs.

Cache, only when justified

Stores selected reusable results temporarily.

Catalogue acceleration and shared rate-limiting infrastructure where appropriate.

Never the sole financial or inventory truth; cache product availability is advisory.

Recommended architecture: one modular Django application with clear internal modules, one Next.js application with role-appropriate sections, PostgreSQL and protected file storage. Avoid splitting every module into a separate service at launch.

flowchart TD
    U[Customer, team and rider browsers] --> N[Next.js and React]
    N --> D[Django REST API]
    D --> P[Supabase PostgreSQL]
    D --> S[Supabase Storage]
    D --> O[Persistent background work]
    O --> X[Payment, email and SMS services]
    X --> D
    U --> M[Map display and location permission]
    M --> D

Django records the durable intent before asynchronous work. Provider callbacks return to Django, where authenticity and state are checked. Rider coordinates arrive from the device; the map is a presentation layer. Proposed same-site routing or carefully configured cookies/CORS/CSRF must be designed before production.

C. What every section does

Customer website

Section

What the customer does

Required behaviour

Home and catalogue

Browse groceries, produce and categories.

Mobile-friendly navigation; show selling units clearly.

Search and filters

Find products and inspect availability.

Paginated results, suitable search indexes, empty/error states.

Product details

Select pack/unit, quantity and view price.

Each selling option identifies a purchasable stock unit.

Cart

Adjust/remove goods; return later.

Guest cart supported; revalidate prices/availability at checkout.

Wishlist

Save favourites after signing in.

Preserve intended save action through sign-in; no stock hold.

Checkout

Supply contact/address, choose delivery or pickup, review total and estimate.

No minimum purchase; show delivery fee separately; backend recalculates.

Payment result

See checking, confirmed, unsuccessful or needs-review outcome.

Never imply lost response equals failure. Refresh recovers backend state.

My orders

See authorised history and eligible reorder.

Reorder creates a current cart at current prices/availability.

Guest tracking

Verify access to one order.

Reference/contact/OTP scoped to that order; separate lost-reference recovery.

Live delivery

View relevant status, last update and available rider location.

Stale label; no invented movement; hide tracking after authorised period ends.

Complaints

Report missing/damaged/wrong goods with pictures.

Verify order access and keep private evidence protected.

Contact Us

Send general enquiries.

Confirmation of receipt, anti-abuse limits and shared staff inbox.

Account settings

Manage profile, addresses, sessions, logout and deletion request.

Fresh verification for sensitive changes; active business records handled separately.

Staff, manager and owner workspace

Section

Purpose

Typical actions and controls

Overview

Show actionable workload.

New orders, delayed work, urgent delivery issues and unresolved financial checks.

Orders and preparation

Coordinate picking, packing and pickup/dispatch.

Filter by state, view item snapshots, record holds, validate stage changes.

Catalogue

Manage product presentation and selling options.

Owner/manager edit listings; archive without destroying order history.

Inventory

Explain stock availability and changes.

Receipts, counts, reservations, allocations, damage, quarantine and reviewed adjustments.

Drivers & Deliveries

Manage riders and delivery execution.

Add/deactivate riders, see availability and workload, assign/reassign, tap to call, inspect issues/history.

Customers/CRM

Support customer relationships.

Permission-limited profile/order context; verified ownership required for access changes. Detailed CRM scope needs refinement.

Purchasing

Record replenishment work.

Supplier/receipt workflow is carried-forward scope; fields and approval policy still need design.

Finance and refunds

Track paid amounts, refunds and discrepancies.

Separate approved from processing/completed; restrict exports and financial permissions.

Reconciliation

Investigate mismatches.

Link provider transaction/refund records to local records, assign unresolved exceptions.

Complaints and support

Manage customer issues.

Assign owner, private notes, protected attachments, reply, resolve and reopen.

Contact inbox

Answer Contact Us enquiries.

Branded email replies with honest delivery status; do not imply inbound replies are integrated.

Notification Centre

Surface new work without constant manual checking.

Silent alerts, per-user read/unread, date/time and direct action link. Reading does not complete work.

Guidelines & Help Centre

Teach staff approved procedures.

Search by situation, role and topic; owner/manager publish versions; important changes require acknowledgement.

Reports and exports

Understand business activity.

Define date range, timezone and metrics; restrict data and audit sensitive exports.

Approvals

Separate requests from authorised decisions.

Refunds, adjustments and recovery where policy requires review.

Security and settings

Control access and configurable policies.

Explicit role grants, session revocation, audit and protected owner functions.

Rider workspace

Riders see assigned work, relevant destination/contact information, their availability, issue reporting, handover verification and a prominent call-for-help action. Their assignment remains recorded if they log out or lose connectivity. Location and order access must stop when authorisation ends; a rider must not browse all customers or retrieve the customer's secret handover code.

Proposed permission boundaries

Action

Customer

Rider

Staff

Manager

Owner

View orders

Own/verified only

Assigned deliveries only

Assigned operational scope

Authorised operations

Authorised business scope

Change fulfilment stage

No

Allowed delivery actions

Allowed preparation actions

Valid operational transitions

Valid operational transitions

Assign riders

No

No

Only explicitly granted

Yes within policy

Yes

Publish guidelines

No

No

No

Yes

Yes

Adjust inventory

No

No

Request/limited action per policy

Review/authorise

Review/authorise

Initiate refunds

No

No

Explicit limited permission only

Approval limits unresolved

Authorised limits

Grant manager access

No

No

No

No

Yes

Read complaint evidence

Own case

Only specifically necessary

Authorised case access

Authorised case access

Authorised business access

This is a proposed enforcement matrix based on the design, not a grant of permissions to actual people. Owner access remains audited and constrained by valid state transitions.

D. Customer and operational pathways

D1. Shopping through verified checkout

flowchart TD
    A[Browse and select goods] --> B[Cart]
    B --> W{Save favourites?}
    W -->|Yes| L[Sign in and save wishlist]
    L --> B
    W -->|Continue purchase| C[Checkout details and estimate]
    C --> Q{Price, stock and fulfilment valid?}
    Q -->|No| E[Explain issue and preserve cart]
    E --> B
    Q -->|Yes| P[Pending order and proposed stock hold]
    P --> Y[Paystack payment]
    Y --> V[Backend verifies result]
    V --> R{Verified and fulfilment possible?}
    R -->|Yes| F[Confirm and queue preparation]
    R -->|Uncertain| H[Checking payment]
    R -->|Paid but blocked| O[Operational review and resolution]
    F --> N[SMS and optional email]

Customers may edit the cart before the pending payment snapshot is created. Once payment starts, do not mutate the amount of that payment attempt. Proposed handling for an edit at this stage: return to cart through an explicit change-order action, reconcile the existing attempt and create a new reviewed checkout snapshot when safe. The exact business rule remains open. After confirmation, additional goods require another order; no ten-minute add-on window is assumed.

D2. Lost responses, delayed verification and payment exceptions

flowchart TD
    A[Submit payment-related action] --> B{Response received?}
    B -->|Yes| C[Display server result]
    B -->|No| D[Show checking status]
    D --> E[Lookup original operation and payment reference]
    E --> F{Authoritative result?}
    F -->|Unknown| G[Reconcile and escalate if overdue]
    G --> E
    F -->|Failed| H[Release eligible hold and offer safe retry]
    F -->|Successful| I{Stock and fulfilment still available?}
    I -->|Yes| J[Allocate once and confirm once]
    I -->|No| K[Record paid status and resolve or refund]

A client retry uses the same operation identity for the same action. A new idempotency key is not a substitute for checking an uncertain previous payment. Expiring stock does not declare the payment failed. Multiple successful attempts must be recorded and reconciled; they must not trigger duplicate preparation.

Situation

Customer sees

Backend action

Slow ordinary request

Loading state, then recoverable error if needed

Bounded request, traceable error; safe retry for reads.

Lost order-creation response

“Checking your order. Please wait before trying again.”

Retrieve the operation result using stable identity.

Payment verification unavailable

“We’re checking your payment. Your order is not confirmed yet.”

Keep verification-needed state; retry/reconcile original reference.

Payment confirmed but stock unavailable

“Payment received; we’re resolving an issue with your order.”

Record money received; operational hold and approved resolution.

Notification failed

Accurate order page remains available

Retry notification separately; do not roll back order/payment.

Session expires

Sign-in prompt; preserve safe cart/navigation context

Reauthenticate; recheck permissions before action.

Concurrent staff edit

Explain that order changed and refresh current state

Reject stale update rather than overwrite newer action.

D3. Pickup and delivery progression

flowchart TD
    A[Confirmed] --> B[Preparing]
    B --> C{Fulfilment method}
    C -->|Pickup| D[Ready for pickup]
    D --> E[Verify collection]
    E --> F[Collected]
    C -->|Delivery| G[Ready for dispatch]
    G --> H[Assign rider and record custody]
    H --> I[Out for delivery]
    I --> J{Handover verified?}
    J -->|Yes| K[Delivered]
    J -->|Offline or disputed| L[Pending evidence or manager review]
    J -->|Unreachable after procedure| M[Return and refund review]

Holds are recorded separately with reason, responsible person, start time and previous stage. Clearing a hold resumes only a valid state; it must not bypass payment or handover checks. Cancellation is permitted only under the applicable stage policy and does not mean money is refunded.

D4. Rider assignment, delays and tracking

flowchart TD
    A[Ready delivery] --> B[Staff reviews rider availability and workload]
    B --> C[Assignment and custody recorded]
    C --> D[Delivery in progress]
    D --> E{Fresh location?}
    E -->|Yes| F[Show actual location and update time]
    E -->|No| G[Mark stale and alert per thresholds]
    D --> H{Issue reported?}
    H -->|Yes| I[Contact team and record action]
    I --> J{Reassignment needed?}
    J -->|Yes| K[Authorised reassignment and custody transfer]
    K --> D
    H -->|No| L[Continue to verified handover]

Availability values are Available, On delivery, Unavailable and Off duty, with update time. Available is not a capacity guarantee. Multiple orders require staff judgement. Rain, traffic and breakdowns change estimates; staff communicate delays. Two-minute stale and five-minute alert thresholds are proposed configurable values. Tracking reliability on locked/background mobile browsers is a launch feasibility test, not a promise.

For an unreachable customer, follow the approved contact procedure and log actual attempts. The carried-forward procedure is three rider attempts over five minutes plus a team attempt; verify that precise timing before configuration. Returned goods enter inspection/quarantine. No redelivery; customer may place a new order. Refund product costs according to eligibility and disclose delivery-fee treatment; Fresavelle-caused complete failure refunds the full amount.

D5. Refund processing

flowchart TD
    A[Refund request and affected items] --> B[Review amount, reason and authority]
    B --> C{Approved?}
    C -->|No| D[Rejected with audit reason]
    C -->|Yes| E[Reserve refundable balance atomically]
    E --> F[Initiate provider operation]
    F --> G{Outcome known?}
    G -->|No| H[Initiation under review]
    H --> I[Reconcile before retry]
    I --> G
    G -->|Processing| J[Await verified final status]
    J --> K{Completed?}
    K -->|Yes| L[Record completion and notify]
    K -->|Failed| M[Investigate and safely resolve]

Calculate eligible balance per successful payment: paid amount minus completed refunds minus approved/in-flight/uncertain refund commitments. Do not release an uncertain commitment solely because a request timed out. Partial refunds can leave a valid remaining balance. Separate request, approval, provider initiation and completion, preserving actors and timestamps. Automatic restocking is not a consequence of issuing a refund.

D6. Complaint and customer-contact handling

flowchart TD
    A[Verified complaint or Contact Us message] --> B[Record case and assign owner]
    B --> C[Investigate and request information]
    C --> D{Financial remedy needed?}
    D -->|Yes| E[Linked refund workflow]
    D -->|No| F[Record customer-facing resolution]
    E --> F
    F --> G[Notify customer]
    G --> H{Customer replies or reopens?}
    H -->|Yes| C
    H -->|No after approved closure period| I[Close case]

Complaints about an order require verified ownership. A general contact message does not establish ownership just by quoting an order reference. Internal notes stay private. Attachments require size/type limits, validation, private access and retention rules. Closure after seven days is a proposed starting policy; the preserved summary adds delivered-notification gating, which needs confirmation. Refund completion does not automatically resolve a complaint.

D7. Guidelines and silent notifications

flowchart TD
    A[Manager or owner edits draft] --> B[Publish immutable guideline version]
    B --> C[Notify relevant team members silently]
    C --> D[Individual read status]
    B --> E{Acknowledgement required?}
    E -->|Yes| F[Record each required person's acknowledgement]
    E -->|No| G[Reading is optional acknowledgement-free guidance]
    F --> H[Report outstanding acknowledgements]

Each article should include situation, responsible role, steps, escalation contact, customer wording, related links and last update. Important versions may require acknowledgement; minor corrections need not. Acknowledgement names the exact version. Publishing wording does not change executable business rules: a new cancellation rule also needs configuration/code review and tests.

Notification event, recipient read state, acknowledgement and underlying task status are separate records. For example, three staff can read “New order” while that order remains unprepared. Record created time and seen/read time individually. No sound alerts.

E. State ownership, persistence and concurrency

State/data

Authoritative owner

Lifetime and refresh

Who changes it?

Concurrency rule

Open menu, selected tab, modal

React component

Temporary; normally reset on refresh

Current browser user

Local only.

Search/filter/page

URL plus frontend

Survives refresh/share when in URL

Current browser user

Server validates filters.

Unsaved form

Frontend; optional scoped draft

Explicit draft policy; never store sensitive secrets

Current browser

Warn about unsaved work where valuable.

Guest cart

Proposed backend cart with opaque browser identifier

Carried-forward 30 days; same-browser recovery

Guest requests

Version/atomic update; reprice at checkout.

Account cart/wishlist

Django/PostgreSQL

Across sessions/devices

Verified owner

Unique item membership; safe merging.

Dashboard copy of an order

Frontend cache

Refreshable copy only

Backend publishes/fetch returns

Invalidate/refetch after mutations.

Orders, stock, payments/refunds

Django/PostgreSQL

Persistent with policy-based retention

Authorised actions, jobs and provider updates

Transactions, locks/constraints, idempotency.

Sessions and challenges

Backend

Explicit expiry/revocation, survives refresh while valid

Authentication services

Single-use challenge consumption atomic.

Live location

Backend plus transient display

Freshness and retention policy required

Assigned rider/device

Reject unauthorised/obsolete updates; timestamp validated.

Complaints and guidelines

Backend

Persistent, versioned where required

Permitted roles and verified customer

Audit changes; published versions immutable.

Notification read state

Backend, per recipient

Survives refresh/device switch

That recipient

Reading does not clear another person's unread state.

Shared application data is not synonymous with temporary frontend state: the order list may be cached in the browser, but the durable order belongs to the backend. Cache expiry must never reverse a paid order or revoke a recorded handover.

F. Proposed database relationships

These diagrams show conceptual relationships; implementation must still specify nullable fields, constraints, deletion policies, indexes and migrations.

Identity and order ownership

erDiagram
    ACCOUNT ||--o| CUSTOMER_PROFILE : has
    ACCOUNT ||--o| TEAM_PROFILE : has
    ACCOUNT ||--o{ ROLE_ASSIGNMENT : receives
    ACCOUNT ||--o{ CONTACT_METHOD : registers
    ACCOUNT ||--o{ SESSION : opens
    ACCOUNT ||--o{ ORDER_ACCOUNT_LINK : verifies
    ORDER ||--o| ORDER_ACCOUNT_LINK : has_owner
    ORDER ||--|{ ORDER_ITEM : snapshots

One account can have customer and team profiles, but team permissions require an authorised role assignment. A guest order has no account link until verification. At most one active customer ownership link per order is the proposed constraint; transfers require an audited dispute process. Roles should not be a single string that prevents legitimate multiple responsibilities.

Catalogue, inventory and payments

erDiagram
    PRODUCT ||--|{ SELLING_OPTION : offers
    SELLING_OPTION ||--o{ STOCK_MOVEMENT : records
    SELLING_OPTION ||--o{ RESERVATION_ITEM : held_by
    RESERVATION ||--|{ RESERVATION_ITEM : contains
    ORDER ||--o{ RESERVATION : tracks
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER ||--o{ PAYMENT_ATTEMPT : attempts
    PAYMENT_ATTEMPT ||--o{ REFUND : funds
    PAYMENT_ATTEMPT o|--o{ PROVIDER_EVENT : correlates
    REFUND ||--o{ REFUND_HISTORY : records

Provider events may arrive before correlation is possible, so store valid uncorrelated events for investigation. Refund events also need correlation to their refund; a generic provider-event record must support both types. Preserve original product names, unit descriptions and integer-kobo prices on order items even when catalogue entries are renamed or archived.

Inventory balances need one explicit accounting convention. Proposed formula, if on-hand includes both held and allocated goods: available = sellable on-hand − active reservation quantity − committed allocation quantity. Shipping then reduces on-hand and clears that allocation in one consistent operation. Never subtract the same quantity as both custody and commitment. Returned goods are not sellable until inspection.

Operations and communications

erDiagram
    ORDER ||--o| DELIVERY : uses
    DELIVERY ||--o{ DELIVERY_ASSIGNMENT : histories
    TEAM_PROFILE ||--o{ DELIVERY_ASSIGNMENT : assigned
    DELIVERY ||--o{ LOCATION_UPDATE : tracks
    ORDER o|--o{ SUPPORT_CASE : concerns
    SUPPORT_CASE ||--o{ CASE_MESSAGE : contains
    SUPPORT_CASE ||--o{ ATTACHMENT : protects
    GUIDELINE ||--|{ GUIDELINE_VERSION : versions
    GUIDELINE_VERSION ||--o{ ACKNOWLEDGEMENT : records
    NOTIFICATION ||--|{ NOTIFICATION_RECIPIENT : targets

Custody events, delivery issues and handover proofs supplement delivery assignments. Case messages distinguish public reply from internal note. Notification delivery attempts to SMS/email are separate from staff recipient read status. Records not drawn include addresses, carts, recovery reviews, audit history, reconciliation runs and outbox jobs.

Essential constraints and index candidates

Unique order reference; unique provider transaction identity within the appropriate provider/environment scope.

Unique idempotency scope/key, storing request fingerprint and operation result. Same key with a different payload is rejected.

Nonnegative stock quantities and valid allocation totals according to the chosen accounting convention; positive purchasable quantities.

Integer-kobo financial amounts and explicit currency; protect aggregate refund balance under concurrency.

One active ownership link per order; unique wishlist account/selling-option pair and acknowledgement account/version pair.

Index order status/created time for queues, customer link/order date for history, rider assignment/status for work, and reservation status/expiry for cleanup.

Index payment reference, refund state, provider processing state, case assignee/state and recipient/unread/created time.

Design text search from actual catalogue queries; use query plans to validate indexes. Avoid adding indexes indiscriminately.

Preserve financial snapshots and audit history; deleting an account must not cascade-delete orders, refunds or necessary evidence.

G. Proposed API surface and request rules

Routes below are design proposals, not existing endpoints. Use a consistent /api/v1 prefix. Resolve authentication and exact schemas before implementation.

Area

Example route/action

Access and outcome

Catalogue

GET /products, GET /products/{id}

Public, paginated, availability advisory.

Cart

GET /cart, PATCH /cart/items/{id}

Owning account or scoped guest cart; version-aware update.

Wishlist

POST /wishlist/items, DELETE /wishlist/items/{id}

Signed-in owner only.

Accounts

POST /auth/register, /auth/login, /auth/logout

Validate, throttle, secure sessions.

Sessions

GET /auth/sessions, DELETE /auth/sessions/{id}

Own sessions; protected all-device revocation.

Recovery

POST /auth/recovery/request, /auth/recovery/complete

Generic initial response; purpose-bound verification.

Guest access

POST /guest-orders/access/request, /access/verify

Specific order/contact challenge, scoped access.

Checkout

POST /checkout/quote, POST /orders

Server-calculated quote and idempotent order creation.

Payment

POST /orders/{id}/payment-attempts, GET /payment-attempts/{id}

Authorised order; prevent unsafe concurrent attempts.

Webhooks

POST /integrations/paystack/webhook

Provider authentication, durable intake and deduplication.

Order action

POST /orders/{id}/transitions

Explicit allowed action, expected version and actor permissions.

Refund

POST /orders/{id}/refunds, POST /refunds/{id}/approve

Separate request/approval/initiation authority and balance checks.

Riders

GET /riders, POST /deliveries/{id}/assignments

Authorised team only; reassignment history.

Delivery

POST /deliveries/{id}/locations, /issues, /handover

Assigned rider and permitted actions; location is not delivery proof.

Support

POST /contact-messages, POST /orders/{id}/complaints

Public contact versus verified order complaint.

Case reply

POST /support-cases/{id}/messages

Enforce public/internal visibility and sender permissions.

Guidelines

GET /guidelines, POST /guidelines/{id}/publish

Role-relevant read, owner/manager publish.

Acknowledgement

POST /guideline-versions/{id}/acknowledgements

Current user acknowledges exact published version.

Notifications

GET /notifications, POST /notifications/{id}/read

Recipient only; no underlying task mutation.

Account deletion

POST /account/deletion-requests

Fresh verification and policy-driven processing.

Common contract: stable error code, readable message, field errors where appropriate, request/operation reference and authoritative current state when relevant. Return an asynchronous operation identifier when work continues. Authorisation is checked on every referenced record, including attachments and downloads. Rate-limit signals should include a retry delay without exposing private account existence.

H. Security and reliability are part of every stage

ACID and concurrency. Commit order snapshots and chosen stock allocation atomically. Lock or atomically update relevant stock/refund balances; process records in a consistent order to limit deadlocks. Store a durable notification/job intent in the same transaction. Perform slow external calls outside locked database transactions. A database transaction cannot roll back a payment already processed by Paystack; reconciliation resolves that boundary.

Idempotency. Stable operation identifiers protect order creation, payment initiation, refunds, handover and notification processing. Database uniqueness and conditional transitions back up application checks. A repeated event may be safely acknowledged without repeating its business effect. Do not assume every provider event includes a unique event ID.

Authentication and abuse control. Secure HttpOnly cookies, HTTPS, CSRF protection where cookie authentication is used, explicit allowed origins, password hashing, permission checks and session revocation. Rate-limit login, OTP issue/verify, recovery, guest tracking, contact forms, uploads and sensitive actions using relevant account/contact/IP signals. Distributed instances require coordinated limits. Protect short OTPs against offline brute force using an appropriate keyed/protected verifier, expiry and atomic one-use consumption; do not log secrets.

Files and data. Validate uploads, restrict file size/type, generate server-owned paths, prevent cross-customer access and use expiring authorised downloads where appropriate. Keep storage service credentials server-side. Retention and deletion policies must cover records, files, logs and backups.

Caching. Cache public catalogue data when beneficial, invalidate or revalidate on catalogue changes, and isolate private data. Always recheck authoritative price, stock, ownership and refundable balance during mutations. Never reuse one customer's authenticated response for another.

Outages and jobs. Define bounded retries with backoff, escalation for stuck jobs, monitoring and durable recovery. Restore-test database and uploaded files. During recovery reconcile uncertain payments/refunds, expired holds, orders, delivery custody and notification queues. Two-hour service recovery is a target, not a guarantee; recovery-point objective remains open.

Acceptance evidence. Test two buyers for the last item, two refund requests for the same balance, duplicate webhooks, a lost successful response, expired reservation followed by late payment, inaccessible private attachments, revoked sessions, invalid role actions and stale rider coordinates. Include these beside the relevant feature; do not defer all security until launch.

I. What the owner sets up, and what Codex builds

This is a setup sequence, not verified current provider-console instructions. At each integration stage Codex should check current official documentation and provide the exact steps for that stage. No accounts, domains, subscriptions or integrations are asserted to exist.

Service

User/owner action

Codex implementation

Evidence before moving on

Repository and local environment

Choose repository/access and development machine context.

Inspect workspace, establish Next.js/Django structure, README and environment template.

Both apps run; exact browser URL and health result supplied.

Supabase database

Create/select project, choose appropriate region/plan, securely provide connection configuration.

Django connection, migrations, minimum permissions, seed data and backup plan.

Application persists real test data and migration is repeatable.

Supabase Storage

Create/select image and private evidence buckets with reviewed policy.

Authorised upload/download routes and metadata records.

Owner can access own evidence; another customer cannot.

Render

Create/select account and approve service/budget choices.

Build/start commands, Next.js and Django services, secrets, workers, health checks.

Approved staging deploy works over HTTPS.

Paystack

Complete required business/provider setup and obtain test configuration securely.

Test checkout, verification, webhook, refund and reconciliation.

Test success, failure, lost response and duplicate handling pass.

Resend and domain

Control sending domain and add requested DNS records.

Branded templates, send job, delivery-event handling and retry records.

Approved test recipient receives expected design; failures visible.

SMS

Choose tested provider and complete sender/account requirements.

Adapter, OTP/transactional templates, receipts and limits.

Tests on relevant Nigerian networks; cost and failures understood.

Maps

Choose provider, budget and allowed domains.

Restricted map integration, real device location ingestion and privacy rules.

Actual rider device, stale position and permission denial tested.

Operations

Name staff owners, support contacts, policies and escalation paths.

Configurable settings, runbooks, permissions and monitoring.

Team can follow an incident exercise.

Store secrets in local environment files excluded from version control and hosting secret settings. Do not paste passwords, private keys, OTPs or live customer data into chat. Tell the user exactly which variable is needed, where to obtain it, where to put it and how to check it without printing its value. Use test providers or clearly labelled adapters until real integration is approved.

J. Stage-by-stage build and browser review

Working agreement: finish one reviewable stage, run appropriate checks, provide the exact running URL and test instructions, then wait for the user's review before beginning the next stage. Changes requested during review belong to the current stage. A mock must be labelled; a frontend success animation is not proof that a backend integration works.

Stage

Deliverable

User browser review

Technical acceptance

0 — Reconcile and prepare

Resolve stage-blocking decisions; repository, plan and environment checklist.

Review navigation plan and selected scope.

Decision log identifies conflicts; no unapproved defaults hidden.

1 — Application foundation

Next.js/React shell and Django API, responsive customer/team/rider layouts.

Open provided URL on desktop/mobile; check navigation and basic brand direction.

Build/health checks; mocks labelled; configuration documented.

2 — Identity and permissions

Accounts, guest context, sessions, verification and roles.

Sign in/out, verify guest access, test role-specific screens and expiry.

Backend authorisation, OTP limits and revocation tests.

3 — Catalogue and stock

Products, selling options, imagery, search and inventory controls.

Add/update product, search, inspect low/out-of-stock and unit clarity.

Constraints, queries and private/public file boundaries.

4 — Cart, wishlist and checkout

Persistent cart, account wishlist, delivery/pickup quote and snapshots.

Guest return, sign-in/save, merge review, fee and unavailable item cases.

Repricing, ownership, concurrency and approved stock rule.

5 — Payment and refund foundation

Paystack test integration, verified confirmation, reconciliation and refunds.

Complete test payment and inspect checking/failure/refund messages.

Duplicate/lost response/late success and refundable balance tests.

6 — Preparation and pickup

Work queues, transitions, holds and collection proof.

Follow order from confirmed through preparation and collection.

Invalid transitions rejected; audit and persistent state verified.

7 — Drivers and delivery

Rider management, assignment, contact, issue handling and handover.

Staff assigns; rider accepts work; customer tracks and confirms handover.

Scoped data, custody, reassignments and offline pending handling.

8 — Maps and live updates

Real position display and fallback behaviour.

Test real devices, deny permission, interrupt connectivity, inspect stale label.

Privacy window, accuracy/freshness and background feasibility.

9 — Communications and support

Resend/SMS, silent alerts, contact inbox and complaints with pictures.

Read/unread isolation, branded reply, upload evidence and reopen case.

Retry safety, no duplicate sends, honest delivery status and private files.

10 — Guidelines and management

Versioned help centre, acknowledgements, agreed reports/settings.

Publish important/minor versions and check role-specific acknowledgements.

Version identity, permission and report calculation tests.

11 — Launch readiness

Restore exercise, load checks, monitoring, runbooks and acceptance sign-off.

Full customer/staff/rider rehearsal and final requested changes.

Every enabled feature's launch gate verified with recorded evidence.

Provider email/SMS may be wired earlier when identity needs it, while broader communications are reviewed in stage 9. Security and auditing are built throughout. Purchasing, advanced CRM and financial reporting require explicit detail before their implementation; their mere presence in the navigation is not completion.

At each stage Codex reports: what changed; what is real versus mocked; checks passed/failed; exact URL; numbered browser actions and expected outcomes; remaining limitations; user setup needed now. Do not ask the user to configure every service on day one.

Copyable Codex instruction

Read this blueprint and the preserved requirements. Treat section A as the override for conflicting decisions. Inspect the existing repository before choosing implementation details. Use Next.js/React, Django/DRF and the selected providers; propose any change explicitly. Build in the stages above, with security, ACID transactions, indexes, idempotency, rate limits and failure handling included with each relevant feature. Before each external setup, explain the service, required account settings, secure configuration steps and how we will test it using current official documentation. After each stage, run checks and give me the exact browser URL, what to click and expected outcomes. Wait for my review before moving to the next stage. Label all mock behaviour and do not claim provider connections or production readiness without evidence. Keep this blueprint, a decision log and launch register updated. Resolve only decisions blocking the current stage; avoid repeatedly asking me to approve already-settled rules.

K. Completeness and final handoff checklist

Topic requested in discussion

Where covered

Technology choices and their purpose

B, I

Customer, staff, manager, owner and rider sections

C

Pathways and diagrams

D, F

Account, session, recovery and guest ownership

A, E, G, H; preserved section 5

Checkout, payment uncertainty and refunds

D1–D2, D5, F–H

Inventory and reservations

A, F, H; preserved sections 3 and 6

Driver management, live map and failed delivery

C, D3–D4; preserved section 4

Complaints, photos and Contact Us

C, D6, G

Guidelines, acknowledgement and silent notifications

D7, E

Database relationships, indexes and APIs

E–H

Security, ACID, idempotency, rate limits and caching

H

Setup help and browser review between stages

I–J

Launch decisions, ownership and evidence

Preserved section 9 plus A and J

Remaining unspecified detail

A and stage blockers; never silently invented

The design is ready to guide staged implementation after the first-stage conflicts are addressed; it is not a claim of exhaustive recovery of all earlier conversation or a final executable schema. Celebrate the team's contributions at the end of the agreed work, as requested: “To everyone who helped shape Fresavelle—and to building something customers and the team can trust.”

Appendix — preserved earlier summary and readiness register

The text below is retained for traceability. It is subject to the conflict/status notes in section A and is not independent proof that every listed detail was finally approved.

Fresavelle system design and pre-launch readiness register

Working handoff for Codex · 31 October 2026

How to use this document

This is a consolidated starting specification assembled from the decisions visible in the current conversation. It is not a verbatim transcript, a completed implementation, or an independently verified full history. Some earlier discussion was not available in full; confirm missing details before implementation. Approved means approved for design, not built or tested. Suggested names, owners and technical implementations are not appointments or completed work. More recent explicit decisions override earlier summaries.

1. Business and scope

Fresavelle sells its own groceries, foodstuffs, fruit and vegetables in Abuja at launch, to households, restaurants and companies at the same listed prices. Use web and mobile browsers; no native app is selected.

No enforced minimum for any customer; even orders of ₦3,000 or less are permitted. Show delivery fee separately before payment; no delivery fee for pickup. Large orders depend on stock and fulfilment capacity. No special business enquiry form; normal orders go through checkout. General Contact Us is included.

Products: configurable categories and listings by owner and manager; pieces, fixed-weight packs, other packs and baskets. One product may have several fixed selling options, each with its own price and stock. No variable-weight pricing. Baskets have their own counts, with no automatic ingredient deduction.

Customers see low-stock indicators and out-of-stock products; owners/managers receive configurable low-stock alerts. Exact thresholds and alert channel remain open.

2. Technology and components

Frontend Next.js and React; Django, Python and Django REST Framework backend as a modular monolith; Render preferred for frontend and backend; Supabase PostgreSQL and Storage; Paystack payments; Resend email; Termii provisional SMS subject to rate and network tests; maps provider open.

Customer storefront, management dashboard, mobile-friendly rider page, backend/API, database, protected file storage, payment, email, SMS and map dependencies. Build and validate real integrations; do not claim any are already configured.

Owner, manager, staff and rider have individual accounts. Shared account system with separate profiles and explicit roles; customer and team capabilities may coexist only after authorised assignment. Owner alone promotes managers and controls delivery areas and charges. Owner and manager manage products and categories and approve staff stock adjustments; refund authority limits remain open. Rider access restricted to assigned work.

3. Customer shopping and checkout

Guests can browse, use a cart and check out without registering. Guest cart retained for 30 days after last change in same browser where identifier persists. Account cart and wishlist persist across devices; wishlist requires sign-in. Preserve intended wishlist action through sign-in.

Customer may consent to merging guest and account carts; retain larger quantity for duplicate selling options, then recheck availability and limits. Cart and wishlist do not hold prices or stock. The rules for cart changes while a payment is pending remain open.

Calculate totals on server; show current price, delivery fee and a realistic fulfilment estimate before payment. No customer-selected delivery/pickup slots and no slot reservation. If busy continue accepting with a reliable later estimate; if no reliable estimate for either available fulfilment method, preserve cart and pause payment until reviewed.

Create pending order and order snapshots, plus 15-minute stock reservation, safely together before redirect to payment. Snapshot item, unit, quantity, price, discount, fees and total. A pending order is not confirmed; redirect is not payment proof. Verify Paystack server-side against reference, amount, currency and environment, and process authenticated repeated updates safely. Confirm order and commit inventory only after successful payment and fulfilment checks; notify SMS and email if provided. Confirmed orders are not customer-edited; new items require a new order.

Reservation expires at original deadline, regardless of verification delays. Payment verification continues independently. Late success: record payment and automatically check and allocate new available stock if all fulfilment checks pass; otherwise order awaiting confirmation on operational hold. No double allocation. Definitive failure releases any active reservation safely; uncertain payment stays under verification, using original reference, and alerts staff; do not claim failure from timeout.

4. Fulfilment, notifications and aftercare

Initial same-day delivery cut-offs: weekdays 4 pm with delivery ending 6 pm; Saturday 3 pm ending 5 pm; Sunday 1 pm ending 3 pm. Show later available estimate after cut-off or when capacity unavailable. Pickup ends at store closing: weekday 7 pm, Saturday 6 pm, Sunday 4 pm. Verify full store, delivery and support opening times against earlier source before configuration.

Pickup targets 10–20 minutes or sooner for regular orders; 30 minutes for large. Starting large-order threshold 20 units with staff flag for extra effort; adjustable. Actual ready message is the confirmation. SMS and optional email at confirmed order, pickup ready, dispatch, delivered/collected, meaningful refund/cancellation updates; substitution contact according to approved preference. Messages are tracked separately by channel.

Live rider map at launch is a design requirement subject to real device feasibility; no misleading fake movement. Stale after 2 minutes, alert staff after 5 minutes; configurable. Location update frequency, map provider, retention and browser background feasibility are open. If unavailable, retain delivery status and display last update. Offline handover is pending verification until server validates or manager records authorised exception.

Delivery and pickup codes entered at handover, backend verified, attempts limited, no exposure in rider responses or logs. Owner/manager authorised exception with reason and evidence if necessary; exact checks open.

Rider page: individual login, availability, assignments, acknowledgement, tap to call support/customer as permitted, report issues and live location. Driver management includes profiles, availability, issues, history. Manual assignment; multiple deliveries only with staff judgement. Both riders confirm physical transfer by default, manager exception logged. Immediate suspension permitted while retaining custody/assignment history. No automatic assignment, route optimisation or in-app voice at launch.

Customer unreachable: rider makes three contact attempts over five minutes, contacts team, team makes final attempt; if still unreachable rider returns order. No redelivery of returned order; customer may order again. Product costs eligible for refund, delivery fee not automatically refunded after a genuine customer-unavailable attempt; if Fresavelle/rider caused failure refund product costs and fee; if entire order cannot be fulfilled refund full amount including fee. For partial unavailable items while remainder delivered refund affected items; fee may remain. Review and disclose policy before payment and check applicable requirements.

Goods damaged/lost while with rider: flag, report and review; cancel and refund affected items, do not send replacements. Entire unfulfilled order full refund including fee. No presumption of rider fault.

Pickup reminder after 1 hour; staff follow-up after 2 hours or before closing if sooner. These are not cancellation deadlines. Overnight storage and cancellation/refund policy remain open. Significant delay starting thresholds: 15 min pickup, 30 min delivery, always notify delivery-day change.

Staff identify committed damaged goods, immediately protect stock; identical replacement units may be allocated by authorised staff, with damage adjustment reviewed by manager/owner. Different substitution requires customer agreement, exact difference refunded or paid; three contact attempts and previously agreed product-based timings need verification against full earlier source.

Order complaints accept protected pictures and verified order access. Separate support case, refund and order records; internal notes private. Resolved complaint automatically closes 7 calendar days after at least one resolution notification is confirmed delivered if no reply or reopening. If no delivery confirmation, remains resolved for staff review. Verified customer or authorised staff can reopen. Customer reopening time limit open.

General Contact Us form feeds shared team inbox; branded outbound emails. No automatic inbound reply threading at launch until selected and tested; do not imply replies are monitored. General enquiries first response target 4 support hours, order issue 2 support hours, urgent active-delivery issue flagged immediately with phone option; targets internal.

5. Identity, access and sessions

Customer password login using email or verified phone; optional extra sign-in verification, fresh verification for sensitive changes. Customer sessions max 7 days and 24 hours of meaningful inactivity; background calls do not extend; logout and individual/all session revocation server-enforced; password reset revokes sessions.

Owner, manager, staff, rider password plus one-time code to verified phone or email; no authenticator app required. Owner/manager/staff session max 8 hours, idle 30 min; rider max 8 hours, idle 1 hour. Rider assignment survives logout/expiry. Starting OTP 6 digits, 5 minutes, max 5 attempts/code, resend cooldown 60 seconds, 3 per 15 min; enforce wider anti-abuse limits; test and configure.

Guest tracking and individual guest-order linking: reference plus checkout phone plus OTP, verify on backend for the particular order; do not reveal account/order existence in pre-verification response. Shared/recycled phone numbers do not justify bulk linking. Lost reference: separate recovery; previously verified email may provide additional check, otherwise authorised support review. Order linked elsewhere not automatically transferred.

Team recovery never changes role or bypasses permissions; individual accounts, audit and session revocation. Manager recovery requires owner; staff/rider assisted recovery by owner/authorised manager. Owner recovery uses trusted contact only as supporting evidence, not automatic access; exact protected process open.

Account deletion requires fresh verification, clear explanation, retention review and session revocation. Active orders, refunds and complaints not automatically cancelled; detailed handling and retention open.

6. Order state and records

Order stages: awaiting payment; awaiting confirmation; confirmed; preparing; ready for pickup; ready for dispatch; out for delivery; delivered; collected; cancelled. Customer-response and operational-review holds separate from progression. Payment, refund and order states independent. Backend validates transitions and records actor, time, prior/new state, reason; retry safe.

Payment attempts pending/processing/verification needed/successful/failed/abandoned/reversed; exact provider mappings open. Reservation active/committed/released/expired. Refund awaiting approval/rejected/approved/initiation under review/processing/completed/failed. Notification queued/sending/accepted/delivered where reported/failed/needs review/cancelled.

Proposed records: account, contact, sessions, challenges, recovery and verified order links; categories, products, selling options, stock balances, reservations, items, movements and holds; carts and cart items; orders and snapshots; payment attempts, provider events and refunds; delivery, assignments, custody, location, issues and handover; support cases, messages, notes and private attachments; guidelines and versions; notifications and individual recipients.

Stock availability must not double-subtract categories or location. With-rider is a custody location; committed is allocation. On return, items held for inspection and not automatically resold. Preserve history and handle previously committed damaged units without double counting.

Financial amounts integer kobo; link refunds to actual successful payment. Preserve append-only financial history; protect concurrent refundable balance including in-flight or uncertain refunds. Provider event identifiers may not always be unique/available; verify signatures and use provider-supported identifiers and reconciliation. Additional payment and multiple successful payments require detailed design.

7. Staff workspace

CRM, orders, inventory, purchasing, finance, reconciliation, reports/exports, support inbox, rider management, approvals, security and settings.

Guidelines & Help Centre: owner/manager edit drafts and publish immutable versions; feedback and acknowledgements reference exact versions; mark selected changes requiring acknowledgement for relevant roles. Changes to guidance do not automatically change enforced business rules.

Silent staff Notification Centre, role-appropriate alerts, individual read status; read, acknowledged and task completion are separate. Notifications retained 90 days; underlying unresolved work remains visible. Customer SMS/email delivery records separate. Browser notifications optional and silent where supported.

8. Security, failure and scale

Role and record-level backend access; no trusting frontend price or status. Private complaint files, minimised rider data, protected secrets, secure cookies, server session revocation, rate limits and per-purpose OTP controls. Secure provider calls; no card details or OTPs in logs.

Transactions, row locking/atomic updates and constraints for stock and money; idempotency for retries; persistent notification intent (transactional outbox or equivalent), monitored background tasks, bounded retries and operational escalation. Do not hold database locks while waiting for external services. Check uncertain provider outcome before retrying.

Appropriate indexes, efficient queries, pagination, private cache isolation; stock/payment authoritative at critical checks; avoid stale price confirmation. Track error, queue, payment and service health; alerts reachable beyond dashboard.

Test: 20/50/100 daily orders, concurrent website users 20/50/100 including 3/10/20 checkout, plus staff and rider traffic; illustrative planning not forecast. At least 3 packers and 10 riders simultaneously; actual travel and capacity depend on conditions. Performance and correctness tested together.

Outage response target 2 hours for critical services, not guarantee; verify payments, reservations, orders, messages and active deliveries after recovery. Preserve original reservation expiry. Restore-test both database and stored files. RPO, plans, alert contacts and procedures open.

9. Pre-launch decisions and readiness register

Use separate decision status (Open/In progress/Decided) and implementation readiness (Not started/Implemented/Testing/Verified/Blocked/Not applicable with reason). Each entry needs ID, owner, approver, target, decision, affected feature, evidence and dependencies. No people, dates or tests have been assigned or completed.

ID

Workstream

Required decision or deliverable

Suggested responsible role

Feature gate / evidence

PAY-01

Payments

Refund approval limits, requester independence, eligible balance

Owner + backend

Refund permissions and concurrency tested

PAY-02

Payments

Provider mapping, reconciliation, substitution top-up

Backend

Paystack sandbox success/failure/retry verified

DEL-01

Tracking

Select map and test location, frequency, retention

Technical lead + owner

Real rider device, stale and privacy tests

POL-01

Policies

Pickup noncollection, refunds, complaint periods, disclosure

Owner + operations

Reviewed terms visible before payment

SEC-01

Accounts

Owner recovery and identity-review evidence

Owner + technical lead

Access-recovery and revocation tests

PRIV-01

Data

Retention, privacy notice, deletion, provider and transfer assessment

Owner + privacy lead

Implement and verify actual handling

REC-01

Recovery

RPO, database and file backups

Technical lead

Restore tests for both

OPS-01

Operations

Named alert contacts, continuity and retry schedules

Operations manager

Simulated outage and incident runbook

INF-01

Infrastructure

Render/Supabase plans, costs and capacity

Technical lead

Agreed load tests and cost review

API-01

Implementation

Constraints, API contracts, rates, provider status mappings

Backend

Integration and concurrency tests

SEC-02

Incident

Compromised account and data incident response

Security lead

Exercise and contact plan

MON-01

Monitoring

External alerting, ownership and thresholds

Technical lead

Demonstrated delivery of alerts

UAT-01

Acceptance

Assign sign-off of customer, dashboard, rider and financial journeys

Owner + operations

Evidence and explicit sign-off

Feature-by-feature launch gates: dependencies, decisions, implementation and tests must be verified before enabling a feature; shared foundations can block multiple features. Exceptions and impact need explicit review; no launch is authorised by this document.

10. Codex instructions and staged collaboration

First inspect the workspace and this specification; report conflicts and unresolved decisions. Do not pretend earlier unseen transcripts have been read. Present a stage plan, then work in meaningful stages; after each stage run suitable checks, explain exact browser URL and what to test, label mocks and wait for user feedback before proceeding. When account setup is required explain service purpose, practical steps, likely costs and test procedure; never ask for passwords, secret keys or OTPs in chat. Use test credentials, no real customer messages or charges; no deployment or publishing without user instruction. Keep decision log, readiness register and a record of implementation and testing. Do not substitute a technology without discussing it. Stage security and failure handling alongside relevant features. Owner and user can review and request changes at each stage.