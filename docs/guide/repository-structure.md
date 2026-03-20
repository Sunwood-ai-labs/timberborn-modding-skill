# Repository Structure

## Top-Level Layout

```text
.
├── SKILL.md
├── assets/
├── docs/
├── references/
└── scripts/
```

## What Each Directory Does

### `assets/`

Reusable implementation starters:

- Blender CLI export template
- building Blueprint template
- material collection template
- template collection template

### `references/`

Detailed guidance loaded on demand:

- standard workflow
- troubleshooting notes

### `scripts/`

Repository-side validation helpers for CI and local checks.

### `docs/`

Public-facing documentation site built with VitePress.

## Why The Repo Uses Both References And Docs

- `references/` are optimized for Codex execution
- `docs/` are optimized for human readers on GitHub and Pages
