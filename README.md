# Mathematical results

Research notes by Beniamin Bogosel, with papers, references and reproducible supplementary calculations. Each result has its own directory under [`Results`](Results). LaTeX manuscript sources and auxiliary build files are excluded from version control; the finished PDFs and BibTeX references are included.

| Result | Paper | References and verification |
| --- | --- | --- |
| A sharp polygonal Finsler–Hadwiger inequality | [PDF](Results/QuantitativeIsoperimetric/sharp_polygonal_finsler_hadwiger.pdf) | [Result directory](Results/QuantitativeIsoperimetric) |

The first note determines the optimal coefficient of the side-length defect in a refinement of the polygonal isoperimetric inequality. It includes the known triangle and quadrilateral cases and an elementary proof for every number of sides. Combined with the classical radial-variance inequality and the established convexification reduction, it also recovers the main stability estimates of Indrei and Nurbekyan with explicit constants.

Run the supplementary mathematical checks with `make check`; Python dependencies are recorded in the result directory. The local manuscript can be rebuilt with `make pdf` when the excluded LaTeX source is available (requires pdfLaTeX and BibTeX). See the [result README](Results/QuantitativeIsoperimetric/README.md) for details and the [research audit](Results/QuantitativeIsoperimetric/RESEARCH_AUDIT.md) for the literature assessment.

The manuscript records the use of AI assistance and retains human authorship and responsibility. The note is prepared for public circulation; it has not undergone journal peer review.
