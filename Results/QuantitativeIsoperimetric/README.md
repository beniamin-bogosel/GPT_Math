# A sharp polygonal Finsler–Hadwiger inequality

Beniamin Bogosel, supported by GPT-5.6 Sol (OpenAI). Revised October 28, 2026.

Faculty of Exact Sciences, Aurel Vlaicu University of Arad, Arad, Romania. [Email](mailto:beniamin.bogosel@uav.ro) · [Webpage](https://beniamin-bogosel.github.io/).

- [Paper (PDF)](sharp_polygonal_finsler_hadwiger.pdf)
- [References (BibTeX)](references.bib)
- [Research audit and literature assessment](RESEARCH_AUDIT.md)
- [Verification script](verify.py) and [recorded results](verification.json)

For a convex polygon with $n\ge3$ sides of lengths $a_1,\ldots,a_n$ and area $A$,

$$
\sum_{i=1}^n a_i^2 \ge 4\tan\frac{\pi}{n}\,A
+\left(1-\frac{\tan(\pi/n)}{\tan(\pi/(n-1))}\right)
\sum_{i<j}(a_i-a_j)^2.
$$

For $n=3$, the coefficient is interpreted as $1$. It is optimal for every $n$, and equality among positive-area convex polygons holds exactly for regular polygons. The proof allows the circumcenter of a cyclic polygon to lie outside the polygon. It also covers polygons with consecutive collinear sides.

The triangle case is classical. The quadrilateral case is [Giugiuc–Dao–Altintas (2018)](https://ijgeometry.com/wp-content/uploads/2018/04/81-86.pdf). The general coefficient answers the optimization problem in [Dao's 2018 question](https://mathoverflow.net/questions/299056). The current search did not locate this coefficient for general $n$; the note makes no exhaustive novelty claim.

## Consequence for the Indrei–Nurbekyan inequality

The sharp side-length bound, combined with the classical Fisher–Ruoff–Shilleto radial inequality, recovers the joint side/radial stability estimate for convex polygons with the explicit constant in Corollary 6.1 of the manuscript. The radial variance uses distances to the vertex barycenter. The joint constant is not asserted to be optimal. Remark 6.2 retains the same established convexification theorem and area conventions as Indrei–Nurbekyan to recover their general Theorem 1.1 and the symmetric-difference estimate in Corollary 1.2. Together with the convex case (their Corollary 1.3), this gives an alternative elementary proof of their main stability estimates. The manuscript also verifies optimality of the linear order in the deficit.

## Build

The LaTeX source is kept locally and excluded from version control, along with auxiliary LaTeX files. The PDF, BibTeX references and verification scripts are included in the repository. The build instructions below require the local `sharp_polygonal_finsler_hadwiger.tex` file; a fresh clone can run the supplementary verification without it.

From the repository root:

```sh
make pdf
```

This requires pdfLaTeX, BibTeX and Python 3. A standard TeX Live installation supplies the LaTeX packages used. The build runs BibTeX and three LaTeX passes, checks for unresolved citations and references and overfull boxes, and copies the finished PDF into this directory. Intermediate files stay in the ignored `build/` directory. The manuscript date is fixed so that it does not change on each build.

To compile manually from this directory:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build sharp_polygonal_finsler_hadwiger.tex
BIBINPUTS=.: bibtex build/sharp_polygonal_finsler_hadwiger
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build sharp_polygonal_finsler_hadwiger.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build sharp_polygonal_finsler_hadwiger.tex
python3 check_build.py
cp build/sharp_polygonal_finsler_hadwiger.pdf sharp_polygonal_finsler_hadwiger.pdf
```

For an arXiv source upload or a journal requiring the generated bibliography, include `build/sharp_polygonal_finsler_hadwiger.bbl` alongside the `.tex` file. The `.bib` file is the editable bibliography source.

## Supplementary verification

An isolated Python environment is optional:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r Results/QuantitativeIsoperimetric/requirements.txt
make check PYTHON="$PWD/.venv/bin/python"
```

With the dependencies already installed, run `make check` directly. The default run checks 400,000 simplex points, symbolic identities, every equal-positive boundary configuration for $n=3,\ldots,12$, and failure of an increased coefficient at strictly positive angles. Vertex coordinates and the shoelace formula independently verify the cyclic reduction. The result is written to `verification.json` with the seed and dependency versions. Numerical checks supplement the analytic proof.

The original [`codex_transform_isoperimetric.md`](codex_transform_isoperimetric.md) is retained as a historical handoff. The revised manuscript and research audit describe the current result and references.
