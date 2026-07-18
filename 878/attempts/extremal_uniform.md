# Uniform extremal construction for `f`

This file proves

`max_{n<=x} f(n) ~ x log x/log log x`.

All logarithms are natural and `e(t)=exp(2*pi*i*t)`.  The analytic inputs are
the prime number theorem, Vaughan's identity, the standard second-derivative
estimate for one-dimensional exponential sums, and Vaaler's trigonometric
minorant for an interval.

## 1. A uniform nonlinear prime exponential sum

Let `T -> infinity`, `L=log T`, choose a sufficiently large fixed `A`, and put

`Y=T L^A`, `R=L^(A+2)`.

**Lemma.**  Uniformly for integers `1<=|h|<=R`,

`S_h=sum_{Y<n<=2Y} Lambda(n)e(hT/log n)
     <<_A Y^(35/36)(log Y)^C`.                                  (1)

Here and below `C` is an absolute constant which may change.

Proof.  Apply Vaughan's identity with `U=V=Y^(1/6)`.  The first two pieces
are Type I sums whose combined outer variable is at most `UV=Y^(1/3)`.
On `m~M`, `n~N=Y/M`, set

`Phi=hT/(log Y)^2`.

The second derivative with respect to `n` of `hT/log(mn)` has fixed sign and
magnitude comparable with `Phi/N^2`.  The second-derivative estimate gives

`sum_{n~N}e(hT/log(mn)) << sqrt(Phi)+N/sqrt(Phi)`.

Since `Y/L^(A+2) << Phi << Y`, summing the divisor-bounded outer
coefficients gives `O(Y^(5/6)(log Y)^C)`.

The remaining Type II blocks have `MN~Y` and, after interchanging the two
variables if needed,

`Y^(1/6)<=M<=Y^(1/2)<=N`.

Their coefficient sequences have divisor-bounded `L^2` norms.  Cauchy in
the `M`-variable followed by the standard `H`-shift inequality in the
`N`-variable reduces the off-diagonal correlations to unweighted sums over
`m~M` with phase

`g(m)=hT/log(m(n+r))-hT/log(mn)`, `1<=r<=H`.

Writing

`lambda=|h|T/[Y(log Y)^3]`,

direct differentiation gives a fixed sign and

`|g''(m)| asymp lambda*r/M`.

The second-derivative estimate, summed over shifts, yields

`|B|/Y << (log Y)^C [H^(-1/2)
 +(lambda H/M)^(1/4)+(lambda H M)^(-1/4)]`.                     (2)

Take `H=floor((M/lambda)^(1/3))`.  Since
`L^(-A-3)<<lambda<<L^(-1)` and `M>=Y^(1/6)`, this choice satisfies
`1<=H<=M<=N`; every term in (2) is
`O(Y^(-1/36)(log Y)^C)`.  This proves (1).

For completeness, the exact Vaughan decomposition used for `n>V` is

`Lambda=mu_{<=U}*log-mu_{<=U}*Lambda_{<=V}*1
        +mu_{>U}*Lambda_{>V}*1`.

The first two convolutions have the stated Type I range.  In the last one,
both grouped variables exceed `Y^(1/6)` and the grouped coefficients have
the required divisor-type second moments.

## 2. Extracting many aligned primes

Put `d=L^(-A)` and let `I=[d,3d]` on `R/Z`.  Vaaler's minorant of degree
`R` has constant coefficient `2d+O(1/R)` and nonzero coefficients
`O(min(d,1/|h|)+1/R)`.  Apply it to `{T/log n}`.  The prime number theorem
and (1) give

`sum_{Y<p<=2Y, {T/log p} in I} log p = (2+o(1))T`.              (3)

Indeed, the constant-term error is `O(Y/R)=O(T/L^2)`, and the Fourier error
is at most `O(log R)*max_{h<=R}|S_h|=o(T)`.  Prime powers with exponent at
least two contribute `O(sqrt(Y)(log Y)^2)=o(T)`, so (3) is a statement about
primes.

In particular, the aligned set contains more than

`(2-o(1))T/log(2Y)`                                                (4)

distinct primes.

## 3. Product padding without changing the exponent floors

Now let `x -> infinity`, take `T=log x`, and retain the notation above.  Put

`s=2A log L`,
`K=floor((T-s)/log(2Y))=(1-o(1))T/L`.

Choose any `K` aligned primes and let `Q` be their product.  Then

`Q<=(2Y)^K<=e^(T-s)=x L^(-2A)`.

Set `n=Q floor(x/Q)`.  Thus `n` is a positive integer at most `x`, every
selected prime divides `n`, and

`n/x >=1-L^(-2A)`.                                               (5)

For a selected prime `p`, put `m=floor(T/log p)`.  From the alignment,

`x exp(-3d log(2Y)) <= p^m <= x exp(-d log Y)`.                 (6)

Since `d log Y=(1+o(1))L^(1-A)` whereas the loss in (5) is
`L^(-2A)`, the upper bound in (6) is strictly below `n` for large `x`.
Also `p^(m+1)>x>=n`.  Hence

`floor(log_p n)=m`,

and (6) gives

`p^floor(log_p n) >= x exp(-O(L^(1-A)))=(1-o(1))x`.

Summing over the `K` selected primes,

`f(n)>=(1-o(1))Kx
      =(1-o(1))x log x/log log x`.                              (7)

## 4. Matching upper bound

For every `n<=x`,

`f(n)<=n omega(n)<=x max_{m<=x}omega(m)`.

If `P_k` is the product of the first `k` primes, the maximum on the right is
the largest `k` with `P_k<=x`.  The PNT gives

`max_{m<=x}omega(m)~log x/log log x`.

Together with (7), this proves the claimed asymptotic uniformly for real
`x -> infinity`.

## Falsification points

The Type II proof must use a second- (or higher-) derivative estimate on the
correlation phase; a first-derivative estimate is invalid because its slope
may approach an integer.  The second Vaughan term must be included in the
Type I range up to `UV`.  Finally, the interval `I` must stay a positive
distance `d` from zero; that margin is exactly what protects the exponent
floor after padding.
