# Operations and business rules

Source: the user's latest explicit working instructions and [revision 2, sections A and D–H and preserved sections 3–6](../design/Fresavelle_Blueprint.md). "Carried forward" is not final approval.

## Approved rules

- Same listed prices for households, restaurants and companies; no enforced minimum; guest checkout allowed; wishlist requires an account.
- Fixed selling options and separately counted baskets; no automatic basket ingredient deductions.
- Display a delivery or pickup estimate before payment. The blueprint rejects guaranteed timing because real conditions change.
- **Stock is reserved for 15 minutes when payment starts.** This inventory hold is not a deadline for the customer's payment or payment verification. This newer explicit instruction settles the older conflict over whether the hold exists and its duration; it does not settle every late-payment policy.
- Paystack payment is verified by the backend; a redirect alone is not payment proof. Handle late or uncertain payment, duplicate events, stock concurrency and refunds under the blueprint, with unresolved details reviewed before implementation.
- Customers track orders; individual staff accounts and role-based restrictions apply. Pickup and delivery use customer handover codes. Dashboard alerts are silent.
- The handoff reports explicit user direction that returned failed deliveries are not redelivered: customers place a new order. Refund and fee treatment must follow the applicable policy and be reviewed before checkout goes live.

## Handoff pathways and safeguards

These describe design intent, not verified functionality or blanket approval of all implementation details.

1. Shopping: show selling options and current prices. A cart or wishlist does not hold stock or prices. Recalculate the order, fees, stock and estimate authoritatively before payment. If no reliable estimate is available, the handoff proposes retaining the cart and pausing payment.
2. Checkout: create a pending order and immutable price/item/fee snapshots with the reservation safely; the order is not confirmed merely because payment began. Once an attempt begins, its amount must not silently change; the precise change-order policy is open.
3. Payment: check provider reference, amount, currency and environment server-side. A lost response or verification timeout is a checking state, not proof of failure. Repeat callbacks and retries must not duplicate fulfilment. Avoid holding database locks while waiting for an external provider.
4. Expiry and late success: the carried-forward pathway expires the hold at its original deadline while payment verification continues; if money later arrives, record it and check stock/fulfilment again, then resolve or refund if unavailable. Exact allocation and exception workflow still needs review. Do not infer that expiry cancels the payment.
5. Fulfilment: prepare, assign and hand over through permitted, audited transitions. Keep review/customer-response holds distinct from order, payment and refund states. Verify handover codes on the backend; restrict attempts and access. Offline or disputed handover awaits verification or authorised review.
6. Rider tracking: access only assigned deliveries; record custody and real device updates. Label stale or unavailable location honestly; never simulate live movement. Reassignment and custody changes require records.
7. Refunds: distinguish request, approval, initiation, processing and completion. Check the refundable balance including in-flight/uncertain commitments, and investigate uncertain provider responses before retrying. Refund does not automatically restock goods.
8. Support: verify access to order complaints; keep evidence private and internal notes separate. A general Contact Us message is not proof of order ownership. Distinguish delivery of a message from merely accepting it.
9. Silent team notifications: recipient-specific read state is separate from task completion and guideline acknowledgement.

## Carried-forward settings requiring owner review

The earlier handoff mentions: guest cart retained for 30 days, merge keeping the higher duplicate quantity, delivery/pickup cut-offs and opening hours, a 20-unit large-order threshold, pickup targets and follow-ups, delay thresholds, three contact attempts in five minutes, stale/alert location thresholds of two/five minutes, seven-day complaint closure, and 90-day notification retention. They are not silently approved; specific hours, exact triggers and exceptions must be confirmed before affected features are enabled.

Outstanding policy details include areas/fees and capacity; pickup noncollection; substitutions, cancellation and refund eligibility/approvals; late payment and change to a pending checkout; complaint reopening and closure; the handover exception procedure and location retention. See the decision log and readiness register.
