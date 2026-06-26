# Workilo Design System (Visual Reference)

Source of truth for **Workilo-branded visuals** — image generation, color, type, and
layout for any post that features the Workilo product. Reverse-engineered from the
Workilo product codebase, brand guidelines (v1.0, Oct 2025), and the canonical Claude
Design "Workilo Design System".

> **Brand separation — read this first.**
> This skill writes copy in **Clive Moore's personal voice** (see `voice-guide.md`):
> contrarian, "Wrong question.", hands the problem back to the reader. That stays the
> copy authority.
> **This file governs VISUALS, not copy** — and only for **Workilo product** posts.
> Do **not** cross-pollinate: don't apply Workilo's "professional but friendly" product
> voice to Clive's personal posts, and don't apply Clive's personal palette/aesthetic to
> Workilo product visuals. Three separate brand identities (Clive personal / Workilo /
> Agency in a Box) — keep them apart.

---

## When to apply this

| Post is about… | Copy voice | Visual system |
|---|---|---|
| Workilo product / workalongs / workflows | Clive personal (voice-guide.md) | **This file** |
| Clive's personal takes, AI ethics, thought leadership | Clive personal | Clive personal aesthetic (not this file) |
| Agency in a Box | Clive personal | AIAB aesthetic (not this file) |

If an image features the Workilo wordmark, app UI, or a workalong character, it follows
this system.

---

## Color

Flat color fields — **no gradients** except one subtle brand→secondary tinted wash on the
Brand Brain banner. No textures, no patterns, no full-bleed photography.

### Brand
| Token | Hex | Use |
|---|---|---|
| `--wk-primary` | `#10B981` | Workilo Green — primary brand & action color |
| `--wk-primary-hover` | `#059669` | hover / pressed action state |
| `--wk-secondary` | `#6D28D9` | purple — steps, sliders, accents |
| `--wk-accent` | `#FF8A00` | orange — energetic highlights, matches the voxel blocks |
| `--wk-info` | `#0EA5E9` | info blue |

### Ink & neutrals
| Token | Hex | Use |
|---|---|---|
| `--wk-ink` | `#0F172A` | primary text |
| `--wk-muted` | `#475569` | secondary text |
| `--wk-border` | `#E2E8F0` | 1px card / input borders |
| `--wk-surface` | `#FFFFFF` | cards, surfaces |
| `--wk-bg` | `#F8FAFC` | soft near-white page background |

### Rules
- Green is the only action/CTA color. Purple/orange/blue are accents — never CTA fills.
- Surfaces are **white on near-white** (`#F8FAFC`). Keep backgrounds neutral; do not tint
  backgrounds green (muddy, unreadable).
- Hover glow on action elements: `0 8px 25px rgba(16,185,129,.4)` (green-tinted).

---

## Typography

System font stack — **no custom display webfont**. Do not substitute one.

```
-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif
```

Signature move — weight contrast at size:
| Role | Weight | Notes |
|---|---|---|
| Display headings (large) | **300 (light)** | the signature look — light at big sizes |
| Section headings | 400 (regular) | |
| Smaller titles | 600 (semibold) | |
| Wordmark only | 800 (extrabold) | reserved for "Workilo" |
| Body | 400, `1rem / 1.6` | minimum 12pt |
| Code / tokens | monospace | |

Casing: **sentence case** for headings, buttons, nav. Title Case only for proper nouns
(Brand Brain, Start Workflow). Wordmark is "Workilo".

---

## Spacing, radius & elevation

- **4px base scale** (steps 1–8). Generous white space; clean, minimal.
- Centered **1200px max-width** containers, **32px gutters**.

| Radius | Value |
|---|---|
| Buttons / inputs | `0.375rem` |
| Cards / banners | `~14px` |
| CTAs / chips | full pill |

| Shadow | Value |
|---|---|
| Card resting | `0 2px 4px rgba(15,23,42,…)` |
| Card raised / banner | `0 10px 30px rgba(15,23,42,…)` |
| Action hover glow | `0 8px 25px rgba(16,185,129,.4)` |

Cards: white, 1px `#E2E8F0` border, soft low-contrast ink-tinted shadow. No heavy borders,
no colored left-border accent cards.

---

## Motion

| Token | Curve |
|---|---|
| House easing | `cubic-bezier(0.4, 0, 0.2, 1)` |
| Bouncy (avatars) | `cubic-bezier(0.34, 1.56, 0.64, 1)` |

- Signature interaction: **lift on hover** — `translateY(-2px)` + deeper shadow on cards & buttons.
- Press = opacity drop (`0.7–0.75`).
- Durations: `0.15s` buttons, `0.3–0.6s` carousels.
- Focus ring: `3px` green `rgba(16,185,129,.25)` — never the default blue outline.
- Always respect `prefers-reduced-motion`.

---

## Imagery — voxel art (the brand's visual signature)

Distinctive **voxel / 3D-blocky (Minecraft-adjacent)** art — warm, saturated, friendly,
with soft drop shadows on transparent backgrounds.

- Characters render `image-rendering: pixelated` and scale up bouncily on hover.
- Isometric "scene" illustrations: workalongs collaborating around physical-looking workstations.
- **No photography. No gradients. No textures.** Visual interest comes entirely from the voxel art.
- Personality lives in the voxel character PNGs — **never emoji**, never stock photos.

### Image-generation prompt seed (for Workilo product visuals)
> Isometric voxel / 3D-pixel illustration, warm saturated palette anchored on Workilo green
> `#10B981` with orange `#FF8A00` and purple `#6D28D9` accent blocks, soft drop shadows,
> transparent or flat near-white `#F8FAFC` background, friendly and optimistic, clean and
> minimal, no text, no photographic elements, no gradients.

---

## Iconography

- **Bootstrap Icons** — line-style, ~1.5px stroke, used inline with text.
- No emoji as icons. No custom glyph sets.

---

## Logos & symbol

| Asset | Use |
|---|---|
| `workilo-logo.png` | voxel "W" + black wordmark |
| `workilo-logo-ko.png` | knockout / white version (on dark) |
| `workilo-symbol-256.png` / `workilo-symbol.png` | symbol only — nav, app, social avatar |

(These ship in the product repo `workilo/static/assets/`; reference them by name in image
briefs — this skill does not bundle the binaries.)

---

## Per-platform image specs

Dimensions for social outputs. Workilo-branded images follow the voxel system above.

| Platform | Format | Dimensions |
|---|---|---|
| LinkedIn | Portrait (preferred) | 1080 × 1350 |
| LinkedIn | Square | 1080 × 1080 |
| LinkedIn | Landscape | 1200 × 627 |
| Instagram | Portrait | 1080 × 1350 |
| Instagram | Square | 1080 × 1080 |
| X / Twitter | Landscape | 1200 × 675 |
| Facebook | Landscape | 1200 × 630 |

Default to **portrait 1080×1350** for LinkedIn/Instagram, **landscape 1200×675** for X.

---

## Terminology (product copy guardrails)

These apply when copy references the Workilo product — they overlap with, and never
contradict, `voice-guide.md`:

- ✅ Use: Workalongs / coworkers, Workflows, Handoffs, Collaborate, Workshop, Brand Brain.
- ❌ Never: "agents", "bots", "AI tools", "automate", "replace".

Positioning: an **AI workshop / AI workforce** — specialist coworkers that collaborate
through structured multi-phase workflows with handoffs. Not "tools", not a chat box.
