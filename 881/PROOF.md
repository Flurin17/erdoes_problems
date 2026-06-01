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

For \(k=2\), the current reductions rule out:

* infinitely many singleton order-3 failures;
* bounded-excess fixed-prefix pair barriers;
* fixed-rank full list-color high-excess barriers;
* cofinite recurrent finite-color Sidon tails;
* the enumerated-Schreier counterexample route.

The remaining \(k=2\) obstruction, if it exists, must be a genuinely
variable-rank collective finite-barrier system that avoids compacting to a
finite recurrent certificate-free coloring.

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

There is an immediate easy case. If \(A\) contains a co-infinite subset
\[
P\subset A
\]
which is still an order-\(k\) basis, then choose any infinite
\[
B\subset A\setminus P.
\]
The set \(A\setminus B\) contains \(P\), so it is an order-\(k\) basis and
hence, by monotonicity, an order-\((k+1)\) basis. Thus the only hard case of
the broader theorem is precisely the case where every infinite deletion
destroys the order-\(k\) basis property, i.e. the minimality hypothesis from
the original problem.

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

There is a related finite-core target that should not be confused with the
full theorem. One might try to prove that there is a finite core
\[
E\subset A
\]
such that for every finite
\[
F\subset A\setminus E
\]
the set \(A\setminus F\) is an order-\((k+1)\) basis. No example in this
workspace currently refutes that statement. But it would still be
insufficient by itself: Lemma 3.1d says that a fixed infinite deletion is
good exactly when all its finite subdeletions share one common eventual
threshold. Warning 3.0 and Example 3.0a show that finite deletions may be
eventually harmless while their thresholds drift past the deleted elements.

If the finite-core target fails, then for every finite \(E\subset A\) there
is a finite \(F\subset A\setminus E\) such that \(A\setminus F\) has
arbitrarily large order-\((k+1)\) holes. Lemma 10.3 then forces terminal
retained gaps outside every protected finite core. This is stronger than
the delayed finite-prefix holes in \(\{1\}\cup2\mathbb N\), where finite
deletions are still eventually order \(3\).

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

## Lemma 2.3b: A fixed recurrent certificate tuple is enough

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\). Suppose
there are elements
\[
e,y_1,\ldots,y_k\in A,\qquad y_i\ne e,
\]
such that:

1. the finite set
   \[
   R=\{e,y_1,\ldots,y_k\}
   \]
   is reflection-recurrent in \(A\), meaning that for every \(L\) there is
   \(m>L\) with
   \[
   m-R\subset A;
   \]
2. for every \(d=1,\ldots,k\), there is \(x_d\in A\) satisfying
   \[
   y_1+\cdots+y_d=(d-1)e+x_d. \tag{1}
   \]

Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(k+1\).

Proof. This is the second half of Theorem 2.3 with the initial
certificates supplied in advance. Initialize the empty-multiset
certificates by
\[
Y(\varnothing,d)=(y_1,\ldots,y_d),\qquad X(\varnothing,d)=(x_d)
\]
for \(d=1,\ldots,k\), and put \(e,x_1,\ldots,x_k\) into the protected set
\(P\). Identity (1) is exactly the certificate identity
\[
\sigma(\varnothing)+y_1+\cdots+y_d=(d-1)e+\sum_{x\in X(\varnothing,d)}x.
\]

