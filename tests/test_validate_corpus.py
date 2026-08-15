"""Regression tests for the corpus validator and the invariants it protects.

Run with:

    pip install jsonschema pyyaml pytest
    python3 -m pytest tests/ -q
"""

from __future__ import annotations

import json
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

import validate_corpus as vc  # noqa: E402

ROOT = vc.REPO_ROOT
ALL_SURFACES = {'specs', 'templates', 'examples'}
SPEC_IDENTITY_KEYS = ('spec_name', 'spec_version', 'category', 'priority', 'tier')
LIFECYCLE_STATUSES = ('draft', 'proposed', 'stable', 'deprecated', 'retired')


@pytest.fixture(scope='module')
def run():
    results, stale = vc.validate(ROOT, ALL_SURFACES)
    return results, stale


def documents(surface):
    """Every (path, surface, schema) binding for a surface. A document can
    appear more than once — specs are bound to two schemas."""
    return [(p, s, n) for p, s, n in vc.collect_documents(ROOT) if s == surface]


def files(surface):
    """Distinct document paths on a surface, in order."""
    seen, out = set(), []
    for path, _surface, _schema in documents(surface):
        if path not in seen:
            seen.add(path)
            out.append(path)
    return out


def frontmatter(path):
    return vc.read_frontmatter(os.path.join(ROOT, path))


# --------------------------------------------------------------------------
# the validator itself
# --------------------------------------------------------------------------

def test_corpus_has_no_unregistered_failures(run):
    results, _ = run
    failures = [(p, n, e) for p, _s, n, e, _k in results if e]
    assert failures == []


def test_no_stale_known_deviations(run):
    """A registered deviation that stopped reproducing must be deleted, or the
    registry silently becomes a suppression list."""
    _, stale = run
    assert stale == []


def test_every_surface_is_actually_checked(run):
    """CD-8: the failure mode was a surface nobody validated. Assert each one
    contributes checks."""
    results, _ = run
    checked = {s for _p, s, _n, _e, _k in results}
    assert checked == ALL_SURFACES
    counts = {s: sum(1 for _p, sur, _n, _e, _k in results if sur == s) for s in ALL_SURFACES}
    assert counts['templates'] >= 32
    assert counts['specs'] >= 179
    assert counts['examples'] >= 70


def test_per_spec_schemas_are_executed():
    """CD-5b: per-spec schemas must be bound to real documents, not just
    listed in schemas/README.md."""
    bound = {n for _p, _s, n in vc.collect_documents(ROOT)
             if n not in vc.NON_SPEC_SCHEMAS}
    assert len(bound) >= 20, 'per-spec schemas are not reaching the corpus'
    assert 'audittrail.schema.json' in bound
    assert 'delegation.schema.json' in bound


def test_schema_refs_resolve_without_network():
    """The registry refuses unknown URIs, so a resolvable $ref proves local
    resolution. contact.schema.json $refs frontmatter.schema.json."""
    registry = vc.build_registry()
    validator = vc.load_schema('contact.schema.json', registry)
    errors = list(validator.iter_errors({'spec_name': 'CONTACT.md', 'spec_version': '0.1.0',
                                         'category': 'Communication', 'tier': 'extended',
                                         'email': 'a@b.test'}))
    assert errors == []


def test_unknown_ref_is_refused_not_fetched():
    registry = vc.build_registry()
    with pytest.raises(Exception):
        registry.resolver().lookup('https://example.invalid/nope.schema.json')


def test_yaml_dates_are_normalised_for_json_schema():
    data = vc.read_frontmatter(os.path.join(ROOT, 'specs', 'compliance', 'AUDITTRAIL.md'))
    assert data['proposed_on'] == '2026-04-18'
    assert isinstance(data['proposed_on'], str)


@pytest.mark.parametrize('body,expected', [
    ('# no frontmatter\n', 'no YAML frontmatter block'),
    ('---\nspec_name: X.md\n', 'unterminated'),
    ('---\n- a\n- b\n---\n', 'not a mapping'),
])
def test_frontmatter_parser_rejects_malformed_documents(tmp_path, body, expected):
    path = tmp_path / 'BAD.md'
    path.write_text(body, encoding='utf-8')
    with pytest.raises(vc.FrontmatterError) as exc:
        vc.read_frontmatter(str(path))
    assert expected in str(exc.value)


