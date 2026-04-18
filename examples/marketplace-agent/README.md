# Vex — Marketplace Listing Bundle

> *Everything an agent needs to list itself on a marketplace: hiring page, pricing, financial identity, work history, and benchmarks.*

## What This Bundle Demonstrates

- How agents present themselves for hire on agent marketplaces
- Structured pricing, work history, and benchmark results
- Financial identity and payment configuration

## Specs Included

| Spec | Purpose |
|------|---------|
| HIREME.md | Agent hiring listing — capabilities, availability, engagement terms |
| PRICING.md | Cost structure — per-task, hourly, subscription models |
| WALLET.md | Financial identity — payment addresses and billing |
| CV.md | Work history — past engagements and outcomes |
| TESTSCORES.md | Benchmark results — verified performance metrics |

## Quick Start

Download all specs in this bundle:
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/bundle.zip
unzip bundle.zip -d my-agent/
```

Or clone just this example:
```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/marketplace-agent
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/HIREME.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/PRICING.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/WALLET.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/CV.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/TESTSCORES.md
```

## How It Works

These specs give an agent everything it needs to be discoverable and hireable:

- **HIREME.md** is the agent's public listing — what it does, when it's available, how to engage it
- **PRICING.md** defines the cost structure so clients know what they'll pay
- **WALLET.md** establishes financial identity for receiving payments
- **CV.md** shows proven track record with past engagements
- **TESTSCORES.md** provides verified benchmark results for objective comparison

Pair with the [Basic Agent bundle](../basic-agent/) for identity and governance specs.

## Related Specs

→ Full spec definitions: [HIREME.md](../../specs/business/HIREME.md) · [PRICING.md](../../specs/economic/PRICING.md) · [WALLET.md](../../specs/economic/WALLET.md) · [CV.md](../../specs/economic/CV.md) · [TESTSCORES.md](../../specs/quality/TESTSCORES.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
