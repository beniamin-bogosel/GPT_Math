
# Codex handoff: transform the existing Isoperimetric manuscript into a public research note

## Goal

Transform the existing manuscript corresponding to `Isoperimetric.pdf` / its LaTeX source into a clean, self-contained public research note centered on the new sharp polygonal Finsler--Hadwiger inequality.

This is intended primarily for GitHub / the author's webpage, not as a journal submission. The tone should therefore be rigorous and polished but transparent about provenance and literature status.

## Required authorship

Use exactly this authorship presentation on the title page:

**Beniamin Bogosel**  
**supported by GPT-5.6 Sol (OpenAI)**

Do not list GPT as a conventional human coauthor. Keep the second line visibly subordinate to the author's name.

Also include an acknowledgement/provenance paragraph near the end saying that GPT-5.6 Sol was used for exploratory calculations, proof testing, literature searches, and drafting, and that Beniamin Bogosel is responsible for the final mathematical content.

## Main theorem to build the paper around

For a convex nondegenerate \(n\)-gon \(P\), \(n\ge 3\), with side lengths \(a_1,\dots,a_n\) and area \(A\),

\[
\sum_{i=1}^n a_i^2
\ge
4\tan\frac{\pi}{n}\,A
+
c_n\sum_{1\le i<j\le n}(a_i-a_j)^2,
\]

with the sharp constant

\[
c_n
=
1-
\frac{\tan(\pi/n)}{\tan(\pi/(n-1))},
\]

using the convention \(\tan(\pi/2)=+\infty\), so \(c_3=1\).

Equality among nondegenerate convex \(n\)-gons occurs exactly for the regular \(n\)-gon. The constant is sharp but, apart from the regular equality case, sharpness is approached at the boundary by a regular \((n-1)\)-gon with one side collapsed / one repeated vertex.

For \(n=3\), recover Finsler--Hadwiger.  
For \(n=4\), recover

\[
c_4=1-\frac1{\sqrt3}
=\frac{\sqrt3-1}{\sqrt3}.
\]

## Authoritative proof architecture

Use the attached/new file `sharp_polygonal_finsler_hadwiger.tex` as the authoritative proof source. Do not revert to the old support-number or outer-bisector attempts as the main argument.

The proof must have these steps.

### 1. Cyclicization

Use the classical theorem:

> Among convex polygons with prescribed side lengths, the maximal-area polygon is cyclic.

Since the side-length terms remain unchanged and the area increases, it is enough to prove the inequality for cyclic polygons.

Cite a reliable source, preferably:
- Kouřimská--Skuppin--Springborn, *A Variational Principle for Cyclic Polygons with Prescribed Edge Lengths*, 2016, for the classical secant-polygon theorem;
- Tang, *Discrete Wirtinger and isoperimetric type inequalities*, Bull. Austral. Math. Soc. 43 (1991), as a precedent for cyclic reduction in polygonal isoperimetry.

Do not assume the circumcenter lies inside the polygon.

### 2. Half-central-angle parametrization

For a cyclic polygon in cyclic order, let the successive central angles be \(2x_i\). Then

\[
x_i\in(0,\pi),\qquad \sum_i x_i=\pi.
\]

One \(x_i\) may exceed \(\pi/2\). This case MUST remain allowed.

Use

\[
a_i=2R\sin x_i,
\qquad
A=R^2\sum_i\sin x_i\cos x_i,
\]

where the area formula is the oriented triangle decomposition relative to the circumcenter.

Set

\[
S=\sum_i\sin x_i,\quad
U=\sum_i\sin^2x_i,\quad
B=\sum_i\sin x_i\cos x_i.
\]

Using

\[
\sum_{i<j}(y_i-y_j)^2
=
n\sum_i y_i^2-\left(\sum_i y_i\right)^2,
\]

reduce the theorem to

\[
\Phi_c(x)
=
cS^2-(nc-1)U-\tan(\pi/n)B\ge0
\]

on the closed simplex

\[
\Delta_n=\{x_i\ge0,\ \sum_i x_i=\pi\}.
\]

### 3. Pairwise mixing lemma

