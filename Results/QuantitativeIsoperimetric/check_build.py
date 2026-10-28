#!/usr/bin/env python3
"""Reject unresolved citations/references, layout overflows and BibTeX warnings."""

from pathlib import Path
import re

base = Path(__file__).resolve().parent / "build" / "sharp_polygonal_finsler_hadwiger"
log = base.with_suffix(".log").read_text(encoding="utf-8")
blg = base.with_suffix(".blg").read_text(encoding="utf-8")
patterns = (
    r"LaTeX Warning:", r"Package \S+ Warning:", r"Overfull \\[hv]box",
    r"Missing character:", r"^!", r"Warning--",
)
failures = [line for line in (log + "\n" + blg).splitlines()
            if any(re.search(pattern, line) for pattern in patterns)]
if failures:
    raise SystemExit("Build checks failed:\n" + "\n".join(failures))
print("LaTeX/BibTeX checks passed: no unresolved references, citations, or overfull boxes.")