Now run the deletion recursion from Theorem 2.3. At each stage the set of
\(Y\)-entries appearing in all current certificates is a subset of
\(\{y_1,\ldots,y_k\}\). This is true initially, and the propagation rule in
Theorem 2.3 defines each new \(Y(S',d)\) as a prefix of an older
\(Y(S,\ell+d)\). Therefore the only recurrence needed at any stage is the
fixed recurrence of
\[
R=\{e,y_1,\ldots,y_k\}.
\]
Choose the recurrent center \(m\) sufficiently large and outside the
finite set of values that would make the new deleted element or any new
protected mirror collide with the already deleted set.

The certificate propagation and the repair identity
\[
e+\sigma(D)\in(|D|+1)(A\setminus B),\qquad 1\le |D|\le k,
\]
are then identical to Theorem 2.3. Lemma 2.2 gives that \(A\setminus B\)
is an order-\((k+1)\) basis. \(\square\)

For \(k=2\), the criterion says the remaining finitely-bad case would be
resolved by a recurrent triple \(e,y_1,y_2\in A\) with
\[
y_1+y_2-e\in A.
\]
Thus Lemma 8.6c would close the bounded-width large-excess branch if its
large recurrent clusters could always be chosen to contain this certificate
pattern. The current obstruction is precisely the possibility that all
available recurrent clusters are certificate-free.

## Corollary 2.3c: Fixed triple criterion for \(k=2\)

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
there are elements
\[
e,y_1,y_2,x\in A,\qquad y_1\ne e,\quad y_2\ne e,
\]
such that
\[
x=y_1+y_2-e
\]
and the triple
\[
R=\{e,y_1,y_2\}
\]
is reflection-recurrent in \(A\). Then there is an infinite \(B\subset A\)
such that \(A\setminus B\) is an asymptotic basis of order \(3\).

Proof. This is Lemma 2.3b for \(k=2\), with \(x_1=y_1\) and
\(x_2=x\). Equivalently, one can see it directly from Lemma 8.2a. Choose
recurrent centers
\[
m_j\to\infty,\qquad m_j-R\subset A,
\]
recursively avoiding the finitely many collisions with previously deleted
and protected elements, and put
\[
b_j=m_j-e.
\]
Keep protected
\[
e,y_1,y_2,x,\qquad m_j-y_1,\ m_j-y_2\quad(j\ge1),
\]
and set \(C=A\setminus\{b_j:j\ge1\}\). Then
\[
b_j+e=m_j=y_1+(m_j-y_1)\in2C,
\]
\[
2b_j+e=2m_j-e=x+(m_j-y_1)+(m_j-y_2)\in3C,
\]
and for \(i<j\),
\[
b_i+b_j+e=(m_j-y_1)+x+(m_i-y_2)\in3C.
\]
These are exactly the one-deleted and two-deleted repair identities in
Lemma 8.2a. Hence \(C\) is an order-3 basis. \(\square\)

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

In fact this criterion is exact, not merely sufficient. Let \(h\ge1\). For
an arbitrary \(A\subseteq\mathbb N\), the following are equivalent:

1. there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
   order-\(h\) asymptotic basis;
2. there is an infinite \(R\subset A\) such that for every finite
   \(F\subset R\) and every \(L\), some
   \[
   b\in R\setminus F,\qquad b>L,
   \]
   makes \(A\setminus(F\cup\{b\})\) an order-\(h\) basis with threshold
   \(<b\).

The implication (2) \(\Rightarrow\) (1) is Lemma 3. Conversely, if
\(A\setminus B\) is an order-\(h\) basis with threshold \(T\), take
\[
R=B\cap(T,\infty).
\]
For finite \(F\subset R\), choose
\[
b\in R\setminus F,\qquad b>\max\{L,T\}.
\]
Since
\[
A\setminus(F\cup\{b\})\supseteq A\setminus B,
\]
the same threshold \(T<b\) works. Thus any positive proof must, in one form
or another, rule out barriers of late-bad successors. Failure of the
criterion is exactly the statement that every infinite \(X\subset A\)
contains a finite \(F\subset X\) and a bound \(L\) such that no
\[
b\in X\setminus F,\qquad b>L,
\]
is late-good over \(F\).

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

The benign basis
\[
A=\{1\}\cup2\mathbb N
\]
shows why arbitrary prefix thresholds are the wrong diagnostic. Prefixes
\[
F_M=\{2,4,\ldots,2M\}
\]
force the least order-3 threshold of \(A\setminus F_M\) to grow past
\(\max F_M\), as in Example 3.0a below. Nevertheless a sparse reservoir has
uniform thresholds. For instance, let
\[
R=10\mathbb N.
\]
If \(F\subset R\) is finite and \(C=A\setminus F\), then
\[
[13,\infty)\subseteq3C.
\]
For even \(n\ge14\), use
\[
n=1+1+(n-2)
\]
unless \(n-2\in F\); in that case \(n-8\notin F\), because \(F\subset
10\mathbb N\), and
\[
n=4+4+(n-8).
\]
For odd \(n\ge13\), use
\[
n=1+2+(n-3)
\]
unless \(n-3\in F\); in that case \(n-5\notin F\), and
\[
n=1+4+(n-5).
\]
Thus every sufficiently large \(b\in R\) is late-good over every finite
previous deletion. The delayed-threshold obstruction, if real, must defeat
all such sparse reservoirs, not just consecutive prefixes.

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

### Lemma 3.1c.1: Weak barriers give prefix-front supersets

Let \(P\subset A\) be infinite, ordered increasingly, and let
\[
\mathcal B
\]
be a family of finite nonempty subsets of \(P\) such that every infinite
\[
X\subset P
\]
contains some member of \(\mathcal B\). Define \(\widehat{\mathcal B}\) to
be the family of all finite sets
\[
S=\{x_1<\cdots<x_n\}\subset P
\]
with the following two properties:

1. \(S\) contains some \(B\in\mathcal B\);
2. the proper initial segment
   \[
   \{x_1,\ldots,x_{n-1}\}
   \]
   contains no member of \(\mathcal B\).

Then every infinite
\[
X=\{x_1<x_2<\cdots\}\subset P
\]
has a unique initial segment in \(\widehat{\mathcal B}\). Thus
\(\widehat{\mathcal B}\) is a prefix-front: no member can be a proper
initial segment of another member, although two members need not be
incomparable by ordinary inclusion.

Moreover, if every member of \(\mathcal B\) is late-bad for order \(h\),
then every member of \(\widehat{\mathcal B}\) is late-bad for order \(h\).
If \(S\in\widehat{\mathcal B}\) contains \(B\in\mathcal B\) and
\[
w\notin h(A\setminus B),
\]
then also
\[
w\notin h(A\setminus S). \tag{1}
\]

Proof. Given infinite \(X=\{x_1<x_2<\cdots\}\), choose the least \(n\) such
that
\[
\{x_1,\ldots,x_n\}
\]
contains a member of \(\mathcal B\). This \(n\) exists by the barrier
hypothesis, and the corresponding prefix lies in
\(\widehat{\mathcal B}\). Minimality of \(n\) gives uniqueness.

Now let \(S=\{x_1<\cdots<x_n\}\in\widehat{\mathcal B}\). By definition,
choose \(B\in\mathcal B\) with \(B\subset S\). Since the proper initial
segment \(\{x_1,\ldots,x_{n-1}\}\) contains no member of \(\mathcal B\), we
must have \(x_n\in B\). Hence
\[
\max B=\max S. \tag{2}
\]
Since \(B\subset S\),
\[
A\setminus S\subset A\setminus B.
\]
Thus any order-\(h\) hole for \(A\setminus B\) remains a hole after deleting
\(S\), proving (1). In particular, if \(A\setminus B\) is not an
order-\(h\) basis, then \(A\setminus S\) is not an order-\(h\) basis either.
If \(A\setminus B\) is an order-\(h\) basis but every threshold for it is at
least \(\max B\), then any threshold for \(A\setminus S\) is also a
threshold for \(A\setminus B\). By (2) it is therefore at least
\(\max S\). Hence \(S\) is late-bad in the delayed-threshold case as well.
\(\square\)

This gives a prefix-front formulation of Corollary 3.1c, but it does not
solve the arithmetic problem. The front node \(S\) may be a strict superset
of the inclusion-minimal hole \(B\), and the private-color and active-repair
normal forms apply to the shrunk hole, not automatically to the whole
prefix. The section-descent problem is precisely to keep enough of that
normal form while passing from weak barriers to prefix-front supersets.

### Lemma 3.1c.2: First-prefix holes keep their last point active

Let \(A\) be an order-\(k\) basis, let \(h=k+1\), and suppose no infinite
deletion from \(A\) leaves an order-\(h\) basis. Let \(N_h\) be an
order-\(h\) threshold for \(A\), and let \(\mathcal P_h\) be the
prefix-front obtained from the late-bad family \(\mathcal L_h\) by Lemma
3.1c.1. Fix
\[
S=\{x_1<\cdots<x_n\}\in\mathcal P_h.
\]
Assume \(\max S>N_h\). Then there is a witness
\[
w\ge \max S-1
\]
with
\[
w\notin h(A\setminus S).
\]
Moreover, if \(F\subset S\) is inclusion-minimal for this fixed
nonrepresentation,
\[
w\notin h(A\setminus F),
\]
then
\[
\max S=x_n\in F. \tag{1}
\]

Consequently, every sufficiently late first-prefix front edge has an
inclusion-minimal terminal-gap subhole whose last front point is active:
there are \(q\in\{1,\ldots,h\}\) and elements
\[
c_1,\ldots,c_{h-q}\in A\setminus F
\]
such that
\[
w=qx_n+c_1+\cdots+c_{h-q}. \tag{2}
\]

Proof. Since \(S\in\mathcal P_h\), Lemma 3.1c.1 says that \(S\) is
late-bad. If \(A\setminus S\) is not an order-\(h\) basis, choose a hole
\[
w\ge\max S-1
\]
outside \(h(A\setminus S)\). If \(A\setminus S\) is an order-\(h\) basis
but late-bad, then no threshold below \(\max S\) works, so there is some
\[
w\ge\max S-1
\]
outside \(h(A\setminus S)\).

Because \(w\ge\max S-1\ge N_h\), the order-\(h\) basishood of \(A\) gives
\(w\in hA\). Thus the inclusion-minimal shrink below is nonempty. Now
shrink \(S\) inclusion-minimally while preserving this fixed
nonrepresentation, and call the result \(F\). Suppose, for contradiction,
that \(x_n\notin F\). Then \(F\subset\{x_1,\ldots,x_{n-1}\}\). Since
\[
w\ge x_n-1\ge\max F,
\]
the set \(F\) is late-bad: if \(A\setminus F\) is not an order-\(h\) basis
this is immediate, while if it is an order-\(h\) basis, every threshold for
it must exceed the missing value \(w\), and hence is at least \(\max F\).
This contradicts the defining property of \(S\in\mathcal P_h\), whose
proper initial segment contains no member of \(\mathcal L_h\). Therefore
\(x_n\in F\).

Finally, if \(A\) is an order-\(k\) basis, Lemma 10.3b applies to the
inclusion-minimal hole \(F,w\). Its active-repair conclusion for
\(f=x_n\) gives (2). \(\square\)

### Corollary 3.1c.3: Active traces form the real barrier

Keep the hypotheses and notation of Lemma 3.1c.2, and pass to the tail
\[
P=A\cap(N_h,\infty).
\]
For every \(S\in\mathcal P_h\) with \(S\subset P\), choose a witness
\[
w_S\ge\max S-1
\]
and an inclusion-minimal set
\[
F_S\subset S
\]
as in Lemma 3.1c.2. Let
\[
\mathcal H_h=\{F_S:S\in\mathcal P_h,\ S\subset P\}.
\]
Then \(\mathcal H_h\) is a weak barrier on \(P\): every infinite
\[
X\subset P
\]
contains some \(F\in\mathcal H_h\). Each \(F=F_S\) satisfies
\[
\max F=\max S,\qquad w_S\ge\max F-1,\qquad
w_S\notin h(A\setminus F),
\]
and \(F\) is late-bad. In the order-\(k\) setting, every element of \(F\)
is active in the terminal-gap normal form of Lemma 10.3b.

Proof. Given infinite \(X\subset P\), the prefix-front property gives an
initial segment \(S\subset X\) with \(S\in\mathcal P_h\). By construction,
\[
F_S\subset S\subset X,
\]
so \(\mathcal H_h\) is a weak barrier. Lemma 3.1c.2 gives
\(\max S\in F_S\), and since \(F_S\subset S\), this gives
\(\max F_S=\max S\). The witness and nonrepresentation properties are part
of the construction. Because \(w_S\ge\max F_S-1\), the same argument as in
Lemma 3.1c.2 shows that \(F_S\) is late-bad. Finally, Lemma 10.3b applied
to the inclusion-minimal hole \(F_S,w_S\) gives the terminal gap and active
repair for every \(f\in F_S\). \(\square\)

Thus rank coming only from inactive prefix fillers is illusory. In any
counterexample, either the active traces \(\mathcal H_h\) have bounded size
on some tail, returning the problem to bounded-width barrier reductions, or
the genuinely active holes themselves have unbounded size. The remaining
variable-rank obstruction must therefore use unbounded active traces or
unbounded-depth private colors, not merely large prefix-front nodes padded
by harmless filler points.

## Lemma 3.1d: Uniform finite-hole characterization of a good deletion

Let \(h\ge1\), let \(A\subseteq\mathbb N\), and let \(X\subseteq A\) be
infinite. Then \(A\setminus X\) is an asymptotic basis of order \(h\) if
and only if there is a threshold \(T\) such that for every finite
\[
F\subset X
\]
one has
\[
[T,\infty)\subseteq h(A\setminus F). \tag{1}
\]

Proof. If \(A\setminus X\) is an order-\(h\) basis with threshold \(T\),
then for every finite \(F\subset X\),
\[
A\setminus F\supseteq A\setminus X,
\]
so (1) follows from monotonicity in the set.

Conversely, suppose (1) holds. Fix \(n\ge T\), and put
\[
F_n=X\cap[1,n].
\]
This set is finite. By (1), there is an \(h\)-term representation of \(n\)
from \(A\setminus F_n\). Since all summands are positive, every summand in
such a representation is at most \(n\). Thus avoiding \(F_n\) is the same
as avoiding all of \(X\), and the representation lies in
\[
h(A\setminus X).
\]
Therefore \([T,\infty)\subseteq h(A\setminus X)\). \(\square\)

Thus Corollary 3.1b is a sparse-prefix way to manufacture the uniform
threshold in Lemma 3.1d. A counterexample must do more than create late
finite holes along one enumeration: for every infinite \(X\subset A\), the
finite deletions inside \(X\) must have no common eventual threshold.

## Lemma 3.1e: Pure delayed barriers under finite-core stability

Let \(h=k+1\), and suppose no infinite deletion from \(A\) leaves an
order-\(h\) basis. Assume also that there is a finite core \(E_0\subset A\)
such that for every finite
\[
F\subset A\setminus E_0
\]
the set \(A\setminus F\) is an order-\(h\) basis.

Then for every finite \(E\subset A\), every infinite
\[
X\subset A\setminus(E\cup E_0),
\]
and every \(L\), there are a finite nonempty set \(F\subset X\) and an
integer \(w>L\) such that:

1. \(A\setminus F\) is an order-\(h\) basis;
2. every order-\(h\) threshold for \(A\setminus F\) is at least \(\max F\);
3. \(w\notin h(A\setminus F)\).

If, in addition, \(A\) is an order-\(k\) basis with threshold \(N_0\) and
\(m_0=\min A\), then \(F\) may be chosen inclusion-minimal for this fixed
witness \(w\), and with \(f_0=\min F\) one has the terminal gap
\[
(A\setminus F)\cap
\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{1}
\]
For such a minimal choice, every \(f\in F\) is active: there is a
multiplicity \(q_f\in\{1,\ldots,h\}\) and elements
\[
c_{f,1},\ldots,c_{f,h-q_f}\in A\setminus F
\]
such that
\[
w=q_f f+c_{f,1}+\cdots+c_{f,h-q_f}. \tag{2}
\]
When \(q_f=h\), no \(c\)-terms appear.
In particular,
\[
q_f f+(h-q_f)m_0\le w. \tag{3}
\]

Proof. Since \(A\) is an order-\(h\) basis by monotonicity, increase \(L\)
if necessary so that \(L\) is above an order-\(h\) threshold for \(A\).
Replace \(X\) by its infinite tail
\[
X'=\{x\in X:x>L+1\}.
\]
By Corollary 3.1c, \(X'\) contains a finite late-bad set \(F_0\). Since
\[
F_0\subset A\setminus E_0,
\]
the finite-core stability hypothesis says that \(A\setminus F_0\) is an
order-\(h\) basis. Therefore \(F_0\) is late-bad only because every
threshold is at least
\[
M=\max F_0.
\]
Equivalently, no threshold \(<M\) works, so there is some
\[
w\ge M-1>L
\]
with
\[
w\notin h(A\setminus F_0).
\]

Shrink \(F_0\) inclusion-minimally while preserving this fixed
nonrepresentation, and call the resulting set \(F\). Then \(F\subset X\),
and finite-core stability gives that \(A\setminus F\) is an order-\(h\)
basis. Since \(w\notin h(A\setminus F)\), every threshold for
\(A\setminus F\) is \(>w\). If \(\max F<M\), then \(w\ge M-1\ge\max F\);
if \(\max F=M\), then \(w\ge M-1\), so every threshold is at least
\(M=\max F\). This proves the delayed-threshold assertions.

When \(A\) is an order-\(k\) basis and \(h=k+1\), the terminal gap (1) is
Lemma 10.3 applied to \(F\) and \(w\). Minimality gives
\[
w\in h(A\setminus(F\setminus\{f\}))
\]
for every \(f\in F\), while \(w\notin h(A\setminus F)\). Hence each such
representation uses at least one copy of \(f\). Let \(q_f\) be the number
of copies of \(f\) in one such representation. All remaining summands avoid
\(F\), because the representation lies in \(A\setminus(F\setminus\{f\})\).
This gives (2), and (3) follows because every remaining summand is at least
\(m_0\). \(\square\)

Thus if finite-core finite-deletion stability is true, any counterexample
must be a pure delayed-threshold counterexample: finite deletions outside
the protected core are eventually repaired at order \(k+1\), but every
infinite tail contains finite subdeletions whose repair threshold is forced
to start at or beyond the deleted block itself.

## Corollary 3.1e': Collective delayed-barrier normal form

Keep the hypotheses of Lemma 3.1e. Then for every finite
\[
E\supseteq E_0,
\]
every infinite
\[
X\subset A\setminus E,
\]
and every \(L\), there are a finite nonempty set
\[
F\subset X
\]
and an integer \(w>L\) such that:

1. \(A\setminus F\) is an order-\(h\) basis;
2. \(F\) is late-bad, but every proper subset \(G\subsetneq F\) is not
   late-bad;
3. \(w\ge\max F-1\) and \(w\notin h(A\setminus F)\);
4. \(F\) is inclusion-minimal for this fixed witness \(w\).

Consequently, if \(A\) is an order-\(k\) basis and \(h=k+1\), then the
terminal gap and active-repair conclusions of Lemma 3.1e hold for this
\(F,w\).

For \(k=2\), in any remaining counterexample the core \(E_0\) may be
enlarged so that every such \(F\) has size at least \(2\).

Proof. As in Lemma 3.1e, increase \(L\) if necessary so it lies above an
order-\(h\) threshold for \(A\), and replace \(X\) by its tail above
\(L+1\). By Corollary 3.1c, this tail contains a late-bad finite set. Choose
one that is inclusion-minimal for the late-bad property, and call it
\(F_0\). Finite-core stability gives that \(A\setminus F_0\) is an
order-\(h\) basis, so \(F_0\) is late-bad only because no threshold below
\[
M=\max F_0
\]
works. Hence there is
\[
w\ge M-1>L
\]
with
\[
w\notin h(A\setminus F_0).
\]

Shrink \(F_0\) inclusion-minimally for this fixed witness \(w\), and call
the result \(F\). It is nonempty because \(w\) is above an order-\(h\)
threshold for \(A\), so \(w\in hA\). Also \(A\setminus F\) is an order-\(h\)
basis by finite-core stability, while \(w\notin h(A\setminus F)\). Thus
every threshold for \(A\setminus F\) is \(>w\), and since
\[
w\ge M-1\ge\max F-1,
\]
the set \(F\) is late-bad. Every proper subset of \(F\) is a proper subset
of the late-bad-minimal set \(F_0\), and hence is not late-bad. The
inclusion-minimality for \(w\) was built into the final shrinking.

The terminal gap and active repairs are exactly the second part of Lemma
3.1e. Finally, when \(k=2\), Corollary 8.3 rules out infinitely many
singleton deletions that are genuine order-3 failures, while Lemma 10.2b
rules out infinitely many singleton deletions that are order-3 bases but
late-bad. Thus only finitely many singleton late-bad sets can occur in a
counterexample; enlarge \(E_0\) to contain those singleton elements.
\(\square\)

The finite diagnostic `EXPERIMENTS/delayed_collective_barrier_search.py`
shows that this normal form is locally nonempty. For instance,
\[
S=\{1,2,3,5,6,7\}
\]
has \(2S\) covering \([2,14]\). Deleting
\[
F=\{5,7\}
\]
leaves a finite three-sum tail only from \(18\) onward, with minimal holes
\[
16,\ 17,
\]
while each singleton subdeletion has finite three-sum tail from \(3\). At
rank \(3\),
\[
S=\{1,2,3,4,5,6,7,8\},\qquad F=\{4,5,6\}
\]
has a minimal hole at \(20\), a finite three-sum tail from \(21\), and all
proper subdeletions have finite three-sum tail from \(3\). These are finite
window artefacts, but they confirm that collective delay is not ruled out
by inclusion-minimality or proper-subdeletion stability alone.
The certificate diagnostic gives the complementary warning: these small
delayed examples are not certificate-free enough to scale as fixed-rank
large-excess obstructions. For the pair example above,
`certificate_free_stats.py` gives
\[
\alpha_{\rm cert}=2,\qquad |S|/\alpha_{\rm cert}=3>2,
\]
so Lemma 8.6g would force a recurrent certificate if such rank-\(2\)
barriers persisted over every finite test set. The unresolved construction
would need either more certificate-free arithmetic or unbounded ranks.

## Proposition 3.1f: Syndetic tail criterion

Let \(k\ge2\), let \(h=k+1\), and let \(A\subseteq\mathbb N\) be an
asymptotic basis of order \(k\), with threshold \(N_0\) and
\[
m_0=\min A.
\]
Suppose \(A\) contains a tail-syndetic subset \(P\): there are \(R\) and
\(G\) such that every interval
\[
(x,x+G],\qquad x\ge R,
\]
contains a point of \(P\). Then:

1. there is a finite core \(E\subset A\) such that every finite
   \(F\subset A\setminus E\) leaves \(A\setminus F\) an order-\(h\) basis;
2. there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
   order-\(h\) basis.

Proof. Choose \(M\) so large that
\[
M+(k-1)m_0-N_0>G.
\]
Put
\[
E=A\cap[1,M].
\]
Let \(F\subset A\setminus E\) be finite. If \(F=\varnothing\), then
\(A\setminus F=A\) is an order-\(h\) basis by monotonicity. Suppose
\(F\ne\varnothing\), and put \(f_0=\min F\). If \(A\setminus F\) were not
an order-\(h\) basis, then there would be arbitrarily large
\[
w\notin h(A\setminus F).
\]
Choose such a \(w\) with
\[
w-f_0-(k-1)m_0>\max\{R,\max F\}.
\]
Lemma 10.3 gives
\[
(A\setminus F)\cap
\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{1}
\]
The interval in (1) has length
\[
f_0+(k-1)m_0-N_0>M+(k-1)m_0-N_0>G
\]
and starts beyond \(R\), so it contains a point of \(P\). It also starts
beyond \(\max F\), so that point is not in \(F\). This contradicts (1).
Thus \(A\setminus F\) is an order-\(h\) basis, proving (1).

For the infinite deletion, pass to a tail of \(P\) whose consecutive gaps
are at most \(G\), enumerate it as
\[
p_1<p_2<\cdots,
\]
and choose an index \(J\) so large that
\[
p_{2J}>2G+N_0-(k-1)m_0.
\]
Let
\[
B=\{p_{2j}:j\ge J\}.
\]
Then \(B\) is infinite, and
\[
P_0=P\setminus B
\]
is still tail-syndetic, with gap at most \(2G\) after a sufficiently large
threshold.

Suppose \(C=A\setminus B\) is not an order-\(h\) basis. Choose a large
\[
w\notin hC
\]
so that the terminal interval below starts beyond a tail-syndetic threshold
for \(P_0\). Put
\[
F_w=B\cap[1,w].
\]
For large \(w\), this set is nonempty and \(\min F_w=p_{2J}\). Since no
positive summand in a representation of \(w\) can exceed \(w\), the
nonrepresentation \(w\notin hC\) implies
\[
w\notin h(A\setminus F_w).
\]
Lemma 10.3 gives
\[
(A\setminus F_w)\cap
\bigl(w-p_{2J}-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{2}
\]
The interval in (2) has length
\[
p_{2J}+(k-1)m_0-N_0>2G
\]
and lies in the tail where \(P_0\) has gaps at most \(2G\). Hence it
contains a point of \(P_0\). This point is not deleted by \(F_w\), a
contradiction. Therefore \(A\setminus B\) is an order-\(h\) basis.
\(\square\)

Consequently, any counterexample to the broad deletion theorem has no
tail-syndetic subset. Equivalently, every infinite subset of \(A\) has
arbitrarily long gaps in the tail. Thus the remaining problem is genuinely
sparse; bounded-gap background structure cannot be responsible for a
negative answer.

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

## Lemma 3.3a: Random thinning is an anti-transversal criterion

Fix a finite core \(E\subset A\), put \(h=k+1\), and let
\[
\mathcal T_E(n)
\]
be the family of inclusion-minimal transversals of \(\mathcal H_E(n)\).
Suppose there are numbers
\[
0\le q_a\le1\qquad(a\in A\setminus E)
\]
such that
\[
\sum_{a\in A\setminus E}q_a=\infty \tag{1}
\]
and
\[
\sum_n\sum_{T\in\mathcal T_E(n)}\prod_{a\in T}q_a<\infty. \tag{2}
\]
Then there is an infinite \(B\subset A\setminus E\) such that
\[
A\setminus B
\]
is an asymptotic basis of order \(h\).

Proof. Delete each \(a\in A\setminus E\) independently with probability
\(q_a\). By (1), the deleted set \(B\) is infinite almost surely.

For a fixed sufficiently large \(n\), the complement \(A\setminus B\) fails
to represent \(n\) at order \(h\) if and only if \(B\) contains some
transversal of \(\mathcal H_E(n)\), and hence contains an inclusion-minimal
transversal. The probability of this event is at most
\[
\sum_{T\in\mathcal T_E(n)}\prod_{a\in T}q_a.
\]
By (2) and Borel-Cantelli, almost surely only finitely many \(n\) fail.
For one outcome with \(B\) infinite and only finitely many failures,
\(A\setminus B\) is an asymptotic basis of order \(h\). \(\square\)

Thus a purely probabilistic proof would still need an additive theorem
saying that the minimal transversals can be made summable while deleting
infinitely many elements. Complete pair barriers or Schreier-type
transversal barriers defeat this condition abstractly: every infinite
deletion contains a bad pair or an initial Schreier edge, so no choice of
probabilities with divergent sum can avoid all bad transversals. The
remaining task is therefore arithmetic, not probabilistic: prove such
collective transversal barriers cannot arise from actual representation
hypergraphs, or construct one.

## Corollary 3.3b: Bounded terminal-gap holes outside any finite core

Assume that no infinite \(B\subset A\) has \(A\setminus B\) an
order-\((k+1)\) basis. Let \(E\subset A\) be finite. Then there is an
integer \(q_E\) such that for arbitrarily large \(n\) there is a finite set
\[
D_n\subset A\setminus E,\qquad 1\le |D_n|\le q_E,
\]
with
\[
n\notin(k+1)(A\setminus D_n). \tag{1}
\]
If \(A\) has order-\(k\) threshold \(N_0\), \(m_0=\min A\), and
\[
d_n=\min D_n,
\]
then these \(n\) may be chosen so large that
\[
(A\setminus D_n)\cap
\bigl(n-d_n-(k-1)m_0,\ n-N_0\bigr]=\varnothing. \tag{2}
\]

Proof. Apply Corollary 3.3 to the finite core \(E\), obtaining arbitrarily
large \(n\) and a bounded transversal
\[
D_n\subset A\setminus E
\]
for the hypergraph \(\mathcal H_E(n)\). Taking \(n\) larger than every
\((k+1)\)-term sum from \(E\), no representation of \(n\) can lie entirely
inside \(E\). Hence every \((k+1)\)-term representation of \(n\) from \(A\)
has a nonempty outside-\(E\) edge and therefore meets \(D_n\). This proves
(1), and \(D_n\) is nonempty because \(n\in(k+1)A\) for all sufficiently
large \(n\).

Now apply Lemma 10.3 to the finite deletion \(D_n\) and the witness
\(w=n\). This gives the terminal gap (2). \(\square\)

Thus a counterexample has bounded-size terminal-gap holes after every fixed
finite core is protected. The bound \(q_E\) may grow with \(E\); this is
exactly how Schreier-type barriers evade a uniform bounded-width reduction.

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

## Corollary 3.4b: Bounded representation functions give a good deletion

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\), with
order-\(k\) threshold \(N_0\). Suppose there is a constant \(R\) such that
every integer has at most \(R\) unordered \(k\)-term representations from
\(A\), counted as multisets. Then there is an infinite
\[
B\subset A
\]
such that \(A\setminus B\) is an asymptotic basis of order \(k+1\).

Proof. We verify Proposition 3.4 with \(E=\varnothing\). Let \(n\) be
large. For each
\[
e\in A\cap[1,n-N_0],
\]
choose one \(k\)-term representation of \(n-e\) from \(A\), and append
\(e\). This gives at least
\[
|A\cap[1,n-N_0]|
\]
distinguished \((k+1)\)-term representations of \(n\). When the
distinguished summand is forgotten, any one \((k+1)\)-term multiset can
arise from at most \(k+1\) choices of the distinguished occurrence. Hence
there are at least
\[
\frac{|A\cap[1,n-N_0]|}{k+1} \tag{1}
\]
distinct \((k+1)\)-term multisets representing \(n\).

Passing from multisets to support sets loses only a constant depending on
\(k\): a support of size at most \(k+1\) carries at most
\[
C_k=\binom{2k+1}{k+1}
\]
multiplicity patterns of total size \(k+1\). Thus the representation
hypergraph \(\mathcal H_\varnothing(n)\) has at least
\[
\frac{|A\cap[1,n-N_0]|}{(k+1)C_k} \tag{2}
\]
edges.

On the other hand, fix a vertex \(x\in A\). Every multiset representation
of \(n\) using \(x\), after removing one occurrence of \(x\), gives a
\(k\)-term multiset representation of \(n-x\). By hypothesis there are at
most \(R\) such multisets. Therefore the degree of \(x\) in
\(\mathcal H_\varnothing(n)\) is at most \(R\), so
\[
\Delta_\varnothing(n)\le R. \tag{3}
\]

Since \(A\) is infinite, \(|A\cap[1,n-N_0]|\to\infty\). Equations (2) and
(3) imply
\[
\frac{|\mathcal H_\varnothing(n)|}{\Delta_\varnothing(n)}\to\infty.
\]
Proposition 3.4 gives an infinite deletion preserving order \(k+1\).
\(\square\)

For \(k=2\), this covers Sidon-type and unique-representation order-2
bases. In particular, any counterexample in the remaining sparse regime
must have unbounded two-term representation function; it cannot be a
purely near-unique Raikov-Stöhr-style basis with only bounded
representation multiplicity.

## Lemma 3.4b': Bounded multiplicity gives a shifted sparse deletion

Let \(S\subseteq\mathbb N\) be an asymptotic basis of order \(k\), with
threshold \(N_0\). Suppose there is a constant \(R\) such that every integer
has at most \(R\) unordered \(k\)-term representations from \(S\), counted
as multisets. Then there is an infinite
\[
T\subset S
\]
such that
\[
k(S\setminus T)+S
\]
is cofinite.

Proof. For each large \(n\), form a hypergraph \(G_n\) on the vertex set
\[
S\cap[1,n].
\]
For every
\[
s\in S\cap[1,n-N_0],
\]
choose one \(k\)-term multiset representation
\[
n-s=a_{s,1}+\cdots+a_{s,k},\qquad a_{s,i}\in S,
\]
and add its support
\[
E_s=\{a_{s,1},\ldots,a_{s,k}\}
\]
as an edge of \(G_n\), ignoring repetitions. One support of size at most
\(k\) carries at most
\[
C_k=\binom{2k-1}{k}
\]
different \(k\)-term multiplicity patterns. Since different values of
\(s\) give different sums \(n-s\), the number of distinct support edges is
at least
\[
|S\cap[1,n-N_0]|/C_k\to\infty. \tag{1}
\]

The maximum degree of \(G_n\) is bounded in terms of \(k\) and \(R\). Fix a
vertex \(x\in S\). If an edge \(E_s\) contains \(x\), then the chosen
multiset representation of \(n-s\), after deleting one occurrence of \(x\),
together with the summand \(s\), gives a \(k\)-term representation of
\[
n-x.
\]
There are at most \(R\) such unordered \(k\)-term multisets, and each has
at most \(k\) choices for which occurrence is the distinguished summand
\(s\). Hence
\[
\Delta(G_n)\le kR. \tag{2}
\]

A greedy matching in a hypergraph of edge size at most \(k\) has size at
least
\[
\frac{|E(G_n)|}{k\Delta(G_n)}.
\]
By (1) and (2), the matching numbers of \(G_n\) tend to infinity uniformly:
for every \(q\), all sufficiently large \(n\) have a matching of size at
least \(q\).

Choose
\[
t_1<t_2<\cdots,\qquad t_i\in S,
\]
so fast that \(t_j\) is larger than a threshold after which every \(G_n\)
has a matching of size at least \(j+2\). Put
\[
T=\{t_j:j\ge1\}.
\]
For large \(n\), choose \(j\) with
\[
t_j\le n<t_{j+1}.
\]
The graph \(G_n\) has \(j+2\) pairwise disjoint support edges. Future
deleted elements are larger than \(n\), and hence cannot appear in a
positive-summand representation of \(n\). The first \(j\) deleted elements
meet at most \(j\) of the disjoint supports. Thus one edge \(E_s\) avoids
\(T\), and
\[
n=a_{s,1}+\cdots+a_{s,k}+s
\]
with all \(a_{s,i}\in S\setminus T\) and \(s\in S\). Hence all sufficiently
large \(n\) lie in \(k(S\setminus T)+S\). \(\square\)

This lemma is weaker than Corollary 3.4b when applied to \(A\) itself,
because the final summand \(s\) is not required to avoid \(T\). Its value is
in quotient and color-copy arguments, where one summand may come from a
different retained class.

## Corollary 3.4c: Sublinear representation multiplicity is enough

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\), and let
\[
A(x)=|A\cap[1,x]|.
\]
For \(X\ge1\), define
\[
R_k(X)=\max_{m\le X} r_{k,A}(m),
\]
where \(r_{k,A}(m)\) is the number of unordered \(k\)-term multiset
representations of \(m\) from \(A\). If
\[
R_k(X)=o(A(X)),
\]
then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(k+1\).

Proof. Repeat the proof of Corollary 3.4b. For each large \(n\), the
hypergraph \(\mathcal H_\varnothing(n)\) has
\[
|\mathcal H_\varnothing(n)|\gg_k A(n-N_0),
\]
because each \(e\in A\cap[1,n-N_0]\) pads a \(k\)-term representation of
\(n-e\). A vertex \(x\) has degree at most
\[
r_{k,A}(n-x)\le R_k(n).
\]
Thus
\[
\frac{|\mathcal H_\varnothing(n)|}{\Delta_\varnothing(n)}
\gg_k \frac{A(n-N_0)}{R_k(n)}\to\infty.
\]
Here \(A(n-N_0)=A(n)+O_{N_0}(1)\), since at most \(N_0\) integers lie in
\((n-N_0,n]\).
Proposition 3.4 applies. \(\square\)

Consequently, a counterexample must have large representation spikes:
\[
R_k(X)\not=o(A(X)).
\]
For \(k=2\), a sparse critical-density counterexample would therefore need
two-sum multiplicities comparable to the counting function along an
unbounded sequence, while still supporting the private-color barriers from
Proposition 8.4f.

## Corollary 3.4d: Counterexamples force shifted representation spikes

Assume that no infinite deletion from the order-\(k\) basis \(A\), with
order-\(k\) threshold \(N_0\), remains an order-\((k+1)\) basis. Let
\(E\subset A\) be finite. Then there are a constant \(\eta_E>0\),
arbitrarily large integers \(n\), and elements
\[
x_n\in A\setminus E
\]
such that
\[
r_{k,A}(n-x_n)\ge \eta_E\, A(n), \tag{1}
\]
where \(r_{k,A}\) counts unordered \(k\)-term multiset representations.

Proof. By Corollary 3.3, for this fixed \(E\) there is an integer \(M_E\)
and arbitrarily large \(n\) for which the matching number of
\(\mathcal H_E(n)\) is less than \(M_E\). Let
\[
C_{k,E}=\binom{|E|+2k+1}{k+1}.
\]
As in Corollary 3.4b, padding one chosen \(k\)-term representation of
\(n-e\) by each
\[
e\in A\cap[1,n-N_0]\setminus E
\]
gives, after forgetting distinguished summands and multiplicities, at
least
\[
\frac{|A\cap[1,n-N_0]|-|E|}{(k+1)C_{k,E}}
\]
edges in \(\mathcal H_E(n)\). Indeed, once an outside-\(E\) support edge is
fixed, there are at most \(C_{k,E}\) possible \((k+1)\)-term multisets using
that edge together with elements of the fixed finite core \(E\), and at most
\(k+1\) choices for the distinguished padded occurrence. For all
sufficiently large \(n\), this edge count is at least
\[
c_{k,E} A(n)
\]
for a constant \(c_{k,E}>0\), because \(E\) and \(N_0\) are fixed.

The greedy matching lower bound used in Proposition 3.4 gives
\[
\operatorname{match}(\mathcal H_E(n))
\ge \frac{|\mathcal H_E(n)|}{(k+1)\Delta_E(n)}.
\]
Since the matching number is less than \(M_E\), we have
\[
\Delta_E(n)\ge \frac{c_{k,E}}{(k+1)M_E}A(n). \tag{2}
\]
Choose a vertex \(x_n\in A\setminus E\) with this degree. Every edge
containing \(x_n\) comes from some \((k+1)\)-term multiset representation
of \(n\) using \(x_n\). Removing one occurrence of \(x_n\) gives a
\(k\)-term multiset representation of \(n-x_n\), and different support
edges give different resulting multisets. Hence
\[
r_{k,A}(n-x_n)\ge \deg_{\mathcal H_E(n)}(x_n).
\]
Combining this with (2) proves (1). \(\square\)

Thus the representation-spike obstruction is not merely global. After any
finite core is protected, a counterexample has arbitrarily large
\((k+1)\)-targets \(n\) with some unprotected summand \(x_n\) such that the
shifted target \(n-x_n\) has order-\(k\) representation multiplicity
comparable to \(A(n)\). For \(k=2\), this means arbitrarily large reflected
clusters
\[
A\cap(n-x_n-A)
\]
of size comparable to the whole counting function at the larger scale.

## Warning 3.4e: Large spikes do not force fixed recurrence

The shifted-spike condition in Corollary 3.4d is necessary for a
counterexample, but it is far from sufficient to force the recurrent
certificate machinery.

Let
\[
A=\{1\}\cup2\mathbb N.
\]
Then \(A\) is an asymptotic basis of order \(2\). For even \(n=2M\), the
two-term representations
\[
2M=2i+2(M-i),\qquad 1\le i\le M-1,
\]
give
\[
r_{2,A}(2M)\asymp M\asymp A(2M).
\]
Equivalently, the reflected cluster
\[
A\cap(2M-A)
\]
contains a positive proportion of \(A\cap[1,2M]\).

Nevertheless \(A\) is not finitely reflection-recurrent. The two-point set
\[
T=\{1,2\}\subset A
\]
has no arbitrarily large reflecting centers: if \(m-1,m-2\in A\), then for
\(m>3\) one of \(m-1,m-2\) is an odd integer larger than \(1\), hence is
not in \(A\). Thus large moving reflected clusters do not by themselves
produce even the two-point recurrence needed by Theorem 2.3.

This example is eventually periodic and satisfies the desired conclusion by
Proposition 7.1. Its role is only diagnostic: a proof cannot replace the
remaining finite-barrier problem by the existence of large representation
spikes. The spikes must interact with the bounded-transversal and
private-color structure.

## Lemma 3.4f: Stable overlap of spikes with one test set gives a good deletion

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). For
\(n\in\mathbb N\), put
\[
U_n=A\cap(n-A).
\]
Suppose there is a finite set \(T_0\subset A\) such that, for arbitrarily
large \(n\),
\[
|U_n\cap T_0|>\alpha_A(T_0),
\]
where \(\alpha_A(T_0)\) is the largest size of a certificate-free subset
of \(T_0\), i.e. a subset containing no triple
\[
e,y_1,y_2,\qquad y_1\ne e,\quad y_2\ne e,\quad y_1+y_2-e\in A.
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. For each such \(n\), the set \(U_n\cap T_0\) contains a certificate
triple
\[
e,y_1,y_2\in U_n\cap T_0,\qquad y_1+y_2-e\in A.
\]
The finite set \(T_0\) contains only finitely many triples, so along an
unbounded sequence of \(n\)'s the same triple \(e,y_1,y_2\) occurs. Since
the triple lies in \(U_n\), we have
\[
n-e,\ n-y_1,\ n-y_2\in A.
\]
Thus \(\{e,y_1,y_2\}\) is reflection-recurrent in \(A\). Corollary 2.3c
gives the desired infinite deletion. \(\square\)

Every large reflected cluster contains many one-shot certificates, but
Lemma 3.4f shows exactly what extra stability is needed. If
\[
U_n
\]
contains two distinct complementary pairs \(\{a,n-a\}\) and
\(\{b,n-b\}\), then
\[
e=b,\qquad y_1=a,\qquad y_2=n-a
\]
satisfy
\[
y_1+y_2-e=n-b\in A.
\]
The problem is that these certificates may all move. A sparse escaping-block
model illustrates the limitation: choose rapidly increasing centers \(n_j\)
and finite blocks
\[
P_j\subset(n_j/4,n_j/3),\qquad Q_j=n_j-P_j,
\]
with \(|P_j|\) dominating all earlier block sizes, and let
\[
A_*=\bigcup_j(P_j\cup Q_j).
\]
Then \(P_j\cup Q_j\subset U_{n_j}\) and the spike at \(n_j\) can dominate
\(A_*(n_j)\), but every fixed finite \(T\subset A_*\) is eventually
disjoint from \(U_{n_j}\). This is not an asymptotic basis construction;
it is a model showing that representation spikes alone do not imply a
fixed recurrent certificate. A proof must prevent this mass escape using
the basis, barrier, or private-color structure.

## Corollary 3.4g: \(k=2\) counterexamples force star-gated holes

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
no infinite deletion from \(A\) remains an order-3 basis. Then for every
finite \(E\subset A\) there are constants \(q_E\) and \(\eta_E>0\) such
that, for arbitrarily large \(w\), there are a finite set
\[
D\subset A\setminus E,\qquad 1\le |D|\le q_E,
\]
and an element \(d\in D\) with:

1. \(w\notin3(A\setminus D)\);
2. there are at least
   \[
   \eta_E A(w)
   \]
   unordered two-term representations
   \[
   w-d=a+b,\qquad a,b\in A\setminus D. \tag{1}
   \]

Proof. Fix \(E\). Corollary 3.3 gives arbitrarily large \(w\) for which
\(\mathcal H_E(w)\) has matching number bounded by some \(M_E\). Let
\(D\) be the union of a maximal matching, so \(D\subset A\setminus E\),
\[
|D|<3M_E=:q_E,
\]
and \(D\) meets every edge of \(\mathcal H_E(w)\). Taking \(w\) larger than
every three-term sum from \(E\), this implies
\[
w\notin3(A\setminus D).
\]

As in Corollary 3.4d, the number of edges of \(\mathcal H_E(w)\) is at
least \(c_E A(w)\) for a constant \(c_E>0\). Since every edge meets \(D\),
some \(d\in D\) lies in at least
\[
\frac{c_E}{q_E}A(w)
\]
edges. Of these edges, at most \(2(|D|-1)\) contain another element of
\[
D\setminus\{d\};
\]
indeed, for a fixed \(d'\in D\setminus\{d\}\), a three-term representation
of \(w\) whose outside-\(E\) support contains both \(d\) and \(d'\) has at
most one further summand, hence determines at most two outside-\(E\)
support edges: \(\{d,d'\}\), if the third summand lies in \(E\) or is a
repeat, and possibly \(\{d,d',w-d-d'\}\).

Also discard the \(O(1)\) edges whose only representatives use \(d\) with
multiplicity at least two. Such a representation has the form \(w=3d\) or
\[
w=2d+a,
\]
so it contributes only the support \(\{d\}\) or the support
\(\{d,a\}\) with \(a=w-2d\).

After discarding these \(O_E(1)\) edges, each remaining edge containing
\(d\) has a representative three-term sum
\[
w=d+a+b
\]
with \(a,b\in A\setminus D\). Distinct outside-\(E\) support edges give
distinct unordered pairs \(\{a,b\}\). Therefore, for all sufficiently large
\(w\), the number of retained two-term representations (1) is at least
\(\eta_E A(w)\) for a suitable constant \(\eta_E>0\). \(\square\)

Thus any \(k=2\) counterexample must contain arbitrarily late finite holes
where one deleted element \(d\) acts as a gate for linearly many retained
two-sum repairs of the same witness. If such a gate \(d\) could be fixed
along an infinite sequence with enough control on the rest of \(D\), the
fixed-star recurrence mechanisms from Lemma 8.2c and Lemma 8.2d would
become relevant. The remaining escape is again motion: the star center
\(d\) and the finite auxiliary deletion set may move beyond every protected
core.

## Corollary 3.4h: Star gates create bounded-count translate rows

Let \(A\subseteq\mathbb N\) be an order-2 basis with threshold \(N_0\).
Let \(D\subset A\) be finite, put
\[
C=A\setminus D,
\]
and suppose
\[
w\notin3C.
\]
Fix \(d\in D\), and define the retained repair row set
\[
R_d(w)=\{a\in C:w-d-a\in C\}.
\]
Then every
\[
a\in R_d(w)
\]
satisfies
\[
a+d\notin2C. \tag{1}
\]
Consequently, if \(r_{2,A}(s)\) denotes the number of unordered two-term
representations of \(s\) from \(A\), then
\[
r_{2,A}(a+d)\le |D| \tag{2}
\]
and
\[
\nu_d(a+d)<|D|. \tag{3}
\]
Consequently, if \(d\) supplies \(M\) unordered retained repairs
\[
w-d=a+b,\qquad a,b\in C,
\]
then every summand appearing in those repairs is a bounded-count translate
row for the same gate \(d\); in particular there are at least \(M\) distinct
values \(a\in A\) with
\[
w-d-a\in A,\qquad r_{2,A}(a+d)\le |D|.
\]

Proof. Let \(a\in R_d(w)\), and write
\[
b=w-d-a\in C.
\]
If \(a+d\in2C\), say
\[
c_1+c_2=a+d,\qquad c_1,c_2\in C,
\]
then
\[
w=b+c_1+c_2\in3C,
\]
contrary to the hole. This proves (1).

Thus every unordered two-term representation of \(a+d\) from \(A\) uses at
least one element of \(D\). For each \(f\in D\), there is at most one such
unordered representation containing \(f\), namely
\[
\{f,\ a+d-f\}.
\]
The union bound gives (2). The representations counted by \(\nu_d(a+d)\)
avoid \(d\), so they must use an element of \(D\setminus\{d\}\); hence there
are at most \(|D|-1\) of them, proving (3).

Finally, distinct unordered pairs \(\{a,b\}\) with fixed sum \(w-d\) have
disjoint supports unless they are the same pair. Therefore \(M\) unordered
repairs contribute at least \(M\) distinct summands \(a\), and each of those
summands satisfies the displayed low-count condition. \(\square\)

Combining Corollaries 3.4g and 3.4h, a \(k=2\) counterexample must produce,
outside every finite protected core, arbitrarily late holes with a moving
deleted gate \(d\) and a set of \(\gg A(w)\) reflected retained rows whose
translates \(a+d\) all have bounded total two-sum representation count. This
is a sharper obstruction than the private-color statement from Lemma 8.4c:
it has no \(N_0\) threshold condition and no deleted-pair exception rows.

## Corollary 3.4i: Star gates may be made collective and minimal

Work in the remaining \(k=2\) case after Corollary 8.3b. Thus there is a
finite set \(E_*\subset A\) such that every
\[
a\in A\setminus E_*
\]
has \(A\setminus\{a\}\) as an order-3 basis with some threshold below
\(a\). Suppose \(A\) is still a counterexample to the desired order-3
deletion conclusion.

Then for every finite \(E\supset E_*\) there are constants
\[
q_E,\eta_E>0
\]
and arbitrarily large \(w\) for which one can find a finite set
\[
F\subset A\setminus E,\qquad 2\le |F|\le q_E,
\]
and a gate \(d\in F\), such that:

1. \(F\) is inclusion-minimal for the hole
   \[
   w\notin3(A\setminus F);
   \]
2. every \(f\in F\) is active in the sense of Lemma 8.4b;
3. writing \(C=A\setminus F\), the gate \(d\) has at least
   \[
   \eta_E A(w)
   \]
   unordered retained repairs
   \[
   w-d=a+b,\qquad a,b\in C. \tag{1}
   \]

Consequently the gate is not a singleton order-3 obstruction: since
\[
w=d+a+b\ge d+2\min A>d
\]
for every repair in (1), and the singleton threshold for
\(A\setminus\{d\}\) is below \(d\), the witness \(w\) has a three-term
representation from \(A\setminus\{d\}\). Every such representation must use
at least one element of \(F\setminus\{d\}\).

Proof. Repeat the proof of Corollary 3.4g with the protected core \(E\).
It gives arbitrarily large \(w\) and a bounded transversal
\[
D_0\subset A\setminus E,\qquad |D_0|\le q_E',
\]
for the hypergraph \(\mathcal H_E(w)\), so
\[
w\notin3(A\setminus D_0).
\]
Shrink \(D_0\) to an inclusion-minimal subset \(F\) with
\[
w\notin3(A\setminus F).
\]
Since \(F\subset A\setminus E_*\), Corollary 8.3b rules out
\(|F|=1\), and Lemma 8.4b gives the activity of every element of \(F\).

Every edge of \(\mathcal H_E(w)\) meets \(F\); otherwise it would give a
three-term representation of \(w\) from \(A\setminus F\), except for the
impossible case in which all outside-\(E\) summands are absent, which is
excluded by taking \(w\) larger than every three-term sum from \(E\). The
edge-count lower bound used in Corollary 3.4g is unchanged, and
\[
|F|\le |D_0|\le q_E'.
\]
Hence some \(d\in F\) lies in \(\gg_E A(w)\) edges.

Discard the \(O_E(1)\) edges that also contain another element of
\(F\setminus\{d\}\), and discard the \(O(1)\) edges whose only
representatives use \(d\) with multiplicity at least two. The same support
counting as in Corollary 3.4g leaves \(\eta_E A(w)\) distinct unordered
pairs \(\{a,b\}\subset A\setminus F\) with \(w=d+a+b\), after decreasing
\(\eta_E\) and increasing the lower bound on \(w\) if necessary. Taking
\[
q_E=q_E'
\]
proves (1).

For the final assertion, choose one retained repair \(w=d+a+b\). Then
\[
w>d.
\]
The singleton threshold for \(A\setminus\{d\}\) is \(<d\), so
\[
w\in3(A\setminus\{d\}).
\]
If a representation of \(w\) from \(A\setminus\{d\}\) avoided all of
\(F\setminus\{d\}\), it would lie in \(3(A\setminus F)\), contradicting
the hole. \(\square\)

## Corollary 3.4j: Counterexamples force large reflected low-count slices

In the remaining \(k=2\) counterexample case of Corollary 3.4i, for every
finite \(E\supset E_*\) there are constants
\[
Q_E,\eta_E>0
\]
and arbitrarily large \(w\) for which some
\[
d\in A\setminus E
\]
satisfies
\[
\left|\{a\in A:\ w-d-a\in A,\ r_{2,A}(a+d)\le Q_E\}\right|
   \ge \eta_E A(w). \tag{1}
\]
In particular,
\[
A(w-d)\ge \eta_E A(w). \tag{2}
\]

Proof. Apply Corollary 3.4i and write \(C=A\setminus F\). The gate
\[
d\in F,\qquad |F|\le q_E,
\]
has at least \(\eta_E A(w)\) unordered retained repairs
\[
w-d=a+b,\qquad a,b\in C.
\]
By Corollary 3.4h, every summand occurring in such a repair satisfies
\[
r_{2,A}(a+d)\le |F|\le q_E.
\]
As above, distinct unordered pairs with the same sum \(w-d\) have disjoint
supports unless they are identical, so the repairs contribute at least
\(\eta_E A(w)\) distinct values \(a\) counted in (1). Taking
\[
Q_E=q_E
\]
proves (1). Those same \(a\)'s all lie in \(A\cap[1,w-d]\), proving (2).
\(\square\)

Thus a proof excluding counterexamples may equivalently target reflected
low-count translate slices: one must show that, after a finite core is
protected, no moving translate \(a\mapsto a+d\) can carry a positive
proportion of a reflected slice
\[
A\cap(w-d-A)
\]
into values with bounded two-sum representation count. This statement is
strictly stronger than forbidding a particular hole, because it mentions
only the distribution of low representation counts along moving reflected
slices.

## Warning 3.4k: Low-count reflected slices alone are not contradictory

The reflected low-count slice pattern in Corollary 3.4j cannot be ruled out
from order-2 basishood alone. The benign basis
\[
A=\{1\}\cup2\mathbb N
\]
already has such slices.

Take
\[
d=1,\qquad w=2M+1.
\]
Then
\[
A(w)=M+1.
\]
For every even
\[
a\in\{2,4,\ldots,2M-2\},
\]
one has
\[
w-d-a=2M-a\in A.
\]
Also \(a+d=a+1\) is odd. Since the only odd element of \(A\) is \(1\), the
only unordered two-term representation of \(a+1\) from \(A\) is
\[
a+1=1+a.
\]
Thus
\[
r_{2,A}(a+d)=1
\]
for \(M-1\) values of \(a\), and
\[
\frac{M-1}{A(w)}=\frac{M-1}{M+1}\to1.
\]
The escape is that all these low-count rows are pinned by the fixed element
\(1\). Once \(1\) is included in the protected core, this particular moving
gate is no longer available. Therefore Corollary 3.4j is useful only if the
bounded-count rows remain unpinned outside every finite protected core.

## Lemma 3.4l: Finitely pinned low-count rows cannot support the star obstruction

Let \(A\subseteq\mathbb N\) be an order-2 asymptotic basis. Suppose there is
a finite set \(P\subset A\) such that for every \(Q\ge1\) there is
\(N_Q\) with the following property:
whenever
\[
s>N_Q,\qquad x,y\in A\setminus P,\qquad s=x+y,
\]
one has
\[
r_{2,A}(s)>Q. \tag{1}
\]

Then for every finite \(E\supset P\), every \(Q\ge1\), and every
\(\eta>0\), there is \(W\) such that for all \(w>W\) and all
\[
d\in A\setminus E,
\]
one has
\[
\left|\{a\in A:\ w-d-a\in A,\ r_{2,A}(a+d)\le Q\}\right|
   <\eta A(w). \tag{2}
\]

Proof. Fix \(E\supset P\), \(Q\), and \(\eta\), and take \(N_Q\) from
(1). If \(d\in A\setminus E\), then \(d\notin P\). Let \(a\) be counted in
(2). If
\[
a+d>N_Q
\]
and \(a\notin P\), then the representation
\[
a+d=a+d
\]
uses two elements of \(A\setminus P\), so (1) gives
\[
r_{2,A}(a+d)>Q,
\]
contrary to the definition of the counted set. Hence every counted \(a\)
lies either in \(P\), or satisfies \(a+d\le N_Q\). Since \(d\ge1\), the
latter alternative implies \(a\le N_Q\). Therefore the counted set has size
at most
\[
|P|+A(N_Q),
\]
independently of \(w\) and \(d\). Since \(A(w)\to\infty\), this bound is
less than \(\eta A(w)\) for all sufficiently large \(w\). \(\square\)

For \(A=\{1\}\cup2\mathbb N\), the lemma applies with \(P=\{1\}\): every
large even sum of two unpinned elements has many even-even representations.
Thus the low-count slices in Warning 3.4k are entirely finite-pinned. A
remaining counterexample would need genuinely unpinned bounded-count
translate rows outside every finite protected core, together with the
collective-hole structure from Corollaries 3.4i and 3.4j.

## Corollary 3.4m: Finitely pinned low-count bases satisfy the \(k=2\) conclusion

Let \(A\subseteq\mathbb N\) be an order-2 asymptotic basis. Suppose there
is a finite set \(P\subset A\) such that for every \(Q\ge1\) there is
\(N_Q\) with
\[
s>N_Q,\quad x,y\in A\setminus P,\quad s=x+y
\quad\Longrightarrow\quad
r_{2,A}(s)>Q. \tag{1}
\]
Then there is an infinite \(B\subset A\) such that
\[
A\setminus B
\]
is an asymptotic basis of order \(3\).

Proof. Assume the contrary. By Corollary 8.3b there is a finite
singleton-exceptional set \(E_*\). Put
\[
E=E_*\cup P.
\]
Corollary 3.4j gives constants \(Q_E,\eta_E>0\) and arbitrarily large
\(w\) for which some \(d\in A\setminus E\) satisfies
\[
\left|\{a\in A:\ w-d-a\in A,\ r_{2,A}(a+d)\le Q_E\}\right|
   \ge \eta_E A(w). \tag{2}
\]
But Lemma 3.4l, applied with \(Q=Q_E\), says that the left side of (2) is
\[
o(A(w))
\]
uniformly for all \(d\in A\setminus E\). This contradicts (2) along the
arbitrarily large witnesses. \(\square\)

This criterion covers bases whose low-representation sums are caused by
finitely many permanent accelerators or residue pins. It does not cover
thin bases with unpinned bounded representation counts, which are already
handled separately by Corollary 3.4b. Any remaining \(k=2\) counterexample
must combine large representation spikes with unpinned bounded-count
translate rows after every finite set is protected.

## Corollary 3.4n: Remaining counterexamples have unpinned low-count stars

In the remaining \(k=2\) counterexample case, for every finite
\[
E\supset E_*
\]
there are constants \(Q_E,\eta_E>0\) and arbitrarily large \(w\) for which
some
\[
d\in A\setminus E
\]
satisfies
\[
\left|\{a\in A\setminus E:\ w-d-a\in A\setminus E,
        r_{2,A}(a+d)\le Q_E\}\right|
   \ge \eta_E A(w). \tag{1}
\]
Equivalently, by enlarging the protected core first, the gate \(d\) may be
required to lie above any prescribed bound.

Proof. Apply Corollary 3.4i with a protected core \(E\) that also contains
all elements below the prescribed bound. It gives arbitrarily large \(w\),
an inclusion-minimal finite hole \(F\subset A\setminus E\), a gate
\[
d\in F,
\]
and at least \(\eta A(w)\) unordered retained repairs
\[
w-d=a+b,\qquad a,b\in A\setminus F.
\]
By Corollary 3.4h, every summand in such a repair has
\[
r_{2,A}(a+d)\le |F|\le q_E.
\]
Discard the \(O_E(1)\) repairs using any element of \(E\) as one of the two
retained summands. Distinct unordered repairs have disjoint supports unless
they are identical, so after decreasing the constant and taking \(w\) large
enough, the remaining repairs contribute \(\gg_E A(w)\) distinct summands
\[
a\in A\setminus E
\]
with complementary summand \(w-d-a\in A\setminus E\). Taking
\[
Q_E=q_E
\]
proves (1). \(\square\)

Thus a counterexample cannot hide all bounded-count rows behind finitely
many small accelerators. Outside every finite protected core it must create
a genuinely new low-count star: one fresh center \(d\) has linearly many
fresh reflected neighbours \(a\), and every cross-sum \(a+d\) has bounded
two-term representation count in the full set \(A\).

## Corollary 3.4o: Uniform exclusion of fresh low-count stars gives a good deletion

Let \(A\subseteq\mathbb N\) be an order-2 asymptotic basis. Suppose there
is a finite set \(E_0\subset A\) such that for every \(Q\ge1\) and every
\(\eta>0\) there is \(W\) with the following property: for all
\[
d\in A\setminus E_0,\qquad t+d>W,
\]
one has
\[
\left|\{a\in A\setminus E_0:\ t-a\in A\setminus E_0,
        r_{2,A}(a+d)\le Q\}\right|
   <\eta A(t+d). \tag{1}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. Assume no such infinite deletion exists. Let \(E_*\) be the
singleton-exceptional set from Corollary 8.3b, and put
\[
E=E_0\cup E_*.
\]
Corollary 3.4n supplies constants \(Q_E,\eta_E>0\) and arbitrarily large
\[
w=t+d
\]
with \(d\in A\setminus E\) for which
\[
\left|\{a\in A\setminus E:\ t-a\in A\setminus E,
        r_{2,A}(a+d)\le Q_E\}\right|
   \ge \eta_E A(t+d). \tag{2}
\]
The set counted in (2) is contained in the set counted in (1) with
\[
Q=Q_E,\qquad \eta=\eta_E.
\]
For \(w=t+d\) large enough this contradicts (1). \(\square\)

This is the current clean analytic target for the remaining \(k=2\) case:
prove a uniform reflected low-count star exclusion after deleting one
finite core.

## Warning 3.4p: Fresh low-count stars are locally compatible

Corollary 3.4o requires genuinely global input. No finite-window argument
from order-2 coverage alone can rule out the fresh low-count stars in
Corollary 3.4n.

Fix a finite core \(E\), an integer \(M\), and let
\[
R\ge\max E.
\]
Choose \(N\) so large that
\[
N>R+M,\qquad N^2>N+M.
\]
Put
\[
d=N,\qquad P=\{N^2+1,\ldots,N^2+M\},\qquad T=N^3,
\]
\[
Q=T-P=\{T-p:p\in P\},\qquad w=d+T,
\]
and
\[
A_0=E\cup\{d\}\cup P\cup Q.
\]
For every \(a=p\in P\),
\[
w-d-a=T-p\in Q,
\]
so \(P\) is a reflected star around the fresh gate \(d\), entirely outside
\(E\).

Moreover, for each \(p=N^2+i\in P\), the sum
\[
d+p=N+N^2+i
\]
has exactly one unordered representation from \(A_0\), namely
\[
d+p.
\]
Indeed, any sum involving an element of \(Q\) is too large; \(P+P\) is too
large because \(2N^2+2>N^2+N+M\); \(E+E\), \(E+d\), and \(d+d\) are too
small; and \(E+P\) cannot hit \(d+p\), since
\[
e+(N^2+j)=N+(N^2+i)
\]
would give \(j-i=N-e\), impossible from \(|j-i|\le M-1\) and
\[
N-e\ge N-R>M.
\]
Thus
\[
r_{2,A_0}(d+p)=1\qquad(p\in P).
\]

Finally, adjoining the cofinite tail
\[
[W,\infty),\qquad W>w,
\]
produces a benign order-2 basis and does not change any of these low-count
rows, since every new element is larger than the relevant sums \(d+p\). The
resulting set has an obvious infinite deletion preserving order \(2\), and
hence order \(3\). The construction only shows that the low-count star
normal form is locally compatible; it does not satisfy the global
late-barrier condition in every infinite tail.

## Corollary 3.4q: Uniform low-count degree control is enough

Let \(A\subseteq\mathbb N\) be an order-2 asymptotic basis. Suppose there
is a finite set \(E_0\subset A\) such that for every \(Q\ge1\),
\[
D_Q(X):=\sup_{d\in A\setminus E_0}
 \left|\{a\in A\setminus E_0:\ a\le X,\ r_{2,A}(a+d)\le Q\}\right|
       =o(A(X)). \tag{1}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. Assume the contrary and let \(E_*\) be the finite exceptional set
from Corollary 8.3b. Put
\[
E=E_0\cup E_*.
\]
Corollary 3.4n supplies constants \(Q_E,\eta_E>0\) and arbitrarily large
\(w\), with a gate \(d\in A\setminus E\), such that
\[
\left|\{a\in A\setminus E:\ w-d-a\in A\setminus E,
        r_{2,A}(a+d)\le Q_E\}\right|
   \ge \eta_E A(w). \tag{2}
\]
Every \(a\) counted in (2) satisfies \(a<w\), and since \(E\supset E_0\)
it is also counted in the definition of \(D_{Q_E}(w)\). Hence
\[
D_{Q_E}(w)\ge\eta_E A(w)
\]
for arbitrarily large \(w\), contradicting (1). \(\square\)

Equivalently, a remaining \(k=2\) counterexample has the following
low-count graph consequence: after every finite core is removed, for some
count bound \(Q\) and infinitely many scales \(X\), there is a fresh vertex
\(d\) adjacent through bounded-count sums \(a+d\) to a positive proportion
of \(A\cap[1,X]\). The reflected condition in Corollary 3.4n is stronger,
but this graph-degree shadow is already necessary.

## Corollary 3.4r: Counterexamples contain large reflected low-Schur packets

In the remaining \(k=2\) counterexample case, for every finite
\[
E\supset E_*
\]
there are constants \(Q_E,\eta_E>0\), arbitrarily large \(w\), and elements
\[
d\in A\setminus E,\qquad t=w-d,
\]
with a finite set
\[
S\subset A\setminus E
\]
such that:

1. \(S\) is large:
   \[
   |S|\ge \eta_E A(w);
   \]
2. \(S\) is reflected at \(t\) outside the core:
   \[
   t-S\subset A\setminus E;
   \]
3. every translated row has bounded full representation count:
   \[
   r_{2,A}(s+d)\le Q_E\qquad(s\in S). \tag{1}
   \]

Consequently \(S\) has only linearly many internal translated Schur triples:
the number of unordered pairs \(\{x,y\}\subset S\), counted with
repetition, and \(s\in S\), satisfying
\[
x+y=s+d \tag{2}
\]
is at most
\[
Q_E|S|. \tag{3}
\]

Proof. Take \(S\) to be the set counted in Corollary 3.4n. Then (1) and
the reflected inclusion are exactly the conclusions there. For each fixed
\[
s\in S,
\]
the number of unordered pairs from \(S\) satisfying (2) is at most the full
number of unordered two-term representations of \(s+d\) from \(A\), which
is at most \(Q_E\). Summing over \(s\in S\) proves (3). \(\square\)

Thus the remaining obstruction is not just a large reflected packet; it is
a large reflected packet that is sparse for the shifted equation
\[
x+y=s+d.
\]
If every large reflected packet outside some finite core forced
superlinear internal solutions of this equation for every fresh \(d\), then
Corollary 3.4r would contradict the counterexample normal form.

The moving-anchor bridge criterion in Lemma 8.2a' explains the relevance of
this translated Schur equation. If one tries to delete
\[
b_j=t_j-d
\]
using a moving anchor \(e_j=s\in S\), then the bridge row
\[
t+b_j=e_j+q_j
\]
and the old-anchor rows
\[
e_j+b_i\in2C
\]
ask for two-sum representations of translated values of the form
\[
s+d
\]
or nearby old translates. Corollary 3.4r says that a counterexample can
force these translated rows to have bounded full representation count on a
large reflected packet. Thus the bridge route will need either many
independent reflected packets, or a way to choose anchors that avoid the
bounded-count translated-Schur bottleneck.

## Corollary 3.4s: Star rows are unique or create shifted overlaps

Keep the hypotheses and notation of Corollary 3.4i. Thus
\[
F\subset A,\qquad C=A\setminus F,\qquad w\notin3C,
\]
and the gate \(d\in F\) has many retained repairs
\[
w=d+a+b,\qquad a,b\in C.
\]
Let \(S\subset C\) be the set of retained summands appearing in these
repairs:
\[
S=\{a\in C:\ w-d-a\in C\}.
\]
Then for every \(a\in S\), either
\[
r_{2,A}(a+d)=1, \tag{1}
\]
with the unique representation \(a+d=a+d\), or there is an element
\[
f\in F\setminus\{d\}
\]
such that
\[
a+d-f\in A. \tag{2}
\]
Consequently, if \(|F|\le q\), then either at least \(|S|/2\) elements of
\(S\) satisfy the unique-private alternative (1), or some
\[
f\in F\setminus\{d\}
\]
satisfies (2) for at least
\[
\frac{|S|}{2(q-1)}
\]
elements of \(S\).

Proof. Fix \(a\in S\). Corollary 3.4h gives
\[
a+d\notin2C.
\]
Therefore every two-term representation of \(a+d\) from \(A\) uses an
element of \(F\). One such representation is the trivial gate
representation
\[
a+d=a+d.
\]
If this is the only unordered representation, then (1) holds. Otherwise
take a different representation. It cannot use \(d\), because a
representation of \(a+d\) using \(d\) has the forced complementary summand
\(a\), giving the same unordered pair. Hence it uses some
\[
f\in F\setminus\{d\},
\]
and the complementary summand is \(a+d-f\in A\), proving (2).

The final assertion is just pigeonhole. If fewer than half of the elements
of \(S\) are unique-private, then more than \(|S|/2\) elements satisfy (2)
for one of at most \(q-1\) choices of \(f\). \(\square\)

Thus the fresh low-count star branch splits again. Either the counterexample
has large reflected packets whose rows are genuinely unique for the moving
gate, or it has large reflected packets that are simultaneously shifted
back into \(A\) by one of the moving differences \(d-f\). A positive proof
must rule out both the unpinned unique-row case and the moving shifted-overlap
case, or show that one of them forces the recurrent certificates from
Corollary 2.3c.

## Corollary 3.4t: The remaining star obstruction has two branches

In the remaining \(k=2\) counterexample case, for every finite
\[
E\supset E_*
\]
there are constants \(q_E,\eta_E>0\) and arbitrarily large \(w\) for which
one of the following alternatives holds.

**Unique-gate branch.** There are
\[
d\in A\setminus E,\qquad t=w-d,
\]
and a set
\[
S\subset A\setminus E,\qquad |S|\ge\eta_E A(w),
\]
such that
\[
t-S\subset A\setminus E
\]
and
\[
r_{2,A}(s+d)=1\qquad(s\in S). \tag{1}
\]

**Shifted-overlap branch.** There are distinct
\[
d,f\in A\setminus E,\qquad t=w-d,
\]
and a set
\[
S\subset A\setminus E,\qquad |S|\ge\eta_E A(w),
\]
such that
\[
t-S\subset A\setminus E
\]
and
\[
S+d-f\subset A. \tag{2}
\]
Equivalently, \(S\) is simultaneously reflected at \(t\) and shifted by the
moving difference \(d-f\) into \(A\).

Proof. Apply Corollary 3.4i with protected core \(E\). We get a bounded
minimal hole \(F\), \(|F|\le q_E'\), a gate \(d\in F\), and
\[
\gg_E A(w)
\]
retained star rows
\[
S_0=\{a\in A\setminus F:\ w-d-a\in A\setminus F\}.
\]
Discard the \(O_E(1)\) rows for which \(a\in E\) or \(w-d-a\in E\). For
large \(w\), a positive proportion remains in \(A\setminus E\); call it
\(S_1\).

Corollary 3.4s applied to the rows in \(S_1\) gives two possibilities. If
at least half of \(S_1\) is unique-private for the gate \(d\), take that
subpacket as \(S\), giving (1). Otherwise, since
\[
|F\setminus\{d\}|\le q_E'-1,
\]
some \(f\in F\setminus\{d\}\) has
\[
a+d-f\in A
\]
for a positive proportion of rows \(a\in S_1\). Taking those rows as \(S\)
gives (2). Adjusting the constants gives \(q_E,\eta_E\). \(\square\)

The shifted-overlap branch is the first place where the star normal form
produces a positive-density three-point pattern
\[
s,\quad s+(d-f),\quad t-s
\]
inside \(A\). The unique-gate branch is the opposite extreme: the reflected
packet is large, but every row \(s+d\) is represented only by the intended
gate pair.

## Warning 3.4u: Shifted-overlap packets are locally compatible

The shifted-overlap branch in Corollary 3.4t also cannot be ruled out by a
finite-window order-2 argument.

Fix a finite core \(E\), a positive shift \(h\), and a positive integer
\(M\). Choose a spacing
\[
L>2h
\]
and let
\[
R\ge\max(E\cup\{h\}).
\]
Choose \(N\) so large that
\[
N>(M-1)L+R+h
\]
and the following elementary separations hold:
\[
N^3-N^2-ML>N^2+ML+N+h, \tag{a}
\]
\[
2(N^2+L)>N^2+ML+N+h, \tag{b}
\]
\[
2(N+h)<N^2+L+N+h. \tag{c}
\]
Now put
\[
f=N,\qquad d=N+h,
\]
\[
P=\{N^2+iL:1\le i\le M\},\qquad P_h=P+h,
\]
\[
T=N^3,\qquad Q=T-P,\qquad w=d+T.
\]
Let
\[
A_0=E\cup\{f,d\}\cup P\cup P_h\cup Q.
\]
For every \(p\in P\),
\[
w-d-p=T-p\in Q
\]
and
\[
p+d=(p+h)+f. \tag{1}
\]
Thus \(P\) is a reflected packet around the fresh gate \(d\), and it is
also shifted by \(h=d-f\) into \(A_0\).

For \(N\) and \(L\) as above, the only unordered representations of
\[
p_i+d=N^2+iL+N+h\qquad(1\le i\le M)
\]
from \(A_0\) are
\[
p_i+d,\qquad (p_i+h)+f. \tag{2}
\]
Write \(p_i=N^2+iL\). A representation using an element of \(Q\) is too
large by (a), because the least element of \(Q\) already exceeds the largest
row \(p_i+d\). A representation using two elements of \(P\cup P_h\) is too
large by (b), and a representation using only elements of
\(E\cup\{f,d\}\) is too small by (c).

It remains to check mixed representations. If
\[
e+p_j=p_i+d\qquad(e\in E,\ p_j\in P),
\]
then
\[
N=(j-i)L+e-h,
\]
contradicting \(N>(M-1)L+R+h\). If
\[
e+(p_j+h)=p_i+d,
\]
then
\[
N=(j-i)L+e,
\]
again impossible. The only representations using \(f\) or \(d\) and one
packet element are the two displayed in (2): equations
\[
f+p_j=p_i+d,\qquad d+(p_j+h)=p_i+d
\]
would force \((j-i)L=h\) and \((j-i)L=-h\), respectively, which are
impossible since \(L>2h\); while
\[
d+p_j=p_i+d,\qquad f+(p_j+h)=p_i+d
\]
force \(j=i\).

Hence
\[
r_{2,A_0}(p+d)=2\qquad(p\in P),
\]
and every row lies in the shifted-overlap branch through the same
\[
f=d-h.
\]
Adjoining a cofinite tail \([W,\infty)\) with \(W>w\) makes a benign
order-2 basis without changing these rows. Therefore the shifted-overlap
branch, like the unique-gate branch in Warning 3.4p, requires global
barrier input to rule out.

## Corollary 3.4v: Fixed branch recurrence collapses

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
there are a nonzero integer \(h\) and distinct elements \(e,y\in A\) such
that
\[
e+h,\ y+h\in A
\]
and, for arbitrarily large \(t\),
\[
t-e,\quad t-y,\quad t-(e+h)\in A. \tag{1}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. The triple
\[
R=\{e,y,e+h\}
\]
is reflection-recurrent by (1). It is a certificate triple in the sense of
Corollary 2.3c, because
\[
y+(e+h)-e=y+h\in A.
\]
Corollary 2.3c gives the desired deletion. \(\square\)

Thus a shifted-overlap obstruction can persist only if the difference
\[
h=d-f
\]
or the shifted rows themselves escape every finite test set. The analogous
unique-gate statement is the same fixed-certificate test in disguise: if a
fixed certificate triple
\[
e,y_1,y_2,\qquad y_1+y_2-e\in A,
\]
is contained in \(S\) or in \(t-S\) for reflected packets with arbitrarily
large \(t\), then it is reflection-recurrent and Corollary 2.3c again gives
a good deletion. Consequently both branches in Corollary 3.4t are now
reduced to genuine mass escape rather than a fixed local pattern.

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
\(P\subset A\), a hypergraph \(\mathcal F\) on \(P\) whose edges are finite
nonempty sets, and witnesses \(w_F\) indexed by \(F\in\mathcal F\),
satisfying:

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

## Proposition 7.1: Eventually periodic bases satisfy finite-core stability

Let \(A\subseteq\mathbb N\) be eventually periodic: there are \(m\ge1\),
a nonempty residue set \(S\subseteq\mathbb Z/m\mathbb Z\), and \(N_0\) such
that for all \(n\ge N_0\),
\[
n\in A\quad\Longleftrightarrow\quad n\bmod m\in S.
\]
If \(A\) is an asymptotic basis of order \(k\), then:

1. there is a finite core \(E\subset A\) such that for every finite
   \(F\subset A\setminus E\), the set \(A\setminus F\) is an asymptotic
   basis of order \(k+1\);
2. there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
   asymptotic basis of order \(k+1\).

Proof. Since \(S\ne\varnothing\), the eventual periodic tail of \(A\)
contains a tail-syndetic subset. Apply Proposition 3.1f. \(\square\)

## Corollary 7.1b: Bases with eventually periodic subbases

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\). Suppose
there is an eventually periodic subset
\[
P\subseteq A
\]
which is itself an asymptotic basis of order \(k\). Then:

1. there is a finite core \(E\subset A\) such that every finite
   \(F\subset A\setminus E\) leaves \(A\setminus F\) an order-\((k+1)\)
   basis;
2. there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
   asymptotic basis of order \(k+1\).

Proof. Apply Proposition 7.1 to \(P\). It gives a finite core
\[
E_P\subset P
\]
such that every finite \(G\subset P\setminus E_P\) leaves \(P\setminus G\)
an order-\((k+1)\) basis. Put \(E=E_P\). If \(F\subset A\setminus E\) is
finite, then
\[
P\setminus(F\cap P)
\]
is an order-\((k+1)\) basis and is contained in \(A\setminus F\). This
proves finite-core stability for \(A\).

Proposition 7.1 also gives an infinite
\[
B\subset P
\]
such that \(P\setminus B\) is an order-\((k+1)\) basis. Since
\[
P\setminus B\subseteq A\setminus B,
\]
the larger set \(A\setminus B\) is also an order-\((k+1)\) basis.
\(\square\)

Thus any counterexample to the broad deletion theorem cannot contain an
eventually periodic order-\(k\) subbasis. In particular, the obstruction is
not merely the presence of nonperiodic or sparse extra elements; it must be
built into every order-\(k\) subbasis of \(A\). Moreover, eventually
periodic bases cannot refute the finite-core finite-deletion stability
target from Reduction 0.

## Example 7.2: Finite deletion can raise the order by an arbitrary amount

Finite-deletion stability at order \(k+1\), with no protected finite core,
is false even for eventually periodic bases. Fix \(m\ge5\). Let
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

## Lemma 8.2a': Moving-anchor bridge repair

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Let
\[
B=\{b_1,b_2,\ldots\}\subset A,
\qquad C=A\setminus B.
\]
Suppose there is a fixed retained element \(t\in C\) such that for every
\(j\) there are retained elements
\[
e_j,q_j\in C
\]
with
\[
t+b_j=e_j+q_j, \tag{1}
\]
and for every \(i\le j\),
\[
e_j+b_i\in2C. \tag{2}
\]
Then \(C\) is an asymptotic basis of order \(3\).

Proof. We verify Lemma 8.2a with center \(t\). The one-deleted repair is
exactly (1):
\[
t+b_j=e_j+q_j\in2C.
\]
For diagonal two-deleted repairs, (1) and (2) with \(i=j\) give
\[
t+2b_j=q_j+(e_j+b_j)\in3C.
\]
For \(i<j\), (1) and (2) give
\[
t+b_i+b_j=q_j+(e_j+b_i)\in3C.
\]
The same identity, with indices swapped if necessary, covers all
\(b_i+b_j+t\). Lemma 8.2a now gives that \(C\) is an order-3 basis.
\(\square\)

This criterion separates two tasks that are fused in the fixed-certificate
construction. The row \(e_j+b_j\in2C\) can come from a reflected packet at a
moving anchor \(e_j\), while the bridge identity \(t+b_j=e_j+q_j\) connects
that moving anchor back to the fixed padder \(t\). The old-anchor rows
\(e_j+b_i\in2C\) are the coherence condition needed to repair mixed
deleted pairs.

The finite diagnostic `EXPERIMENTS/bridge_repair_search.py` checks these
identities in local windows. In the delayed pair example
\[
S=\{1,2,3,5,6,7\},\qquad F=\{5,7\},
\]
it finds the bridge data
\[
t=1,\qquad (b,e_b,q_b)=(5,3,3),(7,2,6).
\]
Thus this local pair delay is repairable by Lemma 8.2a'. By contrast, the
rank-three delayed example
\[
S=\{1,2,3,4,5,6,7,8\},\qquad F=\{4,5,6\}
\]
and the alternating pair-hole window
\[
S=\{1,2,3,6,7,8\},\qquad F=\{6,8\}
\]
have no such bridge data in the finite set, even after trying all orderings
of \(F\). The `--all-orders` search also finds rank-three windows with
bridge data, such as
\[
S=\{1,2,3,4,5,6,7\},\qquad F=\{1,3,4\}.
\]
Thus the bridge route is a real positive mechanism, and high rank alone
does not defeat it, but it is not a complete explanation of all collective
finite holes.

The same diagnostic includes the finite windows that remain active in the
Schreier-stage investigation. It finds no bridge data, even after all
deletion orderings are tried, for the first Schreier seed pair
\[
S=\{1,2,3,4,8\},\qquad F=\{1,4\},
\]
for the first Schreier seed triple \(F=\{2,3,4\}\) in the same \(S\), for
the tail P5 pair
\[
S=\{1,2,4,5,8,10,15,18,19,30\},\qquad F=\{10,30\},
\]
and for the P6 pair-edge escape
\[
S=\{1,2,4,5,8,10,15,18,19,30,38,40,43,44\},\qquad F=\{10,38\}.
\]
So Lemma 8.2a' records an important repair pattern, but it does not absorb
the surviving Schreier/P6 finite obstructions by itself.

## Warning 8.2b: Fixed-center greedy absorption has star obstructions

Lemma 8.2a suggests a direct greedy proof for \(k=2\): fix a retained
center \(e\), choose deleted elements one at a time, and require each new
choice to repair all deleted multisets of size at most two. For a finite
deleted prefix \(D\), call a candidate \(b\in A\setminus(D\cup\{e\})\)
\(e\)-good over \(D\) if, with
\[
C_b=A\setminus(D\cup\{b\}),
\]
one has
\[
e+b\in2C_b,\qquad e+2b\in3C_b, \tag{1}
\]
and
\[
e+d+b\in3C_b\qquad(d\in D). \tag{2}
\]
If every finite prefix \(D\) has arbitrarily large \(e\)-good extensions
outside the finite set of already protected repair summands, then choosing
such extensions recursively gives an infinite \(B\) for which
\[
A\setminus B
\]
is an order-3 basis by Lemma 8.2a.

The missing extension lemma is not a consequence of the existing one-point
and pair-barrier results. If all sufficiently large \(b\) fail to be
\(e\)-good over a fixed finite \(D\), the failures can occur in three
different ways.

First, one can have a fixed-center two-sum failure
\[
e+b\notin2C_b. \tag{3}
\]
This is weaker than a one-point order-3 failure: it only says that the
specific repair \(e+b\) has no two-term retained representation. The set
\(A\setminus\{b\}\) may still be an order-3 basis with threshold below
\(b\).

Second, one can have a diagonal failure
\[
e+2b\notin3C_b. \tag{4}
\]
When \(D=\varnothing\), infinitely many such failures are singleton
order-3 failures and are handled by Corollary 8.3. For nonempty \(D\), an
inclusion-minimal bad set for the same witness may include old elements of
\(D\), so this becomes a finite-prefix obstruction rather than a new
singleton obstruction.

Third, for some fixed old deleted element \(d\in D\), one can have the
star-shaped old-new pair failure
\[
e+d+b\notin3C_b. \tag{5}
\]
For fixed \(d\), (5) is a bounded-top-excess family of pair holes for
\(\{d,b\}\). Corollary 8.6b does not rule this out, because that corollary
requires pair barriers inside every infinite tail. An infinite future
deletion can simply avoid the already committed element \(d\), so a star
around \(d\) is not a cofinite-tail barrier.

Thus a fixed-center greedy absorption proof would need new input: either a
way to vary the center coherently with the deleted pattern, or an argument
turning persistent star-shaped failures into a genuine tail barrier. This
is the same coherence problem illustrated by Example 8.8.

The finite script `EXPERIMENTS/star_pair_search.py` shows that this is not
only a logical possibility. It finds
\[
A_0=\{1,2,3,4,7,10\},
\]
whose two-sums cover through \(14\). With fixed center \(e=1\) and old
deleted element \(d=3\), the later candidates
\[
b=4,7,10
\]
have minimal star holes
\[
e+d+b=8,11,14
\]
respectively:
\[
e+d+b\notin3(A_0\setminus\{d,b\}),
\]
while restoring either \(d\) or \(b\) repairs the displayed witness. This
finite window does not construct an infinite obstruction, but it confirms
that fixed-prefix star poisoning is compatible with genuine local two-sum
coverage.

## Lemma 8.2c: A pure fixed star forces tail recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Fix \(e,d\in A\). Suppose there are infinitely many
\[
b\in A
\]
such that
\[
e+d+b\notin3(A\setminus\{d,b\}). \tag{1}
\]
Then the tail
\[
A\cap(d+e,\infty)
\]
is reflection-recurrent: for every finite
\[
T\subset A\cap(d+e,\infty)
\]
and every \(L\), there is \(m>L\) with
\[
m-T\subset A.
\]
Consequently there is an infinite \(B\subset A\) such that \(A\setminus B\)
is an order-3 basis.

Proof. Fix finite \(T\subset A\cap(d+e,\infty)\) and \(L\). Choose \(b\)
satisfying (1), with
\[
b+e>L,\qquad b+d+e-\max T\ge N_0,
\]
and \(b\notin T\). Put
\[
w=e+d+b.
\]
For each \(t\in T\), the integer \(w-t\) is at least \(N_0\), so it has a
two-term representation from \(A\). If some representation avoided both
\(d\) and \(b\), then adding the retained summand \(t\) would give
\[
w\in3(A\setminus\{d,b\}),
\]
contrary to (1). Hence every two-term representation of \(w-t\) uses \(d\)
or \(b\). It cannot use \(b\), because the remaining summand would be
\[
w-t-b=d+e-t<0.
\]
Therefore a representation uses \(d\), and
\[
w-t=d+(b+e-t)
\]
with \(b+e-t\in A\). Thus
\[
m=b+e
\]
satisfies \(m-T\subset A\) and \(m>L\). Lemma 2.4 gives the desired
infinite deletion. \(\square\)

## Lemma 8.2c': Uniform low-excess fixed pair-stars force tail recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Fix \(d\in A\) and a constant \(D\ge0\). Put
\[
M=\max\{D,d\}.
\]
Suppose that for every finite nonempty
\[
T\subset A\cap(M,\infty)
\]
and every \(L\), there are
\[
b\in A\setminus(T\cup\{d\}),\qquad w\in\mathbb N,
\]
such that
\[
w-\max T\ge N_0,\qquad w-d>L,\qquad b\le w\le b+D, \tag{1}
\]
and
\[
w\notin3(A\setminus\{d,b\}). \tag{2}
\]
Then the tail \(A\cap(M,\infty)\) is reflection-recurrent. Consequently
there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. It is enough to prove the recurrence assertion for nonempty \(T\);
the empty test set is automatic. Fix finite nonempty
\[
T\subset A\cap(M,\infty)
\]
and \(L\), and choose \(b,w\) satisfying (1)--(2). Put
\[
m=w-d.
\]
Then \(m>L\). For each \(t\in T\), the integer \(w-t\) is at least
\(N_0\), so choose a two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A.
\]
If some such representation avoided both \(d\) and \(b\), then, since
\[
t\notin\{d,b\},
\]
adding \(t\) would put \(w\) in \(3(A\setminus\{d,b\})\), contradicting
(2). Hence every two-term representation of \(w-t\) uses \(d\) or \(b\).
It cannot use \(b\), because the other summand would be
\[
w-t-b\le D-t<0,
\]
as \(t>D\). Therefore some representation uses \(d\), say
\[
w-t=d+c_t,\qquad c_t\in A.
\]
Thus
\[
m-t=w-d-t=c_t\in A
\]
for every \(t\in T\). Since \(L\) was arbitrary, \(A\cap(M,\infty)\) is
reflection-recurrent. Lemma 2.4 gives the infinite deletion. \(\square\)

This is the fixed-endpoint analogue of the bounded second-excess argument
in Lemma 8.6a. It still does not close the finite-prefix star obstruction
by itself: the hypothesis is uniform over finite test sets and requires
genuine pair-private holes for \(\{d,b\}\). A prefix star may instead be
repaired after deleting only \(\{d,b\}\) but fail after a larger old core is
deleted, as in the finite example below.

## Lemma 8.2c'': Low-excess fixed-singleton barriers force tail recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Fix \(d\in A\) and \(D\ge0\), and put
\[
M=\max\{D,d\}.
\]
Suppose that for every finite nonempty
\[
T\subset A\cap(M,\infty)
\]
and every \(L\), there are a finite nonempty set
\[
G\subset A\setminus(T\cup\{d\})
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad w-d>L,\qquad \min G\le w\le \min G+D, \tag{1}
\]
and
\[
w\notin3(A\setminus(\{d\}\cup G)). \tag{2}
\]
Then the tail \(A\cap(M,\infty)\) is reflection-recurrent. Consequently
there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. Fix finite nonempty \(T\subset A\cap(M,\infty)\) and \(L\), and
choose \(G,w\) satisfying (1)--(2). Put \(F=\{d\}\cup G\). For each
\(t\in T\), choose a two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A,
\]
which exists because \(w-t\ge N_0\). If some representation avoided \(F\),
then adding \(t\in A\setminus F\) would put \(w\) in \(3(A\setminus F)\),
contrary to (2). Hence every two-term representation of \(w-t\) uses
either \(d\) or an element of \(G\).

No element \(g\in G\) can occur, since
\[
w-t-g\le w-t-\min G\le D-t<0.
\]
Therefore some representation uses \(d\), and
\[
w-t=d+c_t,\qquad c_t\in A.
\]
With \(m=w-d\), this gives \(m>L\) and
\[
m-t=c_t\in A\qquad(t\in T).
\]
Thus \(A\cap(M,\infty)\) is reflection-recurrent, and Lemma 2.4 gives the
desired deletion. \(\square\)

Lemma 8.2c' is the special case \(|G|=1\). The point of the more general
form is that an enumerated Schreier edge first completed by a fixed prefix
vertex has exactly one fixed endpoint and several later moving endpoints.
If its witness remains close to the first later endpoint, all those moving
endpoints are too large to color shifted test rows, so the fixed endpoint
again reflects the tail.

## Lemma 8.2c''': Intermediate endpoint excess gives fractional recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Fix \(D\ge0\) and \(j\ge1\). Suppose that for every
finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(L\), there are distinct elements
\[
f_0,f_1,\ldots,f_r\in A\setminus T,\qquad r\ge j,
\]
with
\[
f_1<\cdots<f_r,
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad w-\max\{f_0,f_1,\ldots,f_{j-1}\}>L,
\qquad w\le f_j+D, \tag{1}
\]
and
\[
w\notin3(A\setminus\{f_0,f_1,\ldots,f_r\}). \tag{2}
\]
Then for every finite nonempty \(T\subset A\cap(D,\infty)\) and every
\(L_0\), there is a subset
\[
U\subset T,\qquad |U|\ge |T|/j,
\]
and a center \(m>L_0\) such that
\[
m-U\subset A. \tag{3}
\]

If, in addition, there is a finite
\[
T_0\subset A\cap(D,\infty)
\]
such that every \(U\subset T_0\) with \(|U|\ge |T_0|/j\) contains a
certificate triple
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. Fix finite nonempty \(T\subset A\cap(D,\infty)\) and \(L_0\), and
apply the hypothesis with \(L>L_0+\max T\). For each \(t\in T\), choose a
two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A,
\]
possible because \(w-t\ge N_0\). By (2), every such representation meets
\[
F=\{f_0,\ldots,f_r\}.
\]
No representation can use \(f_\ell\) with \(\ell\ge j\), since
\[
w-t-f_\ell\le f_j+D-t-f_\ell\le D-t<0.
\]
Thus each \(t\) has a representation using one of
\[
f_0,f_1,\ldots,f_{j-1}.
\]
Pigeonhole gives one such \(f_i\) and a subset
\[
U\subset T,\qquad |U|\ge |T|/j,
\]
for which
\[
w-t=f_i+c_t,\qquad c_t\in A\quad(t\in U).
\]
Then
\[
m=w-f_i
\]
satisfies \(m-U\subset A\), and (1) gives \(m>L_0\).

For the final assertion, apply the first part to \(T_0\) with \(L_0\to
\infty\). Each resulting large subset \(U\subset T_0\) contains a
certificate triple, and since \(T_0\) has only finitely many such triples,
one fixed triple is reflected by arbitrarily large centers. Corollary 2.3c
gives the desired deletion. \(\square\)

The case \(j=1\) recovers Lemma 8.2c'' with \(f_0\) the fixed endpoint:
all moving endpoints are too large to appear, so the whole test set
reflects through \(f_0\). For \(j>1\), the obstruction falls back to the
same certificate-free fractional-recurrence branch as Lemma 8.6g.

For the pure-star setting, more generally, if a fixed finite prefix
\(\Delta\) and infinitely many candidates \(b\) satisfy
\[
e+d+b\notin3(A\setminus(\Delta\cup\{b\}))
\]
for some \(d\in \Delta\), the same proof gives only fractional recurrence: for
each finite tail test set \(T\), the shifted representations of
\[
e+d+b-t
\]
must use one of the finitely many elements of \(\Delta\), and
pigeonholing gives a reflected subset of \(T\) of size at least
\(|T|/|\Delta|\). This falls back to the certificate-free recurrent-cluster
obstruction after Lemma 8.6c, which is why the fixed-center greedy proof
still does not close the remaining case.

## Lemma 8.2d: Multi-center stars force certificates unless large subsets are certificate-free

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Fix a finite nonempty set \(D\subset A\) and elements
\[
e,d_0\in A.
\]
Suppose that for every finite
\[
T\subset A\cap(d_0+e,\infty)
\]
and every \(L\), there is
\[
b\in A\setminus(D\cup T),\qquad b>L,
\]
such that, with
\[
w=e+d_0+b,
\]
one has
\[
w-\max T\ge N_0,\qquad w\notin3(A\setminus(D\cup\{b\})). \tag{1}
\]
If there is a finite
\[
T_0\subset A\cap(d_0+e,\infty)
\]
such that every subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/|D|,
\]
contains a certificate triple
\[
x,y_1,y_2\in U,\qquad y_1\ne x,\quad y_2\ne x,\quad y_1+y_2-x\in A,
\]
then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. We show that a certificate triple in \(T_0\) is reflection-recurrent
and then apply Corollary 2.3c. Let \(L_0\) be arbitrary. Apply the
hypothesis with \(T=T_0\) and \(L\) so large that
\[
L+d_0+e-\max D>L_0+\max T_0.
\]
For each \(t\in T_0\), choose a two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A,
\]
possible because \(w-t\ge N_0\). By (1), every such representation meets
\[
D\cup\{b\}.
\]
It cannot use \(b\), since
\[
w-t-b=d_0+e-t<0.
\]
Choose one element \(f_t\in D\) used by the representation. Some
\[
f\in D
\]
is chosen on a subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/|D|.
\]
For every \(t\in U\), the chosen representation has the form
\[
w-t=f+c_t,\qquad c_t\in A,
\]
so the center
\[
m=w-f=b+d_0+e-f
\]
reflects \(U\) into \(A\). The choice of \(L\) gives
\[
m>L_0+\max T_0.
\]
By the certificate-density hypothesis, choose
\[
x,y_1,y_2\in U,\qquad y_1,y_2\ne x,\qquad y_1+y_2-x\in A.
\]
There are only finitely many triples in \(T_0\), so along an unbounded
sequence of \(L_0\)'s one same certificate triple recurs. Corollary 2.3c
gives the desired infinite deletion. \(\square\)

Thus a finite-prefix star obstruction can persist only in the same
certificate-free regime as Lemma 8.6g: every finite test set in the relevant
tail must contain a certificate-free subset of size at least
\(|T|/|D|\).

## Lemma 8.2e: Finite-core singleton barriers have the same certificate escape

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\), and fix a finite nonempty set \(D\subset A\). Suppose
there is a finite
\[
T_0\subset A\setminus D
\]
such that every subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/(|D|+1),
\]
contains a certificate triple
\[
e,y_1,y_2\in U,\qquad y_1\ne e,\quad y_2\ne e,\quad y_1+y_2-e\in A.
\]
Assume that for every \(L\) there are
\[
b\in A\setminus(D\cup T_0),\qquad w\in\mathbb N,
\]
such that
\[
w-\max T_0\ge N_0,\qquad w-\max D>L+\max T_0, \tag{1}
\]
\[
w\notin3(A\setminus(D\cup\{b\})), \tag{2}
\]
and either
\[
w-b>L+\max T_0 \tag{3}
\]
or
\[
w-b<\min T_0. \tag{4}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. We show that some certificate triple in \(T_0\) is
reflection-recurrent, and then apply Corollary 2.3c. Fix \(L_0\), and apply
the hypothesis with \(L>L_0\). For every \(t\in T_0\), choose a two-term
representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A,
\]
which exists by \(w-\max T_0\ge N_0\). If this representation avoided
\[
D\cup\{b\},
\]
then adding \(t\in A\setminus(D\cup\{b\})\) would put \(w\) in
\[
3(A\setminus(D\cup\{b\})),
\]
contrary to (2). Choose one color
\[
c_t\in(D\cup\{b\})\cap\{a_t,a'_t\}.
\]
Some color \(c\in D\cup\{b\}\) occurs on a subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/(|D|+1).
\]

If \(c=b\), then (4) is impossible, since \(b\) occurring in a
representation of \(w-t\) would leave the other summand \(w-t-b<0\).
Therefore (3) holds, and the center
\[
m=w-b
\]
reflects \(U\) into \(A\). Moreover \(m>L_0+\max T_0\). If \(c\in D\),
then the center
\[
m=w-c
\]
reflects \(U\) into \(A\), and (1) again gives \(m>L_0+\max T_0\).

By the certificate-density hypothesis on \(T_0\), choose a certificate
triple \(e,y_1,y_2\in U\). There are only finitely many such triples in
\(T_0\), so as \(L_0\to\infty\) one fixed certificate triple is reflected
by arbitrarily large centers. Corollary 2.3c gives the desired infinite
deletion. \(\square\)

This covers the two clean delayed-singleton regimes over a fixed finite
core. If the excess \(w-b\) is unbounded, the moving element \(b\) itself
can serve as the color and gives reflected centers \(w-b\). If the excess
is bounded, one chooses \(T_0\) above that bound, so \(b\) cannot appear in
the shifted two-sum rows and the colors come from the fixed core. The only
remaining finite-core singleton escape is again the large certificate-free
subset alternative.

The important limitation is that a prefix star need not descend to a genuine
pair hole. In the finite window
\[
A_0=\{1,2,3,4,5,6,7\},
\]
take
\[
e=1,\qquad D=\{4,6\},\qquad d=6,\qquad b=7,
\]
and
\[
C=A_0\setminus(D\cup\{b\})=\{1,2,3,5\}.
\]
The non-star repairs hold:
\[
e+b=8=3+5\in2C,\qquad e+2b=15=5+5+5\in3C.
\]
But the star repair fails:
\[
e+d+b=14\notin3C.
\]
This is not a pair-private hole for \(\{d,b\}\), because
\[
14=4+5+5\in3(A_0\setminus\{6,7\}).
\]
Indeed the obstruction is minimal for the triple \(\{4,6,7\}\):
\[
14=3+5+6\in3(A_0\setminus\{4,7\}),\qquad
14=2+5+7\in3(A_0\setminus\{4,6\}).
\]
Thus persistent pair-private stars would create a genuine graph barrier on
a tail, but persistent prefix stars can be irreducibly hypergraph-valued.
This is why the fixed-center greedy route again leads back to
Schreier-type finite barriers rather than to the pair-barrier results alone.

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
   f\le w;
   \]
