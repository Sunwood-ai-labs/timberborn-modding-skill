# Contributing

## Scope

Contribute improvements that keep the skill practical for real Timberborn building-mod tasks.

Useful contribution areas:

- clearer route selection guidance
- stronger troubleshooting coverage
- better reusable templates
- docs improvements with English and Japanese parity

## Before Opening A Pull Request

1. Run the skill validator.

```powershell
uv run --with pyyaml python scripts/validate_skill.py .
```

2. Build the docs.

```powershell
Set-Location docs
npm ci
npm run docs:build
```

3. Keep English and Japanese docs structurally aligned when both are touched.

## Pull Request Expectations

- explain what changed and why
- note whether the change affects Route A, Route B, or both
- mention any part that was not verified locally

## Issues

When reporting a problem, include:

- the source asset type such as `GLB`, `FBX`, or `OBJ`
- whether the target was Route A or Route B
- the relevant error log or screenshot
- the paths or filenames involved when possible
