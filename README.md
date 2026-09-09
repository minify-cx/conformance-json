# Minify++ JSON Conformance

Independent JSON conformance evidence for Minify++. The harness pins JSONTestSuite, extracts an explicitly eligible corpus, minifies each case in bounded batches, and applies strict lossless JSON data-model comparison. Upstream sources are acquired on demand and are never committed.

```sh
make deps
make smoke test
make sync extract run
make dashboard
```

Use `python3 tools/conformance.py extract --limit 1000` for iteration. Result JSON records the exact upstream revision, extraction exclusions, minifier identity, raw non-pass evidence and timestamped history.

## Contract

The adapter selects only `y_*.json` parsing fixtures, rejects duplicate object names from the semantic denominator, and counts invalid (`n_`) and implementation-defined (`i_`) fixtures separately. Decimal-backed parsing prevents binary floating-point normalization from hiding number changes.

Statuses are `pass`, `semantic-difference` or `token-difference`, `parser-rejected`, `source-rejected`, and `minify-error`. Only transformed failures fail the run. Any confirmed product defect must be minimized into Minify++'s permanent suite before a corrected complete result is published.

## Evidence policy

A smoke run proves the harness is wired correctly, not corpus conformance. Public claims require a fresh complete extraction and run at the recorded revision. Eligibility totals and every exclusion category must be published alongside the pass count. The dashboard is generated from a completed immutable result; it is not live during execution.