2. for every \(f\in F'\), there is a multiplicity
   \(q_f\in\{1,2,3\}\) and elements
   \(c_{f,1},\ldots,c_{f,3-q_f}\in A\setminus F'\) such that
   \[
   w=q_f f+c_{f,1}+\cdots+c_{f,3-q_f};
   \]
   when \(q_f=3\), no \(c\)-terms appear;
   moreover
   \[
   q_f f+(3-q_f)m_0\le w;
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
representation must use \(f\). Let \(q_f\) be the number of copies of \(f\)
in one such representation. The other summands avoid \(F'\), so
\[
w=q_f f+c_{f,1}+\cdots+c_{f,3-q_f},
\qquad c_{f,i}\in A\setminus F',
\]
which proves (2). The multiplicity bound in (2) follows because every
remaining summand is at least \(m_0\). Since \(q_f\ge1\), (1) follows.

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

## Lemma 8.4c: Holes force private deleted-retained sums

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Let \(F\subset A\) be finite, put
\[
C=A\setminus F,
\]
and suppose
\[
w\notin3C.
\]
Then every retained element \(e\in C\) with \(w-e\ge N_0\) satisfies
\[
w-e\notin2C. \tag{1}
\]
Moreover, if
\[
w-e=f+a,\qquad f\in F,\quad a\in C, \tag{2}
\]
then
\[
e+f\notin2C. \tag{3}
\]
Consequently, if \(e\in C\), \(w-e\ge N_0\), and
\[
w-e\notin F+F,
\]
then there is some \(f\in F\) such that
\[
w-e-f\in C,\qquad e+f\notin2C. \tag{4}
\]
Equivalently, if
\[
e+F\subseteq2C
\]
and \(w-e\ge N_0\), then any three-fold hole \(w\notin3C\) forces
\[
w-e\in F+F. \tag{5}
\]

Proof. If \(w-e\in2C\), then adding \(e\in C\) gives
\[
w\in3C,
\]
contrary to the hypothesis. This proves (1).

Now assume (2). If \(e+f\in2C\), say \(e+f=c+d\) with
\[
c,d\in C,
\]
then
\[
w=e+f+a=c+d+a\in3C,
\]
again a contradiction. Hence (3) holds.

For the consequence, \(w-e\ge N_0\) gives a two-term representation of
\(w-e\) from \(A\). By (1) it cannot use only elements of \(C\). If
\(w-e\notin F+F\), at least one representation has exactly one summand in
\(F\) and one summand in \(C\), say
\[
w-e=f+a,\qquad f\in F,\quad a\in C.
\]
Then \(w-e-f=a\in C\), and (3) gives \(e+f\notin2C\). Statement (5) is the
contrapositive of (4). \(\square\)

This is a necessary condition on any genuine collective hole, not a
sufficient one. It rules out arithmetizations of the abstract Schreier
model in which the retained tail is too absorptive after deleting \(F\):
if a large set of possible padders \(T\subset C\) satisfies
\[
T+F\subseteq2C,
\]
then every \(e\in T\) below the witness must have \(w-e\in F+F\). Thus a
hole cannot be protected against a whole interval of retained padders by
ordinary shifted domination alone; it must also supply a private-sum
incidence from most retained padders to the deleted set. In finite-stage
language, a reflected-Schreier construction would have to color each
relevant retained padder \(e\) by some deleted element \(f\in F\) with
\[
w-e-f\in A_s\setminus F,\qquad
e+f\notin2(A_s\setminus F),
\]
except for the exceptional \(F+F\) values. This is the arithmetic
condition missing from the purely abstract model in Warning 10.3c.

### Corollary 8.4c.1: Absorptive test sets are pair-sum bounded

Keep the hypotheses of Lemma 8.4c. Let \(T\subset C\) be finite and suppose
\[
w-\max T\ge N_0,\qquad T+F\subseteq2C. \tag{1}
\]
Then
\[
|T|\le |F+F|. \tag{2}
\]
In particular, if
\[
|F|=r,
\]
then
\[
|T|\le \frac{r(r+1)}2. \tag{3}
\]

Proof. For every \(t\in T\), condition (1) gives \(t+F\subseteq2C\). By
Lemma 8.4c, the hole \(w\notin3C\) forces
\[
w-t\in F+F.
\]
The map \(t\mapsto w-t\) is injective, so \(|T|\le |F+F|\). The final
bound is the trivial count of unordered deleted-pair sums. \(\square\)

Thus a fixed-rank collective hole cannot coexist with an arbitrarily large
retained test set whose translates by \(F\) are all absorbed into \(2C\).
This is the precise no-go for direct arithmetizations of the abstract
Schreier model that use a thick retained tail. It does not defeat the
actual Schreier escape by itself: for an edge of rank \(r\), the natural
earlier prefix has only \(O(r)\) rows, while \(F+F\) may have \(O(r^2)\)
exception values.

## Lemma 8.4d: Private colors have low matching capacity

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite of size \(r\),
and put
\[
C=A\setminus F.
\]
For \(f\in F\) and \(s\in\mathbb N\), let
\[
\nu_f(s)
\]
be the maximum number of pairwise vertex-disjoint two-term representations
of \(s\) from \(A\) that do not use \(f\). Here a representation
\(s=x+y\) uses the vertices \(\{x,y\}\), with a double representation
\(s=2x\) using the single vertex \(x\).
Equivalently, \(\nu_f(s)\) is just the number of unordered two-term
representations of \(s\) from \(A\setminus\{f\}\): two distinct unordered
representations of the same two-sum cannot share a vertex, since sharing
one summand forces the other summand as well.

If
\[
t+f\notin2C,
\]
then
\[
\nu_f(t+f)<r. \tag{1}
\]
Consequently, in the setting of Lemma 8.4c, for every finite
\[
T\subset C,\qquad w-T\subset[N_0,\infty),
\]
if
\[
E_2=\{t\in T:w-t\in F+F\},
\]
then
\[
T\setminus E_2
\subseteq
\bigcup_{f\in F}
\{t\in T:w-t-f\in C,\ \nu_f(t+f)<r\}. \tag{2}
\]
In particular,
\[
|T\setminus E_2|
\le
\sum_{f\in F}
\left|\{t\in T:w-t-f\in C,\ \nu_f(t+f)<r\}\right|. \tag{3}
\]

Proof. Suppose \(t+f\) has \(r\) pairwise vertex-disjoint two-term
representations from \(A\), none using \(f\). Since \(t+f\notin2C\), every
one of these representations must use at least one vertex from \(F\).
Because the representations avoid \(f\), each must use a vertex from
\[
F\setminus\{f\}.
\]
Pairwise vertex-disjointness lets any fixed vertex of \(F\setminus\{f\}\)
occur in at most one representation, but
\[
|F\setminus\{f\}|=r-1.
\]
This cannot hit \(r\) disjoint representations. Hence (1) holds.

For (2), apply Lemma 8.4c to each
\[
t\in T\setminus E_2.
\]
It gives a color \(f\in F\) such that
\[
w-t-f\in C,\qquad t+f\notin2C.
\]
The first part and (1) give membership in the displayed union. Inequality
(3) follows by counting the union with multiplicity. \(\square\)

This converts the private-color condition into a matching-capacity
obstruction, equivalently a low two-sum representation-count obstruction.
A Schreier edge of rank \(r\) can protect a retained test point \(t\)
through color \(f\) only when the cross-sum \(t+f\) has fewer than \(r\)
two-term representations avoiding \(f\). Thus any
unbounded-rank reflected-Schreier counterexample must arrange a large
supply of low-matching cross-sums, after removing the exceptional
\(F+F\)-rows.

Two cautions are important. First, Lemma 8.4d gives a cover, not a
matching. A single deleted element can privately color many retained
points. For instance,
\[
C=\{1,2,98,99\},\qquad F=\{7\},\qquad w=107
\]
has \(107\notin3C\), while both retained points \(1\) and \(2\) are served
by the same deleted color:
\[
107-1=7+99,\qquad 107-2=7+98,
\]
and
\[
1+7,\ 2+7\notin2C.
\]
Second, the exceptional rows \(w-t\in F+F\) cannot simply be ignored. If
\[
F=\{R+1,\ldots,R+r\},
\]
then
\[
F+F=[2R+2,2R+2r],
\]
so a witness \(w=2R+2r+q\) can make
\[
w-(F+F)=[q,q+2r-2],
\]
an interval of length comparable to \(r\). This is exactly the scale of
the early Schreier prefix. A positive proof through Lemma 8.4d must
control both the low-matching rows and the \(F+F\) exception window.

## Warning 8.4e: Low representation-count rows can be cofinite

Lemma 8.4d is sharp enough to rule out absorptive or highly redundant
local lifts, but no unconditional sparsity statement for its low-count rows
can follow from the order-2 basis property alone.

Fix a finite set \(F_0\subset\mathbb N\) and \(r\ge1\). Choose
\[
m>\max F_0
\]
and put
\[
A=m\mathbb N\cup\{1,2,\ldots,m-1\}. \tag{1}
\]
Then \(A\) is an asymptotic basis of order \(2\): if \(n\equiv i\pmod m\)
with \(1\le i\le m-1\), then for large \(n\)
\[
n=i+(n-i),
\]
and if \(m\mid n\), then
\[
n=m+(n-m).
\]

For every \(f\in F_0\) and every sufficiently large
\[
t\in m\mathbb N,
\]
the cross-sum \(t+f\) has no two-term representation from
\[
A\setminus\{f\}.
\]
Indeed, two multiples of \(m\) have residue \(0\pmod m\), two elements of
\(\{1,\ldots,m-1\}\) are too small for large \(t\), and a mixed
representation of residue \(f\pmod m\) must use the unique small residue
\(f\), which is forbidden. Hence
\[
\nu_f(t+f)=0<r
\]
for all such \(t\), simultaneously for every \(f\in F_0\).

Thus the low-count set
\[
L_{r,f}=\{t\in A:\nu_f(t+f)<r\}
\]
may contain a cofinite tail of an arithmetic progression in \(A\), and the
common intersection
\[
\bigcap_{f\in F_0} L_{r,f}
\]
may be cofinite in the infinite part of \(A\). In particular, there is no
general Sidon, bounded-energy, or sparse-intersection theorem for these
sets in arbitrary order-2 bases. The example is eventually periodic and is
handled positively by Proposition 7.1, but it shows that any use of Lemma
8.4d must exploit more than order-2 coverage.

There are only dense local substitutes. If \(B=A\setminus\{f\}\) and
\[
|B\cap[1,s-1]|\ge\frac{s-1}{2}+r,
\]
then \(s\) has at least \(r\) two-term representations from \(B\). Indeed,
\[
|B\cap(s-B)|\ge2|B\cap[1,s-1]|-(s-1)\ge2r,
\]
and each unordered representation contributes at most two ordered witnesses.
Therefore dense intervals inside \(A\), or lower density above \(1/2\),
force low-count rows to disappear. This is not relevant to the remaining
sparse case after Proposition 3.1f, but it is a useful check on finite
block constructions.

## Proposition 8.4f: Private-color normal form for the remaining \(k=2\) obstruction

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Suppose \(A\) is a counterexample to the desired
order-3 deletion conclusion. Let \(E\subset A\) be the finite exceptional
set from Corollary 8.3b, so that every singleton deletion
\[
A\setminus\{a\},\qquad a\in A\setminus E,
\]
is an order-3 basis with threshold below \(a\).

Then for every finite \(T\subset A\), every infinite
\[
X\subset A\setminus(T\cup E),
\]
and every \(L\), there are a finite set
\[
F\subset X,\qquad |F|\ge2,
\]
and a witness \(w>L\) such that, after replacing \(F\) by an
inclusion-minimal subhole for this \(w\), the following hold. Put
\[
C=A\setminus F,\qquad r=|F|.
\]

1. \(w\notin3C\), but restoring any one element of \(F\) repairs the hole:
   \[
   w\in3(A\setminus(F\setminus\{f\}))\qquad(f\in F).
   \]
2. Every \(f\in F\) is active with a multiplicity \(q_f\in\{1,2,3\}\) as
   in Lemma 8.4b.
3. The terminal retained gap holds:
   \[
   C\cap(w-\min F-\min A,\ w-N_0]=\varnothing.
   \]
4. For every \(t\in T\cap C\) with \(w-t\ge N_0\), either
   \[
   w-t\in F+F,
   \]
   or there is a color \(f=\chi(t)\in F\) such that
   \[
   w-t-f\in C,\qquad t+f\notin2C,\qquad \nu_f(t+f)<r. \tag{1}
   \]

Proof. Lemma 8.4 gives a finite late-bad \(F_0\subset X\) and a witness
\(w>L\) with \(w\notin3(A\setminus F_0)\). Shrink \(F_0\)
inclusion-minimally for this same witness and call the result \(F\). Since
we have \(F\subset X\subset A\setminus E\), Corollary 8.3b gives
\(|F|\ge2\). Lemma 8.4b gives the inclusion-minimal repair and active
multiplicity statements, and Lemma 8.4a gives the terminal retained gap.

Finally fix \(t\in T\cap C\) with \(w-t\ge N_0\). If \(w-t\notin F+F\),
Lemma 8.4c gives a color \(f\in F\) with
\[
w-t-f\in C,\qquad t+f\notin2C.
\]
Lemma 8.4d then gives
\[
\nu_f(t+f)<r.
\]
This proves (4). \(\square\)

Thus the still-open \(k=2\) case is exactly the possibility of such
private-color barriers in every infinite tail, with ranks possibly growing
fast enough to evade finite certificate tests and with low-count rows
possibly living in sparse, non-syndetic parts of the basis. The proposition
is not a new obstruction; it is the consolidated checklist any final proof
or counterexample must now defeat.

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

## Warning 8.4a': Terminal gaps do not yield a sparse-prefix proof

The terminal-gap condition alone cannot prove that a sufficiently sparse
deletion sequence avoids all collective late-bad sets. The location of the
gap is controlled by the witness, and in a sparse basis it may simply fall
inside an ordinary gap of \(A\), or isolate a later deleted point.

A finite model already shows the limitation. Let
\[
4\le f<g,\qquad g>2f,
\]
and put
\[
A_0=\{1,f-1,f,g-1,g\},\qquad F=\{f,g\},\qquad C=A_0\setminus F.
\]
For
\[
w=f+g
\]
we have
\[
w\notin3C.
\]
Indeed the only retained elements are \(1,f-1,g-1\), and a direct list of
their three-fold sums gives
\[
3,\ f+1,\ g+1,\ 2f-1,\ f+g-1,\ 2g-1,\ 3f-3,\ 2f+g-3,\ f+2g-3,\ 3g-3,
\]
none of which is \(f+g\) under the displayed inequalities. Restoring either
deleted point repairs the hole:
\[
w=f+1+(g-1)=g+1+(f-1).
\]
With \(m_0=1\) and \(N_0=2\), the terminal interval from Lemma 8.4a is
\[
(w-f-1,\ w-2]=(g-1,\ f+g-2],
\]
and its only point of \(A_0\) is the deleted point \(g\).

Thus even a two-point active collective hole can satisfy the terminal
retained gap by placing one deleted point in an otherwise empty terminal
window. A final proof must use the stronger shifted two-sum vertex-cover
and low-count row information from Lemma 10.1 and Corollary 3.4t, not only
the terminal gap.

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

## Warning 8.5a.1: The first Schreier barrier is not universal

The closure of the enumerated-Schreier target in Corollary 13.1l.3a does
not by itself close all unbounded finite barriers. There are higher
Schreier-type barriers with no first-prefix pair links on any tail.

Let
\[
P=\{p_1<p_2<\cdots\}.
\]
Define the first Schreier barrier
\[
\mathcal S_1(P)=\{F\subset P:\ |F|=\operatorname{index}(\min F)+1\}.
\]
Now define \(\mathcal S_2(P)\) to consist of all finite unions
\[
F=F_0\cup F_1\cup\cdots\cup F_r
\]
such that
\[
F_0<F_1<\cdots<F_r,\qquad F_j\in\mathcal S_1(P),
\]
and
\[
r+1=\operatorname{index}(\min F_0)+1.
\]
Then \(\mathcal S_2(P)\) is a barrier on \(P\). Indeed, given any infinite
\[
X\subset P,
\]
choose \(F_0\) to be the first \(\operatorname{index}(\min X)+1\) elements
of \(X\). This is an \(\mathcal S_1(P)\)-edge. Since \(X\) is infinite,
repeat the same construction after \(F_0\) to choose \(F_1\), and so on
until the required number of blocks has been chosen. Their union is an
\(\mathcal S_2(P)\)-edge inside \(X\).

However, no infinite
\[
M=\{m_1<m_2<\cdots\}\subset P
\]
has
\[
\mathcal S_1(M)\subseteq \mathcal S_2(P).
\]
The first Schreier barrier on \(M\) contains two-element edges
\[
\{m_1,m_j\}\qquad(j>1),
\]
whereas every \(\mathcal S_2(P)\)-edge contains at least two nonempty
\(\mathcal S_1(P)\)-blocks and therefore has size greater than \(2\).

Thus an arbitrary variable-rank late-bad barrier cannot be reduced by pure
combinatorics to the first-prefix-link structure of Lemma 13.1j. A final
argument must either extract additional arithmetic structure from the
finite holes, or handle higher front ranks directly.

There are even simpler unbounded fronts whose rank is controlled by a later
point rather than by the first point. On
\[
P=\{2,3,4,\ldots\}
\]
define
\[
\mathcal B_2
=\{\{x_1<\cdots<x_m\}\subset P:\ m=x_2\}.
\]
Every infinite
\[
X=\{x_1<x_2<x_3<\cdots\}\subset P
\]
contains the edge
\[
\{x_1,\ldots,x_{x_2}\}\in\mathcal B_2.
\]
But fixing the first point does not fix the edge size; the second point
does. Thus no thinning can make this front look like the complete
first-prefix-link criterion from Lemma 13.1j.

The correct abstract target is therefore a recursive front analysis. For a
front \(\mathcal F\) and a finite initial segment \(s\), consider the
section
\[
\mathcal F_s=\{G:\ s\cup G\in\mathcal F,\ \max s<\min G\}.
\]
A proof that rules out variable-rank barriers must show that admissible
arithmetic holes either descend to a lower-rank section with the same
private-incidence structure, or produce a finite recurrent
certificate-free coloring, already impossible by Lemma 8.6g''''.2. Pure
combinatorics alone does not provide that descent.

### Lemma 8.5a.2: Front sections are fronts

Let \(P\) be an infinite ordered set, and let \(\mathcal F\) be a front on
\(P\): no two members of \(\mathcal F\) contain one another, and every
infinite
\[
X=\{x_1<x_2<\cdots\}\subset P
\]
has a unique initial segment in \(\mathcal F\). Let \(s\subset P\) be a
finite initial segment of some member of \(\mathcal F\), but suppose no
initial segment of \(s\) lies in \(\mathcal F\). Put
\[
P_s=\{p\in P:p>\max s\}
\]
and
\[
\mathcal F_s=\{G\subset P_s:s\cup G\in\mathcal F\}.
\]
Then \(\mathcal F_s\) is a front on \(P_s\).

Proof. Let \(Y\subset P_s\) be infinite. Apply the front property of
\(\mathcal F\) to the infinite ordered set
\[
s\cup Y.
\]
Its unique initial segment in \(\mathcal F\) cannot be a proper initial
segment of \(s\), by the hypothesis on \(s\). Hence it has the form
\[
s\cup G
\]
for some finite initial segment \(G\) of \(Y\), and \(G\in\mathcal F_s\).
This proves existence. Uniqueness and the antichain property for
\(\mathcal F_s\) follow immediately from the corresponding properties of
\(\mathcal F\). \(\square\)

Thus higher-front barriers can be studied recursively through their
sections. The missing arithmetic step is to show that the private-incidence
normal form survives passage to a section strongly enough to run an
induction, rather than merely producing selector-avoidable full cuts.

### Lemma 8.5a.3: Bounded section-depth excess gives fractional recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Fix a finite set
\[
\Delta\subset A,
\]
a number \(D\ge0\), and an integer \(j\ge1\). Suppose that for every finite
nonempty
\[
T\subset A\cap(D,\infty)\setminus\Delta
\]
and every \(L\), there are distinct
\[
g_1<\cdots<g_r,\qquad r\ge j,
\]
in
\[
A\setminus(T\cup\Delta)
\]
and a witness \(w\) such that, with
\[
F=\Delta\cup\{g_1,\ldots,g_r\},
\]
one has
\[
w-\max T\ge N_0,\qquad
w-f>L\quad(f\in\Delta\cup\{g_1,\ldots,g_{j-1}\}), \tag{1}
\]
\[
w\le g_j+D, \tag{2}
\]
and
\[
w\notin3(A\setminus F). \tag{3}
\]
Then for every finite nonempty \(T\subset A\cap(D,\infty)\setminus\Delta\)
and every \(L_0\), there are a subset
\[
U\subset T,\qquad |U|\ge\frac{|T|}{|\Delta|+j},
\]
and a center \(m>L_0\) such that
\[
m-U\subset A. \tag{4}
\]

If, in addition, there is a finite
\[
T_0\subset A\cap(D,\infty)\setminus\Delta
\]
such that every \(U\subset T_0\) with
\[
|U|\ge\frac{|T_0|}{|\Delta|+j}
\]
contains a certificate triple
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. Fix \(T\) and \(L_0\), and apply the hypothesis with
\[
L>L_0+\max T.
\]
For each \(t\in T\), choose a two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A,
\]
which exists because \(w-t\ge N_0\). By (3), every such representation
meets \(F\). It cannot use any \(g_\ell\) with \(\ell\ge j\), because
\[
w-t-g_\ell\le g_j+D-t-g_\ell\le D-t<0.
\]
Thus each \(t\in T\) has a representation using one of the at most
\[
|\Delta|+j-1\le |\Delta|+j
\]
colors in
\[
\Delta\cup\{g_1,\ldots,g_{j-1}\}.
\]
Choose one such color for each \(t\). By pigeonhole, some color \(f\) is
chosen on a subset \(U\subset T\) with
\[
|U|\ge |T|/(|\Delta|+j).
\]
For \(t\in U\),
\[
w-t=f+c_t
\]
with \(c_t\in A\). Hence the center
\[
m=w-f
\]
satisfies \(m-U\subset A\), and (1) gives \(m>L_0\).

For the final assertion, apply the first part to \(T_0\) with \(L_0\to
\infty\). Every resulting \(U\) contains a certificate triple, and since
\(T_0\) is finite one fixed certificate triple is reflected by arbitrarily
large centers. Corollary 2.3c gives the desired deletion. \(\square\)

Thus a variable-rank front section can survive only if, for every bounded
depth \(j\), either its witnesses have unbounded excess over the \(j\)-th
moving endpoint, or every finite test has a large
\((|\Delta|+j)^{-1}\)-fraction certificate-free subset. This is the
section-level analogue of Lemma 8.2c'''.

### Corollary 8.5a.4: Bounded-depth section list-coloring is impossible

Keep \(A,\Delta,D,j\) as in Lemma 8.5a.3. It is impossible that for every
finite nonempty
\[
T\subset A\cap(D,\infty)\setminus\Delta
\]
and every \(M\), there are
\[
g_1<\cdots<g_r,\qquad r\ge j,
\]
a witness \(w\), and a coloring of \(T\) by the finite label set
\[
\Lambda=\Delta\cup\{1,\ldots,j-1\}
\]
such that:

1. every label has a large center:
   \[
   w-f>M\quad(f\in\Delta),\qquad w-g_\ell>M\quad(1\le\ell<j);
   \]
2. if \(t\) receives label \(f\in\Delta\), then
   \[
   w-t-f\in A;
   \]
   and if \(t\) receives label \(\ell\in\{1,\ldots,j-1\}\), then
   \[
   w-t-g_\ell\in A;
   \]
3. every label fiber is certificate-free relative to \(A\).

Proof. If \(\Lambda=\varnothing\), there is no coloring of a nonempty
\(T\). Otherwise enumerate
\[
A\cap(D,\infty)\setminus\Delta=\{a_1,a_2,\ldots\}
\]
and apply the hypothesis to \(T_n=\{a_1,\ldots,a_n\}\) with \(M=n\). By
compactness of the finite product \(\Lambda^{\mathbb N}\), pass to a
subsequence on which each fixed \(a_i\) has a stable label. Let
\[
C_\lambda\qquad(\lambda\in\Lambda)
\]
be the stable fibers. Every \(C_\lambda\) is certificate-free, hence Sidon.

If \(U\subset C_\lambda\) is finite, then for all sufficiently large stages
all elements of \(U\) lie in the \(\lambda\)-fiber. If \(\lambda=f\in
\Delta\), the centers \(w_n-f\) tend to infinity and reflect \(U\) into
\(A\). If \(\lambda=\ell\), the centers \(w_n-g_{n,\ell}\) do the same.
Thus every nonempty stable fiber is reflection-recurrent in \(A\).
Lemma 8.6g''''.2 forbids a finite Sidon coloring of an infinite set by
recurrent nonempty fibers. This contradiction proves the corollary.
\(\square\)

Therefore the large certificate-free subsets allowed by Lemma 8.5a.3
cannot be coherently assigned to finitely many bounded-depth endpoint
slots across all finite tests. A surviving variable-rank front must make
the relevant color palette itself escape to unbounded section depth.

## Lemma 8.5b: Complete fixed-rank barriers have unbounded top excess

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\), and put \(m_0=\min A\). Let \(P\subset A\) be cofinite
in \(A\). Fix \(r\ge2\) and \(D\ge0\). It is impossible that, for all
sufficiently late
\[
F\in[P]^r,
\]
there is a witness \(w_F\) satisfying
\[
\max F\le w_F\le \max F+D,\qquad
w_F\notin3(A\setminus F). \tag{1}
\]

Proof. Suppose such \(P,r,D\) exist. Choose \(T\) so that (1) holds
whenever \(\min F>T\). We first prove a local counting bound. For every
sufficiently large \(x>T\), put
\[
I_x=[x,\ 2x+m_0-D-1]\cap\mathbb N.
\]
We claim that
\[
|P\cap I_x|\le r+N_0+1. \tag{2}
\]
Assume otherwise, and let
\[
Y=P\cap I_x,\qquad y_0=\min Y,\qquad y_*=\max Y.
\]
At most \(N_0\) integers of \(Y\) lie in \((y_*-N_0,y_*]\), so there is an
element
\[
e\in Y\setminus\{y_0\},\qquad e\le y_*-N_0.
\]
Since \(|Y\setminus\{e\}|\ge r\), choose
\[
F\in[Y\setminus\{e\}]^r
\]
containing \(y_0\) and \(y_*\). Then \(\min F=y_0>T\), so (1) supplies
\[
w=w_F.
\]
By Lemma 8.4a,
\[
(A\setminus F)\cap(w-y_0-m_0,\ w-N_0]=\varnothing. \tag{3}
\]
But \(e\notin F\), so \(e\in A\setminus F\). Also \(w\ge y_*\) and
\(e\le y_*-N_0\) give
\[
e\le w-N_0.
\]
On the other side, \(y_*\le2x+m_0-D-1\) and \(y_0\ge x\), so
\[
w-y_0-m_0\le y_*+D-y_0-m_0<y_0<e.
\]
Thus \(e\) lies in the forbidden interval (3), a contradiction. This proves
(2).

Now cover the tail of \(\mathbb N\) by consecutive intervals of the form
\[
I_{x_j}=[x_j,\ 2x_j+m_0-D-1],
\qquad
x_{j+1}=2x_j+m_0-D,
\]
starting with \(x_0\) large enough that \(x_j>T\) and \(x_{j+1}>x_j\). The
number of such intervals needed to reach \(X\) is \(O(\log X)\), and each
contains at most \(r+N_0+1\) points of \(P\). Since \(A\setminus P\) is
finite,
\[
|A\cap[1,X]|=O(\log X). \tag{4}
\]
This contradicts order-2 basishood: if \(A(X)=|A\cap[1,X]|\), then for all
large \(X\), the integers in \([N_0,X]\) are represented by ordered pairs
from \(A\cap[1,X]\), hence
\[
X-N_0+1\le A(X)^2,
\]
so \(A(X)\gg\sqrt X\). \(\square\)

Therefore a complete fixed-rank barrier on a cofinite tail can only evade
the positive theory by having unbounded top excess \(w_F-\max F\) on every
tail, or by abandoning fixed rank. In the bounded-width case, Lemma 8.6
then forces fractional recurrence; the remaining escape is the
certificate-free recurrent-cluster obstruction from Warning 8.6c'.

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

## Warning 8.6c': Large recurrent clusters can be certificate-free

The certificate obstruction after Lemma 8.6c is not an artefact of an
abstract combinatorial model. It can occur inside a benign order-2 basis.

Let
\[
U=\{n\in\mathbb N:n\equiv0\text{ or }1\pmod3\}.
\]
Since \(\{0,1\}+\{0,1\}=\mathbb Z/3\mathbb Z\), the set \(U\) is an
asymptotic basis of order \(2\). We may enlarge \(U\) by a very sparse
set of elements congruent to \(2\pmod3\) without destroying this property.

By a standard sparse induction one can choose finite sets
\[
S_M\subset 2+3\mathbb N,\qquad |S_M|=M\quad(M=1,2,\ldots),
\]
and, for each \(M\), arbitrarily large centers \(m_{M,q}\) such that:

1. all reflected packets
   \[
   m_{M,q}-S_M
   \]
   are positive, pairwise disjoint, and disjoint from \(U\);
2. no element added in any packet or in any \(S_N\) lies in
   \[
   S_M+S_M-S_M
   \]
   except for the trivial forced elements of \(S_M\) themselves.

At each finite stage only finitely many affine equalities are forbidden, so
the next \(S_M\) and the next centers can be placed far enough out in the
residue class \(2\pmod3\) to avoid them. Put
\[
A=U\cup\bigcup_M S_M\cup\bigcup_{M,q}(m_{M,q}-S_M).
\]
Then \(A\) is still an order-2 basis because \(U\subset A\). Each \(S_M\)
is reflection-recurrent in \(A\), since
\[
m_{M,q}-S_M\subset A
\]
for arbitrarily large \(m_{M,q}\). However, by construction, for
\[
e,y_1,y_2\in S_M,\qquad y_1,y_2\ne e,
\]
the candidate certificate element
\[
y_1+y_2-e
\]
does not belong to \(A\). Its residue is \(2\pmod3\), so it is not in
\(U\), and the sparse induction avoided all inserted elements.

Thus arbitrarily large recurrent clusters in an order-2 basis do not, by
themselves, force the fixed-triple hypothesis of Corollary 2.3c. Any
positive use of Lemma 8.6c must exploit the fact that the recurrent clusters
come from genuine finite-barrier witnesses, not merely from their existence
inside an order-2 basis.

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

## Warning 8.6f: In the sparse case, ordinary gaps mimic terminal gaps

After Proposition 3.1f, any counterexample to the broad deletion theorem has
no tail-syndetic subset. In that remaining case the terminal retained gap
from Lemma 8.4a is not, by itself, a strong obstruction.

Let \(A\) be an order-2 basis with threshold \(N_0\), put
\(m_0=\min A\), and suppose \(A\) has arbitrarily long tail gaps. Let
\(F\subset A\) be finite and nonempty, write \(f_0=\min F\), and assume
\[
f_0>N_0-m_0.
\]
Then for every \(L\) there is \(w>L\) such that
\[
(A\setminus F)\cap(w-f_0-m_0,\ w-N_0]=\varnothing. \tag{1}
\]
Indeed, choose
\[
x>L-f_0-m_0
\]
so far out that
\[
A\cap(x,\ x+f_0+m_0-N_0]=\varnothing,
\]
and put \(w=x+f_0+m_0\). Then (1) is exactly this ordinary \(A\)-gap.

Thus the sparse case supplies terminal windows of every relevant length
without using any additive nonrepresentation. The missing input in the
remaining \(k=2\) problem is therefore the arithmetic part of Lemma 8.4:
the same finite set \(F\) must be a vertex cover for all shifted two-sum
representation graphs below the witness. Any proof that only selects an
infinite deletion to avoid complete terminal windows is vulnerable to the
local-isolation pattern in Warning 8.6e.

## Warning 8.6f': Alternating deletions do not defeat collective holes

A natural refinement of the sparse-deletion strategy is to choose an
infinite \(B\subset A\) with no two consecutive elements in the \(A\)-order.
If \(F\subset B\) creates a hole \(w\notin3(A\setminus F)\), Lemma 8.4a
gives
\[
A\cap(w-\min F-m_0,\ w-N_0]\subset F.
\]
Since \(F\subset B\), the terminal interval then contains at most one
element of \(A\). This is a genuine strengthening, but it is still not
enough.

The finite window
\[
S=\{1,2,3,6,7,8\}
\]
has
\[
[2,13]\subseteq2S.
\]
Let
\[
B=\{2,6,8\},\qquad F=\{6,8\},\qquad C=S\setminus F=\{1,2,3,7\}.
\]
The set \(B\) has no two consecutive elements in the \(S\)-order, but
\[
14\notin3C.
\]
With \(N_0=2\), \(m_0=1\), and \(f_0=\min F=6\), the terminal interval is
\[
(14-6-1,\ 14-2]=(7,12],
\]
and
\[
S\cap(7,12]=\{8\}\subset F.
\]
Thus alternating deletion has reduced the terminal window to one deleted
point.

The shifted vertex-cover condition still holds. For every retained
\[
e\in C,\qquad e\le12,
\]
all two-term representations of \(14-e\) from \(S\) use \(6\) or \(8\):
\[
13=6+7,\qquad 12=6+6,\qquad 11=3+8,\qquad 7=1+6.
\]
Therefore terminal-window sparsification alone cannot prove the theorem. A
global argument would still be needed to rule out infinitely many
singleton-terminal-window collective holes.

## Lemma 8.6g: Large-excess barriers force certificates unless large subsets are certificate-free

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Suppose there is an integer \(r\ge1\) with the
following property: for every finite \(T\subset A\) and every \(L\), there
are a finite set
\[
F\subset A\setminus T,\qquad |F|=r,
\]
and a witness \(w\) such that
\[
w-\max F>L,\qquad w-\max T\ge N_0,\qquad
w\notin3(A\setminus F). \tag{1}
\]
Suppose further that there is a finite \(T_0\subset A\) such that every
subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/r,
\]
contains elements \(e,y_1,y_2\in U\) with
\[
y_1\ne e,\qquad y_2\ne e,\qquad y_1+y_2-e\in A. \tag{2}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. We prove that a certificate triple as in Corollary 2.3c is
reflection-recurrent. Fix \(L_0\). Apply the large-excess hypothesis to
the finite set \(T_0\), with
\[
L>\max\{L_0+\max T_0,\ \max T_0+N_0\}.
\]
This gives \(F\subset A\setminus T_0\), \(|F|=r\), and \(w\) satisfying
(1). For each \(t\in T_0\), the integer \(w-t\) is at least \(N_0\), so
choose a two-term representation
\[
w-t=a_t+a'_t,\qquad a_t,a'_t\in A.
\]
By Lemma 10.1, every such representation meets \(F\). Choose one element
\[
f_t\in F
\]
that appears in the chosen representation. For some \(f\in F\), the color
class
\[
U=\{t\in T_0:f_t=f\}
\]
has size at least \(|T_0|/r\). By hypothesis, choose
\[
e,y_1,y_2\in U,\qquad y_1+y_2-e\in A,\qquad y_1,y_2\ne e.
\]
For every \(t\in U\), the chosen representation has the form
\[
w-t=f+c_t
\]
with \(c_t\in A\), hence
\[
(w-f)-t=c_t\in A.
\]
Thus the center
\[
m=w-f
\]
reflects \(\{e,y_1,y_2\}\) into \(A\). Since \(f\le\max F\),
\[
m=w-f\ge w-\max F>L_0+\max T_0,
\]
so these reflecting centers are arbitrarily large as \(L_0\to\infty\).

There are only finitely many triples in \(T_0\). Along an unbounded
sequence of \(L_0\)'s, one same triple \(e,y_1,y_2\) satisfying (2) occurs.
That triple is reflection-recurrent in \(A\). Corollary 2.3c gives the
desired infinite deletion. \(\square\)

Consequently, any large-excess fixed-rank barrier counterexample must have
a strong certificate-free property: every finite test set \(T\subset A\)
has a subset of size at least \(|T|/r\) containing no triple
\[
e,y_1,y_2,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A.
\]
For pair barriers, this says every finite test set has a certificate-free
half-subset. This is much stronger than the existence of the recurrent
certificate-free clusters in Warning 8.6c'.

It is useful to make the rank dependence explicit. For a finite
\[
T\subset A
\]
write
\[
\alpha_A(T)=\max\{|U|:U\subset T\text{ is certificate-free relative to }A\}
\]
and
\[
\Gamma_A(T)=\frac{|T|}{\alpha_A(T)}.
\]
The proof above only uses the inequality
\[
|F|<\Gamma_A(T_0) \tag{3}
\]
for one finite test set \(T_0\): coloring each \(t\in T_0\) by one
deleted element of \(F\) used in a chosen representation of \(w-t\), some
color class has size at least \(|T_0|/|F|>\alpha_A(T_0)\), and hence
contains a certificate triple. Thus any variable-rank large-excess
counterexample must have the following escape property:

for every finite \(T\subset A\), all sufficiently late barriers that are
forced outside \(T\) may have rank at least \(\Gamma_A(T)\).

This is the precise rank-sensitive form of the certificate-free obstruction.
Fixed-rank barriers fail as soon as \(\Gamma_A(T)\) is larger than that
rank for some finite \(T\); Schreier-type barriers try to evade the
argument by letting \(|F|\) grow beyond every finite certificate test.

### Corollary 8.6g.1: Fixed-rank full list-color barriers are impossible

Fix \(r\ge1\). Let \(A\subseteq\mathbb N\) be infinite. It is impossible
that for every finite
\[
T\subset A
\]
and every \(M\), there are a witness \(w\), an ordered \(r\)-tuple of
distinct colors
\[
F=(f_1,\ldots,f_r)\subset A\setminus T,
\]
and a coloring
\[
\chi:T\to\{1,\ldots,r\}
\]
such that:

1. every color center is large:
   \[
   w-f_i>M\qquad(1\le i\le r);
   \]
2. every colored row is reflected by its color:
   \[
   w-t-f_{\chi(t)}\in A\qquad(t\in T);
   \]
3. every fiber
   \[
   \chi^{-1}(i)
   \]
   is certificate-free relative to \(A\).

Proof. Enumerate \(A=\{a_1<a_2<\cdots\}\), put
\[
T_j=\{a_1,\ldots,a_j\},
\]
and choose data as in the hypothesis with \(M=j\). By compactness of
\[
\{1,\ldots,r\}^{\mathbb N},
\]
pass to a subsequence on which the color of every fixed \(a_n\) stabilizes.
Let
\[
C_1,\ldots,C_r
\]
be the stable color classes. Each \(C_i\) is certificate-free relative to
\(A\), hence Sidon.

If \(U\subset C_i\) is finite, then for all sufficiently large stages in
the subsequence, every element of \(U\) lies in the \(i\)-th fiber. The
centers
\[
m_j=w_j-f_{j,i}
\]
tend to infinity because \(m_j>j\), and they satisfy
\[
m_j-U\subset A.
\]
Thus every nonempty stable color class is reflection-recurrent in \(A\).
Applying Lemma 8.6g''''.2 to the finite Sidon coloring after discarding
empty classes shows that each stable color class has size at most \(r\).
Hence
\[
A=C_1\cup\cdots\cup C_r
\]
is finite, contradiction. \(\square\)

Thus fixed-rank high-excess barriers cannot evade Lemma 8.6g merely by
list-coloring every finite test into endpoint-certificate-free fibers. A
remaining fixed-rank obstruction would have to fail the full-list
hypothesis above while still avoiding a single finite certificate-density
test.

For variable rank, the same argument gives only a rank lower bound when a
coherent finite-color compactification exists. If \(q\) recurrent Sidon
colors cover a finite test set \(T\), Lemma 8.6g''''.2 gives
\[
|T|\le q^2.
\]
Thus any variable-rank list-color barrier of this type must use
\[
q\ge\sqrt{|T|}.
\]
Schreier-scale barriers can evade this estimate by assigning singleton or
bounded fibers to the active prefix, so a final argument must force color
reuse rather than only finite colorability.

### Warning 8.6g.2: Variable rank by coverage neighborhoods is selector-avoidable

The most direct way to make the rank large is to delete every endpoint that
covers the active shifted rows. This creates a different obstruction.

Let
\[
F\subset A,\qquad C=A\setminus F,\qquad w\notin3C.
\]
For an active retained padder
\[
e\in C,\qquad w-e\ge N_0,
\]
define its retained-complement coverage neighborhood
\[
N_e=\{f\in A:\ w-e-f\in C\}. \tag{1}
\]
Then
\[
N_e\subset F. \tag{2}
\]
Indeed, if \(f\in N_e\cap C\), then
\[
w=e+f+(w-e-f)\in3C,
\]
contrary to the hole.

Thus a variable-rank construction can make all endpoint fibers tiny by
taking
\[
F\supseteq\bigcup_{e\in T}N_e
\]
for the finite active test set \(T\). But then the bad set is a full cut of
coverage neighborhoods. If a proper subedge
\[
H\subsetneq F
\]
leaves some \(f\in N_e\setminus H\) retained, then
\[
w=e+f+(w-e-f)\in3(A\setminus H).
\]
So the witness is private for the whole neighborhood cut, not for arbitrary
Schreier subedges. An infinite selector can avoid containing whole
block-local cuts unless the construction supplies additional cross-block
coding. This is the current concrete obstruction to using unbounded rank
alone to evade Corollary 8.6g.1.

## Lemma 8.6h: Progressions force certificate density

Let \(A\subseteq\mathbb N\) and let
\[
P=\{a,a+d,\ldots,a+(L-1)d\}\subset A
\]
be an \(L\)-term arithmetic progression. If \(S\subset P\) is
certificate-free, meaning that there are no
\[
e,y_1,y_2\in S,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then
\[
|S|\le2.
\]

Proof. Identify \(P\) with the index interval \(\{0,\ldots,L-1\}\). If
\[
i<j
\]
are two indices in \(S\), then certificate-freeness with
\[
e=i,\qquad y_1=y_2=j
\]
forces
\[
2j-i\ge L, \tag{1}
\]
because otherwise the corresponding progression element lies in \(P\subset
A\). Similarly, using
\[
e=j,\qquad y_1=y_2=i
\]
forces
\[
2i-j<0. \tag{2}
\]
If \(S\) had three indices \(i<j<k\), then (1) applied to \(i<j\) gives
\[
j\ge L/2,
\]
while (2) applied to \(j<k\) gives
\[
k>2j\ge L,
\]
contradicting \(k\le L-1\). Hence \(|S|\le2\). \(\square\)

Therefore, for a fixed rank \(r\), any order-2 basis containing an
arithmetic progression of length \(>2r\) satisfies the finite-test-set
hypothesis in Lemma 8.6g with \(T_0=P\). Large-excess fixed-rank barriers
cannot persist in such a basis.

## Warning 8.6i: Certificate density is not a finite quotient fact

Lemma 8.6h does not follow from residue-level order-2 coverage alone. For
every \(r\ge2\), let
\[
G=\mathbb Z/(2r+1)\mathbb Z,\qquad
A_0=\{1,2,\ldots,r+1\}\subset G.
\]
Then
\[
2A_0=G,
\]
since the sums cover the residues \(2,3,\ldots,2r+2\), which are all
residues modulo \(2r+1\). But \(A_0\) can be partitioned into \(r\)
certificate-free classes:
\[
C_0=\{1,r+1\},\qquad C_j=\{j+1\}\quad(1\le j\le r-1).
\]
Singleton classes are trivial. In \(C_0\), the only possible nontrivial
certificate values are
\[
(r+1)+(r+1)-1\equiv0,\qquad 1+1-(r+1)\equiv r+2
\pmod {2r+1},
\]
and neither residue lies in \(A_0\).

Thus every finite \(T\subset A_0\) has a certificate-free subset of size at
least \(|T|/r\), by taking the largest color-class intersection. This is
only a finite residue obstruction: a naive periodic integer lift introduces
many representatives of the same residue, and those representatives can
create integer certificates. It shows that the certificate-free alternative
in Lemma 8.6g cannot be eliminated by a purely quotient-level
\(2A=G\) argument.

## Warning 8.6j: Certificate-free colorings are only Sidon-sparse

The certificate-density principle needed in Lemma 8.6g cannot be obtained
from a simple density contradiction. If \(C\subset A\) is certificate-free,
then \(C\) is a Sidon set. Indeed, suppose
\[
a+b=c+d,\qquad a,b,c,d\in C,
\]
is a nontrivial equality with \(a\ne c,d\). Then
\[
c+d-a=b\in A,
\]
so \(e=a\), \(y_1=c\), \(y_2=d\) form a forbidden certificate in \(C\).
Thus all nontrivial two-sum collisions inside \(C\) are impossible.

Consequently, if
\[
A=C_1\cup\cdots\cup C_r
\]
is a coloring into certificate-free classes, then
\[
|A\cap[1,X]|=O_r(\sqrt X).
\]
This rules out certificate-free colorings for bases with
\[
|A\cap[1,X]|/\sqrt X\to\infty,
\]
but it does not contradict the lower bound for an order-2 basis, which is
only \(|A\cap[1,X]|\gg\sqrt X\). Thus a proof that every order-2 basis has
a finite test set with small certificate-free independence would need
structure beyond Sidon counting, Schur's theorem, van der Waerden's theorem,
or finite residue coverage.

Finite windows show the same limitation. For example
\[
A_0=\{1,2,7,8,10,11\}
\]
has
\[
[8,22]\subseteq2A_0
\]
and admits the certificate-free 2-coloring
\[
\{1,7,10\}\cup\{2,8,11\}.
\]
This is only a finite-window model, but it shows that certificate-free
colorability is not immediately incompatible with local two-sum interval
coverage.

## Lemma 8.6j': Certificate-free colors separate sum types

Let \(C\subset A\) be certificate-free relative to \(A\). Then
\[
(C+C)\cap(C+(A\setminus C))=\varnothing. \tag{1}
\]
Consequently, if
\[
A=C_1\cup\cdots\cup C_r
\]
is a finite coloring into certificate-free classes, then for every \(i\),
\[
(C_i+C_i)\cap(C_i+(A\setminus C_i))=\varnothing. \tag{2}
\]
In the two-color case \(A=C\cup D\), the mixed sumset is disjoint from both
same-color sumsets:
\[
(C+D)\cap(C+C)=\varnothing,\qquad
(C+D)\cap(D+D)=\varnothing.
\]

Proof. Suppose
\[
c_1+c_2=c+a
\]
with \(c,c_1,c_2\in C\) and \(a\in A\setminus C\). If \(c_1=c\), then
\[
a=c_2\in C,
\]
contradiction; similarly \(c_2\ne c\). Hence
\[
a=c_1+c_2-c\in A
\]
is a forbidden certificate for the three elements \(c,c_1,c_2\in C\). This
proves (1), and (2) follows by applying (1) to each color class. For two
colors, (2) for \(C\) gives
\[
(C+C)\cap(C+D)=\varnothing,
\]
and (2) for \(D\) gives
\[
(D+D)\cap(C+D)=\varnothing.
\]
\(\square\)

Thus a two-color certificate-free order-2 basis would have to be a very
rigid separation between mixed sums and same-color sums. This is compatible
with the critical \(A(X)\asymp\sqrt X\) counting scale, so it is not by
itself a contradiction, but it is stronger than the Sidon bound and rules
out many naive cross-sum constructions.

## Warning 8.6j-2: Same-color supports need not be disjoint

Lemma 8.6j' says that mixed sums are disjoint from both same-color
sumsets. It does not imply that the two same-color sumsets are disjoint
from each other.

For example, let
\[
C=\{1,6\},\qquad D=\{2,5\},\qquad A=C\cup D.
\]
Both \(C\) and \(D\) are certificate-free relative to \(A\): the only
nontrivial certificate candidates in \(C\) are
\[
6+6-1=11,\qquad 1+1-6=-4,
\]
and the candidates in \(D\) are
\[
5+5-2=8,\qquad 2+2-5=-1,
\]
none of which belongs to \(A\). But
\[
1+6=2+5.
\]
Thus
\[
(C+C)\cap(D+D)\ne\varnothing.
\]

Therefore the correct support separation for two certificate-free colors is
only
\[
(C+D)\cap(C+C)=\varnothing,\qquad (C+D)\cap(D+D)=\varnothing.
\]
The same-color supports may overlap. In a certificate-free order-2 basis,
the mixed support is separated from the same-color support, but the
same-color part can be covered redundantly by both colors. The
representation-spike criterion still applies because each color is Sidon:
same-color sums contribute only \(O(1)\) representations per color, so any
large total multiplicity must come from mixed sums.

## Lemma 8.6j-4: Mixed spikes are reflected difference packets

Let
\[
A=C\cup D.
\]
For \(m\in C+D\), put
\[
P_m=\{c\in C:m-c\in D\}.
\]
Then the mixed representation multiplicity of \(m\) is \(|P_m|\), and
\[
m+(P_m-P_m)\subseteq C+D. \tag{1}
\]
If \(C\) is certificate-free relative to \(A\), then \(P_m\) is a Sidon
set.

Proof. Each mixed representation of \(m\) is uniquely determined by its
\(C\)-summand \(c\in P_m\), with \(D\)-summand \(m-c\). This proves the
multiplicity assertion. If \(c,c'\in P_m\), then
\[
m+c-c'=c+(m-c')\in C+D,
\]
which proves (1). Finally \(P_m\subset C\), and certificate-free subsets
are Sidon by Warning 8.6j. \(\square\)

Thus the mixed spikes required by Corollary 8.6j-3 are not arbitrary
high-multiplicity events. They are large Sidon packets whose difference
translates sit inside the mixed support. This matches the almost-cross-color
recurrence in Lemma 8.6g''': large reflected packets from one color into
the other automatically generate large mixed difference packets.

## Lemma 8.6j-5: Mixed support is not cofinite

Let
\[
A=C\cup D
\]
be a two-coloring into certificate-free classes relative to \(A\). If
\[
C
\]
is infinite, then
\[
C+D
\]
is not cofinite. The same holds with \(C\) and \(D\) interchanged.

Proof. Since \(C\) is infinite, the same-color sumset
\[
C+C
\]
contains arbitrarily large integers. By Lemma 8.6j',
\[
(C+C)\cap(C+D)=\varnothing.
\]
Thus \(C+D\) misses arbitrarily large integers, and hence is not cofinite.
\(\square\)

Therefore a two-color certificate-free order-2 basis cannot be covered
eventually by mixed sums alone. Since \(2A\) is cofinite, the infinitely
many holes in \(C+D\) must be supplied by same-color sums. The remaining
pair obstruction is thus a genuine interleaving problem: same-color Sidon
supports cover infinitely many tail points, while mixed reflected Sidon
difference packets supply representation spikes on another unbounded set of
scales.

## Corollary 8.6j-3: Certificate-free counterexamples need mixed spikes

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), and
suppose
\[
A=C_1\cup\cdots\cup C_r
\]
is a finite coloring into certificate-free classes. For \(i<j\), write
\[
R_{ij}(X)=\max_{n\le X}|\{(c_i,c_j)\in C_i\times C_j:\ c_i+c_j=n\}|.
\]
If
\[
\max_{i<j} R_{ij}(X)=o(A(X)),
\]
then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\). In particular, a remaining \(k=2\)
counterexample with a finite certificate-free coloring must have mixed-color
two-sum representation spikes comparable to \(A(X)\).

Proof. By Warning 8.6j, each \(C_i\) is Sidon, so every same-color equation
\[
c+c'=n,\qquad c,c'\in C_i,
\]
has at most one unordered representation. Therefore the full two-sum
representation count of \(A\) below \(X\) is bounded by
\[
r+\sum_{i<j}R_{ij}(X).
\]
Under the displayed hypothesis this is \(o(A(X))\). Corollary 3.4c gives
the desired infinite deletion. \(\square\)

## Warning 8.6j'': Certificate-density would rule out Sidon bases

The certificate-free obstruction is at least as hard as the classical Sidon
basis obstruction. Suppose \(S\subset\mathbb N\) were a Sidon asymptotic
basis of order \(2\). Put
\[
C=3S+1,\qquad D=3S+2,\qquad A=C\cup D.
\]
Then \(A\) is an asymptotic basis of order \(2\). If \(n\) is sufficiently
large, according to its residue modulo \(3\) write
\[
\frac{n-2}{3},\qquad \frac{n-3}{3},\qquad \frac{n-4}{3}
\]
as a sum of two elements of \(S\), and use respectively \(C+C\), \(C+D\),
or \(D+D\).

Moreover \(C\) and \(D\) are certificate-free relative to \(A\). For
example, if
\[
e=3s_e+1,\qquad y_i=3s_i+1\in C\quad(i=1,2),
\]
with \(y_i\ne e\), and
\[
y_1+y_2-e\in A,
\]
then the residue modulo \(3\) forces \(y_1+y_2-e\in C\), say
\[
y_1+y_2-e=3s_3+1.
\]
Thus
\[
s_1+s_2=s_e+s_3.
\]
The Sidon property gives equality of unordered pairs
\[
\{s_1,s_2\}=\{s_e,s_3\},
\]
contradicting \(s_1,s_2\ne s_e\). The proof for \(D\) is identical.

Therefore a theorem that every order-2 basis has finite test sets with
\[
\Gamma_A(T)=|T|/\alpha_A(T)
\]
arbitrarily large would, in particular, rule out Sidon asymptotic bases of
order \(2\). The certificate-density route should therefore not be treated
as a routine Ramsey consequence of order-2 basishood; it reaches the
critical Sidon-basis frontier.

This does not make the displayed \(A\) a counterexample. Since \(S\) is
Sidon, the two-term representation multiplicity of \(A\) is bounded:
each residue class modulo \(3\) fixes the summand type \(C+C\), \(C+D\), or
\(D+D\), and then the quotient equation has at most one unordered
representation in \(S+S\). Thus Corollary 3.4b gives an infinite deletion
from \(A\) whose complement is an order-3 basis. The point is only that the
certificate-density subroute is stronger than what the deletion problem
itself needs in this critical model.

One can also see the exact extra robustness that ordinary minimality of
\(S\) would not supply. Let \(T\subset S\), put \(X=S\setminus T\), and
delete only
\[
3T+1
\]
from \(A\), leaving
\[
A_T=(3X+1)\cup(3S+2).
\]
Then \(A_T\) is an order-3 basis if and only if
\[
2X+S
\]
is cofinite. The residues modulo \(3\) force this condition exactly:
large \(0\)-residue integers are handled by three terms from \(3S+2\),
large \(2\)-residue integers by one term from \(3X+1\) and two from
\(3S+2\) whenever \(X\ne\varnothing\), while large \(1\)-residue integers
must be represented as
\[
(3x_1+1)+(3x_2+1)+(3s+2),
\]
equivalent to the cofiniteness of \(2X+S\). Conversely, if \(2X+S\) is
cofinite, then \(X\ne\varnothing\); fixing one \(x_0\in X\), the
cofiniteness of \(2S\) handles the \(2\)-residue class through
\[
(3x_0+1)+(3s_1+2)+(3s_2+2),
\]
and the cofiniteness of \(3S\) handles the \(0\)-residue class. Thus a
Sidon-copy counterexample would require
\[
2(S\setminus T)+S
\]
to fail cofiniteness for every infinite deletion \(T\subset S\), much
stronger than ordinary strong minimality, which only controls
\[
2(S\setminus T).
\]
Equivalently, the unique two-sum representations in a Sidon basis would
have to form shifted vertex-cover barriers for the graphs
\[
\{\rho(u-s):s\in S,\ u-s\in2S\},
\]
where \(\rho(m)\) denotes the unique two-term representation of \(m\) from
\(S\), when it exists.

## Lemma 8.6j-6: Bounded-multiplicity quotient bases satisfy the shifted deletion

Let \(S\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Suppose its unordered two-term representation function
is bounded:
\[
r_{2,S}(m)\le R\qquad(m\in\mathbb N).
\]
Then there is an infinite
\[
T\subset S
\]
such that
\[
2(S\setminus T)+S
\]
is cofinite.

Proof. For each large \(n\), form a graph \(G_n\) on the vertex set
\[
S\cap[1,n].
\]
For every
\[
s\in S\cap[1,n-N_0],
\]
choose one unordered representation
\[
n-s=a_s+b_s,\qquad a_s,b_s\in S,
\]
and add the support edge
\[
E_s=\{a_s,b_s\}
\]
to \(G_n\). Distinct \(s\)'s give distinct support edges, since the same
support would have the same sum \(a_s+b_s=n-s\). Therefore
\[
|E(G_n)|=|S\cap[1,n-N_0]|\to\infty. \tag{1}
\]

The maximum degree of \(G_n\) is bounded in terms of \(R\). Fix a vertex
\[
x\in S.
\]
If \(x\in E_s\), then for some \(y\in S\),
\[
x+y+s=n,
\]
or
\[
y+s=n-x. \tag{2}
\]
There are at most \(R\) unordered pairs \(\{y,s\}\subset S\) satisfying
(2), and each such unordered pair can produce at most two choices of the
third summand \(s\). Hence
\[
\Delta(G_n)\le2R. \tag{3}
\]
By the greedy matching bound, \(G_n\) has a matching of size at least
\[
\frac{|E(G_n)|}{4R}.
\]
Thus, for every \(q\), all sufficiently large \(n\) have \(q\) pairwise
disjoint support edges.

Choose
\[
t_1<t_2<\cdots,\qquad t_i\in S,
\]
recursively so fast that \(t_j\) is larger than a threshold after which
every \(G_n\) has a matching of size at least \(j+2\). Put
\[
T=\{t_j:j\ge1\}.
\]
Let \(n\) be large, and choose \(j\) with
\[
t_j\le n<t_{j+1}.
\]
Then \(G_n\) has a matching of \(j+2\) disjoint support edges. Future
deleted elements \(t_{j+1},t_{j+2},\ldots\) are larger than \(n\), so they
cannot lie in any support edge for a representation of \(n\). The first
\(j\) deleted elements meet at most \(j\) of the disjoint support edges.
Therefore at least one matched edge \(E_s=\{a_s,b_s\}\) avoids all of
\(T\). For this edge,
\[
n=a_s+b_s+s,\qquad a_s,b_s\in S\setminus T,\quad s\in S.
\]
Thus all sufficiently large \(n\) lie in \(2(S\setminus T)+S\). \(\square\)

Consequently, the Sidon-copy construction in Warning 8.6j'' cannot be a
counterexample when the quotient Sidon basis has bounded two-sum
multiplicity. In particular, an actual certificate-free counterexample
would need the same large shifted representation spikes already forced by
Corollary 3.4d; certificate-free coloring alone is not enough.

## Lemma 8.6j-7: One-color shifted obstructions force mixed spikes

Let \(A\subseteq\mathbb N\), and let \(C\subset A\) be infinite and
certificate-free relative to \(A\). For each \(n\), define a graph
\[
G_n^C
\]
on the vertex set \(C\cap[1,n]\) as follows: put an edge with support
\[
\{c_1,c_2\}
\]
whenever
\[
c_1,c_2\in C,\qquad n-c_1-c_2\in A.
\]
Loops are allowed and use one vertex. If, for every \(q\), all sufficiently
large \(n\) have a matching of size at least \(q\) in \(G_n^C\), then there
is an infinite
\[
T\subset C
\]
such that
\[
2(C\setminus T)+A
\]
is cofinite.

Consequently, if every infinite \(T\subset C\) makes
\[
2(C\setminus T)+A
\]
non-cofinite, then there is a fixed \(q\) and arbitrarily large \(n\) for
which \(G_n^C\) has matching number \(<q\). For those \(n\), a set of at
most \(2(q-1)\) vertices of \(C\) meets every edge. If in addition
\[
|E(G_n^C)|\to\infty
\]
along such \(n\), then there are vertices \(c_n\in C\) for which the mixed
degree
\[
\left|\{c'\in C:\ n-c_n-c'\in A\setminus C\}\right|
\]
tends to infinity.

Proof. The first assertion is the same sparse-deletion matching argument as
Lemma 8.6j-6. Choose
\[
t_1<t_2<\cdots,\qquad t_i\in C,
\]
so fast that \(t_j\) is larger than a threshold after which every \(G_n^C\)
has a matching of size at least \(j+2\). Put \(T=\{t_j:j\ge1\}\). For
large \(n\), choose \(j\) with
\[
t_j\le n<t_{j+1}.
\]
The graph \(G_n^C\) has \(j+2\) disjoint edges. Future deleted elements are
larger than \(n\), so they cannot occur in an edge support representing
\(n\). The first \(j\) deleted elements meet at most \(j\) disjoint edges.
Hence one edge \(\{c_1,c_2\}\) avoids \(T\), and by definition of
\(G_n^C\),
\[
n=c_1+c_2+a,\qquad c_1,c_2\in C\setminus T,\quad a\in A.
\]
This proves cofiniteness of \(2(C\setminus T)+A\).

The contrapositive gives the bounded-matching conclusion. Taking a maximal
matching, the union of its edge supports is a transversal of size at most
\(2(q-1)\).

It remains to isolate the mixed spike. Since \(C\) is certificate-free,
Warning 8.6j says that \(C\) is Sidon. Fix a vertex \(c\in C\). The edges
incident to \(c\) whose residual summand also lies in \(C\) have the form
\[
n-c-c'=d,\qquad c',d\in C,
\]
or
\[
c'+d=n-c.
\]
Sidonicity gives at most one unordered pair \(\{c',d\}\), and hence at most
two such edge supports incident to \(c\). Therefore all but at most two
edges incident to \(c\) have residual summand in \(A\setminus C\).

For the bounded-matching values of \(n\), let \(P_n\subset C\) be a
transversal with \(|P_n|\le2(q-1)\). Since every edge is incident to
\(P_n\), some \(c_n\in P_n\) has degree at least
\[
|E(G_n^C)|/(2q).
\]
Subtracting the at most two same-color-residual edges gives mixed degree at
least
\[
|E(G_n^C)|/(2q)-2,
\]
which tends to infinity along any sequence with \(|E(G_n^C)|\to\infty\).
\(\square\)

This is the one-color version of the mixed-spike obstruction in Corollary
8.6j-3. A certificate-free color can fail the shifted deletion
\[
2(C\setminus T)+A
\]
only if its own \(C+C+A\) representation graphs have bounded moving
transversals; whenever those graphs have many edges, the bounded
transversals force large \(C+(A\setminus C)\) degrees through a few moving
vertices.

## Lemma 8.6j-7a: Cross-residual color matchings give a deletion

Let \(A=C\cup D\cup E\), where the union is disjoint and \(E\) is finite.
For each \(n\), define a graph \(H_n^C\) on the vertex set
\(C\cap[1,n]\) by putting an edge with support
\[
\{c_1,c_2\}
\]
whenever
\[
c_1,c_2\in C,\qquad n-c_1-c_2\in D\cup E.
\]
Loops are allowed and use one vertex. If, for every \(q\), all sufficiently
large \(n\) have a matching of size at least \(q\) in \(H_n^C\), then
there is an infinite
\[
T\subset C
\]
such that \(A\setminus T\) is an order-3 basis.

Proof. Choose
\[
t_1<t_2<\cdots,\qquad t_i\in C,
\]
recursively so fast that \(t_j\) is larger than a threshold after which
every \(H_n^C\) has a matching of size at least \(j+2\). Put
\[
T=\{t_j:j\ge1\}.
\]
Let \(n\) be large and choose \(j\) with
\[
t_j\le n<t_{j+1}.
\]
Then \(H_n^C\) has \(j+2\) disjoint edges. Future deleted elements are
larger than \(n\), hence cannot occur in any edge support for a
representation of \(n\). The first \(j\) deleted elements meet at most
\(j\) of the disjoint supports. Therefore one edge \(\{c_1,c_2\}\) avoids
\(T\), and by definition
\[
n=c_1+c_2+a,\qquad c_1,c_2\in C\setminus T,\quad a\in D\cup E.
\]
Since \(D\cup E\subset A\setminus T\), this is a three-term retained
representation of \(n\). \(\square\)

Thus a counterexample with a cofinite two-color certificate-free tail
\(C\cup D\) must have bounded moving transversals not only in the
one-color graphs from Lemma 8.6j-7, but already in the cross-residual
graphs \(C+C+D\) and \(D+D+C\). The almost-cross-color recurrence from
Lemma 8.6g''' naturally produces star-shaped families in these graphs; the
remaining difficulty is to force disjoint supports rather than stars.

## Lemma 8.6j-7b: Cross-residual stars are low-count stars

Let
\[
A=C\cup D\cup E
\]
be a disjoint union, where \(E\) is finite and \(C,D\) are
certificate-free relative to \(A\). Then there is a constant \(Q_E\) such
that for every same-color pair
\[
x,y\in C\quad\text{or}\quad x,y\in D
\]
one has
\[
r_{2,A}(x+y)\le Q_E. \tag{1}
\]
Consequently, if for some \(n\) and \(p\in C\) there are many
\[
c\in C
\]
with
\[
n-p-c\in D\cup E,
\]
then \(p\) is a low-count star gate in the sense of Corollary 3.4n:
\[
c\mapsto c+p
\]
has uniformly bounded two-sum representation count on that reflected
packet.

Proof. Consider \(x,y\in C\); the proof for \(D\) is identical. Since
\(C\) is certificate-free, it is Sidon by Warning 8.6j, so there is at most
one unordered representation of \(x+y\) from \(C+C\). Since \(D\) is Sidon,
there is at most one unordered representation from \(D+D\). By Lemma
8.6j',
\[
(C+C)\cap(C+D)=\varnothing,
\]
so there is no mixed \(C+D\) representation of \(x+y\). The only remaining
representations use at least one element of the finite set \(E\), and there
are \(O_E(1)\) of those. This proves (1).

If \(n-p-c\in D\cup E\), then with
\[
w=n,\qquad d=p,\qquad a=c
\]
the reflected row has
\[
w-d-a\in A
\]
and (1) gives \(r_{2,A}(a+d)\le Q_E\). \(\square\)

Thus the bipartite Sidon obstruction has not escaped the earlier
low-count-star normal form. Its bounded-transversal branch is precisely a
moving same-color star whose rows have bounded two-sum multiplicity. The
unresolved point is still global: prove that such stars cannot remain
fresh outside every finite protected core, or build a critical-density
construction where they do.

## Warning 8.6j-7c: Cross-color recurrence naturally gives stars

The almost-cross-color recurrence in Lemma 8.6g''' does not by itself
trigger the matching criterion in Lemma 8.6j-7a. Let
\[
A=C\cup D
\]
with \(C\) certificate-free, let \(U\subset C\) be finite, and suppose a
large center \(m\) satisfies
\[
m-U\subset D.
\]
Fix an anchor \(p\in C\) and put
\[
n=m+p.
\]
Then for each \(u\in U\) the cross-residual graph \(H_n^C\) contains the
edge
\[
\{p,u\},
\]
because
\[
n-p-u=m-u\in D.
\]
Thus recurrence supplies arbitrarily large degrees at the moving gate
\(p\), but these edges all meet \(p\) and need not contain a large
matching.

Moreover, certificate-freeness reinforces this star shape for the same
residual rows. If \(x,y\in C\setminus\{p\}\) and
\[
n-x-y=m-u,
\]
then
\[
x+y-p=u\in A,
\]
so \(p,x,y\) would form a forbidden certificate in \(C\). Equivalently, the
same reflected residual \(m-u\) cannot also be supplied by a non-star
same-color pair avoiding \(p\).

This explains why the current reduction stops at the fresh low-count star
branch rather than at the matching criterion. Cofinite order-2 coverage and
separate recurrence produce many cross-residual edges, but they do not
force those edges to be disjoint.

## Lemma 8.6j-7d: Two Sidon colors forbid large shifted-reflected packets

Let
\[
A=C_0\cup C_1\cup E
\]
be a disjoint union, where \(E\) is finite and each \(C_i\) is
certificate-free relative to \(A\). Let \(h\ne0\) and \(t\) be integers.
If
\[
S\subset A\setminus E,\qquad S+h\subset A\setminus E,\qquad t-S\subset A\setminus E,
\]
then
\[
|S|\le 10. \tag{1}
\]

Proof. By Warning 8.6j, each \(C_i\) is Sidon. Color every element of
\(A\setminus E\) by its membership in \(C_0\) or \(C_1\).

First consider the translation \(s\mapsto s+h\). For a fixed color
\(C_i\), there is at most one \(s\in S\cap C_i\) with
\[
s+h\in C_i.
\]
Indeed, two distinct such elements \(s,s'\) would give two distinct
same-color representations
\[
s+(s'+h)=s'+(s+h),
\]
contradicting the Sidon property of \(C_i\). Thus at most two elements of
\(S\) keep their color under translation by \(h\).

Next consider the reflection \(s\mapsto t-s\). For a fixed color \(C_i\),
there are at most two \(s\in S\cap C_i\) with
\[
t-s\in C_i,
\]
because all unordered pairs \(\{s,t-s\}\) have the same same-color sum
\(t\), and a Sidon color admits at most one such pair. Hence at most four
elements of \(S\) keep their color under reflection.

Remove these at most six exceptional elements. For every remaining
\(s\), both maps flip color, so
\[
s+h,\quad t-s
\]
lie in the same color, the color opposite to that of \(s\). For a fixed
target color \(C_i\), the unordered pairs
\[
\{s+h,t-s\}
\]
all have sum \(t+h\). Sidonicity again allows at most one such unordered
pair in \(C_i\), and hence at most two values of \(s\) for that color.
The two target colors contribute at most four non-exceptional elements.
Together with the six exceptional elements, this proves (1). \(\square\)

Consequently, in the cofinite two-color certificate-free tail supplied by
Corollary 13.1l.3, the shifted-overlap branch of Corollary 3.4t cannot
carry packets of size tending to infinity once the finite exceptional set
has been protected. Any surviving low-count-star obstruction in that
two-color reduction must therefore fall in the unique-gate branch, not in
the moving shifted-overlap branch.

## Lemma 8.6j-7e: Same-color exception rows are sparse

Let
\[
A=C_0\cup C_1\cup E
\]
be a disjoint union, where \(E\) is finite and each \(C_i\) is
certificate-free relative to \(A\). Let
\[
F\subset C_0\cup C_1
\]
be finite, put \(R=A\setminus F\), and fix \(w\). For every
\[
c\in F
\]
and every color \(i\in\{0,1\}\), the set
\[
\{a\in F\cap C_i:\ w-a-c\in R\cap C_i\}
\]
has size at most \(1\). Consequently, the number of incidences
\[
(a,c,t)\in F\times F\times (R\setminus E)
\]
with
\[
t=w-a-c
\]
and \(a,t\) in the same color is at most \(2|F|\).

Proof. Fix \(c\in F\) and \(i\in\{0,1\}\). Suppose distinct
\[
a,b\in F\cap C_i
\]
satisfy
\[
t_a=w-a-c\in R\cap C_i,\qquad t_b=w-b-c\in R\cap C_i.
\]
Since \(t_b\in R\), it is not equal to \(a\in F\). Therefore the three
same-color elements
\[
a,\quad b,\quad t_b
\]
form a forbidden certificate: with \(e=a\),
\[
b+t_b-a=b+(w-b-c)-a=w-a-c=t_a\in A.
\]
This contradicts certificate-freeness of \(C_i\). Hence there is at most
one such \(a\) for each fixed pair \((c,i)\). Summing over
\[
c\in F,\qquad i\in\{0,1\}
\]
gives the incidence bound. \(\square\)

This is the two-color refinement of the \(F+F\) exception window in
Corollary 8.4c.1. It does not improve the scalar bound \(|F+F|\) enough to
close the problem: the surviving exception rows may still be star-like and
color-flipping. It does rule out dense same-color rectangles inside the
exception window, which is exactly the pattern that would otherwise mimic
an absorptive finite test set.

## Warning 8.6j-8: Cross reflections give moving, not fixed, certificates

The mixed-spike structure has a tempting but invalid shortcut to Corollary
2.3c. Suppose \(A=C\cup D\), and a large center \(m\) reflects two elements
\[
u_0,u_1\in C
\]
across the coloring:
\[
m-u_0,\ m-u_1\in D.
\]
Then the three elements
\[
e=u_0,\qquad y_1=u_1,\qquad y_2=m-u_1
\]
do form a certificate triple, because
\[
y_1+y_2-e=m-u_0\in A.
\]
Moreover the same center \(m\) reflects the triple:
\[
m-e=m-u_0\in A,\qquad m-y_1=m-u_1\in A,\qquad m-y_2=u_1\in A.
\]

This does not trigger the fixed-certificate deletion theorem. In Corollary
2.3c, using the base element \(e\) and center \(m\) deletes
\[
b=m-e=m-u_0.
\]
But here the required certificate value
\[
x=y_1+y_2-e
\]
is exactly the same element \(m-u_0=b\). The proof of Corollary 2.3c needs
\(x\) to remain protected, while the natural deletion would remove it. In
addition, the element \(y_2=m-u_1\) varies with the center, so the
certificate tuple is not fixed on an unbounded sequence.

Thus large cross-color reflected packets are not by themselves enough.
They must either contain a fixed certificate tuple whose certificate value
is not the deleted mirror, or provide a different repair scheme from the
balanced fixed-certificate recursion.

## Warning 8.6j-9: Pair repairs from reflected packets require a fixed certificate

The obstruction in Warning 8.6j-8 is not just an artefact of choosing the
wrong deleted mirror. Suppose one tries the following more flexible scheme.
Fix a retained base point \(t\in A\), choose large centers \(m_i\), and
delete
\[
b_i=m_i-t.
\]
Assume that for some fixed finite set \(Y\subset A\), the centers reflect
\[
m_i-Y\subset A
\]
and all these mirrors are retained. The one-deleted repair
\[
b_i+t=m_i
\]
can be supplied by any reflected pair
\[
m_i=y+(m_i-y),\qquad y\in Y.
\]
But the two-deleted repair has target
\[
b_i+b_j+t=m_i+m_j-t. \tag{1}
\]
Any balanced repair of (1) using one mirror from each center and one fixed
retained element has the form
\[
(m_i-y_1)+(m_j-y_2)+z.
\]
It equals (1) exactly when
\[
z=y_1+y_2-t. \tag{2}
\]
Thus this whole class of repairs is available precisely when
\[
t,y_1,y_2
\]
form a fixed certificate triple with value \(z\in A\).

Consequently, if \(Y\cup\{t\}\) is certificate-free relative to \(A\), then
reflected packets from \(Y\) cannot by themselves run the usual order-3
deletion recursion. One must either find a reflected packet that contains a
genuine fixed certificate, or use a repair identity that is not of this
balanced two-mirror form.

Lemma 8.2a' gives one such different identity. If a reflected packet at
center \(m_j\) supplies
\[
e_j+b_j=m_j\in2C,\qquad b_j=m_j-e_j,
\]
then the moving-anchor bridge route additionally needs a fixed retained
padder \(t\) and retained elements \(q_j\) with
\[
t+b_j=e_j+q_j,
\]
equivalently
\[
q_j=t+m_j-2e_j\in C,
\]
as well as the old-anchor rows
\[
e_j+b_i\in2C\qquad(i<j).
\]
Thus cross-reflected packets are useful only when they come with these
bridge and old-row conditions, or when they contain a genuine fixed
certificate.

## Corollary 8.6k: Dense order-2 bases cannot support fixed-rank large-excess barriers

Let \(A\subseteq\mathbb N\) be an order-2 asymptotic basis. Suppose
\[
\frac{|A\cap[1,X]|}{\sqrt X}\to\infty. \tag{1}
\]
Then, for every fixed \(r\ge2\), the large-excess fixed-rank obstruction in
Lemma 8.6g cannot persist. More precisely, for all sufficiently large
\[
X
\]
the finite test set
\[
T_X=A\cap[1,X]
\]
has the property that every subset
\[
U\subset T_X,\qquad |U|\ge |T_X|/r,
\]
contains a certificate triple
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A.
\]
Consequently, if a remaining \(k=2\) counterexample has fixed-rank
large-excess barriers of rank \(r\), then (1) fails.

Proof. If \(U\subset A\cap[1,X]\) is certificate-free, then Warning 8.6j
says \(U\) is Sidon. The number of unordered two-sums from \(U\) is
\[
\binom{|U|+1}{2},
\]
and they all lie in \([2,2X]\), so
\[
|U|=O(\sqrt X). \tag{2}
\]
By (1), for fixed \(r\) and all large \(X\),
\[
|A\cap[1,X]|/r
\]
exceeds the implicit Sidon bound in (2). Hence no subset of \(T_X\) of size
at least \(|T_X|/r\) can be certificate-free. Lemma 8.6g then rules out
fixed-rank large-excess barriers of rank \(r\). \(\square\)

This is a conditional density reduction, not a proof of the problem. A thin
order-2 basis can have \(|A\cap[1,X]|=O(\sqrt X)\), exactly the scale at
which Sidon-sized certificate-free sets are not contradictory. Thus the
unresolved counterexample, if it exists, must either be near the critical
order-2 density scale or use genuinely unbounded-rank barriers such as the
Schreier target in Proposition 13.1b-Schreier.

Combining this with Lemma 8.6g gives a clean partial theorem. Let \(A\) be
an order-2 basis satisfying (1). If, in the remaining collective case, there
is a fixed rank \(r\) such that for every finite \(T\subset A\) and every
\(L\) there are
\[
F\subset A\setminus T,\qquad |F|=r,
\]
and a witness \(w\) with
\[
w-\max F>L,\qquad w-\max T\ge N_0,\qquad
w\notin3(A\setminus F),
\]
then the desired infinite deletion exists. Indeed, (1) and the Sidon bound
provide the finite test set required by Lemma 8.6g, and Lemma 8.6g gives a
recurrent certificate triple; Corollary 2.3c then gives an infinite
deletion preserving order \(3\).

This does not by itself settle bounded-width barriers. Lemma 8.5a can
Ramsey-thin a bounded-width obstruction to one fixed rank on an infinite
tail, but Lemma 8.5b's bounded-top-excess contradiction requires a cofinite
tail, not merely a sparse infinite one. Thus the remaining dense case still
allows a sparse fixed-rank tail with bounded top excess, unless an
additional arithmetic argument upgrades it to bounded second-excess
(handled by Lemma 8.6a) or to the large-excess hypothesis above.

## Lemma 8.6g': Pair barriers force certificates unless endpoint lists split certificate-free

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
threshold \(N_0\). Suppose there is a finite set \(T_0\subset A\) with the
following property: for every \(M\) there are \(w\) and distinct
\[
x_w,y_w\in A\setminus T_0
\]
such that
\[
w-\max T_0\ge N_0,\qquad w-x_w>M,\qquad w-y_w>M,
\qquad w\notin3(A\setminus\{x_w,y_w\}), \tag{1}
\]
and the endpoint lists
\[
L_w(t)=\{z\in\{x_w,y_w\}:w-t-z\in A\}\qquad(t\in T_0)
\]
admit no choice function
\[
\chi(t)\in L_w(t)
\]
whose two fibers
\[
\chi^{-1}(x_w),\qquad \chi^{-1}(y_w)
\]
are both certificate-free relative to \(A\). Then there is an infinite
\[
B\subset A
\]
such that \(A\setminus B\) is an asymptotic basis of order \(3\).

Proof. For each \(t\in T_0\), Lemma 10.1 applied to (1) implies that every
two-term representation of \(w-t\) meets \(\{x_w,y_w\}\). Since
\[
w-t\ge N_0,
\]
the target \(w-t\) has a two-term representation from \(A\), so
\(L_w(t)\ne\varnothing\). Choose any
\[
\chi(t)\in L_w(t).
\]
By hypothesis, one fiber contains a certificate triple
\[
e,y_1,y_2,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A.
\]
If this fiber is \(\chi^{-1}(x_w)\), then
\[
w-x_w-\{e,y_1,y_2\}\subset A.
\]
If it is \(\chi^{-1}(y_w)\), then
\[
w-y_w-\{e,y_1,y_2\}\subset A.
\]
Thus some certificate triple in the fixed finite set \(T_0\) is reflected
into \(A\) with arbitrarily large centers, because both endpoint centers in
(1) exceed the arbitrary parameter \(M\). Passing to an unbounded subsequence,
the same triple recurs. Corollary 2.3c gives the desired deletion. \(\square\)

Therefore complete pair barriers can evade the fixed-triple theorem only if,
on every finite test set, the shifted endpoint lists admit a
certificate-free two-coloring. This is stronger and more coherent than the
mere existence of a certificate-free half-subset; it is the list-coloring
form of the remaining pair-barrier obstruction.

## Lemma 8.6g'': Persistent list-colored pair barriers give two recurrent certificate-free colors

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
that for every finite
\[
T\subset A
\]
and every \(M\), there are \(w\) and distinct
\[
x_w,y_w\in A\setminus T
\]
such that
\[
w-x_w>M,\qquad w-y_w>M,\qquad w\notin3(A\setminus\{x_w,y_w\}), \tag{1}
\]
and the endpoint lists
\[
L_w(t)=\{z\in\{x_w,y_w\}:w-t-z\in A\}\qquad(t\in T)
\]
admit a choice function whose two fibers are certificate-free relative to
\(A\). Then \(A\) has a two-coloring
\[
A=C_0\cup C_1
\]
such that:

1. each \(C_i\) is certificate-free relative to \(A\);
2. each \(C_i\) is separately reflection-recurrent in \(A\): for every
   finite \(U\subset C_i\) and every \(L\), there is \(m>L\) with
   \[
   m-U\subset A.
   \]

Proof. Enumerate
\[
A=\{a_1<a_2<\cdots\}
\]
and put \(T_j=\{a_1,\ldots,a_j\}\). For each \(j\), apply the hypothesis
with \(T=T_j\) and \(M=j\). Choose one admissible endpoint choice, and
label the fiber assigned to \(x_j\) by color \(0\), the fiber assigned to
\(y_j\) by color \(1\).

By the diagonal compactness of \(\{0,1\}^{\mathbb N}\), pass to a
subsequence on which the color of every fixed \(a_i\) stabilizes. Let
\[
C_0,C_1
\]
be the resulting color classes.

If some \(C_i\) contained a certificate triple
\[
e,y_1,y_2,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then that finite triple would lie in one stable fiber for all sufficiently
large stages of the subsequence, contradicting that every chosen fiber is
certificate-free. Thus both color classes are certificate-free.

Now fix a finite \(U\subset C_0\) and \(L\). For all sufficiently large
stages \(j\) in the subsequence, the set \(U\) lies in \(T_j\), every
element of \(U\) has stabilized to color \(0\), and \(w_j-x_j>L\). Since
the chosen endpoint for every \(u\in U\) is \(x_j\), the center
\[
m=w_j-x_j
\]
satisfies \(m-U\subset A\). This proves reflection-recurrence for \(C_0\).
The proof for \(C_1\), using the centers \(w_j-y_j\), is identical.
\(\square\)

Consequently, if the large-excess pair-barrier case remains after Lemma
8.6g', then the obstruction is no longer merely finite and local. It must
produce a global partition of \(A\) into two Sidon-like certificate-free
classes, with each class carrying its own independent reflection-recurrence
inside \(A\). Lemmas 8.6g''' and 8.6g'''' show that this global structure
is impossible in the integers.

## Lemma 8.6g''': Recurrent certificate-free colors reflect almost across colors

Let \(A=C\cup D\), and suppose \(C\) is certificate-free relative to \(A\).
Let
\[
U\subset C
\]
be finite, and let \(m>2\max U\). Then
\[
|\{u\in U:m-u\in C\}|\le1. \tag{1}
\]
Consequently, in the two-color obstruction supplied by Lemma 8.6g'', for
each \(i\in\{0,1\}\), every finite
\[
U\subset C_i
\]
and every \(L\) have a center \(m>L\) such that
\[
|\{u\in U:m-u\in C_{1-i}\}|\ge |U|-1. \tag{2}
\]

Proof. A certificate-free subset of \(A\) is Sidon, as in Warning 8.6j.
If two distinct elements \(u,v\in U\) had
\[
m-u,\ m-v\in C,
\]
then
\[
u+(m-u)=v+(m-v). \tag{3}
\]
Since \(m>2\max U\), both \(m-u\) and \(m-v\) are larger than every element
of \(U\). Thus the unordered pairs in (3) are distinct, giving a
nontrivial same-color two-sum collision in \(C\), contrary to the Sidon
property. This proves (1).

For (2), apply the separate reflection-recurrence of \(C_i\) from Lemma
8.6g'' with \(m>\max(L,2\max U)\). Then \(m-U\subset A=C_i\cup C_{1-i}\),
and (1) says at most one mirror lies in \(C_i\). \(\square\)

Thus the compactified pair obstruction is essentially bipartite. In fact,
the integer Sidon condition now gives a contradiction, not merely a
stronger necessary condition.

## Lemma 8.6g'''': Two Sidon colors cannot support recurrence

Let
\[
A=C\cup D\cup E
\]
be a disjoint union, where \(E\) is finite, and suppose both \(C\) and
\(D\) are Sidon. If
\[
|C|\ge3,
\]
then \(C\) is not reflection-recurrent in \(A\). More precisely, for any
three distinct
\[
u_1,u_2,u_3\in C,
\]
there are not arbitrarily large \(m\) such that
\[
m-u_1,\quad m-u_2,\quad m-u_3\in A. \tag{1}
\]

Proof. Suppose such centers \(m\) exist. Take them larger than
\[
2\max\{u_1,u_2,u_3\}+\max(E\cup\{0\}).
\]
For each such \(m\), at most one of the three mirrors
\[
m-u_1,\quad m-u_2,\quad m-u_3
\]
lies in \(C\): two mirrors in \(C\) would give two distinct same-color
representations
\[
u_i+(m-u_i)=u_j+(m-u_j)
\]
with \(m>2\max\{u_1,u_2,u_3\}\), contradicting Sidonicity of \(C\).
None lies in \(E\), so at least two lie in \(D\). Among the
three unordered
pairs
\[
\{u_i,u_j\}\qquad(1\le i<j\le3),
\]
one pair occurs for two distinct centers \(m\ne n\); say
\[
m-u_i,\ m-u_j,\ n-u_i,\ n-u_j\in D.
\]
Then \(D\) has the same-color two-sum collision
\[
(m-u_i)+(n-u_j)=(m-u_j)+(n-u_i). \tag{2}
\]
The unordered pairs in (2) are distinct because \(m\ne n\) and
\(u_i\ne u_j\). This contradicts Sidonicity of \(D\). \(\square\)

Consequently an infinite set \(A\) cannot be partitioned, up to a finite
exceptional set, into two certificate-free color classes that are both
reflection-recurrent in \(A\): at least one class contains three elements,
and certificate-free sets are Sidon. Therefore the persistent list-colorable
pair-barrier hypothesis of Lemma 8.6g'' is impossible.

### Corollary 8.6g''''.1: Cross-reflected packets have size at most two

Let
\[
A=C\cup D\cup E
\]
be a disjoint union, where \(E\) is finite and both \(C\) and \(D\) are
Sidon. Suppose \(D\) is reflection-recurrent in \(A\). If
\[
S\subset C,\qquad t-S\subset D,
\]
then
\[
|S|\le2. \tag{1}
\]

Proof. Put
\[
U=t-S\subset D.
\]
Choose a recurrence center \(m\) for \(U\) so large that
\[
m>t,\qquad m>2\max U,\qquad m-\min U>\max(E\cup\{0\}).
\]
Then
\[
m-U\subset A\setminus E=C\cup D.
\]
Since \(D\) is Sidon, at most one \(u\in U\) can have \(m-u\in D\);
otherwise
\[
u+(m-u)=v+(m-v)
\]
would be a nontrivial same-color collision in \(D\). Hence for all but at
most one \(s\in S\),
\[
m-(t-s)=s+(m-t)\in C.
\]
Let
\[
h=m-t\ne0.
\]
A Sidon set \(C\) contains at most one pair \(s,s+h\) with \(s\in S\):
two distinct such \(s,s'\) would give
\[
s+(s'+h)=s'+(s+h),
\]
a nontrivial same-color collision in \(C\). Thus \(|S|-1\le1\), proving
(1). \(\square\)

This corollary is the packet-level form of Lemma 8.6g'''': finite windows
may contain large cross-reflected Sidon packets, but such a packet cannot
coexist with recurrence of the target color in the integer setting.

### Lemma 8.6g''''.2: Finite Sidon colorings cannot be recurrent

Let
\[
A=E\cup C_1\cup\cdots\cup C_q
\]
be a disjoint union, where \(E\) is finite and each \(C_j\) is Sidon. If
\[
C_i
\]
is reflection-recurrent in \(A\), then
\[
|C_i|\le q. \tag{1}
\]
Consequently, no infinite set \(A\) can be partitioned, up to a finite
exceptional set, into finitely many Sidon color classes that are all
reflection-recurrent in \(A\).

Proof. Suppose \(C_i\) contains \(q+1\) distinct elements; call this set
\[
U.
\]
Take recurrence centers \(m\) for \(U\) arbitrarily large, with
\[
m>2\max U+\max(E\cup\{0\}).
\]
For any such \(m\), at most one mirror \(m-u\) lies in \(C_i\), since two
would give the same-color collision
\[
u+(m-u)=v+(m-v)
\]
inside \(C_i\). None of the mirrors lies in \(E\), so at least \(q\) of the
\(q+1\) mirrors lie in the other \(q-1\) colors. Hence some color
\[
C_j,\qquad j\ne i,
\]
contains mirrors of two distinct elements \(u,v\in U\). There are only
finitely many choices of \((j,\{u,v\})\), so two distinct recurrence
centers \(m\ne n\) have
\[
m-u,\ m-v,\ n-u,\ n-v\in C_j.
\]
Then
\[
(m-u)+(n-v)=(m-v)+(n-u)
\]
is a nontrivial same-color two-sum collision in \(C_j\), contradiction.
Thus \(|C_i|\le q\). If all \(C_i\) are recurrent, every color has at most
\(q\) elements, so \(A\) is finite up to \(E\). \(\square\)

## Warning 8.6g'''a: Bipartite recurrent colors are quotient-compatible

The almost-bipartite conclusion of Lemma 8.6g''' is not a finite quotient
contradiction. In
\[
G=\mathbb Z/6\mathbb Z
\]
put
\[
A_0=\{0,1,2,3\},\qquad C=\{0,2\},\qquad D=\{1,3\}.
\]
Then
\[
2A_0=G.
\]
Both \(C\) and \(D\) are certificate-free relative to \(A_0\). For example,
the only nontrivial certificate candidates in \(C\) are
\[
2+2-0\equiv4,\qquad 0+0-2\equiv4\pmod6,
\]
and \(4\notin A_0\); the check for \(D\) is the same.

Moreover the single center
\[
m=3
\]
reflects the two colors across each other:
\[
3-C=D,\qquad 3-D=C.
\]
Thus finite residue data can exhibit the one-center, two-point shadow of
the bipartite shape from Lemma 8.6g'''. Lemma 8.6g'''' explains why this
does not lift to an infinite integer obstruction: recurrence supplies
arbitrarily many centers for a three-point test set, and two such centers
force an ordinary Sidon collision.

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

The script `EXPERIMENTS/pair_hole_residue_search.py` finds an even smaller
residue shadow of the same mechanism:
\[
R=\{0,1\}\subset\mathbb Z/5\mathbb Z,\qquad x=2,\qquad y=3.
\]
Then
\[
2(R\cup\{x,y\})=\mathbb Z/5\mathbb Z,\qquad 4\notin3R,
\]
and the shifted domination for the hole residue \(4\) is two-centered:
\[
4-R\subset (x+R)\cup(y+R).
\]
This confirms that the residue ingredients for pair holes are cheap. The
hard part is the integer or staged lift: in a thick lift, other
representatives of the exceptional residues repair the hole, while in a
stage construction old exceptional elements must also be dominated.

There is a concrete reason the moving-phase cover model from Warning 8.7c
does not combine with this residue pair-hole mechanism. In the
\(R=\{0,1,4\}\pmod8\) model, \(3R\) misses only residue \(7\). If a
candidate witness has residue \(3\alpha+7\) and a retained old element has
residue outside \(\alpha+R\), then that old element plus two retained
\(R\)-tail elements represents the witness. Hence a genuine pair hole of
this residue type forces every other active old element into the same
allowed translate \(\alpha+R\), while the deleted pair must lie outside it.
For complete pair systems this finite residue separation already fails in
small size: one cannot choose translates of \(\{0,1,4\}\pmod8\) that
separate every pair from all other protected residues.

Equivalently, in an ordered-group phase lift
\[
A_\theta=\{(n,\theta(n)+r):r\in R\},
\]
a genuine hole at a fixed first coordinate would require the phase sums
\[
\theta(a)+\theta(b)+\theta(c)
\]
to be constant modulo \(8\) over all active decompositions
\[
a+b+c=W.
\]
Comparing nearby decompositions such as \((a,b,c)\) and \((a+1,b-1,c)\)
forces \(\theta\) to be affine on the active interval, destroying the
moving-phase freedom used in Warning 8.7c. Thus two-center reflected-cover
models do not by themselves yield additive pair holes; the missing input is
again terminal-gap or shifted vertex-cover control.

## Example 8.7e: Complete minimal pair holes can be certificate-free

The fixed-triple criterion in Corollary 2.3c also cannot be forced from
active minimal pair holes alone. In the finite group
\[
G=\mathbb Z/13\mathbb Z,
\]
put
\[
P=\{0,1,3\},\qquad R=\{7,8,9\},\qquad A_0=P\cup R.
\]
Then
\[
2A_0=G.
\]
The set \(P\) is certificate-free relative to \(A_0\): if
\[
e,y_1,y_2\in P,\qquad y_1,y_2\ne e,
\]
then
\[
y_1+y_2-e\notin A_0.
\]

Nevertheless every pair in \(P\) is an inclusion-minimal three-fold hole:
\[
3\notin3(A_0\setminus\{0,1\}),\qquad
7\notin3(A_0\setminus\{0,3\}),\qquad
6\notin3(A_0\setminus\{1,3\}).
\]
Restoring either endpoint repairs the corresponding hole. For instance
\[
3=0+0+3=1+1+1,\qquad
7=0+0+7=1+3+3,\qquad
6=1+9+9=0+3+3.
\]
Thus the active-multiplicity normal form from Lemma 8.4b is locally
compatible with complete pair barriers that contain no certificate triple.

This is only a finite residue model, not an integer counterexample. Its
role is diagnostic: a proof of Lemma 8.6g's certificate-free alternative
must use the global infinite-barrier structure, not merely inclusion
minimality, activity, or residue-level two-sum coverage.

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

## Lemma 10.2b: Late one-point thresholds force full lower-sumset recurrence

Let \(k\ge2\), and let \(A\subseteq\mathbb N\) be an asymptotic basis of
order \(k\), with threshold \(N_0\) and \(m_0=\min A\). Suppose there are
infinitely many \(b\in A\) such that
\[
A\setminus\{b\}
\]
is an asymptotic basis of order \(k+1\), but has no order-\((k+1)\)
threshold below \(b\). Then for every finite
\[
T\subset A
\]
and every \(L\), there are \(b\in A\setminus T\), an integer \(w_b\), and
\[
d_b=w_b-b>L
\]
such that
\[
d_b-T\subseteq(k-1)A. \tag{1}
\]
Moreover, for \(k=2\), \(A\) is finitely reflection-recurrent and hence has
an infinite deletion whose complement is an order-3 basis.

Proof. For each such \(b\), choose
\[
w_b\ge b-1,\qquad w_b\notin(k+1)(A\setminus\{b\}),
\]
which is possible because \(b-1\) is not a threshold for
\(A\setminus\{b\}\). Put
\[
d_b=w_b-b.
\]
We first show that \(d_b\) is unbounded along these \(b\)'s.

Suppose instead that \(d_b\le D\) for infinitely many \(b\to\infty\), and
put
\[
D_*=\max\{D+(k-1)m_0,\ N_0\}.
\]
Let
\[
C_b=A\setminus\{b\}.
\]
If \(e\in C_b\), \(w_b-e\ge N_0\), and
\[
e>d_b-(k-1)m_0,
\]
then every \(k\)-term representation of \(w_b-e\) from \(A\) must use
\(b\), because otherwise adding \(e\) would represent \(w_b\) from
\((k+1)C_b\). But any \(k\)-term representation using \(b\) has sum at
least
\[
b+(k-1)m_0,
\]
whereas
\[
w_b-e=b+d_b-e<b+(k-1)m_0.
\]
Thus no such \(e\) exists. In particular,
\[
C_b\cap(D_*,\ w_b-N_0]=\varnothing. \tag{2}
\]

Choose \(b\) in the infinite bounded-\(d_b\) sequence so large that there
is an integer \(n\) with
\[
kD_*<n<
\min\{b+(k-1)m_0,\ w_b-N_0+(k-1)m_0\}. \tag{3}
\]
Such \(n\)'s can be chosen arbitrarily large as \(b\to\infty\). We claim
that \(n\notin kA\), contradicting that \(A\) is an order-\(k\) basis.

Indeed, any \(k\)-term representation of \(n\) using \(b\) has sum at least
\[
b+(k-1)m_0>n
\]
by (3). A representation avoiding \(b\) cannot use a term in the interval
\((D_*,w_b-N_0]\) by (2). If it uses a term \(>w_b-N_0\), then its total is
at least
\[
w_b-N_0+1+(k-1)m_0>n
\]
by (3). Hence every term in a representation avoiding \(b\) would have to
be at most \(D_*\), giving total at most \(kD_*<n\), again impossible. This
proves that \(d_b\) is unbounded.

Now fix finite \(T\subset A\) and \(L\). Choose one of the late elements
\[
b\notin T
\]
with
\[
d_b>L+\max T
\]
and \(w_b-\max T\ge N_0\). For every \(t\in T\), the number \(w_b-t\) has a
\(k\)-term representation from \(A\). Every such representation must use at
least one copy of \(b\), or else adding \(t\in A\setminus\{b\}\) would put
\(w_b\) in \((k+1)(A\setminus\{b\})\). Removing one copy of \(b\) from such
a representation gives
\[
w_b-t-b=d_b-t\in(k-1)A.
\]
This proves (1). When \(k=2\), (1) is finite reflection-recurrence in
\(A\), so Theorem 8.2 gives the final assertion. \(\square\)

## Warning 10.2b': Lower-sumset recurrence can be vacuous

For \(k>2\), the conclusion
\[
d-T\subseteq(k-1)A
\]
does not by itself contain usable reflection information about \(A\). The
simple basis
\[
A=\{1\}\cup2\mathbb N
\]
already shows this for \(k=3\). Here \(A\) is an order-2, hence order-3,
asymptotic basis, and
\[
2A
\]
is cofinite. Therefore every finite \(T\subset A\) has
\[
d-T\subseteq2A
\]
for all sufficiently large \(d\). But \(A\) is not finitely
reflection-recurrent: the two-point set \(\{1,2\}\) has no large center
\(m\) with
\[
m-1,\ m-2\in A,
\]
because one of these two numbers is an odd integer larger than \(1\).

Thus the higher-order singleton and delayed-threshold lemmas need an
additional mechanism converting lower-sumset mirrors into actual \(A\)
mirrors, or a new repair scheme that can spend lower-sumset mirrors without
exceeding the order-\((k+1)\) budget.

## Warning 10.2a: The \(k=3\) one-point split

For \(k=3\), Corollary 10.2 has two distinct alternatives. For every finite
\[
T\subset A
\]
one obtains a subset \(U\subset T\) with \(|U|\ge |T|/2\) and arbitrarily
large centers of one of the following forms:
\[
m-U\subseteq2A, \tag{1}
\]
or
\[
m-U\subseteq A. \tag{2}
\]
Only (2) is directly compatible with the fixed-certificate deletion theorem.
Indeed, if a finite set \(T_0\subset A\) has the property that every
half-sized subset contains elements
\[
e,y_1,y_2,y_3
\]
with
\[
y_1+y_2-e\in A,\qquad y_1+y_2+y_3-2e\in A, \tag{3}
\]
and if the alternative (2) occurs for \(T_0\) with arbitrarily large
centers, then one fixed tuple satisfying (3) is reflection-recurrent.
Lemma 2.3b then gives an infinite deletion whose complement is an order-4
basis.

Alternative (1) is the obstruction: its mirrors live in \(2A\), not \(A\).
Replacing a mirror \(m-y\) by two retained summands spends one extra
summand in the repair identities, so the balanced certificate recursion
from Theorem 2.3 no longer has the right order budget. Thus the
one-point-failure route for \(k=3\) reduces either to a half-density
certificate theorem together with repeated occurrence of (2), or to a new
repair mechanism that can use reflected \(2A\)-mirrors without exceeding
four retained summands.

The obstruction is already visible in a finite window from the robust
booster search. Let
\[
A_0=\{1,3,5,20,21,30,31\}.
\]
For \(a=30\), the witness
\[
w=37
\]
satisfies
\[
w\notin4(A_0\setminus\{30\}).
\]
With
\[
T=\{1,3,5\},\qquad d=w-a=7,
\]
the shifted mirrors are
\[
d-T=\{6,4,2\}\subset2A_0,
\]
via
\[
6=3+3,\qquad 4=1+3,\qquad 2=1+1,
\]
but none of \(2,4,6\) lies in \(A_0\). Thus the lower-sumset recurrence in
the \(r=1\) branch is not a notational artefact; it can be genuinely
\(2A\)-valued even in a small local model.

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

## Lemma 10.3b: Global terminal-gap normal form

Let \(k\ge2\), let \(h=k+1\), and let \(A\subseteq\mathbb N\) be an
asymptotic basis of order \(k\), with order-\(k\) threshold \(N_0\), and put
\[
m_0=\min A.
\]
Assume that no infinite \(B\subset A\) has \(A\setminus B\) an
asymptotic basis of order \(h\). Then for every finite \(E\subset A\), every
infinite \(X\subset A\setminus E\), and every \(L\), there are a finite
nonempty set
\[
F\subset X
\]
and an integer \(w>L\) such that
\[
w\notin h(A\setminus F), \tag{1}
\]
and, writing \(f_0=\min F\),
\[
(A\setminus F)\cap
\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{2}
\]

Moreover \(F\) may be chosen inclusion-minimal for the fixed witness \(w\).
For such a minimal choice, every \(f\in F\) is active: there is a
multiplicity \(q_f\in\{1,\ldots,h\}\) and elements
\[
c_{f,1},\ldots,c_{f,h-q_f}\in A\setminus F
\]
with
\[
w=q_f f+c_{f,1}+\cdots+c_{f,h-q_f}. \tag{3}
\]
When \(q_f=h\), no \(c\)-terms appear.
In particular,
\[
q_f f+(h-q_f)m_0\le w. \tag{4}
\]

Proof. By Corollary 3.1c applied to the infinite set \(X\), there is a
finite late-bad set \(F_0\subset X\). To ensure a large witness, first
replace \(X\) by its infinite tail
\[
X'=\{x\in X:x>L+1\}
\]
and choose \(F_0\subset X'\). If \(A\setminus F_0\) is not an order-\(h\)
basis, choose \(w>L\) with
\[
w\notin h(A\setminus F_0).
\]
If \(A\setminus F_0\) is an order-\(h\) basis but late-bad, then no
threshold below \(\max F_0\) works; since \(\max F_0>L+1\), there is
\[
w\ge \max F_0-1>L
\]
with the same displayed nonrepresentation.

Now shrink \(F_0\) inclusion-minimally while preserving this fixed
nonrepresentation, and call the resulting set \(F\). This gives (1). The
terminal gap (2) is Lemma 10.3 applied to \(F\) and \(w\).

For \(f\in F\), minimality gives
\[
w\in h(A\setminus(F\setminus\{f\})).
\]
Since \(w\notin h(A\setminus F)\), every such representation must use at
least one copy of \(f\). Let \(q_f\) be the number of copies of \(f\) in
one such representation. All other summands avoid \(F\), because the
representation lies in \(A\setminus(F\setminus\{f\})\). This gives (3),
and (4) follows because every remaining summand is at least \(m_0\).
\(\square\)

Thus any counterexample to the broad deletion theorem must contain
arbitrarily far, inside every infinite tail and away from every finite
protected core, finite active barriers whose deletion creates a genuine
order-\((k+1)\) hole and a terminal retained gap. This is the rigorous form
of the high-rank obstruction suggested by the finite experiments.

## Corollary 10.3d: Failure of finite-core stability forces genuine \(A\)-gaps

Let \(k\ge2\), \(h=k+1\), and let \(A\subseteq\mathbb N\) be an
asymptotic basis of order \(k\), with threshold \(N_0\) and \(m_0=\min A\).
Suppose the finite-core finite-deletion stability target fails: for every
finite
\[
E\subset A
\]
there is a nonempty finite
\[
F\subset A\setminus E
\]
such that \(A\setminus F\) is not an asymptotic basis of order \(h\).
Then for every finite \(E\subset A\) and every \(L\), there are a finite
nonempty
\[
F\subset A\setminus E
\]
and an integer \(w>L\) such that, after shrinking \(F\) inclusion-minimally
for this \(w\),
\[
w\notin h(A\setminus F), \tag{1}
\]
every \(f\in F\) is active in the sense of Lemma 10.3b, and, writing
\[
f_0=\min F,
\]
the terminal window is a genuine gap of \(A\):
\[
A\cap\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{2}
\]
Moreover, by taking \(E\) to contain \(A\cap[1,R]\), these genuine gaps can
be forced to have lengths tending to infinity.

Proof. Fix \(E\) and \(L\). By the failure hypothesis choose finite
\[
F_0\subset A\setminus E
\]
such that \(A\setminus F_0\) is not an order-\(h\) basis. Since the failure
is genuine, there are arbitrarily large \(h\)-holes after deleting \(F_0\).
Choose
\[
w>\max\{L,\ 2\max F_0+(k-1)m_0\}
\]
with
\[
w\notin h(A\setminus F_0).
\]
Shrink \(F_0\) inclusion-minimally for this fixed witness \(w\), and call
the resulting set \(F\). Then \(F\subset F_0\), so every element of \(F\) is
at most \(\max F_0\), and (1) holds. Lemma 10.3b gives the activity of each
deleted element and the retained terminal gap
\[
(A\setminus F)\cap\bigl(w-f_0-(k-1)m_0,\ w-N_0\bigr]=\varnothing. \tag{3}
\]
Because
\[
f_0\le\max F_0
\]
and
\[
w>2\max F_0+(k-1)m_0,
\]
the left endpoint in (3) is larger than \(\max F_0\), hence larger than
every deleted element of \(F\). Thus no deleted element lies in the terminal
window either, and (3) is the genuine \(A\)-gap (2).

Finally, if \(E\) contains \(A\cap[1,R]\), then \(f_0>R\). The length of
the terminal interval in (2) is
\[
f_0+(k-1)m_0-N_0
\]
up to the endpoint convention, and this tends to infinity with \(R\).
\(\square\)

Thus any disproof of finite-core finite-deletion stability must be built in
the genuinely sparse regime. Its finite barriers cannot merely delete a few
points from a dense tail; their witnesses must sit immediately after actual
long gaps of \(A\), while still satisfying the active-repair and
vertex-cover constraints.

The script `EXPERIMENTS/actual_gap_barrier_search.py` records a small
finite-window model of this genuine-gap normal form. With default bounds it
finds
\[
S=\{1,2,4,5,6\},
\]
whose two-sums cover through \(12\). Deleting
\[
F=\{4,5\}
\]
creates the inclusion-minimal three-fold hole
\[
w=11,
\]
and the terminal window
\[
(11-4-1,\ 11-2]=(6,9]
\]
contains no element of \(S\). This example is only local: it shows that the
genuine-gap condition is not itself inconsistent with finite order-2
coverage, but it says nothing about iterating such barriers in an infinite
basis.

## Lemma 10.3e: Genuine terminal gaps must be covered by the prefix sumset

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\) with
threshold \(N_0\). Suppose
\[
A\cap(G,H]=\varnothing.
\]
Then
\[
[N_0,H]\cap\mathbb N\subseteq k(A\cap[1,G]).
\]
In particular, for a genuine terminal gap from Corollary 10.3d,
\[
G=w-\min F-(k-1)m_0,\qquad H=w-N_0,
\]
the entire interval
\[
[N_0,H]
\]
inside the gap is already covered by \(k\)-term sums of elements before the
gap.

Proof. Let \(n\in[N_0,H]\). Since \(A\) is an order-\(k\) basis, write
\[
n=a_1+\cdots+a_k,\qquad a_i\in A.
\]
No summand can exceed \(H\), because all summands are positive and
\(n\le H\). Also no summand can lie in \((G,H]\), since this interval is an
\(A\)-gap. Hence every summand lies in \(A\cap[1,G]\), proving the claim.
\(\square\)

Thus finite-core failure needs more than long gaps. Each long terminal gap
must be internally covered by the prefix \(k\)-sumset, while the adjacent
finite deletion \(F\) still vertex-covers the shifted representation graphs
that would otherwise repair the witness. This is the coverage-versus-barrier
tension seen in the staged finite searches.

## Lemma 10.3f: Genuine terminal barriers are prefix-local

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(k\), with
threshold \(N_0\) and \(m_0=\min A\). Let \(h=k+1\), let \(F\subset A\) be
finite and nonempty, put
\[
C=A\setminus F,
\]
and suppose
\[
w\notin hC. \tag{1}
\]
Assume that, with
\[
G=w-\min F-(k-1)m_0,
\]
one has
\[
F\subset A\cap[1,G],\qquad A\cap(G,w-N_0]=\varnothing. \tag{2}
\]
Then the obstruction is prefix-local in the following sense.

1. If \(e\in C\cap[1,G]\) and \(w-e\ge N_0\), then every \(k\)-term
   representation of \(w-e\) from \(A\) meets \(F\), and all of its
   summands lie in \(A\cap[1,G]\).
2. If \(F\) is inclusion-minimal for the witness \(w\), then for every
   \(f\in F\) there is an active repair
   \[
   w=q_f f+c_{f,1}+\cdots+c_{f,h-q_f},
   \]
   with \(q_f\in\{1,\ldots,h\}\), whose retained summands all lie in
   \[
   A\cap[1,G].
   \]

Proof. For (1), Lemma 10.1 says every \(k\)-term representation of \(w-e\)
meets \(F\). Let
\[
w-e=a_1+\cdots+a_k
\]
be such a representation, and choose one summand \(f\in F\). If \(a_i\notin
F\), then
\[
a_i\le w-e-f-(k-2)m_0\le w-m_0-\min F-(k-2)m_0=G.
\]
If \(a_i\in F\), then \(a_i\le G\) by (2). Thus every summand lies in the
prefix \(A\cap[1,G]\).

For (2), inclusion-minimality gives, for each \(f\in F\), a representation
\[
w=q_f f+c_{f,1}+\cdots+c_{f,h-q_f}
\]
with \(q_f\ge1\) and \(c_{f,i}\in C\). For any retained summand \(c_{f,i}\),
\[
c_{f,i}\le w-q_f f-(h-q_f-1)m_0.
\]
Since \(h=k+1\), \(f\ge\min F\), and \(q_f\ge1\), the right side is at most
\[
w-\min F-(k-1)m_0=G.
\]
Thus every retained summand lies in \(A\cap[1,G]\). \(\square\)

Consequently, the genuine-gap finite-core obstruction is a completely
finite prefix gadget: the prefix \(A\cap[1,G]\) already covers the gap by
\(k\)-sums, contains the deleted active set \(F\), supplies the restored
repairs for each \(f\in F\), and supplies all shifted representations that
are vertex-covered by \(F\). Later elements beyond the terminal gap play no
role in the local obstruction.

## Proposition 10.3g: Interval half-deletion barriers are locally scalable

The prefix-local genuine-gap normal form from Corollary 10.3d and Lemmas
10.3e--10.3f is locally sharp for \(k=2\). Let
\[
M\ge X\ge1,
\]
and set
\[
I=[X+1,X+M],\qquad J=[X+2M,X+3M-1],
\]
\[
S=I\cup J,\qquad r=\left\lfloor\frac{M-1}{2}\right\rfloor,
\]
\[
F=\{X+2M,\ X+2M+1,\ldots,\ X+2M+r\},
\]
and
\[
w=3X+5M.
\]
Then:

1. the two-fold sumset of \(S\) covers the full interval
   \[
   [2X+2,\ 3X+5M-2]\subseteq2S; \tag{1}
   \]
2. \(w\notin3(S\setminus F)\);
3. \(F\) is inclusion-minimal for the hole \(w\);
4. with the global minimum \(m_0=1\), the terminal window
   \[
   (w-\min F-1,\ w-2]=(2X+3M-1,\ 3X+5M-2] \tag{2}
   \]
   contains no element of \(S\).

Proof. The sum intervals are
\[
I+I=[2X+2,\ 2X+2M],
\]
\[
I+J=[2X+2M+1,\ 2X+4M-1],
\]
and
\[
J+J=[2X+4M,\ 2X+6M-2].
\]
Since \(M\ge X\),
\[
3X+5M-2\le2X+6M-2,
\]
so these intervals prove (1).

Put \(C=S\setminus F\). The retained high block is
\[
J'=[X+2M+r+1,\ X+3M-1].
\]
A three-term sum from \(C\) cannot equal \(w\). Three low terms from \(I\)
sum at most
\[
3X+3M<w.
\]
One retained high term and two low terms sum at most
\[
(X+3M-1)+2(X+M)=3X+5M-1<w.
\]
Two retained high terms and one low term sum at least
\[
2(X+2M+r+1)+(X+1)>3X+5M=w,
\]
because \(2r+3\ge1\). Three high terms are larger still. Hence
\[
w\notin3C.
\]

For inclusion-minimality, let
\[
f=X+2M+i,\qquad 0\le i\le r.
\]
Then
\[
w=2f+(X+M-2i).
\]
Since \(2i\le2r\le M-1\), the element
\[
X+M-2i
\]
lies in \(I\subset C\). Thus restoring \(f\) repairs the hole, and every
\(f\in F\) is active.

Finally,
\[
w-\min F-1=3X+5M-(X+2M)-1=2X+3M-1.
\]
The low block \(I\) lies below this value, and the high block \(J\) ends at
\[
X+3M-1\le2X+3M-1
\]
because \(X\ge1\). This proves the terminal \(S\)-gap (2). \(\square\)

Thus no proof can rule out finite-core failure using only prefix coverage,
genuine terminal gaps, and inclusion-minimal active repairs. These features
exist in arbitrarily large finite windows. The unresolved issue is global:
one must either prove that such interval barriers cannot be coded into an
unbounded barrier met by every infinite deletion while maintaining coverage
between stages, or build exactly such a staged construction.

## Lemma 10.3h: Covered interval-block barriers are threshold cuts

The interval construction in Proposition 10.3g is rigid inside the
coverage-compatible terminal-gap regime. Keep
\[
I=[X+1,X+M],\qquad J=[X+2M,X+3M-1],\qquad S=I\cup J,
\]
where \(M\ge X\ge1\). Write the high elements as
\[
H_d=X+2M+d,\qquad 0\le d\le M-1,
\]
and put
\[
w_q=3X+5M+q.
\]
Let \(D\) be a nonempty subset of \(\{0,\ldots,M-1\}\), set
\[
F_D=\{H_d:d\in D\},\qquad C_D=S\setminus F_D,
\]
and assume
\[
-X\le q\le M-X. \tag{1}
\]
Then \(w_q\notin3C_D\), \(F_D\) is inclusion-minimal for this hole, and
the terminal interval
\[
(w_q-\min F_D-1,\ w_q-2]
\]
contains no point of \(S\) if and only if \(D\) is one of the following
sets, with empty intervals omitted:

* if \(q\le0\), then
  \[
  D=[0,\lfloor(M+q-1)/2\rfloor]\cup[M+q,M-1]; \tag{2}
  \]
* if \(q>0\), then
  \[
  D=[\lceil q/2\rceil,M-1], \tag{3}
  \]
  or, when \(q\le M-2\),
  \[
  D=[0,\lfloor(M+q-1)/2\rfloor]. \tag{4}
  \]

In particular every such \(D\) has size at least \(\lceil M/2\rceil\).
Thus large interval blocks do not support singleton, pair, or any fixed-rank
coverage-compatible terminal-gap barriers.

Proof. Use low coordinates
\[
L_a=X+1+a,\qquad 0\le a\le M-1.
\]
In the range (1), three low terms are smaller than \(w_q\), and three high
terms are larger than \(w_q\). Hence only two types of representations can
matter.

First, two high terms and one low term give
\[
H_r+H_s+L_a=w_q
\]
exactly when
\[
r+s+a=M+q-1.
\]
Equivalently, after choosing retained high coordinates \(r,s\), such a
low coordinate exists precisely when
\[
q\le r+s\le M+q-1. \tag{5}
\]
Second, one high term and two low terms give
\[
H_r+L_a+L_b=w_q
\]
exactly when
\[
r+a+b=3M+q-2.
\]
Since \(0\le a+b\le2M-2\), this is possible exactly for retained
\[
r\ge M+q, \tag{6}
\]
which can occur only when \(q<0\).

Let \(R=\{0,\ldots,M-1\}\setminus D\) be the retained high coordinates.
The condition \(w_q\notin3C_D\) is therefore equivalent to saying that
(6) never occurs in \(R\), and no two elements of \(R\), with repetition
allowed, have sum in the interval (5). Inclusion-minimality of \(F_D\) is
equivalent to maximality of \(R\) with respect to these two avoidance
conditions: restoring \(H_d\) repairs the hole exactly when adjoining the
coordinate \(d\) creates one of the forbidden representations.

Suppose first that \(q\le0\). Condition (6) forces
\[
R\subseteq[0,M+q-1].
\]
Because the lower endpoint in (5) is nonpositive, the pair-sum condition
says that every retained pair must have sum at least \(M+q\). The unique
maximal set with this property is
\[
R=[\lceil(M+q)/2\rceil,M+q-1],
\]
with the evident empty interpretation when \(M+q=0\). Taking complements
gives (2).

Now suppose \(q>0\). Condition (6) is void. For each \(r\in R\), the
self-pair \(2r\) cannot lie in (5), so every retained coordinate is either
\[
r\le\lfloor(q-1)/2\rfloor
\]
or
\[
r\ge\lceil(M+q)/2\rceil.
\]
These two alternatives cannot be mixed: if \(a\) is in the lower range and
\(b\) in the upper range, then, since \(q<M\), the sum \(a+b\) lies in
\([q,M+q-1]\). Hence a maximal retained set is either the full low block
\[
R=[0,\lfloor(q-1)/2\rfloor],
\]
whose complement is (3), or the full high block
\[
R=[\lceil(M+q)/2\rceil,M-1],
\]
whose complement is (4). The latter retained block is nonempty exactly when
\(q\le M-2\); at the endpoint \(q=M-1\) the empty retained set is not
maximal, because the low block can still be adjoined.

It remains only to check the actual terminal gap. For the sets above,
\[
\min D\le X+q.
\]
This is immediate when \(\min D=0\), and for (3) follows from
\(\lceil q/2\rceil\le X+q\). Therefore
\[
X+3M-1\le w_q-(X+2M+\min D)-1,
\]
so the whole high block \(J\) lies at or below the left endpoint of the
terminal interval. The low block lies even lower, and the terminal interval
contains no point of \(S\). Conversely, if a covered terminal-gap barrier
exists in the range (1), the maximality classification above forces exactly
one of (2)--(4). Finally the displayed formulas give \(|D|\ge\lceil
M/2\rceil\) in every case. \(\square\)

The script `EXPERIMENTS/interval_barrier_family.py` probes whether other
subsets \(F\subset J\) inside the same block can do better. It enumerates
coverage-compatible witnesses \(w\) with \(w-2\in2S\), an actual terminal
\(S\)-gap, and inclusion-minimal three-sum failure after deleting \(F\).
Its `--verify-classification` mode exhaustively checks Lemma 10.3h for
specified finite values of \(X,M\).
For example:
\[
X=3,\quad M=8
\]
has no supported deletions of ranks \(1,2,3\), and the first
coverage-compatible barrier is the lower half
\[
F=(19,20,21,22),\qquad w=49.
\]
Similarly
\[
X=5,\quad M=12
\]
has no supported deletions of ranks \(1,\ldots,5\), and the first barrier is
\[
F=(29,30,31,32,33,34),\qquad w=75.
\]
In all searched cases \(5\le M\le12\), \(1\le X\le M\), no
coverage-compatible pair deletion occurs. If the coverage condition is
dropped, small-rank holes do appear, but only far beyond the two-sum
coverage interval; for instance, with \(X=5,M=12\), the pair
\((37,39)\) has a terminal hole at \(117\), while \(2S\) covers only
through \(80\). These endpoint artefacts do not satisfy the finite-core
burden from Lemma 10.3e.

It is important that disjoint interval gadgets alone would not give a
counterexample. If a staged construction protected only one finite set
\[
F_s
\]
inside each stage, an infinite deletion could choose one element from each
\(F_s\) and avoid containing any whole protected set \(F_s\). Such a
deletion would not be forced to miss the corresponding witnesses. Therefore
the interval half-deletion family is only a local component for a negative
construction. A genuine counterexample would still need an unbounded
barrier on the protected tail, for example a Schreier-type family, with
frozen witnesses for every barrier edge and with all cross-edge poisoning
controlled.

## Warning 10.3i: Interval cuts are not themselves a barrier

The preceding interval classification also rules out a naive
Schreier-indexed block construction. Suppose a construction uses disjoint
finite blocks \(J_s\) and, in each block, a nonempty coverage-compatible
terminal cut
\[
F_s\subset J_s,\qquad |F_s|\ge2,
\]
whose deletion creates a local witness. Then the family
\[
\{F_s:s\ge1\}
\]
is not a deletion barrier on \(\bigcup_s F_s\): choose one element
\[
x_s\in F_s
\]
from each block and put \(B=\{x_s:s\ge1\}\). The set \(B\) is infinite but
contains no whole \(F_s\).

The same obstruction applies to finitely many threshold cuts per block. If
\(\mathcal F_s\) is a finite family of proper subsets of a block \(J_s\)
and no member is a singleton forced by the construction, one can choose
points in the blocks recursively so that the infinite selector avoids
containing every member of every \(\mathcal F_s\). Thus block-local
terminal cuts must be tied together by a genuine cross-block finite-set
barrier.

Consequently, an interval-gadget counterexample has an additional coding
burden beyond Lemma 10.3h. It must assign witnesses to a barrier family on
individual elements of \(A\), not merely to large threshold cuts inside
separate intervals. In a Schreier-type attempt, the construction must make
the arithmetic hole work for every finite Schreier edge, even though such
edges are arbitrary finite subsets of the protected enumeration; a single
interval block supplies only the rigid prefix/suffix cuts from Lemma
10.3h.

## Warning 10.3c: Compactness and random deletion do not see additive structure

The broad deletion theorem cannot be proved from finite-deletion robustness
or compactness alone. There is an abstract representation-system model with
arbitrarily long good finite deletion prefixes but no infinite good
deletion.

Let \(U=\mathbb N\), fix \(h=k+1\), and let \(\mathcal S\) be the Schreier
barrier
\[
\mathcal S=\{F\subset U:\ F\text{ finite and } |F|=\min F\}.
\]
Every infinite \(B\subset U\) contains infinitely many members of
\(\mathcal S\): if \(b=\min B\), take the first \(b\) elements of \(B\) to
obtain one member, then repeat in the tail beyond it.

For each \(F\in\mathcal S\), create a special target \(w_F>\max F\), all
chosen distinct. Declare the \(h\)-term representation edges of \(w_F\) to
be exactly
\[
\{f\}\cup R,\qquad f\in F,\quad
R\subset U\setminus F,\quad |R|=h-1.
\]
All ordinary targets are declared to have every \(h\)-element subset of
\(U\) as a representation.

Then the full set \(U\) represents every target. If \(D\subset U\) is
finite, only the special targets with \(F\subset D\) fail after deleting
\(D\), so finite deletions are eventually harmless. But if \(B\subset U\)
is infinite, then \(B\) contains infinitely many \(F\in\mathcal S\); for
each such \(F\), every representation of \(w_F\) uses an element of \(F\),
so \(w_F\) is not represented from \(U\setminus B\). The witnesses are
unbounded because \(w_F>\max F\).

This model is not additive and is not a counterexample to Erdős Problem
#881. Its role is diagnostic: a proof must use arithmetic information from
the genuine \(kA\)-coverage and shifted representation constraints. Pure
Zorn, compactness, finite-prefix, or independent random-deletion arguments
can be defeated by Schreier-type finite barriers.

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

The standard binary Raikov-Stöhr basis also supports the positive direction.
Let
\[
A_0=\{n>0:\operatorname{supp}_2(n)\subseteq 2\mathbb N\},\qquad
A_1=\{n>0:\operatorname{supp}_2(n)\subseteq 2\mathbb N+1\},
\]
and put
\[
A=A_0\cup A_1.
\]
With \(0\) allowed for padding this is an exact order-2 basis by splitting
the binary support into even-position and odd-position parts; without \(0\),
the usual one-bit carry-down handles all sufficiently large pure-class
exceptions. Thus \(A\) is an asymptotic order-2 basis. Delete
\[
B=\{x\in A_0: |\operatorname{supp}_2(x)|\text{ is even}\}.
\]
Let \(C=A\setminus B\). Then \(C\) is an asymptotic basis of order \(3\).
Indeed, split the binary support of \(n\) into even-position bits \(S\) and
odd-position bits \(T\).

If \(S,T\ne\varnothing\), then:

* if \(|S|\) is even, split \(S\) into two nonempty odd parts and use
  \(T\) as the third summand;
* if \(|S|\) is odd and \(|T|\ge2\), use \(S\) as one retained \(A_0\)
  summand and split \(T\) into two nonempty \(A_1\) summands;
* if \(|S|\) is odd and \(T=\{t\}\), then
  \[
  2^t=2^{t-1}+2^{t-1},
  \]
  with \(t-1\) even, so the two new summands are retained \(A_0\)
  singletons.

If \(T=\varnothing\), then:

* if \(|S|\ge3\) is odd, split \(S\) into three nonempty odd parts;
* if \(|S|\) is even and \(S\) contains \(s\ge2\), use \(S\setminus\{s\}\)
  as one odd retained \(A_0\) summand and split
  \[
  2^s=2^{s-1}+2^{s-1}
  \]
  into two retained \(A_1\) singletons;
* if \(S=\{s\}\), then for \(s\ge2\),
  \[
  2^s=2^{s-1}+2^{s-2}+2^{s-2}.
  \]

If \(S=\varnothing\), then no \(A_1\) elements were deleted. If
\(|T|\ge3\), split \(T\) into three nonempty parts. If
\[
T=\{t_1,t_2\},\qquad t_2\ge3,
\]
write
\[
2^{t_2}=2^{t_2-1}+2^{t_2-1},
\]
and use \(2^{t_1}\) as the third \(A_1\) summand. If \(T=\{t\}\) and
\(t\ge3\), write
\[
2^t=2^{t-1}+2^{t-2}+2^{t-2}.
\]
The finitely many excluded small cases are \(1\) and \(2\). Thus all
sufficiently large integers lie in \(3C\).

The same model also fails to realize the certificate-free escape from
Lemma 8.6g. Let
\[
X=\left\{\sum_{j\in F}4^j:\ \varnothing\ne F\subset\mathbb N
\text{ finite}\right\},\qquad Y=2X,
\]
so \(X=A_0\) after relabelling the even binary positions and \(Y=A_1\).
No finite coloring of
\[
A=X\cup Y
\]
can have all color classes certificate-free relative to \(A\). Indeed,
restrict such a coloring to \(X\). By Hindman's finite-unions theorem,
there are disjoint nonempty finite sets \(U,V\subset\mathbb N\) such that
\[
x_U,\quad x_V,\quad x_{U\cup V}
\]
have the same color, where \(x_F=\sum_{j\in F}4^j\). Put
\[
e=x_U,\qquad y_1=x_{U\cup V}=x_U+x_V,\qquad y_2=x_V.
\]
Then \(y_1,y_2\ne e\) and
\[
y_1+y_2-e=(x_U+x_V)+x_V-x_U=2x_V\in Y\subset A.
\]
Thus \(e,y_1,y_2\) are a monochromatic certificate, contradiction.

Therefore the digital route currently gives no counterexample: the
carry-free model and the natural binary critical-density model both satisfy
the desired conclusion and contain finite certificate tests, while an exact
additive embedding of the free monoid into \(\mathbb N\) is unavailable.

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
Suppose further that there is a hypergraph \(\mathcal F\) on \(A\), all of
whose edges are finite nonempty sets, and, for every \(F\in\mathcal F\), a stage
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

## Proposition 13.1b-Schreier: A sharpened unbounded-rank stage target

The only counterexample route not addressed by the fixed-rank restrictions
above is an unbounded-rank barrier. The following criterion isolates what a
Schreier-type construction would have to achieve in the \(k=2\) case.

Let
\[
P=\{p_1<p_2<\cdots\}
\]
be a cofinite subset of the final set, and let
\[
\mathcal S=\{F\subset P:\ |F|=\operatorname{index}(\min F)+1\}
\]
be the Schreier barrier on \(P\). Suppose there are increasing finite sets
\[
A_0\subset A_1\subset A_2\subset\cdots
\]
and increasing ceilings
\[
C_s\to\infty,\qquad R_s\to\infty
\]
such that, for all sufficiently large \(s\):

1. all elements added after stage \(s\) are larger than \(R_s\);
2. with \(m_0=\min A_0\),
   \[
   R_s+m_0\le C_s; \tag{1}
   \]
3. the new coverage interval satisfies
   \[
   [C_{s-1}+1,C_s]\subseteq2A_s; \tag{2}
   \]
4. every Schreier edge \(F\in\mathcal S\) first completed by stage \(s\)
   has a frozen witness
   \[
   C_{s-1}<w_F\le R_s,\qquad w_F\notin3(A_s\setminus F); \tag{3}
   \]
5. each such hole is inclusion-minimal:
   \[
   w_F\in3(A_s\setminus(F\setminus\{f\}))\qquad(f\in F); \tag{4}
   \]
6. and it satisfies the genuine shifted-domination condition: for every
   retained
   \[
   e\in A_s\setminus F,\qquad w_F-e\ge C_{s-1}+1,
   \]
   every two-term representation of \(w_F-e\) from \(A_s\) meets \(F\).
7. the witnesses are unbounded along the Schreier barrier: for every
   infinite \(B\subset P\) and every \(L\), there is
   \[
   F\in\mathcal S,\qquad F\subset B,\qquad w_F>L. \tag{5}
   \]

Then
\[
A=\bigcup_s A_s
\]
is an asymptotic basis of order \(2\), and for every infinite
\[
B\subset A
\]
the set \(A\setminus B\) is not an asymptotic basis of order \(3\).
Consequently \(A\setminus B\) is not an order-2 basis either.

Proof. The coverage intervals (2) imply that \(A\) is an order-2 basis.
Let \(B\subset A\) be infinite and \(L\) arbitrary. Since \(A\setminus P\)
is finite, \(B\cap P\) is infinite. By (5), applied to \(B\cap P\), choose
\[
F\in\mathcal S,\qquad F\subset B\cap P,\qquad w_F>L.
\]
Let \(s=s(F)\) be the stage at which \(F\) was completed. Since all later
elements are \(>R_s\ge w_F\), no later positive summand can occur in a
three-term representation of \(w_F\). Thus (3) persists:
\[
w_F\notin3(A\setminus F).
\]
Because \(F\subset B\), we have \(A\setminus B\subseteq A\setminus F\), so
\[
w_F\notin3(A\setminus B).
\]
The witnesses can be chosen arbitrarily large, so \(A\setminus B\) is not
an order-3 basis. If it were an order-2 basis, padding by any retained
element would make it an order-3 basis; if it is finite, it is not an
asymptotic basis. Hence it is not an order-2 basis. \(\square\)

Conditions (4)--(6) are not needed for the formal implication, but they are
the arithmetic compatibility checks any credible construction must pass:
they make the local holes match the minimal active-barrier normal form from
Lemma 8.4b and the shifted vertex-cover condition from Lemma 10.1. The
criterion is not ruled out by the fixed-rank lemmas because edge sizes in
\(\mathcal S\) tend to infinity on tails.

### Variant 13.1b-enum: The Schreier order need not be the value order

The formal barrier implication above does not require the Schreier order to
be the numerical order on \(P\). Let
\[
P=\{u_1,u_2,\ldots\}
\]
be any enumeration of a cofinite subset of the final set, and define
\[
\mathcal S_{\rm enum}
=\{\{u_i\}\cup G:\ G\subset\{u_j:j>i\},\ |G|=i\}.
\]
If the stage construction assigns persistent witnesses \(w_F\) to the
edges \(F\in\mathcal S_{\rm enum}\), and these witnesses are unbounded in
every infinite set of enumeration indices, then the proof of Proposition
13.1b is unchanged. Every infinite \(B\subset P\) has a least enumeration
index \(i\), and then contains an edge of \(\mathcal S_{\rm enum}\) with
first vertex \(u_i\); the unbounded-witness hypothesis supplies such edges
above any prescribed \(L\).

This matters for the finite diagnostics below. The current
`schreier_stage_search.py` tests the value-ordered target
\[
p_1<p_2<\cdots,
\]
so repair fillers larger than a new protected point are immediately
promoted into later protected vertices and must already carry their own
Schreier edges. An enumerated barrier could, in principle, delay those
fillers in the barrier order even though their numerical values are small.
That does not remove the arithmetic burden; when a delayed filler \(q\) is
eventually promoted, Corollary 13.1h.1 still requires a witness outside all
shifted sets \(p+2(A_s\setminus\{a,q\})\) from the old retained endpoints
\(p\). Thus the P6 failure rules out the immediate value-ordered promotion
route, while the delayed-enumeration route remains a separate construction
problem.

The script `EXPERIMENTS/schreier_stage_search.py` verifies that the first
finite Schreier pattern is not locally inconsistent. It finds
\[
A_0=\{1,2,3,4,8\},
\]
whose two-sums cover through \(12\). With protected tail
\[
P_0=\{1,2,3,4\},
\]
the first Schreier edges have minimal dominated holes
\[
\{1,2\}\mapsto6,\qquad
\{1,3\}\mapsto7,\qquad
\{1,4\}\mapsto10,\qquad
\{2,3,4\}\mapsto12.
\]
This is finite evidence only. It shows that the Schreier-stage target is
not ruled out by the local active-hole and shifted-domination checks at the
first stage; it says nothing about iterating the construction with
unbounded witnesses and coverage buffers.
With `--extend-first --max-new 5 --max-candidate 55`, the same script tries
to extend this seed by up to five new elements through \(55\), while
checking all Schreier edges among the first five protected elements. It
finds no second-stage extension under those bounds. This is again finite
evidence only, but it locates the first iteration pressure point for the
unbounded-rank route.
The direct search with
`--protected-count 6 --max-value 17 --max-size 9` does find a larger local
pattern:
\[
A_1=\{1,2,4,5,6,8,14,16,17\},
\]
with two-sum coverage through \(25\) and all twelve Schreier edges among
the first six protected points carrying minimal dominated holes. Thus the
failure to extend the first seed is not by itself a proof of local
impossibility; early choices matter substantially.
The more relevant tail-protected mode also finds examples. With
`--protected-count 4 --min-protected 10 --max-value 30 --max-size 10`, it
finds
\[
A_2=\{1,2,4,5,8,10,15,18,19\}
\]
with protected tail \(\{10,15,18,19\}\), two-sum coverage through \(30\),
and minimal dominated holes
\[
\{10,15\}\mapsto19,\quad
\{10,18\}\mapsto30,\quad
\{10,19\}\mapsto29,\quad
\{15,18,19\}\mapsto27.
\]
So the local finite obstruction persists even when the protected Schreier
points are separated from the small coverage core.
The same script's `--tail-chain` mode records a one-step extension:
\[
\{1,2,4,5,8,10,15,18,19\}
\]
with protected \(\{10,15,18,19\}\) extends to
\[
\{1,2,4,5,8,10,15,18,19,30\}
\]
with protected \(\{10,15,18,19,30\}\) and coverage through \(38\). The
bounded search then finds no sixth protected point \(p_6\le120\), even
allowing up to three additional fillers through \(151\). The observed
pressure is the same as in the stage arguments: the new pair
\(\{10,p_6\}\) needs a terminal retained gap clearing the old protected
point \(30\), but moving \(p_6\) far enough to create such a gap outruns the
available two-sum coverage.

## Lemma 13.1f: Finite forbidden windows for stage witnesses

Let \(S\subset\mathbb N\) be finite, let
\[
m=\min S,
\]
and suppose
\[
[N,H]\subseteq2S.
\]
Let \(F\subset S\) be nonempty, put \(a=\min F\), and let \(w\le H\). If
\[
w\notin3(S\setminus F),
\]
then
\[
(S\setminus F)\cap(w-a-m,\ w-N]=\varnothing. \tag{1}
\]
Equivalently, every retained \(c\in S\setminus F\) forbids the whole witness
window
\[
c+N\le w\le c+a+m-1. \tag{2}
\]

Proof. If
\[
c\in(S\setminus F)\cap(w-a-m,\ w-N],
\]
then \(w-c\in[N,H]\), so choose
\[
w-c=x+y,\qquad x,y\in S.
\]
If \(x,y\notin F\), then
\[
w=c+x+y\in3(S\setminus F),
\]
contrary to the hypothesis. Thus one of \(x,y\) lies in \(F\), and hence
\[
w-c=x+y\ge a+m.
\]
This contradicts \(c>w-a-m\). Therefore (1) holds, and (2) is just (1)
rewritten with \(c\) fixed. \(\square\)

## Lemma 13.1g: Minimal stage holes have an exact repair intersection

Let \(S\subset\mathbb N\) be finite, let \(F\subset S\) be nonempty, put
\[
C=S\setminus F,
\]
and suppose
\[
w\notin3C. \tag{1}
\]
Then \(F\) is inclusion-minimal for the hole \(w\), meaning that
\[
w\in3(S\setminus(F\setminus\{f\}))\qquad(f\in F), \tag{2}
\]
if and only if, for every \(f\in F\),
\[
w\in (f+2C)\cup(2f+C)\cup\{3f\}. \tag{3}
\]

Proof. Restoring only \(f\) changes the retained set from \(C\) to
\[
C\cup\{f\}.
\]
Because \(w\notin3C\), a three-term representation of \(w\) from
\[
C\cup\{f\}
\]
must use at least one copy of \(f\). According to whether it uses one, two,
or three copies of \(f\), this is exactly the alternatives
\[
w\in f+2C,\qquad w\in2f+C,\qquad w=3f.
\]
Thus (2) is equivalent to (3) for each \(f\in F\). \(\square\)

Therefore a candidate witness for a finite Schreier edge must lie not only
outside \(3C\) and outside the forbidden terminal windows from Lemma
13.1f, but also in the repair intersection
\[
\bigcap_{f\in F}\bigl((f+2C)\cup(2f+C)\cup\{3f\}\bigr).
\]
The P6 diagnostics below use precisely this extra intersection: some
candidate values survive the terminal windows but fail because at least one
deleted vertex has no restored repair.

## Lemma 13.1h: Retained endpoints poison candidate intervals

Let \(S\subset\mathbb N\) be finite, let
\[
E=\{a,q\}\subset S,
\]
put \(C=S\setminus E\), and suppose \(p\in C\). If integers \(R\ge q\)
and \(q-p\le R-p\) satisfy
\[
[q-p,\ R-p]\subseteq2C, \tag{1}
\]
then
\[
[q,R]\subseteq3C. \tag{2}
\]
In particular, no pair edge \(E\) can have a witness in the interval
\([q,R]\).

Proof. For every \(v\in[q,R]\), condition (1) gives
\[
v-p\in2C.
\]
Since \(p\in C\),
\[
v=p+(v-p)\in C+2C=3C.
\]
This proves (2), and therefore every \(v\in[q,R]\) is poisoned as a
candidate witness for deleting \(E\). \(\square\)

This lemma explains one recurring failure mode in the finite Schreier
searches. When a first pair-edge witness forces new retained fillers, an
old retained endpoint can combine with the current two-sum buffer to make
all small candidates for the next pair edge already lie in \(3C\). The
loophole is equally clear: a construction would have to break the interval
\([q-p,R-p]\) after deleting the new pair, or push the new protected point
beyond the poisoned range.

### Corollary 13.1h.1: Promoted pair vertices need shifted gaps

Let \(S\subset\mathbb N\), let \(a<q\) be elements of \(S\), and put
\[
C=S\setminus\{a,q\}.
\]
If \(v\notin3C\), then every retained
\[
p\in C
\]
satisfies
\[
v-p\notin2C. \tag{1}
\]
Consequently, a candidate witness \(v\) for the pair edge \(\{a,q\}\)
must lie outside
\[
\bigcup_{p\in C}(p+2C). \tag{2}
\]
In particular, if a previously retained endpoint \(p<q\) has
\[
[q-p,R-p]\subseteq2C,
\]
then no witness for \(\{a,q\}\) can lie in \([q,R]\).

Proof. If \(v-p\in2C\) for some \(p\in C\), then
\[
v=p+(v-p)\in C+2C=3C,
\]
contrary to the hypothesis. The union statement is the same assertion for
all retained \(p\). The final interval statement is Lemma 13.1h. \(\square\)

Thus any finite-stage construction that repairs a pair edge by adding
mirrors or fillers and later promotes those fillers into the protected tail
incurs a new obligation: before the filler \(q\) can support its own pair
edge with the old lower endpoint \(a\), the stage must reserve a shifted
two-sum gap for a witness \(v\) against every old retained \(p\). This is
the local closure cost visible in the P6 diagnostic.

## Lemma 13.1i: Low-excess pair holes force private mirrors

Let \(S\subset\mathbb N\) be finite, let \(a<p\) be elements of \(S\), put
\[
F=\{a,p\},\qquad C=S\setminus F,
\]
and suppose
\[
[N,H]\subseteq2S,\qquad w=p+u\le H,\qquad w\notin3C. \tag{1}
\]
Let \(e\in C\) satisfy
\[
w-e\ge N,\qquad w-e\notin F+F. \tag{2}
\]
Then at least one of the following alternatives holds:
\[
u-e\in C,\qquad e+p\notin2C, \tag{3}
\]
or
\[
p+u-a-e\in C,\qquad e+a\notin2C. \tag{4}
\]
In particular, if (4) holds and \(e<u-a\), then the mirror
\[
q=p+u-a-e
\]
is a new element of \(C\) larger than \(p\).

Proof. Since \(w-e\in[N,H]\), choose a two-term representation
\[
w-e=s_1+s_2,\qquad s_i\in S.
\]
If both \(s_i\) lay in \(C\), then \(w=e+s_1+s_2\in3C\), contrary to
(1). Thus the representation meets \(F\). Because \(w-e\notin F+F\), it
meets \(F\) in exactly one element.

If the representation uses \(p\), then
\[
w-e-p=u-e\in C.
\]
If also \(e+p\in2C\), then
\[
w=(u-e)+(e+p)\in C+2C=3C,
\]
contradiction. Hence (3) holds.

If the representation uses \(a\), then
\[
w-e-a=p+u-a-e\in C.
\]
If also \(e+a\in2C\), then
\[
w=(p+u-a-e)+(e+a)\in C+2C=3C,
\]
again a contradiction. Hence (4) holds. The final assertion is immediate
from \(e<u-a\). \(\square\)

Thus a low-excess pair witness is not only a terminal-gap object. Each
active retained row must be assigned a private color, and the lower color
can force new retained mirrors beyond the moving endpoint \(p\). If those
mirrors are later included in the protected tail, Lemma 13.1h can poison
their first candidate intervals; the open question is whether a sparse
hierarchical construction can route these mirrors without losing the
two-sum coverage buffer.

Consequently, if a first-completed Schreier edge \(F\) with
\[
a=\min F,\qquad y=\max F
\]
has a stage witness \(w\), then activity gives \(w\ge y+2m\), while the
stage ceiling gives \(w\le R_s\). No witness can exist if
\[
[y+2m,\ R_s]\subseteq
\bigcup_{c\in A_s\setminus F}[c+N,\ c+a+m-1]. \tag{3}
\]
Thus a finite stage must place each witness in a gap left by the retained
points' forbidden windows. The missing global obstruction is precisely to
derive such a covering (3) for some newly completed Schreier edge from the
two-sum coverage and buffer conditions alone.

The P5-to-P6 stall in the finite search illustrates the same pressure in a
more concrete form. Let
\[
S=\{1,2,4,5,8,10,15,18,19,30\},\qquad a=10,
\]
and try to add a sixth protected point \(p>30\). Suppose the pair edge
\[
F=\{10,p\}
\]
has a witness \(w=p+u<2p+1\) in a finite extension
\[
A=S\cup\{p\}\cup Q,\qquad \min Q>p,
\]
with two-sum coverage through \(w\). Since restoring \(p\) repairs the
hole, the low-excess assumption forces
\[
u\in2(S\setminus\{10\}). \tag{4}
\]
Moreover, for every retained old point
\[
c\in S\setminus\{10\},\qquad u\le c,
\]
one must have
\[
p+u-c-10\in S. \tag{5}
\]
Indeed, \(w-c=p+u-c\le p\), so neither \(p\) nor any element of \(Q\) can
occur in a positive two-term representation of \(w-c\). Since \(w-c\) is in
the covered range and \(w\notin3(A\setminus F)\), every two-term
representation of \(w-c\) from \(A\) must meet \(F\). It cannot use \(p\),
so it must use \(10\), giving (5).

If \(u\le18\), then (5) with \(c=18,19,30\) says that, for
\[
L=p+u-10,
\]
the three integers
\[
L-18,\qquad L-19,\qquad L-30
\]
all lie in \(S\). But \(L-19\) and \(L-18\) are consecutive elements of
\(S\), and the only consecutive pairs in \(S\) are
\[
(1,2),\qquad(4,5),\qquad(18,19).
\]
In these three cases \(L-30\) is respectively \(-10,-7,7\), never an
element of \(S\). Hence every such low-excess pair witness must satisfy
\[
w-p=u\ge19. \tag{6}
\]

A bounded enumeration of the remaining range \(19\le u\le30\), using
(4), (5), and the three-sum hole condition, leaves only one pair-edge
escape:
\[
p=38,\qquad w=58,
\]
which is realized by
\[
A=S\cup\{38,40,43,44\}.
\]
Thus the first new pair edge \(\{10,p\}\) alone does not prove the P6
failure. In the actual Schreier P6 test, the extension with \(p=38\) fails
because the new higher-rank edges
\[
\{15,18,38\},\quad \{15,19,38\},\quad
\{15,30,38\},\quad \{18,19,30,38\}
\]
have no compatible witnesses. The surviving obstruction is therefore the
simultaneous closure of many reflected terminal windows, not just a single
pair-edge inequality.

Lemma 8.4c gives the exact row condition behind this simultaneous-closure
pressure. For a finite stage \(S\), edge \(F\), retained set
\[
C=S\setminus F,
\]
covered interval \([N,H]\subseteq2S\), and candidate witness \(w\le H\),
every active retained padder
\[
e\in C,\qquad w-e\ge N,\qquad w-e\notin F+F
\]
must have at least one private color
\[
f\in F,\qquad w-e-f\in C,\qquad e+f\notin2C. \tag{7}
\]
The diagnostic script `EXPERIMENTS/private_sum_matrix.py` prints these
exact colors for the alternating-deletion window, the first Schreier seed,
and the P6 pair-edge escape. In the escape above, \(F=\{10,38\}\) and
\(w=58\), every active row has a color:
\[
\begin{array}{c|c}
e&\text{allowable colors}\\ \hline
1,2,15,19&38\\
4,8,30,40,43,44&10\\
5,18&10\text{ or }38.
\end{array}
\]
Thus the new necessary condition does not refute the first pair-edge
escape. It refutes only the naive lift in which the retained tail absorbs
all sums \(T+F\) back into \(2C\). Once the fillers \(40,43,44\) are
protected, the later Schreier edges have to satisfy their own row
conditions and their own inclusion-minimal repairs; this is where the
bounded search fails. A viable reflected-Schreier construction must
therefore carry, for every first-completed edge \(F\), not only a witness
\(w_F\), but also a full private-color incidence matrix satisfying (7),
with all added mirrors and fillers either kept in a fixed finite
exceptional set or assigned their own later barrier witnesses.

The enhanced `--p6-pair-diagnostic` output separates the first failures
into poisoned candidate witnesses, missing reflected rows, absorbed rows
\(e+f\in2C\), and missing inclusion-minimal repairs. For the pair-edge
escape above, the early new protected edges
\[
\{10,40\},\quad \{10,43\},\quad \{10,44\}
\]
already fail because their first possible witnesses lie in \(3C\). The
higher-rank edge
\[
\{18,19,30,38\}
\]
has non-poisoned candidates \(w=39\) and \(w=41\), but those candidates are
not inclusion-minimal: restoring all single deleted vertices does not
repair the hole. This confirms that the P6 stall is not one local
pair-edge condition; it is simultaneous private-color closure plus
minimal-repair closure across the new protected fillers.

The same diagnostic gives an exact finite obstruction for the protected
fillers. In
\[
A=\{1,2,4,5,8,10,15,18,19,30,38,40,43,44\},
\]
with two-sum coverage through \(63\), each filler
\[
q\in\{40,43,44\}
\]
satisfies
\[
[q,63]\subseteq3(A\setminus\{10,q\}).
\]
Hence no witness inside the current covered window can certify the
Schreier pair edge \(\{10,q\}\). The old retained endpoint \(38\) accounts
for many of these poisoned candidates by Lemma 13.1h, but it leaves
shifted two-sum gaps; the remaining old retained points fill those gaps in
three sums. Thus the first pair-edge escape is not usable in a cofinite
protected tail unless the construction also supplies a separate mechanism
for shielding the fillers' own pair edges.

The delayed-enumeration loophole from Variant 13.1b-enum also fails for
this exact finite set if only the fillers are delayed. The diagnostic
`--p6-order-diagnostic` keeps
\[
\{40,43,44\}
\]
available as retained fillers but tests all \(6!\) enumeration orders of
\[
\{10,15,18,19,30,38\}.
\]
No order gives witnesses for all Schreier edges among these six vertices.
The best orders still have three failed edges, for example
\[
(10,18,15,19,30,38)
\]
fails at
\[
\{18,15,38\},\qquad \{18,19,38\},\qquad \{15,19,30,38\}.
\]
Thus delaying the fillers alone does not repair the P6 finite obstruction;
an enumerated-barrier construction would also have to alter the placement
or witness scheme for the new vertex \(38\) itself.
The obstruction appears before the full \(6!\)-order check. Among the six
vertices, the only vertex with pair witnesses to every other vertex is
\[
10.
\]
So any successful enumeration would have to start with \(10\). But after
placing \(10\) first, no remaining vertex has all required rank-three
Schreier edges against the four-element tail. This two-level prefix failure
is the exact finite combinatorial obstruction reported by the diagnostic.

The bounded search mode `--p6-enum-search` tests this delayed-enumeration
escape from the P5 seed without fixing \(p_6=38\). With
`--max-p6 80 --max-extra 1 --max-extra-value 120`, it checks all candidates
with at most one delayed filler through \(120\), precomputes the protected
subsets that have witnesses, and then tests all enumeration orders. It
finds no extension. In that range only \(p_6\le38\) pass the coverage
filter; larger \(p_6\)'s already outrun the available two-sum coverage with
one delayed filler.
After replacing the order test by Lemma 13.1j-style lazy prefix-link
pruning, the same mode also checks
`--max-p6 55 --max-extra 2 --max-extra-value 95`. It finds no extension
among \(14912\) coverage-passing candidates with up to two delayed fillers.
A wider delayed-filler run
`--max-p6 45 --max-extra 3 --max-extra-value 75` checks \(89702\)
coverage-passing candidates and again finds no extension; after
\(p_6=38\), no later candidate passes the coverage filter within those
bounds. Thus the first P6 obstruction is not removed by one or two small
delayed fillers, nor by three delayed fillers in this smaller value range.
Any continuation must use a more global placement of \(p_6\) and its
support fillers.

## Lemma 13.1j: Enumerated Schreier stages require complete prefix links

Let \(V\) be a finite set, and for each \(r\ge2\) let
\[
\mathcal G_r\subseteq[V]^r
\]
be the family of \(r\)-element subsets that are supported by whatever local
witness condition is being tested. An ordering
\[
v_1,\ldots,v_n
\]
of \(V\) supports all finite Schreier edges in this stage if and only if,
for every \(i\) with \(i\le n-i\),
\[
\{v_i\}\cup H\in\mathcal G_{i+1}
\qquad\text{for every }H\in[\{v_{i+1},\ldots,v_n\}]^i. \tag{1}
\]
In particular, \(v_1\) must be joined by good pairs to every later vertex;
after \(v_1\) is fixed, \(v_2\) must have a complete good-triple link on
the remaining tail; and so on.

Proof. In the enumerated Schreier family, the edges first completed by the
vertex \(v_i\) are exactly the sets
\[
\{v_i\}\cup H,\qquad H\in[\{v_{i+1},\ldots,v_n\}]^i,
\]
whenever the tail has at least \(i\) elements. Requiring all these edges to
belong to the corresponding good family is precisely (1). \(\square\)

For the P6 finite set above, \(\mathcal G_r\) is the family of protected
\(r\)-subsets with an inclusion-minimal dominated witness in the current
coverage window. Lemma 13.1j explains the diagnostic output: the first
prefix-link condition forces \(v_1=10\), and the second prefix-link
condition has no solution. Thus the finite obstruction is not merely that
one unlucky value order fails; the supported-subset hypergraph has no
Schreier-compatible prefix links at all.

## Corollary 13.1k: First-prefix low-excess links force a good deletion

Work in the \(k=2\) case, and let \(A\) be an asymptotic basis of order
\(2\), with threshold \(N_0\). Fix \(d\in A\) and \(D\ge0\), and put
\[
M=\max\{D,d\}.
\]
Suppose that for every finite nonempty
\[
T\subset A\cap(M,\infty)
\]
and every \(L\), there are
\[
p\in A\setminus(T\cup\{d\}),\qquad w\in\mathbb N,
\]
such that
\[
w-\max T\ge N_0,\qquad w-d>L,\qquad p\le w\le p+D,
\]
and
\[
w\notin3(A\setminus\{d,p\}).
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. This is Lemma 8.2c' with \(b=p\). \(\square\)

Thus an enumerated Schreier counterexample cannot have a first prefix
vertex \(d\) whose pair links to the later tail are uniformly
low-top-excess in this finite-test sense. Lemma 13.1j says that the first
enumeration vertex must support all later pair edges. Corollary 13.1k says
that, in a genuine counterexample, those links must either have unbounded
top excess on some tail, lose pair-private status when arbitrary finite
test sets are avoided, or be replaced by a higher-rank prefix obstruction.
The next corollary shows that the non-uniform escape is unavailable for
infinitely many genuine rank-2 pair links.

## Corollary 13.1l: First-prefix pair excess must diverge on tails

Work in the \(k=2\) case, and suppose \(A\) is a counterexample to the
desired order-3 deletion conclusion, with order-2 threshold \(N_0\). Fix
\(d\in A\). Then for every constant \(D\ge0\), there are only finitely
many \(p\in A\) for which there is a witness \(w\) satisfying
\[
p\le w\le p+D,\qquad w\notin3(A\setminus\{d,p\}). \tag{1}
\]

Equivalently, if an enumerated Schreier construction uses \(d\) as the
first prefix vertex and supplies genuine pair-private witnesses to later
vertices \(p\), then the minimal excess \(w-p\) of those pair witnesses
must tend to infinity along every infinite later tail.

Proof. If (1) holds for infinitely many \(p\), choose one such witness
\(w_p\) for each of them. Since \(w_p\ge p\), these witnesses are
unbounded on the infinite set of corresponding \(p\)'s. For any finite
nonempty
\[
T\subset A\cap(\max\{D,d\},\infty)
\]
and any \(L\), choose \(p\notin T\cup\{d\}\) from that infinite set with
\[
w_p-\max T\ge N_0,\qquad w_p-d>L.
\]
Corollary 13.1k gives an infinite \(B\subset A\) such that \(A\setminus B\)
is an order-3 basis, contradicting that \(A\) is a counterexample.
\(\square\)

## Corollary 13.1l.1: Higher prefix edges need divergent first-tail excess

Work in the \(k=2\) case, and suppose \(A\) is a counterexample to the
desired order-3 deletion conclusion, with order-2 threshold \(N_0\). Fix
\[
d\in A,\qquad r\ge1.
\]
Let \(Y\subset A\setminus\{d\}\) be infinite. Then for every \(D\ge0\) it
is not possible that every \(r\)-element subset \(H\subset Y\) has a
witness \(w_H\) satisfying
\[
\min H\le w_H\le \min H+D,\qquad
w_H\notin3(A\setminus(\{d\}\cup H)). \tag{1}
\]

Equivalently, for any fixed prefix vertex \(d\) and any fixed rank \(r+1\),
the minimum possible excess
\[
w_H-\min H
\]
for genuine holes of \(\{d\}\cup H\) is unbounded on every infinite later
tail \(Y\). Missing witnesses count as infinite excess.

Proof. Suppose (1) holds for some \(D\) and infinite \(Y\). Put
\[
M=\max\{D,d\}.
\]
Fix finite nonempty \(T\subset A\cap(M,\infty)\) and \(L\). Choose
\[
H\in[Y]^r
\]
disjoint from \(T\cup\{d\}\), with
\[
\min H>\max\{M,\max T+N_0,L+d\}.
\]
Then its witness \(w_H\) satisfies
\[
w_H-\max T\ge N_0,\qquad w_H-d>L,\qquad
\min H\le w_H\le\min H+D,
\]
and Lemma 8.2c'' gives a good infinite deletion, contradiction. \(\square\)

For an enumerated Schreier target, apply this with \(d=u_i\), \(r=i\), and
\(Y\) an infinite subset of the later vertices \(\{u_j:j>i\}\). Since
Lemma 13.1j requires all edges \(\{u_i\}\cup H\) with
\(H\in[Y]^i\), a counterexample cannot witness all of them within bounded
distance of their first later endpoint. Thus every prefix level in a
Schreier lift must develop its own divergent first-tail excess, not merely
the first pair level.

## Corollary 13.1l.2: Fixed-prefix high-excess pair tails become list-colored

Work in the \(k=2\) case, and suppose \(A\) is a counterexample to the
desired order-3 deletion conclusion, with order-2 threshold \(N_0\). Fix
\[
d\in A
\]
and let \(Y\subset A\setminus\{d\}\) be infinite. Suppose that every
\[
p\in Y
\]
has at least one genuine pair witness
\[
w_p\notin3(A\setminus\{d,p\}). \tag{1}
\]
By Corollary 13.1l, for every \(D\) only finitely many \(p\in Y\) have any
witness with \(w-p\le D\). In fact, the high-excess witnesses must be
endpoint-list coherent: for every finite nonempty
\[
T\subset A\setminus\{d\}
\]
and every \(M\), there are \(p\in Y\setminus T\) and a witness \(w\) for
\(\{d,p\}\) such that
\[
w-\max T\ge N_0,\qquad w-d>M,\qquad w-p>M, \tag{2}
\]
and the endpoint lists
\[
L_w(t)=\{z\in\{d,p\}:w-t-z\in A\}\qquad(t\in T)
\]
admit a choice function whose two fibers are certificate-free relative to
\(A\).

Consequently, suppose an infinite set \(R\subset A\setminus\{d\}\) has the
following finite-test property: for every finite nonempty \(T\subset R\)
and every \(M\), there are \(p\in A\setminus(T\cup\{d\})\) and a witness
\(w\) satisfying (2) whose endpoint lists on \(T\) admit a certificate-free
choice function. Then \(R\) has a two-coloring
\[
R=C_d\cup C_p
\]
such that both \(C_d\) and \(C_p\) are certificate-free relative to \(A\),
and both are separately reflection-recurrent in \(A\).

Proof. Fix finite nonempty \(T\subset A\setminus\{d\}\). If, for every
\(M\), there were a witness satisfying (2) whose endpoint lists admitted no
certificate-free choice function, Lemma 8.6g' with
\[
x_w=d,\qquad y_w=p
\]
would give an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis, contradiction.

Now fix \(M_0\). The bounded-excess conclusion from Corollary 13.1l and
the assumed witnesses (1) give witnesses satisfying (2) for every
\(M\ge M_0\). If none of the witnesses satisfying (2) with \(M=M_0\) were
list-colored, then choosing such a witness for each \(M\ge M_0\) would
produce the forbidden no-list family above. Therefore a list-colored
witness satisfying (2) exists for \(T\) and \(M_0\). Since \(M_0\) was
arbitrary, the first assertion follows.

For the final assertion, enumerate \(R=\{r_1,r_2,\ldots\}\) and put
\[
T_j=\{r_1,\ldots,r_j\}.
\]
Choose list-colored witnesses for \(T_j\) with \(M=j\). Color a point of
\(T_j\) by \(d\) or by \(p_j\), according to the chosen endpoint list
color. Passing to a subsequence, the color of every fixed \(r_i\)
stabilizes. Let \(C_d\) and \(C_p\) be the resulting stable fibers.

If one stable fiber contained a certificate triple
\[
e,y_1,y_2,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then that triple would eventually lie in one certificate-free finite fiber,
impossible. Thus both stable fibers are certificate-free. If
\(U\subset C_d\) is finite, then for all sufficiently large \(j\) the
chosen center \(w_j-d\) reflects \(U\) into \(A\), and \(w_j-d\to\infty\).
The same argument with centers \(w_j-p_j\) proves recurrence for finite
\(U\subset C_p\). \(\square\)

## Corollary 13.1l.3: A Schreier first tail is bipartite recurrent Sidon

In any \(k=2\) counterexample realized by the enumerated-Schreier target of
Variant 13.1b-enum, let
\[
u_1
\]
be the first protected vertex and let
\[
P_1=\{u_j:j>1\}
\]
be the later protected tail. Then \(P_1\) has a two-coloring
\[
P_1=C_0\cup C_1
\]
such that:

1. each \(C_i\) is certificate-free relative to \(A\), hence Sidon;
2. each \(C_i\) is separately reflection-recurrent in \(A\);
3. consequently, since \(P_1\) is cofinite in \(A\), one has
   \[
   |A\cap[1,X]|=O(\sqrt X);
   \]
4. and the mixed representation counts between the two colors are not
   uniformly \(o(A(X))\). More precisely,
   \[
   \max_{n\le X}|\{(c_0,c_1)\in C_0\times C_1:c_0+c_1=n\}|
   \]
   is not \(o(A(X))\).

Proof. Lemma 13.1j requires the first prefix vertex \(u_1\) to have a
genuine pair witness with every later vertex \(p\in P_1\). Apply
Corollary 13.1l.2 with \(d=u_1\) and \(R=Y=P_1\). This gives (1) and (2).
Warning 8.6j gives the Sidon conclusion for certificate-free sets, so the
union of two such colors has \(O(\sqrt X)\) elements up to \(X\); adding
the finite set \(A\setminus P_1\) proves (3). Finally, if the mixed counts
between \(C_0\) and \(C_1\) were uniformly \(o(A(X))\), color the finite
exceptional set \(A\setminus P_1\) by singleton colors. Those singleton
colors are certificate-free and contribute only \(O(1)\) mixed
representations to each target. Corollary 8.6j-3 would then give the
desired infinite deletion, contradicting that \(A\) is a counterexample.
\(\square\)

## Corollary 13.1l.3a: The enumerated-Schreier first tail is impossible

No \(k=2\) counterexample can be realized by the enumerated-Schreier target
of Variant 13.1b-enum.

Proof. Corollary 13.1l.3 would give an infinite cofinite tail
\[
P_1=C_0\cup C_1
\]
where both colors are certificate-free, hence Sidon, and both colors are
reflection-recurrent in \(A\). Put
\[
E=A\setminus P_1.
\]
Since \(P_1\) is infinite, one of \(C_0,C_1\) contains at least three
elements. Lemma 8.6g'''' forbids that color from being
reflection-recurrent in
\[
A=C_0\cup C_1\cup E.
\]
This contradicts Corollary 13.1l.3. \(\square\)

Thus the enumerated-Schreier route is closed at the first-tail level. The
finite bipartite windows below remain useful diagnostics for local
obstructions, but they cannot be promoted to an infinite recurrent
two-color tail in the integers.

### Diagnostic 13.1l.4: Bipartite Sidon windows are locally compatible

The script `EXPERIMENTS/bipartite_sidon_window_search.py` searches finite
integer windows for exactly the local shape left by Corollary 13.1l.3: a
partition
\[
A=C\cup D
\]
into two certificate-free colors, a long covered interval in \(2A\), and a
mixed center with several representations from \(C+D\). With
`--max-value 16 --size 6 --limit 10`, it finds many examples. The best
window printed is
\[
C=\{11,15,16\},\qquad D=\{8,9,13\},
\]
for which
\[
2(C\cup D)
\]
contains the whole interval \([16,32]\), both colors are
certificate-free relative to \(A\), and the mixed center
\[
24
\]
has three representations:
\[
24=11+13=15+9=16+8.
\]
The enhanced output also prints the minimum exact matching sizes for the
cross-residual graphs \(C+C+D\) and \(D+D+C\) across the covered interval.
For the displayed top windows these minima are
\[
(0,0),
\]
so the examples satisfy the mixed-spike condition but not the stronger
cross-residual matching hypothesis from Lemma 8.6j-7a.
Sorting by matching strength with
`--sort matching --max-value 20 --size 8` still leaves the per-color minima
at \((0,0)\), though the best-color minimum is \(1\): each target in the
covered interval has a cross-residual edge from at least one color, but no
single color supplies such edges throughout the interval.
The same diagnostic now prints
`unique_star=(count,d,t,rows)`, where \(t-\text{rows}\subset A\) and every
row \(s+d\) is uniquely represented in \(2A\). For the top six-point
window above it gives
\[
(5,16,24,\{9,11,13,15,16\}),
\]
so the unique-gate branch isolated in Corollary 13.1l.5 is also locally
compatible.

Thus the bipartite recurrent-Sidon obstruction is not finitely
inconsistent. A final contradiction must use the infinite quantitative
requirements: cofinite order-2 coverage, recurrence at unbounded centers,
the Schreier barrier links, or threshold control for infinite deletions.

## Corollary 13.1l.5: Schreier two-color stars are unique-gate

In any \(k=2\) counterexample realized by the enumerated-Schreier target of
Variant 13.1b-enum, let
\[
P_1=C_0\cup C_1
\]
be the cofinite two-color tail from Corollary 13.1l.3. Then, after
protecting any finite
\[
E\supset A\setminus P_1,
\]
the low-count-star alternative from Corollary 3.4t cannot occur in its
shifted-overlap branch for all sufficiently large witnesses. Consequently,
for every such \(E\), the unique-gate branch of Corollary 3.4t occurs for
arbitrarily large \(w\): there are
\[
d\in A\setminus E,\qquad t=w-d,
\]
and
\[
S\subset A\setminus E,\qquad |S|\gg_E A(w),
\]
such that
\[
t-S\subset A\setminus E
\]
and
\[
r_{2,A}(s+d)=1\qquad(s\in S). \tag{1}
\]

Proof. Replace \(E\) by a larger finite set \(E'\) containing both \(E\)
and the finite exceptional set from Corollary 3.4t. Since
\(A\setminus E'\subset P_1\), every element outside \(E'\) has one of the
two Sidon colors \(C_0,C_1\).

Suppose the shifted-overlap branch of Corollary 3.4t occurs with distinct
\[
d,f\in A\setminus E'
\]
and packet \(S\). Put
\[
h=d-f\ne0.
\]
That branch gives
\[
S+h\subset A,\qquad t-S\subset A.
\]
Because \(S\) and \(t-S\) lie outside \(E'\), and only \(O_{E'}(1)\)
elements of \(S\) can have \(s+h\in E'\), discarding those rows lets us
apply Lemma 8.6j-7d. Hence
\[
|S|\le 10+O_{E'}(1).
\]
But Corollary 3.4t supplies
\[
|S|\ge\eta_{E'} A(w)
\]
for a fixed \(\eta_{E'}>0\), and \(A(w)\to\infty\). Hence the
shifted-overlap branch is impossible for all sufficiently large such
witnesses. Since Corollary 3.4t gives arbitrarily large witnesses in one
of its two branches, the unique-gate branch must occur arbitrarily often.
\(\square\)

Thus the enumerated-Schreier obstruction has lost the moving
shifted-overlap escape. Its remaining low-count stars must be genuinely
unique rows \(s+d\), with no alternate deleted color \(f\) shifting a
positive-density packet back into \(A\).

## Corollary 13.1l.6: The unique-gate branch has two color subbranches

Keep the hypotheses of Corollary 13.1l.5, and write the cofinite tail as
\[
P_1=C_0\cup C_1.
\]
After enlarging the protected finite set, for every remaining unique-gate
packet
\[
d,\quad t,\quad S
\]
from Corollary 13.1l.5, all but \(O(1)\) elements \(s\in S\) satisfy
\[
s\in C_i\quad\Longrightarrow\quad t-s\in C_{1-i}. \tag{1}
\]
Consequently, after passing to a positive proportion of \(S\), one of the
following two alternatives holds, where \(d\in C_\delta\).

**Same-color unique branch.** There is a packet
\[
S'\subset C_\delta,\qquad |S'|\gg_E A(w),
\]
such that
\[
t-S'\subset C_{1-\delta}
\]
and
\[
r_{2,A}(s+d)=1\qquad(s\in S').
\]

**Mixed degree-one branch.** There is a packet
\[
S'\subset C_{1-\delta},\qquad |S'|\gg_E A(w),
\]
such that
\[
t-S'\subset C_{\delta}
\]
and
\[
r_{2,A}(s+d)=1\qquad(s\in S').
\]

Proof. For a fixed color \(C_i\), if two distinct unordered pairs
\[
\{s,t-s\}
\]
with \(s,t-s\in C_i\) occurred, they would give two same-color
representations of the sum \(t\), contradicting Sidonicity of \(C_i\).
Thus at most two values of \(s\) per color fail the color-flipping relation
(1). Discarding those \(O(1)\) rows, split the remaining packet according
to whether \(s\) has the same color as \(d\) or the opposite color. One of
the two classes has positive proportion, giving the two alternatives.
\(\square\)

This leaves two different unique-row mechanisms. In the same-color branch,
the rows \(s+d\) are same-color Sidon sums with no opposite-color
two-sum collision. In the mixed branch, they are mixed sums of degree one
in the bipartite representation graph.
In the actual cofinite recurrent two-color setting of Corollary 13.1l.3,
Corollary 8.6g''''.1 bounds either subbranch by \(2\); the split remains a
useful finite diagnostic, not a viable infinite escape.

### Diagnostic 13.1m: High-excess pair starts push the filler problem upward

Corollary 13.1l does not say that a finite first-prefix pair edge must be
low-excess impossible. The mode
`schreier_stage_search.py --pair-edge-search` searches directly for
extensions of the P5 seed
\[
S=\{1,2,4,5,8,10,15,18,19,30\}
\]
with a pair-private dominated hole for \(\{10,p\}\), allowing witnesses
\[
w=p+u
\]
well above the low-excess range. With
`--max-p6 40 --max-u 60 --max-nodes 20000 --max-found 2`, it finds
\[
p=37,\quad u=32,\quad w=69,
\]
using fillers
\[
\{40,41,44,51,54,55,58\},
\]
and also
\[
p=37,\quad u=43,\quad w=80,
\]
using fillers
\[
\{40,41,51,52,55,62,65,66,69\}.
\]
In both cases the two-sum coverage reaches the witness, and the pair edge
\(\{10,37\}\) has the required local witness. But when all numerical
fillers at least \(10\) are treated as protected vertices, the
complete-prefix-link test has no supported order. Even if those fillers are
delayed, the core vertices
\[
\{10,15,18,19,30,37\}
\]
already have no supported order: both displayed extensions fail at
\[
\{15,18,37\},\quad \{15,19,37\},\quad
\{15,30,37\},\quad \{18,19,30,37\}.
\]
For the three rank-three edges
\[
\{15,18,37\},\quad \{15,19,37\},\quad \{15,30,37\},
\]
the failure is complete poisoning: every candidate in the covered interval
already lies in
\[
3(A\setminus F).
\]
The rank-four edge has non-poisoned candidates, but they fail
inclusion-minimal repair for one of the deleted vertices.
Promoting the fillers only adds further pair-link failures; in the first
extension, \(10\) has failed pair links to every filler
\[
40,41,44,51,54,55,58.
\]

Thus high excess repairs the first pair edge only by creating a larger
debt: many fillers must be delayed in the Schreier enumeration, and
Corollary 13.1l then applies again when any one of them is eventually
promoted. This is still finite evidence, but it sharpens the remaining
construction target. A viable enumerated-Schreier lift must build a
hierarchy in which first-prefix pair excess diverges at each promoted
level without the required fillers becoming an unlinked tail.

### Warning 13.1n: Mirrored packets leave promoted-mirror debt

The construction-side version of Lemma 8.4c is concrete. For a finite
Schreier edge \(F\), a witness \(w\), and a finite retained test set
\[
T\subset A\setminus F,
\]
one can try to choose a private coloring
\[
\chi:T\to F
\]
and add mirror fillers
\[
q_e=w-e-\chi(e)\qquad(e\in T).
\]
The Lemma 8.4c row condition then becomes
\[
q_e\in A\setminus F,\qquad e+\chi(e)\notin2(A\setminus F). \tag{1}
\]
If every \(f\in F\) occurs as some color \(\chi(e)\), restoring any one
deleted element \(f\) repairs the hole through
\[
w=f+e+q_e.
\]
Thus mirrored Sidon packets can satisfy the private-incidence matrix
row-by-row, at least as a finite affine-avoidance problem.

The debt appears when a filler \(q_e\) is later promoted into the protected
tail. For any old retained endpoint \(p\), Lemma 13.1h says that if an
interval of shifted values is already absorbed,
\[
[q_e-p,R-p]\subseteq2(A\setminus\{d,q_e\}),
\]
then every candidate witness up to \(R\) for the pair \(\{d,q_e\}\) is
poisoned by \(p+2(A\setminus\{d,q_e\})\). A staged mirrored-packet
construction must therefore put each promoted mirror into a new buffer
beyond all old poison intervals. A single block that merely protects its
own mirrors does not iterate; the promoted mirrors become the next
complete-prefix-link problem.

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
Suppose further that there is a hypergraph \(\mathcal F\) on \(A\), all of
whose edges are finite nonempty sets, and, for every \(F\in\mathcal F\), a stage
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

For \(k=2\), this is Proposition 13.1b. Unlike the earlier finite-uniform
formulation, this version also covers Schreier-type barriers whose edge
sizes are unbounded. For \(k=3\), the robust-booster pair-stage searches are
attempts to realize this criterion with \(\mathcal F\) consisting of
cross-stage pairs.

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

The high-rank version of the obstruction is visible in finite residue
models. The script `EXPERIMENTS/finite_barrier_hypergraph.py` constructs
the hypergraph of finite deletions \(F\subset S\) for which
\((k+1)(S\setminus F)\) is not the whole residue group. In
\(\mathbb Z/5\mathbb Z\), with
\[
S=\mathbb Z/5\mathbb Z,
\]
every singleton and pair deletion is harmless at order \(3\), but every
triple deletion is bad: the complement has two residues, and a three-fold
sumset of two residues has at most four elements. Thus the bad triples form
a complete rank-3 finite barrier. This is only a residue model, since
integer lifts can repair deleted residue representatives, but it confirms
the barrier shape suggested by Reduction 0: a negative construction may
need genuinely high-rank finite edges rather than singleton or pair
private witnesses.

The script `EXPERIMENTS/collective_rank_search.py` gives an integer-window
analogue. Its first rank-3 example is the interval
\[
A=\{1,2,3,4,5,6,8,9\},
\]
whose two-sums cover \([2,18]\). Every singleton and pair deletion still
covers \([9,18]\) by three-fold sums, but several triple deletions create
holes in that window. This is not a construction, but it supplies a finite
test bed for any proposed high-rank barrier mechanism without relying on
holes beyond the finite two-sum coverage interval.

The same script finds a rank-4 analogue under slightly larger bounds:
\[
A=\{1,2,3,4,5,6,8,9,10,11\},
\]
whose two-sums cover \([2,22]\). On the window \([12,22]\), every deletion
of size \(<4\) still gives three-fold coverage, while several four-point
deletions create holes. Thus finite collective barriers persist beyond the
first triple examples. The unresolved issue is still global: an infinite
counterexample would need these finite barriers to form an unbounded
barrier met by every infinite deletion, with witnesses frozen below later
stages.

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
A bounded non-greedy DFS gives the same qualitative picture: with increments
of size at most \(3\), candidate values up to \(100\), and the two-point
buffer imposed, the best chain has depth \(2\), for instance adding
\[
\{4,11\}
\]
and then
\[
\{18,21\}.
\]
Thus the observed stall is not only an artefact of the first greedy
singleton choices in the smallest range.

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

### Diagnostic 16.1: The robust-booster third stage is domination-limited

In the cross-stage pair search after the two successful stages, the current
data are
\[
C=\{1,3,20,21,23,30,31\},\qquad f=5,\qquad N=40.
\]
For the residue-restricted singleton candidates checked by
`EXPERIMENTS/robust_booster_pair_stage_search.py --diagnose`, only
\[
b=41,\qquad b=43
\]
extend three-fold coverage with the required two-point buffer. For both
candidates, the pair witnesses exist only for the old elements \(20\) and
\(30\); they fail for
\[
1,\ 3,\ 21,\ 23,\ 31.
\]
Thus the first obstruction to continuing the robust-booster lift is not a
coverage endpoint failure. It is the inability of one new element to carry
simultaneous order-4 private witnesses against many old elements. This is
the same collective-barrier pressure as in the \(k=2\) Schreier route,
rather than a pure singleton-booster phenomenon.

A bounded non-greedy DFS with candidate values up to \(110\), increments of
size at most \(3\), and slack \(100\) also reaches only depth \(2\). Wider
enumeration shows several alternative first moves and some alternative
second moves, but the tested branches still have no third extension. This
keeps the robust-booster pair route open only as a genuinely large-block or
new-design problem, not as a small non-greedy search miss.

## Attempt 17: Finite accelerators are not a shortcut

One tempting higher-order negative route is to begin with a strongly
minimal order-\((k+1)\) basis \(M\), add a finite accelerator \(F\), and
hope that
\[
A=M\cup F
\]
is an order-\(k\) basis while every infinite deletion from \(M\) still
destroys order \(k+1\). This does not follow from minimality of \(M\).

If \(B\subset M\), then
\[
(k+1)((M\setminus B)\cup F)
=\bigcup_{r=0}^{k+1}\bigl(rF+(k+1-r)(M\setminus B)\bigr). \tag{1}
\]
Thus a witness \(w\notin(k+1)(M\setminus B)\) supplied by the minimality of
\(M\) survives in \(A\setminus B\) only if, for every \(r\)-term accelerator
sum \(\sigma\in rF\),
\[
w-\sigma\notin(k+1-r)(M\setminus B). \tag{2}
\]
Condition (2) is much stronger than ordinary infinite-deletion minimality
of \(M\); it is the same shifted-hole requirement that appears in Lemma
10.1 and in the staged barrier criteria.

Example 7.2 shows that finite accelerators can lower the apparent order by
an arbitrarily large amount, but that example is eventually periodic and is
covered by Proposition 7.1. Lemmas 6 and 6.1 explain why a purely residue
version of this shortcut also fails: residue accelerators create
\((k+1)\)-term repairs involving the accelerator, while thick integer lifts
replace a deleted representative by another representative except near
block endpoints.

Therefore a finite-accelerator counterexample would need an
\(F\)-robust minimal basis \(M\): every infinite deletion would have to
produce unbounded witnesses surviving all shifted repairs (2). That is not
a separate shortcut; it is another form of the unresolved collective
finite-barrier construction in Propositions 13.1b-general and 13.1e.

## Dependency Graph

* Reduction 0 shows that the stated infinite-deletion minimality hypothesis
  is redundant for counterexamples. The problem is equivalent to the broader
  assertion that every order-\(k\) asymptotic basis has an infinite deletion
  that remains order \(k+1\).
* The co-infinite order-\(k\) subbasis split in Reduction 0 handles every
  basis containing a co-infinite order-\(k\) subbasis. Hence the only
  remaining hard case of the broad theorem is the original
  infinite-deletion-minimal case.
* Theorem 1 is independent and resolves \(k=1\).
* Lemma 2 would imply the desired conclusion if an infinite \(B\) satisfying
  the two absorption hypotheses can be forced.
* Lemma 2.2 gives the general multi-hit repair criterion: a fixed retained
  padder may absorb any multiset of at most \(k\) deleted summands.
* Theorem 2.3 proves that finite reflection-recurrence gives a good infinite
  deletion in every order, using balanced repair certificates.
* Lemma 2.3b isolates the exact fixed-data version: one recurrent
  certificate tuple \(e,y_1,\ldots,y_k\), satisfying the balanced affine
  identities, is already enough for the protected-reservoir deletion.
* Corollary 2.3c records the direct \(k=2\) fixed-triple version:
  recurrence of \(\{e,y_1,y_2\}\) plus \(y_1+y_2-e\in A\) gives a good
  order-3 deletion.
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
* The finite-core finite-deletion stability target in Reduction 0 separates
  genuine finite fatal deletions from delayed finite-prefix holes. It is not
  refuted by the current examples, and even if true would still require
  Lemma 3.1d-style common threshold control.
* Lemma 3 would imply the desired conclusion if an infinite late-deletable
  reservoir exists.
* The paragraph after Lemma 3 records that this reservoir criterion is
  equivalent to the existence of a good infinite deletion; failure is exactly
  a barrier of late-bad successors.
* Corollary 3.1 says any counterexample must eventually block all large
  late-deletable one-point removals at order \(k+1\).
* Corollary 3.1b reformulates the threshold obstruction as late-bad finite
  prefixes.
* Corollary 3.1c says the late-bad finite sets must form a barrier on \(A\)
  in any counterexample.
* Lemma 3.1c.1 turns any weak late-bad barrier into a prefix-front of
  late-bad supersets. The conversion preserves the maximal element and
  genuine holes, but may lose inclusion-minimal private-incidence structure.
* Lemma 3.1c.2 recovers the most important part of that structure: for a
  first-prefix front edge, any sufficiently late inclusion-minimal shrink
  must keep the last front point, so that point is active in the terminal
  gap normal form.
* Corollary 3.1c.3 replaces padded prefix-front edges by their active
  traces. These traces are themselves a weak late-bad barrier; hence
  surviving variable rank must occur in active holes, not just in inactive
  prefix filler.
* Lemma 3.1d gives an exact fixed-deletion test: \(A\setminus X\) is an
  order-\(h\) basis if and only if all finite deletions inside \(X\) have a
  common order-\(h\) threshold.
* Lemma 3.1e says that, under finite-core finite-deletion stability, any
  remaining counterexample must be purely delayed: finite deletions are
  eventually repaired, but every infinite tail contains finite subdeletions
  whose thresholds start at or beyond the deleted block.
* Corollary 3.1e' sharpens this to an inclusion-minimal collective delayed
  barrier normal form. For \(k=2\), after finitely many singleton
  exceptions are protected, the delayed barriers all have size at least
  two.
* Proposition 3.1f proves finite-core finite-deletion stability and the
  desired infinite deletion for every basis containing a tail-syndetic
  subset. It uses Lemma 10.3 to rule out terminal gaps after finite
  deletions.
* The contrapositive of Proposition 3.1f says every counterexample has no
  tail-syndetic subset; every infinite subset of \(A\) has arbitrarily long
  tail gaps.
* Lemma 3.2 proves the theorem under an arbitrarily-large protected matching
  hypothesis for \((k+1)\)-representations.
* Corollary 3.3 converts failure of the broad positive theorem into bounded
  moving transversals for representation hypergraphs.
* Lemma 3.3a records the exact first-moment random-thinning criterion:
  independent deletion works if minimal transversals are summable, but this
  is precisely an anti-barrier condition and does not bypass complete-pair or
  Schreier-type collective obstructions.
* Corollary 3.3b turns those bounded transversals into bounded-size
  terminal-gap holes outside any prescribed finite protected core.
* Proposition 3.4 proves the conclusion for bases with sufficiently
  redundant \((k+1)\)-representations.
* Corollary 3.4b applies this to bounded order-\(k\) representation
  functions. Any order-\(k\) basis whose \(k\)-term representation counts
  are uniformly bounded has a good infinite deletion; in particular, a
  \(k=2\) counterexample cannot be a bounded-representation/Sidon-type thin
  basis.
* Lemma 3.4b' gives the shifted version needed for quotient/copy
  constructions: bounded order-\(k\) multiplicity gives an infinite
  \(T\subset S\) with \(k(S\setminus T)+S\) cofinite.
* Corollary 3.4c strengthens this from bounded multiplicity to
  \(R_k(X)=o(A(X))\), where \(R_k(X)\) is the maximum \(k\)-term
  representation count up to \(X\). Thus a counterexample needs
  representation spikes comparable to its counting function.
* Corollary 3.4d localizes those spikes: after any finite core is
  protected, a counterexample has arbitrarily large targets \(n\) and an
  unprotected summand \(x\) for which \(n-x\) has \(\gg A(n)\)
  \(k\)-term representations.
* Warning 3.4e shows that large moving representation spikes do not by
  themselves imply finite reflection-recurrence; the benign basis
  \(\{1\}\cup2\mathbb N\) has maximal two-sum spikes but no recurrent
  center for \(\{1,2\}\).
* Lemma 3.4f gives the usable form of spike recurrence: if the large
  reflected clusters \(U_n=A\cap(n-A)\) repeatedly overlap one finite
  certificate-dense test set, then a fixed recurrent certificate triple
  appears and Corollary 2.3c gives a good deletion. The escaping-block
  model after it explains why large spikes alone do not guarantee this.
* Corollary 3.4g combines bounded transversals with the padded edge lower
  bound in the \(k=2\) case: every counterexample has arbitrarily late
  finite holes where one deleted element gates \(\gg A(w)\) retained
  two-sum repairs of the witness.
* Corollary 3.4h strengthens the private-color consequence for star gates:
  every retained repair summand \(a\) has \(a+d\notin2(A\setminus D)\) and
  full representation count \(r_{2,A}(a+d)\le |D|\), with no threshold or
  deleted-pair exceptions.
* Corollary 3.4i strengthens this after the singleton-exceptional core is
  protected: the star gate can be chosen inside an inclusion-minimal
  collective hole of bounded size, so every deleted vertex is active and
  individually order-3-good.
* Corollary 3.4j packages the remaining star obstruction as a reflected
  low-count translate slice: for arbitrarily large \(w\), a moving
  \(d\notin E\) sends \(\gg_E A(w)\) points of
  \(A\cap(w-d-A)\) into bounded two-sum representation values.
* Warning 3.4k shows that reflected low-count slices are not contradictory
  in arbitrary order-2 bases: \(\{1\}\cup2\mathbb N\) has large slices
  pinned by the element \(1\).
* Lemma 3.4l shows that finitely pinned low-count rows cannot support the
  star obstruction after the pins are protected. A remaining counterexample
  must have unpinned bounded-count translate rows outside every finite core.
* Corollary 3.4m gives the corresponding positive criterion for \(k=2\):
  if one finite pin set accounts for all large bounded-count two-sums, then
  the desired infinite deletion exists.
* Corollary 3.4n makes the remaining unpinned obstruction explicit: outside
  every finite core, a fresh gate \(d\) has \(\gg_E A(w)\) fresh reflected
  neighbours \(a\) with \(r_{2,A}(a+d)\) bounded.
* Corollary 3.4o is the matching positive criterion: a uniform exclusion of
  fresh reflected low-count stars after one finite core gives a good
  deletion.
* Warning 3.4p gives finite local star gadgets outside any prescribed core,
  showing that Corollary 3.4o needs global tail or minimal-hole input.
* Corollary 3.4q gives a simpler graph-degree version: if bounded-count
  translate neighbours have \(o(A(X))\) initial-segment degree uniformly in
  the center after one finite core, then the desired deletion exists.
* Corollary 3.4r packages the surviving obstruction as a large reflected
  packet \(S\) with only \(O(|S|)\) solutions to \(x+y=s+d\) inside \(S\).
* Corollary 3.4s splits star rows into unique-private rows for the moving
  gate or shifted-overlap rows coming from another deleted vertex.
* Corollary 3.4t turns this into the current two-branch normal form:
  remaining counterexamples must have either large unique-gate reflected
  packets or large shifted-overlap reflected packets.
* Warning 3.4u shows that shifted-overlap packets are locally compatible,
  so the shifted branch also needs global input.
* Corollary 3.4v records the branch-specific recurrence collapse: fixed
  shifted-overlap rows, or a fixed certificate triple inside either side of
  the reflected packet, already give the desired deletion by Corollary 2.3c.
  Thus the remaining obstruction is genuine mass escape.
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
* Proposition 7.1 applies the syndetic-tail criterion to prove finite-core
  finite-deletion stability, and hence the desired conclusion, for all
  eventually periodic asymptotic bases.
* Corollary 7.1b extends this to every basis containing an eventually
  periodic order-\(k\) subbasis.
* Lemma 8 gives a necessary condition for one-point deletion to fail at
  order 3 in an order-2 basis.
* Corollary 8.1 says infinitely many such failures force finite
  reflection-recurrence of \(A\).
* Lemma 8.2a isolates the repair criterion used to turn a carefully chosen
  infinite deletion into an order-3 basis.
* Lemma 8.2a' gives a moving-anchor bridge variant: a fixed padder \(t\)
  can be connected to moving anchors \(e_j\) by bridges
  \(t+b_j=e_j+q_j\), provided the old-anchor rows \(e_j+b_i\in2C\) hold.
* Warning 8.2b records why the most direct fixed-center greedy use of
  Lemma 8.2a does not close the remaining \(k=2\) case: a finite prefix can
  create fixed-center or star-shaped old-new obstructions not covered by
  the singleton and cofinite-tail pair-barrier theorems.
* Lemma 8.2c shows that a pure star around one fixed old element actually
  forces tail reflection-recurrence; the unresolved greedy obstruction is
  the finite-prefix multi-center version, which gives only fractional
  recurrence.
* Lemma 8.2c' gives the bounded pair-private analogue: a fixed lower
  endpoint with uniformly low-top-excess pair witnesses over arbitrary
  finite tail tests also forces tail reflection-recurrence.
* Lemma 8.2c'' extends this to fixed-singleton finite barriers: if all
  moving deleted endpoints are above the shifted rows because the witness
  is close to their minimum, the fixed endpoint reflects the whole tail.
* Lemma 8.2c''' gives the intermediate endpoint version: closeness to the
  \(j\)-th moving endpoint yields \(1/j\)-fractional recurrence, closing
  only when large fractional subsets force certificates.
* Lemma 8.2d gives the matching certificate-forcing statement for
  multi-center fixed-prefix stars; persistent star obstructions must again
  live in the large certificate-free subset regime.
* Lemma 8.2e applies the same certificate-forcing mechanism to fixed-core
  delayed-singleton barriers, splitting the moving color into bounded- and
  unbounded-excess regimes.
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
* Lemma 8.4c adds a second necessary condition for collective holes: every
  retained padder below the witness either leaves \(w-e\) as a deleted-pair
  sum or has a private deleted-retained sum \(e+f\notin2(A\setminus F)\).
  This rules out direct Schreier lifts whose retained tail absorbs
  \(T+F\) back into \(2(A\setminus F)\).
* Corollary 8.4c.1 quantifies that no-go: if \(T+F\subseteq2(A\setminus F)\)
  for an active retained test set \(T\), then \(|T|\le|F+F|\). This kills
  fixed-rank absorptive lifts with arbitrarily large tests, but not
  Schreier-scale ranks where the active prefix can be only linear in
  \(|F|\).
* Lemma 8.4d converts private colors into a rank-sensitive low-matching
  obstruction: if \(|F|=r\), a color \(f\) can serve \(t\) only when
  \(t+f\) has fewer than \(r\) disjoint two-term representations avoiding
  \(f\). The notes after it record why this is only a capacity obstruction,
  not a Hall matching theorem, and why \(F+F\) exception rows matter at
  Schreier scale.
* Warning 8.4e shows that these low-count rows can be cofinite in the
  infinite part of an order-2 basis, even simultaneously for every
  \(f\) in a prescribed finite set. Thus Lemma 8.4d is useful only when
  combined with non-sparse redundancy, dense intervals, or additional
  structure beyond order-2 coverage.
* Proposition 8.4f consolidates the remaining \(k=2\) counterexample
  normal form: every infinite tail must contain an inclusion-minimal
  collective hole with a terminal gap and a private-color/low-count
  incidence for every active finite test row, except for deleted-pair
  exception rows.
* Warning 8.5 records that bounded-width barriers do not automatically
  reduce to one fixed uniformity, and that abstract barriers need not have
  bounded width on any infinite tail.
* Lemma 8.5a says that if bounded width is supplied by arithmetic, Ramsey
  thinning reduces the late-bad barrier to one fixed uniformity on an
  infinite tail.
* Warning 8.5a.1 shows that the closed first-Schreier target is not a
  universal model for unbounded barriers: second-order Schreier fronts are
  still barriers but contain no pair-level first-prefix links on any tail;
  the second-element front shows rank may be controlled by later points.
  The remaining abstract target is recursive front-section descent plus
  arithmetic input.
* Lemma 8.5a.2 supplies the basic recursive tool: proper sections of a
  front are fronts on the tail. The missing step is preserving the
  arithmetic private-incidence normal form under this descent.
* Lemma 8.5a.3 supplies the corresponding arithmetic bounded-depth tool:
  if a fixed front node plus the first \(j\) moving endpoints have bounded
  excess to the \(j\)-th moving endpoint, then every finite test has a
  \(1/(|\Delta|+j)\)-fraction reflected by one center; certificate density
  then gives a good deletion.
* Corollary 8.5a.4 rules out coherent bounded-depth endpoint list-coloring:
  finite section-depth palettes compact to recurrent Sidon colors, again
  impossible by Lemma 8.6g''''.2.
* Lemma 8.5b rules out complete fixed-rank barriers on a cofinite tail with
  bounded top excess \(w_F-\max F\); terminal gaps would force
  \(A(X)=O(\log X)\), contradicting order-2 basishood.
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
* Warning 8.6c' shows this certificate obstruction can occur inside a
  harmless order-2 basis: one can add arbitrarily large recurrent clusters
  that avoid all fixed-triple certificates \(y_1+y_2-e\in A\).
* Example 8.6d shows that unbounded second-excess minimal collective holes
  are locally compatible with strong order-2 minimality and singleton
  order-3 stability; any bounded-second-excess reduction must use the
  global barrier hypothesis over every infinite deletion.
* Warning 8.6f records that in the no-tail-syndetic case left by
  Proposition 3.1f, ordinary \(A\)-gaps already mimic the terminal windows
  from Lemma 8.4a; the unresolved obstruction is the shifted two-sum
  vertex-cover condition, not gap existence.
* Warning 8.6f' rules out a natural alternating-deletion shortcut: even if
  the deletion set has no consecutive elements in the \(A\)-order, finite
  collective holes can have singleton terminal windows and still satisfy
  shifted domination.
* Lemma 8.6g uses that vertex-cover condition: fixed-rank large-excess
  barriers plus one finite test set with no large certificate-free subset
  force a recurrent certificate triple and hence a good deletion. The
  rank-sensitive paragraph after it says variable-rank barriers can evade
  this only by outrunning the certificate-density ratio of every finite test
  set.
* Corollary 8.6g.1 rules out the full-list fixed-rank escape: if every
  finite test could be split into endpoint-certificate-free fibers with
  unbounded endpoint centers, compactness would produce finitely many
  recurrent Sidon colors, contradicting Lemma 8.6g''''.2.
* Warning 8.6g.2 explains why the obvious variable-rank escape is not
  enough: deleting full shifted coverage neighborhoods makes fibers tiny,
  but proper subedges are repaired by any retained member of the omitted
  neighborhood, so the bad sets are selector-avoidable block cuts unless
  additional cross-block coding is supplied.
* Lemma 8.6g' sharpens the pair-barrier case from large certificate-free
  halfsets to endpoint list-colorings: pair holes force a recurrent
  certificate unless the shifted endpoint lists can split every finite test
  set into two certificate-free fibers.
* Lemma 8.6g'' compactifies the surviving list-colorable pair obstruction:
  if it persists for every finite test set, then \(A\) has a global
  two-coloring into certificate-free classes, and each color is separately
  reflection-recurrent in \(A\).
* Lemma 8.6g''' adds that these recurrent colors must reflect almost across
  colors: same-color mirrors would create nontrivial Sidon collisions.
* Lemma 8.6g'''' turns that almost-cross-color recurrence into an integer
  contradiction: two recurrence centers for the same three source points
  force a Sidon collision in the opposite color. Hence the persistent
  list-colorable pair obstruction from Lemma 8.6g'' is impossible.
* Corollary 8.6g''''.1 is the packet-level version: a cross-reflected
  packet \(S\subset C\), \(t-S\subset D\), has size at most two when the
  target Sidon color \(D\) is recurrent.
* Lemma 8.6g''''.2 generalizes this to any finite Sidon coloring: in a
  \(q\)-color partition up to finite exceptions, a recurrent color has at
  most \(q\) elements. Hence no finite certificate-free coloring of a
  cofinite tail can make all colors recurrent.
* Warning 8.6g'''a shows only the finite quotient shadow of this shape:
  one center can swap two two-point colors modulo \(6\), but this does not
  lift to arbitrarily many integer centers for a three-point test set.
* Lemma 8.6h supplies such finite test sets when \(A\) contains long
  arithmetic progressions; Warning 8.6i shows the corresponding
  certificate-density statement is not a finite quotient consequence of
  residue-level order-2 coverage.
* Warning 8.6j says certificate-free color classes are Sidon, which gives
  only an \(O(\sqrt X)\) counting bound and therefore does not contradict
  thin order-2 bases.
* Lemma 8.6j' strengthens this: each certificate-free color has its
  same-color sums disjoint from its mixed sums with the rest of \(A\).
* Warning 8.6j-2 records the limit of that separation: in two colors, the
  two same-color sumsets may still overlap.
* Lemma 8.6j-4 identifies mixed representation spikes with reflected Sidon
  difference packets in the mixed support.
* Lemma 8.6j-5 says the mixed support is not cofinite as soon as one
  certificate-free color is infinite, because same-color sums are unbounded
  and disjoint from mixed sums.
* Corollary 8.6j-3 connects certificate-free colorings back to the
  representation-count criteria: if all mixed-color two-sum counts are
  sublinear relative to \(A(X)\), Corollary 3.4c gives a good deletion.
  Hence any certificate-free counterexample needs large mixed spikes.
* Warning 8.6j'' shows that a universal certificate-density theorem would
  reach the Sidon-basis frontier. A hypothetical Sidon order-2 basis can be
  copied into two certificate-free residue classes, although the resulting
  order-2 basis still has bounded representation multiplicity and is handled
  by Corollary 3.4b. The exact failed counterexample condition is the
  stronger shifted requirement \(2(S\setminus T)+S\) non-cofinite after
  every infinite deletion \(T\subset S\).
* Lemma 8.6j-6 proves that this shifted Sidon-copy requirement fails for
  every quotient basis with bounded two-sum multiplicity: there is an
  infinite \(T\) for which \(2(S\setminus T)+S\) is cofinite.
* Lemma 8.6j-7 gives the corresponding one-color graph alternative:
  failure of the shifted deletion inside a certificate-free color forces
  bounded moving transversals, and if the graphs have many edges those
  transversals create mixed-color degree spikes.
* Lemma 8.6j-7a gives the direct cross-residual matching criterion:
  arbitrarily large matchings in \(C+C+(A\setminus C)\) representation
  graphs allow a sparse deletion from \(C\) that leaves an order-3 basis.
* Lemma 8.6j-7b identifies the complementary star branch with the existing
  low-count-star normal form: same-color rows in a two-color
  certificate-free tail have uniformly bounded representation count.
* Warning 8.6j-7c explains why separate recurrence does not force the
  matching branch: it naturally creates high-degree moving stars, and
  certificate-freeness blocks non-star same-residual edges.
* Lemma 8.6j-7d adds a useful two-color Sidon constraint: a packet cannot
  be simultaneously translated by a nonzero \(h\) and reflected by a center
  \(t\) in a cofinite two-color certificate-free tail, except for \(O(1)\)
  rows. The two maps flip colors and then create too many same-color
  representations of \(t+h\).
* Lemma 8.6j-7e gives the corresponding exception-window refinement:
  same-color \(F+F\) exception rows in a two-color certificate-free tail
  have only \(O(|F|)\) incidences, leaving only color-flipping star-like
  exception patterns as a possible large obstruction.
* Warning 8.6j-8 explains why the resulting cross-color reflected packets
  do not directly trigger Corollary 2.3c: the moving certificate value is
  the natural deleted mirror.
* Warning 8.6j-9 records the corresponding repair-identity obstruction:
  deleting mirrors \(m_i-t\) and repairing pairs with one mirror from each
  center requires a fixed certificate \(y_1+y_2-t\in A\).
* Corollary 8.6k uses the Sidon bound to rule out fixed-rank large-excess
  barriers in order-2 bases with \(|A\cap[1,X]|/\sqrt X\to\infty\), while
  noting that sparse fixed-rank tails with bounded top excess are not ruled
  out by the cofinite-tail counting lemma.
* Example 8.7 shows that pair barriers can be irreducibly multi-centered at
  the residue level, so Lemma 8.6 cannot be upgraded by a simple pigeonhole
  argument.
* Example 8.7e shows that even complete inclusion-minimal pair holes with
  active repairs can be certificate-free in a finite residue model.
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
* Lemma 10.2b proves the delayed-threshold analogue: late one-point
  deletions force full recurrence into \((k-1)A\), which again becomes
  usable reflection-recurrence only for \(k=2\).
* Warning 10.2b' shows lower-sumset recurrence can be vacuous for \(k>2\):
  \((k-1)A\) may already be cofinite while \(A\) has no finite reflection
  recurrence.
* Lemma 10.1 records the finite-vertex-cover obstruction for collective
  holes after finite deletions.
* Lemma 10.3 strengthens this for all orders: a finite
  order-\((k+1)\) hole after deleting \(F\) forces a terminal retained gap
  below the witness, starting at \(w-\min F-(k-1)\min A\).
* Lemma 10.3b combines the broad deletion reduction, the late-bad barrier
  formulation, and Lemma 10.3: every counterexample must have active
  inclusion-minimal finite terminal-gap barriers in every infinite tail,
  away from every finite protected core.
* Corollary 10.3d shows that if the stronger finite-core finite-deletion
  stability target fails, those terminal windows can be made genuine long
  gaps of \(A\) itself; `actual_gap_barrier_search.py` records a small
  finite-window model.
* Lemma 10.3e adds the prefix-coverage burden for such genuine gaps: the
  gap interval must already lie in the \(k\)-fold sumset of the prefix
  before the gap.
* Lemma 10.3f sharpens this to prefix-locality: active repairs and shifted
  representations dominated by the finite barrier use only prefix summands
  before the genuine terminal gap.
* Proposition 10.3g gives arbitrarily large interval half-deletion barriers,
  showing the prefix-local genuine-gap normal form is locally sharp.
* Lemma 10.3h classifies the coverage-compatible terminal-gap barriers
  inside those interval blocks: they are threshold cuts of size at least
  half the high block, so the interval gadget cannot by itself supply
  fixed-rank or Schreier-type coding.
* Warning 10.3i adds that interval threshold cuts are not deletion barriers
  by themselves: disjoint block cuts can be avoided by an infinite selector,
  so a counterexample must still code a genuine cross-block finite-set
  barrier on individual elements.
* Warning 10.3c gives an abstract Schreier-barrier representation model
  showing why compactness, Zorn, finite-prefix, and independent random
  deletion arguments need genuine additive input.
* Lemma 10.4 records the higher-order analogue of bounded second-excess
  barriers: they force large reflected subpatterns into lower sumsets
  \((k-1)A\), which becomes full recurrence only when \(k=2\).
* Example 11 gives a residue-padding family satisfying the desired
  conclusion for every \(k\ge2\).
* Attempt 12 records that the clean direct-sum digital model satisfies the
  desired conclusion, and the standard binary Raikov-Stöhr basis has an
  explicit even-support deletion leaving an order-3 basis; a faithful
  carry-free embedding into \(\mathbb N\) is impossible.
* Attempt 13 records the staged protected-block counterexample route and
  the coverage-versus-witness-efficiency gap.
* Proposition 13.1 gives a precise finite-stage criterion that would produce
  a \(k=2\) counterexample if suitable stages can be built.
* Proposition 13.1b replaces singleton stage protection by an unbounded
  finite-barrier system, while noting that order-2 minimality then needs a
  separate proof.
* Proposition 13.1b-Schreier sharpens the remaining unbounded-rank target:
  a Schreier barrier with frozen witnesses, coverage buffer,
  inclusion-minimal activity, and shifted two-sum domination would produce a
  \(k=2\) counterexample.
* Variant 13.1b-enum notes that the Schreier barrier may use an arbitrary
  enumeration of a cofinite protected set, not necessarily the numerical
  order; this leaves delayed promotion of fillers as a possible but still
  arithmetically constrained route.
* Lemma 13.1f extracts finite forbidden windows for stage witnesses. In the
  P5 Schreier seed, the new pair edge has only one low-excess escape, and
  the full P6 failure comes from simultaneous higher-rank edge closure. The
  private-color diagnostic after it records the exact Lemma 8.4c incidence
  matrix required of any reflected-Schreier lift.
* Lemma 13.1g adds the exact inclusion-minimal repair intersection for
  finite stage holes.
* Lemma 13.1h records the retained-endpoint poison interval that kills
  whole ranges of pair-edge witness candidates.
* Corollary 13.1h.1 gives the pointwise promoted-filler version: a witness
  for a pair edge \(\{a,q\}\) must avoid \(p+2C\) for every retained old
  endpoint \(p\). The P6 protected-filler diagnostic verifies this closure
  cost in the first pair-edge escape.
* Lemma 13.1i records the low-excess private-mirror closure: pair holes
  force active rows to choose endpoint colors, and the lower endpoint can
  generate new retained mirrors above the moving endpoint.
* The P6 enumeration-order diagnostic shows that delaying only the fillers
  \(40,43,44\) does not rescue the finite P6 escape: all orders of
  \(\{10,15,18,19,30,38\}\) still have failed edges involving \(38\).
* Lemma 13.1j abstracts this into the complete-prefix-link criterion for
  finite enumerated Schreier stages: the first vertex needs complete good
  pair links, the second needs complete good triple links on the remaining
  tail, and so on.
* The bounded P6 enumeration search now also checks \(89702\) candidates
  with up to three delayed fillers through \(75\), finding no extension
  for \(p_6\le45\).
* Corollary 13.1k applies Lemma 8.2c' to those first-prefix pair links:
  uniformly low-top-excess links in the finite-test sense would give a good
  deletion, so a counterexample must use unbounded excess, non-uniform
  links, or higher-rank prefix obstructions.
* Corollary 13.1l removes the non-uniform escape for rank-2 first-prefix
  links: infinitely many bounded-excess pair witnesses for a fixed lower
  endpoint already supply Corollary 13.1k's finite-test quantifier.
* Corollary 13.1l.1 applies Lemma 8.2c'' to every fixed Schreier prefix
  level: witnesses must have unbounded excess over the first later endpoint
  on every infinite later tail.
* Corollary 13.1l.2 adds the high-excess pair consequence: fixed-prefix
  pair tails must be endpoint-list colorable on every finite test set, and
  compactness yields two recurrent certificate-free tail colors.
* Corollary 13.1l.3 specializes this to the enumerated-Schreier target:
  the first protected tail must be a cofinite union of two recurrent Sidon
  colors at critical density, with large mixed two-sum spikes.
* Corollary 13.1l.3a applies Lemma 8.6g'''' to that cofinite two-color
  tail, closing the enumerated-Schreier counterexample route at the
  first-tail level.
* Diagnostic 13.1l.4 records finite integer windows with exactly this
  bipartite certificate-free and mixed-spike shape. Its unique-star output
  also shows that the remaining unique-gate branch is locally compatible.
* Corollary 13.1l.5 combines the two-color tail with Lemma 8.6j-7d:
  the shifted-overlap branch of the low-count-star normal form is bounded
  in the enumerated-Schreier reduction, so any surviving star obstruction
  must be a large unique-gate packet.
* Corollary 13.1l.6 splits that packet by color into same-color unique rows
  and mixed degree-one rows, after discarding only \(O(1)\) non-flipping
  reflected rows; Corollary 8.6g''''.1 bounds both subbranches in the
  cofinite recurrent setting.
* Diagnostic 13.1m shows that high-excess first-pair starts are locally
  possible in the P5 seed, but only by adding fillers that immediately fail
  the next complete-prefix-link test when promoted.
* Warning 13.1n packages the construction-side reason: mirrored private
  packets can satisfy Lemma 8.4c row-by-row, but every mirror later promoted
  into the protected tail inherits new poisoned pair intervals from old
  retained endpoints.
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
  private for individual integers without losing three-term coverage, and
  robust against all shifted finite-accelerator repairs.
* Diagnostic 16.1 records that the robust-booster pair-stage lift stalls at
  the third stage because singleton candidates \(41,43\) extend coverage but
  fail simultaneous pair witnesses against many old elements; the obstruction
  is domination, not coverage alone.
* Attempt 17 records that adding a finite accelerator to a minimal
  order-\((k+1)\) basis is not a shortcut to a counterexample; the witnesses
  must survive every accelerator shift, which is again the collective
  barrier problem.
