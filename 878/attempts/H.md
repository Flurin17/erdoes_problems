# Route: the summatory function `H(x)`

## Status

This route proves an explicit oscillatory asymptotic expansion, the bound
`H(x)<<x log_3 x`, and arbitrarily large `x` with `H(x)>>x log_4 x`.  The
proposed uniform upper bound `H(x)<<x log_4 x` remains open locally.

## Exact decomposition

Let `pi_<(y)=#{p prime:p<y}`.  Writing `n=pm` gives

`H(x)=sum_{m>=1} (1/m) sum_{p<x/m}p^{floor(log_p m)}`.            (1)

The part with `floor(log_p m)=0` is
`A_0(x)=sum_{m^2<x}(pi_<(x/m)-pi(m))/m`.                         (2)

For `j>=1`, the part with `p^j<=m<p^{j+1}` is

`A_j(x)=sum_{p^{j+1}<x}p^j sum_{p^j<=m<min(p^{j+1},x/p)}1/m`.   (3)

The harmonic estimate `sum_{a<=m<b}1/m=log(b/a)+O(1/a)` yields

`A_j=sum_{p^{j+1}<x}p^j min(log p,log(x/p^{j+1}))
     +O(pi_<(x^{1/(j+1)}))`.

The total error for `j>=1` is `O(sqrt(x)/log x)` by Chebyshev.

## Explicit oscillatory asymptotic

For `p^2<=x`, put `ell_p=floor(log_p x)`, `theta_p={log_p x}`, and

`M(x)=sum_{p^2<=x} log p * ((p^{ell_p-1}-p)/(p-1)
                            +p^{ell_p-1}theta_p)`.              (4)

Summing the logarithmic main terms extracted from (3) geometrically gives
(4); the accumulated harmonic error is the `O(sqrt(x)/log x)` term above.
When `theta_p=0`, the strict cutoff excludes the terminal block and the theta
term vanishes; when `p^2=x`, the summand is zero.  Also

`A_0(x)=sum_{m<sqrt(x)}pi(x/m)/m+O(sqrt(x))`.                    (5)

Use the standard fixed-order PNT expansion, uniformly for `y>=sqrt(x)`,

`pi(y)=y sum_{k=0}^{N-1} k!/(log y)^{k+1}
       +O_N(y/(log y)^{N+1})`.                                  (PNT_N)

Taylor expansion and
`sum_m (log m)^s/m^2=(-1)^s zeta^{(s)}(2)` give

`H(x)=M(x)+x sum_{r=0}^{N-1} C_r/(log x)^{r+1}
       +O_N(x/(log x)^{N+1})`,                                  (6)

where `C_r=r! sum_{s=0}^r (-1)^s zeta^{(s)}(2)/s!`.  In particular,

`H(x)=M(x)+zeta(2)x/log x+O(x/log^2 x)`.                         (7)

This is pointwise, but its leading oscillatory term need not simplify to a
constant multiple of `x`.

## Phase reduction and upper bounds

Let `u_p=log(x/p^{ell_p})` in `[0,log p)`.  The terminal part of (4) is
`x sum_{p^2<=x}u_p e^{-u_p}/p`, while its completed-block part is `O(x)`.
Thus the proposed upper bound is equivalent, up to `O(x)`, to

`sum_{p^2<=x}u_p e^{-u_p}/p << log_4 x`.                         (8)

The proof in `almost_all_f.md` gives unconditionally
`H(x)<<x(1+log_3 x)`.  A sufficient missing statement is

`sum_{log_2 x<p<(log x)^2}u_p e^{-u_p}/p << log_4 x`.            (9)

The intervals in (9) can be shorter than one; direct Brun--Titchmarsh and
naive large-sieve bounds do not resolve them.

## The quadruple logarithm is necessary

There are arbitrarily large `x` for which `H(x)>>x log_4 x`.    (10)

Fix large `P`.  Simultaneous Dirichlet approximation gives an integer `q`,
at most `Q^{pi(P)}` for `Q=ceil(100P log P)`, such that
`||q/log p||<=1/Q` for every prime `3<=p<=P`.  Multiplying by an integer at
most `P` if necessary makes `q>=P` and keeps errors below
`1/(100 log P)`.  Put `x=exp(q+1)`.  Every listed prime then has terminal
phase in `[0.99,1.01]`, so its terminal block contributes `>>x/p`.  Mertens
gives `H(x)>>x log log P`.  Chebyshev gives `log q<<P`, hence
`log_4 x<=log log P+O(1)`.  An unbounded subsequence proves (10).

Thus the proposed upper bound, if true, is order-sharp; neither `H(x)=O(x)`
nor a constant-linear pointwise asymptotic is possible.

## Dependency graph

- (1)--(5): finite identities, harmonic estimates, and Chebyshev.
- (6): precisely `(PNT_N)` plus convergent logarithmic moments.
- `H<<x log_3 x`: Mertens plus interval Brun--Titchmarsh.
- (10): simultaneous Dirichlet approximation, Mertens, and Chebyshev.
- Open node: (9), an aggregate spacing estimate for medium prime powers.
