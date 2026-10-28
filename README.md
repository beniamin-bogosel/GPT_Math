# Mathematical results

Research notes by Beniamin Bogosel, with papers, references and reproducible supplementary calculations. Each result has its own directory under [`Results`](Results). LaTeX manuscript sources and auxiliary build files are excluded from version control; the finished PDFs and BibTeX references are included.

| Result | Paper | References and verification |
| --- | --- | --- |
| A sharp polygonal Finsler–Hadwiger inequality | [PDF](Results/QuantitativeIsoperimetric/sharp_polygonal_finsler_hadwiger.pdf) | [Result directory](Results/QuantitativeIsoperimetric) |
| Progress on the Meissner conjecture | [PDF](Results/MeissnerConjecture/MeissnerConjectureWork.pdf) | References and verification details in the PDF |
| Area-minimizing polygons with a regular difference body | [PDF](Results/RegularDifferenceBody/discrete_area_m3n.pdf) | References and complete proof in the PDF |

The first note determines the optimal coefficient of the side-length defect in a refinement of the polygonal isoperimetric inequality. It includes the known triangle and quadrilateral cases and an elementary proof for every number of sides. Combined with the classical radial-variance inequality and the established convexification reduction, it also recovers the main stability estimates of Indrei and Nurbekyan with explicit constants.

The second report consolidates work on the Meissner conjecture, including independent verification of Hyra's lower-bound calculation, certified circumradius localization, and structural results on finite Meissner polyhedra and restricted tetrahedral cells. The conjecture remains open. Only the main PDF is included here.

The third note determines the minimum area of a convex polygon whose difference body is a prescribed regular $6n$-gon, for every integer $n\ge1$, and classifies all equality cases. The proof uses finite support data and polygon mixed areas. Only the main PDF is included here.

Run the first note's supplementary mathematical checks with `make check`; Python dependencies are recorded in its result directory. Its local manuscript can be rebuilt with `make pdf` when the excluded LaTeX source is available (requires pdfLaTeX and BibTeX). See the [result README](Results/QuantitativeIsoperimetric/README.md) for details and the [research audit](Results/QuantitativeIsoperimetric/RESEARCH_AUDIT.md) for the literature assessment.

The first manuscript records the use of AI assistance and retains human authorship and responsibility. The note is prepared for public circulation; it has not undergone journal peer review.
