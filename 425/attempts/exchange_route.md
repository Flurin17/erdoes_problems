# Route: extremal exchange and missing-prime charging

Choose an extremal set \(A\) that contains as many primes as possible.

## Exact one-prime blocker

For a missing prime \(p\), adjoining \(p\) creates a collision exactly when
there are pairwise distinct old elements
\[
 kp,\ d,\ kd\in A,\qquad k\ge2,
\]
because
\[
 p(kd)=(kp)d.
\]
Replacing \(x\in A\) by \(p\) is safe exactly when \(x\) meets every such
witness.

A prime-maximal extremizer therefore has at least two distinct witness
multipliers for every missing prime.  In particular, every prime \(p>n/3\)
belongs to \(A\).

## Exact simultaneous exchange

For a set \(Q\) of missing primes, \((A\setminus X)\cup Q\) is admissible if
and only if \(X\) hits all old blockers of the three forms
\[
 \{kq,d,kd\},\qquad \{kq,kr\},\qquad \{1,qr\},
\]
where \(q,r\in Q\) are distinct and \(k\ge2\).

The first form is the one-prime blocker.  A collision with one new prime on
each side reduces to \(q(kr)=r(kq)\), giving the second.  A pair of new
primes colliding with an old pair reduces to \(qr=1\cdot qr\), giving the
third.  Unique factorization excludes all other distributions.

If a transversal of these blockers had size at most \(|Q|\), the exchange
would enlarge \(A\), or preserve its size while increasing its prime count.
Thus every nonempty \(Q\) has composite transversal number at least
\(|Q|+1\).  This yields a strict-Hall missing-prime/composite graph and an
exact matching ledger:
\[
 \#\{\text{unmatched nonprimes}\}=|A|-\pi(n).
\]

## Ratio lemma

For fixed \(k\ge2\), put
\[
 D_k=\{d:d,kd\in A\}.
\]
Then \(|D_k|\le2\); if two elements occur, one equals \(k\) times the other.
Otherwise \(d(ke)=e(kd)\) is a nontrivial collision.

## Quantitative consequences

If \(n/(T+1)>T\), witness-multiplier pairs inject, giving
\[
 \#\{q>n/(T+1):q\notin A\}\le\binom{T-1}{2}.
\]
The large-prime tail charge and the rough-semiprime dyadic graph both have
target-order net excess after missing prime factors are subtracted.

## Exact obstruction

Individual insertability does not tensor:
\[
 A=\{2p,2q\}
\]
allows \(p\) or \(q\) separately, but not both, since
\(p(2q)=q(2p)\).  Likewise \(A=\{1,pq\}\) forces the third blocker form.
The missing-prime two-core is real; exchange must be combined with the
arithmetic colored-kernel route rather than used as a stand-alone proof.