def test_known_deviation_registry_entries_are_complete():
    required = {'path', 'schema', 'json_path', 'keyword', 'error_signature',
                'surface', 'defect', 'track', 'reason'}
    assert set(vc.DEVIATION_FIELDS) == required
    for entry in vc.load_deviations():
        assert required <= set(entry), entry
        assert os.path.exists(os.path.join(ROOT, entry['path'])), entry['path']
        assert len(entry['reason']) > 80, 'a deviation needs a real justification'
        assert re.match(r'^[0-9a-f]{64}$', entry['error_signature']), entry


# --------------------------------------------------------------------------
# known deviations are bound to one named error, not to a location
#
# The registry's whole claim is that it is not a suppression list. Matching on
# path + schema + JSON path + keyword alone does not support that claim: a
# materially different error at the same coordinates would inherit the excuse.
# These tests pin the signature binding and the substitution failure.
# --------------------------------------------------------------------------

def _errors(schema, instance):
    registry = vc.Registry()
    validator = vc.Draft202012Validator(schema, registry=registry)
    return sorted(validator.iter_errors(instance), key=lambda e: e.json_path)


# Two branches that can each fail in more than one way, so the same anyOf
# keyword at the same JSON path can fail with different internal structure.
MINI_SCHEMA = {
    '$schema': 'https://json-schema.org/draft/2020-12/schema',
    '$id': 'https://totalmarkdown.ai/schemas/mini.schema.json',
    'title': 'MINI.md Schema',
    'anyOf': [
        {'required': ['alpha']},
        {'required': ['beta'], 'properties': {'beta': {'type': 'string'}}},
    ],
}

# Both instances fail MINI_SCHEMA with keyword `anyOf` at json_path `$`.
MISSING_BOTH = {'gamma': 1}       # neither branch's required key is present
WRONG_TYPE = {'beta': 5}          # beta present but the wrong type


def test_error_signature_is_stable_across_unrelated_instance_edits():
    """A signature that churns when an unrelated field is edited is a signature
    nobody maintains, and the registry would decay to matching on location."""
    base = _errors(MINI_SCHEMA, MISSING_BOTH)
    extra = _errors(MINI_SCHEMA, dict(MISSING_BOTH, unrelated='new value'))
    assert len(base) == len(extra) == 1
    assert vc.error_signature(base[0]) == vc.error_signature(extra[0])


def test_error_signature_distinguishes_a_materially_different_failure():
    """Same schema, same keyword, same JSON path — different failure inside."""
    a, b = _errors(MINI_SCHEMA, MISSING_BOTH)[0], _errors(MINI_SCHEMA, WRONG_TYPE)[0]
    assert (a.json_path, a.validator) == (b.json_path, b.validator) == ('$', 'anyOf')
    assert vc.error_signature(a) != vc.error_signature(b)


def test_error_signature_is_bound_to_the_schema_constraint():
    """Editing the constraint the deviation was reasoned about changes the
    signature, so the entry must be re-reviewed rather than silently carried."""
    widened = json.loads(json.dumps(MINI_SCHEMA))
    widened['anyOf'].append({'required': ['delta']})
    a = _errors(MINI_SCHEMA, MISSING_BOTH)[0]
    b = _errors(widened, MISSING_BOTH)[0]
    assert vc.error_signature(a) != vc.error_signature(b)


def test_a_substituted_error_does_not_match_the_registered_deviation():
    """The masquerade the review found: coarse coordinates match, so the entry
    is indexed against this error — but it must not be excused by it."""
    registered = _errors(MINI_SCHEMA, MISSING_BOTH)[0]
    substituted = _errors(MINI_SCHEMA, WRONG_TYPE)[0]
    entry = {'path': 'examples/mini-bundle/MINI.md', 'schema': 'mini.schema.json',
             'json_path': '$', 'keyword': 'anyOf',
             'error_signature': vc.error_signature(registered)}
    args = (entry, 'examples/mini-bundle/MINI.md', 'mini.schema.json')

    assert vc.deviation_targets(*args, registered)
    assert vc.deviation_matches(*args, registered)

    assert vc.deviation_targets(*args, substituted), 'the entry is indexed against it'
    assert not vc.deviation_matches(*args, substituted), 'but it must not be excused'


def test_registered_deviation_matches_the_error_it_names():
    """Positive control: the real registry entry is bound to the real error, so
    the signature mechanism is not merely refusing everything."""
    entries = [e for e in vc.load_deviations() if e['path'] == 'specs/identity/CONTACT.md']
    assert len(entries) == 1
    entry = entries[0]
    validator = vc.load_schema(entry['schema'], vc.build_registry())
    data = frontmatter(entry['path'])
    matches = [e for e in validator.iter_errors(data)
               if vc.deviation_matches(entry, entry['path'], entry['schema'], e)]
    assert len(matches) == 1, 'the registered CD-5c deviation no longer names a real error'


