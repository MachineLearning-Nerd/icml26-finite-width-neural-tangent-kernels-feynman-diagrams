#!/usr/bin/env python3
"""Verify the published finite-width NTK dossier without rerunning science."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_ORIGIN = (
    "https://github.com/MachineLearning-Nerd/"
    "icml26-finite-width-neural-tangent-kernels-feynman-diagrams"
)
EXPECTED_BRANCHES = {
    "main",
    "audit/five-diagram-baseline",
    "audit/five-million-cancellation",
    "audit/gelu-finite-width-correction",
    "audit/paper-scale-critical-depth",
    "audit/symbolic-rules-scale-invariance",
    "release/cumulative-evidence",
    "release/publication-gates",
}
EXPECTED_IDENTITY = (
    "MachineLearning-Nerd",
    "MachineLearning-Nerd@users.noreply.github.com",
)
FIXED_COMMAND = (
    "uv sync --frozen --all-extras && "
    "uv run --frozen python -m reproduction.run_all"
)
ERRORS: list[str] = []


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        ERRORS.append(f"{relative}: cannot parse JSON: {exc}")
        return {}


def main() -> int:
    origin_result = run("git", "remote", "get-url", "origin")
    origin = origin_result.stdout.strip().removesuffix(".git").rstrip("/")
    require(origin == EXPECTED_ORIGIN, f"unexpected origin: {origin!r}")

    symref = run("git", "ls-remote", "--symref", "origin", "HEAD")
    require(
        "ref: refs/heads/main\tHEAD" in symref.stdout,
        "origin HEAD does not point to main",
    )

    heads = run("git", "ls-remote", "--heads", "origin")
    remote_branches = set()
    for line in heads.stdout.splitlines():
        fields = line.split("\t", 1)
        if len(fields) == 2 and fields[1].startswith("refs/heads/"):
            remote_branches.add(fields[1].removeprefix("refs/heads/"))
    require(remote_branches == EXPECTED_BRANCHES, f"remote branches: {sorted(remote_branches)}")
    require(
        not any(branch.startswith("orx/") for branch in remote_branches),
        "old orx branch remains on the remote",
    )

    local_heads = run(
        "git",
        "for-each-ref",
        "--format=%(refname:strip=2)",
        "refs/heads",
    )
    local_branches = set(filter(None, local_heads.stdout.splitlines()))
    require(
        local_branches <= EXPECTED_BRANCHES,
        f"unexpected local branches: {sorted(local_branches - EXPECTED_BRANCHES)}",
    )
    old_refs = run("git", "for-each-ref", "refs/original")
    require(not old_refs.stdout.strip(), "refs/original exists")

    count_result = run("git", "rev-list", "--count", "--all")
    try:
        commit_count = int(count_result.stdout.strip())
    except ValueError:
        commit_count = 0
    require(commit_count >= 13, f"reachable commit count is only {commit_count}")

    identity_output = run(
        "git",
        "log",
        "--all",
        "--format=%an%x09%ae%x09%cn%x09%ce",
    ).stdout
    for line in filter(None, identity_output.splitlines()):
        author_name, author_email, committer_name, committer_email = line.split("\t")
        require(
            (author_name, author_email) == EXPECTED_IDENTITY,
            f"non-canonical author identity: {line}",
        )
        require(
            (committer_name, committer_email) == EXPECTED_IDENTITY,
            f"non-canonical committer identity: {line}",
        )
    messages = run("git", "log", "--all", "--format=%B").stdout
    require(
        "Co-authored-by:" not in messages and "Co-Authored-By:" not in messages,
        "co-author trailer found in commit messages",
    )

    required_files = [
        "README.md",
        "STATUS.md",
        "BRANCH_AUDIT.md",
        "AUTHOR_THANK_YOU.md",
        "CITATION.cff",
        "CLAIM_EVIDENCE.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "SOURCE_AUDIT.md",
        "claims.json",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
        "reproduction/release_gate.py",
        "release/space_upload_allowlist.json",
        "space/data/cumulative_run.json",
        "space/data/release_rerun_summary.json",
        "space/pages/claim-1.md",
        "space/pages/claim-2.md",
        "space/pages/claim-3.md",
        "space/pages/claim-4.md",
        "space/pages/claim-5.md",
    ]
    for relative in required_files:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    manifest = load_json("EVIDENCE_MANIFEST.json")
    require(manifest.get("branch_contract") == {
        "default": "main",
        "total": 8,
        "descriptive": 7,
        "old_prefix_absent": "orx/",
    }, "branch contract mismatch")
    for relative, expected in manifest.get("aggregates", {}).items():
        path = ROOT / relative
        require(path.is_file(), f"missing aggregate input: {relative}")
        if path.is_file():
            require(sha256(path) == expected, f"aggregate hash mismatch: {relative}")
    for row in manifest.get("files", []):
        relative = row.get("path", "")
        path = ROOT / relative
        expected = row.get("sha256")
        require(path.is_file(), f"manifest file missing: {relative}")
        require(expected not in (None, "", "PENDING"), f"manifest hash pending: {relative}")
        if path.is_file() and expected not in (None, "", "PENDING"):
            require(sha256(path) == expected, f"manifest hash mismatch: {relative}")

    claims = load_json("claims.json")
    require(
        claims.get("repository") ==
        "MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams",
        "claims repository marker mismatch",
    )
    require(
        claims.get("overall_verdict") ==
        "VERIFIED_SCOPED_FINITE_CONTRACTS_NOT_UNIVERSAL"
        and claims.get("publication_allowed") is False
        and claims.get("score_claim") is False
        and claims.get("official_author_endorsement") is False,
        "claims publication boundary mismatch",
    )
    reproduction = load_json("reproduction_verdicts.json")
    require(
        reproduction.get("repository") ==
        "MachineLearning-Nerd/icml26-finite-width-neural-tangent-kernels-feynman-diagrams"
        and reproduction.get("overall_verdict") ==
        "VERIFIED_SCOPED_FINITE_CONTRACTS_NOT_UNIVERSAL"
        and reproduction.get("publication_allowed") is False
        and reproduction.get("score_claim") is False
        and reproduction.get("official_author_endorsement") is False,
        "reproduction publication boundary mismatch",
    )
    require(
        [(row.get("id"), row.get("status")) for row in reproduction.get("claims", [])]
        == [(row.get("id"), row.get("status")) for row in claims.get("claims", [])],
        "reproduction claim statuses mismatch",
    )
    expected_statuses = {
        1: "VERIFIED_FINITE_RULE_RECONSTRUCTION",
        2: "VERIFIED_FIVE_DIAGRAM_CERTIFICATE",
        3: "VERIFIED_SYMBOLIC_AND_FINITE_EMPIRICAL_CONTRACT",
        4: "VERIFIED_FOUR_REPRESENTATIVE_GELU_WIDTHS",
        5: "VERIFIED_FINITE_CRITICAL_DEPTH_CONTRACT",
    }
    actual_claims = {item.get("id"): item for item in claims.get("claims", [])}
    require(set(actual_claims) == set(expected_statuses), "claims.json IDs mismatch")
    for claim_id, status in expected_statuses.items():
        require(
            actual_claims.get(claim_id, {}).get("status") == status,
            f"claims.json status mismatch for Claim {claim_id}",
        )

    state = load_json("AUTONOMOUS_STATE.json")
    require(
        state.get("phase") == "published_and_verified"
        and state.get("publication_allowed") is False
        and state.get("overall_verdict") ==
        "VERIFIED_SCOPED_FINITE_CONTRACTS_NOT_UNIVERSAL"
        and state.get("score_claim") is False
        and state.get("official_author_endorsement") is False
        and state.get("branch_count") == len(EXPECTED_BRANCHES),
        "state publication boundary mismatch",
    )

    cumulative = load_json("space/data/cumulative_run.json")
    require(cumulative.get("passed") is True, "cumulative run did not pass")
    require(cumulative.get("fixed_command") == FIXED_COMMAND, "fixed command mismatch")
    c1 = cumulative.get("claim1", {})
    c2 = cumulative.get("claim2", {})
    c3 = cumulative.get("claim3", {})
    c4 = cumulative.get("claim4", {})
    c5 = cumulative.get("claim5", {})
    require(c1.get("verifier", {}).get("passed") is True, "Claim 1 verifier failed")
    require(c1.get("checker", {}).get("passed") is True, "Claim 1 checker failed")
    require(c1.get("verifier", {}).get("checks", {}).get("invalid_unpaired_color_rejected") is True,
            "Claim 1 invalid-color control missing")
    require(c2.get("verifier", {}).get("passed") is True, "Claim 2 verifier failed")
    require(c2.get("checker", {}).get("passed") is True, "Claim 2 checker failed")
    require(c2.get("control", {}).get("passed") is True, "Claim 2 control failed")
    require(c2.get("control", {}).get("actual_exit") == 1, "Claim 2 control did not reject mutation")
    require(c2.get("verifier", {}).get("checks", {}).get("exactly_five_diagrams") is True,
            "Claim 2 five-diagram check missing")
    require(c3.get("symbolic", {}).get("passed") is True, "Claim 3 symbolic verifier failed")
    require(c3.get("symbolic_checker", {}).get("passed") is True, "Claim 3 symbolic checker failed")
    require(c3.get("symbolic_control", {}).get("passed") is True, "Claim 3 symbolic control failed")
    require(c3.get("empirical", {}).get("passed") is True, "Claim 3 empirical contract failed")
    require(c3.get("empirical", {}).get("checks", {}).get(
        "exact_five_million_initializations_per_width"
    ) is True, "Claim 3 five-million check missing")
    require(c3.get("empirical", {}).get("network_initializations_per_activation_width") == 5_000_000,
            "Claim 3 sample count mismatch")
    require(
        c3.get("empirical", {}).get("architecture", {}).get("hidden_widths") == [20, 80],
        "Claim 3 widths mismatch",
    )
    require(
        c3.get("empirical", {}).get("architecture", {}).get("bias") is False,
        "Claim 3 bias-free architecture missing",
    )
    require(c3.get("empirical", {}).get("checks", {}).get(
        "statistical_contract_passes"
    ) is True, "Claim 3 statistical contract missing")
    require(c3.get("empirical", {}).get("verification", {}).get("passed") is True,
            "Claim 3 empirical verification missing")
    require(c3.get("empirical", {}).get("verification", {}).get("checks", {}).get(
        "all_offdiagonal_controls_detect_at_least_1pct_correction_at_5se"
    ) is True, "Claim 3 off-diagonal control missing")
    require(c4.get("verifier", {}).get("passed") is True, "Claim 4 verifier failed")
    require(
        c4.get("verifier", {}).get("network_initializations_per_width") == 100_000,
        "Claim 4 sample count mismatch",
    )
    require(
        [row.get("width") for row in c4.get("verifier", {}).get("rows", [])]
        == [32, 56, 100, 220],
        "Claim 4 widths mismatch",
    )
    require(c4.get("verifier", {}).get("checks", {}).get(
        "infinite_width_negative_control_fails"
    ) is True, "Claim 4 negative control missing")
    require(
        c4.get("verifier", {}).get("negative_control_infinite_width_substitution", {}).get(
            "passed"
        ) is False,
        "Claim 4 infinite-width mutation unexpectedly passed",
    )
    require(c5.get("verifier", {}).get("passed") is True, "Claim 5 verifier failed")
    require(c5.get("verifier", {}).get("width") == 200, "Claim 5 width mismatch")
    require(c5.get("verifier", {}).get("depth") == 30, "Claim 5 depth mismatch")
    require(
        c5.get("verifier", {}).get("network_initializations_per_regime") == 1_000,
        "Claim 5 sample count mismatch",
    )
    c5v = c5.get("verifier", {}).get("verification", {})
    for key in (
        "critical_slope_within_3_standard_errors",
        "critical_diagonal_linear_r_squared_at_least_0_995",
        "low_variance_control_has_negative_exponential_log_slope",
        "high_variance_control_has_positive_exponential_log_slope",
        "high_variance_curve_rejected_by_critical_contract",
    ):
        require(c5v.get("checks", {}).get(key) is True, f"Claim 5 control missing: {key}")

    rerun = load_json("space/data/release_rerun_summary.json")
    require(rerun.get("passed") is True, "independent release rerun did not pass")
    require(rerun.get("fixed_command") == FIXED_COMMAND, "rerun command mismatch")
    require(rerun.get("claim_status") == {
        "claim1": "VERIFIED",
        "claim2": "VERIFIED",
        "claim3": "VERIFIED",
        "claim4": "VERIFIED",
        "claim5": "VERIFIED",
    }, "rerun claim status mismatch")
    require(
        rerun.get("independent_rerun_maximum_combined_standard_error_z") == {
            "claim3": 0.0,
            "claim4": 0.0,
            "claim5": 0.0,
        },
        "rerun z summary mismatch",
    )

    gate = run("env", "PYTHONDONTWRITEBYTECODE=1", "python3", "reproduction/release_gate.py")
    require(gate.returncode == 0, f"release gate failed with {gate.returncode}: {gate.stderr.strip()}")

    if ERRORS:
        print("FINAL_AUDIT=FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"FINAL_AUDIT=VERIFIED branches={len(remote_branches)} commits={commit_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
