# Mathematical and bibliographic audit

Checked October 28, 2026. This records the assessment behind the revised manuscript and distinguishes mathematical validation from the literature search.

## Mathematical assessment

The proof establishes the stated inequality for convex polygons of positive area, including polygons with consecutive collinear sides. No gap was found in the central cyclic reduction, two-variable minimization, or identification of the sharp coefficient. The following details have been made explicit in the revision:

1. The fixed-side maximal-area theorem applies because positive-area polygons satisfy the strict polygon inequalities. Equality in that comparison forces cyclicity. The source is the secant-polygon theorem discussed by Kouřimská–Skuppin–Springborn, Section 1, Theorem B, rather than a claim that their existence theorem alone proves area maximality.
2. The half central angles lie in $(0,\pi)$; an angle above $\pi/2$ remains admissible. The signed area is $A=R^2\sum\sin x_i\cos x_i$.
3. With the other coordinates fixed, the two-variable expression is a quadratic in $z=\cos((x-y)/2)$. Its coefficients are now displayed. If at least three coordinates are positive, unequal positive coordinates give an interior value of $z$ and cannot occur at a minimum. With exactly two positive coordinates, one only needs the existence of an endpoint minimizer; not every minimizer need have equal positive coordinates.
4. The one-positive-coordinate configuration has zero functional value and is included explicitly. It is a boundary artifact, not a positive-area polygon.
5. The derivative of $h(t)=\cot(\pi/t)$ is correct and gives strict concavity. The smallest allowable bound on the coefficient is the $m=n-1$ configuration.
6. Regular polygons are the only positive-area equality cases. An increased coefficient fails on the strictly convex approximating sequence, not just on the boundary.
7. When $n=3$, the sharp sequence tends to a doubled segment with side lengths $(2,2,0)$. The phrase “regular two-gon” is unnecessary. For $n\ge4$, the limit is a regular $(n-1)$-gon with one repeated vertex.
8. All three deficit/variance normalizations are equivalent. The coefficient $\gamma_n=nc_n-1$ is positive, so division by it is justified. Symbolic expansion gives

   $$\gamma_n=\frac{2\pi^2}{3n^2}+\frac{\pi^2}{3n^3}+O(n^{-4}).$$

   In particular, the normalized variance coefficient tends to $3/(2\pi^2)$, as asserted in the original draft.

## Primary references and their roles

The side-length estimate also recovers joint side/radial stability after the classical radial inequality is applied. The explicit derivation is recorded below and in Section 6 of the manuscript.

