# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability in agent-md-specs or agent-md-validator,
please report it responsibly.

**Email:** security@totalmarkdown.ai
**Response time:** We aim to acknowledge reports within 48 hours.

## Scope

This policy covers:
- Vulnerabilities in the agent-md-validator tool
- Security issues in spec templates that could lead to misconfiguration
- Broken or misleading security guidance in any spec

## Disclosure

We follow coordinated disclosure. Please do not open public issues for
security vulnerabilities. We will credit reporters in our changelog
unless anonymity is requested.

## Security of Spec Content

agent-md-specs defines configuration vocabulary — not runtime security
controls. The specs describe *what* should be configured; enforcement
depends on the runtime environment. See ENFORCEMENT.md for the
framework's approach to bridging declaration and verification.
