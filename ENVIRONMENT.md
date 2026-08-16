# Environment and reproduction record

## Fixed entrypoint

The committed scientific entrypoint is:

~~~bash
uv sync --frozen --all-extras && uv run --frozen python -m reproduction.run_all
~~~

The lockfile is <code>uv.lock</code>. The release gate is
<code>reproduction/release_gate.py</code>; it checks the evaluator-visible
surface, historical archive, allowlist hashes, links, secrets, SVGs, and the
marimo notebook without launching another scientific run.

## Accepted runs

| Run | Git SHA | Backend and allocation | Scientific runtime | Result |
| --- | --- | --- | ---: | --- |
| Cumulative evidence | <code>4236e14fff388b849196a0f53b77c39d16b88209</code> | Hugging Face cpu-upgrade; 8-CPU cgroup quota; 32 GB; no GPU | 5225.6622065010015 s | Claims 1–5 passed |
| Independent release rerun | <code>0955d05f3d38f60adc356c3ea8fcf4fce3adb2b2</code> | Hugging Face cpu-upgrade; 8 CPUs; 32 GB; no GPU | 5363.6862576100975 s; scheduler 3h02m | Passed; maximum combined-SE z for Claims 3–5 was 0.0 |

The cumulative JSON records an actual OS affinity of 64 CPUs but a cgroup quota
of 8 CPUs. The declared resource contract is therefore the quota, not the host
affinity count.

## Reproduction policy

The dossier commit documents already-accepted runs and does not silently launch
the five-million-network workload again. A fresh scientific run should be
identified by its own Git SHA, resource contract, runtime, and raw JSON before
being treated as evidence.

Claim 3 uses an unbiased two-probe parameter-space Hutchinson estimator in place
of the paper implementation's exact recursive Jacobian trace. Claim 4 tests
four representative source widths rather than every plotted marker. These are
documented scope boundaries, not hidden equivalences.

## Local verification

Run the lightweight repository verifier with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~

It checks repository identity, branch topology, commit attribution, dossier
hashes, raw evidence fields, claim controls, and the existing release gate. It
does not run <code>reproduction.run_all</code>.
