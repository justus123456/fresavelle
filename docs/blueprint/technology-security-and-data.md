# Technology, security and data

Source: user's approved starting technology and [revision 2 sections B, E–I and preserved sections 2, 5–8](../design/Fresavelle_Blueprint.md).

## Approved starting technology

| Area | Choice and status |
|---|---|
| Frontend | Next.js with React |
| Backend | Python, Django, Django REST Framework; modular monolith |
| Database and file storage | Supabase PostgreSQL and Supabase Storage |
| Payments | Paystack |
| Email | Resend |
| SMS | Termii is provisional, subject to current pricing and tests |
| Hosting | Render preferred initially for frontend and backend; plans/configuration not yet selected |
| Maps | Provider open |

No service is assumed configured. Changing an approved technology requires discussion. Consult current official documentation when an integration is actually reached, and assess costs at that time.

## Architecture and ownership

The handoff proposes one Next.js frontend and one modular Django application, with Django responsible for authoritative business actions, permissions, stock, order and money state. PostgreSQL persists records; storage keeps product and protected complaint files. A worker/scheduler approach is open. Proposed schema, API paths, authentication approach and permission matrix are design candidates, not implemented interfaces. Customer, staff and rider access is checked by the backend for each record, not merely hidden in the interface.

Customer/rider location comes from an authorised real device; a map provider only displays or processes it. Define consent, scope, freshness and retention before activation. No background tracking guarantee can be assumed for mobile browsers.

## Safety and reliability to build alongside each capability

- Check ownership and role on every protected action and file; individual team accounts, auditable actions, protected handover codes and minimised personal data.
- Secure sessions and revocation, password handling, per-purpose verification, anti-abuse controls, suitable cookies/CSRF/HTTPS and protection from cross-user leaks. Exact session and recovery policies remain open.
- Backend-authoritative prices, stock, payment and refunds; integer kobo as the handoff's proposed financial representation. Transactional/atomic stock and refundable-balance changes, durable work records, stable retry identity and safe duplicate handling. Payment verification and reconciliation remain independent of browser redirects and hold expiry.
- Protect files with validated uploads and authorised downloads; no secrets or personal data in logs or chat. Private complaint evidence is not public product imagery.
- Retry and monitor background jobs; investigate uncertain provider outcomes before retrying; provide operational escalation. Backup and restore-test both database and files; set recovery targets and ownership before launch.
- Test security, correctness, concurrency and failure paths with the feature itself: e.g. two buyers for the last item, duplicate provider callbacks, lost successful response, late payment, two concurrent refunds, revoked sessions, cross-user attachments, stale rider coordinates.

Carried-forward session durations and OTP numbers conflict with other earlier discussion and are not approved defaults. The exact role grants, session lifetimes, team recovery, provider mappings, job architecture, retention and deletion policies remain open.
