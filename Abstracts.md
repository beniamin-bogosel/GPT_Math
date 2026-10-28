# Abstracts

Author: [Beniamin Bogosel](https://beniamin-bogosel.github.io/), Faculty of Exact Sciences, Aurel Vlaicu University of Arad, Arad, Romania. Email: [beniamin.bogosel@uav.ro](mailto:beniamin.bogosel@uav.ro).

Prepared with assistance from OpenAI GPT models. The author retains responsibility for the content.

## 1. A sharp polygonal Finsler–Hadwiger inequality

[Paper (PDF)](Results/QuantitativeIsoperimetric/sharp_polygonal_finsler_hadwiger.pdf)

For every convex $n$-gon of positive area $A$ with side lengths $a_1,\ldots,a_n$, we prove

$$
\sum_{i=1}^n a_i^2 \ge 4\tan\frac{\pi}{n}\,A
+c_n\sum_{i<j}(a_i-a_j)^2,
\qquad c_n=1-\frac{\tan(\pi/n)}{\tan(\pi/(n-1))},
$$

where $c_3=1$. The coefficient is optimal, and equality holds exactly for regular polygons. Sharpness is approached by cyclic polygons with one side tending to zero and the other sides tending to those of a regular $(n-1)$-gon, or a doubled segment when $n=3$. The proof combines the classical maximal-area property of cyclic polygons with a two-variable minimization on the simplex of half central angles. Equivalently, we determine the best constant controlling the side-length variance by the polygonal isoperimetric deficit. Combined with a classical radial-variance inequality and the established convexification reduction, the estimate recovers the main stability estimates of Indrei and Nurbekyan with explicit constants. The cases $n=3$ and $n=4$ recover known Finsler–Hadwiger inequalities.

## 2. Meissner Conjecture Work

[Paper (PDF)](Results/MeissnerConjecture/MeissnerConjectureWork.pdf)

We give an independent, exact-arithmetic verification of the geometric lower-bound calculation publicly posted by Hyra, including its nonsmooth analytic reduction and all eighteen cap rows. Applying that method to a different radius partition yields the substantial localization

$$
R(K)\leq0.60247\ \Longrightarrow\
V(K)\geq\frac{1336460360333}{10^{13}}\pi>V_{\mathrm M},
$$

so every width-one volume minimizer has circumradius greater than $0.60247$. This is not a better universal volume bound than Jiang's stated $0.41275$. We consolidate further analytic and computer-assisted results: generating circumcontacts of finite Meissner polyhedra; improved static repair using Jiang's contact deficit; square-cell stability for a specified canonical refinement class; joint product–radius ascent criteria; and a uniform instability certificate for symmetric stars with every odd number of opposite vertices at least five. A separate analysis explains an obstruction to using Hynd's weak flow backward. All hypotheses, numerical qualifications, and unresolved steps are retained. The conjecture, maximal circumradius of a minimizer, and the unrestricted tetrahedral completion inequality remain open.

## 3. Area-minimizing polygons with a regular difference body

[Paper (PDF)](Results/RegularDifferenceBody/discrete_area_m3n.pdf)

Let $m=3n$, and let $P_m$ be the regular $2m$-gon of inradius one. We determine the least area of a convex polygon $T$ satisfying $T-T=P_m$, and classify every minimizer. The minimum is

$$
\frac{m\sin(\pi/m)-\sqrt3}{2\cos^2(\pi/(2m))}.
$$

Equality holds precisely when the cyclic side-length sequence consists of three blocks of $n$ maximal lengths alternating with three blocks of $n$ zero lengths. The proof constructs a circumscribed regular hexagon from finitely many support values and derives an exact nonnegative area deficit using polygon mixed areas. The equality argument is a finite normal-cone calculation. No continuous constant-width area-minimization theorem is used.
