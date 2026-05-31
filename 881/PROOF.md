# Evolving Proof or Counterexample

## Problem

Let \(A\subseteq\mathbb N\) be an asymptotic additive basis of order \(k\)
such that removing any infinite subset of \(A\) destroys the property of
being an order-\(k\) basis. Decide whether there must exist an infinite
\(B\subseteq A\) such that \(A\setminus B\) is an asymptotic additive basis
of order \(k+1\).

## Status

Complete for \(k=1\). Open in this workspace for \(k\ge 2\). No complete
proof or counterexample has been verified yet.

## Reduction 0: The minimality hypothesis is redundant for counterexamples

If \(C\subseteq\mathbb N\) is an asymptotic basis of order \(h\), then it
is also an asymptotic basis of every larger order. Indeed, let
\(c_0=\min C\), and suppose
\[
[N,\infty)\subseteq hC.
\]
Then for every \(n\ge N+c_0\),
\[
n-c_0\in hC,
\]
so
\[
n=c_0+(n-c_0)\in(h+1)C.
\]
Iterating proves monotonicity in the order.

Consequently, if an order-\(k\) basis \(A\) has no infinite
\(B\subset A\) such that \(A\setminus B\) is an order-\((k+1)\) basis, then
for every infinite \(B\subset A\), the set \(A\setminus B\) is not an
order-\(k\) basis. Thus \(A\) is automatically minimal in the sense of the
problem.

Therefore Erdős Problem #881 is equivalent to the following broader
deletion theorem:

> Every asymptotic basis \(A\subseteq\mathbb N\) of order \(k\) contains an
> infinite subset \(B\) such that \(A\setminus B\) is an asymptotic basis of
> order \(k+1\).

Equivalently, every order-\(k\) basis contains a co-infinite subset
\[
C\subset A
\]
which is an order-\((k+1)\) basis.

The original minimality assumption is not available as extra leverage in a
proof by contradiction: assuming that no good infinite deletion exists
already implies it. Conversely, any counterexample to the broader deletion
theorem is automatically a counterexample to the stated problem.

In this language, Corollary 3.1b gives an exact threshold formulation. Let
\(h=k+1\). The broader deletion theorem holds for \(A\) if and only if
there is an increasing sequence
\[
b_1<b_2<\cdots,\qquad b_i\in A,
\]
such that every finite prefix \(F_j=\{b_1,\ldots,b_j\}\) has
\[
A\setminus F_j
\]
as an order-\(h\) basis with some threshold \(N_j<b_j\). The forward
direction is Corollary 3.1b. Conversely, if \(A\setminus B\) is an
order-\(h\) basis with threshold \(N\), enumerate the tail of \(B\) above
\(N\) as \(b_1<b_2<\cdots\). Then
\[
A\setminus F_j\supseteq A\setminus B
\]
for every \(j\), so the same threshold \(N<b_j\) works.

Thus any counterexample to the broader theorem must make late-bad finite
sets an unavoidable barrier, and by Lemma 10.3 each genuine hole in such a
barrier creates a terminal retained gap. It is not enough to have sparse
bases, ordinary essential elements, or isolated one-point witnesses: every
infinite deletion must contain, arbitrarily far out, a finite set \(F\)
whose removal simultaneously blocks all shifted \(k\)-representations of a
witness \(w\), while \(kA\) still covers the stage intervals.

## Theorem 1: The answer is yes for \(k=1\)

Let \(A\subseteq\mathbb N\) be an asymptotic additive basis of order \(1\).
Then \(A\) is cofinite, so there is \(M\) such that
\([M,\infty)\subseteq A\).

Choose an infinite set \(B\subseteq A\) with counting function
\[
B(x)=|B\cap[1,x]|=o(x).
\]
This can be done by taking a sufficiently sparse increasing subsequence of
\(A\). Put \(C=A\setminus B\).

We prove that \(C\) is an asymptotic basis of order \(2\). Let \(n\) be
large, and consider the interval
\[
I_n=[M,n-M]\cap\mathbb N.
\]
For every \(x\in I_n\), both \(x\) and \(n-x\) lie in \(A\). The choices of
\(x\) that fail to give a representation from \(C+C\) are contained in
\[
(B\cap I_n)\cup\{x\in I_n:n-x\in B\}.
\]
There are at most \(2B(n)\) such choices. Since
\[
|I_n|=n-2M+1
\]
and \(B(n)=o(n)\), for all sufficiently large \(n\) we have
\(|I_n|>2B(n)\). Hence some \(x\in I_n\) satisfies
\[
x\notin B,\qquad n-x\notin B.
\]
Then \(x,n-x\in C\), and \(n=x+(n-x)\in 2C\).

Therefore \(C=A\setminus B\) is an asymptotic additive basis of order \(2\),
as required.

The minimality hypothesis for \(k=1\) is automatic: if \(A\) is cofinite and
\(B\subseteq A\) is infinite, then \(A\setminus B\) is not cofinite and so
is not an order-1 asymptotic basis.

## Lemma 2: One-hit absorption criterion

Let \(A\) be an order-\(k\) asymptotic basis, let \(B\subseteq A\), and set
\(C=A\setminus B\). Suppose there is \(t\in C\) such that:

1. for all sufficiently large \(m\), there is a representation
   \(m=a_1+\cdots+a_k\) with \(a_i\in A\) and with at most one of the
   \(a_i\) lying in \(B\);
2. for every \(b\in B\), \(b+t\in 2C\).

Then \(C\) is an order-\(k+1\) asymptotic basis.

Proof. Let \(n\) be sufficiently large that \(m=n-t\) has a representation
as in condition 1. If that representation uses no element of \(B\), then
\[
n=t+a_1+\cdots+a_k\in (k+1)C.
\]
If it uses exactly one element \(b\in B\), then by condition 2 write
\[
b+t=c_1+c_2,\qquad c_1,c_2\in C.
\]
Replacing \(b+t\) by \(c_1+c_2\) gives a \((k+1)\)-term representation of
\(n\) from \(C\). Thus all sufficiently large \(n\) lie in \((k+1)C\).
\(\square\)

This lemma is a possible positive route. The unresolved point is whether one
can always choose an infinite \(B\) satisfying the two hypotheses under the
minimality assumption.

## Lemma 2.2: Multi-hit absorption criterion

Let \(A\) be an asymptotic basis of order \(k\), let \(B\subseteq A\), and
put
\[
C=A\setminus B.
\]
Suppose there is \(t\in C\) such that for every \(r=1,\ldots,k\) and every
choice of deleted elements \(b_1,\ldots,b_r\in B\), with repetitions
allowed,
\[
t+b_1+\cdots+b_r\in(r+1)C.
\]
Then \(C\) is an asymptotic basis of order \(k+1\).

Proof. Let \(n\) be sufficiently large that \(n-t\in kA\), and choose a
representation
\[
n-t=a_1+\cdots+a_k,\qquad a_i\in A.
\]
If none of the \(a_i\) lies in \(B\), then
\[
n=t+a_1+\cdots+a_k\in(k+1)C.
\]
Otherwise let \(b_1,\ldots,b_r\) be the submultiset of deleted summands in
this representation. The remaining \(k-r\) summands lie in \(C\). By the
hypothesis,
\[
t+b_1+\cdots+b_r\in(r+1)C.
\]
Adding the \(k-r\) retained summands gives a \((k+1)\)-term representation
of \(n\) from \(C\). Hence every sufficiently large \(n\) lies in
\((k+1)C\). \(\square\)

Lemma 2 is the \(r\le1\) version of this criterion. Lemma 8.2a is the
special case \(k=2\), written separately because it is the main repair
target in the remaining \(k=2\) analysis.

