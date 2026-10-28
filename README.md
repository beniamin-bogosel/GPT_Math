# Mathematical results

Research notes by [Beniamin Bogosel](https://beniamin-bogosel.github.io/), Aurel Vlaicu University of Arad ([email](mailto:beniamin.bogosel@uav.ro)), with papers, references and reproducible supplementary calculations. Each result has its own directory under [`Results`](Results). LaTeX manuscript sources and auxiliary build files are excluded from version control; the finished PDFs and BibTeX references are included.

Read the numbered abstracts in [Abstracts.md](Abstracts.md).

| No. | Result | Paper | References and verification |
| --- | --- | --- | --- |
| 1 | A sharp polygonal Finsler–Hadwiger inequality | [PDF](Results/QuantitativeIsoperimetric/sharp_polygonal_finsler_hadwiger.pdf) | [Result directory](Results/QuantitativeIsoperimetric) |
| 2 | Meissner Conjecture Work | [PDF](Results/MeissnerConjecture/MeissnerConjectureWork.pdf) | References and verification details in the PDF |
| 3 | Area-minimizing polygons with a regular difference body | [PDF](Results/RegularDifferenceBody/discrete_area_m3n.pdf) | References and complete proof in the PDF |

Run the first note's supplementary mathematical checks with `make check`; Python dependencies are recorded in its result directory. Its local manuscript can be rebuilt with `make pdf` when the excluded LaTeX source is available (requires pdfLaTeX and BibTeX). See the [result README](Results/QuantitativeIsoperimetric/README.md) for details and the [research audit](Results/QuantitativeIsoperimetric/RESEARCH_AUDIT.md) for the literature assessment.

The manuscripts acknowledge assistance from OpenAI GPT models; the author retains responsibility for the content. The first note is prepared for public circulation; it has not undergone journal peer review.
