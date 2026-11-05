# Product and launch scope

Source: [revision 2, sections C, J and preserved sections 1–8](../design/Fresavelle_Blueprint.md), the pasted revision, and the user's newer working instructions. See [decision log](../project/decision-log.md) for evidence status.

## Approved product direction

Fresavelle is an Abuja grocery, foodstuff, fruit and vegetable business serving households, restaurants and companies through the same website and listed prices. No enforced minimum order. Web and mobile browsers are in scope; a native app is not selected.

- Guest browsing, cart and checkout; account required for wishlists.
- Fixed selling units such as pieces and fixed-weight packs; no variable-weight pricing. Basket products carry their own stock and do not automatically consume ingredients.
- Show a delivery or pickup estimate before payment. Pickup and delivery use customer handover codes.
- Customers can track orders; staff and riders have separate restricted interfaces. Each team member has an individual account and permissions.
- Staff dashboard notifications are silent. Protect customer data, complaint photos, payment details and rider location.
- Customer frontend should be story-led, modern and easy to use, using photographs/backgrounds and useful floating details. The dashboard reference applies to later admin work, not necessarily the storefront.

## Working launch scope

The following comes from the handoff's launch pathways and is a planning baseline, not a claim that each sub-policy is approved or verified:

- Customer storefront: catalogue, search, product details and selling options; cart, account wishlist, guest/account checkout, estimates, tracking, reorder, account controls, support and Contact Us.
- Commerce and operations: inventory, reservation, backend-verified test then production payment, refunds/reconciliation, order preparation, pickup, delivery and handover.
- Team workspace: appropriate order queues, product/stock management, approvals, rider management, private support cases, notifications, guidelines, and agreed management views.
- Rider workspace: assigned work, availability, issue reporting, handover and location with proper access limits. Real location/map is a launch design requirement subject to genuine device feasibility and a selected provider; show honest fallback/staleness.
- Security, recovery, monitoring, privacy, testing and operational policies accompany each feature and receive final launch review.

## Later or not selected

Native apps are not selected. Automated rider assignment, route optimisation, in-app voice and automatic inbound email threading are not in the launch design. Advanced CRM, purchasing workflows and financial reporting are mentioned, but their exact scope and launch priority require clarification; do not imply they are implemented or automatically defer them without owner review. Detailed requirements for reports, categories and integrations remain open.

## Design reference boundary

The prior desktop videos depict a logistics product and are a visual reference for the future admin dashboard; they do not establish Fresavelle's business features. No admin interface is to be built during Stage 0.
