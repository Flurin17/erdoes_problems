# Erdos Problem 647 Certificate

Pending explicit `n > 24`.

## Certificate Method

For a proposed integer `n`, write `m = n-k`. The inequality is equivalent to

```text
tau(n-k) <= k+2        for every 1 <= k < n.
```

Let

```text
B = max_{m < n} tau(m).
```

Then for all `k >= B`,

```text
n-k + tau(n-k) <= n-k+B <= n.
```

So a finite certificate only needs to verify shifts

```text
1 <= k <= B-1.
```

The verifier computes `B` independently by enumerating nonincreasing
exponent vectors over consecutive primes. This is exact because any integer
with maximal divisor count below a bound can be replaced by one with larger
exponents on smaller primes without increasing the integer and without
changing its divisor count.

When an explicit candidate is found, this file must be replaced by the
candidate data:

```text
n
B = max_{m<n} tau(m)
witnesses attaining B
factorization of n-k for 1 <= k <= B-1
tau(n-k) for each checked k
max_{m<n}(m+tau(m))
all m attaining the maximum
commands and outputs from two independent verifiers
```