# --------------------------------------------------------------------------
# a miniature corpus, so registry behaviour can be exercised end to end
# without touching the real schemas/ or known-deviations.json
# --------------------------------------------------------------------------

@pytest.fixture
def mini_corpus(tmp_path, monkeypatch):
    """Build a throwaway corpus and point the validator's schema directory and
    deviation registry at it. Returns (root, write_document, write_registry)."""
    root = tmp_path / 'corpus'
    schemas = root / 'schemas'
    schemas.mkdir(parents=True)
    (root / 'specs' / 'mini').mkdir(parents=True)
    (root / 'examples' / 'mini-bundle').mkdir(parents=True)
    (schemas / 'mini.schema.json').write_text(json.dumps(MINI_SCHEMA), encoding='utf-8')
    (root / 'specs' / 'mini' / 'MINI.md').write_text('---\nspec_name: MINI.md\n---\n', encoding='utf-8')
    monkeypatch.setattr(vc, 'SCHEMA_DIR', str(schemas))
    monkeypatch.setattr(vc, 'DEVIATIONS_FILE', str(schemas / 'known-deviations.json'))

    doc = root / 'examples' / 'mini-bundle' / 'MINI.md'

    def write_document(frontmatter_mapping):
        body = ''.join('%s: %s\n' % (k, json.dumps(v)) for k, v in frontmatter_mapping.items())
        doc.write_text('---\n%s---\n\n# MINI\n' % body, encoding='utf-8')

    def write_registry(instance):
        signature = vc.error_signature(_errors(MINI_SCHEMA, instance)[0])
        (schemas / 'known-deviations.json').write_text(json.dumps({'deviations': [{
            'path': 'examples/mini-bundle/MINI.md', 'schema': 'mini.schema.json',
            'json_path': '$', 'keyword': 'anyOf', 'error_signature': signature,
            'surface': 'examples', 'defect': 'MINI-1', 'track': 1,
            'reason': 'x' * 100,
        }]}), encoding='utf-8')

    return root, write_document, write_registry


def test_registered_example_deviation_is_reported_not_failed(mini_corpus):
    root, write_document, write_registry = mini_corpus
    write_document(MISSING_BOTH)
    write_registry(MISSING_BOTH)
    results, stale = vc.validate(str(root), {'examples'})
    assert stale == []
    assert [e for _p, _s, _n, e, _k in results] == [[]]
    assert len(results[0][4]) == 1


def test_a_substituted_example_error_fails_the_run(mini_corpus):
    """End to end: the registry names one failure; a different failure appears
    at the same location. It must be reported as unregistered *and* leave the
    entry stale, so the run cannot come out green."""
    root, write_document, write_registry = mini_corpus
    write_registry(MISSING_BOTH)
    write_document(WRONG_TYPE)
    results, stale = vc.validate(str(root), {'examples'})
    errors = [e for _p, _s, _n, e, _k in results for e in e]
    assert len(errors) == 1
    assert 'does not describe this error' in errors[0]
    assert len(stale) == 1, 'the entry no longer reproduces and must be flagged'
    assert vc.report(results, stale, {'examples'}) is False


def _summary_row(output, surface):
    """The named cells of one row of report()'s summary table."""
    lines = output.splitlines()
    header = [l for l in lines if l.startswith('surface')][0].split()[1:]
    row = [l for l in lines if l.startswith(surface)][0].split()[1:]
    assert len(header) == len(row)
    return dict(zip(header, row))


def test_report_never_counts_a_known_deviation_as_passed(mini_corpus, capsys):
    """The review finding: a document with a live known failure was counted in
    `passed`. It belongs in `known`."""
    root, write_document, write_registry = mini_corpus
    write_document(MISSING_BOTH)
    write_registry(MISSING_BOTH)
    results, stale = vc.validate(str(root), {'examples'})
    assert vc.report(results, stale, {'examples'}) is True
    assert _summary_row(capsys.readouterr().out, 'examples') == {
        'files': '1', 'checks': '1', 'passed': '0',
        'known': '1', 'failed': '0', 'errors': '0'}


def test_the_real_corpus_reports_contact_as_known_not_passed(run, capsys):
    """The same finding, on the real corpus: 179 spec files, 178 clean."""
    results, stale = run
    vc.report(results, stale, ALL_SURFACES)
    out = capsys.readouterr().out
    assert _summary_row(out, 'specs') == {'files': '179', 'checks': '203', 'passed': '178',
                                          'known': '1', 'failed': '0', 'errors': '0'}
    assert 'known deviation is a live failure, not a pass' in out


