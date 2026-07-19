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

## Exact typed-design and graph-packing reduction

It is useful to write \(h=y+w\) and to use \(N\) for the common linear
scale.  The coupled profile is equivalent to a family of blocks on
\(X_1\sqcup X_2\) with
\[
 |X_1|=xN,\quad |X_2|=zN,
\]
\[
 yN\text{ blocks of type }(a\sqrt N,b\sqrt N),\qquad
 wN\text{ blocks of type }(0,b\sqrt N),
\]
where
\[
 a=\frac{x}{\sqrt y},\qquad b=\frac z{\sqrt h}.
\]
Every pair of ground points must occur in at most one block.  The \(X_1\)
and \(X_2\) pair budgets are asymptotically saturated, while the mixed-pair
load is
\[
 \rho=\sqrt{y/h}=0.517638\ldots .
\]

Each marginal design exists with only \(o(N^2)\) uncovered pairs.  Over
\(\mathbb F_q\), choose \(S\subseteq\mathbb F_q\), take points
\((\alpha,\beta)\in S\times\mathbb F_q\), and index blocks by
\((t,u)\in\mathbb F_q^2\), with
\[
 (\alpha,\beta)\in B_{t,u}\quad\Longleftrightarrow\quad
 u=\alpha t+\beta.
\]
Every block has size \(|S|\), and two points of different first coordinate
lie in exactly one common block.  Taking
\[
 q_1^2\sim yN,\quad |S_1|\sim a\sqrt N,
\qquad
 q_2^2\sim hN,\quad |S_2|\sim b\sqrt N
\]
realizes the two saturated same-part profiles.

Thus the only missing condition is a graph packing.  Let \(H_i\) be the
intersection graph of the blocks in the \(i\)-th marginal design.  One must
inject all \(yN\) vertices of \(H_1\) into the \(hN\) vertices of \(H_2\) so
that
\[
 E(\phi(H_1))\cap E(H_2)=\varnothing.                 \tag{GP}
\]
For exact \(2\)-design marginals the leading degrees and edge densities are
\[
 \deg H_1=xN+O(\sqrt N),\quad \frac{\deg H_1}{|H_1|}
   \to\frac xy,
\]
\[
 \deg H_2=zN+O(\sqrt N),\quad \frac{\deg H_2}{|H_2|}
   \to\frac zh.
\]
All immediate capacity tests have large slack; in particular
\[
 \frac xy+\frac zh=0.21529\ldots<1.
\]
Weighted rank/frame-potential inequalities, local pencil bounds, and the
known spectra of the marginal block graphs also leave a fixed positive
margin.  Consequently (GP), not a marginal design or pair-count issue, is the
precise construction bottleneck.

There is an equivalent lift formulation.  For a finite group \(\Gamma\),
assign a difference set \(S_{ur}\subseteq\Gamma\) to every macro incidence
and lift by
\[
 (u,g)\sim(r,h)\quad\Longleftrightarrow\quad h-g\in S_{ur}.
\]
The lift is \(C_4\)-free exactly when, for every ordered macro pair \(u,v\),
the cross-difference multisets
\[
 S_{ur}-S_{vr}
\]
are internally simple and mutually disjoint as \(r\) varies (with zero
omitted for \(u=v\)).  The fractional pair inequalities record only the
cardinality conditions for this typed strong difference family; they do not
construct it.

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

More precisely, in the \(N\)-scale notation, independent random blocks have
same-part pair codegrees tending to \(\operatorname{Pois}(1)\) and mixed
codegrees tending to \(\operatorname{Pois}(\rho)\).  The expected excess
\((C-1)_+\) is \(1/e\) in the saturated classes and
\(\rho-1+e^{-\rho}>0\) in the mixed class.  Hence deletion-only repair loses
\(\Theta(N)\) blocks, or \(\Theta(N^{3/2})\) incidences: a nonvanishing
fraction of the desired contribution.

The obstruction to the usual affine subnet is particularly sharp.  The
marginal field orders have ratio
\[
 q_1/q_2=\rho>1/2.
\]
After two source parallel classes are embedded direction-by-direction, their
carrier is an \(A\times B\) grid with \(|A|=|B|=q_1\).  Every line of a third
ambient direction meets that grid because \(2q_1>q_2\), so the class would
need all \(q_2\), rather than \(q_1\), ambient lines.  This rules out the
standard direction-preserving affine/subnet ansatz, but not a nonlinear
packing satisfying (GP).

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

Either construct the typed strong difference family (equivalently, solve
(GP)) attaining the coupled value, or prove a higher-order packing
inequality not implied by two-path, rank, spectral, or codegree constraints.
