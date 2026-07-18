# Exact modular-jump computation

The forbidden candidates for $p\in(k,2k)$ are exactly the blocks
$[qp+1,qp+k]$.  Starting at $2k+1$, the algorithm chooses a block containing
the cursor with farthest right endpoint, records it, and moves one past that
endpoint.  Every skipped integer is certified forbidden.  When no block
contains the cursor, that cursor is $n_k$.

Termination follows because the first multiple of
$P_k=\prod_{k<p<2k}p$ above $2k$ is admissible.  A certificate consists of a
contiguous chain of witnessed blocks ending immediately before $n_k$, followed
by direct verification that $n_k\bmod p$ is $0$ or greater than $k$ for every
relevant prime.

The implementation is output-sensitive: if the certificate has $C$ blocks
and $r=|\mathcal P_k|$, its direct form takes $O(Cr)$ modular operations after
prime generation.  It gives no asymptotic bound on $C$ or $n_k$.

All certificates for $1\le k\le50$ were checked by a verifier that independently
reconstructs the prime set; fresh direct and forbidden-union scans reproduce
the same values.  The verifier explicitly rejects nonintegral fields and uses
ordinary exceptions rather than `assert`, so optimization cannot disable its
checks.  `math.isqrt` keeps prime generation exact.  The segmented and
modular-jump implementations are independent falsification paths.
