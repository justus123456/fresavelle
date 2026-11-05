# Admin dashboard design reference

This visual reference is for a future Fresavelle dashboard. The videos show a logistics application and do not establish Fresavelle's features or data. Both are 576 × 576 recordings of a desktop interface on a light-gray presentation canvas. Small text is difficult to read; timestamps are approximate.

## Original videos

- admin-dashboard-reference.mp4: original 11.30.10 recording, approximately 43 seconds. AI agents and settings.
- admin-dashboard-reference-operations.mp4: original 11.32.57 recording, approximately 47 seconds. Operations, dispatch, shipment details and tracking.

Both originals are preserved without re-encoding.

## Directly visible

### Layout, sidebar and header

The interface appears in a white, subtly bordered, rounded shell. A narrow icon-only rail on the left has a dark circular logo at the top, notification badges, purple active indication and a profile avatar near the bottom. The gray around the shell could be video presentation background. Fixed sidebar behavior while scrolling is not shown.

A compact header contains a title, sometimes small contextual text, a pale rounded search box, monitoring controls, a prominent pill action, notification icons and an account/control icon. Titles shown include AI agents, Settings, Dispatch, Live tracking and a shipment identifier. The overview starts with a greeting.

Content is dense but organized, using narrow consistent gutters, padded panels, left-aligned headings, large key numbers and small muted labels. The overview has a metric row, a large shipment panel beside a brief, and a lower map and timeline. Dispatch and tracking have a left list, central map and right details.

### Color, typography and components

The palette is mostly white and pale gray with dark text and occasional near-black emphasis panels. Purple accents selected navigation, buttons, routes, progress, toggles and selected states. Green/lime, amber and red appear in statuses. Pale lavender highlights panels and options. Type looks like a clean modern sans-serif; exact family, sizes, hex colors and spacing are not reliably identifiable. Cards have soft corners and subtle fills or borders; pills have rounder ends.

The overview has large metrics with small labels and colored status pills. A shipment card combines a route, driver details, delivery times, truck image and a route line with stops. A lavender operations brief includes summary text, lists and actions. A muted map and timeline use colored routes or bars.

Dispatch shows a shipment queue, central map and selected route callout, recommendations panel and driver timeline. Tracking shows a larger map between a list and vehicle details. Maps have pale backgrounds, dark routes, colored segments and circular markers. Shipment details include a route line, load-plan grid and event timeline.

The AI agents page has a wide black summary panel with white text and metrics, followed by a three-column grid of cards with icons, names, statuses, metrics, activity and thin purple progress lines. Settings use light cards, switches and capability rows with segmented choices. Enabled switches appear purple and off switches gray. A conventional sortable data table is not clearly shown.

Visible controls include pill-shaped black or purple primary buttons, pale or outlined secondary buttons, search inputs, segmented controls, checkboxes, text areas and switches.

### Dialogs, feedback and behavior

Centered white rounded dialogs appear over dimmed and visibly blurred backgrounds. A route-approval dialog compares current and proposed options and offers reject, review and approve actions. A sandbox-results dialog shows metrics, outcome rows and actions. A pause-agents confirmation includes consequences, duration choices, a reason field, a checkbox and cancel/confirm actions. Small dark toast-style notifications appear near the bottom in some transitions; wording and timing are unclear.

AI-agents recording: overview and cards near the beginning; agent configuration and sandbox results around 10–15 seconds; settings and permission controls around 20–25 seconds; pause-all confirmation around 35 seconds.

Operations recording: overview near the beginning; Dispatch around 10 seconds; route-approval dialog around 15 seconds; shipment view around 20–30 seconds; live tracking around 35–40 seconds.

The edited demos show navigation, selected items, dialogs, controls and feedback. They do not establish exact click targets, keyboard behavior, persistence, network effects or complete workflows. Zooming, panning, fading and moving page elements are visible, but may be video editing or prototype presentation effects. Hover styling, motion duration and easing are not reliably established.

No mobile layout, breakpoint, mobile navigation or actual resize behavior is shown. A square video of a scaled-down desktop interface is not evidence of a mobile design.

## Assumptions and open decisions

The logistics and AI-agent screens provide visual references, not requirements for Fresavelle's business features. A future implementation may adapt the observed shell, hierarchy, palette, purple accents and modular density to the actual brief. Exact tokens, content, icons and dimensions remain to be chosen. Responsive layouts, accessibility behavior, hover and focus states, loading and error states, and detailed interactions must be designed and validated later. Inspect both original videos again before implementation or revision, particularly for motion and details that sampled frames cannot resolve.
