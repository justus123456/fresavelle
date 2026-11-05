# Stage 1 storefront design direction

Status: reference-led homepage revision, awaiting review. Shopping and backend integrations are not connected.

- Direction: a centred, confident sans-serif introduction and a large grocery photograph, with two category links overlapping its edges on wide screens. On phones the links sit at the bottom of the image without obscuring the copy.
- Palette: warm ivory, forest green and lavender #D2C3F6. Lavender is used for the produce link and smaller accents, with clean solid surfaces for product information.
- Structure: photographic category tiles and a separate, simpler product grid use different layouts. The hero and category images are generated illustrative samples; they are not actual Fresavelle product photos.
- Homepage layout: keep the centred hero compact so a substantial portion of the photograph is visible on a typical desktop screen. Use small, softly shadowed category links with consistently aligned labels and arrows; on phones, arrange them neatly along the bottom without hiding important imagery. Do not impose a fixed viewport height on mobile.
- Sections: label the photographic tiles “Shop by category” and the product grid “Explore the selection”. Keep the frosted captions short so the photographs remain prominent, and use comfortable but compact spacing between sections. Align product names, units, prices and controls consistently across the grid.
- Preview: one page-level notice explains that products, prices and availability are examples. Search, account, wishlist, cart and add-to-cart are disabled pending later stages.
- Accessibility: visible focus indicators, text alternatives for meaningful imagery and reduced-motion support. Shadows and frosted treatment are restrained, with a solid fallback.

## Homepage motion

The headline, supporting copy, primary action and hero photograph enter in a noticeable stagger on page load. The two overlapping category links drift continuously, with a smaller range on phones, and pause while hovered or keyboard-focused. Users who prefer reduced motion receive a still layout.
