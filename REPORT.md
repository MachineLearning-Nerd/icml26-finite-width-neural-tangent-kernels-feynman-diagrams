# Finite-width NTK audit report

## Result

All five claims are **VERIFIED under explicit finite contracts**:

1. finite reconstruction of the Section 4 graphical rules;
2. the five-diagram order-1/n topology certificate;
3. symbolic cancellation plus a five-million-network finite empirical contract;
4. a source-faithful four-width GeLU correction comparison;
5. finite width-200, depth-30 critical stability with low/high controls.

This is an audit result, not a claim that finite computation proves every
universal statement in the paper.

## Evidence summary

| Claim | Key measurement or certificate | Scope |
| --- | --- | --- |
| 1 | Unique signatures, both F partitions, recursion translation, and malformed-color rejection all pass | Rule reconstruction, not an all-orders formal proof |
| 2 | Exactly five diagrams: two quadratic and three quartic; independent checker and missing-vertex control pass | Topology and coefficient certificate |
| 3 | ReLU/LeakyReLU diagonal z-scores 0.773, 1.110, 0.324, 0.891 at widths 20/80; off-diagonal controls detect 1.34–8.30% shifts | 5,000,000 initializations per activation-width pair plus symbolic assumptions |
| 4 | Four-layer GeLU at widths 32/56/100/220; median residual ratio 0.1283; infinite-width substitution fails | Four representative source widths, 100,000 networks each |
| 5 | Critical slope 0.679499 ± 0.012189 versus 0.669128 predicted; z=0.851; R2=0.999900 | Width 200, depths 1–30, 1,000 initializations per regime |

The exact claim-to-code paths and controls are in
[CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md). The immutable raw values are in
[space/data/cumulative_run.json](space/data/cumulative_run.json).

## Historical evaluation status

The evaluator-visible Hugging Face artifact has a historical judged score of
**0/10** at revision
<code>beea5e8b4af3e149d85796bd4922b6d03339a6ac</code>. The release report's
projected 8–10/10 range and its best-supported 10/10 outcome are forecasts,
not new judge results. This repository does not rewrite the historical score.

## Limitations

- Claim 1 checks an executable finite rule table and representative translations,
  not every all-orders consequence.
- Claim 2 checks the published finite topology certificate, not every tensor
  derivation.
- Claim 3's theorem contract assumes a bias-free NTK-parameterized Gaussian MLP
  and separates symbolic evidence from finite sampling.
- Claim 4 uses an unbiased Hutchinson estimator and four representative source
  widths.
- Claim 5 is a finite empirical architecture experiment, not a universal
  asymptotic proof.
- No author review or endorsement is claimed.