## Theorem 2.3: Reflection-recurrence gives a good deletion in every order

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\). Suppose
that \(A\) is finitely reflection-recurrent:
for every finite \(T\subset A\) there are arbitrarily large \(m\) such that
\[
m-T\subset A.
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(k+1\).

Proof. We construct \(B=\{b_1,b_2,\ldots\}\) and a protected set
\[
P\subset A\setminus B
\]
so that Lemma 2.2 applies. Fix \(e\in A\), which will remain protected.

We use finite algebraic certificates. For a multiset \(S\) of deleted
elements, write \(|S|=q\) and \(\sigma(S)\) for the sum of its elements,
with multiplicity. For every multiset \(S\) of currently deleted elements
with \(q<k\), and every
\[
d=1,\ldots,k-q,
\]
we maintain:

* an ordered \(d\)-tuple \(Y(S,d)=(y_1,\ldots,y_d)\) of elements of
  \(A\setminus\{e\}\);
* a \((q+1)\)-tuple \(X(S,d)\) of protected elements of \(P\);

such that
\[
\sigma(S)+y_1+\cdots+y_d
=(d-1)e+\sum_{x\in X(S,d)}x. \tag{1}
\]

First build the certificates for \(S=\varnothing\). Choose
\[
x_1=y_1\in A\setminus\{e\},
\]
giving the \(d=1\) certificate. Suppose
\[
y_1+\cdots+y_d=(d-1)e+x_d
\]
has been constructed, with \(x_d\in A\). By reflection-recurrence applied
to \(\{e,x_d\}\), choose \(M\) so large that
\[
M-e,\ M-x_d\in A,\qquad M-x_d\ne e.
\]
Put
\[
x_{d+1}=M-e,\qquad y_{d+1}=M-x_d.
\]
Then
\[
y_1+\cdots+y_d+y_{d+1}=de+x_{d+1}.
\]
Continuing to \(d=k\) gives all empty-multiset certificates. Add \(e\) and
all \(x_d\) appearing in these certificates to \(P\).

Now suppose \(b_1,\ldots,b_j\), the protected set \(P\), and all
certificates have been constructed. Let \(R\) be the finite set consisting
of \(e\) and every entry of every current \(Y(S,d)\). By
reflection-recurrence, choose a large \(m=m_{j+1}\) such that
\[
m-R\subset A,
\]
avoiding the finitely many values that would make
\[
b_{j+1}=m-e
\]
already deleted or protected, or would make some \(m-y\) with
\[
y\in R\setminus\{e\}
\]
already deleted. Define
\[
b_{j+1}=m-e.
\]
For every \(y\in R\setminus\{e\}\), add \(m-y\) to the protected set \(P\).
These elements are retained by construction.

We now create repairs for all deleted multisets whose largest-index element
is \(b_{j+1}\). Let \(S\) be an old deleted multiset of size \(q\), and let
\(\ell\ge1\) satisfy
\[
q+\ell\le k.
\]
Let
\[
Y(S,\ell)=(y_1,\ldots,y_\ell).
\]
Using (1),
\[
\sigma(S)+y_1+\cdots+y_\ell
=(\ell-1)e+\sum_{x\in X(S,\ell)}x.
\]
Therefore
\[
e+\sigma(S)+\ell b_{j+1}
=\sum_{p=1}^{\ell}(m-y_p)+\sum_{x\in X(S,\ell)}x. \tag{2}
\]
The right side has \(\ell+q+1\) protected summands, so (2) is exactly the
repair required by Lemma 2.2 for the multiset
\[
S+\ell\{b_{j+1}\}.
\]

It remains to propagate certificates for future stages. Let
\[
S'=S+\ell\{b_{j+1}\},
\qquad |S'|=q+\ell<k,
\]
and let
\[
d=1,\ldots,k-q-\ell.
\]
Take the old certificate for \((S,\ell+d)\), and write
\[
Y(S,\ell+d)=(y_1,\ldots,y_{\ell+d}).
\]
Define
\[
Y(S',d)=(y_1,\ldots,y_d)
\]
and
\[
X(S',d)=X(S,\ell+d)\cup
\{m-y_{d+1},\ldots,m-y_{d+\ell}\},
\]
counting multiplicities. A direct substitution in (1) gives
\[
\sigma(S')+y_1+\cdots+y_d
=(d-1)e+\sum_{x\in X(S',d)}x,
\]
and the new entries in \(X(S',d)\) are protected. Thus all certificates are
maintained.

The recursion produces an infinite \(B\) disjoint from \(P\). Let
\[
C=A\setminus B.
\]
Take any deleted multiset \(D\) of size \(r\le k\), and let \(b_j\) be its
largest-index element, with multiplicity \(\ell\). Write
\[
D=S+\ell\{b_j\}
\]
where \(S\) uses only older deleted elements. At stage \(j\), equation (2)
gave
\[
e+\sigma(D)\in(r+1)P\subset(r+1)C.
\]
Thus the hypothesis of Lemma 2.2 holds with \(t=e\), so \(C=A\setminus B\)
is an asymptotic basis of order \(k+1\). \(\square\)

## Lemma 2.4: Tail reflection-recurrence is enough

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\). Suppose
there is \(D\) such that for every finite
\[
T\subset A\cap(D,\infty)
\]
there are arbitrarily large \(m\) with
\[
m-T\subset A.
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(k+1\).

Proof. The proof of Theorem 2.3 uses reflection-recurrence only for the
finite set \(R\) consisting of the fixed padder \(e\) and the finitely many
entries occurring in the certificate tuples \(Y(S,d)\). We choose these
initial certificate entries in the tail \(A\cap(D,\infty)\).

First choose
\[
e,x_1=y_1\in A\cap(D,\infty),\qquad x_1\ne e.
\]
Suppose the empty-multiset certificate has been built through \(d\), with
all entries \(e,x_d,y_1,\ldots,y_d\) larger than \(D\). By the tail
recurrence hypothesis applied to \(\{e,x_d\}\), choose \(M\) arbitrarily
large such that \(M-e,M-x_d\in A\). Taking \(M\) large also ensures
\[
M-e>D,\qquad M-x_d>D,\qquad M-x_d\ne e.
\]
Set \(x_{d+1}=M-e\) and \(y_{d+1}=M-x_d\), exactly as in Theorem 2.3. This
builds the initial certificates with all relevant \(Y\)-entries in the
tail.

During the main deletion recursion, the set \(R\) to which recurrence is
applied is always a subset of the fixed finite tail set
\[
\{e,y_1,\ldots,y_k\}.
\]
Indeed, the certificate propagation in Theorem 2.3 only reuses prefixes of
old \(Y\)-tuples; the newly created elements \(m-y\) are protected
\(X\)-entries, not future \(Y\)-entries. Thus the tail recurrence
hypothesis supplies each required center \(m\), and \(m\) may be chosen so
large that all new protected elements and deleted elements are positive,
new, and outside the finite forbidden set.

The repair identities and the final application of Lemma 2.2 are unchanged
from Theorem 2.3. Hence the constructed infinite deletion leaves an
order-\((k+1)\) basis. \(\square\)

## Lemma 3: Late finite-deletion reservoir criterion

Let \(h=k+1\). Suppose \(R\subseteq A\) is infinite and has the following
property: for every finite \(F\subset R\) and every \(L\), there is
\(b\in R\setminus F\), \(b>L\), such that
\[
A\setminus(F\cup\{b\})
\]
is an asymptotic basis of order \(h\) with some threshold \(N_b<b\).

Then there exists an infinite \(B\subset R\) such that \(A\setminus B\) is
an asymptotic basis of order \(h\).

Proof. Choose \(b_1<b_2<\cdots\) recursively. Having chosen
\(F_j=\{b_1,\ldots,b_j\}\), let \(N_j\) be a threshold for
\(A\setminus F_j\) as an order-\(h\) basis. Choose
\[
b_{j+1}>\max\{b_j,N_j\}
\]
using the reservoir property, with a new threshold \(N_{j+1}<b_{j+1}\).
Let \(B=\{b_j:j\ge1\}\).

Fix \(n\) sufficiently large. Choose \(j\) such that
\[
N_j\le n<b_{j+1}.
\]
Since \(A\setminus F_j\) is an order-\(h\) basis above \(N_j\), \(n\) has an
\(h\)-term representation from \(A\setminus F_j\). Every summand in that
representation is at most \(n<b_{j+1}\), hence it is not one of the future
deleted elements \(b_{j+1},b_{j+2},\ldots\). Therefore the same
representation lies in \(h(A\setminus B)\).

Thus \(A\setminus B\) is an order-\(h\) asymptotic basis. \(\square\)

This lemma reduces a positive proof to finding infinitely many late
finite-deletable elements at order \(k+1\). That has not yet been proved.

## Warning 3.0: Finite-deletion independence is not enough by itself

It is tempting to argue as follows: if there is an infinite \(B_0\subset A\)
such that \(A\setminus F\) is an order-\((k+1)\) basis for every finite
\(F\subset B_0\), then delete a sufficiently sparse infinite subset of
\(B_0\). This argument is incomplete without threshold control.

Indeed, after choosing a finite prefix \(F_j=\{b_1,\ldots,b_j\}\), let
\(N_j\) be a threshold for \(A\setminus F_j\). To cover all
\[
n\in[b_j,b_{j+1}),
\]
one needs \(N_j\le b_j\), not merely \(N_j<b_{j+1}\). But \(N_j\) is known
only after \(b_j\) has already been chosen. Thus finite deletability must be
supplemented by the late-threshold condition in Lemma 3.

Consequently, a counterexample may have all finite subsets of some infinite
set deletable at order \(k+1\), yet still evade the naive diagonal if each
new deletion pushes the threshold beyond the deleted element.

This points to a delayed-gap counterexample pattern: finite deletions are
eventually repaired, but only after thresholds beyond the deleted elements;
infinitely many such delayed repairs could leave unbounded gaps. No rigorous
construction of this type is currently known in this workspace.

For \(k=2\), the delayed-gap pattern would still need a strong translate
immunity condition. If an infinite deletion is \(D\) and a proposed gap is
\(n\), then every retained \(c\in A\setminus D\) with \(n-c\) above the
order-2 threshold must have
\[
n-c\notin2(A\setminus D).
\]
Thus delayed gaps for finite prefixes do not automatically survive in the
infinite deletion; later retained elements can repair them by padding
two-term representations.

## Warning 3.0b: The finite-deletion tree has no terminal-node normal form

The threshold issue in Warning 3.0 also invalidates a tempting
finite-booster normal form. Let \(h\ge2\) and put
\[
A=\{1\}\cup h\mathbb N.
\]
Then \(A\) is an asymptotic basis of order \(h\). No infinite deletion
\(B\subset A\) leaves an order-\(h\) basis: if \(1\in B\), only multiples
of \(h\) remain, while if \(B\cap h\mathbb N\) is infinite, then for each
deleted multiple \(b\) the integer
\[
b+h-1
\]
has every \(h\)-term representation from \(A\) forced to use exactly
\(h-1\) copies of \(1\) and the single multiple \(b\).

Nevertheless there is no finite \(F\subset A\) such that \(A\setminus F\)
is an ordinary minimal order-\(h\) basis. If \(1\in F\), then
\(A\setminus F\) is not an order-\(h\) basis. If \(1\notin F\), then
\(F\) removes only finitely many multiples of \(h\), and deleting one more
remaining multiple still leaves an order-\(h\) basis after a later
threshold.

Thus an infinite branch through the tree of finite order-\(h\)-deletions
need not diagonalize to an infinite deletion preserving order \(h\). The
least thresholds can run past the deleted elements. This example is not a
counterexample to Erdős Problem #881 when \(h=k+1\), since
\(\{1\}\cup h\mathbb N\) is not an order-\(h-1\) basis; it only rules out
the proposed normal-form reduction.

## Example 3.0a: Minimality does not control finite-prefix delays

The residue-padding basis
\[
A=\{1\}\cup2\mathbb N
\]
is an order-2 basis and is strongly minimal under infinite deletions at
order \(2\), as in Example 11. Also, all singleton deletions
\[
A\setminus\{2d\}
\]
are order-3 bases; deleting \(1\) is the only one-point order-3 failure.

Nevertheless, the finite prefixes
\[
F_M=\{2,4,\ldots,2M\}
\]
are late-bad for order \(3\). Put
\[
C_M=A\setminus F_M=\{1\}\cup\{2r:r\ge M+1\}.
\]
Then \(C_M\) is an order-3 basis with least threshold
\[
4M+4>2M=\max F_M.
\]
Indeed, every even \(n\ge4M+4\) has
\[
n=1+1+(n-2),
\]
where \(n-2\ge4M+2\) is retained. Every odd \(n\ge4M+5\) has
\[
n=1+2(M+1)+(n-2M-3),
\]
where the last summand is an even retained element. Hence all
\[
n\ge4M+4
\]
lie in \(3C_M\). But
\[
4M+3\notin3C_M:
\]
three even summands are even, two copies of \(1\) plus an even summand are
even, and one copy of \(1\) plus two retained evens is at least
\[
1+(2M+2)+(2M+2)=4M+5.
\]
Thus no threshold below \(4M+4\) works.

This example shows that order-2 minimality, even together with eventual
order-3 stability of almost all one-point deletions, does not prevent
arbitrarily late finite-prefix thresholds. A positive proof must choose the
deleted elements sparsely or exploit additional structure; it cannot rely on
arbitrary finite prefixes being non-late-bad.

## Corollary 3.1: What a counterexample must block

Let \(h=k+1\). Suppose no infinite \(B\subseteq A\) has \(A\setminus B\)
an order-\(h\) basis. Then there exist a finite set \(F\subset A\) and a
bound \(L\) such that \(A\setminus F\) is an order-\(h\) basis, but for
every \(b\in A\setminus F\) with \(b>L\), at least one of the following
holds:

1. \(A\setminus(F\cup\{b\})\) is not an order-\(h\) basis;
2. every threshold \(N_b\) for \(A\setminus(F\cup\{b\})\) as an
   order-\(h\) basis satisfies \(N_b\ge b\).

Proof. If the conclusion failed, then with
\[
R=A\setminus F
\]
for every finite \(F\subset A\) for which \(A\setminus F\) is an
order-\(h\) basis and for every \(L\), there would be some
\(b\in A\setminus F\), \(b>L\), such that
\[
A\setminus(F\cup\{b\})
\]
is an order-\(h\) basis with a threshold \(N_b<b\). Lemma 3 would then
construct an infinite deletion preserving order \(h\), contrary to the
assumption. \(\square\)

Thus a counterexample must, after some finite deletion, make every
sufficiently large remaining element either genuinely order-\(h\)-essential
or only deletable with a threshold not below the element itself.

## Corollary 3.1b: Late-bad finite prefixes

Let \(h=k+1\). For a nonempty finite set \(F\subset A\), call \(F\)
**late-bad** if either \(A\setminus F\) is not an order-\(h\) basis, or
every order-\(h\) threshold for \(A\setminus F\) is at least \(\max F\).

If there is an infinite increasing sequence
\[
b_1<b_2<\cdots,\qquad b_i\in A,
\]
such that every finite prefix
\[
F_j=\{b_1,\ldots,b_j\}
\]
is not late-bad, then \(B=\{b_j:j\ge1\}\) is an infinite deletion for which
\[
A\setminus B
\]
is an order-\(h\) basis.

Proof. Since \(F_j\) is not late-bad, \(A\setminus F_j\) is an order-\(h\)
basis with a threshold \(N_j<\max F_j=b_j\). Let \(n\) be large and choose
\(j\) such that
\[
b_j\le n<b_{j+1}.
\]
Then \(n\ge b_j>N_j\), so \(n\) has an order-\(h\) representation from
\(A\setminus F_j\). All future deleted elements are \(>n\), so the same
representation avoids all of \(B\). Hence \(n\in h(A\setminus B)\).
\(\square\)

Thus, in any counterexample, every infinite increasing sequence in \(A\)
must have a late-bad finite prefix. This is the threshold-sensitive finite
barrier form of the problem.

The converse is also useful: the finite-prefix threshold strategy is not a
weaker sufficient condition but exactly the desired conclusion. If
\[
B=\{b_1<b_2<\cdots\}\subset A
\]
and \(A\setminus B\) is an order-\(h\) basis with threshold \(N\), then
discarding the finitely many \(b_i\le N\) gives a tail whose every finite
prefix \(F_j\) satisfies
\[
A\setminus F_j\supseteq A\setminus B
\]
and hence is an order-\(h\) basis with the same threshold \(N<b_j\).
Therefore proving the existence of an infinite sequence with no late-bad
prefix is equivalent to proving the desired infinite deletion.

## Corollary 3.1c: Barrier formulation of a counterexample

Let \(h=k+1\), and suppose no infinite deletion from \(A\) leaves an
order-\(h\) basis. Let \(\mathcal L_h\) be the family of finite nonempty
sets \(F\subset A\) that are late-bad in the sense of Corollary 3.1b. Then
\(\mathcal L_h\) is a barrier in the following weak sense:

for every infinite \(X\subset A\), there exists a finite
\[
F\subset X,\qquad F\in\mathcal L_h.
\]

Proof. If some infinite \(X\subset A\) contained no finite late-bad subset,
then choosing its elements increasingly
\[
b_1<b_2<\cdots
\]
would give an infinite sequence all of whose finite prefixes are not
late-bad. Corollary 3.1b would then produce an infinite deletion preserving
order \(h\), contradiction. \(\square\)

Together with Lemma 10.1, this means that a counterexample must provide a
finite-set barrier \(\mathcal L_h\) such that each \(F\in\mathcal L_h\) is
not merely combinatorial: it creates either a genuine order-\(h\) failure or
a delayed threshold, and in the genuine-failure case \(F\) is a vertex cover
for many order-\(k\) representation hypergraphs.

## Lemma 3.2: Protected matching criterion

Let \(A\) be an asymptotic basis of order \(k\). Suppose there is a finite
set \(E\subset A\) such that for every \(r\ge1\) there is \(N_r\) with the
following property: for every \(n\ge N_r\), there are \(r\)
\((k+1)\)-term representations
\[
n=a_{i,1}+\cdots+a_{i,k+1}\qquad(1\le i\le r)
\]
from \(A\), such that the sets of summands outside \(E\),
\[
\{a_{i,1},\ldots,a_{i,k+1}\}\setminus E,
\]
are pairwise disjoint as \(i\) varies.

Then there is an infinite \(B\subset A\setminus E\) such that
\[
A\setminus B
\]
is an asymptotic basis of order \(k+1\).

Proof. Choose \(b_1<b_2<\cdots\) recursively in \(A\setminus E\), requiring
\[
b_j>N_{j+2}\qquad(j\ge1).
\]
This is possible because \(A\setminus E\) is infinite. Let
\[
B=\{b_j:j\ge1\}.
\]

Let \(n\) be sufficiently large. Choose \(j\) such that
\[
b_j\le n<b_{j+1}.
\]
Then \(n\ge b_j>N_{j+2}\). By hypothesis, \(n\) has \(j+2\)
representations whose outside-\(E\)
summand sets are pairwise disjoint. Future deleted elements
\(b_{j+1},b_{j+2},\ldots\) are larger than \(n\), so they cannot occur in a
representation of \(n\) by positive summands. Among the first \(j\) deleted
elements, each can meet the outside-\(E\) summand set of at most one of the
\(j+2\) disjoint representations. Hence at least one representation avoids
all of \(B\). Since \(B\cap E=\varnothing\), that representation lies in
\((k+1)(A\setminus B)\). Thus all sufficiently large \(n\) are represented.
\(\square\)

So a broad positive theorem would follow from proving that, after protecting
a finite exceptional core, the \((k+1)\)-representation hypergraphs of all
large \(n\) have arbitrarily large matchings. Conversely, a counterexample
must have infinitely many large \(n\) whose \((k+1)\)-representations admit
bounded transversals outside every finite protected core.

## Corollary 3.3: Hypergraph transversal obstruction

Assume that no infinite \(B\subset A\) has \(A\setminus B\) an
order-\((k+1)\) basis. Let \(E\subset A\) be finite. For \(n\), form the
finite hypergraph \(\mathcal H_E(n)\) whose vertices are
\[
A\cap[1,n]\setminus E
\]
and whose edges are the nonempty sets
\[
\{a_1,\ldots,a_{k+1}\}\setminus E
\]
coming from \((k+1)\)-term representations
\[
n=a_1+\cdots+a_{k+1},\qquad a_i\in A.
\]
Then there is an integer \(r_E\) and arbitrarily large \(n\) such that the
matching number of \(\mathcal H_E(n)\) is \(<r_E\). Consequently, for those
\(n\), there is a transversal
\[
D_n\subset A\setminus E,\qquad |D_n|\le (k+1)(r_E-1),
\]
meeting every \((k+1)\)-representation of \(n\) outside \(E\).

Proof. If the matching numbers were unbounded uniformly for all sufficiently
large \(n\), then the hypothesis of Lemma 3.2 would hold with this \(E\),
and we could delete an infinite subset of \(A\setminus E\) while preserving
order \(k+1\), contrary to the assumption. Hence for some \(r_E\), the
matching number is \(<r_E\) for arbitrarily large \(n\).

For such an \(n\), take a maximal matching. It has at most \(r_E-1\) edges,
each of size at most \(k+1\). The union of these edges meets every edge of
\(\mathcal H_E(n)\), by maximality, and has size at most
\((k+1)(r_E-1)\). \(\square\)

This corollary is often the most concrete form of the remaining problem:
one must either rule out such bounded moving transversals for arbitrary
order-\(k\) bases, or build a counterexample whose representation
hypergraphs exhibit them. By Reduction 0, such a counterexample would
automatically satisfy the Erdős infinite-deletion minimality hypothesis.

## Proposition 3.4: Redundant representation criterion

With the notation of Corollary 3.3, suppose there is a finite
\(E\subset A\) such that, for every \(R\ge1\), all sufficiently large \(n\)
satisfy
\[
|\mathcal H_E(n)|>(k+1)(R-1)\Delta_E(n),
\]
where \(\Delta_E(n)\) is the maximum degree of a vertex in
\(\mathcal H_E(n)\). Then there is an infinite \(B\subset A\setminus E\)
such that \(A\setminus B\) is an order-\((k+1)\) basis.

Proof. A greedy matching in a hypergraph with edge size at most \(k+1\) has
size at least
\[
\frac{|\mathcal H_E(n)|}{(k+1)\Delta_E(n)}.
\]
Indeed, after choosing an edge, at most \((k+1)\Delta_E(n)\) edges meet it.
The displayed hypothesis therefore implies that for every \(R\), all
sufficiently large \(n\) have a matching of size at least \(R\). Lemma 3.2
applies. \(\square\)

This proposition proves the desired conclusion for any basis whose
\((k+1)\)-representations are sufficiently redundant after ignoring a finite
core. A counterexample must therefore have large integers whose
representation hypergraphs are not merely small, but efficiently covered by
bounded vertex sets.

## Lemma 3.5: Transversals are shifted finite barriers

Let \(A\) be an asymptotic basis of order \(k\), let \(E\subset A\) be
finite, and let \(D\subset A\setminus E\) meet every edge of
\(\mathcal H_E(n)\), where \(\mathcal H_E(n)\) is the hypergraph from
Corollary 3.3. Then for every
\[
c\in A\setminus(E\cup D)
\]
with \(n-c\) large enough to be in the asymptotic range, every \(k\)-term
representation of \(n-c\) from \(A\) uses at least one element of \(D\).

Proof. If
\[
n-c=a_1+\cdots+a_k
\]
with \(a_i\in A\setminus D\), then
\[
n=c+a_1+\cdots+a_k
\]
is a \((k+1)\)-term representation of \(n\). Its outside-\(E\) summand set
contains \(c\) and contains no element of \(D\), contradicting that \(D\)
is a transversal of \(\mathcal H_E(n)\). \(\square\)

Thus bounded moving transversals are exactly finite order-\(k\) barriers
for a large family of shifted targets \(n-c\), as \(c\) ranges over
retained elements of \(A\). This is stronger than the minimality hypothesis
from Lemma 2.1, but it is not formally contradicted by it: Lemma 2.1 says
finite barriers must occur inside every infinite deletion, not that no
single finite barrier can control many shifted targets.

## Lemma 3.5a: Protected shifts are also dominated

Let \(A\), \(E\), \(D\), and \(\mathcal H_E(n)\) be as in Lemma 3.5. Let
\[
c\in A\setminus D
\]
and suppose \(n-c\) is large enough to lie in the order-\(k\) asymptotic
range of \(A\). If every \(k\)-term representation of \(n-c\) using only
elements of \(E\) is impossible, then every \(k\)-term representation of
\(n-c\) from \(A\) uses at least one element of \(D\).

Proof. Suppose
\[
n-c=a_1+\cdots+a_k
\]
is a \(k\)-term representation from \(A\) avoiding \(D\). If every
\(a_i\in E\), this contradicts the extra hypothesis. Otherwise
\[
n=c+a_1+\cdots+a_k
\]
is a \((k+1)\)-term representation of \(n\). Its outside-\(E\) summand set
is nonempty, avoids \(D\), and therefore gives an edge of
\(\mathcal H_E(n)\) missed by the transversal \(D\), contradiction.
\(\square\)

This allows the finite protected core \(E\) to contain test shifts
\(c\). For large \(n\), a fixed finite \(E\) cannot by itself represent
\(n-c\), so the same bounded transversal dominates all shifts by elements
of \(E\) as well. The remaining gap is uniformity: the bound on \(D\) in
Corollary 3.3 may depend on \(E\), so enlarging \(E\) to include a large
test pattern does not force a single reflected center by pigeonhole.

The following finite gadget shows why the protected-matching route cannot
be forced from the order-\(k\) basis property alone. Fix a finite set
\[
C\subset\mathbb N,\qquad p\in C,\qquad M=\max C,
\]
choose
\[
d>kM,\qquad n>2(d+kM),
\]
and put
\[
R=\{n-d-(k-1)p-c:c\in C\},\qquad A_0=C\cup\{d\}\cup R.
\]
Then every \((k+1)\)-term representation of \(n\) from \(A_0\) uses \(d\),
while for every \(c\in C\),
\[
n=c+d+\underbrace{p+\cdots+p}_{k-1\text{ times}}+
  (n-d-(k-1)p-c).
\]
Indeed, a representation without \(d\) cannot use zero elements of \(R\),
because \(n>2(d+kM)> (k+1)M\); it cannot use at least two elements of \(R\),
because each element of \(R\) is larger than \(n-d-kM\), so two of them
already exceed \(n\); and with exactly one element \(r_c\in R\), the other
\(k\) summands from \(C\) would have to sum to
\[
d+(k-1)p+c>kM,
\]
which is impossible. Hence \(\{d\}\) is a one-point transversal for all
\((k+1)\)-representations of \(n\), and simultaneously a finite barrier for
the shifted \(k\)-representations of \(n-c\), \(c\in C\).

This is only a local obstruction, not a counterexample to the problem. The
hard part is making such gates coexist with global asymptotic coverage and
the late-threshold requirements from Lemma 3.

## Counterexample Reduction

Suppose \(k\ge 2\). A counterexample would follow from an asymptotic
order-\(k\) basis \(A\) and a cofinite subset \(P\subseteq A\) such that for
each \(a\in P\) there is a witness \(t_a\) with \(t_a\to\infty\) along
infinite subsets and
\[
t_a\in kA,\qquad t_a\notin (k+1)(A\setminus\{a\}).
\]
Then any infinite \(B\subseteq A\) contains infinitely many elements of
\(P\), so \(A\setminus B\) misses infinitely many unbounded witnesses
\(t_a\) even at order \(k+1\).

The key missing piece is an infinite construction of such robust witnesses
while retaining the order-\(k\) basis property.

## Counterexample Reduction 2: Unbounded finite barriers

A more flexible counterexample would follow from a cofinite infinite set
\(P\subset A\), a finite-uniform hypergraph \(\mathcal F\) on \(P\), and
witnesses \(w_F\) indexed by \(F\in\mathcal F\), satisfying:

1. for every \(F\in\mathcal F\),
   \[
   w_F\notin(k+1)(A\setminus F);
   \]
2. \(\mathcal F\) is an **unbounded barrier** with respect to the witness
   map \(F\mapsto w_F\): for every infinite \(X\subset P\) and every \(L\),
   there is \(F\in\mathcal F\) such that
   \[
   F\subset X,\qquad w_F>L.
   \]

Then every infinite \(B\subset A\) contains protected finite sets with
arbitrarily large witnesses. Indeed, \(B\cap P\) is infinite, so for every
\(L\) choose \(F\in\mathcal F\) with
\[
F\subset B\cap P,\qquad w_F>L.
\]
Since
\[
A\setminus B\subseteq A\setminus F,
\]
we have
\[
w_F\notin(k+1)(A\setminus B).
\]
These missing witnesses are unbounded as \(L\to\infty\), so
\(A\setminus B\) is not an order-\((k+1)\) basis.

The unboundedness clause is essential. A hypergraph with no infinite
independent set only guarantees that every infinite \(B\) contains at least
one protected finite set \(F\); one finite missing witness does not prevent
\(A\setminus B\) from being an asymptotic basis.

Equivalently, for every \(L\), the tail hypergraph
\[
\mathcal F_{>L}=\{F\in\mathcal F:w_F>L\}
\]
has no infinite independent set in \(P\). This tail form is often easier to
test: every infinite deletion must be forced to contain protected finite
sets whose witnesses escape every fixed initial interval.

By Lemma 10.1, any such witness must make \(F\) a vertex cover for all
relevant order-\(k\) representation hypergraphs of \(w_F-e\), as \(e\) runs
over retained padders. This is the finite-barrier version of the domination
obstruction.

## Lemma 2.1: Strong minimality as finite barriers at order \(k\)

Let \(A\) be an asymptotic basis of order \(k\). The following are
equivalent.

1. For every infinite \(B\subset A\), the set \(A\setminus B\) is not an
   asymptotic basis of order \(k\).
2. For every infinite \(B\subset A\) and every \(N\), there are an integer
   \(n\ge N\) and a finite set \(F\subset B\) such that every \(k\)-term
   representation of \(n\) from \(A\) uses at least one element of \(F\).

Proof. Suppose (1) holds. Fix infinite \(B\subset A\). Since
\(A\setminus B\) is not an order-\(k\) basis, for every \(N\) there is
\(n\ge N\) with
\[
n\notin k(A\setminus B).
\]
Equivalently, every \(k\)-term representation of \(n\) from \(A\) uses some
element of \(B\). As all summands in a representation of \(n\) are at most
\(n\), the finite set
\[
F=B\cap[1,n]
\]
meets every such representation.

Conversely, if (2) holds and some infinite \(B\) had \(A\setminus B\) an
order-\(k\) basis, then for all sufficiently large \(n\) there would be a
\(k\)-term representation of \(n\) avoiding \(B\), contradicting (2) for
large \(N\). \(\square\)

Thus the hypothesis of the problem says exactly that every infinite subset
of \(A\) contains finite order-\(k\) barriers for arbitrarily large
witnesses. The desired conclusion asks for an infinite subset \(B\) whose
finite barriers at order \(k\) do not become barriers at order \(k+1\).

## Lemma 4: Finite private two-sum gadgets tensor

Call a finite set \(T\subset[0,D]\) a full private two-sum gadget if
\[
T+T=[0,2D]
\]
and for each \(t\in T\) there is a sum \(u_t\in T+T\) with exactly one
unordered representation from \(T+T\), and that representation uses \(t\).

If \(T\subset[0,D]\) and \(S\subset[0,E]\) are full private two-sum gadgets,
then
\[
U=T+(2D+1)S
\]
is a full private two-sum gadget in \([0,D+(2D+1)E]\).

Proof. Put \(Q=2D+1\). Every integer in
\[
[0,2D+2QE]
\]
has a unique decomposition \(x+Qy\) with \(0\le x\le 2D\) and
\(0\le y\le 2E\). Since \(T+T=[0,2D]\) and \(S+S=[0,2E]\), this proves
\(U+U=[0,2(D+QE)]\).

For privacy, take \(u=t+Qs\in U\). Choose private sums
\[
x_t=t+t'\in T+T,\qquad y_s=s+s'\in S+S
\]
whose unique unordered representations use \(t\) and \(s\), respectively.
Then
\[
x_t+Qy_s=(t+Qs)+(t'+Qs')
\]
has a unique unordered representation from \(U+U\), because reducing modulo
\(Q\) fixes the low-coordinate representation and then the high-coordinate
representation. Thus the unique representation uses \(u\). \(\square\)

The base gadget \(T=\{0,1,3,4\}\subset[0,4]\) is full and private. Hence
there are arbitrarily large finite full private two-sum gadgets.

This lemma is not yet a counterexample. The obstruction is cross-block
repair: if a shifted block \(M+T\) covers a full interval of two-sums and
there is a retained earlier element \(e\), then every witness \(2M+u\) with
\(u\ge e\) is vulnerable to the repair
\[
2M+u=e+(2M+u-e),
\]
because \(2M+u-e\) is again a two-sum of current block elements. A successful
counterexample must prevent this repair for all but finitely many elements,
or avoid full interval blocks.

## Lemma 5: Finite safe-marker gadgets exist, but inefficiently

Let \(E\subset\mathbb N\) be finite and let \(L\ge1\). There is a finite
set \(T\subset\mathbb N_0\) such that:

1. \(T+T\) contains \([0,2L]\);
2. for every \(t\in T\) there is a sum \(u_t\in T+T\) whose unordered
   representation from \(T+T\) is unique and uses \(t\);
3. for every \(t\in T\) and every \(e\in E\), \(u_t-e\notin T+T\).

Proof. Put \(C=[0,L]\). We will add marker elements
\[
p_0,p_1,\ldots,p_L
\]
so rapidly increasing that the following finite list of forbidden
equalities is avoided.

For \(c\in C\), we want \(c+p_c\) to be a private sum for \(c\). For the
marker \(p_c\), we want \(2p_c\) to be a private sum. Thus define
\[
u_c=c+p_c,\qquad u_{p_c}=2p_c.
\]
Choose the markers recursively. At stage \(c\), after
\(p_0,\ldots,p_{c-1}\) have been chosen, choose \(p_c\) larger than every
previously chosen marker, larger than \(2L+\max E\), and outside the finite
set of values that would make one of the following equalities true:

* \(c+p_c=x+y\) with \(\{x,y\}\ne\{c,p_c\}\) and
  \(x,y\in C\cup\{p_0,\ldots,p_c\}\);
* \(2p_c=x+y\) with \(\{x,y\}\ne\{p_c,p_c\}\) and
  \(x,y\in C\cup\{p_0,\ldots,p_c\}\);
* \(c+p_c-e=x+y\) or \(2p_c-e=x+y\), with \(e\in E\) and
  \(x,y\in C\cup\{p_0,\ldots,p_c\}\).

This is possible because only finitely many integer values of \(p_c\) are
excluded. In addition, require
\[
p_{c+1}> 2p_c+2L+\max E
\]
at the next step. This growth condition guarantees that no later marker can
create a new representation of an earlier private sum or of an earlier
shifted forbidden value: every sum involving a later marker is already
larger than the earlier quantities under consideration.

Let
\[
T=C\cup\{p_0,\ldots,p_L\}.
\]
Then \(C+C=[0,2L]\), proving (1). By the avoidance conditions and the
growth condition, each \(c+p_c\) is uniquely represented and uses \(c\), and
each \(2p_c\) is uniquely represented and uses \(p_c\). The same conditions
give \(u_t-e\notin T+T\) for all \(e\in E\). \(\square\)

This lemma shows that local safe private witnesses are not the obstacle.
The obstacle is efficiency: the marker construction has diameter much larger
than the interval \([0,2L]\) that it covers. In an infinite block
counterexample, future blocks must begin above all current protected
witnesses, while the order-2 coverage intervals must still leave no gaps.
Lemma 5 does not provide enough coverage per diameter to meet both demands.

## Lemma 5.1: Dense intervals repair marker witnesses

Let \(I=[r,r+L]\cap\mathbb N\), and let \(F\subset I\) have size \(m\).
Then
\[
[2r+2m,\ 2r+2L-2m]\subseteq 2(I\setminus F).
\]

Proof. Let \(s\) lie in the displayed interval. The possible first summands
\(x\in I\) with \(s-x\in I\) form an interval of integers. Since \(s\) is
at distance at least \(2m\) from both endpoints of \(2I=[2r,2r+2L]\), this
interval contains more than \(2m\) choices. Deleting \(F\) forbids at most
\(m\) choices with \(x\in F\) and at most \(m\) choices with \(s-x\in F\).
Thus some admissible \(x\) remains, giving \(s=x+(s-x)\in2(I\setminus F)\).
\(\square\)

Consequently, if \(J\subseteq2(A\setminus F)\) is such a central interval
and \(w\notin3(A\setminus F)\), then
\[
(A\setminus F)\cap(w-J)=\varnothing.
\]
Any retained \(e\in w-J\) would give \(w=e+j\) with
\(j\in J\subseteq2(A\setminus F)\).

This blocks a natural interval-plus-marker construction. If
\(I=[r,r+L]\subset A\), \(U=2r+2L\), and a marker \(p=U+t\) is used to try
to protect \(a\in I\) with witness \(p+a\), then for every \(a\) with
\[
a+t+2\in I
\]
one has
\[
p+a=(a+t+2)+(U-2),
\]
and \(U-2\in2(I\setminus\{a\})\) by the lemma. Thus a marker close enough
to continue coverage protects only endpoint elements of a dense interval;
placing it far away creates a coverage gap.

## Lemma 6: A modular finite-accelerator obstruction

Let \(G\) be an abelian group, let \(S\subseteq G\), and let \(f\in G\).
If \(S\cup\{f\}\) is a \(k\)-basis of \(G\), meaning
\[
k(S\cup\{f\})=G,
\]
then every element of \(G\) has a \((k+1)\)-term representation from
\(S\cup\{f\}\) using at least one copy of \(f\).

Proof. Translate by \(-f\). Put \(T=S-f\). The hypothesis becomes
\[
k(T\cup\{0\})=G.
\]
Every element \(g\in G\) therefore has a representation
\[
g=t_1+\cdots+t_k,\qquad t_i\in T\cup\{0\}.
\]
Appending one more \(0\) gives a \((k+1)\)-term representation using the
accelerator \(0\). Translating back, this is a \((k+1)\)-term
representation from \(S\cup\{f\}\) using \(f\). \(\square\)

Consequently, a counterexample cannot be proved by a purely modular design
where a finite accelerator lowers the order from \(k+1\) to \(k\) while
private order-\((k+1)\) witnesses remain in residue classes inaccessible to
the accelerator. The accelerator reaches every residue at order \(k+1\).

## Lemma 6.1: Thick residue lifts do not give single-element privacy

Let \(S\subseteq\mathbb Z/m\mathbb Z\) satisfy \(2S=\mathbb Z/m\mathbb Z\),
and suppose that for some \(s_0\in S\) there is a residue
\[
\rho\notin3(S\setminus\{s_0\}).
\]
This is a common finite cyclic analogue of one-point essentiality. It does
not lift to single-integer essentiality in a thick block
\[
T_L=\{s+mq:s\in S,\ 0\le q\le L\}.
\]

Indeed, by Lemma 6 with \(k=2\), the residue \(\rho\) has a three-term
representation using \(s_0\):
\[
\rho\equiv s_0+u+v\pmod m,\qquad u,v\in S.
\]
Write
\[
s_0+u+v=\rho+mc
\]
for the corresponding carry. For a central quotient \(Q\), the integer
\[
\rho+mQ
\]
has representations
\[
\rho+mQ=(s_0+mq)+(u+mi)+(v+mj)
\]
whenever
\[
q+i+j=Q-c,\qquad 0\le q,i,j\le L.
\]
If \(Q-c\) lies away from the endpoints of \([0,3L]\), there are
\(\gg L^2\) such triples. Deleting a single integer
\[
a=s_0+mq_0
\]
removes only those triples with \(q=q_0\), at most \(O(L)\) of them. Hence
for all large \(L\) and central \(Q\), some representation remains after
deleting \(a\).

Thus finite cyclic examples where deleting one residue destroys
three-sum coverage prove whole-residue-class essentiality, not
single-integer essentiality. The only residue-lift witnesses that can remain
private after deleting one integer must be forced near endpoint quotients,
where the number of lifts is small. This matches Example 13.2 and also
explains why such endpoint witnesses do not leave the long buffer needed
for an iteration of Proposition 13.1.

## Example 7: A strongly minimal order-2 basis with a good infinite deletion

Let \(a\equiv3\pmod5\), and for a sufficiently large threshold \(N_0\) let
\[
C=\{n\ge N_0:n\equiv0\text{ or }1\pmod5\},\qquad A=C\cup\{a\}.
\]
Then \(A\) is an asymptotic basis of order \(2\), strongly minimal under
infinite deletions at order \(2\), and has an infinite deletion leaving an
order-3 basis.

Proof. Since \(C+C\) contains all sufficiently large integers in residue
classes \(0,1,2\pmod5\), and \(a+C\) contains all sufficiently large
integers in residue classes \(3,4\pmod5\), \(A\) is an order-2 basis.

Let \(B\subseteq A\) be infinite. If \(B\cap C\) is infinite, then for every
\(b\in B\cap C\) large enough, the integer \(a+b\) has no representation as
a sum of two elements of \(A\setminus B\). Indeed, \(C+C\) has residues only
\(0,1,2\pmod5\), while \(a+b\) has residue \(3\) or \(4\pmod5\), so a
two-term representation must be \(a+c\). Equality gives \(c=b\), which has
been deleted. If \(B\cap C\) is finite, then \(B\) can be infinite only by
including \(a\) and finitely many other elements, impossible; hence every
infinite \(B\) destroys order \(2\). Thus \(A\) is strongly minimal at order
\(2\).

Now choose an infinite \(B\subset C\) whose relative counting function is
\(o(x)\) in each of the progressions \(0\pmod5\) and \(1\pmod5\). Put
\(C'=C\setminus B\) and \(A'=A\setminus B=C'\cup\{a\}\). The \(k=1\)
counting argument, applied inside arithmetic progressions, shows that
\(C'+C'\) contains all sufficiently large integers in the residue classes
\(0,1,2\pmod5\). Adding one more element of \(C'\) gives all sufficiently
large integers in residue classes \(0,1,2,3\pmod5\). Also \(a+2C'\) gives
all sufficiently large integers in residue classes \(3,4,0\pmod5\), and
\(2a+C'\) gives residue classes \(1,2\pmod5\). Therefore every sufficiently
large integer lies in \(3A'\), so \(A'\) is an order-3 basis. \(\square\)

## Proposition 7.1: Eventually periodic bases satisfy the conclusion

Let \(A\subseteq\mathbb N\) be eventually periodic: there are \(m\ge1\),
a nonempty residue set \(S\subseteq\mathbb Z/m\mathbb Z\), and \(N_0\) such
that for all \(n\ge N_0\),
\[
n\in A\quad\Longleftrightarrow\quad n\bmod m\in S.
\]
If \(A\) is an asymptotic basis of order \(k\), then there is an infinite
\(B\subset A\) such that \(A\setminus B\) is an asymptotic basis of order
\(k+1\).

Proof. Since \(A\) is an order-\(k\) basis, the residue set satisfies
\[
kS=\mathbb Z/m\mathbb Z.
\]
As \(S\ne\varnothing\), this implies
\[
(k+1)S=kS+S=\mathbb Z/m\mathbb Z.
\]
Choose one residue \(s_0\in S\), and let \(B\) be an infinite subset of
\[
\{n\in A:n\equiv s_0\pmod m\}
\]
with zero relative density in that progression; for instance, take a rapidly
growing sequence in that progression.

We claim \(C=A\setminus B\) is an order-\((k+1)\) basis. Fix a residue
class \(r\pmod m\), and choose residues \(s_1,\ldots,s_{k+1}\in S\) with
\[
s_1+\cdots+s_{k+1}\equiv r\pmod m.
\]
For all large \(n\equiv r\pmod m\), the number of solutions to
\[
x_1+\cdots+x_{k+1}=n,\qquad
x_i\equiv s_i\pmod m,\qquad x_i\ge N_0,
\]
is \(\gg n^k\). The solutions with some \(x_i\in B\) are \(o(n^k)\), since
\(B(x)=o(x)\) inside its progression and there are only \(O(n^{k-1})\)
choices for the remaining variables once one coordinate is fixed. Therefore,
for all sufficiently large \(n\equiv r\pmod m\), at least one such solution
uses no element of \(B\). All its coordinates lie in \(C\), so
\[
n\in(k+1)C.
\]
There are finitely many residue classes \(r\), hence \(C\) is an
order-\((k+1)\) asymptotic basis. \(\square\)

## Example 7.2: Finite deletion can raise the order by an arbitrary amount

Finite-deletion stability at order \(k+1\) is false, even for eventually
periodic bases. Fix \(m\ge5\). Let
\[
C=\{n\ge N_0:n\equiv0\text{ or }1\pmod m\}
\]
and let \(f\) be a fixed positive integer with \(f\equiv2\pmod m\). Put
\[
A=C\cup\{f\}.
\]
The residue set of \(A\) is \(\{0,1,2\}\pmod m\). If
\[
h=\left\lceil\frac{m-1}{2}\right\rceil+1,
\]
then every residue modulo \(m\) is a sum of \(h\) residues from
\(\{0,1,2\}\), and the representation can be chosen with at least one
residue \(0\) or \(1\). The corresponding \(C\)-summand can absorb all
sufficiently large size, so \(A\) is an asymptotic basis of order \(h\).

After deleting the single element \(f\), only the residues \(\{0,1\}\)
remain. A sum of \(t\) such residues can realize only residues
\[
0,1,\ldots,t\pmod m
\]
before wraparound; hence \(C\) cannot be an asymptotic basis of order
\(t<m-1\), while it is an asymptotic basis of order \(m-1\). Thus deleting
one non-essential finite accelerator can raise the required order from about
\(m/2\) to \(m-1\), an arbitrarily large jump.

This example rules out any proof that tries to show arbitrary finite
deletions outside a finite essential core preserve order \(k+1\).

## Lemma 8: One-point order-3 failure forces translate thickness

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\), and let \(a\in A\). Put \(S=A\setminus\{a\}\). If
\(S\) is not an asymptotic basis of order \(3\), then for every finite
set \(T\subset S\) there are arbitrarily large integers \(m\) such that
\[
m-T\subset S.
\]

Proof. Since \(S\) is not an order-3 basis, there are arbitrarily large
integers \(n\notin 3S\). Fix a finite \(T\subset S\), and choose such an
\(n\) with
\[
n>\max T+N_0,\qquad n>\max T+2a.
\]
For each \(t\in T\), the integer \(n-t\) is at least \(N_0\), hence lies in
\(2A\). If \(n-t\in2S\), then
\[
n=t+(n-t)\in S+2S=3S,
\]
contradicting the choice of \(n\). Thus \(n-t\in2A\setminus2S\).

Since the only element removed from \(A\) is \(a\), every two-term
representation of \(n-t\) from \(A\) uses \(a\). The alternative
\(n-t=2a\) is excluded by \(n>\max T+2a\). Therefore
\[
n-t=a+s_t
\]
for some \(s_t\in S\). Put \(m=n-a\). Then \(m-t=s_t\in S\) for every
\(t\in T\). As the missing integers \(n\) can be chosen arbitrarily large,
so can \(m\). \(\square\)

Consequently, if for some \(a\in A\) there is a finite
\(T\subset A\setminus\{a\}\) for which the intersection
\[
\bigcap_{t\in T}(S+t)
\]
is bounded, then \(A\setminus\{a\}\) is an order-3 basis. This gives a
concrete obstruction to a \(k=2\) counterexample: any order-3-essential
large element must leave behind a set that is additively thick in this
finite-translate sense.

## Corollary 8.1: Infinitely many bad one-point deletions force recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
there are infinitely many \(a\in A\) such that \(A\setminus\{a\}\) is not an
asymptotic basis of order \(3\). Then for every finite \(T\subset A\) there
are arbitrarily large \(m\) such that
\[
m-T\subset A.
\]

Proof. Given finite \(T\subset A\), choose a bad element
\[
a\in A\setminus T.
\]
Apply Lemma 8 to \(S=A\setminus\{a\}\). Since \(T\subset S\), there are
arbitrarily large \(m\) with \(m-T\subset S\subset A\). \(\square\)

Thus a \(k=2\) counterexample with infinitely many one-point order-3
essential elements must be finitely reflection-recurrent. A possible
positive strategy is to prove that such recurrence permits an infinite
deletion preserving order \(2\), contradicting the Erdős minimality
hypothesis.

The next theorem proves the weaker conclusion needed for Erdős Problem
#881: finite reflection-recurrence permits an infinite deletion preserving
order \(3\).

## Lemma 8.2a: A two-deleted-summand repair criterion

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Let \(B\subset A\), put
\[
C=A\setminus B,
\]
and suppose there is \(e\in C\) such that:

1. for every \(b\in B\),
   \[
   b+e\in2C;
   \]
2. for every \(b,b'\in B\), allowing \(b=b'\),
   \[
   b+b'+e\in3C.
   \]

Then \(C\) is an asymptotic basis of order \(3\).

Proof. Let \(n\) be large enough that \(n-e\ge N_0\). Since \(A\) is an
order-2 basis, choose
\[
n-e=x+y,\qquad x,y\in A.
\]
If \(x,y\in C\), then \(n=e+x+y\in3C\). If exactly one of \(x,y\), say
\(x=b\), lies in \(B\), then
\[
n=y+(b+e)\in C+2C=3C
\]
by condition 1. If both \(x,y\in B\), then condition 2 gives
\[
n=x+y+e\in3C.
\]
Thus all sufficiently large \(n\) lie in \(3C\). \(\square\)

In applications it is often enough to build an explicit protected reservoir.
If \(P\subset C\), \(e\in P\), and
\[
b+e\in2P\qquad(b\in B),
\]
while
\[
b+b'+e\in3P\qquad(b,b'\in B),
\]
then the hypotheses of Lemma 8.2a hold. Theorem 8.2 constructs such a
protected reservoir recursively from finite reflection-recurrence.

## Theorem 8.2: Reflection-recurrence gives a good deletion for \(k=2\)

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Suppose that \(A\) is finitely reflection-recurrent:
for every finite \(T\subset A\) there are arbitrarily large \(m\) such that
\[
m-T\subset A.
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. We will construct \(B\) so that Lemma 8.2a applies. First choose
fixed retained elements that will handle diagonal
repairs. Pick distinct \(e,q\in A\). By reflection-recurrence applied to
\(\{e,q\}\), choose \(r\) so large that
\[
r-e,\ r-q\in A,\qquad r-q\ne e.
\]
Put
\[
u=q,\qquad v=r-q,\qquad w=r-e.
\]
Then
\[
u+v=e+w,
\]
with \(u,v,w\in A\) and \(u,v\ne e\).

We recursively choose deleted elements
\[
B=\{b_1,b_2,\ldots\}
\]
and a protected set \(P\subset A\) that will never be deleted. Initially
put
\[
\{e,u,v,w\}\subset P.
\]
For each deleted element \(b_i\), we will maintain protected elements
\[
s_i,t_i\in P
\]
such that
\[
s_i-t_i=b_i-e,\qquad t_i\ne e. \tag{1}
\]

Assume \(b_1,\ldots,b_j\) and the corresponding protected elements have
been chosen. Let
\[
X_j=\{e,u,v,t_1,\ldots,t_j\}\subset A.
\]
By reflection-recurrence there are arbitrarily large \(m\) with
\[
m-X_j\subset A.
\]
Choose such an \(m=m_{j+1}\) avoiding the finite set of values that would
make one of the following collisions occur:

* \(m-e\) is already deleted or protected;
* one of \(m-u,m-v,m-t_1,\ldots,m-t_j\) is already deleted;
* one of \(m-u,m-v,m-t_1,\ldots,m-t_j\) equals \(m-e\).

This finite avoidance is possible because the admissible centers \(m\) are
arbitrarily large. Define
\[
b_{j+1}=m-e.
\]
Add the needed mirrors
\[
m-u,\quad m-v,\quad m-t_1,\ldots,m-t_j
\]
to \(P\). These elements are in \(A\) by the choice of \(m\), and none is
deleted.

It remains to create the pair-repair data for the new \(b_{j+1}\). Apply
reflection-recurrence to the finite set \(\{e,b_{j+1}\}\), and choose a
large \(M\) such that
\[
M-e,\ M-b_{j+1}\in A,
\]
again avoiding finitely many collisions with the current deleted and
protected sets, ensuring the two new elements are not equal to
\(b_{j+1}\), and ensuring
\[
M-b_{j+1}\ne e.
\]
Put
\[
s_{j+1}=M-e,\qquad t_{j+1}=M-b_{j+1},
\]
and add them to \(P\). Then \(s_{j+1},t_{j+1}\in P\) and
\[
s_{j+1}-t_{j+1}=b_{j+1}-e,\qquad t_{j+1}\ne e,
\]
so (1) is maintained. The recursion gives an infinite set
\[
B=\{b_j:j\ge1\}
\]
disjoint from the protected set \(P\). Let
\[
C=A\setminus B.
\]

We record the repair identities. First, for each \(j\),
\[
b_j+e=m_j=(m_j-u)+u\in2C, \tag{2}
\]
because \(u\) and \(m_j-u\) are protected. Second, if \(i<j\), then
\[
b_j+b_i+e=m_j+b_i=(m_j-t_i)+s_i+e\in3C, \tag{3}
\]
using \(s_i-t_i=b_i-e\) and the fact that \(m_j-t_i,s_i,e\in C\). Third,
for the diagonal case,
\[
2b_j+e=2m_j-e=(m_j-u)+(m_j-v)+w\in3C, \tag{4}
\]
because \(u+v=e+w\) and \(m_j-u,m_j-v,w\in C\).

Equations (2), (3), and (4) are precisely the two repair hypotheses in
Lemma 8.2a. Therefore \(C=A\setminus B\) is an asymptotic basis of order
\(3\). \(\square\)

## Corollary 8.3: The \(k=2\) problem is solved in the infinitely-bad case

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). If there
are infinitely many \(a\in A\) such that \(A\setminus\{a\}\) is not an
asymptotic basis of order \(3\), then there is an infinite \(B\subset A\)
such that \(A\setminus B\) is an asymptotic basis of order \(3\).

Proof. Corollary 8.1 gives finite reflection-recurrence of \(A\). Apply
Theorem 8.2. \(\square\)

## Lemma 8.3a: Late one-point deletions also force recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\), and let \(m_0=\min A\). Suppose that there are
infinitely many \(b\in A\) such that \(A\setminus\{b\}\) is an order-3
basis but has no order-3 threshold below \(b\). Then \(A\) is finitely
reflection-recurrent. Consequently there is an infinite
\(B\subset A\) such that \(A\setminus B\) is an order-3 basis.

Proof. For each such \(b\), choose
\[
w_b\ge b-1,\qquad w_b\notin3(A\setminus\{b\}).
\]
This is possible because \(b-1\) is not a threshold for
\(A\setminus\{b\}\). Put
\[
d_b=w_b-b.
\]
We first show that \(d_b\to\infty\) along every infinite sequence of these
late elements with \(b\to\infty\).

Let
\[
C_b=A\setminus\{b\}.
\]
If \(e\in C_b\) and \(w_b-e\ge N_0\), then every two-term representation of
\(w_b-e\) from \(A\) must use \(b\); otherwise adding \(e\) would give a
three-term representation of \(w_b\) from \(C_b\). If also \(e>d_b\), then
\[
w_b-e=b+(d_b-e)<b,
\]
so no positive two-term representation of \(w_b-e\) can use \(b\). Hence
\[
A\cap(d_b,\ w_b-N_0]\subseteq\{b\}. \tag{1}
\]

If the numbers \(d_b\) were bounded along an infinite sequence, say
\(d_b\le D\), and increasing \(D\) if necessary so that \(D\ge m_0\), then
(1) implies that every element of \(A\), except possibly \(b\), in
\[
(D,\ b+d_b-N_0]
\]
is absent. Choose
\[
n>\max\{N_0,\ 2D\}
\]
with
\[
n<\min\{b+m_0,\ b+d_b-N_0+m_0\}.
\]
This is possible for all sufficiently large \(b\), since \(d_b\ge-1\).
The integer \(n\) cannot be represented as a sum of two elements of \(A\).
A representation using \(b\) is already at least \(b+m_0>n\). A
representation avoiding \(b\) cannot use any element in
\((D,b+d_b-N_0]\), and any element larger than \(b+d_b-N_0\) would already
make the two-term sum exceed \(n\). Hence a representation avoiding \(b\)
uses only elements at most \(D\), and has sum at most \(2D<n\). This
contradicts that \(A\) is an order-2 basis. Therefore \(d_b\) is unbounded.

Now fix a finite set \(T\subset A\) and a bound \(L\). Choose a late
element \(b\notin T\) such that
\[
d_b>\max(T\cup\{L\})
\]
and
\[
w_b-\max T\ge N_0.
\]
For every \(t\in T\), the integer \(w_b-t\) has a two-term representation
from \(A\), and every such representation uses \(b\). Therefore
\[
w_b-t=b+c_t
\]
with \(c_t\in A\), or equivalently
\[
d_b-t\in A.
\]
Thus
\[
d_b-T\subset A.
\]
Since \(d_b\) can be made arbitrarily large, \(A\) is finitely
reflection-recurrent. The final assertion follows from Theorem 8.2.
\(\square\)

Thus any unresolved \(k=2\) counterexample must lie in the complementary
case: all but finitely many one-point deletions \(A\setminus\{a\}\) are
order-3 bases with some threshold below \(a\), but infinite deletions still
fail at order \(3\) through collective finite barriers or uncontrolled
finite-prefix thresholds.

## Corollary 8.3b: In a \(k=2\) counterexample, late barriers are non-singleton

Let \(A\subseteq\mathbb N\) be an order-2 basis which is a counterexample
to the desired \(k=2\) conclusion. Then there is a finite set
\[
E\subset A
\]
such that for every \(a\in A\setminus E\), the singleton deletion
\[
A\setminus\{a\}
\]
is an order-3 basis with some threshold \(N_a<a\). Consequently, for every
infinite \(X\subset A\setminus E\), there is a finite set
\[
F\subset X,\qquad |F|\ge2,
\]
which is late-bad at order \(3\) in the sense of Corollary 3.1b.

Proof. If infinitely many one-point deletions are not order-3 bases, then
Corollary 8.3 gives the desired infinite deletion, contrary to the
counterexample assumption. If infinitely many one-point deletions are
order-3 bases but have no threshold below the deleted element, then Lemma
8.3a gives the desired infinite deletion, again a contradiction. Thus all
but finitely many \(a\in A\) have the stated singleton property; put the
exceptions in \(E\).

By Corollary 3.1c, every infinite \(X\subset A\setminus E\) contains a
finite late-bad subset \(F\). No singleton subset of \(X\) is late-bad,
because each singleton deletion has an order-3 threshold below its only
element. Hence \(|F|\ge2\). \(\square\)

## Lemma 8.4: The remaining \(k=2\) obstruction is collective

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Suppose the set
\[
E_1=\{a\in A:A\setminus\{a\}\text{ is not an order-3 basis}\}
\]
is finite, and put
\[
G=A\setminus E_1.
\]
If there is no infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis, then for every infinite \(X\subset G\) and every \(L\) there
exist a finite nonempty set \(F\subset X\) and an integer \(w_F>L\) such
that
\[
w_F\notin3(A\setminus F).
\]
Moreover, for every retained padder \(e\in A\setminus F\) with
\[
w_F-e\ge N_0,
\]
the set \(F\) meets every two-term representation of \(w_F-e\) from \(A\).
Equivalently,
\[
(A\setminus F)\cap[1,w_F-N_0]
\subseteq
\bigcup_{f\in F}(w_F-f-A).
\]

Proof. Assume no infinite deletion leaves an order-3 basis. By Corollary
3.1c, the late-bad finite sets for order \(3\) form a barrier on \(A\).
Fix infinite \(X\subset G\) and \(L\), and pass to the infinite tail
\[
X'=\{x\in X:x>L+1\}.
\]
Choose a finite late-bad set \(F\subset X'\). Then \(\max F>L+1\).

If \(A\setminus F\) is not an order-3 basis, it has arbitrarily large
holes, so choose \(w_F>L\) with
\[
w_F\notin3(A\setminus F).
\]
Otherwise \(A\setminus F\) is an order-3 basis, but every order-3 threshold
for it is at least \(\max F\). Therefore \(\max F-1\) is not a threshold,
so there exists
\[
w_F\ge \max F-1>L
\]
with \(w_F\notin3(A\setminus F)\).

The vertex-cover assertion is exactly Lemma 10.1 with \(k=2\). The
reflected-cover inclusion follows because, for every retained
\[
e\le w_F-N_0,
\]
every representation \(w_F-e=x+y\) uses some \(f\in F\), so
\[
w_F-e=f+a
\]
for some \(a\in A\), equivalently \(e\in w_F-f-A\). \(\square\)

Since \(F\subset G\), no singleton in \(F\) is genuinely bad at order \(3\).
Thus the obstruction in Lemma 8.4 is either a delayed threshold for a
finite deletion that is eventually repaired, or a genuinely collective
finite deletion failure. In particular, the remaining \(k=2\) case cannot
be settled by considering one-point deletions alone.

## Lemma 8.4b: Minimal collective-hole normal form

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\), and put \(m_0=\min A\). Let \(w\) be large
enough that \(w\in3A\). Suppose \(F\subset A\) is finite and
\[
w\notin3(A\setminus F).
\]
Choose \(F'\subseteq F\) inclusion-minimal with
\[
w\notin3(A\setminus F').
\]
Then:

1. for every \(f\in F'\),
   \[
   f\le w-2m_0;
   \]
2. for every \(f\in F'\), there are \(c_f,d_f\in A\setminus F'\) such that
   \[
   w=f+c_f+d_f;
   \]
3. for every retained element \(e\in A\setminus F'\) with
   \(w-e\ge N_0\), the set \(F'\) meets every two-term representation of
   \(w-e\) from \(A\).

Moreover, if every singleton deletion \(A\setminus\{f\}\), \(f\in F'\), is
an order-3 basis with some threshold below \(f\), then \(|F'|\ge2\).

Proof. Minimality gives
\[
w\in3(A\setminus(F'\setminus\{f\}))
\]
for every \(f\in F'\). Since \(w\notin3(A\setminus F')\), every such
representation must use \(f\). Thus
\[
w=f+c_f+d_f,\qquad c_f,d_f\in A\setminus F',
\]
which proves (2). Since \(c_f,d_f\ge m_0\), (1) follows.

For (3), let \(e\in A\setminus F'\) and \(w-e\ge N_0\). If
\[
w-e=x+y,\qquad x,y\in A,
\]
with \(x,y\notin F'\), then \(w=e+x+y\in3(A\setminus F')\), a
contradiction. Hence every such two-term representation meets \(F'\).

Finally suppose \(F'=\{f\}\). By (1), \(w\ge f\). If
\(A\setminus\{f\}\) has an order-3 threshold \(N_f<f\), then
\(w\ge f>N_f\) implies
\[
w\in3(A\setminus\{f\}),
\]
contrary to the choice of \(F'\). Hence, under the stated singleton
threshold hypothesis, the minimal hole is genuinely collective:
\(|F'|\ge2\). \(\square\)

This normal form is now the default form for the remaining \(k=2\) case:
after Corollary 8.3b and after choosing witnesses above the fixed order-3
threshold of \(A\), any late-bad finite set can be shrunk to an
inclusion-minimal collective hole whose every deleted element is actually
used in a repair after the other deleted elements are restored. The false
shortcut is to expect such a set to contain a bad pair. For example, in the
finite set
\[
A_0=\{1,2,3,4,5\},\qquad F=\{1,2,3\},\qquad w=9,
\]
one has \(9\notin3(A_0\setminus F)\), but restoring any one element of
\(F\) repairs the hole. Thus an inclusion-minimal collective hole need not
have any bad two-element subhole.

## Lemma 8.4a: Collective holes force a retained gap

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\), and put \(m_0=\min A\). Let \(F\subset A\) be finite and
nonempty, put \(C=A\setminus F\), and suppose
\[
w\notin3C.
\]
Writing \(f_0=\min F\), one has
\[
C\cap(w-f_0-m_0,\ w-N_0]=\varnothing. \tag{1}
\]

Proof. Let
\[
e\in C\cap(w-f_0-m_0,\ w-N_0].
\]
Then \(w-e\ge N_0\), so \(w-e\in2A\). Since \(w\notin3C\), every two-term
representation of \(w-e\) from \(A\) must use an element of \(F\); otherwise
adding \(e\) would give a three-term representation of \(w\) from \(C\).
Thus
\[
w-e=f+a
\]
with \(f\in F\) and \(a\in A\). But then
\[
w-e\ge f_0+m_0,
\]
whereas \(e>w-f_0-m_0\) gives
\[
w-e<f_0+m_0,
\]
a contradiction. \(\square\)

Consequently, if \(F_i\) are finite sets with \(|F_i|\le q\),
\(\min F_i\to\infty\), and witnesses
\[
w_i\notin3(A\setminus F_i)
\]
satisfying \(w_i-\min F_i\le D\), then such a sequence cannot occur in an
order-2 basis. Indeed, (1) implies
\[
A\cap[1,w_i-N_0]\subseteq
[1,D-m_0]\cup F_i
\]
for all \(i\), so \(|A\cap[1,w_i-N_0]|\) is bounded. But an order-2 basis
must have \(|A\cap[1,x]|\to\infty\), since otherwise \(2A\cap[1,x]\) would
have bounded size and could not contain all sufficiently large integers up
to \(x\).

Thus any bounded-size genuine finite-barrier sequence with
\(\min F\to\infty\) must have
\[
w-\min F\to\infty.
\]
For late-bad sets with \(w\ge\max F-1\), this says that a bounded-size
remaining obstruction cannot keep both its internal diameter and its
witness excess bounded.

## Warning 8.5: Bounded-width barriers need not have one fixed size

In the bounded-width version of Lemma 8.4, it is tempting to try to pass to
one fixed cardinality \(r\). This is not justified by pure combinatorics. A
finite union of families that are not barriers can be a barrier.

For example, partition an infinite set \(P\) into two infinite parts
\[
P=P_0\cup P_1.
\]
The singleton family
\[
\mathcal F_1=\{\{x\}:x\in P_0\}
\]
is not a barrier, because \(P_1\) avoids it. The pair family
\[
\mathcal F_2=[P_1]^2
\]
is not a barrier on \(P\), because \(P_0\) avoids it. But
\[
\mathcal F_1\cup\mathcal F_2
\]
is a barrier: every infinite subset of \(P\) either contains an element of
\(P_0\), giving an edge of \(\mathcal F_1\), or has infinitely many
elements in \(P_1\), giving an edge of \(\mathcal F_2\).

Thus a bounded-width collective obstruction may genuinely mix different
sizes. Any proof of the finitely-bad \(k=2\) case must either use more
arithmetic structure than the abstract barrier property, or handle such
mixed-size barriers directly.

There is also no purely combinatorial reduction to bounded width. On an
infinite ordered set \(P=\{p_1<p_2<\cdots\}\), the Schreier-type family
\[
\mathcal S=\{F\subset P:\ |F|=\operatorname{index}(\min F)+1\}
\]
is a barrier: every infinite \(X=\{x_1<x_2<\cdots\}\subset P\) contains the
set consisting of its first \(\operatorname{index}(x_1)+1\) elements. But
on every infinite tail of \(P\), the sizes of the sets in \(\mathcal S\)
are unbounded. Hence even after thinning to an infinite subset, the
late-bad barrier in a counterexample need not have bounded size for
combinatorial reasons alone.

## Lemma 8.5a: Bounded-width barriers can be made uniform on a tail

Let \(P\subseteq\mathbb N\) be an infinite set, let \(q\ge2\), and suppose
that for every infinite \(X\subset P\) and every \(L\), there is a finite set
\[
F\subset X,\qquad 2\le |F|\le q,
\]
with a witness \(w_F>L\) for some property \(\mathcal P(F,w_F)\). Then
there are an integer
\[
r\in\{2,\ldots,q\}
\]
and an infinite set
\[
M=\{m_1<m_2<\cdots\}\subset P
\]
such that for every \(L\) there is \(J(L)\) with the following property:
every
\[
F\in[\{m_j:j\ge J(L)\}]^r
\]
has some witness \(w_F>L\) satisfying \(\mathcal P(F,w_F)\).

Proof. For fixed \(L\) and \(2\le s\le q\), let
\[
\mathcal H_{s,L}
=\{F\in[P]^s:\text{ there is }w>L\text{ with }\mathcal P(F,w)\}.
\]
The hypothesis says that
\[
\bigcup_{s=2}^q\mathcal H_{s,L}
\]
has no infinite independent set.

We claim that for each fixed \(L\), there are \(s(L)\in\{2,\ldots,q\}\)
and an infinite \(P_L\subset P\) such that
\[
[P_L]^{s(L)}\subseteq\mathcal H_{s(L),L}. \tag{1}
\]
This follows by induction on \(q\). For \(q=2\), it is exactly infinite
Ramsey's theorem applied to pairs, since there is no infinite independent
set. For the induction step, apply Ramsey's theorem to the \(q\)-subsets
and \(\mathcal H_{q,L}\). If there is an infinite clique, (1) holds with
\(s(L)=q\). Otherwise pass to an infinite set independent for
\(\mathcal H_{q,L}\); the lower-uniformity union still has no infinite
independent subset, so the induction hypothesis applies.

Apply the claim successively for \(L=1,2,3,\ldots\), producing nested
infinite sets
\[
P=P_0\supset P_1\supset P_2\supset\cdots
\]
and values \(s(L)\). Since only finitely many values occur, choose an
infinite sequence \(L_1<L_2<\cdots\) on which \(s(L_i)=r\) is constant.
Choose
\[
m_i\in P_{L_i}
\]
recursively increasing. For fixed \(L\), choose \(i\) with \(L_i\ge L\).
The tail \(\{m_j:j\ge i\}\) lies in \(P_{L_i}\), so every \(r\)-subset of
that tail has a witness \(>L_i\ge L\). \(\square\)

This lemma is useful only after an arithmetic argument supplies a bounded
width \(q\). The Schreier example above shows that no such \(q\) follows
from the abstract barrier property alone.

## Lemma 8.6: Large-excess collective barriers force partial recurrence

Keep the hypotheses of Lemma 8.4. Suppose that for some \(q\), the sets
\(F\) in Lemma 8.4 can always be chosen with \(|F|\le q\) and with
arbitrarily large excess over the barrier. More precisely, assume that for
every infinite \(X\subset G\) and every \(L\), there are \(F\subset X\),
\(|F|\le q\), and a witness \(w\) satisfying the conclusion of Lemma 8.4
such that
\[
w-\max F>L.
\]
Then \(A\) has the following partial reflection-recurrence property: for
every finite \(T\subset A\), there are arbitrarily large \(m\) and a subset
\[
U\subset T,\qquad |U|\ge |T|/q,
\]
such that
\[
m-U\subset A.
\]

Proof. Fix finite \(T\subset A\) and \(L_0\). Choose an infinite
\[
X\subset G
\]
disjoint from \(T\). By the large-excess bounded-width hypothesis, with
\[
L>\max\{L_0+\max T,\ \max T+N_0\},
\]
there are \(F\subset X\), \(|F|\le q\), and a witness \(w\) such that
\[
w-\max F>L,\qquad
w\notin3(A\setminus F).
\]
For every \(t\in T\), we have \(t\notin F\) and \(w-t\ge N_0\). Since
\(A\) is an order-2 basis, choose a representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A.
\]
By Lemma 10.1, every such representation uses an element of \(F\). Hence
for each \(t\in T\), there are \(f_t\in F\) and \(c_t\in A\) with
\[
w-t=f_t+c_t.
\]
By pigeonhole, some \(f\in F\) occurs for a subset
\[
U\subset T,\qquad |U|\ge |T|/|F|\ge |T|/q.
\]
Putting
\[
m=w-f
\]
gives
\[
m-t=c_t\in A\qquad(t\in U).
\]
Since \(f\le\max F\), we have
\[
m=w-f\ge w-\max F>L_0+\max T,
\]
so the reflected center \(m\) can be made arbitrarily large by increasing
\(L_0\). \(\square\)

For \(q=1\), large-excess singleton barriers give full finite
reflection-recurrence and hence Theorem 8.2 applies. For \(q\ge2\), the
partial recurrence is weaker: it does not by itself give the simultaneous
reflected mirrors needed in the repair construction of Theorem 8.2. If the
only available barriers have bounded excess, then this recurrence argument
does not apply; this is exactly the delayed-threshold obstruction.

## Lemma 8.6a: Bounded second-excess finite barriers force a good deletion

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Suppose there are a finite set \(E\subset A\) and a
constant \(D\) such that for every infinite \(X\subset A\setminus E\) and
every \(L\), there are a finite set
\[
F=\{f_1<\cdots<f_r\}\subset X,\qquad r\ge2,
\]
and a witness \(w\) satisfying
\[
w>L,\qquad w\ge\max F-1,\qquad w\le f_2+D,
\]
and
\[
w\notin3(A\setminus F).
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. We prove tail finite reflection-recurrence and apply Lemma 2.4.
Let
\[
T\subset A\cap(D,\infty)
\]
be finite, and let \(L_0\) be arbitrary. Choose an infinite
\[
X\subset A\setminus(E\cup T)
\]
whose pairwise gaps exceed \(L_0+1\). Apply the hypothesis with
\[
L>\max T+N_0.
\]
Then for every \(t\in T\), \(w-t\ge N_0\), so by Lemma 10.1 the set \(F\)
meets every two-term representation of \(w-t\) from \(A\).

No such representation can use any \(f_i\) with \(i\ge2\), because
\[
w-t-f_i\le f_2+D-t-f_i\le D-t<0.
\]
Therefore every two-term representation of \(w-t\) uses \(f_1\). Since
\(w-t\in2A\), there is \(c_t\in A\) with
\[
w-t=f_1+c_t.
\]
Put \(m=w-f_1\). Then
\[
m-t=c_t\in A\qquad(t\in T).
\]
Moreover,
\[
m=w-f_1\ge f_2-f_1-1>L_0
\]
because \(w\ge\max F-1\ge f_2-1\) and the elements of \(X\) have pairwise
gaps greater than \(L_0+1\). Thus the reflection centers can be made
arbitrarily large for every finite \(T\subset A\cap(D,\infty)\). Lemma 2.4
gives the desired infinite deletion. \(\square\)

## Corollary 8.6b: Bounded top-excess pair barriers force a good deletion

Work in the remaining \(k=2\) case after Corollary 8.3b. Thus there is a
finite set \(E\subset A\) such that every \(a\in G=A\setminus E\) has
\[
A\setminus\{a\}
\]
an order-3 threshold below \(a\). Suppose that there is a constant \(D\)
such that for every infinite \(X\subset G\) and every \(L\), there are
\[
x<y,\qquad x,y\in X,
\]
and a witness \(w>L\) satisfying
\[
y\le w\le y+D,\qquad w\notin3(A\setminus\{x,y\}).
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. Apply Lemma 8.6a with the same exceptional set \(E\) and with
\[
F=\{x,y\}.
\]
The hypotheses \(y\le w\le y+D\) are exactly
\[
w\ge\max F-1,\qquad w\le f_2+D.
\]
\(\square\)

In the same remaining case, genuine pair witnesses below the larger deleted
element are only low-threshold artefacts. If \(x<y\) lie in \(G\), if
\[
w\notin3(A\setminus\{x,y\}),
\]
and if \(w\) is at least a threshold \(N_x<x\) for \(A\setminus\{x\}\), then
necessarily \(w\ge y\). Indeed, if \(w<y\), then every three-term
representation of \(w\) from \(A\setminus\{x\}\) automatically avoids
\(y\), contradicting the displayed hole.

## Lemma 8.6c: Fractional recurrence gives large recurrent clusters

Let \(A\subseteq\mathbb N\), and suppose there is \(q\ge1\) such that for
every finite \(T\subset A\) and every \(L\), there are \(m>L\) and
\(U\subset T\) satisfying
\[
|U|\ge |T|/q,\qquad m-U\subset A. \tag{1}
\]
Then for every \(M\) there is a set
\[
S\subset A,\qquad |S|=M,
\]
such that for every \(L\) there is \(m>L\) with
\[
m-S\subset A. \tag{2}
\]

Proof. Choose a finite \(T\subset A\) with \(|T|\ge qM\). For each integer
\(L=1,2,\ldots\), apply (1) and choose an \(M\)-element subset
\[
S_L\subset U_L.
\]
There are only finitely many \(M\)-element subsets of \(T\), so some
\(S\) occurs as \(S_L\) for infinitely many, hence unbounded, values of
\(L\). For any prescribed \(L_0\), choose such an occurrence with
\(L>L_0\). Its reflecting center gives \(m>L_0\) and \(m-S\subset A\).
\(\square\)

Applied to Lemma 8.6, bounded-width large-excess barriers force
arbitrarily large finite sets that are fully reflection-recurrent. This is
stronger than the stated one-shot partial recurrence, but it still does not
close the \(k=2\) problem.

First, Lemma 8.6c cannot be diagonalized to an infinite set \(P\subset A\)
whose every finite subset is reflection-recurrent. The obstruction is
already combinatorial. Let the "good" finite subsets of \(\mathbb N\) be
\[
\mathcal G=\{S:\ S\text{ finite and } |S|\le \min S\}.
\]
This hereditary family has a \(1/2\)-fractional property: if
\[
T=\{t_1<\cdots<t_n\},
\]
then the upper half of \(T\) has size at least \(n/2\) and minimum at least
its size, so it lies in \(\mathcal G\). But no infinite \(P\subset\mathbb N\)
has all finite subsets in \(\mathcal G\): if \(p=\min P\), then any
\((p+1)\)-element subset of \(P\) containing \(p\) has size larger than its
minimum.

Second, even an infinite \(P\) whose finite subsets reflect into \(A\) would
not by itself run the protected-reservoir construction. Theorem 2.3 needs a
recurrent finite set carrying the initial repair certificates: for \(k=2\),
one needs recurrent entries \(e,y_1,y_2\) with
\[
y_1+y_2=e+x,\qquad x\in A,
\]
and with \(y_1,y_2\ne e\). After a deletion \(b=m-e\) is chosen, the
construction also creates new mirrors and then needs recurrence for finite
sets containing those generated elements. A fixed recurrent cluster does
not guarantee that these adaptive mirrors remain recurrent. This is the
current precise obstruction to turning fractional recurrence into a full
positive proof.

## Example 8.6d: Unbounded second-excess is locally compatible

The bounded second-excess hypothesis in Lemma 8.6a is a genuine extra
assumption; it is not forced by strong order-2 minimality, singleton
order-3 stability, inclusion-minimality, or reflected-cover domination.

Let
\[
A=\{1\}\cup2\mathbb N.
\]
This is an order-2 basis and is strongly minimal under infinite deletion at
order \(2\): if \(1\) is deleted then no odd integer is represented, while
if \(1\) is retained and infinitely many evens \(2d\) are deleted, then
each corresponding odd integer
\[
2d+1
\]
has the unique order-2 representation \(1+2d\).

All sufficiently large singleton even deletions are order-3-good with a
threshold below the deleted element. If \(d\ge5\), then
\[
A\setminus\{2d\}
\]
represents every \(n\ge9\) as a sum of three elements: even \(n\) has
\[
n=1+1+(n-2),
\]
unless \(n-2=2d\), in which case
\[
n=2+2+(2d-2).
\]
For \(d\ge5\), all summands in these even representations are retained.
Odd \(n\) has a representation
\[
n=1+2a+2b
\]
with \(a,b\ge1\) chosen so that neither even summand is \(2d\). For
\(n\ge9\) this can always be done by moving one unit between \(a\) and
\(b\) if necessary. Hence a threshold \(9<2d\) works for large \(d\).

Now fix \(M\ge2\), put
\[
w_M=4M+3,
\qquad
F_M=\{2M+2,2M+4,\ldots,4M\}.
\]
Then
\[
w_M\notin3(A\setminus F_M).
\]
Indeed, \(w_M\) is odd, so any three-term representation from \(A\) uses
one copy of \(1\) and two even summands whose sum is \(4M+2\). After
removing \(F_M\), the retained evens below \(4M+2\) are at most \(2M\), so
their pairwise sums are at most \(4M\), while any retained even above the
gap is already too large.

The hole is inclusion-minimal. If
\[
f=2M+2j\in F_M,\qquad 1\le j\le M,
\]
then
\[
w_M=1+f+(4M+2-f),
\]
and
\[
4M+2-f=2(M+1-j)
\]
is a retained even. Restoring any one deleted element therefore repairs the
hole.

The reflected-cover domination also holds. For retained \(e\) with
\(w_M-e\ge2\), every two-term representation of \(w_M-e\) uses an element
of \(F_M\). If \(e=1\), this says that every representation of
\(4M+2\) as a sum of two evens uses an even in the removed interval. If
\(e=2r\le2M\), then
\[
w_M-e=1+(4M+2-2r),
\]
and the even summand lies in \(F_M\). There are no other retained
positive \(e\) with \(w_M-e\ge2\).

However, writing \(F_M=\{f_1<\cdots<f_M\}\), the second-excess is
\[
w_M-f_2=(4M+3)-(2M+4)=2M-1\to\infty.
\]
Thus any proof that forces bounded second-excess subbarriers must use the
global barrier hypothesis over every infinite \(X\), not only the local
arithmetic of a single minimal collective hole.

## Warning 8.6e: The retained-gap lemma alone cannot choose the deletion

Lemma 8.4a suggests a sparse-deletion strategy: choose an infinite
\(B\subset A\) so that no finite \(F\subset B\), \(f=\min F\), can contain
all \(A\)-points in a terminal interval
\[
(w-f-m_0,\ w-N_0].
\]
Then no finite \(F\subset B\) could create a three-fold hole. This strategy
does not follow from order-2 basishood alone.

The obstruction is combinatorial. For a fixed \(f\in A\), Lemma 8.4a asks
us to hit every finite set of the form
\[
A\cap(y,\ y+f+m_0-N_0]
\]
with a retained element, whenever this interval is the terminal gap of a
candidate witness. Order-2 basishood gives global two-sum coverage, but it
does not give a local lower bound for the number of \(A\)-points in such
intervals. In particular, the known lemmas do not rule out an infinite tail
\[
C=\{c_1<c_2<\cdots\}\subset A
\]
with the following local isolation pattern: for every \(i<j\), there is an
interval of length \(c_i+m_0-N_0\) whose intersection with \(A\) is exactly
\[
\{c_j\}.
\]
Then every infinite \(B\subset C\) contains \(c_i<c_j\), and the interval
attached to \((i,j)\) has all its \(A\)-points inside \(B\). Thus the
no-complete-terminal-gap selection problem has no infinite solution in this
model.

This is not an additive counterexample, because it does not construct the
corresponding witnesses \(w\notin3(A\setminus F)\). It only shows that
Lemma 8.4a by itself is insufficient. A sparse-gap proof would need an
additional arithmetic thickness statement ruling out such locally isolated
terminal windows in genuine order-2 bases.

## Example 8.7: Pair barriers can be genuinely two-centered

Lemma 8.6 cannot be improved by a simple pigeonhole argument from pair
barriers to full reflection-recurrence. In the finite group
\(\mathbb Z/7\mathbb Z\), let
\[
S=\{0,1,2,4\}.
\]
Then
\[
2S=\mathbb Z/7\mathbb Z,
\]
and every singleton deletion remains a three-fold basis:
\[
3(S\setminus\{s\})=\mathbb Z/7\mathbb Z
\qquad(s\in S).
\]
However, deleting the pair \(\{0,1\}\) creates the three-fold hole
\[
2\notin3(S\setminus\{0,1\}).
\]
The reflected-cover condition corresponding to Lemma 10.1 is
\[
S\subseteq (2-0-S)\cup(2-1-S).
\]
Indeed, for each \(e\in S\), at least one of
\[
2-e,\qquad 1-e
\]
lies in \(S\).

But there is no single residue \(c\) with
\[
c-S\subseteq S.
\]
Thus the pair barrier is intrinsically two-centered: the finite pattern
\(S\) is covered by two reflected copies of \(S\), but not by one. This is
only a residue-level obstruction, not an integer counterexample. By Lemma
6.1, thick residue lifts lose single-integer privacy in central quotients.
It does show that any proof of the finitely-bad \(k=2\) case must rule out
persistent multi-center reflected barriers, not merely invoke Lemma 10.1
and pigeonhole.

## Example 8.7b: Complete finite pair barriers can still be two-centered

There is also no purely Ramsey-theoretic reason that a persistent pair
barrier must contain many one-centered pairs. In
\[
G=\mathbb Z/5\mathbb Z,\qquad S=\{0,1,2,3\},
\]
one has
\[
2S=G,
\]
and every singleton deletion remains a three-fold basis:
\[
3(S\setminus\{s\})=G\qquad(s\in S).
\]
However, every pair deletion creates a three-fold hole. Indeed, after
deleting two elements, only two residues remain, and the three-fold sumset
of two residues has at most four elements.

For example, deleting \(\{0,1\}\) leaves \(\{2,3\}\), and
\[
0\notin3\{2,3\}.
\]
The reflected-cover centers attached to this hole are \(0-0=0\) and
\(0-1=4\). Neither center covers all of \(S\):
\[
0-S=\{0,2,3,4\},\qquad 4-S=\{1,2,3,4\}.
\]
Together they cover \(S\), but each misses one deleted endpoint.

Thus even a complete finite graph of bad pairs can be intrinsically
two-centered. As before, this is not an integer construction. It only shows
that the infinite pair-barrier case needs an arithmetic coherence argument,
not just Ramsey thinning to a tail where all pairs are bad.

## Warning 8.7c: Coherent pair covers need not collapse to one center

Even coherent infinite families of two-center reflected covers do not, at
the cover level, force full reflection-recurrence. This warning isolates the
extra input needed in the pair-barrier case: one must use the fact that the
covers come from actual two-sum representation graphs and genuine
three-fold holes, not just their set-cover shadow.

Work in the ordered abelian group
\[
G=\mathbb Z\times\mathbb Z/8\mathbb Z
\]
and order elements by the first coordinate. Let
\[
H=\{0,1,3\}\subset\mathbb Z/8\mathbb Z,
\qquad
T_*=\{(0,2),(0,4),(0,5),(0,6)\}.
\]
The two residue facts are
\[
H+\{2,4,5,6\}=\mathbb Z/8\mathbb Z, \tag{1}
\]
and
\[
H\cap(H+4)=\varnothing. \tag{2}
\]

Choose a sparse infinite set \(P_0=\{p_1<p_2<\cdots\}\subset\mathbb Z\).
Define a phase function
\[
\theta:\mathbb Z\to\mathbb Z/8\mathbb Z
\]
with \(\theta(0)=\theta(p_i)=0\), and with the following property: for
every difference \(D=p_j-p_i\), \(i<j\), and every length \(R\), there are
arbitrarily far intervals \(I\subset\mathbb Z\) of length \(R\) such that
\[
\theta(n+D)=\theta(n)+4\pmod 8\qquad(n\in I). \tag{3}
\]
This is obtained by assigning disjoint far intervals to the countably many
requirements \((D,R)\), taking \(P_0\) sparse enough to avoid conflicts, and
defining \(\theta\) arbitrarily elsewhere.

Let the "holes" be
\[
C=\{(n,\theta(n)+h):h\in H\},
\]
and put
\[
A=G\setminus C,\qquad
P=\{(p_i,2):i\ge1\}\subset A.
\]
The inclusion \(P\subset A\) follows from \(\theta(p_i)=0\) and
\(2\notin H\); likewise \(T_*\subset A\).

Take \(x=(p_i,2)<y=(p_j,2)\) in \(P\), and write
\[
\delta=y-x=(p_j-p_i,0).
\]
Given any finite \(T\subset A\), choose an interval \(I\) satisfying (3)
for \(D=p_j-p_i\), long enough and far enough that the first coordinates of
\(m-t\), \(t\in T\), all lie in \(I\). Then for every \(t\in T\), the two
candidates
\[
m-t,\qquad m+\delta-t
\]
have hole fibers whose phase differs by \(4\). By (2), they cannot both be
holes, so at least one lies in \(A\). Equivalently,
\[
T\subset(m-A)\cup(m+\delta-A). \tag{4}
\]
This is exactly the two-center reflected-cover pattern supplied by Lemma
10.1 for a pair \(\{x,y\}\), with centers \(w-y=m\) and \(w-x=m+\delta\).

However no single center reflects \(T_*\) into \(A\). For any
\[
c=(n,r)\in G,
\]
identity (1) gives some \(t\in T_*\) such that \(c-t\in C\). Hence
\[
c-T_*\nsubseteq A.
\]
Thus every cover in (4) is genuinely two-centered on the fixed test set
\(T_*\), and this remains true coherently for all pairs in the infinite
tail \(P\).

This model is not an integer additive counterexample, and it does not
construct the corresponding witnesses \(w\notin3(A\setminus\{x,y\})\). It
does show that the missing positive step cannot be a Ramsey or coherence
argument applied only to the reflected-cover inclusions from Lemma 10.1.

## Example 8.7d: Genuine bad pairs need not give one-center recurrence

The previous warning used only the cover-level shadow of pair holes. The
following integer example shows that even one genuine bad pair, together
with actual order-2 coverage, does not force one-center recurrence, bounded
top-excess, or a density contradiction.

Fix a large integer \(q\) and put
\[
x=8q+2,\qquad y=8q+6,\qquad R=\{0,1,4\}\pmod 8.
\]
Let
\[
A=\{x,y\}\cup\{n>y:n\bmod 8\in R\}.
\]
Then \(A\) is an asymptotic basis of order \(2\). Residue-wise,
\[
R+R=\{0,1,2,4,5\}\pmod 8,
\]
while
\[
x+R=\{2,3,6\}\pmod 8,\qquad y+R=\{6,7,2\}\pmod 8.
\]
Together these cover all residues modulo \(8\), and the tail in the
residue classes \(R\) is cofinite in those classes, so every sufficiently
large integer has a two-term representation from \(A\).

Now let \(w\) be any sufficiently large integer with
\[
w\equiv7\pmod 8.
\]
After deleting the pair \(\{x,y\}\), only the \(R\)-tail remains. Since
\[
3R=\{0,1,2,3,4,5,6\}\pmod 8,
\]
we have
\[
w\notin3(A\setminus\{x,y\}).
\]
Thus \(\{x,y\}\) is a genuine bad pair for arbitrarily large witnesses, and
\[
w-y\to\infty.
\]

The reflected cover is genuinely split. If \(e\in A\setminus\{x,y\}\) is a
tail element, then:
\[
\begin{array}{c|c|c}
e\bmod8 & w-y-e\bmod8 & w-x-e\bmod8\\ \hline
0 & 1\in R & 5\notin R\\
1 & 0\in R & 4\in R\\
4 & 5\notin R & 1\in R
\end{array}
\]
For large \(w\), the entries in \(R\) are represented by actual tail
elements of \(A\). Hence the two centers \(w-y\) and \(w-x\) cover all
large retained tail padders, but neither center covers all three residue
classes.

Moreover choose a finite test set
\[
T=\{t_0,t_1,t_4\}\subset A
\]
with \(t_r\equiv r\pmod8\) for \(r\in R\). No sufficiently large center
\(m\) satisfies
\[
m-T\subset A.
\]
Indeed, this would require
\[
m\bmod8\in R+0,\qquad
m\bmod8\in R+1,\qquad
m\bmod8\in R+4,
\]
but
\[
R\cap(R+1)\cap(R+4)=\varnothing.
\]

Thus the local inference from a genuine pair hole to one-center
reflection-recurrence is false. A positive proof must use the global
barrier/minimality hypotheses across all infinite deletions, not only the
local data from a single pair.

## Example 8.8: Finite-center repairs need coherence

A naive finite-center replacement for Lemma 8.2a is false. It is not enough
that each deleted pattern be repairable with some retained center; the same
center must be compatible with the representation being repaired.

Work in the finite group \(G=\mathbb Z/5\mathbb Z\). Let
\[
S=\{0,1,2,3\},\qquad D=\{0,3\},\qquad C=S\setminus D=\{1,2\}.
\]
Then
\[
2S=G,
\]
and both singleton deletions remain three-fold bases:
\[
3(S\setminus\{0\})=G,\qquad 3(S\setminus\{3\})=G.
\]
But the pair deletion has a hole:
\[
3C=\{0,1,3,4\},\qquad 2\notin3C.
\]

The two retained residues \(1,2\) repair all singleton and pair deleted
patterns if the center is allowed to depend on the pattern:
\[
0+2\in2C,\qquad 3+1\in2C,
\]
and
\[
0+0+1,\ 0+3+1,\ 0+3+2,\ 3+3+2\in3C.
\]
However, no single center works. With \(e=1\), the repairs for \(0+e\) and
\(3+3+e\) fail; with \(e=2\), the repairs for \(3+e\) and \(0+0+e\) fail.

The hole \(2\) diagonalizes against the centers. For \(e=1\),
\[
2-e=1=0+1=3+3,
\]
and the deleted patterns \(\{0\}\) and \(\{3,3\}\) are exactly the ones not
repairable with center \(1\). For \(e=2\),
\[
2-e=0=0+0=2+3,
\]
and the deleted patterns \(\{0,0\}\) and \(\{3\}\) are exactly the ones not
repairable with center \(2\).

Thus a finite-center repair theorem would need a coherence hypothesis: for
each large \(n\), at least one retained center \(e\) must have a
representation of \(n-e\) whose deleted subpattern is repairable with that
same \(e\). Covering the possible deleted patterns by different centers is
algebraically insufficient.

## Lemma 9: Robust two-sum witnesses force domination gaps

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Let \(a\in A\), and suppose
\[
w=a+p\in 2A,\qquad p\in A,
\]
satisfies
\[
w\notin 3(A\setminus\{a\}).
\]
Then
\[
A\cap(p,\ a+p-N_0]\subseteq\{a\}.
\]

Proof. Let \(e\in A\setminus\{a\}\) and suppose
\[
p<e\le a+p-N_0.
\]
Then \(w-e=a+p-e\ge N_0\), so \(w-e\in2A\). If \(w-e\in2(A\setminus
\{a\})\), then adding \(e\) gives
\[
w=e+(w-e)\in 3(A\setminus\{a\}),
\]
contradiction. Hence every two-term representation of \(w-e\) from \(A\)
must use \(a\). But \(w-e<a\), because \(e>p\). A two-term sum of positive
integers using \(a\) is at least \(a+1>a\), impossible. This contradiction
proves the claimed gap. \(\square\)

In particular, dense interval-block constructions cannot protect many
elements by individual robust two-sum witnesses: the partner \(p\) for a
protected element \(a\) must sit so high that almost no other element of
\(A\) lies between \(p\) and \(a+p-N_0\). This is incompatible with naive
full-interval blocks and explains the inefficiency in Lemma 5.

## Lemma 10: General one-point failure forces reflected patterns

Let \(k\ge2\), let \(A\subseteq\mathbb N\) be an asymptotic basis of order
\(k\) with threshold \(N_0\), let \(a\in A\), and put
\[
C=A\setminus\{a\}.
\]
If \(C\) is not an asymptotic basis of order \(k+1\), then for every finite
set \(T\subset C\) and every \(L\), there exist an integer \(n>L\), a
nonempty subset \(U\subseteq T\) with
\[
|U|\ge \left\lceil\frac{|T|}{k-1}\right\rceil,
\]
and an integer \(r\in\{1,\ldots,k-1\}\) such that
\[
n-r a-U\subseteq (k-r)C.
\]
Equivalently, for every \(u\in U\),
\[
n-r a-u\in (k-r)C.
\]

Proof. Since \(C\) is not an order-\((k+1)\) basis, there are arbitrarily
large integers \(n\notin (k+1)C\). Choose such an \(n\) with
\[
n>L,\qquad n>\max T+N_0,\qquad n>\max T+k a.
\]
For each \(t\in T\), the integer \(n-t\) is at least \(N_0\), hence lies in
\(kA\). If \(n-t\in kC\), then
\[
n=t+(n-t)\in (k+1)C,
\]
contradiction. Therefore every \(k\)-term representation of \(n-t\) from
\(A\) uses at least one copy of \(a\).

Choose one such representation and let \(r_t\) be the number of copies of
\(a\) used. The inequality \(n>\max T+k a\) rules out \(r_t=k\), so
\[
r_t\in\{1,\ldots,k-1\}.
\]
The remaining \(k-r_t\) terms lie in \(C\), and therefore
\[
n-r_ta-t\in(k-r_t)C.
\]
By the pigeonhole principle, some value \(r\in\{1,\ldots,k-1\}\) occurs for
at least \(\lceil |T|/(k-1)\rceil\) elements of \(T\). Let \(U\) be those
elements. Then \(n-ra-U\subseteq(k-r)C\), as claimed. \(\square\)

For \(k=2\), Lemma 10 reduces to Lemma 8.

## Corollary 10.2: Infinitely many one-point failures force fractional lower-sumset recurrence

Let \(k\ge2\), and let \(A\subseteq\mathbb N\) be an asymptotic basis of
order \(k\). Suppose there are infinitely many \(a\in A\) such that
\[
A\setminus\{a\}
\]
is not an asymptotic basis of order \(k+1\). Then for every finite
\[
T\subset A
\]
and every \(L\), there exist an integer \(n>L\), a subset
\[
U\subseteq T,\qquad |U|\ge \left\lceil\frac{|T|}{k-1}\right\rceil,
\]
and an integer \(r\in\{1,\ldots,k-1\}\) such that
\[
n-r a-U\subseteq(k-r)A
\]
for some \(a\in A\setminus T\).

Proof. Choose a bad element \(a\in A\setminus T\), possible because there
are infinitely many bad elements. Apply Lemma 10 to
\[
C=A\setminus\{a\}
\]
and the finite set \(T\subset C\). The conclusion gives
\[
n-r a-U\subseteq(k-r)C\subseteq(k-r)A.
\]
\(\square\)

For \(k=2\), this is exactly finite reflection-recurrence of \(A\), because
\(r=1\) and \(k-r=1\). For \(k>2\), the reflected subpattern lands only in a
lower sumset \((k-r)A\), and only a fraction of the original finite pattern
is controlled. This is why Theorem 2.3 does not by itself resolve the
infinitely-bad case in higher order.

## Lemma 10.1: Finite deletion holes force vertex-cover domination

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\) with
threshold \(N_0\). Let \(F\subset A\) be finite, put \(C=A\setminus F\),
and suppose \(w\notin(k+1)C\). Then for every \(e\in C\) with
\[
w-e\ge N_0
\]
the finite set \(F\) intersects every \(k\)-term representation of \(w-e\)
from \(A\).

Equivalently, if \(R_k(x)\) denotes the family of \(k\)-term representation
multisets of \(x\) from \(A\), then
\[
F\text{ is a vertex cover of }R_k(w-e)
\]
for every retained padder \(e\in C\) with \(w-e\ge N_0\).

Proof. If some representation of \(w-e\) from \(A\) avoided \(F\), then it
would be a representation from \(C\). Adding \(e\in C\) would give
\[
w=e+(w-e)\in(k+1)C,
\]
contrary to the assumption. \(\square\)

For \(k=2\), this says that if a finite deletion \(F\) creates a large
order-3 hole \(w\), then every retained small padder \(e\) forces all
two-sum representations of \(w-e\) to pass through \(F\). Thus collective
holes do not avoid the domination phenomenon; they replace one-point
domination by finite vertex-cover domination.

In the special case \(k=2\) and \(F=\{x,y\}\), if \(w\notin3(A\setminus F)\),
then
\[
A\cap[1,w-N_0]\setminus F\subseteq (w-x-A)\cup(w-y-A).
\]
Indeed, for each retained \(e\le w-N_0\), every two-sum representation of
\(w-e\) uses \(x\) or \(y\), so \(w-e=x+a\) or \(w-e=y+a\) for some
\(a\in A\).

## Lemma 10.3: Finite holes force terminal retained gaps

Let \(k\ge2\), and let \(A\subseteq\mathbb N\) be an asymptotic basis of
order \(k\), with threshold \(N_0\), and put \(m_0=\min A\). Let
\(F\subset A\) be finite and nonempty, put \(C=A\setminus F\), and suppose
\[
w\notin(k+1)C.
\]
If \(f_0=\min F\), then
\[
C\cap\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{1}
\]

Proof. Take
\[
e\in C\cap\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr].
\]
Since \(w-e\ge N_0\), there is a \(k\)-term representation of \(w-e\) from
\(A\). By Lemma 10.1, every such representation uses an element of \(F\).
But any \(k\)-term representation using an element of \(F\) has sum at
least
\[
f_0+(k-1)m_0,
\]
whereas \(e>w-f_0-(k-1)m_0\) gives
\[
w-e<f_0+(k-1)m_0.
\]
This contradiction proves (1). \(\square\)

Consequently, if \(F_i\) are finite sets with \(|F_i|\le q\),
\(\min F_i\to\infty\), and witnesses
\[
w_i\notin(k+1)(A\setminus F_i)
\]
satisfying \(w_i-\min F_i\le D\), then such a sequence cannot occur in an
order-\(k\) basis. For (1) gives
\[
A\cap[1,w_i-N_0]\subseteq
[1,D-(k-1)m_0]\cup F_i,
\]
so \(|A\cap[1,w_i-N_0]|\) is bounded, contradicting the fact that an
asymptotic basis of finite order must have an unbounded counting function.

## Lemma 10.4: Bounded higher-excess barriers force lower-sumset reflection

Let \(k\ge2\), and let \(A\subseteq\mathbb N\) be an asymptotic basis of
order \(k\), with threshold \(N_0\). Let
\[
F=\{f_1<\cdots<f_r\}\subset A
\]
be finite, put \(C=A\setminus F\), and suppose
\[
w\notin(k+1)C.
\]
Fix \(j\in\{2,\ldots,r\}\) and \(D\ge0\), and assume
\[
w\le f_j+D. \tag{1}
\]
Let \(T\subset C\) be finite and satisfy
\[
\min T>D,\qquad w-\max T\ge N_0.
\]
Then there are an index \(i<j\) and a subset
\[
U\subset T,\qquad |U|\ge \frac{|T|}{j-1},
\]
such that
\[
w-f_i-U\subseteq (k-1)A. \tag{2}
\]

Proof. For each \(t\in T\), the integer \(w-t\) is at least \(N_0\), so it
has a \(k\)-term representation from \(A\). By Lemma 10.1, every such
representation uses some element of \(F\).

No representation of \(w-t\) can use any \(f_\ell\) with \(\ell\ge j\).
Indeed, (1) gives
\[
w-t-f_\ell\le f_j+D-t-f_\ell\le D-t<0,
\]
whereas the remaining summands in a representation are positive integers.
Hence every chosen representation of \(w-t\) uses one of
\(f_1,\ldots,f_{j-1}\).

Choose one representation for each \(t\). By the pigeonhole principle, some
\(f_i\), \(i<j\), occurs for at least \(|T|/(j-1)\) values of \(t\); call
that subset \(U\). Removing this \(f_i\) from the chosen representations
gives
\[
w-t-f_i\in(k-1)A\qquad(t\in U),
\]
which is (2). \(\square\)

For \(j=2\), all of \(T\) reflects through \(f_1\) into \((k-1)A\). When
\(k=2\), this is genuine reflection-recurrence in \(A\), which is why
Lemma 8.6a can close bounded second-excess barriers in the order-2 case.
For \(k>2\), the reflected pattern lands only in a lower sumset
\((k-1)A\); this is exactly the gap that remains in the robust \(k=3\)
booster-pair attempts.

## Example 11: Residue-padding bases where the answer is yes

For \(k\ge2\), let
\[
A_k=\{1\}\cup k\mathbb N.
\]
Then \(A_k\) is an asymptotic basis of order \(k\), is strongly minimal
under infinite deletions at order \(k\), and has an infinite deletion that
leaves an order-\((k+1)\) basis.

First, \(A_k\) is an order-\(k\) basis. Let \(n\) be large and write
\[
n\equiv r\pmod k,\qquad 0\le r\le k-1.
\]
Then
\[
n=\underbrace{1+\cdots+1}_{r\text{ times}}
  +kq_1+\cdots+kq_{k-r}
\]
with positive integers \(q_i\) chosen so that
\[
q_1+\cdots+q_{k-r}=\frac{n-r}{k};
\]
this is possible for all sufficiently large \(n\).

Second, \(A_k\) is strongly minimal under infinite deletions. Let
\(B\subset A_k\) be infinite. Then \(B\) contains infinitely many multiples
\(b\in k\mathbb N\). For each such \(b\), put
\[
t_b=b+k-1.
\]
In a \(k\)-term sum from \(A_k\), if \(j\) summands are equal to \(1\), then
the residue modulo \(k\) is \(j\). Since \(t_b\equiv k-1\pmod k\) and
\(0\le j\le k\), necessarily \(j=k-1\), leaving exactly one multiple of
\(k\). Equality forces that multiple to be \(b\). Hence if \(b\in B\), then
\[
t_b\notin k(A_k\setminus B).
\]
These witnesses are unbounded, so \(A_k\setminus B\) is not an order-\(k\)
basis.

Finally let
\[
B_0=\{k2^i:i\ge1\},\qquad
D=\mathbb N\setminus\{2^i:i\ge1\}.
\]
We claim that \(D\) is an asymptotic basis of every order \(L\ge2\). For
\(M\ge10\), if \(M-3\) is not a power of two then
\[
M=3+(M-3)\in2D.
\]
If \(M-3\) is a power of two, then \(M-5\) is not a power of two for
\(M\ge10\), since two powers of two differ by \(2\) only in the exceptional
pair \(2,4\). Hence
\[
M=5+(M-5)\in2D.
\]
For \(L>2\), subtract \(3(L-2)\) and pad with \(L-2\) copies of \(3\), so
all sufficiently large \(M\) lie in \(LD\).

Now set
\[
C=A_k\setminus B_0=\{1\}\cup kD.
\]
Let \(n\) be large and \(n\equiv r\pmod k\), \(0\le r\le k-1\). Put
\[
L=k+1-r.
\]
Then \(L\ge2\), and for all sufficiently large \(n\),
\[
\frac{n-r}{k}\in LD.
\]
Writing \((n-r)/k=d_1+\cdots+d_L\) with \(d_i\in D\), we get
\[
n=\underbrace{1+\cdots+1}_{r\text{ times}}
  +kd_1+\cdots+kd_L\in(k+1)C.
\]
Thus \(C\) is an order-\((k+1)\) basis. \(\square\)

## Attempt 12: Digital strongly minimal bases

A Raikov-Stöhr-type construction is a natural source of strongly minimal
order-\(k\) bases. Partition digit positions into \(k\) infinite classes and
let each component consist of numbers whose nonzero digits lie in one class.
The intended order-\(k\) representation splits the digit expansion by these
classes. If one deletes, in a single class, elements with even-size support,
then at order \(k+1\) an even support can be split into two odd supports.

This gives the right combinatorial picture, and it works perfectly in a
formal direct-sum digit monoid. As an integer construction, however, the
argument is incomplete: allowing enough digit coefficients to represent all
integers introduces possible carries in alternative representations, while
restricting to \(0/1\) digits avoids carries but no longer represents all
base-\(q\) digit coefficients with only \(k\) summands. A correct integer
version would need a mixed-radix or spacing device that simultaneously
represents all sufficiently large integers and prevents carry-based
alternative representations in the private-witness argument.

In the clean direct-sum digit monoid, the construction actually supports
the positive direction rather than a counterexample. For \(k=2\), let
\[
M=X\oplus Y
\]
be a direct sum of two free commutative digit monoids and let
\[
A=X\cup Y
\]
with a zero element available for padding. Every \(m=x+y\in M\) lies in
\(2A\). This model is strongly minimal at order \(2\): if infinitely many
elements are deleted from \(X\), then each deleted \(b\in X\) gives
unbounded private witnesses \(b+y\), \(y\in Y\), whose unique mixed
representation uses \(b\).

However, delete the infinite set of positive even-weight elements of \(X\),
and call the remainder \(C\). Every \(x\in X\) is a sum of at most two
retained \(X\)-elements: an odd \(x\) is retained, while a positive
even-weight \(x\) splits as
\[
x=e+(x-e)
\]
with both parts odd by choosing a unit digit \(e\le x\). Hence every
\[
m=x+y
\]
lies in \(3C\). The formal direct-sum construction therefore has the
desired infinite deletion.

Moreover, a faithful carry-free additive embedding of this monoid into
\((\mathbb N,+)\) is impossible once the rank is at least \(2\). If
\(\phi(u)=a\) and \(\phi(v)=b\) for two independent generators, then
\[
\phi(bu)=ba=ab=\phi(av),
\]
although \(bu\ne av\) in the free commutative monoid. Equivalently, bounded
integer digit systems must use carries to represent all coefficients, and
those carries create integer representations absent from the formal monoid.

A finite residue decoration does not remove the basic splitting problem.
Suppose a model has \(k\) digit classes and finite nonempty residue sets
\[
R_1,\ldots,R_k\subseteq G
\]
in an abelian group \(G\), and suppose the residue layer covers every
target residue with one term from each digit class:
\[
R_1+\cdots+R_k=G. \tag{2}
\]
Then for any target residue \(\rho\in G\), any class \(i\), and any
prescribed residue \(r\in R_i\), there is a \((k+1)\)-term residue
representation of \(\rho\) using \(r\) and still using one term from every
digit class. Indeed, by (2),
\[
\rho-r=s_1+\cdots+s_k,\qquad s_j\in R_j,
\]
so
\[
\rho=r+s_1+\cdots+s_k.
\]
Thus residue constraints alone cannot force a \((k+1)\)-term repair to
have exactly one term from a chosen digit class. They always allow an
additional term in that class, which is precisely the residue-level shadow
of splitting the deleted digit component into two retained components.

Thus the digital route currently gives no counterexample: the carry-free
model satisfies the desired conclusion, while an exact additive embedding
into \(\mathbb N\) is unavailable.

## Attempt 13: Staged protected-block counterexample

The most direct route to a counterexample for \(k=2\) is a staged block
construction. At stage \(s\), after all previous protected witnesses have
been placed below a cutoff \(M_s\), one would add a finite block \(S_s\)
above \(M_s\) so that:

1. the enlarged set has \(2A\)-coverage through a new interval ending past
   \(M_s\);
2. every element \(a\in S_s\) has a witness \(w_a\in2A\) with
   \(w_a\notin3(A\setminus\{a\})\);
3. the next stage begins above all \(w_a\), so later elements do not create
   new representations of old witnesses.

Finite safe-marker gadgets from Lemma 5 achieve item 2 against any fixed
old finite set, but they do so inefficiently: the witnesses are far beyond
the interval covered by the block's two-sums. Starting the next block above
those witnesses then leaves a coverage gap. Dense interval blocks solve
item 1 but fail item 2 by Lemma 9, because a protected witness
\(w=a+p\) forces
\[
A\cap(p,\ a+p-N_0]\subseteq\{a\}.
\]

Thus the unresolved construction problem is to find efficient finite blocks
that simultaneously cover up to (or past) their protected witnesses while
satisfying the domination-gap constraints. Current finite searches have
found no nondegenerate examples under small old-shift constraints.

One particularly tempting subattempt fails as follows. Suppose at a finite
stage \(A_s\) has
\[
[0,N_s]\subseteq2A_s
\]
and add a marker \(p_s=N_s+1\). The marker can be used to define candidate
witnesses \(p_s+a\) for old elements \(a\in A_s\), and Lemma 9 suggests
leaving the interval \((p_s,p_s+\max A_s]\) empty. But the new sums involving
\(p_s\) are only
\[
p_s+A_s,
\]
which need not contain the interval \([p_s,p_s+N_s]\). Thus the marker does
not extend coverage unless \(A_s\) itself already contains a long interval.
Adding such dense interval structure restores coverage but immediately
conflicts with the domination gaps required by Lemma 9.

The dense-block conflict can be stated more generally. Let a stage contain
an interval
\[
I=[r,r+L]\cap\mathbb N\subset A_s
\]
and try to protect \(a\in I\) by a marker witness
\[
w=p+a,\qquad p\in A_s.
\]
If there is a retained element \(e\in I\setminus\{a\}\) such that
\[
p+a-e\in[2r+2,\ 2r+2L-2],
\]
then
\[
w\in3(A_s\setminus\{a\}).
\]
Indeed, the displayed central interval lies in \(2(I\setminus\{a\})\) by
Lemma 5.1 with \(m=1\), so
\[
p+a-e=u+v
\]
with \(u,v\in I\setminus\{a\}\), and hence
\[
w=e+u+v\in3(A_s\setminus\{a\}).
\]
Thus a marker witness can be private only if
\[
p+a-(I\setminus\{a\})
\]
avoids the central two-sum interval of \(I\setminus\{a\}\). For interior
points \(a\), this forces the marker far enough from the dense block that
the marker sums no longer bridge the next coverage gap. This is the
interval form of the same coverage-versus-privacy obstruction.

## Proposition 13.1: A finite-stage criterion for a \(k=2\) counterexample

Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots\subset\mathbb N
\]
and increasing endpoints
\[
N_0<N_1<N_2<\cdots
\]
such that, writing \(P_s=A_s\setminus A_{s-1}\), the following hold for all
sufficiently large \(s\):

1. \(P_s\) is finite and nonempty, and every element of \(P_s\) is larger
   than \(N_{s-1}\);
2. the new coverage interval is covered at order 2:
   \[
   [N_{s-1}+1,N_s]\subseteq2A_s;
   \]
3. every new element has a local order-3-private witness below the stage
   endpoint: for every \(a\in P_s\) there is
   \[
   w_{s,a}\in[N_{s-1}+1,N_s]
   \]
   such that
   \[
   w_{s,a}\notin3(A_s\setminus\{a\}).
   \]

Then
\[
A=\bigcup_{s\ge0}A_s
\]
is an asymptotic basis of order \(2\), is strongly minimal under infinite
deletions at order \(2\), and no infinite deletion \(B\subset A\) leaves
\(A\setminus B\) an asymptotic basis of order \(3\). Hence such stages would
give a negative answer to Erdős Problem #881 for \(k=2\).

Proof. The coverage intervals in (2) imply that every sufficiently large
integer lies in \(2A_s\subseteq2A\) for some \(s\), so \(A\) is an order-2
basis.

Let \(B\subset A\) be infinite. Since \(A_0\) and each \(P_s\) are finite,
\(B\) meets infinitely many \(P_s\). Choose \(a_s\in B\cap P_s\) for
infinitely many \(s\). The witnesses \(w_{s,a_s}\) are unbounded because
\[
w_{s,a_s}>N_{s-1}\to\infty.
\]
Moreover,
\[
w_{s,a_s}\notin3(A_s\setminus\{a_s\}).
\]
All elements added after stage \(s\) are larger than \(N_s\), while
\(w_{s,a_s}\le N_s\), so later elements cannot appear in a positive
three-term representation of \(w_{s,a_s}\). Therefore
\[
w_{s,a_s}\notin3(A\setminus\{a_s\}).
\]
Since \(A\setminus B\subseteq A\setminus\{a_s\}\), we have
\[
w_{s,a_s}\notin3(A\setminus B)
\]
for infinitely many unbounded witnesses. Thus \(A\setminus B\) is not an
order-3 basis. A fortiori it is not an order-2 basis. \(\square\)

This proposition is currently only a reduction. Lemmas 5.1 and 9 explain
why the most obvious dense-interval/marker stages fail.

After Corollary 8.3, this singleton stage route is known to be impossible
for \(k=2\). Indeed, the conclusion of the stage hypotheses would make
infinitely many one-point deletions fail at order \(3\), while Corollary
8.3 says that any order-2 basis with infinitely many such one-point
failures has a good infinite deletion. Thus Proposition 13.1 is best read
as a diagnostic for why naive private-witness block constructions cannot
exist in the \(k=2\) setting.

## Proposition 13.1b: Stage barriers need only be unbounded

The singleton protection in Proposition 13.1 can be replaced by any
unbounded finite-barrier system.

Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots\subset\mathbb N
\]
and increasing endpoints \(N_s\to\infty\) such that, for all sufficiently
large \(s\),
\[
[N_{s-1}+1,N_s]\subseteq2A_s
\]
and every element added after stage \(s\) is larger than \(N_s\). Let
\[
A=\bigcup_s A_s.
\]
Suppose further that there is a finite-uniform hypergraph
\(\mathcal F\) on \(A\) and, for every \(F\in\mathcal F\), a stage
\(s(F)\) and a witness \(w_F\) such that
\[
F\subset A_{s(F)},\qquad w_F\le N_{s(F)},\qquad
w_F\notin3(A_{s(F)}\setminus F),
\]
and such that \(\mathcal F\) is an unbounded barrier with respect to
\(F\mapsto w_F\):
for every infinite \(B\subset A\) and every \(L\), there is
\[
F\in\mathcal F,\qquad F\subset B,\qquad w_F>L.
\]

Then \(A\) is an asymptotic basis of order \(2\), and no infinite
\(B\subset A\) leaves \(A\setminus B\) an asymptotic basis of order \(3\).

Proof. The interval coverage gives the order-2 basis property. Let
\(B\subset A\) be infinite and let \(L\) be arbitrary. Choose
\(F\in\mathcal F\) with \(F\subset B\) and \(w_F>L\). Since every element
added after stage \(s(F)\) is larger than \(N_{s(F)}\ge w_F\), no later
element can occur in a positive three-term representation of \(w_F\). Hence
\[
w_F\notin3(A\setminus F).
\]
Because \(F\subset B\),
\[
A\setminus B\subseteq A\setminus F,
\]
so
\[
w_F\notin3(A\setminus B).
\]
As this holds for arbitrarily large \(L\), the set \(A\setminus B\) is not
an order-3 basis. \(\square\)

This proposition does not by itself prove strong minimality at order \(2\).
For a full counterexample to Erdős Problem #881, the same construction must
also ensure that every infinite deletion destroys order \(2\). Proposition
13.1 achieves that because every new singleton has an order-3-private
witness, hence also an order-2-private witness. In the more general
barrier form, order-2 minimality must be supplied separately or by a second
unbounded barrier for two-term representations.

## Proposition 13.1b-general: General finite-stage barrier criterion

Let \(k\ge1\). Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots\subset\mathbb N
\]
and increasing endpoints \(N_s\to\infty\) such that, for all sufficiently
large \(s\),
\[
[N_{s-1}+1,N_s]\subseteq kA_s
\]
and every element added after stage \(s\) is larger than \(N_s\). Let
\[
A=\bigcup_s A_s.
\]
Suppose further that there is a finite-uniform hypergraph
\(\mathcal F\) on \(A\) and, for every \(F\in\mathcal F\), a stage
\(s(F)\) and a witness \(w_F\) such that
\[
F\subset A_{s(F)},\qquad w_F\le N_{s(F)},\qquad
w_F\notin(k+1)(A_{s(F)}\setminus F),
\]
and such that \(\mathcal F\) is an unbounded barrier with respect to
\(F\mapsto w_F\): for every infinite \(B\subset A\) and every \(L\), there
is
\[
F\in\mathcal F,\qquad F\subset B,\qquad w_F>L.
\]

Then \(A\) is an asymptotic basis of order \(k\), and for every infinite
\(B\subset A\), the set \(A\setminus B\) is not an asymptotic basis of
order \(k+1\). Consequently \(A\setminus B\) is not an asymptotic basis of
order \(k\) either.

Proof. The interval coverage gives the order-\(k\) basis property. Let
\(B\subset A\) be infinite and \(L\) arbitrary. Choose
\[
F\in\mathcal F,\qquad F\subset B,\qquad w_F>L.
\]
All elements added after stage \(s(F)\) are larger than
\(N_{s(F)}\ge w_F\), so no later element can appear in a positive
\((k+1)\)-term representation of \(w_F\). Hence the local nonrepresentation
persists:
\[
w_F\notin(k+1)(A\setminus F).
\]
Since \(F\subset B\), we have \(A\setminus B\subseteq A\setminus F\), and
therefore
\[
w_F\notin(k+1)(A\setminus B).
\]
These missing witnesses are unbounded as \(L\to\infty\), so
\(A\setminus B\) is not an order-\((k+1)\) basis. If \(A\setminus B\) were
an order-\(k\) basis and nonempty, padding would make it an order-\((k+1)\)
basis; if it is empty or finite, it is not an asymptotic basis. Thus it is
not an order-\(k\) basis either. \(\square\)

For \(k=2\), this is Proposition 13.1b. For \(k=3\), the robust-booster
pair-stage searches are attempts to realize this criterion with
\(\mathcal F\) consisting of cross-stage pairs.

## Lemma 13.1d: Positive-summand buffer needed for any staged construction

Let \(A_s\subset\mathbb N\) be a finite stage, let \(m=\min A_s\), and let
\(N_s\) be a declared endpoint. Suppose every element added after stage
\(s\) is larger than \(N_s\). If the final union \(A\) is to be an
asymptotic basis of order \(k\), then the current stage must already cover
the immediate buffer
\[
[N_s+1,\ N_s+(k-1)m]\subset kA_s
\]
for all sufficiently large \(s\).

Proof. If
\[
n\le N_s+(k-1)m,
\]
then any \(k\)-term representation of \(n\) that uses a later element is at
least
\[
(N_s+1)+(k-1)m>n,
\]
because all summands are positive and every old or later summand is at
least \(m\). Hence every eventual \(k\)-term representation of such \(n\)
must already lie in \(kA_s\). \(\square\)

For the \(k=2\) stage criteria this requires a one-point buffer beyond the
declared endpoint; for the possible \(k=3\) adjacent-order route it requires
a two-point buffer when \(m=1\). This explains why endpoint witnesses in
Examples 13.2 and in the finite \(k=3\) searches do not immediately
iterate.

## Proposition 13.1c: Cross-stage pair barriers would give a counterexample

Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots\subset\mathbb N
\]
and increasing endpoints \(N_s\to\infty\), and write
\[
P_s=A_s\setminus A_{s-1}.
\]
Assume that, for all sufficiently large \(s\):

1. \(P_s\) is nonempty and every element of \(P_s\) is larger than
   \(N_{s-1}\);
2. the new interval is covered at order \(2\):
   \[
   [N_{s-1}+1,N_s]\subseteq2A_s;
   \]
3. every cross-stage pair has a local order-3-private witness: for every
   \[
   a\in A_{s-1},\qquad b\in P_s,
   \]
   there is
   \[
   w_{s,a,b}\in[N_{s-1}+1,N_s]
   \]
   such that
   \[
   w_{s,a,b}\notin3(A_s\setminus\{a,b\}).
   \]

Then
\[
A=\bigcup_s A_s
\]
is an asymptotic basis of order \(2\), is strongly minimal under infinite
deletions at order \(2\), and no infinite deletion \(B\subset A\) leaves
\(A\setminus B\) an asymptotic basis of order \(3\). Hence such stages
would give a negative answer to Erdős Problem #881 for \(k=2\).

Proof. The interval coverage gives the order-2 basis property. Let
\(B\subset A\) be infinite. Since the stages are finite, \(B\) meets
infinitely many increments \(P_s\). Choose
\[
a\in B\cap P_i
\]
for some sufficiently large stage \(i\). Then for infinitely many
\(s>i\), the set \(B\cap P_s\) is nonempty; choose \(b_s\in B\cap P_s\).
For each such \(s\), the pair \(\{a,b_s\}\) has a witness
\[
w_{s,a,b_s}\in[N_{s-1}+1,N_s].
\]
All elements added after stage \(s\) are larger than \(N_s\), so they cannot
occur in a positive three-term representation of \(w_{s,a,b_s}\). Therefore
\[
w_{s,a,b_s}\notin3(A\setminus\{a,b_s\}).
\]
Since
\[
A\setminus B\subseteq A\setminus\{a,b_s\},
\]
we have
\[
w_{s,a,b_s}\notin3(A\setminus B)
\]
for unbounded \(s\), and the witnesses are unbounded because
\(w_{s,a,b_s}>N_{s-1}\to\infty\). Hence \(A\setminus B\) is not an order-3
basis, and a fortiori it is not an order-2 basis. \(\square\)

This criterion targets the finitely-bad \(k=2\) obstruction: singleton
deletions may be harmless at order \(3\), while cross-stage pairs form an
unbounded barrier. No construction satisfying the stage hypotheses is known
in this workspace.

Corollary 8.6b further restricts this route. In any cross-stage pair
construction that evades the positive theorem, the witnesses for pairs
\[
a<b,\qquad a\in A_{s-1},\ b\in P_s,
\]
cannot have \(w_{s,a,b}-b\) bounded on every infinite tail. Persistent pair
barriers must have unbounded top excess, or else tail reflection-recurrence
would give a good deletion.

The greedy script `EXPERIMENTS/cross_stage_pair_search.py` finds
\[
\{1,2\}\to\{1,2,3\}\to\{1,2,3,5\}
\]
and then stalls. The bounded DFS script
`EXPERIMENTS/cross_stage_pair_dfs.py` shows that this two-stage stall is
partly a greedy artefact: it finds the non-greedy chain
\[
\{1,2\}\to\{1,2,4\}\to\{1,2,4,6,7\}
   \to\{1,2,4,6,7,8\}
\]
with declared endpoints \(4,7,15\). The same default DFS bounds find no
fourth stage. This is finite evidence only, but it locates the construction
pressure more accurately: after several old elements are present, a new
block must protect many old-new pairs simultaneously while still leaving
the positive-summand coverage buffer from Lemma 13.1d.

The distinction between formal pair holes and genuinely collective pair
holes matters. With the script's `--minimal` flag, each old-new witness is
required to be repaired after restoring either endpoint of the pair. Under
the same default bounds the search finds only
\[
\{1,2\}\to\{1,2,4,5\}
\]
with endpoint \(9\), and no second stage. This agrees with the theoretical
picture after Corollary 8.3b: in the unresolved \(k=2\) case, degenerate
old-singleton witnesses must eventually disappear, leaving much harder
minimal collective barriers.

## Proposition 13.1e: Cross-stage pairs in order \(k\)

Let \(k\ge1\). Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots\subset\mathbb N
\]
and increasing endpoints \(N_s\to\infty\), and write
\[
P_s=A_s\setminus A_{s-1}.
\]
Assume that, for all sufficiently large \(s\):

1. \(P_s\) is nonempty and every element of \(P_s\) is larger than
   \(N_{s-1}\);
2. the new interval is covered at order \(k\):
   \[
   [N_{s-1}+1,N_s]\subseteq kA_s;
   \]
3. every cross-stage pair has a local order-\((k+1)\)-private witness: for
   every
   \[
   a\in A_{s-1},\qquad b\in P_s,
   \]
   there is
   \[
   w_{s,a,b}\in[N_{s-1}+1,N_s]
   \]
   such that
   \[
   w_{s,a,b}\notin(k+1)(A_s\setminus\{a,b\}).
   \]

Then
\[
A=\bigcup_s A_s
\]
is an asymptotic basis of order \(k\), and no infinite deletion
\(B\subset A\) leaves \(A\setminus B\) an asymptotic basis of order
\(k+1\). Hence \(A\) is strongly minimal under infinite deletions at order
\(k\).

Proof. This is a special case of Proposition 13.1b-general. Let
\(\mathcal F\) be the family of cross-stage pairs \(\{a,b\}\) with
\(a\in A_{s-1}\) and \(b\in P_s\) for sufficiently large \(s\), and assign
the witness \(w_{s,a,b}\). Every infinite \(B\subset A\) meets infinitely
many stage increments. Choose one element
\[
a\in B
\]
from a sufficiently large stage. Then \(B\) meets infinitely many later
increments \(P_s\); for each such \(s\), choose \(b_s\in B\cap P_s\). The
pairs \(\{a,b_s\}\) lie in \(\mathcal F\) and have witnesses
\[
w_{s,a,b_s}>N_{s-1}\to\infty.
\]
Thus \(\mathcal F\) is an unbounded barrier, and Proposition
13.1b-general applies. \(\square\)

The script `EXPERIMENTS/robust_booster_pair_stage_search.py` is a finite
\(k=3\) search for this criterion with a retained booster.

## Example 13.2: An isolated endpoint stage

Proposition 13.1 is not locally inconsistent. Let \(a\ge4\) be even and put
\[
N=a-1,\qquad A_{s-1}=\{1,3,5,\ldots,a-1\},\qquad P_s=\{a\}.
\]
Then with
\[
A_s=A_{s-1}\cup\{a\},\qquad N_s=2a,
\]
the interval \([N+1,N_s]=[a,2a]\) is contained in \(2A_s\). Indeed, if
\(n\) is odd and \(a<n<2a\), then
\[
n=a+(n-a),
\]
where \(n-a\) is an odd element of \(A_{s-1}\). If \(n\) is even and
\(a\le n\le2a-2\), then
\[
n=(a-1)+(n-a+1),
\]
and both summands are odd elements of \(A_{s-1}\). Finally \(2a=a+a\).

The new element \(a\) has the local private witness
\[
w_{s,a}=2a.
\]
After deleting \(a\), the remaining set consists only of odd numbers, so
every three-term sum from \(A_s\setminus\{a\}\) is odd. Therefore
\[
2a\notin3(A_s\setminus\{a\}).
\]

This shows that the finite-stage obstruction is not purely local. The stage
avoids Lemma 9 because the witness is the endpoint sum \(a+a\): with
\(p=a\) and threshold \(N+1=a\), the forbidden interval
\[
(p,\ w_{s,a}-(N+1)]
\]
is empty. It also avoids Lemma 5.1 because the old set is a progression of
odd numbers, not a dense integer interval.

The stage does not iterate by itself. It leaves no two-sum buffer beyond
\(N_s=2a\). Since the next stage's new elements must all be larger than
\(N_s\), the first integer after \(N_s\) would already have to be covered by
old two-sums. Thus an iterable counterexample still needs stages whose
private witnesses lie below the end of a longer covered buffer, or a
weaker infinite construction in which only a cofinite protected subset of
the added elements needs local witnesses.

## Attempt 14: The affine finite-booster construction is not verified

The 2026-05-03 comment on the problem page links a proposed negative
construction for every \(k\ge2\). Its local witness lemma has the following
shape: after a finite set \(S\) and an element \(c\in S\) have been chosen,
one adjoins fresh variables so that a number \(p\) has a
\((k+1)\)-term representation using \(c\), but no \((k+1)\)-term
representation after \(c\) is deleted. The proof avoids finitely many affine
hyperplanes corresponding to forbidden formal representations.

This is not enough for a staged asymptotic basis. Once the old set already
covers a long interval at order \(k\), a genuine hole
\[
p\notin(k+1)(A\setminus\{c\})
\]
forces shifted domination: for every retained padder \(e\) with \(p-e\) in
the covered range, every \(k\)-term representation of \(p-e\) from \(A\)
must use \(c\). In the notation of Lemma 10.1, the singleton \(\{c\}\) must
be a vertex cover for all the representation hypergraphs of these shifted
targets.

For \(k=2\), this obstruction is decisive. Lemma 8 and Theorem 8.2 prove
that an order-2 basis with infinitely many one-point order-3 failures is
finitely reflection-recurrent and therefore has an infinite deletion that
remains an order-3 basis. Hence the linked construction, which claims
one-point order-3 private witnesses for every element of an order-2 basis,
cannot be correct as stated.

The first unproved compatibility point is therefore not the purely local
affine avoidance, but the simultaneous requirement that all shifted targets
\(p-e\) remain covered only through representations using \(c\). Finite
experiments in `EXPERIMENTS/stage_buffer_search.py` and
`EXPERIMENTS/cross_stage_pair_search.py` continue to find only endpoint or
short-chain artefacts unless this shifted-domination requirement is weakened
to collective barriers.

Here is a direct finite obstruction to the lemma's interval-placement
claim when \(k=2\). Take
\[
S=\{2\}\cup [R,2R],\qquad c=2,
\]
and prescribe the interval
\[
J=[2R+1,4R+1].
\]
For every \(p\in J\), one has
\[
p-1\in[2R,4R]\subset 2(S\setminus\{2\}).
\]
Therefore
\[
p\in 1+2(S\setminus\{2\})
\subset 3((S'\setminus\{2\})\cup\{1\})
\]
for every later enlargement \(S'\supset S\). No choice of fresh variables
inside this interval can make \(p\) private after deleting \(2\). In the
linked staged construction, the old coverage block already supplies exactly
this kind of shifted two-sum coverage for the interval where the next
\(p_s\) is prescribed.

## Attempt 15: Adjacent-order minimality for \(k=3\)

A possible negative route for \(k\ge3\) is to construct an asymptotic
order-\(k\) basis \(A\) that is ordinary minimal as an order-\((k+1)\)
basis. This would imply the desired no-answer only if the order-\((k+1)\)
private elements are cofinite in \(A\), or if they are replaced by an
unbounded finite-barrier family. Indeed, if \(P\subset A\) is the set of
elements having unbounded one-point order-\((k+1)\) witnesses, then every
infinite \(B\subset A\) meets \(P\) infinitely often if and only if
\(A\setminus P\) is finite.

The experiment `EXPERIMENTS/adjacent_stage_search.py` tests the first
nontrivial case \(k=3\). Starting from
\[
A_0=\{1,2,3\},
\]
the greedy singleton search finds local stages
\[
\{1,2,3\}\to\{1,2,3,6\}\to\{1,2,3,6,14\},
\]
with order-4 private witnesses \(13\) for \(6\) and \(22\) for \(14\).
These are endpoint-style stages: after the second stage, three-sum coverage
extends only to \(23\), leaving at most the two-point buffer required by
Lemma 13.1d.

Searching with the buffer imposed finds only short chains in small ranges,
for example
\[
\{1,2,3\}\cup\{4,11\},\qquad
\{1,2,3\}\cup\{7,10\},
\]
and then a second stage such as adjoining \(23\). No third buffered
singleton stage was found within the tested bounds. This is finite evidence
only, but it reinforces the structural obstruction from Lemma 10.3:
singleton order-4 holes force terminal retained gaps, so cofinally many
singletons with bounded excess cannot coexist with order-3 coverage.

The more plausible \(k=3\) negative route is therefore the same as in the
remaining \(k=2\) case: unbounded collective barriers, such as cross-stage
pairs, rather than cofinite singleton private witnesses.

## Attempt 16: Robust residue boosters for \(k=3\)

There is a finite cyclic model for a negative construction with a retained
booster. In \(G=\mathbb Z/10\mathbb Z\), set
\[
S=\{0,1,3\},\qquad f=5.
\]
Then
\[
4S=G,\qquad 3(S\cup\{f\})=G.
\]
Moreover, deleting any residue in \(S\) leaves a four-fold hole even though
the booster \(f\) remains:
\[
4(\{1,3,5\})\subseteq 2\mathbb Z/10\mathbb Z,
\]
so deleting \(0\) misses every odd residue, while direct calculation gives
\[
7\notin4\{0,3,5\},\qquad
9\notin4\{0,1,5\}.
\]
Thus the residue-level pattern has exactly the desired order mismatch:
\(S\) is a four-fold residue basis, adjoining one finite booster lowers the
residue order to three, and the four-fold private residue holes survive
with the booster retained.

This does not yet lift to an integer counterexample. A thick lift of the
three residue classes loses single-integer privacy: deleting one integer in
the class \(s\) leaves many other integers of residue \(s\), and central
quotient representations can replace the deleted lift. A successful lift
would need endpoint or block gadgets that force the required residue \(s\)
to be realized by one prescribed integer while retaining enough three-term
coverage, including the buffer of Lemma 13.1d.

The script `EXPERIMENTS/robust_booster_residue.py` records this search. It
is a better finite seed than the invalid affine booster attempt, but the
integer lifting problem remains open in this workspace.

The companion script `EXPERIMENTS/robust_booster_stage_search.py` searches
for finite integer stages using this residue pattern. It finds the local
buffered extension
\[
C_0=\{1,3,20,21\},\quad f=5,\quad
C_1=C_0\cup\{30,31\}.
\]
With
\[
A_1=C_1\cup\{5\},
\]
three-fold sums cover through \(47\), and the new elements have robust
four-fold witnesses
\[
37\notin4(A_1\setminus\{30\}),\qquad
38\notin4(A_1\setminus\{31\}).
\]
The declared endpoint can be \(38\), leaving the two-point buffer required
for an order-3 staged construction. The default greedy search then stalls
at the next stage. Thus the residue pattern has nontrivial finite
integer traction, but not yet an iterable construction.
The script's `--extend` mode exhausts possible next increments of size at
most \(5\) using elements up to \(120\), and tries random increments of
sizes \(6,\ldots,12\); it still finds no continuation. This is heuristic
evidence that the lift needs a more global block design or collective
barriers, not a proof of impossibility.

The cross-stage pair version has slightly more traction. The script
`EXPERIMENTS/robust_booster_pair_stage_search.py` starts from the same
\(C_0=\{1,3,20,21\}\), first adds \(23\), and then adds \(30,31\). At each
of these two stages, every old-new pair has a four-fold witness below the
declared endpoint, and the three-fold coverage interval leaves the required
two-point buffer. The next stage stalls in the default search. Its
`--extend` mode exhausts increments of size at most \(4\) using elements up
to \(160\), and tries random increments of sizes \(5,\ldots,12\), finding no
third extension.
Its diagnostic mode shows the immediate failure: among singleton candidates
in the prescribed residue classes, only \(41\) and \(43\) extend coverage,
and both fail the pair-witness condition against the old elements
\[
1,\ 3,\ 21,\ 23,\ 31.
\]
Thus the obstruction is not merely lack of coverage; it is simultaneous
domination for many old elements.

## Dependency Graph

* Reduction 0 shows that the stated infinite-deletion minimality hypothesis
  is redundant for counterexamples. The problem is equivalent to the broader
  assertion that every order-\(k\) asymptotic basis has an infinite deletion
  that remains order \(k+1\).
* Theorem 1 is independent and resolves \(k=1\).
* Lemma 2 would imply the desired conclusion if an infinite \(B\) satisfying
  the two absorption hypotheses can be forced.
* Lemma 2.2 gives the general multi-hit repair criterion: a fixed retained
  padder may absorb any multiset of at most \(k\) deleted summands.
* Theorem 2.3 proves that finite reflection-recurrence gives a good infinite
  deletion in every order, using balanced repair certificates.
* Lemma 2.4 shows that reflection-recurrence only on a tail of \(A\) is
  enough, because the certificate construction can be initialized entirely
  in that tail.
* Lemma 2.1 reformulates the strong minimality hypothesis as a finite
  barrier property for order-\(k\) representations.
* Warning 3.0 explains why finite deletability alone is insufficient without
  threshold control.
* Example 3.0a shows that strong order-2 minimality does not control
  order-3 thresholds for arbitrary finite prefixes, even in the benign
  basis \(\{1\}\cup2\mathbb N\).
* Lemma 3 would imply the desired conclusion if an infinite late-deletable
  reservoir exists.
* Corollary 3.1 says any counterexample must eventually block all large
  late-deletable one-point removals at order \(k+1\).
* Corollary 3.1b reformulates the threshold obstruction as late-bad finite
  prefixes.
* Corollary 3.1c says the late-bad finite sets must form a barrier on \(A\)
  in any counterexample.
* Lemma 3.2 proves the theorem under an arbitrarily-large protected matching
  hypothesis for \((k+1)\)-representations.
* Corollary 3.3 converts failure of the broad positive theorem into bounded
  moving transversals for representation hypergraphs.
* Proposition 3.4 proves the conclusion for bases with sufficiently
  redundant \((k+1)\)-representations.
* Lemma 3.5 identifies bounded transversals with shifted finite barriers
  and gives a local one-gate gadget showing why order-\(k\) coverage alone
  cannot force the protected-matching hypothesis.
* Lemma 3.5a shows that bounded transversals also dominate shifts by
  protected elements, provided the shifted target is too large for the
  finite protected core alone.
* The counterexample reduction would disprove the problem for \(k\ge 2\) if
  a block construction supplies robust private witnesses for all but
  finitely many elements.
* Counterexample Reduction 2 weakens this to unbounded finite protected
  barriers: every infinite deletion must contain protected finite sets with
  arbitrarily large witnesses. The unboundedness clause is necessary.
* Lemma 4 supplies arbitrarily large finite local gadgets for the
  counterexample route, but the cross-block repair paragraph explains why
  these gadgets do not by themselves solve the problem.
* Lemma 5 proves that finite safe private witnesses can be built against any
  fixed finite set of earlier shifts. It shifts the counterexample problem to
  finding efficient safe gadgets whose protected witnesses are not too far
  beyond their coverage intervals.
* Lemma 5.1 shows dense interval blocks repair almost all marker witnesses
  after finite deletions.
* Lemma 6 rules out a purely residue-class finite-accelerator
  counterexample.
* Lemma 6.1 explains why finite cyclic one-residue essentiality does not
  lift to single-integer private witnesses in thick residue blocks, except
  near endpoints.
* Example 7 is a test case showing the desired conclusion for a nontrivial
  strongly minimal order-2 basis.
* Proposition 7.1 proves the desired conclusion for all eventually periodic
  asymptotic bases.
* Lemma 8 gives a necessary condition for one-point deletion to fail at
  order 3 in an order-2 basis.
* Corollary 8.1 says infinitely many such failures force finite
  reflection-recurrence of \(A\).
* Lemma 8.2a isolates the repair criterion used to turn a carefully chosen
  infinite deletion into an order-3 basis.
* Theorem 8.2 proves that finite reflection-recurrence gives an infinite
  deletion preserving order 3.
* Corollary 8.3 therefore resolves the \(k=2\) problem whenever infinitely
  many one-point deletions fail at order 3.
* Lemma 8.3a also resolves the case where infinitely many one-point
  deletions are order-3 bases but only with thresholds at least as large as
  the deleted element.
* Corollary 8.3b says every remaining \(k=2\) counterexample has, after a
  finite exceptional set, only non-singleton late-bad barriers.
* Lemma 8.4 identifies the remaining \(k=2\) finitely-bad case as a
  collective finite-barrier problem with reflected-cover domination.
* Lemma 8.4a strengthens the domination picture: any finite order-3 hole
  after deleting \(F\) creates a retained gap below the witness, from
  \(w-\min F-\min A\) up to \(w-N_0\).
* Lemma 8.4b puts collective holes in inclusion-minimal normal form: every
  surviving deleted element is used in a three-term repair after the other
  deleted elements are restored. The finite example following it shows that
  such a minimal collective hole need not contain a bad pair subhole.
* Warning 8.5 records that bounded-width barriers do not automatically
  reduce to one fixed uniformity, and that abstract barriers need not have
  bounded width on any infinite tail.
* Lemma 8.5a says that if bounded width is supplied by arithmetic, Ramsey
  thinning reduces the late-bad barrier to one fixed uniformity on an
  infinite tail.
* Lemma 8.6 shows that bounded-width barriers with large witness excess
  force partial reflection-recurrence.
* Lemma 8.6a proves that finite barriers whose witnesses have bounded
  excess over the second-smallest deleted element force tail
  reflection-recurrence and hence a good deletion.
* Corollary 8.6b gives the pair-barrier consequence: bounded top-excess
  pair barriers cannot persist in a counterexample.
* Lemma 8.6c sharpens partial recurrence to arbitrarily large finite
  recurrent clusters, but also records two obstructions: fractional
  recurrence does not compact to an infinite recurrent core, and fixed
  recurrent clusters do not support the adaptive mirrors in Theorem 2.3.
* Example 8.6d shows that unbounded second-excess minimal collective holes
  are locally compatible with strong order-2 minimality and singleton
  order-3 stability; any bounded-second-excess reduction must use the
  global barrier hypothesis over every infinite deletion.
* Example 8.7 shows that pair barriers can be irreducibly multi-centered at
  the residue level, so Lemma 8.6 cannot be upgraded by a simple pigeonhole
  argument.
* Example 8.8 shows that finite-center repair conditions need coherence:
  repairing different deleted patterns with different retained centers does
  not by itself imply an order-3 basis after deletion.
* Lemma 9 gives a necessary domination-gap condition for individual robust
  two-sum witnesses in the \(k=2\) counterexample route.
* Lemma 10 generalizes Lemma 8 to arbitrary \(k\), replacing translates of
  \(A\setminus\{a\}\) by translates into lower sumsets.
* Corollary 10.2 says infinitely many one-point failures in general order
  force only fractional recurrence into lower sumsets; for \(k=2\) this
  becomes full reflection-recurrence.
* Lemma 10.1 records the finite-vertex-cover obstruction for collective
  holes after finite deletions.
* Lemma 10.3 strengthens this for all orders: a finite
  order-\((k+1)\) hole after deleting \(F\) forces a terminal retained gap
  below the witness, starting at \(w-\min F-(k-1)\min A\).
* Lemma 10.4 records the higher-order analogue of bounded second-excess
  barriers: they force large reflected subpatterns into lower sumsets
  \((k-1)A\), which becomes full recurrence only when \(k=2\).
* Example 11 gives a residue-padding family satisfying the desired
  conclusion for every \(k\ge2\).
* Attempt 12 records that the clean direct-sum digital model satisfies the
  desired conclusion, while a faithful carry-free embedding into
  \(\mathbb N\) is impossible.
* Attempt 13 records the staged protected-block counterexample route and
  the coverage-versus-witness-efficiency gap.
* Proposition 13.1 gives a precise finite-stage criterion that would produce
  a \(k=2\) counterexample if suitable stages can be built.
* Proposition 13.1b replaces singleton stage protection by an unbounded
  finite-barrier system, while noting that order-2 minimality then needs a
  separate proof.
* Proposition 13.1b-general gives the same finite-stage barrier criterion
  for every order \(k\), and observes that failure at order \(k+1\)
  automatically gives strong infinite-deletion minimality at order \(k\).
* Proposition 13.1c gives a concrete pair-barrier stage criterion: protecting
  every old-new pair would already produce a \(k=2\) counterexample.
* Lemma 13.1d records the positive-summand buffer condition that every
  staged construction must satisfy before moving all future elements past
  the declared endpoint.
* Proposition 13.1e extends the cross-stage pair criterion to every order
  \(k\); the robust \(k=3\) booster-pair experiments are finite searches for
  this criterion.
* Example 13.2 gives an isolated stage satisfying the local conditions, but
  explains why endpoint witnesses do not provide the buffer needed for an
  iteration.
* Attempt 14 records why the commented affine finite-booster construction is
  not a verified counterexample: local affine avoidance does not prove the
  shifted domination forced by existing order-\(k\) coverage, and for
  \(k=2\) the claimed singleton-private pattern contradicts Theorem 8.2.
* Attempt 15 records the adjacent-order minimality route for \(k=3\); small
  buffered singleton searches stall, pointing again toward collective
  finite barriers as the only viable negative mechanism.
* Attempt 16 gives a robust cyclic booster pattern for \(k=3\), while
  isolating the remaining lift problem: private residue holes must be made
  private for individual integers without losing three-term coverage.
