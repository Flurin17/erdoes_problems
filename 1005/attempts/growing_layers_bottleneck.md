# Former growing-layer bottleneck

This file preserves the obstruction that remained after the bounded-defect calculation. With
\[
u=n(1-y),\qquad v=n(1-x),
\]
a tempting fixed-row CRT argument tried to prove $v-u\le2+o(1)$. For moving defects this was nonuniform: the first coprime witness could have period comparable to $\operatorname{lcm}(d,d-2)$. Treating the fixed-row witness as uniform would therefore be invalid.

The final proof does not use that step. It chooses a minimum-denominator point $p/q$ and splits into three regimes:

- bounded $q$: signed cusp layers give at most $n+o(n)$;
- $q\to\infty$, $q=o(n)$: audited primitive-density packing gives at most $(6/\pi^2+o(1))n$;
- $q/n\to\alpha>0$: the finite cusp envelope gives at most $(16/15+o(1))n$.

Thus the historical bottleneck is resolved in `PROOF.md` while its first exact obstruction is preserved here.
