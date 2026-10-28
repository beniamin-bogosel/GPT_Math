#!/usr/bin/env python3
"""Supplementary symbolic and numerical checks; these do not replace the proof.

Run from any directory: python3 Results/QuantitativeIsoperimetric/verify.py
"""

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def symbolic_checks():
    p, d, z, r, u0, b0, c, n, tau = sp.symbols(
        "p d z r u0 b0 c n tau", real=True
    )
    x, y = p / 2 + d, p / 2 - d
    identities = [
        sp.sin(x) + sp.sin(y) - 2 * sp.sin(p / 2) * sp.cos(d),
        sp.sin(x) ** 2 + sp.sin(y) ** 2
        - (1 - sp.cos(p) * (2 * sp.cos(d) ** 2 - 1)),
        sp.sin(x) * sp.cos(x) + sp.sin(y) * sp.cos(y)
        - sp.sin(p) * (2 * sp.cos(d) ** 2 - 1),
    ]
    for residual in identities:
        require(sp.trigsimp(sp.expand_trig(residual)) == 0, "pair identity")

    # u0 and b0 are the contributions of the other coordinates to U and B.
    pair_phi = (
        c * (r + 2 * sp.sin(p / 2) * z) ** 2
        - (n * c - 1) * (u0 + 1 - sp.cos(p) * (2 * z**2 - 1))
        - tau * (b0 + sp.sin(p) * (2 * z**2 - 1))
    )
    poly = sp.Poly(sp.expand(pair_phi), z)
    alpha = 4 * c * sp.sin(p / 2) ** 2 + 2 * (n * c - 1) * sp.cos(p)
    alpha -= 2 * tau * sp.sin(p)
    beta = 4 * c * r * sp.sin(p / 2)
    require(sp.simplify(poly.coeff_monomial(z**2) - alpha) == 0, "alpha")
    require(sp.simplify(poly.coeff_monomial(z) - beta) == 0, "beta")
    require(poly.degree() == 2, "quadratic degree")

    m, s, q = sp.symbols("m s q", nonzero=True, real=True)
    stratum = c * (m * s) ** 2 - (n * c - 1) * m * s**2 - tau * m * s * q
    expected = m * s**2 * (1 - c * (n - m) - tau * q / s)
    require(sp.expand(stratum - expected) == 0, "stratum evaluation")

    t = sp.symbols("t", positive=True)
    u = sp.pi / t
    h = sp.cot(u)
    h_second = -2 * u**3 / (sp.pi**2 * sp.sin(u) ** 2) * (1 - u * sp.cot(u))
    require(sp.simplify(sp.diff(h, t, 2) - h_second) == 0, "h second derivative")

    # Check all changes of normalization without specializing the side lengths.
    Q, L, A = sp.symbols("Q L A", real=True)
    D = n * Q - L**2
    delta = L**2 - 4 * n * tau * A
    residual = n * (Q - 4 * tau * A - c * D) - (delta - (n * c - 1) * D)
    require(sp.expand(residual) == 0, "deficit conversion")
    require(sp.expand(n * (Q - L**2 / n) - D) == 0, "D equals n V")

    gamma, k = sp.symbols("gamma k", positive=True)
    side_constant = 1 / (n**2 * gamma)
    radial_constant = (1 + n**2 * side_constant) / (8 * n**2 * k)
    joint_constant = 1 / (n**2 * gamma) + (1 + 1 / gamma) / (8 * n**2 * k)
    require(sp.simplify(side_constant + radial_constant - joint_constant) == 0,
            "joint side and radial constant")
    gain, delta_convex = sp.symbols("gain delta_convex", nonnegative=True)
    delta_original = delta_convex + 4 * n * tau * gain
    require(sp.simplify(delta_original / (4 * n * tau) - gain
                        - delta_convex / (4 * n * tau)) == 0,
            "convexification deficit decomposition")

    T = sp.symbols("T")
    c4 = 1 - 1 / sp.sqrt(3)
    quad_area = (Q - c4 * (3 * Q - 2 * T)) / 4
    published_area = T / (3 + sp.sqrt(3)) - Q / (2 * (sp.sqrt(3) + 1) ** 2)
    require(sp.simplify(quad_area - published_area) == 0, "2018 quadrilateral form")

    # t=1/n. Remove the first two orders before extracting the leading coefficient.
    gamma = 1 / t - 1 - sp.tan(sp.pi * t) / (t * sp.tan(sp.pi * t / (1 - t)))
    expansion = sp.series(gamma, t, 0, 4).removeO().expand()
    expected_series = 2 * sp.pi**2 * t**2 / 3 + sp.pi**2 * t**3 / 3
    require(sp.simplify(expansion - expected_series) == 0, "gamma asymptotics")
    return {
        "pair_quadratic": "passed",
        "stratum_formula": "passed",
        "concavity_derivative": "passed",
        "deficit_and_variance_conversions": "passed",
        "joint_stability_and_convexification_constants": "passed",
        "published_quadrilateral_equivalence": "passed",
        "gamma_expansion": "2*pi**2/(3*n**2) + pi**2/(3*n**3) + O(n**-4)",
    }


