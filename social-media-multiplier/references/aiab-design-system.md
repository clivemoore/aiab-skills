# Agency in a Box / Clive Moore Personal — Design System (Visual Reference)

Source of truth for **Clive's personal-brand visuals** and **Agency in a Box (AIAB)
visuals**. Light-first interpretation of the AIAB brand: **white canvas, orange action,
silver-grey neutrals, charcoal ink, Futura-style geometric display type.**

> **Brand separation — read this first.**
> Copy is always Clive's personal voice (`voice-guide.md`) — contrarian, "Wrong question.",
> hands the problem back. This file governs **VISUALS** for Clive-personal and AIAB posts.
> Do **not** use the **Workilo** voxel + green system here, and do not use this
> orange/charcoal/Futura system on Workilo product visuals. Same family, two members
> (Clive personal and AIAB share this look); Workilo is separate.

## Provenance — what's extracted vs. designed

- **Extracted from the live agencyinabox.ca (computed CSS, June 2026):** the color hexes
  and the typefaces (Futura PT display, system-ui body). These are authoritative.
- **Designed here, not extracted:** the **light-first mapping** (the live agency *site* is
  dark — charcoal `#15181a` surfaces; this personal-brand system flips that to a white
  canvas per Clive's brief), plus radius / spacing / motion conventions. Treat those as
  brand-consistent defaults, adjust freely.
- **Correction:** a prior note assumed **Avenir** for this brand. The live product ships
  **Futura PT**. Use Futura PT (with fallbacks); Avenir is not the brand face.
- **Collision watch:** AIAB orange `#ED8B00` ≈ Workilo accent orange `#FF8A00`. Orange does
  NOT distinguish the two brands. The separators are everything else — Futura geometric
  type + charcoal/silver neutrals + editorial photography here, vs. voxel art + green +
  system-ui there.

---

## Color (light-first)

White-dominant. Orange is the single action/brand color. Silver-grey is the named
secondary. Charcoal is ink. Warm, confident, editorial — not playful.

### Brand
| Token | Hex | Use |
|---|---|---|
| `--aiab-orange` | `#ED8B00` | primary brand & action color (CTAs, links, accents) |
| `--aiab-orange-hover` | `#C9760A` | hover / pressed on a light canvas (darken) |
| `--aiab-orange-soft` | `#FFB769` | warm light highlight / tint accent (the live site's accent-text) |
| `--aiab-tint` | `#FFF3E3` | warm orange wash surface (light analogue of the site's `#241b0e`) |

### Ink & neutrals
| Token | Hex | Use |
|---|---|---|
| `--aiab-ink` | `#2C3234` | primary text (the brand charcoal / theme-color) |
| `--aiab-ink-strong` | `#15181A` | near-black for max-contrast display headings |
| `--aiab-muted` | `#5C6468` | secondary text (darkened for contrast on white) |
| `--aiab-silver` | `#AAB2B8` | the named brand **silver/grey** — dividers, decorative, captions |
| `--aiab-silver-2` | `#CED4DA` | lighter silver — subtle fills |
| `--aiab-border` | `#E2E5E7` | 1px borders on white |
| `--aiab-surface` | `#FFFFFF` | cards / surfaces |
| `--aiab-surface-2` | `#F5F6F7` | subtle grey surface / section banding |
| `--aiab-bg` | `#FAFBFB` | near-white page background |

### Rules
- White is the canvas. Orange is the **only** action color — used sparingly, with intent.
- Silver-grey is structural/decorative (rules, captions, secondary chrome) — never an
  action color, never body text on white (too low contrast; use `--aiab-muted`).
- Charcoal `#2C3234` is the text-on-orange pairing and the dominant ink.
- One accent at a time. No green (that's Workilo). No multi-color confetti.

---

## Typography

Geometric display + neutral body — the signature contrast of the brand.

| Role | Family | Notes |
|---|---|---|
| Display / headings | **`"Futura PT"`**, then `Futura, "Century Gothic", system-ui, sans-serif` | geometric, confident, tight tracking at large sizes |
| Body / UI | `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` | clean, neutral, readable |
| Code / tokens | `ui-monospace, SFMono-Regular, Menlo, monospace` | |

- Headings: Futura PT, medium-to-bold weight, **sentence case** (Title Case only for proper
  nouns: Agency in a Box, AI Workflow Score).
- Body: 1rem / 1.55 line-height, charcoal ink, generous measure.
- Futura PT is an Adobe Fonts (Typekit) face — if unavailable in a generated asset, fall
  back to Futura / Century Gothic before any other geometric sans.

---

## Spacing, radius & elevation (designed conventions)

- **4px base scale.** Generous editorial whitespace — this brand breathes.
- Centered max-width ~1200px containers.

| Radius | Value | Use |
|---|---|---|
| Buttons / inputs | `8px` | |
| Cards / banners | `12px` | |
| Pills / chips | full | |

| Shadow | Value |
|---|---|
| Card resting | `0 1px 3px rgba(44,50,52,0.08)` |
| Card raised | `0 8px 24px rgba(44,50,52,0.12)` |

Cards: white, 1px `#E2E5E7` border, soft charcoal-tinted shadow. Flat, editorial, no heavy
chrome.

---

## Imagery & aesthetic

Editorial and confident — the opposite of Workilo's playful voxel world.

- **Real photography is allowed and encouraged** (case studies, people, workspaces) — unlike
  the Workilo system which forbids photography. Prefer warm, natural, professional shots.
- **Duotone / treated images:** charcoal `#2C3234` + orange `#ED8B00` duotone is the
  signature image treatment for a branded look.
- **Geometric accents:** thin orange rules, geometric Futura type as graphic element,
  generous negative space on white.
- **No voxel art. No green. No emoji.** Voxel + green is exclusively Workilo.
- Logos: AIAB wordmark `aiab-logotype.svg` (on light) and `aiab-logotype-ko.svg` (knockout,
  on charcoal/photo). Reference by name — binaries are not bundled in this skill.

### Image-generation prompt seed (Clive personal / AIAB visuals)
> Editorial, confident, minimal composition on a clean white background, single warm orange
> `#ED8B00` accent against charcoal `#2C3234` and silver-grey `#AAB2B8`, geometric and modern,
> generous negative space, professional and human, no text, no voxel/3D-pixel style, no green.
> (For photographic concepts: warm natural professional photography, optional charcoal+orange
> duotone treatment.)

---

## Per-platform image specs

Same dimensions as the platform standard; the *style* follows the AIAB system above when the
post is Clive-personal or AIAB.

| Platform | Format | Dimensions |
|---|---|---|
| LinkedIn | Portrait (preferred) | 1080 × 1350 |
| LinkedIn | Square | 1080 × 1080 |
| LinkedIn | Landscape | 1200 × 627 |
| Instagram | Portrait | 1080 × 1350 |
| Instagram | Square | 1080 × 1080 |
| X / Twitter | Landscape | 1200 × 675 |
| Facebook | Landscape | 1200 × 630 |

---

## Terminology

Agency in a Box positioning: "We run, build, and modernize the digital operations behind
growing agencies." Services-first ("services, not subscriptions"); the AIAB *platform* is
the forthcoming productized version. `.ca is the team, .app is the product.`

Copy still follows `voice-guide.md` — this section only grounds AIAB references factually.
