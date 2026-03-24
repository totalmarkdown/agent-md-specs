---
spec_name: "AGENTS.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Forge"
agent_version: "3.2.0"
---

# AGENTS.md — TechCo Platform

## Build

```bash
npm run build          # TypeScript compilation (strict mode)
npm run build:watch    # Development mode with hot reload
```

## Test

```bash
npm test               # Jest unit tests (>90% coverage required)
npm run test:e2e       # Playwright end-to-end tests
npm run test:int       # Integration tests against staging DB
```

## Lint & Format

```bash
npm run lint           # ESLint + Prettier (auto-fix with --fix)
npm run typecheck      # tsc --noEmit strict check
```

## Code Style

- TypeScript strict mode, `noUncheckedIndexedAccess` enabled
- Never use `any` — use `unknown` with type guards instead
- Prefer composition over inheritance
- Use barrel exports (`index.ts`) per module
- Error handling: custom error classes extending `AppError`
- Database queries via Drizzle ORM, no raw SQL in application code

## PR Conventions

- Conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`
- Maximum 400 lines changed per PR (split larger work)
- Require 1 approval before merge
- Squash merge to main, preserve commit body
- Branch naming: `feat/ticket-123-description`, `fix/brief-description`, `chore/cleanup-name`

## Deploy

```bash
npm run deploy:staging    # Auto-deploy on merge to main
npm run deploy:production # Manual approval required via release manager
```

Staging deploys are automatic after CI passes. Production deploys
require sign-off from an on-call engineer in #releases.