This is the key elementary step and should be written very carefully.

Fix all variables except \(x,y\), fix \(p=x+y\), and write

\[
x=\frac p2+d,\qquad
y=\frac p2-d,\qquad
z=\cos d.
\]

Then

\[
\cos\frac p2\le z\le1.
\]

If

\[
r=\sum_{\text{other indices}}\sin x_j,
\]

show that

\[
\Phi_c=az^2+bz+d_0
\]

with

\[
b=4cr\sin\frac p2\ge0.
\]

Use the following exact logic:

- If at least three coordinates are positive, then for a positive pair \(x,y\), \(r>0\), so \(b>0\).
- If \(a\ge0\), then \(2az+b>0\) because \(z\ge0\), so the pair cannot be an unequal interior minimizer.
- If \(a<0\), the quadratic is strictly concave, so an unequal interior pair cannot minimize it.
- Therefore, at a global minimizer with at least three positive coordinates, all positive coordinates are equal.
- If exactly two coordinates are positive, then \(p=\pi\) and \(r=0\); the quadratic is \(az^2+d_0\), whose minimum can be chosen at an endpoint. This is enough to conclude that *some* global minimizer has all positive entries equal.
- Include the \(m=1\) fully degenerate simplex point only as a harmless boundary artifact; it does not correspond to a nondegenerate polygon.

Conclude that the minimum is attained at

\[
(\underbrace{\pi/m,\dots,\pi/m}_{m\text{ times}},0,\dots,0).
\]

### 4. Evaluate the \(m\)-strata

For \(m\ge2\), compute

\[
\Phi_c
=
m\sin^2\frac{\pi}{m}
\left[
1-c(n-m)-\tan\frac{\pi}{n}\cot\frac{\pi}{m}
\right].
\]

Thus the \(m\)-stratum requires

\[
c\le
c_{n,m}
=
\frac{
1-\tan(\pi/n)/\tan(\pi/m)
}{
n-m
}.
\]

### 5. Identify the worst stratum

Define

\[
h(x)=\cot\frac{\pi}{x},\qquad x\ge2.
\]

Compute

\[
h''(x)
=
-\frac{2u^3}{\pi^2\sin^2u}(1-u\cot u),
\qquad u=\frac{\pi}{x}.
\]

Since \(\tan u>u\) on \((0,\pi/2)\), \(h''<0\).

Use concavity to show

\[
\frac{h(n)-h(m)}{n-m}
\ge
h(n)-h(n-1),
\]

hence

\[
c_{n,m}\ge c_{n,n-1}.
\]

Therefore the optimal coefficient is

\[
c_n=c_{n,n-1}
=
1-\frac{\tan(\pi/n)}{\tan(\pi/(n-1))}.
\]

### 6. Equality and sharpness

For equality among nondegenerate polygons:

- equality in cyclicization forces cyclicity;
- all \(x_i>0\);
- the pairwise mixing argument rules out unequal positive coordinates at a zero global minimum;
- hence all \(x_i=\pi/n\), so the polygon is regular.

For sharpness, use

\[
x_1=\cdots=x_{n-1}
=
\frac{\pi-\varepsilon}{n-1},
\qquad
x_n=\varepsilon,
\]

and let \(\varepsilon\downarrow0\).

### 7. Equivalent quantitative forms

Include

\[
D(P)=\sum_{i<j}(a_i-a_j)^2
\]

and

\[
\delta_n(P)=L^2-4n\tan(\pi/n)A.
\]

Derive

\[
\delta_n(P)\ge \gamma_nD(P),
\]

where

\[
\gamma_n
=
nc_n-1
=
(n-1)-n\frac{\tan(\pi/n)}{\tan(\pi/(n-1))}.
\]

Also, with

\[
V(P)=\sum_i(a_i-L/n)^2,\qquad D(P)=nV(P),
\]

write

\[
V(P)\le
\frac{\delta_n(P)}{n\gamma_n}.
\]

If using the normalized side variance

\[
\sigma_s^2(P)=\frac1nV(P),
\]

then

