# Design System Document

## 1. Overview & Creative North Star: "The Digital Grove"

This design system is built for the high-performance developer who values both technical precision and the grounding calm of nature. Our Creative North Star is **"The Digital Grove."** We reject the sterile, "neon-and-plastic" aesthetic of typical developer tools in favor of an atmosphere that feels organic yet architecturally sound—inspired by the resource management and structural ingenuity of *Timberborn*.

The system moves beyond the "standard SaaS dashboard" by employing **Atmospheric Depth**. Instead of flat grids and harsh dividers, we use a sophisticated hierarchy of dark surfaces, intentional asymmetry in spacing, and high-contrast editorial typography. We treat the UI not as a flat screen, but as a layered environment where code and logic reside within a lush, deep-forest ecosystem.

---

### 2. Colors: The Tonal Forest

Our palette is rooted in the earth. We use deep charcoal and forest greens to create a high-contrast environment that reduces eye strain during long coding sessions.

*   **Background & Surface Hierarchy:**
    *   **Primary Background (`surface`):** `#121416`. This is our "ground" layer.
    *   **Nesting Tiers:** To create depth, use `surface_container_low` (`#1a1c1e`) for secondary panels and `surface_container_highest` (`#333537`) for active or elevated elements.
*   **The Forest Accents:**
    *   **Primary (`primary`):** `#83d8a6`. A vibrant, minty green used for high-visibility highlights.
    *   **The Deep Wood (`primary_container`):** `#2f855a`. Our signature forest green. Use this for substantial brand moments and hero CTAs.

#### The "No-Line" Rule
Traditional 1px solid borders are strictly prohibited for layout sectioning. Separation must be achieved through **Background Color Shifts**. To separate a sidebar from a main feed, transition from `surface` to `surface_container_low`. The eye should perceive structure through tonal blocks, not drawn lines.

#### The "Glass & Gradient" Rule
To add a premium feel to floating overlays or "code-lens" views, utilize `surface_variant` (`#333537`) with a `backdrop-blur` of 12px-20px and 60% opacity. For primary CTAs, apply a subtle linear gradient from `primary` to `primary_container` (top-left to bottom-right) to inject "visual soul" and a tactile, three-dimensional quality.

---

### 3. Typography: Editorial Logic

The typography system bridges the gap between high-end editorial design and technical utility.

*   **Display & Headlines (Space Grotesk):** We use Space Grotesk for all `display` and `headline` roles. Its geometric, slightly quirky terminals provide a tech-forward, custom-engineered feel.
*   **Interface & Body (Inter):** Inter handles the heavy lifting for UI labels and body copy. Its neutrality ensures that the "Digital Grove" aesthetic remains legible and professional.
*   **Code Blocks (Fira Code):** (Specified in implementation) Monospace with ligatures is mandatory for all code snippets to maintain the "developer-first" priority.

**Hierarchy as Identity:** Use `display-lg` (3.5rem) sparingly to anchor major landing views. The extreme contrast between large `display` text and small `label-md` (0.75rem) UI elements creates an "Architectural Layout" feel that feels intentional and high-end.

---

### 4. Elevation & Depth: Tonal Layering

We do not use shadows to represent "height" in the traditional sense; we use them to represent **"Light within the Grove."**

*   **The Layering Principle:** Depth is achieved by stacking containers. A `surface_container_lowest` (`#0c0e10`) card placed on a `surface_container` (`#1e2022`) background creates a natural inset effect.
*   **Ambient Shadows:** For floating modals, use an extra-diffused shadow: `box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4)`. The shadow color should never be pure black; it should be a tinted version of the background to maintain the "atmospheric" feel.
*   **The "Ghost Border" Fallback:** If a container sits on a surface with an identical tone, use the `outline_variant` (`#3f4942`) at **15% opacity**. This creates a "whisper" of a boundary without breaking the "No-Line" rule.

---

### 5. Components: The Built Environment

#### Buttons
*   **Primary:** Gradient of `primary` to `primary_container`. Bold, uppercase `label-md` type. Radius: `md` (`0.375rem`).
*   **Secondary:** `surface_container_high` background with `on_surface` text. No border.
*   **Tertiary:** Transparent background with `primary` text. Hover state triggers a subtle `surface_variant` background fill.

#### Input Fields
*   **Style:** Background `surface_container_lowest`. No bottom border. Instead, use a 2px `primary` left-border indicator that only appears on `:focus`.
*   **Typography:** User input should always use `body-md` in `on_surface`.

#### Cards & Lists
*   **Strict Rule:** No dividers. Separate list items using `spacing-4` (`0.9rem`) of vertical white space or by alternating background tones between `surface_container_low` and `surface_container`.
*   **Interaction:** On hover, a card should shift from `surface_container` to `surface_container_high` and transition its border-radius from `md` to `lg` for a "soft expansion" effect.

#### The "Code Lens" (Special Component)
A container specifically for code snippets. It uses `surface_container_lowest` with a `primary_container` glow effect (opacity 5%) in the top-right corner, mimicking sunlight hitting a forest floor.

---

### 6. Do’s and Don’ts

#### Do
*   **DO** use `spacing-16` and `spacing-24` for section margins to create "breathing room" typical of high-end editorial layouts.
*   **DO** use `primary_fixed_dim` (`#83d8a6`) for small success indicators and status dots.
*   **DO** lean into asymmetry. A wider left margin than right margin on hero text can create a sophisticated, custom-built appearance.

#### Don’t
*   **DON’T** use 100% opaque `outline` tokens for borders. It creates "visual noise" that contradicts the minimalist Grove aesthetic.
*   **DON’T** use standard grey shadows. Always ensure shadows are deep and desaturated to match the `surface` palette.
*   **DON’T** use generic "Success Green" or "Warning Red" at full saturation. Always use the `error` (`#ffb4ab`) and `primary` (`#83d8a6`) tokens to maintain the system’s specific tonal range.