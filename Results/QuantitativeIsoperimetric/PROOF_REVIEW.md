# Proof review

Reviewed October 28, 2026, against the manuscript containing Section 6 and Remark 6.2.

The recommendations below have since been incorporated into Remarks 3.2,
6.2 and 6.3: the two-coordinate boundary formula, the scope of the
self-intersecting-polygon deduction, and the explicit perturbation coefficient.

## Verdict

The analytic proof of Theorem 2.1 is correct. The optimal coefficient, the characterization of equality, and the equivalent variance estimates follow from the argument as written. I found no missing case in the two-variable minimization. Corollary 6.1 correctly follows from the cited classical radial inequality.

The general-polygon implications in Remark 6.2 are valid **as deductions within the same area and convexification framework used by Indrei–Nurbekyan**. They are not a new, independent treatment of area or convexification for self-intersecting polygons. That dependence should remain explicit in any abstract or introductory claim.

This review is an analytic check, not a formal proof certificate. The previously recorded numerical checks are supplementary.

## 1. Cyclic reduction

A positive-area convex polygon satisfies each strict polygon inequality: equality of one side length with the sum of the others would force the remaining chain to lie on that side, contradicting positive area. Thus its ordered side lengths admit a cyclic maximizer. The secant-polygon theorem cited in Section 3 supplies both area maximality and the assertion that a maximizer is cyclic.

Writing the residual as

$$F(P)=\sum_i a_i^2-cD(P)-4\tau_n A(P),$$

and denoting the cyclic maximizer by $P_*$, one has

$$F(P)=F(P_*)+4\tau_n\bigl(A(P_*)-A(P)\bigr).$$

Both terms on the right are nonnegative once the cyclic case is proved. This establishes the reduction and makes its equality condition transparent. It also covers the allowed collinear consecutive sides of the original polygon.

The successive angular gaps must be taken in counterclockwise vertex order. Their halves lie in $(0,\pi)$ and sum to $\pi$. The formula $A=R^2\sum_i\sin x_i\cos x_i$ uses signed triangles, so allowing one $x_i>\pi/2$ is correct. There is no missing factor of two.

## 2. The mixing lemma

For a pair of coordinates with sum $p$, set $x=p/2+d$, $y=p/2-d$ and $z=\cos d$. The feasible interval is $[\cos(p/2),1]$. If the coordinates are positive and unequal, $z$ is strictly inside this interval.

The quadratic coefficients stated in the paper follow directly:

$$\alpha=4c\sin^2(p/2)+2(nc-1)\cos p-2\tau_n\sin p,
\qquad \beta=4cr\sin(p/2).$$

At a minimizer with at least three positive coordinates, a selected positive pair has $p<\pi$. Every remaining positive coordinate is strictly below $\pi$, so $r>0$ and $\beta>0$. For $\alpha\ge0$ the quadratic is strictly increasing on the feasible interval, since $z\ge0$. For $\alpha<0$ it is strictly concave. In either case an unequal positive pair has a strictly improving feasible replacement. This proves that all positive coordinates of such a minimizer are equal.

The case of exactly two positive coordinates deserves attention but is handled correctly. In that case $y=\pi-x$, and direct substitution gives

$$\Phi_c(x,\pi-x,0,\ldots,0)
=2\bigl(1-(n-2)c\bigr)\sin^2x.$$

A minimum can therefore be chosen at $x=0,\pi$, or $\pi/2$. If the coefficient vanishes, the whole edge minimizes the restriction. In particular, for $n=3,c=1$, every point of such an edge has value zero. This does **not** contradict the lemma: it asserts existence of an equal-positive minimizer and characterizes all minimizers only when at least three coordinates are positive. It also causes no additional positive-area equality cases.

## 3. Boundary evaluation and optimal coefficient

The evaluation

$$\Phi_c(x^{(m)})=
m\sin^2(\pi/m)\left[1-c(n-m)-\tau_n\cot(\pi/m)\right]$$

is correct for $m\ge2$. The separate $m=1$ value is zero. For $m=n$ the bracket is zero; for $2\le m<n$ it yields the stated upper bound $c_{n,m}$.

For $h(t)=\cot(\pi/t)$, the displayed second derivative is correct. Strict concavity extends to the closed endpoint $t=2$ by continuity. The secant slope from $m$ to $n$ is at least the last unit secant slope, with strict inequality if $m<n-1$. This is the correct direction of comparison. Thus the most restrictive boundary value is $m=n-1$.

No circular use of the desired quantitative inequality occurs: the geometric maximization theorem and the trigonometric calculation suffice.

## 4. Equality and sharpness

Once nonnegativity is established on the full closed simplex, a positive-coordinate equality configuration is a global minimizer. The strengthened assertion of the mixing lemma then forces all half central angles to equal $\pi/n$. Together with equality in cyclicization, this proves that regular polygons are the only positive-area equality cases.

