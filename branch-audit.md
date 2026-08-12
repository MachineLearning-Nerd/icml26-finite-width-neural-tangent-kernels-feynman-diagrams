# Branch and attribution audit

Repository target: `MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams`

Former repository name: `icml26-repro-SOlPHMdSY3-finite-width-neural-tangent-kernels-from-feynman-diagrams`

`main` is the cumulative publication surface. The seven former `orx/*` branch
tips are preserved as exact checkpoints under descriptive names; they are
independent experiment lineage refs, not claims that every checkpoint is an
ancestor of `main`.

| Clean branch | Former branch | Purpose |
| --- | --- | --- |
| `audit/five-diagram-baseline` | `orx/audited-five-diagram-baseline` | CPU-only five-diagram baseline and Claim 2 certificate. |
| `audit/symbolic-rules-scale-invariance` | `orx/symbolic-rules-and-scale-invariance-proofs` | Graphical rules, symbolic identities, and Claims 1–3 certificate. |
| `audit/paper-scale-critical-depth` | `orx/paper-scale-critical-depth-stability` | Width-200, depth-30 critical stability and Claim 5 controls. |
| `audit/gelu-finite-width-correction` | `orx/source-faithful-gelu-finite-width-correction` | Source-faithful Figure 2 GeLU correction and Claim 4 checker. |
| `audit/five-million-cancellation` | `orx/five-million-scale-invariant-cancellation` | Five-million-network diagonal cancellation and off-diagonal controls. |
| `release/cumulative-evidence` | `orx/evaluator-visible-cumulative-release` | Independent cumulative rerun and raw release evidence. |
| `release/publication-gates` | `orx/candidate-space-and-release-gates` | Blind traversal, visibility, hash, secret, image, and notebook gates. |

## Attribution policy

All reachable commits will be normalized to:

```text
MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>
```

The repository rename and old-branch deletion are publication steps, not changes
to the experiment contents. Before publication, the old and clean refs will be
compared by commit, and after publication the live GitHub branch list and commit
identity set will be checked.

## Publication checklist

- [x] README documents the paper, repository contents, claims, evidence paths, citation, and thank-you note.
- [x] Each former branch has one descriptive target name.
- [x] Existing reports and notebook navigation use the target repository name and clean branch names.
- [x] Seven former branch tips are present locally and ready for publication.
- [ ] Normalize reachable commit author and committer identities.
- [ ] Rename the GitHub repository.
- [ ] Push the clean branch refs and remove the former `orx/*` refs.
- [ ] Verify the default branch, branch count, README blob, stale refs, and live identity set through GitHub.
