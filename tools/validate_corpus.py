#!/usr/bin/env python3
"""Validate the agent-md-specs corpus frontmatter against its JSON Schemas.

This is the checked-in implementation of the schema validation that CI runs.
It exists as a script rather than inline workflow YAML so that contributors
can reproduce exactly what CI does:

    pip install jsonschema pyyaml
    python3 tools/validate_corpus.py

Three document classes are validated, because the corpus contains three
different kinds of file and they do not share one contract:

  specs/**/*.md          Specification documents. Validated against
                         schemas/spec-document.schema.json — the shared
                         frontmatter fields plus the lifecycle `status`
                         marker defined in SPEC_LIFECYCLE.md — and, where
                         one exists, additionally against the spec's own
                         per-spec schema.

  templates/*.template.md
                         Starter files an adopter copies. Validated against
                         schemas/frontmatter.schema.json. Each template
                         declares the identity of the spec it instantiates
                         and carries `[REPLACE THIS — ...]` placeholders in
                         every other field, so it cannot satisfy per-spec
                         value constraints by construction.

  examples/**/*.md       Instance documents — what a deployed agent actually
                         ships. Validated against the per-spec schema bound
                         by filename (WHOAMI.md -> schemas/whoami.schema.json),
                         falling back to frontmatter.schema.json when no
                         per-spec schema exists. This is Level 3 conformance
                         as defined in schemas/README.md.

All `$ref`s resolve against the local schemas/ directory. The registry is
built with a retriever that refuses every unknown URI, so a schema that
gained a remote `$ref` would fail the run instead of silently reaching the
network from CI.

Known deviations are declared in schemas/known-deviations.json. A declared
deviation is reported but does not fail the run; a declared deviation that
no longer reproduces fails the run, so the file cannot rot into a blanket
suppression list. Each entry is bound to a deterministic signature of the
error it names, so a materially different failure at the same location is
reported as an unregistered failure instead of inheriting the entry's
excuse. A document carrying a live known deviation is counted in its own
`known` column and is never reported as passed.
"""

from __future__ import annotations

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import sys

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_DIR = os.path.join(REPO_ROOT, 'schemas')
SCHEMA_BASE_URI = 'https://totalmarkdown.ai/schemas/'
DEVIATIONS_FILE = os.path.join(SCHEMA_DIR, 'known-deviations.json')

# Schemas that describe a document class rather than a single spec, and so
# must never be reached by filename binding.
NON_SPEC_SCHEMAS = {'frontmatter.schema.json', 'spec-document.schema.json'}


# --------------------------------------------------------------------------
# frontmatter
# --------------------------------------------------------------------------

class FrontmatterError(Exception):
    pass


def read_frontmatter(path):
    """Return the parsed YAML frontmatter of a Markdown file.

    The frontmatter is the block delimited by a `---` line at line 1 and the
    next `---` line on its own. Raises FrontmatterError when the file has no
    well-formed block, so a missing or malformed block is a validation
    failure rather than a silently skipped file.
    """
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    if not lines or lines[0].strip() != '---':
        raise FrontmatterError('no YAML frontmatter block at line 1')
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            try:
                data = yaml.safe_load('\n'.join(lines[1:i]))
            except yaml.YAMLError as exc:
                raise FrontmatterError('unparseable YAML frontmatter: %s' % exc)
            if data is None:
                data = {}
            if not isinstance(data, dict):
                raise FrontmatterError('frontmatter is not a mapping')
            return jsonify(data)
    raise FrontmatterError('unterminated YAML frontmatter block')


