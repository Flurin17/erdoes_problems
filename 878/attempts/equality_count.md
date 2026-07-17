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

