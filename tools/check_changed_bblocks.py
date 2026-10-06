#!/usr/bin/env python3
"""Fail when a building block touched by a change does not pass bblocks-postprocess validation.

postprocess --fail-on-error only fails on processing exceptions; validation failures end up in
build/tests/report.json and never fail the run. This script is the acceptance gate for pull
requests: it maps the changed files to the building blocks that contain them (nearest directory
with a bblock.json under the items dir), plus the blocks that depend on those, and exits non-zero if
any of them failed. Failures in untouched blocks are listed but do not fail the check.

Usage: check_changed_bblocks.py <report.json> <base-ref> [--items-dir _sources] [--prefix ogc.hosted.seadots.]
Writes a Markdown summary to $GITHUB_STEP_SUMMARY when set.
"""
import argparse, json, os, subprocess, sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("base_ref")
    ap.add_argument("--items-dir", default="_sources")
    ap.add_argument("--prefix", default="ogc.hosted.seadots.")
    a = ap.parse_args()

    items = Path(a.items_dir)
    changed = subprocess.run(["git", "diff", "--name-only", f"{a.base_ref}...HEAD"],
                             capture_output=True, text=True, check=True).stdout.split()
    touched = set()
    for f in changed:
        p = Path(f)
        if items not in p.parents:
            continue
        for d in [p.parent, *p.parent.parents]:
            if d == items.parent:
                break
            if (d / "bblock.json").exists():
                touched.add(a.prefix + ".".join(d.relative_to(items).parts))
                break

    # Blocks depending on a touched block can break too.
    deps = {}
    for bj in items.glob("**/bblock.json"):
        bid = a.prefix + ".".join(bj.parent.relative_to(items).parts)
        deps[bid] = [x.replace("bblocks://", "") for x in json.loads(bj.read_text(encoding="utf-8")).get("dependsOn", [])]
    grew = True
    while grew:
        grew = False
        for bid, ds in deps.items():
            if bid not in touched and touched.intersection(ds):
                touched.add(bid)
                grew = True

    report = json.loads(Path(a.report).read_text(encoding="utf-8"))["bblocks"]
    failed_touched = sorted(b for b in touched if b in report and not report[b]["result"])
    failed_other = sorted(b for b, r in report.items() if not r["result"] and b not in touched)
    missing = sorted(b for b in touched if b not in report)

    lines = ["## Building blocks validation", "",
             f"Touched by this change (incl. dependants): {len(touched)}", ""]
    for b in sorted(touched):
        r = report.get(b)
        status = "missing from report" if r is None else ("pass" if r["result"] else "**FAIL**")
        counts = "" if r is None else f" ({r['counts']['passed']}/{r['counts']['total']} items)"
        lines.append(f"- `{b}`: {status}{counts}")
    if failed_other:
        lines += ["", f"Failing blocks not touched by this change (not blocking): {len(failed_other)}", ""]
        lines += [f"- `{b}`" for b in failed_other]
    text = "\n".join(lines) + "\n"
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(text)
    return 1 if failed_touched or missing else 0


if __name__ == "__main__":
    sys.exit(main())
