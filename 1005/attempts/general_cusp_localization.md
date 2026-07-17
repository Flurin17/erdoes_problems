# General rational-cusp route

Fix a reduced (p/q\in(0,1]) and choose (r/s) with (ps-qr=1). Every nearby lattice point has unique coordinates
\[
(a,b)=m(p,q)+k(r,s),
\]
and is primitive exactly when ((m,k)=1). The denominator cap is (mq+ks\le n), angular order is controlled by (m/k), and compatibility is
\[
(p\Delta m+r\Delta k)(q\Delta m+s\Delta k)\ge0. \tag{1}
\]

For a fixed scaled window (m/k\in[An,Bn]), row (k) contributes
\[
\varphi(k)\left(\min\left(B,\frac1{qk}\right)-A\right)_+n+O_k(1). \tag{2}
\]
Thus bounded transverse layers at a denominator-(q) cusp have a density scaled by (1/q). A direct unsafe-layer analysis of (1) starts at transverse gap (p+q); it gives a density strictly below (1) for every fixed cusp (q\ge2). The upper cusp (1/1) is exceptional and is exactly the four-defect model.

The unresolved localization issue is uniformity when the best rational cusp denominator and the number of transverse layers both grow with (n). Neither complement symmetry nor a fixed (SL_2(\mathbb Z)) chart removes this issue: complement does not preserve the compatibility cone.

## Refuted shortcut

It is false that a side whose Stern--Brocot parent denominator tends to infinity necessarily has (o(n)) points. Let (n=q^2), (P=(q-1,q)), and take the parent (R=(q-2,q-1)). The Farey interval from (P+R) to (P) is admissible, has (P) as its unique minimum-denominator point, and contains (sum_{t\le q/3}\varphi(t)=\Theta(n)) points even though the parent denominator is (q-1\to\infty). This kills the naive minimum-denominator localization step; any global proof must also bound such growing-denominator cusp fans quantitatively.