def test_deviation_registry_requires_a_signature(mini_corpus):
    root, _write_document, _write_registry = mini_corpus
    open(vc.DEVIATIONS_FILE, 'w', encoding='utf-8').write(json.dumps({'deviations': [{
        'path': 'examples/mini-bundle/MINI.md', 'schema': 'mini.schema.json',
        'json_path': '$', 'keyword': 'anyOf', 'surface': 'examples',
        'defect': 'MINI-1', 'track': 1, 'reason': 'x' * 100}]}))
    with pytest.raises(vc.DeviationRegistryError) as exc:
        vc.load_deviations()
    assert 'error_signature' in str(exc.value)


def test_deviation_registry_rejects_a_malformed_signature(mini_corpus):
    root, _write_document, _write_registry = mini_corpus
    open(vc.DEVIATIONS_FILE, 'w', encoding='utf-8').write(json.dumps({'deviations': [{
        'path': 'examples/mini-bundle/MINI.md', 'schema': 'mini.schema.json',
        'json_path': '$', 'keyword': 'anyOf', 'error_signature': 'not-a-hash',
        'surface': 'examples', 'defect': 'MINI-1', 'track': 1, 'reason': 'x' * 100}]}))
    with pytest.raises(vc.DeviationRegistryError):
        vc.load_deviations()


# --------------------------------------------------------------------------
# CD-5a / CD-8 — templates are conformant and stay conformant
# --------------------------------------------------------------------------

def test_every_template_declares_the_identity_of_its_spec():
    specs = {os.path.basename(p): frontmatter(p) for p in files('specs')}
    seen = 0
    for path in files('templates'):
        name = os.path.basename(path).replace('.template.md', '.md')
        assert name in specs, '%s has no matching spec' % path
        template = frontmatter(path)
        for key in SPEC_IDENTITY_KEYS:
            assert template.get(key) == specs[name].get(key), \
                '%s: %s is %r, spec says %r' % (path, key, template.get(key), specs[name].get(key))
        seen += 1
    assert seen == 32


# --------------------------------------------------------------------------
# TOTA-79 / TOTA-90 / TOTA-80 — the `domain` assertion stays removed
#
# TOTA-79 removed 179 per-spec `domain:` assertions because 132 of the named
# .dev domains were unregistered and available to anyone: a CC0 standard that
# points readers at domains it does not control invites a cheap, plausible
# hijack. TOTA-90 did the same for examples/, TOTA-80 for the two remaining
# third-party pointers at the repo root, and this change for templates/.
#
# Nothing in the corpus stopped it coming back. These are the regressions that
# do — fail-closed, over the whole of specs/** and templates/**, so a spec or
# template added later is covered without anyone remembering to list it.
# --------------------------------------------------------------------------

def test_no_frontmatter_domain_assertion_anywhere_in_specs_and_templates():
    """The corpus-wide guard. Frontmatter only — deliberately not a repo-wide
    `^domain:` regex, which would also match the `domain: string` lines inside
    the fenced schema-example blocks in specs/cognitive/TRAINING.md and
    specs/identity/GLOSSARY.md. Those are spec content describing a field an
    adopter's own document may carry, not assertions this repo makes, and
    TOTA-79 preserved them deliberately."""
    checked = 0
    for surface in ('specs', 'templates'):
        for path in files(surface):
            assert 'domain' not in frontmatter(path), (
                '%s reintroduces a `domain:` frontmatter assertion. It was removed '
                'deliberately (TOTA-79/90/80 + TOTA-81); no replacement field is '
                'added and the canonical location is the repository itself.' % path)
            checked += 1
    # Fail closed: an empty or mis-globbed corpus must not pass vacuously.
    assert checked == 179 + 32, 'expected 211 documents, checked %d' % checked


def test_the_frontmatter_contract_does_not_define_domain():
    """Requirement (2): the schema must not require *or* offer the field. A
    validator that still advertises `domain` as a known property is an
    invitation to put it back."""
    for name in ('frontmatter.schema.json', 'spec-document.schema.json'):
        with open(os.path.join(ROOT, 'schemas', name), encoding='utf-8') as fh:
            schema = json.load(fh)
        assert 'domain' not in schema.get('properties', {}), name
        assert 'domain' not in schema.get('required', []), name
        assert 'domain' not in schema.get('then', {}).get('required', []), name


