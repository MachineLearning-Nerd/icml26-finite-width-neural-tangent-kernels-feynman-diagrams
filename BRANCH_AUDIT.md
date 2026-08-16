# Branch and attribution audit

## Repository identity

- Current repository:
  <https://github.com/MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams>
- Former repository:
  <code>icml26-repro-SOlPHMdSY3-finite-width-neural-tangent-kernels-from-feynman-diagrams</code>
- Default branch: <code>main</code>
- Expected remote branches: exactly eight
- Former prefix: <code>orx/</code>; no former-prefixed branch is part of the
  publication set

The pre-dossier main checkpoint was
<code>a979bec40f514449150a117dc67f345349e154f5</code>. A recovery bundle made
before dossier edits has SHA-256
<code>c1d072b3ebd4c70e12d87d39103c4524df3f2a2d0df72f1c288e9e74f3aea141</code>
and contains the pre-dossier refs.

## Final branch contract

The seven non-main branches preserve exact experiment-lineage tips. They are
independent lineage references; their existence does not assert that every tip
is an ancestor of <code>main</code>.

| Clean branch | Former branch | Tip before dossier | Purpose |
| --- | --- | --- | --- |
| <code>audit/five-diagram-baseline</code> | <code>orx/audited-five-diagram-baseline</code> | <code>b67e545b132ece6edf16be7e1d9a224a5ea3fda8</code> | CPU-only five-diagram baseline and Claim 2 certificate |
| <code>audit/five-million-cancellation</code> | <code>orx/five-million-scale-invariant-cancellation</code> | <code>4fc0ba6a754ab4d55e9cb55ee52aa6e4ebfa5d89</code> | Five-million-network diagonal cancellation and off-diagonal controls |
| <code>audit/gelu-finite-width-correction</code> | <code>orx/source-faithful-gelu-finite-width-correction</code> | <code>fdf55ddf82863f4e155e5b7e40cd3467b476b369</code> | Source-faithful four-layer GeLU correction and Claim 4 checker |
| <code>audit/paper-scale-critical-depth</code> | <code>orx/paper-scale-critical-depth-stability</code> | <code>3e3f2ce0c531193fc39198e7aeee2e10c53772df</code> | Width-200, depth-30 critical stability and Claim 5 controls |
| <code>audit/symbolic-rules-scale-invariance</code> | <code>orx/symbolic-rules-and-scale-invariance-proofs</code> | <code>306b269a61a5878058a9ea5b8305a37d7c823cd6</code> | Graphical rules, symbolic identities, and Claims 1–3 certificate |
| <code>release/cumulative-evidence</code> | <code>orx/evaluator-visible-cumulative-release</code> | <code>2c723c96c6d3f5c575ac4f5bfb393c13a7c6ff7f</code> | Independent cumulative rerun and raw release evidence |
| <code>release/publication-gates</code> | <code>orx/candidate-space-and-release-gates</code> | <code>0261ba08378ca0dd1805f4170ed3117706a626b2</code> | Blind traversal, visibility, hash, secret, image, and notebook gates |
| <code>main</code> | former cumulative surface | <code>a979bec40f514449150a117dc67f345349e154f5</code> | Cumulative publication surface; dossier commits extend this branch |

## Attribution contract

Every reachable commit must use:

<code>MachineLearning-Nerd &lt;37579156+MachineLearning-Nerd@users.noreply.github.com&gt;</code>

Commit messages must not contain a <code>Co-authored-by:</code> trailer. The
repository verifier checks both author and committer identities across all
reachable refs.

## Verification contract

The publication verifier checks:

1. the canonical GitHub origin and main default branch;
2. the exact eight remote branch names and absence of <code>orx/</code> or
   <code>refs/original</code>;
3. the reachable commit count and canonical author/committer identities;
4. the dossier files, machine-readable claim statuses, and evidence hashes;
5. the raw cumulative run, controls, sample counts, and finite scope fields;
6. the existing evaluator-visible release gate.

Run it with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~
