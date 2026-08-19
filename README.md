# Finite-Width Neural Tangent Kernels from Feynman Diagrams

Independent claim-by-claim reproduction and audit for:

> Max Guillen, Philipp Misof, and Jan E. Gerken, “Finite-Width Neural Tangent Kernels from Feynman Diagrams.”

Paper: [arXiv:2508.11522](https://arxiv.org/abs/2508.11522) · [version 4](https://arxiv.org/abs/2508.11522v4) · published at ICML 2026.

This repository is an independent reproduction workspace, not an author-maintained
implementation. It contains executable verifiers, independent checkers, negative
controls, raw release data, reports, and the evaluator-visible `space/` surface.

## Current status

All five claims are **verified under explicit finite contracts**. “Verified” means
that the stated executable contract, checker, and control passed; it does not turn
finite sampling into a proof of a universal theorem.

| Claim | Paper target | Reproduction result | Scope boundary |
| --- | --- | --- | --- |
| 1 | Section 4 graphical rules determine the order-`1/n` `D/F/A/B` recursions | **VERIFIED** by finite rule/signature reconstruction and an invalid-color control | Does not machine-check every all-orders statement |
| 2 | Exactly five order-`1/n` diagrams contribute to the two-line NTK mean recursion | **VERIFIED**: two quadratic plus three quartic IDs, coefficients, independent sum, and missing-vertex control | Verifies the published topology certificate, not every tensor derivation |
| 3 | Positive-homogeneous, bias-free activations have no finite-width diagonal correction | **VERIFIED** by symbolic cancellation plus a five-million-network ReLU/LeakyReLU experiment | Symbolic assumptions and finite empirical corroboration are reported separately |
| 4 | v4 Figure 2 four-layer GeLU means follow the first-order correction above width 20 | **VERIFIED** at widths 32, 56, 100, and 220 with 100,000 samples per width | Four representative plotted widths, not every source marker |
| 5 | Width-200 ReLU critical `C_W=2` behavior is linear while low/high controls decay/grow | **VERIFIED** at depths 1–30 with 1,000 initializations per regime | Finite empirical architecture claim, not a universal theorem |

The strongest result is Claim 3: for widths 20 and 80, all diagonal shifts were
within a precommitted 1% equivalence margin, while off-diagonal controls shifted
by 1.34–8.30%. The evaluator-visible artifact was published to the
[DineshAI/SOlPHMdSY3 Hugging Face Space](https://huggingface.co/spaces/DineshAI/SOlPHMdSY3/tree/beea5e8b4af3e149d85796bd4922b6d03339a6ac)
at immutable revision `beea5e8b4af3e149d85796bd4922b6d03339a6ac`.

## Audit dossier

The repository-level audit record is split into small, reviewable documents:

- [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) maps every paper claim to its
  implementation, checker, negative control, decisive output, and scope
  boundary.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the paper identity, source
  anchors, immutable source hashes, and repository rename.
- [ENVIRONMENT.md](ENVIRONMENT.md) records the locked command, accepted runs,
  resource contract, estimator substitutions, and rerun policy.
- [REPORT.md](REPORT.md) gives the concise result, historical score, forecast
  boundary, and limitations.
- [BRANCH_AUDIT.md](BRANCH_AUDIT.md) records the final branch topology,
  former-to-clean names, exact tips, and attribution policy.
- [claims.json](claims.json) is the machine-readable claim status ledger.
- [reproduction_verdicts.json](reproduction_verdicts.json) records each claim's
  status, production path, evidence, and scope boundary in machine-readable form.
- [CITATION.cff](CITATION.cff) and [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md)
  provide citation metadata and the thank-you note to the paper authors.
- [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) hashes the dossier and
  immutable evidence inputs.

`publication_allowed` is `false` for a complete universal-paper reproduction or
score. The five claims are verified only under the finite contracts recorded
above; no author endorsement or current score is claimed.

The canonical evaluator-visible evidence is under
[space/](space/): its claim pages, raw JSON, source archive manifest, and
release surface are the reader-facing record. The root [pages/](pages/) notes
are earlier source-contract notes retained for provenance and are not silently
treated as a replacement for the verified <code>space/</code> pages.

Run the repository-level final check with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~

## How each claim is produced

Every full run uses the same locked entrypoint:

```bash
uv sync --frozen --all-extras && uv run --frozen python -m reproduction.run_all
```

| Claim | Production path | Independent evidence and control |
| --- | --- | --- |
| 1 | `reproduction/diagram_rules.py` enumerates admissible signatures; `reproduction/claim1_verifier.py` reconstructs the direct/propagated `F` terms and `D/F/A/B` coverage | Independent checks are returned by the verifier; invalid unpaired color must be rejected |
| 2 | `reproduction/claim2_verifier.py` consumes the finite rule enumerator and returns the five diagram IDs and coefficients | `claim2_independent_checker.py` rebuilds the algebraic sum; `claim2_negative_control.py` removes a required vertex and must fail |
| 3 | `claim3_verifier.py` proves the homogeneity identities and symbolic cancellation; `claim3_paper_scale.py` samples the source-scale architecture | Symbolic checker, sign-injection control, exact-Jacobian empirical checker, and 2% injected-correction control |
| 4 | `claim4_gelu.py` compares fresh four-layer GeLU samples with immutable PDF-extracted first-order and infinite-width curves | `claim4_independent_checker.py` re-extracts the source curve; the infinite-width substitution is the failing control |
| 5 | `claim5_stability.py` measures width-200 depth 1–30 at low, critical, and high `C_W` | `claim5_independent_checker.py` reconstructs the critical formula; low/high initialization regimes are required controls |

The canonical reader-facing evidence is in
[`space/pages/index.md`](space/pages/index.md), the five claim pages, and
[`space/data/cumulative_run.json`](space/data/cumulative_run.json). The technical
summary is [`reports/reproduction/report.md`](reports/reproduction/report.md),
and the final release audit is
[`reports/reproduction/release_report.md`](reports/reproduction/release_report.md).

## Branch map and experiment provenance

`main` is the cumulative publication surface. The former `orx/*` names are
recorded for provenance; each exact checkpoint is published below under a
descriptive `audit/*` or `release/*` name.

| Clean branch | Former branch | What it does |
| --- | --- | --- |
| [`audit/five-diagram-baseline`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/audit/five-diagram-baseline) | `orx/audited-five-diagram-baseline` | CPU-only five-diagram baseline; Claim 2 evidence |
| [`audit/symbolic-rules-scale-invariance`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/audit/symbolic-rules-scale-invariance) | `orx/symbolic-rules-and-scale-invariance-proofs` | Rules, symbolic identities, and first cancellation certificate; Claims 1–3 |
| [`audit/paper-scale-critical-depth`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/audit/paper-scale-critical-depth) | `orx/paper-scale-critical-depth-stability` | Width-200, depth-30 critical stability; Claim 5 |
| [`audit/gelu-finite-width-correction`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/audit/gelu-finite-width-correction) | `orx/source-faithful-gelu-finite-width-correction` | Source-faithful four-layer GeLU correction; Claim 4 |
| [`audit/five-million-cancellation`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/audit/five-million-cancellation) | `orx/five-million-scale-invariant-cancellation` | Five-million-network ReLU/LeakyReLU diagonal cancellation; Claim 3 |
| [`release/cumulative-evidence`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/release/cumulative-evidence) | `orx/evaluator-visible-cumulative-release` | Independent cumulative rerun and release data |
| [`release/publication-gates`](https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams/tree/release/publication-gates) | `orx/candidate-space-and-release-gates` | Blind traversal, manifest, hash, visibility, secret, image, and notebook gates |

The exact command, commit, runtime, allocation, and result for each experiment
remain in the reports and raw JSON. Historical checkpoints are preserved as branch
refs; they are not silently rewritten into the cumulative `main` narrative.

## Repository map

- `reproduction/` — executable claim verifiers, independent checkers, controls, and the cumulative runner.
- `space/` — text-only evaluator surface, claim pages, raw JSON, figures, and logbook.
- `reports/reproduction/` — illustrated technical report and release report.
- `notebooks/finite_width_ntk_reproduction.py` — self-contained marimo reading/tutorial notebook.
- `pages/` — earlier source-contract and experiment notes retained for provenance.
- `release/space_upload_allowlist.json` — exact text/figure publication allowlist.

## Environment and limitations

Scientific runs used Hugging Face `cpu-upgrade`, an actual 8-CPU cgroup quota, a
32 GB RAM contract, and no GPU. The five-million experiment took 5,225.662 seconds;
the independent release rerun took 5,363.686 seconds. The locked `uv.lock` is the
environment record. Claim 3 combines symbolic evidence with finite sampling;
Claim 4 uses representative widths; and none of the finite experiments alone
proves the paper’s universal quantifiers.

## Citation

```bibtex
@article{guillen2026finitewidth,
  title         = {Finite-Width Neural Tangent Kernels from Feynman Diagrams},
  author        = {Guillen, Max and Misof, Philipp and Gerken, Jan E.},
  journal       = {arXiv preprint arXiv:2508.11522},
  year          = {2026},
  eprint        = {2508.11522},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  doi           = {10.48550/arXiv.2508.11522}
}
```

Please cite the paper using the authors’ preferred venue record when available;
the stable arXiv record is [arXiv:2508.11522v4](https://arxiv.org/abs/2508.11522v4).

## Thank you

Thank you to Max Guillen, Philipp Misof, and Jan E. Gerken for developing and
publishing a technically rich framework that makes finite-width NTK corrections
auditable. The paper’s explicit diagrammatic rules, source equations, and clear
finite experiments made an independent claim-by-claim reproduction possible.

This repository is offered as a respectful, transparent companion audit: it aims
to make the assumptions, evidence paths, controls, and remaining limitations easy
for readers to inspect.

## Attribution

All approved repository commits are attributed to:

```text
MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>
```
