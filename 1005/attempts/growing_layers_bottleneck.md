# Growing-layer bottleneck

Use (u=n(1-y),v=n(1-x)) and defect rows as in `bounded_defect_variational.md`. If one could prove uniformly for admissible blocks with (v\to\infty) that
\[
v-u\le2+o(1), \tag{1}
\]
then the subregime (v=o(n)) would close elementarily. Discarding coprimality, row lengths sum to
\[
\begin{aligned}
|B|&\le
\sum_{d\le u} nd\left(\frac1u-\frac1v\right)
+\sum_{u<d\le v}n\left(1-\frac d v\right)+O(v)\\
&\le \frac{v-u}{2}n+O\left(\frac nv+v\right).
\end{aligned}
\]
Thus (1) gives (|B|\le n+o(n)) when (v\to\infty,v=o(n)).

The tempting proof of (1) uses odd rows (d,d-2) and a denominator-offset-one CRT witness. It is valid for each fixed (d), but is not uniform: the first witness in a moving overlap can have a period comparable to (operatorname{lcm}(d,d-2)). Treating (1) as proved without a quantitative short-interval coprime theorem would be an error.

When (v\asymp n), the interval has angular width (O(1/n)) around an interior slope. Fixed rational cusps are controlled by `general_cusp_localization.md`; irrational or drifting rational centers remain the same uniform discrepancy problem in another chart.

This is the first open dependency in the candidate (16/15) upper proof.