| Reference | Verified information and relevance |
| --- | --- |
| P. Finsler and H. Hadwiger, *Einige Relationen im Dreieck*, Comment. Math. Helv. **10** (1937), 316–326. [Publisher](https://link.springer.com/article/10.1007/BF01214300); [original scan](https://www.e-periodica.ch/cntmng?pid=com-001%3A1937%3A10%3A%3A25). | Classical triangle inequality; DOI added. |
| L. M. Giugiuc, Dao Thanh Oai and K. Altintas, *An inequality related to the lengths and area of a convex quadrilateral*, Int. J. Geom. **7** (2018), no. 1, 81–86. [Journal PDF](https://ijgeometry.com/wp-content/uploads/2018/04/81-86.pdf). | Theorem 1.1 is algebraically identical to the $n=4$ case. The manuscript shows the conversion explicitly. This was missing from the draft bibliography. |
| Dao Thanh Oai, *Strengthened version of Isoperimetric inequality with n-polygon*, MathOverflow, April 30, 2018. [Original question and answers](https://mathoverflow.net/questions/299056). | Poses precisely the form under study. The proposed coefficient fails for triangles, as Pinelis's July 10, 2018 answer observes. The present formula determines the optimal coefficient asked for. |
| E. Indrei and L. Nurbekyan, *On the stability of the polygonal isoperimetric inequality*, Adv. Math. **276** (2015), 62–86. [Publisher](https://www.sciencedirect.com/science/article/pii/S0001870815000675); [author preprint](https://arxiv.org/abs/1402.4460). | Gives simultaneous side/radial stability. Section 3.1 explicitly reduces the convex case to bounding side variance using the classical radial estimate. Our sharp side bound therefore recovers their convex Corollary 1.3 with an explicit constant. “Sharp” there concerns exponents. |
| J. C. Fisher, D. Ruoff and J. Shilleto, *Perpendicular polygons*, Amer. Math. Monthly **92** (1985), no. 1, 23–37. [Publisher](https://www.tandfonline.com/doi/abs/10.1080/00029890.1985.11971529). | Classical radial-variance inequality. Publisher metadata checked; the precise inequality is verified in Indrei–Nurbekyan, equations (3.1)–(3.2), which attributes it to page 35 of this paper. |
| E. Indrei, *A sharp lower bound on the polygonal isoperimetric deficit*, Proc. Amer. Math. Soc. **144** (2016), no. 7, 3115–3122. [DOI](https://doi.org/10.1090/proc/12947); [author preprint](https://arxiv.org/abs/1502.05978). | Adds angular variance to the stability framework; Theorem 1.1 and Corollary 1.2 distinguish the result from the side-only coefficient. Final journal publication is 2016; the preprint is 2015. |
| H. Kouřimská, L. Skuppin and B. Springborn, *A variational principle for cyclic polygons with prescribed edge lengths*, in A. I. Bobenko (ed.), *Advances in Discrete Differential Geometry*, Springer, 2016, 177–195. [Publisher](https://link.springer.com/chapter/10.1007/978-3-662-50447-5_5); [author preprint](https://arxiv.org/abs/1506.08069). | Provides existence/uniqueness of cyclic polygons and a historical account of the fixed-side maximal-area theorem. Chapter DOI added. |
| D. Tang, *Discrete Wirtinger and isoperimetric type inequalities*, Bull. Austral. Math. Soc. **43** (1991), no. 3, 467–474. [Publisher](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/discrete-wirtinger-and-isoperimetric-type-inequalities/339C6AD84F07684A5034A15EAACFC747). | Reference for classical polygonal isoperimetry and discrete Wirtinger methods. Use the journal year 1991, not the later online digitization date. |
| B. Bogosel, *Optimal Finsler–Hadwiger inequalities*, Results Math. **80** (2025), no. 3, Article 88. [Publisher](https://link.springer.com/article/10.1007/s00025-025-02405-6); [author preprint](https://arxiv.org/abs/2508.06285). | Determines nonlinear optimal relations for triangles. It is relevant prior work by the same author, distinct from the general polygon theorem. |

## Implication for joint stability

Write $\delta=\delta_n(P)$ and let $\sigma_r^2$ denote the variance of distances to the vertex barycenter. The classical radial bound recorded by Indrei–Nurbekyan is

$$8n^2\sin^2(\pi/n)\,\sigma_r^2\le\delta+n^2\sigma_s^2.$$

The sharp side estimate gives $n^2\sigma_s^2\le\delta/\gamma_n$. Substitution and addition give

$$\sigma_s^2+\sigma_r^2\le\left[\frac1{n^2\gamma_n}+\frac{1+\gamma_n^{-1}}{8n^2\sin^2(\pi/n)}\right]\delta.$$

This proves the convex Indrei–Nurbekyan estimate with an explicit joint constant, without asserting optimality of that joint constant. The earlier manuscript comparison omitted this implication and has been corrected.

For the general polygon setting and area conventions in their Section 3.8, retain the same established length-preserving convexification theorem. It preserves side variance and has nonnegative total area gain $T=A(P_c)-A(P)$, giving $\delta_n(P)=\delta_n(P_c)+4n\tau_nT$. Apply the side estimate to $P_c$, and the radial inequality directly to $P$, to obtain the same joint estimate and control of $T$. This recovers their Theorem 1.1, including their non-simple-polygon setting, with the explicit coefficient $C_n+1/(4n\tau_n)$.

For simple polygons the symmetric-difference distance to the resulting convexification is at most the sum of the stepwise symmetric differences, which equals $T$. This also recovers their Corollary 1.2. Thus Theorem 1.1 and Corollaries 1.2–1.3 follow from the elementary side-length argument together with the classical radial inequality and the same known convexification reduction. No new convexification theorem is being claimed. The source for that auxiliary result is G. Toussaint, *The Erdős–Nagy theorem and its ramifications*, Comput. Geom. **31** (2005), no. 3, 219–236, [publisher DOI](https://doi.org/10.1016/j.comgeo.2004.12.005); the precise use of area for non-simple polygons is inherited from Indrei–Nurbekyan.

Optimality of the linear order in the deficit follows by moving one vertex of a regular polygon radially: side variance is of order $t^2$, the deficit is smooth and $O(t^2)$ at its minimum, and the side estimate supplies the matching lower bound. Hence an exponent greater than one on the deficit is impossible. The combined numerical coefficient is not asserted to be optimal.

## Search scope and novelty

Searches included polygonal Finsler–Hadwiger inequalities, optimal side-length variance constants, quantitative polygonal isoperimetry, the exact quadrilateral coefficient, and references in the papers above. Following the quadrilateral reference led to the original general question. Searches were performed on October 28, 2026; full-text primary sources and publisher metadata were consulted where accessible.

The classical triangle case and the exact quadrilateral case are established precedents. The general optimization problem was already posed publicly. No source giving the displayed optimal coefficient for every $n$ was located in this targeted search. This supports cautious positioning as an explicit sharp answer to that problem; it does not certify exhaustive novelty. Neither the manuscript nor this audit claims an exhaustive database or citation-index review.

## Reproducible checks

The committed `verification.json` records the deterministic default run of `verify.py`:

- All symbolic checks passed: pair identities and quadratic coefficients, boundary formula, concavity derivative, conversion of all deficits, equivalence to the published quadrilateral result, and the asymptotic expansion.
- 40,000 sampled configurations for each $n=3,\ldots,12$, for 400,000 in total. Three Dirichlet distributions sample the simplex; a fourth distribution forces one half central angle above $\pi/2$.
- The smallest sampled functional value was approximately $-9.2\times10^{-16}$, consistent with floating-point roundoff and within the $10^{-10}$ tolerance.
- Direct chord and shoelace calculations independently checked the geometric formulas on 1,000 configurations per $n$, including 500 forced exterior-center configurations.
- Symbolic checks also verify the joint stability constant and the convexification deficit decomposition. Numerical checks of the radial and joint inequalities use the cyclic polygons and noncircular affine images of them, with distances measured from each polygon's own vertex barycenter.
- Every equal-positive boundary configuration was checked. Increasing the coefficient by $10^{-4}$ failed both at the $m=n-1$ boundary and at strictly positive angles with the last angle $10^{-10}$.
- An 80-digit calculation checked convergence of the normalized variance coefficient to $3/(2\pi^2)$.

The analytic proof carries the theorem; sampling is supplementary. The LaTeX build checks for missing references/citations and overfull boxes. The original authorship and assistance statement have been retained, and the current Codex revision is disclosed separately.
