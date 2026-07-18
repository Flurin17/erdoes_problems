# Route: counting `f(n)=F(n)`

If `1` is admissible, `F_unit(n)=F_{>1}(n)+1>f(n)` for every `n`; the
counting function is exactly zero.

Under the nonunit convention, the exact criterion is

`f(n)=F(n)` iff
`M_n(B)<=sum_{p in B}p^{floor(log_p n)}` for every `B subset P(n)`. (1)

## Classified small supports

- `n=1` and one-prime support always have equality.
- For `P(n)={p,q}`, `F(n)=max(n,f(n))`.
- For three primes, with singleton values `A_s` and two-prime exact-support
  maxima `Q_st`,
  `F=max(f,n,Q_pq+A_r,Q_pr+A_q,Q_qr+A_p)`.
- For squarefree `n=pq`, `p<q`, `h=floor(log_p q)`, equality is exactly
  `q<=p^{h+1}/(p-1)`.

The last condition gives log-periodic prime-counting profiles for fixed `p`,
not a constant global density.

## Obstructions and open tail

At `n=120`, `f(n)>n` but a pair block improves it.  At `n=3689`, all pair
tests pass but the full block fails.  At `n=78690`, no pair improves but the
block `{3,43,61}` does.  Thus bounded block tests do not characterize equality.

The full nonunit asymptotic remains open locally.  A largest-prime
decomposition `n=mP` reduces fixed `m` to finitely many phase conditions, but
requires a uniform tail theorem for large cores `m` and for
`P^+(n)<=sqrt(n)`.  No such theorem is proved.  Restricted small-support
asymptotics cannot be promoted to the requested full count without it.

## Resonant spikes rule out a constant `x/log x` asymptotic

Let `E(x)=#{n<x:f(n)=F(n)}` under the nonunit convention.  There is an
unbounded sequence of `x` for which

`E(x) >> x log_3 x/log x`.                                      (4)

Proof.  Fix a small `a>0`, and for `p|m` put
`d_p(m)=p^{floor(log_p m)}`.  Call `m<=z` safe when

`d_p(m)<=e^{-a}m` for every `p|m`.

For fixed `p`, unsafe multiples lie in the intervals
`[p^k,e^a p^k)`.  Their harmonic mass is at most

`1/p + a log z/(p log p)+1/(p(p-1))`.

Since `sum_p1/(p log p)<infinity`, choose `a` so small that summing these
bounds leaves

`sum_{m<=z, m safe}1/m >> log z`.                               (5)

Use simultaneous Dirichlet approximation to choose a log-height `T_0` whose
distance from a multiple of `log p` is at most `a/8` for every `p<=z`.
This may be done with

`log T_0=O(z log log z/log z)`.

On a fixed one-sided slab immediately after `T_0`, every `p<=z` satisfies

`p^{floor(t/log p)}/e^t >= e^{-a/2}>e^{-a}>1/2`.                (6)

For a safe core `m<=z` and a prime `P>m`, put `n=mP` with `log n` in this
slab.  Since `P^2>n`, a block containing `P` and core support `C` has value
`P M_m(C)`.  If `|C|=1`, safety and (6) dominate it; if `|C|>=2`, the two
corresponding singleton weights already sum to more than `n`.  Core-only
blocks of size at least two are handled in the same way.  Hence every subset
inequality holds and `f(n)=F(n)`.

For each safe `m`, PNT counts `>>x/(m log x)` eligible outer primes in the
slab; the representations are disjoint because `P` is the unique largest
prime.  Summing (5) gives `E(x)>>x log z/log x`.  The bound on `T_0` implies
`log_3 x<=log z+O(1)`, proving (4).

Consequently

`limsup_{x->infinity} E(x)log x/x=infinity`.                    (7)

Thus no asymptotic `E(x)~C x/log x` with fixed finite `C` is possible.  The
same construction survives after excluding every fixed set of cores or every
fixed bounded support size; a uniform large-core tail is therefore false,
not merely unproved.  A matching upper envelope or a complete moving-profile
asymptotic remains open.