def constants(n):
    tau = np.tan(np.pi / n)
    c = 1.0 if n == 3 else 1 - tau / np.tan(np.pi / (n - 1))
    return tau, c, n * c - 1


def phi(angles, n, coefficient=None):
    tau, c, _ = constants(n)
    if coefficient is not None:
        c = coefficient
    sine = np.sin(angles)
    S = sine.sum(axis=-1)
    U = (sine**2).sum(axis=-1)
    B = (sine * np.cos(angles)).sum(axis=-1)
    return c * S**2 - (n * c - 1) * U - tau * B


def geometry_checks(angles, n):
    # Independently recover chord lengths and signed area from vertex coordinates.
    theta = np.concatenate((np.zeros((len(angles), 1)), 2 * np.cumsum(angles[:, :-1], axis=1)), axis=1)
    vertices = np.stack((np.cos(theta), np.sin(theta)), axis=-1)
    following = np.roll(vertices, -1, axis=1)
    sides = np.linalg.norm(following - vertices, axis=-1)
    area = (vertices[..., 0] * following[..., 1] - vertices[..., 1] * following[..., 0]).sum(axis=1) / 2
    require(np.allclose(sides, 2 * np.sin(angles), atol=2e-13, rtol=0), "chord geometry")
    formula_area = (np.sin(angles) * np.cos(angles)).sum(axis=1)
    require(np.allclose(area, formula_area, atol=2e-13, rtol=0), "shoelace area")
    tau, c, gamma = constants(n)
    # Compute the defect by pairwise differences, independently of n Q - L^2.
    defect = np.zeros(len(angles))
    for i in range(n):
        for j in range(i):
            defect += (sides[:, i] - sides[:, j]) ** 2
    residual = (sides**2).sum(axis=1) - 4 * tau * area - c * defect
    deficit_residual = sides.sum(axis=1) ** 2 - 4 * n * tau * area - gamma * defect
    require(np.allclose(residual, 4 * phi(angles, n), atol=2e-12, rtol=0), "geometric reduction")
    require(np.allclose(n * residual, deficit_residual, atol=3e-11, rtol=0), "geometric deficit conversion")
    require(float(residual.min()) >= -1e-10, "geometric inequality")

    # Check the classical radial inequality and its combination with our bound.
    # A noncircular affine image also tests noncyclic convex polygons.
    for transform in (np.eye(2), np.array([[2.0, 0.4], [0.0, 0.6]])):
        points = vertices @ transform.T
        following = np.roll(points, -1, axis=1)
        lengths = np.linalg.norm(following - points, axis=-1)
        areas = (points[..., 0] * following[..., 1]
                 - points[..., 1] * following[..., 0]).sum(axis=1) / 2
        delta = lengths.sum(axis=1) ** 2 - 4 * n * tau * areas
        side_variance = lengths.var(axis=1)
        radii = np.linalg.norm(points - points.mean(axis=1, keepdims=True), axis=-1)
        radial_variance = radii.var(axis=1)
        k = np.sin(np.pi / n) ** 2
        classical_residual = delta + n**2 * side_variance - 8 * n**2 * k * radial_variance
        require(float(classical_residual.min()) >= -1e-10, "classical radial inequality")
        joint_constant = 1 / (n**2 * gamma) + (1 + 1 / gamma) / (8 * n**2 * k)
        joint_residual = joint_constant * delta - side_variance - radial_variance
        require(float(joint_residual.min()) >= -1e-10, "joint stability inequality")


