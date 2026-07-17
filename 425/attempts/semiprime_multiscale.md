# Route: weighted semiprime graphs

## Result proved

PROOF.md proves
\[
 \liminf\frac{F(n)-\pi(n)}
 {n^{3/4}(\log n)^{-3/2}}
 \ge c_0,\qquad c_0=2^{11/4}/3^{3/4}.
\]
The coefficient is the exact optimum for disjoint reciprocal interval
components constructed from rectangular projective-plane incidence graphs.

## Current global bottleneck

This interval optimum is not yet the optimum over all \(C_4\)-free graphs
supported by \(pq\le n\).  Aggregate two-path inequalities allow a strictly
larger fractional profile.

Using two consecutive Bellman blocks with normalized masses
\[
 x=1/\sqrt{18},\quad y=\sqrt{3/2},\quad
 z\approx0.10439,\quad w\approx3.34606,
\]
the diagonal construction contributes \(x\sqrt y+z\sqrt w\).  A hypothetical
coupling of \(X_2\) to \(Y_1\cup Y_2\) would contribute
\[
 x\sqrt y+z\sqrt{y+w},
\]
raising the Problem-425 coefficient by about \(0.091\).

All ordinary codegree constraints have slack except the homogeneous pair
constraints.  A finite stability calculation gives, with
\(s=e(X_1,Y_1)\), \(t=e(X_2,Y_1)\), \(T=e(X_2,Y_1\cup Y_2)\),
\[
 \frac{st}{|Y_1|}
 \le |X_1||X_2|+\sqrt{\Delta_1\Delta_2},
\]
where
\[
 \Delta_1=|X_1|(|X_1|-1)+s-s^2/|Y_1|,
\quad
 \Delta_2=|X_2|(|X_2|-1)+T-T^2/(|Y_1|+|Y_2|).
\]
At the proposed profile this is far from obstructing the coupling.

## Algebraic routes eliminated

The desired two-level coupling cannot arise from any of the following
standard templates.

1. A single affine/projective plane trace: the exact line-intersection
   variance leaves only \(O(q)\), rather than \(\Theta(q^2)\), lines with the
   required dense trace.
2. A proper subplane or subfield: a proper subplane of order \(r\) in a plane
   of order \(q\) requires \(q\ge r^2\), whereas both orders here are
   proportional.
3. A Latin subsquare or transversal-design subdesign: a proper Latin
   subsquare forces \(q\ge2r\), but the required ratio is \(q/r<2\).
4. Parallel-class extension: pairwise-intersection constraints force
   \(\Theta(Q^3)\) new points rather than the available \(\Theta(Q^2)\).
5. Translation/Sidon constructions: disjoint difference budgets recover
   only the separate-block coefficient.
6. Random embedding: a positive fraction of mixed pairs have codegree at
   least two, and repairing them loses \(\Theta(Q^3)\) incidences.

## Falsification computation

For \(U=Q^2\), solve the exact \(C_4\)-free four-part problem on allowed
blocks
\[
 X_1Y_1,\quad X_2Y_1,\quad X_2Y_2
\]
with part sizes nearest \(Ux,Uz,Uy,Uw\).  Determine whether the optimum divided
by \(Q^3\) approaches the diagonal or the coupled fractional value.  This is
the first computational obligation for the lower route.

## Next proof obligation

Either construct a genuinely distributed mixed orthogonal array attaining
the coupled value, or prove a higher-order packing inequality not implied by
two-path/codegree constraints.
