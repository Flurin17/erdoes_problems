# Route: the maximal order of `f`

## Proven upper bound

Let `W(x)=max_{n<=x}omega(n)`.  If `P_k` is the product of the first `k`
primes, then `W(x)=max{k:P_k<=x}`.  The standard PNT consequences
`log P_k~k log k` give `W(x)~log x/log log x`.  Since every summand of
`f(n)` is at most `n`, uniformly for `n<=x`,

`max_{n<=x}f(n)<=(1+o(1))x log x/log log x`.                    (1)

## Proven sharp limsup lower bound

Let `A->infinity`, `eta=1/log A`, and `P=4A(log A)^2`.  For real `t` put

`C(t)=#{p<=P: eta^2<=t-m log p<=eta for some integer m>=1}`.

Averaging over `A<=t<=2A`, and using PNT with partial summation, gives

`(1/A)int_A^{2A}C(t)dt=(4+o(1))A/log A`.                        (2)

Choose a `t` with more than `(3+o(1))A/log A` candidates, put
`s=log(4/eta^2)`, and let
`k=floor((t-s)/log P)=(1-o(1))t/log t`.  For any `k` candidates let `Q`
be their product and set `n=Q floor(e^t/Q)`.  Then
`Q<=P^k<=e^{t-s}` and `n>e^{t-eta^2/2}`.  For every selected `p`,
`eta^2<=t-m log p<=eta` implies `p^m<n<p^{m+1}`, so
`p^{L_p(n)}=p^m>=e^{t-eta}>=e^{-eta}n`.  Hence

`f(n)>=(1-o(1))n log n/log log n`.                              (3)

Together with (1),

`limsup_{x->infinity} max_{n<=x}f(n)/(x log x/log log x)=1`.    (4)

## Full limit: precise open node

The averaging in (2) finds a favorable `t` only somewhere in a long interval.
Even an additive `polylog(t)` loss in `t=log x` is a fatal multiplicative
loss at the cutoff `x`.  The full asymptotic needs a prime-power crowding
statement at every prescribed `T=log x`, producing about `T/log T` aligned
primes while keeping their product below `e^{T-o(1)}`.

A tempting Selberg-integral route would need

`int_X^{2X}|psi(y+h)-psi(y)-h|^2dy << Xh(log X)^2`

for `h=X^{o(1)}` (even polylogarithmic `h`).  Three independent audits agree
that this is not a standard unconditional theorem in the needed range; it is
available under RH.  Conditional on it, root intervals and integer padding do
give the full constant `1`, but this is not an unconditional solution.

Thus the source's full maximal-order asymptotic remains open locally; (1) and
(4) are the strongest proved statements here.