def numerical_checks(samples, seed):
    rng = np.random.default_rng(seed)
    report = []
    for n in range(3, 13):
        tau, c, gamma = constants(n)
        require(c > 0 and gamma > 0, "positive constants")
        require(abs(c - 1) < 1e-15 if n == 3 else True, "triangle constant")
        if n == 4:
            require(abs(c - (1 - 1 / np.sqrt(3))) < 1e-15, "quadrilateral constant")
        batches = [np.pi * rng.dirichlet(np.full(n, alpha), size=samples)
                   for alpha in (0.2, 1.0, 5.0)]
        # Force the first gap above pi/2, including gaps very close to pi.
        large = rng.uniform(np.pi / 2 + 1e-9, np.pi - 1e-6, size=samples)
        rest = rng.dirichlet(np.ones(n - 1), size=samples) * (np.pi - large[:, None])
        batches.append(np.column_stack((large, rest)))
        angles = np.concatenate(batches)
        residual = phi(angles, n)
        require(np.isfinite(residual).all(), "finite residuals")
        require(float(residual.min()) >= -1e-10, f"simplex inequality, n={n}")
        geometry_checks(np.concatenate((angles[:500], batches[-1][:500])), n)

        # Include every equal-positive boundary configuration and regular equality.
        for m in range(1, n + 1):
            point = np.zeros(n)
            point[:m] = np.pi / m
            expected = 0.0 if m == 1 else m * np.sin(np.pi / m) ** 2 * (
                1 - c * (n - m) - tau / np.tan(np.pi / m)
            )
            require(abs(float(phi(point, n)) - expected) < 1e-12, "boundary formula")
            require(float(phi(point, n)) >= -1e-12, "boundary sign")
        regular = np.full(n, np.pi / n)
        require(abs(float(phi(regular, n))) < 1e-12, "regular equality")

        increment = 1e-4
        boundary = np.zeros(n)
        boundary[: n - 1] = np.pi / (n - 1)
        bad_boundary = float(phi(boundary, n, c + increment))
        require(bad_boundary < -1e-8, "larger coefficient fails on boundary")
        epsilon = 1e-10
        interior = np.full(n, (np.pi - epsilon) / (n - 1))
        interior[-1] = epsilon
        bad_interior = float(phi(interior, n, c + increment))
        require(bad_interior < -1e-8, "larger coefficient fails at positive angles")
        require(float(phi(interior, n)) >= -1e-10, "sharp sequence sign")
        sine = np.sin(interior)
        ratio = ((sine**2).sum() - tau * (sine * np.cos(interior)).sum())
        ratio /= n * (sine**2).sum() - sine.sum() ** 2
        require(abs(float(ratio) - c) < 1e-7, "sharp coefficient limit")

        report.append({
            "n": n,
            "c_n": float(c),
            "gamma_n": float(gamma),
            "samples": len(angles),
            "outside_circumcenter_samples": int((angles.max(axis=1) > np.pi / 2).sum()),
            "minimum_phi": float(residual.min()),
            "phi_with_coefficient_increased_by_0.0001": bad_interior,
        })
    return report


def high_precision_checks():
    with mp.workdps(80):
        target = 3 / (2 * mp.pi**2)
        errors = []
        for n in (100, 1000, 10000):
            gamma = n - 1 - n * mp.tan(mp.pi / n) / mp.tan(mp.pi / (n - 1))
            value = 1 / (n * n * gamma)
            error = abs(value - target)
            errors.append(error)
        require(errors[2] < errors[1] < errors[0], "variance asymptotic convergence")
        require(errors[-1] < mp.mpf("0.00001"), "variance asymptotic limit")
        return {"precision_decimal_digits": 80,
                "normalized_variance_limit": str(+target),
                "coefficient_at_n_10000": str(+value)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=10000,
                        help="samples per distribution per n (four distributions)")
    parser.add_argument("--seed", type=int, default=20261028)
    parser.add_argument("--output", type=Path, help="optional JSON report")
    args = parser.parse_args()
    require(args.samples > 0, "sample count must be positive")
    result = {
        "status": "passed",
        "seed": args.seed,
        "versions": {"numpy": np.__version__, "sympy": sp.__version__, "mpmath": mp.__version__},
        "symbolic": symbolic_checks(),
        "numerical": numerical_checks(args.samples, args.seed),
        "asymptotic": high_precision_checks(),
    }
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