def test_contributor_docs_do_not_ask_for_a_domain_field():
    """The prose contract, which is what a human contributor actually reads.
    CONTRIBUTING.md's frontmatter list and the PR template's frontmatter
    checklist both named `domain` as required long after the field was gone."""
    for rel in ('CONTRIBUTING.md', os.path.join('.github', 'PULL_REQUEST_TEMPLATE.md')):
        text = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        for line in text.split('\n'):
            if 'domain' not in line.lower():
                continue
            # Allowed: prose that says the field does *not* exist, and the CC0
            # "public domain" boilerplate.
            if re.search(r'no `?domain`? (field|frontmatter)|not assert|fails? CI'
                         r'|public domain|public-domain', line, re.I):
                continue
            assert 'frontmatter' not in line.lower() and 'required' not in line.lower(), \
                '%s still asks contributors for a domain field: %r' % (rel, line.strip())


# --------------------------------------------------------------------------
# TOTA-109 — the prose field list and the enforced schema are one contract
#
# The inverse of the sweep above. That one catches a doc asking for a field
# the schema rejects; these catch a doc omitting fields the schema requires.
# CONTRIBUTING.md listed neither `tier` nor `status` for months, so frontmatter
# written by following it produced five schema errors. Nothing caught it
# because the existing 179 specs are all clean — only new contributors, who
# are the entire audience for that file, ever hit it.
#
# Every expectation below is *derived* from schemas/. Restating the field list
# in the test would just move the drift one file over.
# --------------------------------------------------------------------------

CONTRIBUTING_MD = 'CONTRIBUTING.md'
PR_TEMPLATE_MD = os.path.join('.github', 'PULL_REQUEST_TEMPLATE.md')


