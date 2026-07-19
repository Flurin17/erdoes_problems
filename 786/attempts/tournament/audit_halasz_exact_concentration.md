# Audit: exact Halasz concentration

## Verdict

The claimed finite, uniform exact-fibre bound is consistent with the
standard Halasz concentration theorem for real additive functions:
\[
 {1\over x}\sup_t\#\{n\le x:f(n)=t\}
 \ll (1+H)^{-1/2},\qquad
 H=\sum_{\substack{p\le x\\f(p)\ne0}}{1\over p}.       \tag{1}
\]
The interval theorem must retain the correctly scaled logarithmic drift.

## Correct drift formula

For
\[
 Q_h(f;x)={1\over x}\sup_u\#\{n\le x:u<f(n)\le u+h\},
\]
the standard form (up to absolute normalizations) is
\[
 Q_h(f;x)\ll(1+E_h)^{-1/2},                             \tag{2}
\]
where
\[
 E_h=\inf_{\tau\in\mathbb R}\left\{
 (\tau/h)^2+\sum_{p\le x}{1\over p}
 \min\left(1,\left|{f(p)-\tau\log p\over h}\right|^2\right)
 \right\}.                                             \tag{3}
\]
Equivalently, with \(\lambda=\tau/h\),
\[
 E_h=\inf_{\lambda\in\mathbb R}\left\{
 \lambda^2+\sum_{p\le x}{1\over p}
 \min\left(1,\left|{f(p)\over h}-\lambda\log p\right|^2\right)
 \right\}.                                             \tag{4}
\]
Thus (3) requires the penalty \((\tau/h)^2\), not \(\tau^2\).

The naive interval analogue is false.  For \(f(n)=\log n\) and \(h=1\),
the interval \((\log x-1,\log x]\) contains all \(x/e<n\le x\), whence
\[
 Q_1(f;x)\ge1-e^{-1}+o(1),                              \tag{5}
\]
despite \(\sum_{p\le x}1/p\to\infty\).  Formula (3) correctly permits
this: \(\tau=1\) kills the prime sum and has bounded drift cost.

## Exact finite fibre

Fix \(x,f\), let \(H>0\), and put
\[
 m=\min_{p\le x,\ f(p)\ne0}|f(p)|>0.
\]
Choose
\[
 0<h<{m\over1+\sqrt H\log x}.                          \tag{6}
\]
Then \(E_h=H\).  Indeed, \(\lambda=0\) gives \(E_h\le H\).  If
\(\lambda^2\ge H\), the drift cost is at least \(H\).  Otherwise
\(|\lambda|<\sqrt H\), and for every active prime
\[
 \left|{f(p)\over h}-\lambda\log p\right|
 \ge {m\over h}-\sqrt H\log x>1.                       \tag{7}
\]
All active summands saturate, so the prime sum is \(H\).  This proves the
reverse inequality.  For \(H=0\), plainly \(E_h=0\).

The fibre at \(t\) lies in \((t-h,t]\); (2) and (6) prove (1).  This is
finite and uniform, so \(f\) may depend on \(x\), and arbitrarily small
nonzero real weights are allowed.

## Use caveats

* Cite the finite uniform theorem for general additive functions.  A
  fixed-function asymptotic is insufficient for moving \(f_x\).
* A theorem only for strongly additive functions does not immediately
  handle completely additive prime powers.
* The variant denominator \(\sum(1-1/p)/p\) is equivalent up to constants.
