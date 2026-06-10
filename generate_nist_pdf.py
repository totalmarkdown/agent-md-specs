"""Generate professional NIST NCCoE response PDF from markdown content."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib import colors
import os


OUTPUT_PATH = os.path.expanduser("~/Desktop/nist-nccoe-response.pdf")

# Also save to current-issues for easy access
COPY_PATH = os.path.expanduser("~/current-issues/nist-nccoe-response.pdf")


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'DocTitle',
        parent=styles['Title'],
        fontSize=16,
        leading=20,
        spaceAfter=6,
        fontName='Times-Bold',
        textColor=HexColor('#1a1a1a'),
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=2,
        fontName='Times-Roman',
        textColor=HexColor('#444444'),
    ))

    styles.add(ParagraphStyle(
        'SectionHead',
        parent=styles['Heading1'],
        fontSize=13,
        leading=16,
        spaceBefore=18,
        spaceAfter=8,
        fontName='Times-Bold',
        textColor=HexColor('#1a1a1a'),
    ))

    styles.add(ParagraphStyle(
        'SubHead',
        parent=styles['Heading2'],
        fontSize=11,
        leading=14,
        spaceBefore=12,
        spaceAfter=6,
        fontName='Times-Bold',
        textColor=HexColor('#333333'),
    ))

    styles.add(ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=6,
        fontName='Times-Roman',
        textColor=HexColor('#1a1a1a'),
        alignment=TA_JUSTIFY,
    ))

    styles.add(ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=6,
        fontName='Times-Bold',
        textColor=HexColor('#1a1a1a'),
    ))

    styles.add(ParagraphStyle(
        'BulletItem',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=3,
        fontName='Times-Roman',
        textColor=HexColor('#1a1a1a'),
        leftIndent=18,
        bulletIndent=6,
    ))

    styles.add(ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        fontName='Times-Roman',
        textColor=HexColor('#1a1a1a'),
    ))

    styles.add(ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        fontName='Times-Bold',
        textColor=HexColor('#1a1a1a'),
    ))

    styles.add(ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        fontName='Times-Roman',
        textColor=HexColor('#888888'),
        alignment=TA_CENTER,
    ))

    return styles


def make_table(headers, rows, col_widths=None):
    """Create a clean table with header row."""
    s = build_styles()
    data = [[Paragraph(h, s['TableCellBold']) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), s['TableCell']) for c in row])

    if col_widths is None:
        col_widths = [6.5 * inch / len(headers)] * len(headers)

    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#f0f0f0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#1a1a1a')),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#cccccc')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    canvas.setFillColor(HexColor('#888888'))
    canvas.drawString(
        inch, 0.5 * inch,
        "TotalMarkdown.ai — agent-md-specs — CC0 1.0 Universal"
    )
    canvas.drawRightString(
        7.5 * inch, 0.5 * inch,
        f"Page {doc.page}"
    )
    canvas.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.85 * inch,
        leftMargin=1 * inch,
        rightMargin=1 * inch,
    )

    s = build_styles()
    story = []

    # ── Title Block ──
    story.append(Paragraph(
        "Response to NCCoE Concept Paper:<br/>"
        '"Accelerating the Adoption of Software and<br/>'
        'AI Agent Identity and Authorization"',
        s['DocTitle']
    ))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#cccccc')))
    story.append(Spacer(1, 8))

    for line in [
        "<b>Submitted by:</b> TotalMarkdown.ai",
        "<b>Date:</b> March 2026",
        "<b>Repository:</b> github.com/totalmarkdown/agent-md-specs",
        "<b>Release:</b> v1.0.2-nist-submission",
        "<b>License:</b> CC0 1.0 Universal (Public Domain)",
    ]:
        story.append(Paragraph(line, s['DocSubtitle']))

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#dddddd')))

    # ── Section 1: Executive Response ──
    story.append(Paragraph("1. Executive Response", s['SectionHead']))

    story.append(Paragraph("The Problem", s['SubHead']))
    story.append(Paragraph(
        "AI agents operating in production environments need to declare far more than task instructions. "
        "They need verifiable identity, scoped authority, auditable intent, tamper-evident action records, "
        "and provable compliance with declared constraints. Current agent configuration approaches — "
        "including AGENTS.md (AAIF), CLAUDE.md (Anthropic), and ad-hoc program files — address behavior "
        "and project instructions but leave identity, authorization, and accountability undefined.",
        s['Body']
    ))

    story.append(Paragraph("Our Approach", s['SubHead']))
    story.append(Paragraph(
        "agent-md-specs is a proposed open standard library of 174 Markdown file type specifications "
        "covering every dimension of AI agent governance. The framework defines a declarative vocabulary "
        "layer that sits between human-readable policy definition and machine-enforceable runtime controls.",
        s['Body']
    ))
    story.append(Paragraph(
        "The specifications serve two distinct purposes:",
        s['Body']
    ))
    story.append(Paragraph(
        "<b>Static configuration specs</b> (e.g., WHOAMI.md, LIMITS.md, DELEGATION.md) are committed to "
        "version control and define the agent's permanent identity, constraints, and organizational "
        "configuration.",
        s['BulletItem'], bulletText='•'
    ))
    story.append(Paragraph(
        "<b>Runtime schema specs</b> (e.g., INTENT.md, SESSION.md, AUDITTRAIL.md) define the format "
        "and validation rules for ephemeral data generated during agent execution — API payloads, "
        "session tokens, and audit log entries. These are not files overwritten on disk; they are "
        "schemas that runtime systems consume.",
        s['BulletItem'], bulletText='•'
    ))
    story.append(Paragraph(
        "This distinction means agent-md-specs functions as a declarative policy specification that "
        "compiles down into machine-enforceable rules via policy engines (e.g., OPA/Rego), API gateways, "
        "and identity providers — not as a file-based runtime system.",
        s['Body']
    ))

    story.append(Paragraph("Why Markdown", s['SubHead']))
    story.append(Paragraph(
        "While machine-native formats (JSON, YAML) are necessary for runtime execution, they fail as "
        "human-auditable governance artifacts. Compliance officers, security architects, and enterprise "
        "CISOs need to read and approve the policies that govern agent behavior. Markdown provides this "
        "human readability while remaining machine-parseable via YAML frontmatter and structured sections. "
        "JSON Schema definitions are provided for all core specifications, enabling automated validation "
        "at three levels: syntax, completeness, and content conformance.",
        s['Body']
    ))

    story.append(Paragraph("Ecosystem Context", s['SubHead']))
    story.append(Paragraph(
        "The markdown-as-agent-configuration pattern is already an industry standard: AGENTS.md "
        "(60,000+ repositories), CLAUDE.md and SKILL.md (Anthropic ecosystem), and Karpathy's program.md "
        "(51,900+ stars). agent-md-specs standardizes and extends this pattern into the identity, "
        "governance, compliance, and accountability dimensions that production deployments require.",
        s['Body']
    ))

    # ── Section 2: Mapping ──
    story.append(Paragraph("2. Mapping to NCCoE Concept Paper Questions", s['SectionHead']))

    # 2.1
    story.append(Paragraph("2.1 Identification", s['SubHead']))
    story.append(Paragraph(
        '<i>"How might agents be identified in an enterprise architecture? '
        'What metadata is essential for an AI agent\'s identity?"</i>',
        s['Body']
    ))
    for item in [
        "<b>WHOAMI.md</b> — Declarative identity document: name, version, capabilities, model, owner, organizational affiliation.",
        "<b>ID.md</b> — Permanent UUID anchor with cryptographic binding.",
        "<b>ATTESTATION.md</b> — Identity verification via SPIFFE/SPIRE, X.509, or DIDs, with hardware binding (TPM/HSM) and software binding (container hash). Implements SP 800-63-4 identity assurance levels.",
        "<b>SESSION.md</b> — Ephemeral, task-scoped identity. Each session generates short-lived credentials destroyed on task completion.",
    ]:
        story.append(Paragraph(item, s['BulletItem'], bulletText='•'))

    # 2.2
    story.append(Paragraph("2.2 Authentication", s['SubHead']))
    story.append(Paragraph(
        '<i>"What constitutes strong authentication for an AI agent? How do we handle key management?"</i>',
        s['Body']
    ))
    for item in [
        "<b>ATTESTATION.md</b> — Complete credential lifecycle: issuance, rotation, revocation, and compromise recovery. Maps to SPIFFE/SPIRE and supports FIDO2/YubiKey for human-in-the-loop binding.",
        "<b>SECRETS.md</b> — Declares required credentials without storing values — the manifest that infrastructure teams provision from.",
    ]:
        story.append(Paragraph(item, s['BulletItem'], bulletText='•'))

    # 2.3
    story.append(Paragraph("2.3 Authorization", s['SubHead']))
    story.append(Paragraph(
        '<i>"How can zero-trust principles be applied? How do we establish least privilege? '
        'How do we handle delegation? How might an agent convey intent?"</i>',
        s['Body']
    ))
    for item in [
        "<b>DELEGATION.md</b> — Complete authority chain from human principal to agent with scope constraints, time bounds, budget caps, sub-delegation policies, and revocation. Maps to OAuth 2.0 On-Behalf-Of flows. Addresses the confused deputy problem via explicit scope allow-lists.",
        "<b>LEASTPRIVILEGE.md</b> — SP 800-207 zero-trust: minimal baseline, JIT escalation, automatic de-escalation, deny-and-log for unknown actions.",
        "<b>INTENT.md</b> — Pre-action intent declaration with confidence scoring, impact assessment, and human review thresholds. Confidence scores must be externally validated, not agent self-assessed. Intent declarations are hash-bound to audit trail entries.",
    ]:
        story.append(Paragraph(item, s['BulletItem'], bulletText='•'))

    # 2.4
    story.append(Paragraph("2.4 Auditing and Non-Repudiation", s['SubHead']))
    story.append(Paragraph(
        '<i>"How can we ensure tamper-proof logging? How do we ensure non-repudiation?"</i>',
        s['Body']
    ))
    story.append(Paragraph(
        "<b>AUDITTRAIL.md</b> — Tamper-resistant records with hash-chain integrity, cryptographic signing, "
        "and compliance retention mappings (GDPR: 3yr, HIPAA: 6yr, SOC2: 1yr, EU AI Act: 10yr). Each entry "
        "links to the delegation chain, declared intent, and I/O hashes for complete non-repudiation.",
        s['BulletItem'], bulletText='•'
    ))

    # 2.5
    story.append(Paragraph("2.5 Data Flow Tracking", s['SubHead']))
    story.append(Paragraph(
        '<i>"Track and maintain provenance of user prompts and data input sources."</i>',
        s['Body']
    ))
    story.append(Paragraph(
        "<b>PROVENANCE.md</b> — Input source registries with trust classification, prompt provenance, "
        "context window hashing, transformation logs, and data classification escalation rules — addressing "
        "sensitivity when individually non-sensitive data becomes sensitive when aggregated.",
        s['BulletItem'], bulletText='•'
    ))

    # 2.6
    story.append(Paragraph("2.6 Prompt Injection", s['SubHead']))
    story.append(Paragraph(
        '<i>"What controls help prevent prompt injections? What minimizes impact after injection?"</i>',
        s['Body']
    ))
    story.append(Paragraph(
        "<b>PROMPTSHIELD.md</b> — Defense-in-depth: instruction boundary enforcement, privilege separation, "
        "content sandboxing, canary token detection, containment procedures, recovery playbooks, and red team "
        "testing requirements. Treats injection as a capability integrity problem.",
        s['BulletItem'], bulletText='•'
    ))

    # ── Section 3: Accountability Chain ──
    story.append(Paragraph("3. The Accountability Chain", s['SectionHead']))
    story.append(Paragraph(
        "These specifications create a complete, verifiable chain from human authorization to tamper-evident "
        "record, mapped to operational phases and SP 800-207 Zero Trust Architecture components:",
        s['Body']
    ))

    chain_table = make_table(
        ["Step", "Specification", "Question Answered", "Phase", "ZTA Component"],
        [
            ["1", "DELEGATION.md", "Who authorized this agent?", "Pre-deployment", "Policy Info Point"],
            ["2", "WHOAMI.md + ID.md", "Who is this agent?", "Pre-deployment", "Policy Info Point"],
            ["3", "ATTESTATION.md", "Can it prove its identity?", "Runtime (continuous)", "Policy Info Point"],
            ["4", "SESSION.md", "What is its runtime scope?", "Runtime (per-task)", "Microsegmentation"],
            ["5", "LEASTPRIVILEGE.md", "What can it do right now?", "Runtime (per-action)", "Policy Decision Pt"],
            ["6", "INTENT.md", "What does it intend to do?", "Runtime (per-action)", "Trust zone boundary"],
            ["7", "PROMPTSHIELD.md", "Is the input safe?", "Runtime (per-input)", "Policy Enforce. Pt"],
            ["8", "PROVENANCE.md", "Where did the data come from?", "Runtime (per-input)", "Policy Info Point"],
            ["", "[ACTION TAKEN]", "", "", ""],
            ["9", "AUDITTRAIL.md", "What happened, provably?", "Post-action", "Continuous Diag."],
            ["10", "ENFORCEMENT.md", "Can we verify all above?", "Continuous", "Policy Enforce. Pt"],
            ["11", "ESCALATION.md", "Should a human review?", "On-trigger", "Human override"],
        ],
        col_widths=[0.35*inch, 1.15*inch, 1.6*inch, 1.15*inch, 1.15*inch]
    )
    story.append(chain_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "ENFORCEMENT.md defines three verification layers: (1) pre-deployment CI/CD validation, "
        "(2) runtime behavioral drift detection via infrastructure-level policy enforcement points "
        "(not on-agent self-policing), and (3) post-hoc cryptographic verification of audit trails "
        "against declared intents and delegation chains.",
        s['Body']
    ))

    # ── Section 4: Atlas Example ──
    story.append(Paragraph("4. Demonstration: The Atlas Enterprise Example", s['SectionHead']))
    story.append(Paragraph(
        "The repository includes a complete enterprise example demonstrating all accountability chain "
        "specs in a realistic financial services scenario.",
        s['Body']
    ))

    for line in [
        "<b>Agent:</b> Atlas v2.1 — Financial Analysis Agent",
        "<b>Organization:</b> Acme Corp (fictional)",
        "<b>Delegated by:</b> CFO Sarah Chen",
        "<b>Model:</b> Claude Sonnet 4",
        "<b>Purpose:</b> Generate quarterly financial reports and forecasts",
    ]:
        story.append(Paragraph(line, s['DocSubtitle']))

    story.append(Spacer(1, 6))

    for item in [
        "Delegation scoped to read-only financial data and report generation, expiring quarterly, no sub-delegation, revocable via compliance portal",
        "SPIFFE workload identity (spiffe://acme.corp/finance/agents/atlas) with X.509 certificate and 90-day key rotation",
        "30-minute session boundaries with ephemeral in-memory credentials, max 50 actions, mandatory memory wipe (audit entries preserved)",
        "JIT privilege escalation requiring CFO FIDO2 approval for email, auto de-escalation after single use",
        "SHA-256 hash-chain audit trail with 7-year SOX retention, signed entries, auditor query endpoint",
        "Financial-domain canary tokens, SQL injection blocking, halt-and-alert containment",
        "Hard limits: never execute trades, never access HR data, never communicate outside acme.corp",
    ]:
        story.append(Paragraph(item, s['BulletItem'], bulletText='•'))

    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Repository path: examples/nist-nccoe-bundle/",
        s['Body']
    ))

    # ── Section 5: Standards Alignment ──
    story.append(Paragraph("5. Standards Alignment and Next Steps", s['SectionHead']))

    story.append(Paragraph("Relationship to Referenced Standards", s['SubHead']))

    standards_table = make_table(
        ["Standard", "Role", "How agent-md-specs Relates"],
        [
            ["MCP (AAIF)", "Tool connectivity", "Governs which MCP connections are authorized via PERMISSIONS.md"],
            ["AGENTS.md", "Project instructions", "agent-md-specs adds identity, governance, accountability"],
            ["OAuth 2.0 / OIDC", "Auth transport", "DELEGATION.md defines policy; OAuth transports at runtime"],
            ["SPIFFE/SPIRE", "Workload identity", "ATTESTATION.md specifies SPIFFE as primary verification method"],
            ["SP 800-207", "Zero Trust Arch.", "11-step accountability chain maps to PEP, PDP, PIP"],
            ["SP 800-63-4", "Digital Identity", "WHOAMI.md + ATTESTATION.md implement assurance levels"],
            ["NGAC", "Attribute-based AC", "LEASTPRIVILEGE.md defines dynamic policies NGAC enforces"],
            ["SCIM", "Identity lifecycle", "SESSION.md credential lifecycle maps to SCIM provisioning"],
        ],
        col_widths=[1.1*inch, 1.0*inch, 3.4*inch]
    )
    story.append(standards_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Tooling and Validation", s['SubHead']))
    for item in [
        "<b>agent-md-validator</b> (v0.1.0): Open-source CLI validating YAML frontmatter, required sections, cross-references, and tier compliance. github.com/totalmarkdown/agent-md-validator",
        "<b>JSON Schemas</b>: Machine-readable definitions for all 39 Core specs enabling automated Level 1 (syntax), Level 2 (completeness), and Level 3 (content) validation.",
    ]:
        story.append(Paragraph(item, s['BulletItem'], bulletText='•'))

    story.append(Paragraph("Governance", s['SubHead']))
    story.append(Paragraph(
        "The project follows a formal specification lifecycle (Draft → Proposed → Stable → Deprecated → Retired) "
        "with an RFC process for Core spec changes. All 174 specifications are CC0 public domain with zero "
        "licensing friction for adoption by government agencies, enterprises, or standards bodies.",
        s['Body']
    ))

    story.append(Paragraph("Invitation", s['SubHead']))
    story.append(Paragraph(
        "We welcome the opportunity to participate in future NCCoE workshops, demonstration projects, or "
        "working groups related to AI agent identity and authorization. The complete framework is available at:",
        s['Body']
    ))
    story.append(Paragraph(
        "<b>https://github.com/totalmarkdown/agent-md-specs</b>",
        s['Body']
    ))

    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#cccccc')))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<i>Submitted by TotalMarkdown.ai · CC0 1.0 Universal (Public Domain) · March 2026</i>",
        s['Footer']
    ))

    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated: {OUTPUT_PATH}")

    # Copy to current-issues
    import shutil
    shutil.copy2(OUTPUT_PATH, COPY_PATH)
    print(f"Copy saved: {COPY_PATH}")


if __name__ == "__main__":
    build_pdf()