The proposed sharpness sequence lies strictly inside the simplex, so it represents strictly convex cyclic polygons. For every fixed $c>c_n$, its limiting residual is strictly negative. Continuity therefore produces actual positive-area counterexamples to that larger coefficient. Sharpness is not being inferred merely from a degenerate object outside the theorem's domain.

The limiting defect is $4(n-1)\sin^2(\pi/(n-1))>0$. This also justifies optimality after conversion to the perimeter-deficit and variance forms. The doubled segment for $n=3$ is correctly distinguished from the regular $(n-1)$-gon for $n\ge4$.

## 5. Positivity and asymptotics

The identities $D=nV=n^2\sigma_s^2$ and

$$nF(P)=\delta_n(P)-(nc_n-1)D(P)$$

give all the conversions in Section 2. For $n\ge4$, monotonicity of $t\tan(\pi/t)$ yields $\gamma_n>0$; the case $n=3$ is checked separately. Thus every division is legitimate.

An expansion one order beyond that stated is

$$\gamma_n=\frac{2\pi^2}{3n^2}+\frac{\pi^2}{3n^3}+O(n^{-4}).$$

Consequently all three asymptotic statements in Section 5 are consistent.

## 6. Joint stability and its external ingredients

The classical radial inequality is recorded explicitly in Indrei–Nurbekyan, Section 3.1, equations (3.1)–(3.2):

$$8n^2\sin^2(\pi/n)\sigma_r^2\le\delta_n+n^2\sigma_s^2.$$

Here radii are distances from the **vertex barycenter**. Substituting the side bound and adding gives exactly the stated $C_n$. No optimality of this combined constant follows from optimality of the side constant, and the paper correctly avoids claiming it.

For a second analytic check of the radial bound, identify centered vertices with complex numbers and write $z_j=\sum_{k=1}^{n-1}b_k e^{2\pi i kj/n}$. With $\alpha=\pi/n$ and signed shoelace area,

$$Q-4\tan\alpha\,A
=n\sum_{k=1}^{n-1}
\frac{4\sin(k\alpha)\sin((k-1)\alpha)}{\cos\alpha}|b_k|^2.$$

The coefficient vanishes for $k=1$ and is at least $8\sin^2\alpha$ for $2\le k\le n-1$. Also,

$$\sigma_r^2
\le\frac1n\sum_j(|z_j|-|b_1|)^2
\le\frac1n\sum_j|z_j-b_1e^{2\pi i j/n}|^2
=\sum_{k=2}^{n-1}|b_k|^2.$$

This verifies the radial estimate independently for counterclockwise simple polygons, and also explains why an area convention matters for self-intersections.

## 7. Convexification: scope that should remain explicit

For simple polygons, the supplied deduction is complete once the cited length-preserving convexification theorem is invoked. The area-gain identity gives $T\le\delta_n/(4n\tau_n)$, side variance is preserved, and the radial estimate is applied to the original polygon. The stepwise symmetric-difference estimate gives $\alpha_c\le T$. The claimed constants are correct.

For self-intersecting polygons, the manuscript refers to the setting of Indrei–Nurbekyan rather than defining $A$ independently. Their Section 3.8 uses precisely the same preservation and area-gain identities. Substituting the present bound into that reduction is valid, but a reader should not interpret the statement as applying to any chosen meaning of “area” of a self-intersecting polygon.

**Editorial recommendation:** present Remark 6.2 explicitly as recovery of their theorem *under their conventions and cited reduction*. If a fully self-contained extension to self-intersections is desired, define the area functional and state the exact convexification theorem needed. This is a scope/precision issue in the secondary consequence, not a gap in Theorem 2.1.

The phrase “alternative elementary proof” is justified for the new side-length argument. For the complete stability theorem, the qualification “combined with the classical radial inequality and the established convexification reduction” is essential and is already present.

## 8. Sharpness of the exponent

The perturbation argument is correct. On a unit regular polygon, moving one vertex radially by $t$ changes the two adjacent side lengths to first order by $t\sin(\pi/n)$ and leaves the others fixed. Hence

$$\sigma_s^2(P_t)
=\frac{2(n-2)}{n^2}\sin^2(\pi/n)t^2+O(t^3).$$

The coefficient is positive for every $n\ge3$. The deficit is smooth near the regular polygon and has a local minimum there, so it is $O(t^2)$. The proved side bound supplies a matching lower bound. Thus no exponent $p>1$ on the deficit is possible, even after a perimeter normalization by smooth rescaling.

## Recommended disposition

Theorem 2.1 and its sharp variance corollary are mathematically ready for external review. The joint stability derivation is correct. The broad recovery claim should retain its explicit reliance on the original general-polygon conventions. Optional improvements are to display the two-positive-coordinate formula and the perturbation coefficient above; neither is needed to repair a logical gap.

Sources rechecked: [Indrei–Nurbekyan](https://arxiv.org/pdf/1402.4460), especially Sections 2.1, 3.1 and 3.8. The main proof also uses the secant-polygon theorem already cited in the manuscript. No independent re-proof of the general convexification theorem is claimed.