def doc_text(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8').read()


def contributing_section(heading='## Spec format requirements'):
    body = doc_text(CONTRIBUTING_MD).split(heading)
    assert len(body) == 2, '%s has %d %r headings, expected 1' % (
        CONTRIBUTING_MD, len(body) - 1, heading)
    return body[1].split('\n## ')[0]


def spec_document_validator():
    """The validator CI runs, not a lookalike: same registry, same local-only
    $ref resolution as tools/validate_corpus.py."""
    return vc.load_schema('spec-document.schema.json', vc.build_registry())


def enforced_required_fields(tier):
    """Ask the validator which fields it demands for a spec of this tier;
    do not re-read `required` by hand. `required` alone is a trap —
    frontmatter.schema.json carries an if/then that makes `priority`
    required when `tier: core`, and a hand-read misses it. Missing exactly
    that kind of clause is the bug this section exists to prevent."""
    missing = set()
    for error in spec_document_validator().iter_errors({'tier': tier}):
        match = re.match(r"^'([^']+)' is a required property$", error.message)
        if match:
            missing.add(match.group(1))
    assert missing, 'no required-property errors for tier=%r; check would pass vacuously' % tier
    return missing | {'tier'}  # supplied in the probe, so never reported missing


def documented_required_fields():
    """CONTRIBUTING.md's nested `**required**` bullet list, as
    {field: bullet text, continuation lines folded in}, in document order."""
    fields, inside, current = {}, False, None
    for line in contributing_section().split('\n'):
        if re.match(r'^(\S|-\s)', line):
            inside = bool(re.search(r'\*\*required\*\*', line))
            current = None
            continue
        nested = re.match(r'^  -\s+`([a-z_]+)`\s*(.*)$', line)
        if inside and nested:
            current = nested.group(1)
            fields[current] = nested.group(2)
        elif current and re.match(r'^    \S', line):
            fields[current] += ' ' + line.strip()
        elif not line.strip():
            current = None
    return fields


def test_contributing_lists_exactly_the_fields_the_schema_requires():
    documented = documented_required_fields()
    assert documented, '%s has no nested **required** frontmatter list' % CONTRIBUTING_MD
    assert set(documented) == enforced_required_fields('core'), (
        '%s documents %s; the schema requires %s'
        % (CONTRIBUTING_MD, sorted(documented), sorted(enforced_required_fields('core'))))


def test_contributing_flags_the_conditionally_required_fields_as_conditional():
    """`priority` is required only for `tier: core`. Listing it flatly as
    required is wrong in the other direction, and the honest fix is to say
    when it applies rather than to pick a side."""
    conditional = enforced_required_fields('core') - enforced_required_fields('extended')
    documented = documented_required_fields()
    for field in conditional:
        assert re.search(r'required for\s+`tier:\s*core`', documented[field], re.I), \
            '%s does not say %r is required only for tier: core' % (CONTRIBUTING_MD, field)
    for field in set(documented) - conditional:
        assert not re.search(r'required for\s+`tier:', documented[field], re.I), \
            '%s marks %r conditional, but the schema requires it always' % (CONTRIBUTING_MD, field)


def test_pr_template_checklist_lists_exactly_the_fields_the_schema_requires():
    lines = [l for l in doc_text(PR_TEMPLATE_MD).split('\n') if 'required fields' in l]
    assert len(lines) == 1, 'expected 1 frontmatter checklist line, found %d' % len(lines)
    head = lines[0].split('required fields', 1)[1].split('(')[0]
    documented = set(re.findall(r'`([a-z_]+)`', head))
    assert documented == enforced_required_fields('core'), (
        '%s checklist names %s; the schema requires %s'
        % (PR_TEMPLATE_MD, sorted(documented), sorted(enforced_required_fields('core'))))


def test_contributing_gives_the_allowed_values_for_every_enumerated_field():
    """A field name without its enum is still a CI failure in waiting:
    `category: identity` and `priority: extended` both parse and both fail."""
    section = contributing_section()
    validator = spec_document_validator()
    checked = 0
    for field in sorted(documented_required_fields()):
        enum = enumerated_values(validator.schema, field)
        if enum is None or len(enum) > 12:
            continue  # `category` has 40-odd values; covered by the check below
        for value in enum:
            assert '`%s`' % value in section, \
                '%s omits the %r value %r' % (CONTRIBUTING_MD, field, value)
        checked += 1
    # Fail closed: an unparsed or empty field list must not pass vacuously —
    # that is precisely the state CONTRIBUTING.md was in before TOTA-109.
    assert checked >= 3, 'only %d enumerated fields checked; expected tier, status, priority' % checked


def enumerated_values(schema, field):
    """The enum for a field, wherever in the composed schema it is declared."""
    for source in [schema] + [vc.load_schema(os.path.basename(entry['$ref']),
                                             vc.build_registry()).schema
                              for entry in schema.get('allOf', []) if '$ref' in entry]:
        prop = source.get('properties', {}).get(field)
        if prop and 'enum' in prop:
            return prop['enum']
    return None


def test_contributing_category_examples_are_real_enum_values():
    """`category` is a capitalised label, not the lowercase directory name.
    Guessing it from the path is how a contributor writes `identity`."""
    section = contributing_section()
    categories = enumerated_values(spec_document_validator().schema, 'category')
    examples = re.search(r'`category`.*?\(e\.g\.\s*([^)]*)\)', section, re.S)
    assert examples, '%s gives no example category values' % CONTRIBUTING_MD
    found = re.findall(r'`([^`]+)`', examples.group(1))
    assert found, '%s example categories are not in backticks' % CONTRIBUTING_MD
    for value in found + re.findall(r'`category:\s*([^`]+)`', section):
        assert value in categories, \
            '%s offers category %r, which is not in the enum' % (CONTRIBUTING_MD, value)
    assert any(' ' in value for value in found), \
        '%s gives no multi-word category example, the case that trips on casing' % CONTRIBUTING_MD


def test_frontmatter_written_from_contributing_validates_clean():
    """The acceptance check, run the way the defect was found: build a
    frontmatter block using only what CONTRIBUTING.md tells a contributor —
    every required field, each set to the first value the doc offers for it —
    and validate it against the schema CI enforces. This construction
    produced 5 errors before TOTA-109 and must produce 0 after."""
    validator = spec_document_validator()
    for tier in enumerated_values(validator.schema, 'tier'):
        instance = {'tier': tier}
        for field, bullet in documented_required_fields().items():
            if field == 'tier':
                continue
            offered = re.findall(r'`([^`]+)`', bullet)
            assert offered, '%s offers no value for %r' % (CONTRIBUTING_MD, field)
            instance[field] = offered[0]
        errors = [e.message for e in validator.iter_errors(instance)]
        assert errors == [], 'frontmatter per %s (tier=%s) fails: %s' % (
            CONTRIBUTING_MD, tier, errors)


def test_frontmatter_with_a_multi_word_category_validates_clean():
    """The `specs/regulatory/` → `Regulatory Compliance` mapping, which is the
    single most likely thing for a contributor to get wrong."""
    validator = spec_document_validator()
    instance = {'spec_name': 'MYSPEC.md', 'spec_version': '1.0.0',
                'category': 'Regulatory Compliance', 'tier': 'core',
                'status': 'draft', 'priority': 'High'}
    assert [e.message for e in validator.iter_errors(instance)] == []


def test_contributing_names_the_schema_that_actually_governs_specs():
    """It named frontmatter.schema.json, which omits `status`. Following the
    named schema to the letter still failed CI."""
    section = contributing_section()
    assert 'schemas/spec-document.schema.json' in section, \
        '%s does not name spec-document.schema.json as the contract' % CONTRIBUTING_MD
    assert re.search(r'authoritative machine contract is\s*\n?`schemas/spec-document',
                     section), '%s points "authoritative" at the wrong schema' % CONTRIBUTING_MD


def test_contributor_docs_are_in_the_validate_specs_workflow_triggers():
    """Same argument as the templates trigger above, one file over. Every
    check in this module lives in the pytest job, and that job did not fire on
    an edit to CONTRIBUTING.md or the PR template — so the guards protecting
    those two files could not run on a change to them. A check that cannot
    fire on the file it guards is not a check."""
    workflow = open(os.path.join(ROOT, '.github', 'workflows', 'validate-specs.yml'),
                    encoding='utf-8').read()
    for path in ('CONTRIBUTING.md', '.github/PULL_REQUEST_TEMPLATE.md'):
        assert workflow.count("- '%s'" % path) >= 2, \
            '%s missing from the push and/or pull_request triggers' % path


def test_index_makes_no_domain_assertion():
    """TOTA-79's own INDEX.md assertion, kept as a separate check rather than
    folded into the frontmatter sweep above: INDEX.md has no frontmatter, so
    the sweep cannot see it. It is a generated table that once carried a
    Domain column and a "Note on domains" paragraph for all 179 specs."""
    text = open(os.path.join(ROOT, 'INDEX.md'), encoding='utf-8').read()
    assert len(text) > 1000, 'INDEX.md looks truncated; this check would pass vacuously'
    assert not re.search(r'\|\s*Domain\s*\|', text), 'INDEX.md has a Domain column again'
    assert not re.search(r'\bmd\.dev\b|\.dev\b', text), 'INDEX.md names a .dev domain again'
    assert not re.search(r'note on domains', text, re.I), 'INDEX.md domains note is back'


def test_templates_are_in_the_validate_specs_workflow_triggers():
    """CD-8: a correct validator that never fires on a template edit is not a
    check. Guard the trigger paths, not just the validation step."""
    workflow = open(os.path.join(ROOT, '.github', 'workflows', 'validate-specs.yml'),
                    encoding='utf-8').read()
    assert workflow.count("- 'templates/**'") >= 2, 'templates/** missing from push and/or pull_request'
    assert 'tools/validate_corpus.py' in workflow


# --------------------------------------------------------------------------
# CD-9 / CD-10 — the lifecycle marker is machine-validated and documented once
# --------------------------------------------------------------------------

def test_every_spec_declares_a_lifecycle_status():
    assert len(files('specs')) == 179
    for path in files('specs'):
        assert frontmatter(path).get('status') in LIFECYCLE_STATUSES, path


def test_proposed_specs_are_exactly_the_five_promoted_in_v131():
    proposed = sorted(os.path.basename(p) for p in files('specs')
                      if frontmatter(p).get('status') == 'proposed')
    assert proposed == ['ATTESTATION.md', 'AUDITTRAIL.md', 'DELEGATION.md',
                        'INTENT.md', 'LEASTPRIVILEGE.md']


def test_proposed_specs_record_when_their_comment_window_opened():
    for path in files('specs'):
        data = frontmatter(path)
        if data.get('status') == 'proposed':
            assert re.match(r'^\d{4}-\d{2}-\d{2}$', str(data.get('proposed_on', ''))), path


def test_public_docs_agree_with_the_corpus_about_lifecycle_stage():
    """CD-9: README.md and SPEC_LIFECYCLE.md published different stability
    commitments for the same specs. They must now agree, and agree with the
    frontmatter."""
    statuses = [frontmatter(p).get('status') for p in files('specs')]
    draft = str(statuses.count('draft'))
    proposed = str(statuses.count('proposed'))
    for name in ('README.md', 'SPEC_LIFECYCLE.md'):
        text = open(os.path.join(ROOT, name), encoding='utf-8').read()
        assert not re.search(r'All 179 specs.{0,80}Draft', text, re.S), \
            '%s still claims all 179 specs are Draft' % name
        assert draft in text, '%s does not state the Draft count (%s)' % (name, draft)
        assert proposed in text, '%s does not state the Proposed count (%s)' % (name, proposed)


def test_lifecycle_status_enum_is_the_documented_one():
    schema = json.load(open(os.path.join(vc.SCHEMA_DIR, 'spec-document.schema.json'),
                            encoding='utf-8'))
    assert schema['properties']['status']['enum'] == list(LIFECYCLE_STATUSES)
    assert 'status' in schema['required']


def test_frontmatter_schema_does_not_claim_the_overloaded_status_field():
    """`status` means lifecycle stage on a spec and agent availability on a
    HIREME instance. Defining it in the shared schema would invalidate
    currently-valid adopter documents; see the CD-10 note in
    schemas/README.md."""
    schema = json.load(open(os.path.join(vc.SCHEMA_DIR, 'frontmatter.schema.json'),
                            encoding='utf-8'))
    assert 'status' not in schema['properties']
    hireme = vc.read_frontmatter(os.path.join(ROOT, 'templates', 'HIREME.template.md'))
    assert hireme['status'] not in LIFECYCLE_STATUSES


# --------------------------------------------------------------------------
# CD-11 / CD-12 — governance model is expressible and the top stage is reachable
# --------------------------------------------------------------------------

def test_lifecycle_stage_is_not_bound_to_a_version_range():
    """CD-11: stage headings encoded stage in the version number, which made
    'breaking fix to a Proposed spec' inexpressible."""
    text = open(os.path.join(ROOT, 'SPEC_LIFECYCLE.md'), encoding='utf-8').read()
    for heading in ('### Draft (v0.x.x)', '### Proposed (v0.5.0+)', '### Stable (v1.0.0+)'):
        assert heading not in text, heading
    assert re.search(r'###\s+Draft\s*$', text, re.M)
    assert re.search(r'###\s+Proposed\s*$', text, re.M)
    assert re.search(r'###\s+Stable\s*$', text, re.M)


def test_no_spec_was_promoted_by_this_change():
    """CD-11's fix must not move any spec up a stage as a side effect."""
    for path in files('specs'):
        data = frontmatter(path)
        assert data['status'] in ('draft', 'proposed'), path
        assert data['spec_version'] == '0.1.0', path


def test_stable_gate_is_computable():
    """CD-12: the Stable criterion 'passes Level 3' pointed at a check nothing
    executed. It must now return a number."""
    ready = vc.stable_gate(ROOT)
    assert isinstance(ready, int)
    assert ready > 0


def test_the_five_proposed_specs_have_level3_evidence():
    """Not a promotion — the repository-checkable part of the Stable gate."""
    results, _ = vc.validate(ROOT, {'examples'})
    failing = {os.path.basename(p) for p, _s, _n, e, _k in results if e}
    deviating = {os.path.basename(p) for p, _s, _n, _e, k in results if k}
    for name in ('AUDITTRAIL.md', 'DELEGATION.md', 'INTENT.md',
                 'LEASTPRIVILEGE.md', 'ATTESTATION.md'):
        instances = [p for p, _s, _n, _e, _k in results if os.path.basename(p) == name]
        assert instances, '%s has no example instance document' % name
        assert name not in failing
        assert name not in deviating, 'a known deviation is not Level-3 evidence'


def test_stable_gate_accepts_a_clean_example_instance(mini_corpus, capsys):
    """Control for the test below: without a deviation, the mini spec is ready."""
    root, write_document, _write_registry = mini_corpus
    write_document({'alpha': 'set'})
    assert vc.stable_gate(str(root)) == 1
    assert 'NOT LEVEL 3' not in capsys.readouterr().out


def test_stable_gate_treats_a_known_example_deviation_as_not_ready(mini_corpus, capsys):
    """The review finding: stable_gate() ignored the `known` list, so an example
    that does not validate could still contribute level3_ready=yes once its
    failure was registered. A registered deviation is an accepted failure, not
    conformance, and must not open a route to Stable."""
    root, write_document, write_registry = mini_corpus
    write_document(MISSING_BOTH)
    write_registry(MISSING_BOTH)

    results, stale = vc.validate(str(root), {'examples'})
    assert stale == [] and not any(e for _p, _s, _n, e, _k in results), \
        'the deviation is registered, so the run itself is green'

    assert vc.stable_gate(str(root)) == 0, 'a deviating instance is not Level-3 evidence'
    out = capsys.readouterr().out
    assert 'NOT LEVEL 3 specs/mini/MINI.md' in out
    assert 'examples/mini-bundle/MINI.md' in out