\[
\sigma_s^2(P)
\le
\frac{\delta_n(P)}{n^2\gamma_n},
\qquad
\frac1{n^2\gamma_n}\to\frac{3}{2\pi^2}.
\]

Check the asymptotic carefully before finalizing.

## How to transform the old manuscript

The current manuscript is exploratory and contains:
- a triangle/Finsler--Hadwiger discussion;
- radial formulas;
- an outer-bisector/self-improvement attempt;
- an inscribed/cyclic polygon idea;
- a tangential-polygon idea.

Restructure drastically.

Recommended final structure:

1. **Introduction**
   - classical polygonal isoperimetric inequality;
   - Finsler--Hadwiger for \(n=3\);
   - known quadrilateral coefficient;
   - Indrei--Nurbekyan quantitative stability;
   - state that this note isolates the pure side-length correction and gives an explicit sharp coefficient by an elementary route.

2. **Main theorem and equivalent forms**

3. **Cyclic reduction**

4. **Pairwise mixing lemma**

5. **Proof of the sharp constant**

6. **Equality, degenerations, asymptotics**

7. **Relation with quantitative polygonal isoperimetry**

8. **Acknowledgement/provenance**

The old outer-bisector and support-number explorations should NOT remain in the main proof. If they are historically useful, move them to a short final section titled “Exploratory remarks” or omit them entirely.

The cyclic idea from the old Section 5 is the one that matured into the final proof and may be mentioned briefly in the introduction as motivation, without reproducing the unfinished calculations.

## Literature positioning

Use at least:

- P. Finsler and H. Hadwiger, *Einige Relationen im Dreieck*, Comment. Math. Helv. 10 (1937), 316--326.
- E. Indrei and L. Nurbekyan, *On the stability of the polygonal isoperimetric inequality*, Adv. Math. 276 (2015), 62--86, DOI 10.1016/j.aim.2015.02.013.
- H. Kouřimská, L. Skuppin, B. Springborn, *A Variational Principle for Cyclic Polygons with Prescribed Edge Lengths*, in *Advances in Discrete Differential Geometry*, 2016, 177--195.
- D. Tang, *Discrete Wirtinger and isoperimetric type inequalities*, Bull. Austral. Math. Soc. 43 (1991), 467--474, DOI 10.1017/S0004972700029312.

Important: do NOT claim that the sharp coefficient is new as a settled bibliographic fact. Use wording such as:

> “A targeted literature search did not locate this coefficient in the general \(n\)-gon setting; the present note is posted publicly without an exhaustive novelty claim.”

If a more complete literature search finds the theorem elsewhere, revise the introduction accordingly rather than hiding the overlap.

## Verification tasks before considering the note finished

1. Symbolically rederive the pairwise quadratic in \(z=\cos d\); do not rely only on the prose derivation.
2. Check the \(m\)-stratum formula.
3. Check the concavity derivative for \(h(x)=\cot(\pi/x)\).
4. Numerically sample the simplex for \(n=3,\dots,12\), including cases with one \(x_i>\pi/2\), and verify \(\Phi_{c_n}\ge -10^{-10}\) up to floating-point error.
5. Verify that increasing \(c_n\) by a small amount makes the \((n-1)\)-stratum negative.
6. Check \(n=3\) gives coefficient \(1\).
7. Check \(n=4\) gives \(1-1/\sqrt3\).
8. Check every equation after converting between the pairwise-defect, variance, and perimeter-deficit forms.
9. Compile LaTeX with no undefined references/citations and fix overfull boxes.
10. Do not silently strengthen the theorem to arbitrary nonconvex polygons unless a separate rigorous reduction is supplied.

## Style

Keep the paper short and elementary. Avoid presenting the proof as a complicated quantitative-stability argument: the point is that the sharp coefficient is obtained by a simple global reduction to cyclic polygons and a two-variable mixing argument.

Use restrained language:
- “we prove,” “we record,” “the argument shows”;
- avoid “breakthrough,” “surprising new theorem,” etc.;
- be explicit about the public-note status and incomplete novelty search.

The final paper should be understandable without reading the old exploratory manuscript.