def jsonify(value):
    """Normalise YAML scalars into their JSON equivalents.

    PyYAML resolves unquoted ISO dates to datetime objects. JSON Schema has
    no date type — `format: date` is defined over strings — so dates are
    serialised back to ISO-8601 before validation.
    """
    if isinstance(value, dict):
        return {str(k): jsonify(v) for k, v in value.items()}
    if isinstance(value, list):
        return [jsonify(v) for v in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    return value


# --------------------------------------------------------------------------
# schema registry — local resolution only
# --------------------------------------------------------------------------

def build_registry():
    def refuse(uri):
        raise NoSuchResource(ref=uri)

    registry = Registry(retrieve=refuse)
    for path in sorted(glob.glob(os.path.join(SCHEMA_DIR, '*.schema.json'))):
        with open(path, encoding='utf-8') as fh:
            contents = json.load(fh)
        name = os.path.basename(path)
        resource = Resource.from_contents(contents, default_specification=DRAFT202012)
        # Bind every spelling a $ref inside schemas/ can produce: the bare
        # filename, the declared $id, and the $id-relative resolution.
        registry = registry.with_resource(uri=name, resource=resource)
        registry = registry.with_resource(uri=SCHEMA_BASE_URI + name, resource=resource)
        if '$id' in contents:
            registry = registry.with_resource(uri=contents['$id'], resource=resource)
    return registry


def load_schema(name, registry):
    with open(os.path.join(SCHEMA_DIR, name), encoding='utf-8') as fh:
        return Draft202012Validator(json.load(fh), registry=registry)


# --------------------------------------------------------------------------
# document classification
# --------------------------------------------------------------------------

def per_spec_schema_name(md_path):
    """schemas/<basename>.schema.json for MEMORY.md -> memory.schema.json."""
    base = os.path.basename(md_path)
    if not base.endswith('.md'):
        return None
    name = base[: -len('.md')].lower() + '.schema.json'
    if name in NON_SPEC_SCHEMAS:
        return None
    if os.path.exists(os.path.join(SCHEMA_DIR, name)):
        return name
    return None


def collect_documents(root):
    """Yield (path, surface, schema_name) for every corpus document.

    A document appears once per schema it is bound to. Specification
    documents are bound to the spec-document contract and, where the spec
    publishes one, to its own per-spec schema as well: that second binding
    is what makes CD-5b's per-spec schemas executed rather than decorative.
    """
    def rel(p):
        return os.path.relpath(p, root).replace(os.sep, '/')

    for path in sorted(glob.glob(os.path.join(root, 'specs', '**', '*.md'), recursive=True)):
        if os.path.basename(path) == 'README.md':
            continue
        yield rel(path), 'specs', 'spec-document.schema.json'
        per_spec = per_spec_schema_name(path)
        if per_spec:
            yield rel(path), 'specs', per_spec

    for path in sorted(glob.glob(os.path.join(root, 'templates', '*.md'))):
        if os.path.basename(path) == 'README.md':
            continue
        yield rel(path), 'templates', 'frontmatter.schema.json'

    for path in sorted(glob.glob(os.path.join(root, 'examples', '**', '*.md'), recursive=True)):
        if os.path.basename(path) == 'README.md':
            continue
        yield rel(path), 'examples', per_spec_schema_name(path) or 'frontmatter.schema.json'


# --------------------------------------------------------------------------
# known deviations
# --------------------------------------------------------------------------

DEVIATION_FIELDS = ('path', 'schema', 'json_path', 'keyword', 'error_signature',
                    'surface', 'defect', 'track', 'reason')

SIGNATURE_RE = re.compile(r'^[0-9a-f]{64}$')


class DeviationRegistryError(Exception):
    pass


def load_deviations():
    if not os.path.exists(DEVIATIONS_FILE):
        return []
    with open(DEVIATIONS_FILE, encoding='utf-8') as fh:
        deviations = json.load(fh).get('deviations', [])
    for i, entry in enumerate(deviations):
        missing = [field for field in DEVIATION_FIELDS if field not in entry]
        if missing:
            raise DeviationRegistryError(
                'deviations[%d] (%s) is missing %s' % (i, entry.get('path', '?'), ', '.join(missing)))
        if not SIGNATURE_RE.match(str(entry['error_signature'])):
            raise DeviationRegistryError(
                'deviations[%d] (%s) error_signature must be 64 lowercase hex characters, got %r'
                % (i, entry['path'], entry['error_signature']))
    return deviations


def canonical(value):
    """Stable JSON encoding, used only as hash input."""
    return json.dumps(value, sort_keys=True, separators=(',', ':'), default=str)


def error_shape(error):
    """The structural identity of a validation error.

    Derived from where in the schema the failure happened — the absolute
    schema path and the failing keyword's schema value — plus, recursively,
    the shape of every sub-error a composite keyword collected. An `anyOf`
    failure therefore carries the shape of each branch's own failure.

    Deliberately excludes the instance data and the rendered message. Those
    change whenever an unrelated frontmatter field is edited, and a signature
    that churns on unrelated edits is one nobody maintains. What they buy is
    covered instead by the sub-error structure: a materially different failure
    at the same location fails differently *inside* the schema, and that shows
    up here.
    """
    return {
        'json_path': error.json_path,
        'keyword': error.validator,
        'schema_path': '/'.join(str(part) for part in error.absolute_schema_path),
        'keyword_value': error.validator_value,
        'context': sorted((error_shape(sub) for sub in (error.context or ())), key=canonical),
    }


def error_signature(error):
    """SHA-256 over error_shape() — what a registry entry is bound to."""
    return hashlib.sha256(canonical(error_shape(error)).encode('utf-8')).hexdigest()


def deviation_targets(entry, path, schema_name, error):
    """Whether the entry was written about this document, schema and location.

    Coarse on purpose: this is the coordinate set a registry entry is indexed
    by, and it is *not* sufficient to excuse an error. Used to tell a genuinely
    unregistered failure apart from one that has changed shape underneath an
    existing entry, so the latter gets a diagnostic instead of a bare FAIL.
    """
    return (
        entry['path'] == path
        and entry['schema'] == schema_name
        and entry['json_path'] == error.json_path
        and entry['keyword'] == error.validator
    )


def deviation_matches(entry, path, schema_name, error):
    """Whether the entry excuses this exact error.

    Location alone is not enough — a different error at the same path, schema,
    JSON path and keyword must not be able to masquerade as the frozen
    deviation. The signature is what makes the registry a statement about one
    named failure rather than a suppression rule for a location.
    """
    return (deviation_targets(entry, path, schema_name, error)
            and entry['error_signature'] == error_signature(error))


# --------------------------------------------------------------------------
# validation
# --------------------------------------------------------------------------

def validate(root, surfaces):
    registry = build_registry()
    validators = {}
    deviations = load_deviations()
    matched = [False] * len(deviations)

    results = []
    for path, surface, schema_name in collect_documents(root):
        if surface not in surfaces:
            continue
        if schema_name not in validators:
            validators[schema_name] = load_schema(schema_name, registry)
        try:
            data = read_frontmatter(os.path.join(root, path))
        except FrontmatterError as exc:
            results.append((path, surface, schema_name, [str(exc)], []))
            continue
        errors, known = [], []
        for error in sorted(validators[schema_name].iter_errors(data), key=lambda e: e.json_path):
            hit = None
            substituted = None
            for i, entry in enumerate(deviations):
                if not deviation_targets(entry, path, schema_name, error):
                    continue
                if deviation_matches(entry, path, schema_name, error):
                    matched[i] = True
                    hit = entry
                    break
                substituted = entry
            text = '%s: %s' % (error.json_path, error.message)
            if hit:
                known.append('%s  [%s / Track %s] %s' % (text, hit['defect'], hit['track'], hit['reason']))
            elif substituted:
                errors.append(
                    '%s\n      the registered %s deviation at this location does not describe this error: '
                    'expected signature %s, observed %s. The failure has materially changed; re-review it '
                    'and update schemas/known-deviations.json deliberately.'
                    % (text, substituted['defect'], substituted['error_signature'], error_signature(error)))
            else:
                errors.append(text)
        results.append((path, surface, schema_name, errors, known))

    stale = [deviations[i] for i, hit in enumerate(matched)
             if not hit and deviations[i].get('surface', 'specs') in surfaces]
    return results, stale


def blank_counts():
    return {'files': set(), 'checks': 0, 'failed': set(), 'errors': 0,
            'deviating': set(), 'known': 0, 'known_checks': set()}


def report(results, stale, surfaces):
    """Print the run and return whether it passed.

    `passed` counts only documents that are actually clean. A document with a
    live known deviation is a document that does not validate: it is counted in
    `known`, never in `passed`. It still does not fail the run — that is the
    admitted contract for a named, defect-attributed deviation — but the
    summary must not describe it as conformant.
    """
    errors = known = 0
    failed_files = set()
    deviating_files = set()
    by_surface = {}
    for path, surface, schema_name, errs, kn in results:
        counts = by_surface.setdefault(surface, blank_counts())
        counts['files'].add(path)
        counts['checks'] += 1
        if kn:
            counts['known'] += len(kn)
            counts['deviating'].add(path)
            counts['known_checks'].add((path, schema_name))
            deviating_files.add(path)
            known += len(kn)
        for line in kn:
            print('KNOWN DEVIATION %s [%s]\n      %s' % (path, schema_name, line))
        if errs:
            counts['failed'].add(path)
            counts['errors'] += len(errs)
            failed_files.add(path)
            errors += len(errs)
            print('FAIL %s [%s]' % (path, schema_name))
            for line in errs:
                print('      %s' % line)

    for entry in stale:
        print('STALE DEVIATION %s [%s] %s no longer reproduces — remove it from '
              'schemas/known-deviations.json' % (entry['path'], entry['schema'], entry['json_path']))

    print('')
    print('%-12s %7s %7s %7s %7s %7s %7s' % ('surface', 'files', 'checks', 'passed',
                                             'known', 'failed', 'errors'))
    tf = tc = tk = 0
    for surface in ('specs', 'templates', 'examples'):
        if surface not in surfaces:
            continue
        c = by_surface.get(surface, blank_counts())
        tf += len(c['files'])
        tc += c['checks']
        tk += len(c['known_checks'])
        print('%-12s %7d %7d %7d %7d %7d %7d' % (
            surface, len(c['files']), c['checks'],
            len(c['files'] - c['failed'] - c['deviating']),
            len(c['deviating']), len(c['failed']), c['errors']))
    print('%-12s %7d %7d %7d %7d %7d %7d' % (
        'TOTAL', tf, tc, tf - len(failed_files | deviating_files),
        len(deviating_files), len(failed_files), errors))
    print('')
    print('passed = documents with no validation error and no known deviation;')
    print('         a known deviation is a live failure, not a pass.')
    print('known deviations reported: %d error(s) over %d check(s) in %d file(s) '
          '(see schemas/known-deviations.json)' % (known, tk, len(deviating_files)))
    print('stale deviation entries:   %d' % len(stale))
    return not failed_files and not stale


# --------------------------------------------------------------------------
# CD-12 — Level 3 / Stable-gate readiness
# --------------------------------------------------------------------------

def stable_gate(root):
    """Report, per spec, whether the SPEC_LIFECYCLE.md Stable criteria that
    this repository can actually check are met:

      - a per-spec JSON Schema exists;
      - at least one example bundle ships an instance document for the spec;
      - every such instance document passes that schema (Level 3), with no
        known deviation registered against any of them.

    A registered deviation is an accepted *failure*, not conformance. An
    instance document carrying one has not passed Level 3, so it cannot
    contribute Level-3 evidence for promoting its spec to Stable — otherwise
    registering a deviation would become a route to Stable for a spec whose
    own example does not validate.

    The remaining Stable criteria (30 days without unresolved issues, two
    independent implementations) are not repository-checkable and are not
    reported here.
    """
    registry = build_registry()
    results, _ = validate(root, {'examples'})
    failures = {}
    deviating = {}
    instances = {}
    for path, _surface, schema_name, errs, known in results:
        base = os.path.basename(path)
        instances.setdefault(base, []).append(path)
        if errs:
            failures.setdefault(base, []).extend(errs)
        if known:
            deviating.setdefault(base, set()).add(path)

    rows = []
    for spec_path in sorted(glob.glob(os.path.join(root, 'specs', '**', '*.md'), recursive=True)):
        base = os.path.basename(spec_path)
        if base == 'README.md':
            continue
        schema = per_spec_schema_name(spec_path)
        seen = instances.get(base, [])
        deviations = deviating.get(base, set())
        ready = bool(schema) and bool(seen) and base not in failures and not deviations
        rows.append((os.path.relpath(spec_path, root).replace(os.sep, '/'),
                     bool(schema), len(seen), len(deviations), ready))

    print('%-46s %-8s %-10s %-6s %s' % ('spec', 'schema', 'instances', 'known', 'level3_ready'))
    for path, has_schema, n, n_known, ready in rows:
        print('%-46s %-8s %-10d %-6d %s' % (path, 'yes' if has_schema else 'no', n, n_known,
                                            'yes' if ready else 'no'))
    blocked = [(path, sorted(deviating[os.path.basename(path)]))
               for path, has_schema, n, n_known, ready in rows if n_known and has_schema and n]
    print('')
    for path, docs in blocked:
        print('NOT LEVEL 3 %s — instance document(s) carry a known deviation: %s'
              % (path, ', '.join(docs)))
    if blocked:
        print('')
    ready_n = sum(1 for r in rows if r[4])
    # The workflow step reports the tail of this output, so the headline
    # numbers are the last lines printed.
    print('Level 3 ready (schema + >=1 example instance + all instances pass, '
          'no known deviation): %d / %d' % (ready_n, len(rows)))
    if blocked:
        print('Not ready because an instance document carries a known deviation: %d spec(s)'
              % len(blocked))
    return ready_n


def print_signatures(root, surfaces):
    """Print the error signature of every current failure.

    A registry entry has to name an exact signature, so there must be a way to
    read one off a real run. This prints them and nothing else; registering a
    deviation still means editing schemas/known-deviations.json by hand with an
    owning defect id and a justification.
    """
    registry = build_registry()
    validators = {}
    rows = 0
    for path, surface, schema_name in collect_documents(root):
        if surface not in surfaces:
            continue
        validators.setdefault(schema_name, load_schema(schema_name, registry))
        try:
            data = read_frontmatter(os.path.join(root, path))
        except FrontmatterError:
            continue
        for error in sorted(validators[schema_name].iter_errors(data), key=lambda e: e.json_path):
            if not rows:
                print('%-64s  %s' % ('error_signature', 'path [schema] json_path keyword'))
            print('%-64s  %s [%s] %s %s' % (error_signature(error), path, schema_name,
                                            error.json_path, error.validator))
            rows += 1
    if not rows:
        print('no failing check to sign')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--root', default=REPO_ROOT,
                        help='repository root to validate (default: this checkout)')
    parser.add_argument('--surface', action='append', choices=['specs', 'templates', 'examples'],
                        help='limit validation to one surface (repeatable; default: all)')
    parser.add_argument('--stable-gate', action='store_true',
                        help='report per-spec Level 3 / Stable-gate readiness instead of validating')
    parser.add_argument('--signatures', action='store_true',
                        help='print the error signature of every current failure, for '
                             'registering a deviation in schemas/known-deviations.json')
    args = parser.parse_args(argv)

    surfaces = set(args.surface) if args.surface else {'specs', 'templates', 'examples'}

    try:
        if args.stable_gate:
            stable_gate(args.root)
            return 0
        if args.signatures:
            print_signatures(args.root, surfaces)
            return 0
        results, stale = validate(args.root, surfaces)
    except DeviationRegistryError as exc:
        print('schemas/known-deviations.json is invalid: %s' % exc, file=sys.stderr)
        return 2
    return 0 if report(results, stale, surfaces) else 1


if __name__ == '__main__':
    sys.exit(main())
