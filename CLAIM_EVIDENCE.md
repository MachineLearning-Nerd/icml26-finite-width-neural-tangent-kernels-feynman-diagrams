# Claim-to-evidence ledger

## Reading this ledger

The status word **VERIFIED** means that the named executable contract, checker,
and intended negative control passed against the committed evidence. It does
not mean that finite computation proves a universal theorem. Universal
quantifiers, estimator substitutions, source-width coverage, and other
boundaries are stated explicitly below.

The canonical evaluator-visible evidence is under
<code>space/</code>. The root-level <code>reproduction/</code> programs are the
corresponding full-workspace implementations.

## Claims and production paths

| Claim | Paper target | Primary implementation | Independent check | Negative/control path | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Section 4 graphical rules generate the order-1/n D/F/A/B recursions | <code>reproduction/diagram_rules.py</code> and <code>reproduction/claim1_verifier.py</code> | Verifier checks unique external signatures, two F channel partitions, direct/propagated F terms, D/F/A/B coverage, and direct/recursive translations | Invalid unpaired color is rejected | VERIFIED: finite rule reconstruction |
| 2 | Section 5.1 has exactly five order-1/n diagrams for the two-line NTK mean recursion | <code>reproduction/claim2_verifier.py</code> | <code>reproduction/claim2_independent_checker.py</code> rebuilds IDs, derivative profile, vertex names, and coefficients | <code>reproduction/claim2_negative_control.py</code> removes the quartic F vertex and must exit nonzero | VERIFIED: five-diagram certificate |
| 3 | Positive-homogeneous, bias-free activations have no finite-width diagonal correction | <code>reproduction/claim3_verifier.py</code>, <code>claim3_paper_scale.py</code>, and the empirical checker | Symbolic identities plus <code>claim3_independent_checker.py</code> and exact-Jacobian/Hutchinson empirical checks | Symbolic GeLU scale-invariance mutation, injected-sign control, and injected two-percent diagonal correction must fail | VERIFIED: symbolic and finite empirical contract |
| 4 | Four-layer GeLU means above width 20 follow the first-order correction more closely than infinite width | <code>reproduction/claim4_gelu.py</code> | <code>reproduction/claim4_independent_checker.py</code> re-extracts immutable PDF curves and checks the source-width decoding | Infinite-width substitution is required to fail the first-order contract | VERIFIED: four representative source widths |
| 5 | At critical C_W=2, width-200 ReLU NTKs scale linearly through depth 30 while low/high C_W regimes decay/grow | <code>reproduction/claim5_stability.py</code> | <code>reproduction/claim5_independent_checker.py</code> checks the critical formula, slope, fit, and intervals | Low and high initialization regimes must show the intended exponential controls | VERIFIED: finite critical-depth contract |

## Decisive evidence

### Claim 1

The committed certificate is
<code>e6fa6bc262d4c3654ca9268e0204356dc3f8f07f7c3620e81aa2ba6394fcf889</code>.
The source anchors are S4.SS1, S4.E7, and S4.E11 in arXiv v4. Both direct and
propagated F constructions are present, and the invalid-color control rejects
the malformed signature.

### Claim 2

The committed certificate is
<code>3e60f600b5a623dbf3f5301bc1c59d848c12a4a95c1742ee26f34abf91ae7141</code>.
The five serialized IDs contain two quadratic and three quartic insertions with
the paper coefficients 1/2, 1/8, C_W/2, C_W, and 1. The missing-vertex control
observes four diagrams, verifier false, and exit code 1.

### Claim 3

The symbolic certificate is
<code>9cb51c72e4e39a0129a9f0ab6163d9c70acc7fac79981798b8f0e4af8e1b9153</code>.
The exact finite empirical contract uses the paper's four-layer, bias-free,
two-output architecture, C_W=2, widths 20 and 80, ReLU and LeakyReLU with
alpha=0.1, two Hutchinson probes, and exactly 5,000,000 initializations per
activation-width pair. Diagonal z-scores are 0.773, 1.110, 0.324, and 0.891;
off-diagonal control z-scores are 48.49, 43.62, 10.98, and 10.78.

### Claim 4

The finite contract uses exact GeLU, four layers, C_W=1.98305826, 100,000
networks at each of widths 32, 56, 100, and 220. The median residual ratio
reported by the source-curve comparison is 0.12828394677580282. The source
curves are immutable inputs; replacing them with the infinite-width curve is
the failing control.

### Claim 5

The finite contract uses width 200, depths 1 through 30, and 1,000
initializations per low, critical, and high regime. The critical predicted
slope is 0.6691276431083679 and the observed through-origin slope is
0.6794990439584496 with standard error 0.01218850284716703 and z=0.8509167.
The critical regression has R2=0.9998995277420369; all 30 points are within
the 99% intervals. Low and high log slopes are -2.02514775 and +0.74684715.

## Raw evidence and boundary

- Cumulative run: <code>space/data/cumulative_run.json</code>, passed at Git SHA
  <code>4236e14fff388b849196a0f53b77c39d16b88209</code>.
- Independent release rerun:
  <code>space/data/release_rerun_summary.json</code>, passed at Git SHA
  <code>0955d05f3d38f60adc356c3ea8fcf4fce3adb2b2</code>.
- Reader-facing claim pages: <code>space/pages/claim-1.md</code> through
  <code>space/pages/claim-5.md</code>.
- Full technical narrative: <code>reports/reproduction/report.md</code>.

This evidence supports the finite contracts above. It does not by itself
establish every all-orders theorem, every plotted source width, or author
endorsement.
