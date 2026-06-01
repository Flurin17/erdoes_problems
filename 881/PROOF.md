# Evolving Proof or Counterexample

## Problem

Let \(A\subseteq\mathbb N\) be an asymptotic additive basis of order \(k\)
such that removing any infinite subset of \(A\) destroys the property of
being an order-\(k\) basis. Decide whether there must exist an infinite
\(B\subseteq A\) such that \(A\setminus B\) is an asymptotic additive basis
of order \(k+1\).

## Status

Complete for \(k=1\) and \(k=2\). The \(k=2\) case is closed by Theorem
13.1l.2p: after the singleton exceptional set is removed, Corollary
3.1c.3 supplies a weak barrier of nonsingleton actual active traces, Lemma
3.1c.4 thins it to an actual prefix-front, and Corollary 13.1l.2o forbids
the resulting finite-prefix weak active suffix barrier.

Open in this workspace for \(k\ge3\). The surviving higher-order question
is whether the \(k=2\) active-trace/front closure has an analogue for
\((k+1)\)-term barriers, or whether robust higher-order collective
barriers such as the staged \(k=3\) pair/booster attempts can be lifted to
an infinite basis.

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

### Lemma 3.1c.4: Weak actual barriers contain actual prefix-fronts

Let \(P\) be an infinite ordered set and let
\[
\mathcal B\subset [P]^{<\omega}\setminus\{\varnothing\}
\]
be a weak barrier: every infinite \(X\subset P\) contains some
\[
B\in\mathcal B,\qquad B\subset X.
\]
Then there are an infinite \(Q\subset P\) and a subfamily
\[
\mathcal F\subset\mathcal B\cap[Q]^{<\omega}
\]
such that \(\mathcal F\) is a prefix-front on \(Q\). In particular, if the
members of \(\mathcal B\) are inclusion-minimal active traces equipped with
witnesses, no padded supersets are introduced; \(\mathcal F\) consists of
actual traces with the same witnesses.

Proof. For an infinite
\[
X=\{x_1<x_2<\cdots\}\subset P,
\]
say \(X\in\mathcal O\) if some finite initial segment
\[
\{x_1,\ldots,x_n\}
\]
belongs to \(\mathcal B\). The set \(\mathcal O\subset[P]^\omega\) is open
in the usual product topology on increasing sequences. By the open
Galvin-Prikry theorem, there is an infinite \(Q\subset P\) such that either
every infinite \(X\subset Q\) lies in \(\mathcal O\), or no infinite
\(X\subset Q\) lies in \(\mathcal O\).

The second alternative is impossible. Since \(\mathcal B\) is a weak
barrier, the infinite set \(Q\) contains some \(B\in\mathcal B\). Then
\[
X=B\cup(Q\cap(\max B,\infty))
\]
is an infinite subset of \(Q\), and \(B\) is an initial segment of \(X\).
Thus \(X\in\mathcal O\), a contradiction.

Therefore every infinite subset of \(Q\) has an initial segment belonging
to \(\mathcal B\). Let \(\mathcal F\) be the subfamily of
\(\mathcal B\cap[Q]^{<\omega}\) consisting of those \(B\) for which no
proper initial segment of \(B\), relative to the order on \(Q\), lies in
\(\mathcal B\). Given infinite \(X=\{x_1<x_2<\cdots\}\subset Q\), choose
the least \(n\) such that \(\{x_1,\ldots,x_n\}\in\mathcal B\). The least
initial segment lies in \(\mathcal F\), and uniqueness is immediate from
least length. Hence \(\mathcal F\) is a prefix-front on \(Q\). \(\square\)

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

### Warning 8.5a.1b: Active last points do not by themselves give descent

Lemma 3.1c.2 and Corollary 3.1c.3 show that first-prefix late-bad fronts
can be replaced by active traces containing the last front point. This
removes purely inactive rank inflation, but it still does not give a
purely combinatorial section descent.

Use the second-element front
\[
\mathcal B_2=\{\{x_1<\cdots<x_m\}\subset\{2,3,\ldots\}:m=x_2\}.
\]
For
\[
S=\{x_1<\cdots<x_m\}\in\mathcal B_2
\]
write
\[
a=x_2,\qquad b=x_m=\max S,
\]
and declare the active trace to be
\[
F_S=\{a,b\}.
\]
Then every infinite
\[
X=\{x_1<x_2<\cdots\}
\]
contains the front edge \(S=\{x_1,\ldots,x_{x_2}\}\), and the associated
trace \(F_S=\{x_2,x_{x_2}\}\) contains the last front point. The remaining
points of \(S\setminus F_S\) are inactive fillers.

This model satisfies the formal conclusion of Lemma 3.1c.2, but it does
not descend to a collective hole in the suffix after the prefix point
\(a\). Once \(a\) is fixed in the prefix, the moving part of the active
trace is only the singleton \(\{b\}\), while singleton late-bad barriers
are already excluded in the remaining \(k=2\) case. A formal private-color
model can still color all inactive fillers by the moving last point \(b\),
with the color depth \(x_2-1\) escaping to infinity.

Thus active-last information narrows the obstruction but does not close it.
A final proof must rule out last-gated or unbounded-depth active traces by
arithmetic means, or else construct them coherently. Bounded-depth section
arguments such as Lemma 8.5a.3 and Corollary 8.5a.4 do not cover this
abstract pattern.

### Lemma 8.5a.2p: Prefix-front sections are prefix-fronts

Let \(P\) be an infinite ordered set. Call \(\mathcal F\) a
**prefix-front** on \(P\) if every infinite
\[
X=\{x_1<x_2<\cdots\}\subset P
\]
has a unique initial segment in \(\mathcal F\). No inclusion-antichain
condition is assumed.

Let \(s\subset P\) be a finite initial segment of some member of
\(\mathcal F\), and suppose no initial segment of \(s\) lies in
\(\mathcal F\). Put
\[
P_s=\{p\in P:p>\max s\}
\]
and
\[
\mathcal F_s=\{G\subset P_s:s\cup G\in\mathcal F\}.
\]
Then \(\mathcal F_s\) is a prefix-front on \(P_s\).

Proof. Let \(Y\subset P_s\) be infinite. The set \(s\cup Y\), ordered
increasingly, has a unique initial segment \(H\in\mathcal F\). By the
hypothesis on \(s\), the set \(H\) cannot be a proper initial segment of
\(s\). Since \(s\) itself is an initial segment of some prefix-front member, the
unique initial segment \(H\) must extend all of \(s\), so
\[
H=s\cup G
\]
for a finite initial segment \(G\) of \(Y\). Thus \(G\in\mathcal F_s\).
If \(Y\) had two initial segments \(G_1,G_2\in\mathcal F_s\), then
\[
s\cup G_1,\qquad s\cup G_2
\]
would be two initial segments of \(s\cup Y\) in \(\mathcal F\), contrary to
uniqueness. \(\square\)

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

### Corollary 8.5a.5: Pure terminal gating collapses to recurrence

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Suppose
that for every finite
\[
T\subset A
\]
and every \(L\), there are \(g\in A\), a witness parameter \(w\), and
\[
m=w-g>L
\]
such that
\[
m-T\subset A. \tag{1}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

In particular, an unbounded-depth front obstruction cannot have the moving
terminal endpoint color every protected finite test set with arbitrarily
large centers. If, for arbitrarily large terminal endpoints \(g=\max F\),
the private-color relations
\[
w-t-g\in A\qquad(t\in T)
\]
hold simultaneously for every prescribed finite \(T\), then the obstruction
is already impossible.

Proof. Condition (1) is exactly finite reflection-recurrence of \(A\).
Apply Theorem 2.3 with \(k=2\). \(\square\)

Thus the last-gated escape in Warning 8.5a.1b must either split every large
finite test among several moving active colors, keep the terminal centers
bounded for some fixed test, or force the stable fibers to be
certificate-free in a way that avoids compactification to finitely many
recurrent Sidon colors.

### Lemma 8.5a.6: Finite moving-label Sidon palettes are impossible

Let \(P\subset A\) be cofinite in \(A\), and let \(\Lambda\) be a finite
label set.
It is impossible that for every finite
\[
T\subset P
\]
and every \(M\), there are centers
\[
m_\lambda>M\qquad(\lambda\in\Lambda)
\]
and a coloring
\[
\chi:T\to\Lambda
\]
such that:

1. for every \(t\in T\),
   \[
   m_{\chi(t)}-t\in A;
   \]
2. every color fiber \(\chi^{-1}(\lambda)\) is certificate-free relative to
   \(A\).

Proof. Enumerate
\[
P=\{p_1<p_2<\cdots\}
\]
and apply the hypothesis to \(T_n=\{p_1,\ldots,p_n\}\) with \(M=n\). By
compactness of the finite product \(\Lambda^{\mathbb N}\), pass to a
subsequence on which the color of every fixed \(p_i\) stabilizes. Let
\[
C_\lambda\qquad(\lambda\in\Lambda)
\]
be the stable fibers.

Every \(C_\lambda\) is certificate-free, hence Sidon. If \(U\subset
C_\lambda\) is finite, then for all sufficiently large stages in the
subsequence all elements of \(U\) have color \(\lambda\), and the center
\(m_{\lambda,n}\) is larger than any prescribed bound. Thus \(C_\lambda\)
is reflection-recurrent in \(A\). Together with the finite exceptional set
\[
E=A\setminus P,
\]
the stable fibers form a finite Sidon coloring
\[
A=E\cup\bigcup_{\lambda\in\Lambda}C_\lambda
\]
whose nonempty color classes are all reflection-recurrent in \(A\). Lemma
8.6g''''.2 forbids this. \(\square\)

This lemma covers bounded-depth endpoint palettes, the terminal endpoint as
a moving label, and any finite mixture of them. Therefore a surviving
last-gated front obstruction must make the number of genuinely used moving
labels grow without bound, or else keep at least one required label center
bounded on a fixed finite test.

### Warning 8.5a.7: Mobile injective colors evade finite palettes

Lemma 8.5a.6 still does not close unbounded active traces. A front can
avoid every finite moving-label palette by assigning different protected
test points to different moving active endpoints.

Consider the first Schreier front on
\[
P=\{2,3,\ldots\},
\qquad
\mathcal S_1=\{\{x_1<\cdots<x_m\}\subset P:m=x_1\}.
\]
Given a finite protected test
\[
T=\{t_1,\ldots,t_M\},
\]
choose a front edge
\[
F=\{f_1<\cdots<f_r\}\in\mathcal S_1
\]
with \(r>M\), and declare the whole edge \(F\) to be the active trace.
Color
\[
t_i\mapsto f_i\qquad(1\le i\le M).
\]
Every color fiber is a singleton, hence certificate-free. The terminal
point \(f_r\) is active but need not color any protected test point, so
Corollary 8.5a.5 does not apply. No fixed finite palette is used as \(M\)
varies, so Lemma 8.5a.6 does not apply either.

This is only a formal incidence model: it does not construct an additive
basis, witnesses, or private sums. It shows that the remaining obstruction
must force either color reuse on some finite palette, or a genuine
arithmetic contradiction for mobile injective active colors.

The model also explains why naive section induction can fail. Once the
first point \(f_1=r\) of a Schreier edge is fixed, the section has bounded
length \(r-1\); the unboundedness comes entirely from moving the first
point. Thus no fixed proper section inherits the full "all finite tests"
mobile-color obstruction.

### Example 8.5a.7b: Parity blocks realize mobile-injective colors

The mobile-injective pattern is not merely combinatorial. It occurs in
arbitrarily large finite additive windows.

Fix \(r\ge2\), and put
\[
S_r=\{1,2,\ldots,2r\},\qquad
F_r=\{1,3,\ldots,2r-1\},\qquad
C_r=S_r\setminus F_r=\{2,4,\ldots,2r\}.
\]
Let
\[
w_r=2r+3.
\]
Then
\[
w_r\notin3C_r, \tag{1}
\]
because \(3C_r\) consists only of even numbers. The hole is
inclusion-minimal with respect to \(F_r\): for
\[
f_j=2j-1\in F_r
\]
one has
\[
w_r-f_j=2r+4-2j=2+2(r+1-j)\in2C_r. \tag{2}
\]
Thus restoring any one deleted odd element repairs the witness.

Moreover every retained row
\[
e_i=2i\in C_r
\]
has a private color
\[
\chi(e_i)=2r+1-2i\in F_r
\]
with a common retained mirror:
\[
w_r-e_i-\chi(e_i)=2\in C_r. \tag{3}
\]
At the same time,
\[
e_i+\chi(e_i)=2r+1\notin2C_r, \tag{4}
\]
again by parity. Hence the row-color graph from Lemma 8.4c contains a
perfect matching of size \(r\), with every color fiber a singleton.

Thus no argument can rule out mobile-injective active colors using only the
local private-sum conditions from Lemma 8.4c. The obstruction must use
global iteration, threshold control, or the way the support fillers and
active colors must themselves become future barrier vertices.

The finite diagnostic `EXPERIMENTS/mobile_injective_color_search.py` finds
the case \(r=3\) immediately:
\[
S_3=\{1,2,3,4,5,6\},\qquad F_3=\{1,3,5\},
\]
with witnesses \(9,11,13\) and a perfect row-color matching between evens
and odds.

### Warning 8.5a.7c: Private matchings do not imply Schreier links

Mobile-injective private colors are much weaker than the complete
prefix-link hypergraphs required by Lemma 13.1j. The gap is already visible
in a range-separated finite packet.

Let
\[
T=\{t_1<\cdots<t_m\}\subset\mathbb N
\]
be finite. Put
\[
R=\max T+m
\]
and choose \(N>4R\). Define
\[
w=10N,\qquad f_i=N+i,\qquad q_i=9N-t_i-i.
\]
Let
\[
F=\{f_1,\ldots,f_m\},\qquad
C=T\cup\{q_1,\ldots,q_m\},\qquad S=C\cup F.
\]
Then
\[
w-t_i-f_i=q_i\in C, \tag{1}
\]
and
\[
t_i+f_i=N+t_i+i\notin2C. \tag{2}
\]
Indeed, \(2C\) lies in the separated ranges \(T+T\ll N\),
\(T+\{q_i\}\sim9N\), and \(\{q_i\}+\{q_j\}\sim18N\).
More explicitly, \(T+T<N\), while every sum involving a \(q_i\) is larger
than \(8N\).

Also
\[
w\notin3C, \tag{3}
\]
because \(3C\) lies in separated ranges near \(0,9N,18N,27N\), none of
which contains \(10N\). For instance, a sum with no \(q_i\) is less than
\(N\); a sum with two or three \(q_i\)'s is larger than \(16N\); and a sum
with exactly one \(q_i\) has the form
\[
9N-t_i-i+t_j+t_k,
\]
which cannot equal \(10N\) because
\[
|t_j+t_k-t_i-i|<N.
\]
Restoring \(f_i\) repairs the hole:
\[
w=f_i+t_i+q_i. \tag{4}
\]
Thus \(F\) is inclusion-minimal for the witness \(w\), and the private
row-color graph contains the injective matching
\[
t_i\mapsto f_i.
\]

However this packet has no hereditary Schreier-link content. For the same
witness \(w\), if \(E\subsetneq F\), choose \(f_j\in F\setminus E\). Then
\[
w=f_j+t_j+q_j\in3(S\setminus E),
\]
so the proper subdeletion \(E\) is not bad for \(w\). Thus a private
matching can be anti-hereditary: the full active set is needed to create
the hole, while every proper subedge is repaired by an omitted active
color.

Consequently, one cannot infer the complete prefix-link condition of Lemma
13.1j from mobile-injective private colors alone. A positive proof must add
a promotion principle showing that the colors used in such packets become
future barrier vertices with their own witnesses; a counterexample attempt
must pay exactly this promoted-color debt.

The range-separated packet has a stronger feature: the new mirrors
\(q_i\) do not immediately force a new color palette. The same active color
\(f_i\) gates both the old row \(t_i\) and its mirror \(q_i\):
\[
w-q_i-f_i=t_i\in C. \tag{5}
\]
Moreover
\[
q_i+f_i=10N-t_i\notin2C, \tag{6}
\]
again by the same range separation. Hence each moving color \(f_i\) can
carry the two-point fiber
\[
\{t_i,q_i\}.
\]
This fiber is certificate-free relative to \(S\). Indeed, the only
nontrivial same-fiber certificate candidates are
\[
2q_i-t_i
\]
and
\[
2t_i-q_i,
\]
the first lying near \(18N\) and outside \(S\), the second negative for
large \(N\). Thus the support mirrors of the private matching can be folded
back into the same moving labels. The promoted-color debt is subtler: it
concerns the active colors \(f_i\) themselves becoming future deletion
vertices, not merely the retained mirrors \(q_i\) created to certify the
current hole.

The same separation occurs in a small covered additive window. Let
\[
A_0=\{1,2,3,4,5,8\},\qquad F=\{2,4,8\},\qquad C=A_0\setminus F=\{1,3,5\}.
\]
Then
\[
[2,13]\subseteq2A_0,
\]
and
\[
10\notin3C
\]
by parity. The hole is inclusion-minimal:
\[
10=2+3+5=4+1+5=8+1+1
\]
after restoring \(2,4,8\), respectively. The private row-color graph has
the perfect matching
\[
1\mapsto8,\qquad 3\mapsto4,\qquad 5\mapsto2,
\]
and the rows satisfy
\[
1+8=9,\qquad3+4=7,\qquad5+2=7,
\]
none of which lies in
\[
2C=\{2,4,6,8,10\}.
\]

However the active colors \(F=\{2,4,8\}\) do not support a Schreier order
inside the covered window. The pair \(\{2,4\}\) has a high-window witness
\[
8\notin3(A_0\setminus\{2,4\}),
\]
but deleting \(\{2,8\}\) or \(\{4,8\}\) leaves three-sum coverage from
\(\max\{2,8\}-1=7\) and \(\max\{4,8\}-1=7\) through \(13\). Thus no vertex
has pair links to both other vertices, so Lemma 13.1j's first prefix-link
condition fails for every ordering of \(F\), despite the mobile-injective
private coloring of the collective hole.

The interval parity blocks from Example 8.5a.7b give the same separation
at arbitrary rank. For \(r\ge4\), the odd active set
\[
F_r=\{1,3,\ldots,2r-1\}
\]
has the collective parity hole \(w_r=2r+3\), but it has no
Schreier-compatible order using pair links in the covered window
\([2,4r]\). Indeed, if \(E=\{a,b\}\subset F_r\), \(a<b\), and \(1\notin
E\), then \(1\), all evens, and at least one odd are retained. Every
\[
n\in[b-1,4r]
\]
lies in \(3([1,2r]\setminus E)\): even \(n\)'s are sums of three retained
evens, except for small even values which are \(1+1+(n-2)\), and odd
\(n\)'s are \(1\) plus two retained evens. If \(E=\{1,b\}\) with
\[
b\ge7,
\]
then \(3\) and all evens are retained; every even \(n\ge6\) is a sum of
three retained evens, and every odd \(n\ge7\) is \(3\) plus two retained
evens. Thus the only odd pairs with a high-window hole are contained in
\[
\{1,3\},\qquad \{1,5\}.
\]
For \(r\ge4\), no vertex of \(F_r\) is linked by such pair holes to every
other vertex of \(F_r\). Lemma 13.1j therefore cannot even start. The
collective mobile-injective hole is again strictly weaker than a
Schreier-prefix-link hypergraph.

### Warning 8.5a.7d: Independent mobile packets are selector-avoidable

The parity and range-separated packets cannot be used as independent
blocks. Suppose an attempted construction produces pairwise disjoint finite
sets
\[
P_1,P_2,\ldots
\]
and, in each block, a finite family \(\mathcal H_s\) of local active edges
such that every
\[
H\in\mathcal H_s
\]
has size at least \(2\), and all witnesses attached to \(\mathcal H_s\)
are blocked only when the deletion contains one whole \(H\). Then
\[
\mathcal H=\bigcup_s\mathcal H_s
\]
is not a weak barrier on \(\bigcup_sP_s\). Choose one point
\[
p_s\in P_s
\]
from each block and put
\[
B=\{p_s:s\ge1\}.
\]
The set \(B\) is infinite, but it contains no member of any
\(\mathcal H_s\), because it meets each block in only one point. Thus it
contains no member of \(\mathcal H\).

Consequently, an infinite counterexample cannot be obtained by placing
unrelated mobile-injective packets in disjoint intervals, even if each
packet has a large collective hole and perfect private-color matching. The
packet edges must be wired into a genuine cross-block barrier, or else
some singleton edges must persist. The singleton alternative is already
excluded in the remaining \(k=2\) case by Corollary 8.3b. This is the
combinatorial content of the promoted-color debt: active colors from one
packet must become vertices in later packet edges often enough that every
infinite deletion contains a whole active edge.

### Lemma 8.5a.7e: Sparse deletion avoids bounded-fiber mobile packets

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Fix constants
\[
D\ge0,\qquad L\ge1.
\]
Then there is an infinite set
\[
B=\{b_1<b_2<\cdots\}\subset A
\]
with the following property. No finite nonempty
\[
F\subset B,\qquad r=|F|,
\]
has a witness \(w\) such that:

1. \(w\notin3(A\setminus F)\);
2. \(w\ge\max F-D\);
3. the active retained rows
   \[
   R(F,w)=\{e\in A\setminus F:\ e\le w-N_0,\ w-e\notin F+F\}
   \]
   admit a private-color assignment
   \[
   \chi:R(F,w)\to F
   \]
   with
   \[
   w-e-\chi(e)\in A\setminus F,\qquad
   e+\chi(e)\notin2(A\setminus F)
   \]
   for every \(e\in R(F,w)\), and with every fiber satisfying
   \[
   |\chi^{-1}(f)|\le L\qquad(f\in F).
   \]

Proof. First note the capacity bound. If \(F,w,\chi\) satisfy the displayed
properties, then every element
\[
e\in A\cap[1,w-N_0]
\]
is in one of three classes:

* \(e\in F\), giving at most \(r\) choices;
* \(e\notin F\) and \(w-e\in F+F\), giving at most \(|F+F|\le r(r+1)/2\)
  choices;
* \(e\in R(F,w)\), giving at most \(Lr\) choices by the fiber bound.

Hence
\[
A(w-N_0)\le r+\frac{r(r+1)}2+Lr\le (L+2)r^2. \tag{1}
\]

Now construct \(B\) recursively. Since \(A(x)\to\infty\), choose
\[
b_r\in A
\]
strictly increasing so fast that
\[
A(b_r-D-N_0)>(L+2)r^2 \tag{2}
\]
for every \(r\ge1\), ignoring finitely many negative arguments by starting
far enough out. Let \(B=\{b_r:r\ge1\}\).

Suppose a finite \(F\subset B\) of size \(r\) satisfied the three
properties with witness \(w\). Then
\[
\max F\ge b_r,
\]
and by \(w\ge\max F-D\),
\[
w-N_0\ge b_r-D-N_0.
\]
Therefore (2) gives
\[
A(w-N_0)>(L+2)r^2,
\]
contradicting the capacity bound (1). \(\square\)

In a \(k=2\) counterexample, apply Corollary 3.1c to the sparse set
\(B\) supplied by the lemma. Any sufficiently late inclusion-minimal
late-bad edge inside \(B\) has a witness \(w\ge\max F-1\), so it satisfies
condition (2) with \(D=1\). Lemma 8.4c supplies private colors for all
non-\(F+F\) retained rows. Hence, for every fixed \(L\), such an edge must
force some active color to serve more than \(L\) retained rows. The
surviving mobile-color obstruction is therefore not genuinely injective on
sparse deletions: it must create unbounded private-color fibers, or use
deleted-pair exceptions \(F+F\) at rank comparable to the ambient counting
function.

### Lemma 8.5a.7e': Sparse deletion avoids rank-controlled fiber bounds

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\), with
order-2 threshold \(N_0\). Fix \(D\ge0\), and let
\[
\Phi:\mathbb N_{\ge1}\to\mathbb N
\]
be any function. Then there is an infinite set
\[
B=\{b_1<b_2<\cdots\}\subset A
\]
with the following property. No finite nonempty
\[
F\subset B,\qquad r=|F|,
\]
has a witness \(w\) satisfying conditions (1)--(3) of Lemma 8.5a.7e with
every private-color fiber bounded by
\[
|\chi^{-1}(f)|\le\Phi(r)\qquad(f\in F). \tag{1}
\]

Proof. The same capacity count gives the sharper rank-dependent bound
\[
A(w-N_0)\le r+|F+F|+r\Phi(r)
   \le r+\frac{r(r+1)}2+r\Phi(r). \tag{2}
\]
Choose \(b_r\in A\) strictly increasing, and far enough out that
\[
A(b_r-D-N_0)>
   r+\frac{r(r+1)}2+r\Phi(r) \tag{3}
\]
for every \(r\ge1\). If \(F\subset B\) has size \(r\), then
\[
\max F\ge b_r.
\]
Thus any witness with \(w\ge\max F-D\) satisfies
\[
w-N_0\ge b_r-D-N_0,
\]
and (3) contradicts (2). \(\square\)

This functional version removes a remaining loophole in Lemma 8.5a.7e:
the fiber bound may grow arbitrarily with the rank of the deleted edge.
Consequently, a counterexample cannot merely hide behind fibers of size
\(O(|F|)\), or \(O(|F|^C)\), or any other prescribed rank function after a
sufficiently sparse deletion.

### Corollary 8.5a.7f: Counterexamples force large private fibers

Work in the remaining \(k=2\) case, and suppose \(A\) is a counterexample
to the desired order-3 deletion conclusion. Then for every finite
\[
E\subset A
\]
and every \(M,L_0\), there are:

* a finite set \(F\subset A\setminus E\);
* a witness \(w>L_0\) with
  \[
  w\notin3(A\setminus F),\qquad w\ge\max F-1;
  \]
* an active color \(f\in F\);
* a set
  \[
  U\subset A\setminus F,\qquad |U|=M,
  \]

such that, putting
\[
m=w-f,
\]
one has
\[
m-U\subset A\setminus F \tag{1}
\]
and
\[
u+f\notin2(A\setminus F)\qquad(u\in U). \tag{2}
\]

Proof. Apply the construction in Lemma 8.5a.7e with \(D=1\) and
\(L=M-1\), choosing the sparse set \(B\) inside \(A\setminus E\) and above
\(L_0+1\). This is possible because deleting finitely many elements and an
initial segment does not change the fact that \(A(x)\to\infty\). By
Corollary 3.1c,
the infinite set \(B\) contains a finite late-bad set \(F_0\). Since
\(\min F_0>L_0+1\), it has a witness
\[
w\ge\max F_0-1>L_0
\]
with \(w\notin3(A\setminus F_0)\). Shrink \(F_0\) inclusion-minimally for
this fixed witness and call the result \(F\). Then
\[
F\subset B\subset A\setminus E,\qquad
w\notin3(A\setminus F),\qquad
w\ge\max F-1.
\]

For every retained row
\[
u\in R(F,w)=\{e\in A\setminus F:\ e\le w-N_0,\ w-e\notin F+F\},
\]
Lemma 8.4c gives at least one private color \(f\in F\) satisfying
\[
w-u-f\in A\setminus F,\qquad u+f\notin2(A\setminus F).
\]
Choose one such color for each row. If every color fiber had size at most
\(M-1\), then \(F,w\) would violate the defining property of the sparse set
\(B\) from Lemma 8.5a.7e. Hence some \(f\in F\) has a fiber of size at
least \(M\). Taking any \(M\)-element subset of that fiber gives \(U\), and
(1)--(2) follow. \(\square\)

This is not yet reflection-recurrence: the large fiber \(U\) may move with
the active color and witness, and it may be certificate-free. But the
purely injective packet model is eliminated. Any final counterexample must
produce arbitrarily large private reflected fibers while also preventing
those fibers from compacting to a recurrent certificate triple or to a
finite recurrent Sidon coloring.

### Corollary 8.5a.7f.1: Large private fibers split into two branches

Work in the remaining \(k=2\) counterexample case. Then for every finite
\[
E\subset A
\]
and every \(M,L_0\), there are:

* a finite set \(F\subset A\setminus E\);
* a witness \(w>L_0\) with
  \[
  w\notin3(A\setminus F),\qquad w\ge\max F-1;
  \]
* an active color \(f\in F\);
* a set
  \[
  U\subset A\setminus F,\qquad |U|=M;
  \]

such that, with
\[
m=w-f,
\]
one has
\[
m-U\subset A\setminus F \tag{1}
\]
and
\[
u+f\notin2(A\setminus F)\qquad(u\in U), \tag{2}
\]
and one of the following alternatives holds.

**Unique-gate branch.**
\[
r_{2,A}(u+f)=1\qquad(u\in U), \tag{3}
\]
where \(r_{2,A}\) counts unordered two-term representations from \(A\);
the unique representation is \(u+f=u+f\).

**Shifted-overlap branch.** There is a fixed
\[
g\in F\setminus\{f\}
\]
such that
\[
U+f-g\subset A\setminus F. \tag{4}
\]

Proof. Apply Lemma 8.5a.7e' with \(D=1\), with
\[
\Phi(r)=rM+\frac{r(r+1)}2,
\]
and with the sparse set chosen inside \(A\setminus E\) and above
\(L_0+1\). As in Corollary 8.5a.7f, Corollary 3.1c gives a finite
late-bad set \(F_0\) inside this sparse set; after shrinking for its fixed
witness \(w\), Lemma 8.4c supplies a private-color assignment on the active
retained rows. If every color fiber had size at most
\[
rM+\frac{r(r+1)}2,
\]
where \(r=|F|\), this would contradict Lemma 8.5a.7e'. Hence some
\[
f\in F
\]
has a private fiber \(U_0\) of size
\[
|U_0|>rM+\frac{r(r+1)}2. \tag{5}
\]
For every \(u\in U_0\),
\[
w-u-f\in A\setminus F,\qquad u+f\notin2(A\setminus F). \tag{6}
\]

Discard the rows with
\[
u+f\in F+F.
\]
There are at most
\[
|F+F|\le\frac{r(r+1)}2
\]
such rows, so the remaining set \(U_1\subset U_0\) has
\[
|U_1|>rM. \tag{7}
\]

Split the rows \(u\in U_1\) according to the full two-sum representations
of \(u+f\) in \(A\). The trivial representation \(u+f=u+f\) uses the
deleted color \(f\). If it is the only unordered representation, call
\(u\) unique. Otherwise choose another unordered representation of
\(u+f\). It cannot lie wholly in \(A\setminus F\), by (6). It also cannot
use \(f\), because the complementary summand would have to be \(u\), giving
the same unordered pair. Therefore it uses some
\[
g\in F\setminus\{f\}
\]
and the complementary summand is \(u+f-g\in A\). Since \(u\in U_1\), this
complementary summand cannot lie in \(F\); otherwise \(u+f\in F+F\). Hence
\[
u+f-g\in A\setminus F. \tag{8}
\]

If at least \(M\) elements of \(U_1\) are unique, choose those elements for
\(U\), and the unique-gate branch holds. Otherwise fewer than \(M\)
elements are unique, so by (7) more than
\[
(r-1)M
\]
elements have a shifted-overlap witness \(g\in F\setminus\{f\}\). If
\(r=1\), this is impossible, so the unique branch must already hold. If
\(r\ge2\), the pigeonhole principle gives one fixed \(g\in F\setminus\{f\}\)
serving at least \(M\) rows. Taking those rows for \(U\) gives
(1)--(2) and (4). \(\square\)

Thus the unbounded-fiber obstruction is not amorphous. In every finite
tail it has arbitrarily large subfibers whose private sums \(u+f\) are
either genuinely unique in the full basis \(A\), or all shifted back into
\(A\setminus F\) by the same deleted difference \(f-g\). The former branch
resembles the low-representation packets of Section 3; the latter is the
first rank-free form of promoted active-color recurrence.

### Lemma 8.5a.7i: Certificate-free shifted fibers are shift-separated

Let \(A\subseteq\mathbb N\), let \(h\ne0\), and let
\[
U\subset A
\]
be finite with
\[
U+h\subset A. \tag{1}
\]
If \(U\) is certificate-free relative to \(A\), meaning that there are no
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A,
\]
then
\[
U\cap(U-h)=\varnothing. \tag{2}
\]

Proof. Suppose instead that
\[
u,\ u+h\in U.
\]
Since \(u+h\in U\), (1) gives
\[
u+2h=(u+h)+h\in A.
\]
Taking
\[
e=u,\qquad y_1=y_2=u+h
\]
produces a certificate
\[
y_1+y_2-e=u+2h\in A,
\]
contrary to certificate-freeness. \(\square\)

Consequently the retained shifted-overlap branch in Corollary 8.5a.7f.1
has a new finite-test pressure. For a fixed nonzero \(h\), write
\[
\alpha_h(T)=\max\{|S|:\ S\subset T,\ S\cap(S-h)=\varnothing\}.
\]
If a fixed finite \(T\subset A\) with \(T+h\subset A\) is reflected by
arbitrarily large centers on subsets \(U\subset T\) with
\[
|U|>\alpha_h(T),\qquad U+h\subset A,
\]
then some pair \(u,u+h\in U\) occurs. The triple
\[
u,\ u+h,\ u+h
\]
is reflected by the same center and satisfies
\[
(u+h)+(u+h)-u=u+2h\in A.
\]
Since \(T\) is finite, one such triple recurs along an unbounded sequence
of centers, and Corollary 2.3c gives a good infinite deletion. Thus a
surviving shifted-overlap counterexample must either move the shift \(h\),
or keep every fixed-\(h\) reflected fiber inside \(h\)-independent subsets
of all finite tests.

### Lemma 8.5a.7j: Unique-gate fibers are gate-independent

Let \(A\subseteq\mathbb N\), let \(f\in A\), and let
\[
U\subset A\setminus\{f\}
\]
be finite. Suppose
\[
r_{2,A}(u+f)=1\qquad(u\in U), \tag{1}
\]
with the unique unordered representation of \(u+f\) being the gate pair
\[
u+f.
\]
Then
\[
(U+f-U)\cap A\subset\{f\}. \tag{2}
\]
Equivalently, for distinct \(u,v\in U\),
\[
u+f-v\notin A. \tag{3}
\]

Proof. If \(u,v\in U\) are distinct and
\[
x=u+f-v\in A,
\]
then
\[
u+f=v+x
\]
is an unordered two-term representation of \(u+f\) from \(A\). It is not
the same unordered pair as \(\{u,f\}\): equality would force either
\(v=u\), or \(v=f\), both impossible because \(v\ne u\) and
\(U\cap\{f\}=\varnothing\). Thus (1) fails. \(\square\)

Thus the unique-gate branch also has an independence graph. For finite
\[
T\subset A\setminus\{f\},
\]
write
\[
\iota_f(T)=\max\{|S|:\ S\subset T,\ (S+f-S)\cap A\subset\{f\}\}.
\]
Every unique-gate fiber inside \(T\) has size at most \(\iota_f(T)\).

### Corollary 8.5a.7k: Finite gate palettes collapse to certificates

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Fix a
finite gate palette
\[
P\subset A
\]
and a finite test set
\[
T_0\subset A\setminus P.
\]
For \(f\in P\), define
\[
\beta_f(T_0)=\max\left\{|S|:\ \substack{
S\subset T_0,\ S\text{ certificate-free relative to }A,\\
(S+f-S)\cap A\subset\{f\}}\right\}. \tag{1}
\]
Suppose that for every \(L\) there are
\[
f\in P,\qquad U\subset T_0,\qquad m>L
\]
such that
\[
m-U\subset A,\qquad r_{2,A}(u+f)=1\ (u\in U),\qquad |U|>\beta_f(T_0).
\tag{2}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. By Lemma 8.5a.7j, each set \(U\) in (2) is \(f\)-independent:
\[
(U+f-U)\cap A\subset\{f\}.
\]
Since \(|U|>\beta_f(T_0)\), the definition of \(\beta_f(T_0)\) forces
\(U\) to contain a certificate triple
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A. \tag{3}
\]
The center \(m\) reflects this triple into \(A\), because
\[
m-U\subset A.
\]
Let \(L\to\infty\). There are only finitely many choices of \(f\in P\) and
only finitely many triples inside \(T_0\). Hence one certificate triple
(3) is reflected by arbitrarily large centers. Corollary 2.3c gives the
desired infinite deletion. \(\square\)

### Corollary 8.5a.7l: Finite shifted palettes collapse to certificates

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Fix a
finite set of nonzero shifts
\[
H\subset\mathbb Z\setminus\{0\}
\]
and a finite test set
\[
T_0\subset A.
\]
For \(h\in H\), define
\[
\gamma_h(T_0)=\max\left\{|S|:\ \substack{
S\subset T_0,\ S+h\subset A,\ S\text{ certificate-free relative to }A,\\
S\cap(S-h)=\varnothing}\right\}. \tag{1}
\]
Suppose that for every \(L\) there are
\[
h\in H,\qquad U\subset T_0,\qquad m>L
\]
such that
\[
m-U\subset A,\qquad U+h\subset A,\qquad |U|>\gamma_h(T_0). \tag{2}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-3 basis.

Proof. Fix data as in (2). If
\[
U\cap(U-h)\ne\varnothing,
\]
then Lemma 8.5a.7i produces a certificate triple inside \(U\). If
\[
U\cap(U-h)=\varnothing,
\]
then (2) and the definition of \(\gamma_h(T_0)\) imply that \(U\) is not
certificate-free, so again \(U\) contains a certificate triple
\[
e,y_1,y_2\in U,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A. \tag{3}
\]
The center \(m\) reflects the triple by \(m-U\subset A\). Since \(H\) and
\(T_0\) are finite, one certificate triple recurs along arbitrarily large
centers as \(L\to\infty\). Corollary 2.3c gives the desired deletion.
\(\square\)

Corollaries 8.5a.7k--8.5a.7l are finite-palette no-go results. A surviving
large-fiber counterexample cannot keep unique gates in a fixed finite
palette while exceeding the corresponding \(\beta_f\)-independence numbers,
and it cannot keep shifted overlaps in a fixed finite shift palette while
exceeding the corresponding \(\gamma_h\)-independence numbers. Thus both
branches must move their parameters, or else every recurring finite test
must have large subsets that are simultaneously certificate-free and
independent for the relevant gate or shift.

### Example 8.5a.7g: Large one-color private fibers are locally compatible

The conclusion of Corollary 8.5a.7f is still only a global obstruction, not
a local contradiction. A single active color can carry an arbitrarily large
certificate-free private fiber in a finite range-separated packet.

Let
\[
U=\{u_1,\ldots,u_M\}
\]
be a finite Sidon set, for instance powers of \(2\). Choose \(N\) much
larger than every element of \(U\), and put
\[
w=10N,\qquad f=N,\qquad g=N+1,\qquad t=3N.
\]
For \(u\in U\), define
\[
q_u=9N-u,
\]
and put
\[
q_g=6N-1.
\]
Let
\[
F=\{f,g\},\qquad
C=U\cup\{q_u:u\in U\}\cup\{t,q_g\},\qquad S=C\cup F.
\]
By range separation,
\[
w\notin3C. \tag{1}
\]
Restoring \(f\) repairs \(w\) through every \(u\in U\):
\[
w=f+u+q_u, \tag{2}
\]
and restoring \(g\) repairs \(w\) through
\[
w=g+t+q_g. \tag{3}
\]
Thus \(F\) is inclusion-minimal for the witness \(w\).

The color \(f\) serves the whole fiber \(U\), since
\[
w-u-f=q_u\in C \qquad(u\in U), \tag{4}
\]
while
\[
u+f=N+u\notin2C. \tag{5}
\]
Again this follows from range separation: \(2C\) lies near \(0,3N,6N,9N,
12N,15N,18N\), not in the interval \(N+U\). The fiber \(U\) is
certificate-free relative to \(S\), because any certificate value
\[
u_i+u_j-u_k
\]
with \(u_i,u_j\ne u_k\) is below \(N\), and the Sidon property of \(U\)
prevents it from landing back in \(U\); it cannot land in the other ranges
of \(S\).

Thus large private fibers can be locally certificate-free and
range-separated. A proof must use their forced recurrence across all finite
tails, or the promotion of their active colors into later barriers, rather
than a one-stage contradiction.

### Example 8.5a.7m: Moving unique-gate fibers are locally compatible

The unique-gate branch in Corollary 8.5a.7f.1 also has no local
contradiction once the gate is allowed to move. Let
\[
U=\{u_1,\ldots,u_M\}
\]
be a finite Sidon set, and choose \(N\) much larger than every element of
\(U\). Put
\[
w=10N,\qquad f=N,\qquad g=2N,\qquad t=3N,\qquad q_g=5N,
\]
and for \(u\in U\), put
\[
q_u=9N-u.
\]
Let
\[
F=\{f,g\},\qquad C=U\cup\{q_u:u\in U\}\cup\{t,q_g\},\qquad S=C\cup F.
\]
The same range separation as in Example 8.5a.7g gives
\[
w\notin3C. \tag{1}
\]
Restoring \(f\) repairs \(w\) through every \(u\in U\):
\[
w=f+u+q_u, \tag{2}
\]
and restoring \(g\) repairs \(w\) through
\[
w=g+t+q_g. \tag{3}
\]
Thus \(F\) is inclusion-minimal for this local witness.

For every \(u\in U\),
\[
w-u-f=q_u\in C,\qquad u+f\notin2C. \tag{4}
\]
Moreover,
\[
r_{2,S}(u+f)=1, \tag{5}
\]
with the unique representation \(u+f=u+f\). Indeed, \(u+f=N+u\) is too
large to be a sum of two elements of \(U\), while every element of
\[
S\setminus(U\cup\{f\})
\]
is larger than \(N+u\) once \(N>\max U\); the representation using \(f\)
forces the other summand to be \(u\). The Sidon choice of \(U\), together
with range separation, again makes \(U\) certificate-free relative to
\(S\).

The diagnostic `fiber_palette_independence.py` verifies this with
\[
U=(1,2,4,8,16),\qquad N=260,\qquad F=(260,520),\qquad
w=2600,\qquad m=2340.
\]
It reports \(w\notin3C\), both single-color repairs, private rows for
\(f\), full uniqueness \(r_{2,S}(u+f)=1\) for every \(u\), and
certificate-freeness of \(U\). Thus Lemma 8.5a.7j and Corollary
8.5a.7k are genuinely finite-palette obstructions: a moving unique gate can
still carry an arbitrarily large local private fiber.

### Corollary 8.5a.7n: Fixed finite palettes have bounded bad centers

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\) which is
a counterexample to the desired order-3 deletion conclusion.

First fix a finite gate palette
\[
P\subset A
\]
and a finite test set
\[
T_0\subset A\setminus P.
\]
Then there is \(L_*(P,T_0)\) such that no
\[
m>L_*(P,T_0)
\]
admits data
\[
f\in P,\qquad U\subset T_0
\]
with
\[
m-U\subset A,\qquad r_{2,A}(u+f)=1\ (u\in U),\qquad |U|>\beta_f(T_0),
\tag{1}
\]
where \(\beta_f(T_0)\) is defined in Corollary 8.5a.7k.

Second fix a finite shift palette
\[
H\subset\mathbb Z\setminus\{0\}
\]
and a finite test set
\[
T_0\subset A.
\]
Then there is \(L_*(H,T_0)\) such that no
\[
m>L_*(H,T_0)
\]
admits data
\[
h\in H,\qquad U\subset T_0
\]
with
\[
m-U\subset A,\qquad U+h\subset A,\qquad |U|>\gamma_h(T_0), \tag{2}
\]
where \(\gamma_h(T_0)\) is defined in Corollary 8.5a.7l.

Proof. If the first assertion failed, then for every \(L\) there would be
data satisfying (1) with \(m>L\). Corollary 8.5a.7k would give an infinite
\[
B\subset A
\]
such that \(A\setminus B\) is an order-3 basis, contradicting the
counterexample assumption. The second assertion is identical, using
Corollary 8.5a.7l. \(\square\)

Therefore any recurring finite test in a counterexample has only three
ways to avoid a recurrent certificate: the reflection centers stay bounded,
the relevant gate or shift leaves every fixed finite palette, or the
reflected fiber stays inside the appropriate certificate-free independence
number. Example 8.5a.7m realizes the second option locally for the
unique-gate branch.

### Corollary 8.5a.7o: Forced fibers avoid prescribed palettes

Work in the remaining \(k=2\) counterexample case. Let
\[
E,P\subset A
\]
be finite, let
\[
H\subset\mathbb Z\setminus\{0\}
\]
be finite, and let \(M,L_0\) be given. Then the data in Corollary
8.5a.7f.1 may be chosen so that, in addition,
\[
F\subset A\setminus(E\cup P) \tag{1}
\]
and
\[
(F-F)\cap H=\varnothing. \tag{2}
\]
In particular, in the unique-gate branch the gate \(f\) lies outside the
prescribed palette \(P\), while in the shifted-overlap branch the shift
\[
h=f-g
\]
lies outside the prescribed shift palette \(H\).

Proof. Repeat the proof of Corollary 8.5a.7f.1, but build the sparse set
\[
B=\{b_1<b_2<\cdots\}
\]
with two extra recursive restrictions. At step \(r\), choose
\[
b_r\in A\setminus(E\cup P)
\]
above \(L_0+1\), so far out that the rank-controlled capacity inequality
from Lemma 8.5a.7e' holds for
\[
\Phi(r)=rM+\frac{r(r+1)}2,
\]
and avoiding the finite set
\[
\{b_i+h,\ b_i-h:\ 1\le i<r,\ h\in H\}. \tag{3}
\]
This is possible because \(A\) is infinite and only finitely many values
are forbidden at each step. The resulting \(B\) still has the
rank-controlled sparse-deletion property, and it also satisfies
\[
(B-B)\cap H=\varnothing. \tag{4}
\]

Apply Corollary 3.1c to this infinite \(B\), shrink the resulting late-bad
set for its fixed witness, and then run the proof of Corollary 8.5a.7f.1.
The output finite set \(F\) is a subset of \(B\), so (1)--(2) follow from
the construction of \(B\). The final assertions are immediate from
\(f,g\in F\). \(\square\)

Thus not only are fixed finite palettes unable to support recurrent
oversized fibers; in a genuine counterexample the forced finite bad edges
can be found after deleting any prescribed gate palette and after avoiding
any prescribed finite set of deleted-color differences. The remaining
moving-parameter escape is therefore cofinal in the gate and shift
parameters.

### Corollary 8.5a.7p: Forced fibers avoid finite row cores

Work in the remaining \(k=2\) counterexample case. Let
\[
E_{\rm del},E_{\rm row},P\subset A
\]
be finite, let
\[
H\subset\mathbb Z\setminus\{0\}
\]
be finite, and let \(M,L_0\) be given. Then the data in Corollary
8.5a.7f.1 may be chosen so that
\[
F\subset A\setminus(E_{\rm del}\cup P),\qquad (F-F)\cap H=\varnothing,
\tag{1}
\]
and
\[
U\subset A\setminus(F\cup E_{\rm row}),\qquad |U|=M. \tag{2}
\]
The same unique-gate or shifted-overlap alternative from Corollary
8.5a.7f.1 holds on this \(U\).

Proof. Apply Corollary 8.5a.7o with the same
\[
E_{\rm del},P,H,L_0
\]
but with
\[
M'=M+|E_{\rm row}|
\]
in place of \(M\). This gives \(F\), \(w\), \(f\), and a fiber
\[
U'\subset A\setminus F,\qquad |U'|=M',
\]
satisfying the private reflected conditions and one of the two branch
alternatives, while (1) holds. Since at most \(|E_{\rm row}|\) elements of
\(U'\) lie in \(E_{\rm row}\), the set
\[
U'\setminus E_{\rm row}
\]
has at least \(M\) elements. Choose any \(M\)-element subset and call it
\(U\). All private, reflected, unique-gate, and shifted-overlap conditions
are inherited by subsets of \(U'\). \(\square\)

Thus the forced large fibers can be made to escape finite cores on both
sides: the deleted active colors avoid any prescribed finite deletion
palette, and the retained rows avoid any prescribed finite row core. The
remaining obstruction must therefore recur only through moving finite tests
or through parameters that move cofinally.

### Corollary 8.5a.7q: Forced private packets avoid finite mirror cores

Work in the remaining \(k=2\) counterexample case. Let
\[
E_{\rm del},E_{\rm row},E_{\rm mir},P\subset A
\]
be finite, let
\[
H\subset\mathbb Z\setminus\{0\}
\]
be finite, and let \(M,L_0\) be given. Then the data in Corollary
8.5a.7f.1 may be chosen so that
\[
F\subset A\setminus(E_{\rm del}\cup P),\qquad (F-F)\cap H=\varnothing,
\tag{1}
\]
\[
U\subset A\setminus(F\cup E_{\rm row}),\qquad |U|=M, \tag{2}
\]
and, with \(m=w-f\),
\[
m-U\subset A\setminus(F\cup E_{\rm mir}). \tag{3}
\]
Again the same unique-gate or shifted-overlap alternative from Corollary
8.5a.7f.1 holds on \(U\).

Proof. Apply Corollary 8.5a.7p with
\[
M'=M+|E_{\rm mir}|
\]
in place of \(M\), and with the same finite sets \(E_{\rm del}\),
\(E_{\rm row}\), \(P\), and \(H\). This gives a set \(U'\) of size \(M'\)
avoiding \(E_{\rm row}\), with
\[
m-U'\subset A\setminus F.
\]
For a fixed center \(m\), the map
\[
u\mapsto m-u
\]
is injective. Hence at most \(|E_{\rm mir}|\) elements \(u\in U'\) have
\[
m-u\in E_{\rm mir}.
\]
Discard those rows and choose any \(M\)-element subset of the remainder.
All required private and branch conditions are inherited by subsets.
\(\square\)

Consequently a counterexample supplies arbitrarily large completely fresh
private packets: after any finite stage one can find a late-bad edge whose
deleted colors, retained private rows, and retained mirrors all avoid the
old stage, while the deleted-color differences avoid any prescribed finite
shift palette. A construction of a negative answer would have to wire these
fresh packets into later barrier edges; independent fresh packets alone are
selector-avoidable by Warning 8.5a.7d.

### Corollary 8.5a.7r: Selectors force cross-packet promoted edges

Work in the remaining \(k=2\) counterexample case, and let
\[
E_*
\]
be the finite singleton-exceptional set from Corollary 8.3b. Let
\[
F_1,F_2,\ldots
\]
be pairwise disjoint nonempty finite subsets of
\[
A\setminus E_*.
\]
Then for every infinite
\[
I\subset\mathbb N
\]
and every selector
\[
x_s\in F_s\qquad(s\in I),
\]
the selected set
\[
X=\{x_s:s\in I\}
\]
contains arbitrarily late bad cross-packet edges: for every \(L\) there is
a finite set
\[
G\subset X,\qquad |G|\ge2,
\]
and an integer \(v>L\) such that
\[
v\ge\max G-1,\qquad
v\notin3(A\setminus G). \tag{1}
\]
Since \(X\) contains at most one point of each \(F_s\), every such \(G\)
uses vertices from at least two distinct packets.

Proof. Put
\[
X_L=\{x\in X:\ x>L+1\}.
\]
This is an infinite subset of \(A\setminus E_*\). By Corollary 3.1c,
\(X_L\) contains a finite late-bad set
\[
G\subset X_L.
\]
By Corollary 8.3b, no singleton subset of \(A\setminus E_*\) is late-bad.
Hence
\[
|G|\ge2.
\]

It remains to choose the displayed witness. If \(A\setminus G\) is not an
order-3 basis, then it has unbounded holes, so choose
\[
v>\max\{L,\max G\}
\]
with \(v\notin3(A\setminus G)\). If \(A\setminus G\) is an order-3 basis,
then late-badness means it has no threshold below \(\max G\). Hence some
\[
v\ge\max G-1>L
\]
satisfies \(v\notin3(A\setminus G)\). In both cases (1) holds. The
selector property forces \(G\) to meet at least two of the sets \(F_s\).
\(\square\)

Combining this with Corollary 8.5a.7q gives the current exact wiring debt.
One may recursively build pairwise disjoint fresh private packets
\[
\Pi_s=(F_s,w_s,f_s,U_s,m_s)
\]
whose deleted colors, private rows, and mirrors avoid all earlier packet
data. But for every infinite subcollection and every choice of one deleted
color from each \(F_s\), Corollary 8.5a.7r forces arbitrarily late bad
edges among the selected colors. Therefore a counterexample cannot be a
disjoint union of self-contained private packets. Its late-bad hypergraph
must promote colors from many packets into new cross-packet edges on every
infinite selector.

### Corollary 8.5a.7s: Fresh packets project to index barriers

Keep the hypotheses of Corollary 8.5a.7r. For a finite set
\[
G\subset\bigcup_sF_s
\]
that meets each \(F_s\) in at most one point, write
\[
\operatorname{supp}(G)=\{s:\ G\cap F_s\ne\varnothing\}.
\]
For \(L\ge0\), let \(\mathcal G_L\) be the family of finite sets
\[
G\subset\bigcup_sF_s
\]
such that:

1. \(G\) meets each \(F_s\) in at most one point;
2. \(|G|\ge2\);
3. there is \(v>L\) with
   \[
   v\ge\max G-1,\qquad v\notin3(A\setminus G).
   \]

Then \(\mathcal G_L\) is a product-selector barrier: for every infinite
\[
I\subset\mathbb N
\]
and every selector
\[
x_s\in F_s\qquad(s\in I),
\]
there is \(G\in\mathcal G_L\) with
\[
G\subset\{x_s:s\in I\}. \tag{1}
\]
Consequently the support family
\[
\mathcal S_L=\{\operatorname{supp}(G):G\in\mathcal G_L\}
\]
is a weak barrier on \(\mathbb N\), and every member of \(\mathcal S_L\)
has size at least \(2\).

Proof. The product-selector assertion is exactly Corollary 8.5a.7r applied
to the chosen selector. The support assertion follows by choosing, for an
arbitrary infinite \(I\), any selector \(x_s\in F_s\) for \(s\in I\). The
set \(G\) given by (1) has support contained in \(I\), so \(\mathcal S_L\)
meets every infinite \(I\). Since \(|G|\ge2\) and \(G\) meets each packet in
at most one point, \(|\operatorname{supp}(G)|\ge2\). \(\square\)

Thus the promoted-edge debt has an ordinary front shadow on packet indices.
For each threshold \(L\), the fresh-packet construction induces a
non-singleton weak barrier \(\mathcal S_L\) on the index set, while
\(\mathcal G_L\) records the stronger product constraint that every choice
of one deleted color per packet must contain a realized arithmetic bad edge.
A positive proof must show that such product-selector barriers cannot carry
the private-incidence structure above; a negative construction must realize
them, not merely an abstract index front.

### Corollary 8.5a.7t: Product-selector debt has finite complete windows

Keep the hypotheses and notation of Corollary 8.5a.7s. Fix \(L\). For
every infinite
\[
I\subset\mathbb N
\]
there is a finite nonempty set
\[
J\subset I
\]
such that every finite selector
\[
y_j\in F_j\qquad(j\in J)
\]
contains a bad cross-packet edge from \(\mathcal G_L\): there is
\[
G\in\mathcal G_L,\qquad G\subset\{y_j:j\in J\}. \tag{1}
\]
In particular, for every \(L\) and every infinite packet tail, the
counterexample must realize a finite product cover by arithmetic bad edges
with witnesses \(>L\).

Proof. Relabel \(I=\{i_1<i_2<\cdots\}\). Suppose no finite
\[
J\subset I
\]
has the displayed product-cover property. Then for every \(n\) there is a
selector
\[
y_{i_j}^{(n)}\in F_{i_j}\qquad(1\le j\le n)
\]
such that no
\[
G\in\mathcal G_L
\]
is contained in
\[
\{y_{i_1}^{(n)},\ldots,y_{i_n}^{(n)}\}. \tag{2}
\]
Since every \(F_{i_j}\) is finite, the tree of partial selectors satisfying
(2) at their length is finitely branching and has nodes at every depth. By
Koenig's lemma, it has an infinite branch
\[
y_{i_j}\in F_{i_j}\qquad(j\ge1)
\]
whose every finite initial segment satisfies (2). But Corollary 8.5a.7s,
applied to this infinite selector on \(I\), gives
\[
G\in\mathcal G_L,\qquad G\subset\{y_{i_j}:j\ge1\}.
\]
The support of \(G\) is finite, so \(G\) lies in some finite initial
segment of the branch, contradicting (2). \(\square\)

Thus the promoted-edge debt is finitely visible: it is not enough for a
construction to arrange an abstract infinite selector barrier. At
arbitrarily late thresholds and inside every infinite packet tail, some
finite packet window must already be completely wired so that every product
choice of one deleted color contains a realized arithmetic late-bad edge.

### Lemma 8.5a.7u: Product covers force low-rank edges or many edges

Let
\[
J
\]
be finite, and let
\[
F_j\qquad(j\in J)
\]
be finite nonempty blocks. Let \(\mathcal H\) be a family of finite sets
\[
G\subset\bigcup_{j\in J}F_j
\]
such that every \(G\in\mathcal H\) meets each block in at most one point,
and suppose \(\mathcal H\) covers the product:
for every selector
\[
y_j\in F_j\qquad(j\in J),
\]
there is \(G\in\mathcal H\) with
\[
G\subset\{y_j:j\in J\}. \tag{1}
\]
For \(G\in\mathcal H\), put
\[
\sigma(G)=\{j\in J:\ G\cap F_j\ne\varnothing\}.
\]
Then
\[
\sum_{G\in\mathcal H}\prod_{j\in\sigma(G)}\frac1{|F_j|}\ge1. \tag{2}
\]
Consequently, if
\[
|F_j|\ge m\qquad(j\in J)
\]
and every \(G\in\mathcal H\) has
\[
|\sigma(G)|\ge q,
\]
then
\[
|\mathcal H|\ge m^q. \tag{3}
\]

Proof. The product of the blocks has size
\[
T=\prod_{j\in J}|F_j|.
\]
A fixed edge \(G\) is contained in exactly
\[
\prod_{j\in J\setminus\sigma(G)}|F_j|
\]
selectors. Since the sets of selectors covered by the edges of
\(\mathcal H\) cover the whole product, the union bound gives
\[
T\le \sum_{G\in\mathcal H}\prod_{j\in J\setminus\sigma(G)}|F_j|.
\]
Dividing by \(T\) gives (2). If \(|F_j|\ge m\) and
\(|\sigma(G)|\ge q\), then each summand in (2) is at most \(m^{-q}\), so
\[
1\le |\mathcal H|m^{-q},
\]
which proves (3). \(\square\)

Applied to the finite windows from Corollary 8.5a.7t, this says that a
counterexample has only two product-cover options. Either some finite
window contains low-rank promoted bad edges, especially pair edges when
\(|\sigma(G)|=2\), or avoiding all supports below \(q\) requires at least
\(m^q\) realized arithmetic late-bad edges in that one finite window, where
\[
m=\min_{j\in J}|F_j|.
\]
Thus a construction cannot hide the promoted-edge debt in a small number of
high-rank cross-packet constraints.

### Corollary 8.5a.7v: Pair-cylinder subcovers are impossible

Work in the remaining \(k=2\) counterexample case, and let
\[
F_1,F_2,\ldots
\]
be the disjoint fresh deleted-color packets from Corollary 8.5a.7r. It is
impossible that the promoted debt can be carried by pairs alone in the
following product sense: for every \(L\), every infinite
\[
I\subset\mathbb N
\]
and every selector
\[
x_s\in F_s\qquad(s\in I),
\]
there are \(i<j\) in \(I\) and a witness \(v>L\) such that
\[
v\ge x_j-1,\qquad v\notin3(A\setminus\{x_i,x_j\}). \tag{1}
\]

Proof. Put
\[
P=\bigcup_sF_s.
\]
The hypothesis first gives an ordinary pair barrier on the reservoir \(P\):
if \(X\subset P\) is infinite, then \(X\) meets infinitely many packets;
choosing one point \(x_s\in X\cap F_s\) from each such packet and applying
the hypothesis gives a bad pair contained in \(X\), above any prescribed
threshold \(L\).

The proofs of Corollary 8.6b and Lemmas 8.6g'--8.6g'''' use only the
ability to choose bad pairs outside an arbitrary finite test set. Therefore
they apply to the infinite reservoir \(P\) just as they apply to a cofinite
tail. We recall the reduction to make the quantifiers explicit.

If there is \(D\) such that every infinite \(X\subset P\) and every \(L\)
contain a pair \(x<y\) and a witness
\[
v>L,\qquad y\le v\le y+D,\qquad v\notin3(A\setminus\{x,y\}),
\]
then the proof of Corollary 8.6b gives tail reflection-recurrence and
hence a good infinite deletion, contradicting the counterexample
assumption. The lower bound \(v\ge y\) is automatic for sufficiently late
pairs in the remaining case: singleton deletions have order-3 thresholds
below the smaller endpoint, and a genuine pair witness below \(y\) would
already be repaired after deleting only \(x\).

Thus, for every \(D\), there are an infinite \(X_D\subset P\) and a
threshold \(L_D\) such that no pair in \(X_D\) has a witness
\[
v>L_D,\qquad v\le\max\{x,y\}+D. \tag{2}
\]
Fix a finite test set \(T\subset A\) and \(M\). Remove from \(X_D\) both
\(T\) and the finitely many elements at most \(\max T\), and take \(D\)
larger than \(M+N_0\). Applying the pair-cylinder hypothesis inside the
remaining selector tail with threshold
\[
L>\max\{L_D,\max T+N_0\}
\]
gives a pair \(x<y\) outside \(T\) and a witness \(v\). By (2),
\[
v-y>D,\qquad v-x>D,\qquad v-\max T\ge N_0. \tag{3}
\]
Therefore high-excess pair witnesses exist outside every finite test set.

For such a pair and finite test \(T\), define endpoint lists
\[
L_v(t)=\{z\in\{x,y\}:v-t-z\in A\}\qquad(t\in T).
\]
Lemma 10.1 makes these lists nonempty. If for some finite \(T_0\) and
arbitrarily large parameters the lists admit no choice whose two fibers are
certificate-free relative to \(A\), Lemma 8.6g' produces a recurrent
certificate triple and Corollary 2.3c gives a good deletion. Otherwise,
for every finite \(T\) and every \(M\), there are high-excess pair
witnesses whose endpoint lists are two-colorable with certificate-free
fibers. Lemma 8.6g'' compactifies these finite list colorings to a
partition of \(A\) into two certificate-free reflection-recurrent colors.
Lemma 8.6g'''' forbids such two recurrent Sidon colors in the integers.

Both alternatives contradict that \(A\) is a counterexample. Hence the
pair-cylinder product subcover cannot exist. \(\square\)

Consequently, any surviving product-selector debt from Corollary 8.5a.7t
must be genuinely high-rank on some selector tail. It is not enough for a
finite product window merely to contain many pair edges; if pairs alone
cover all selectors on every tail, the earlier pair-barrier machinery
already gives the desired infinite deletion.

### Corollary 8.5a.7w: High-rank selector debt is cofinally forced

In the remaining \(k=2\) counterexample case, for arbitrarily large
thresholds \(L\) there are an infinite packet set
\[
I\subset\mathbb N
\]
and a selector
\[
x_s\in F_s\qquad(s\in I)
\]
such that no pair from the selector lies in \(\mathcal G_L\). For every
such selector, Corollary 8.5a.7s still supplies
\[
G\in\mathcal G_L,\qquad G\subset\{x_s:s\in I\},
\]
and necessarily
\[
|G|\ge3.
\]

Proof. If the first assertion failed, then for some \(L_0\) and every
\[
L\ge L_0
\]
the pair subfamily of \(\mathcal G_L\) would product-cover every infinite
packet selector tail. Since the condition \(v>L\) is monotone in \(L\),
this would imply the pair-cylinder hypothesis of Corollary 8.5a.7v for
every threshold. That corollary gives a contradiction. Hence the
pair-avoiding selectors exist for arbitrarily large \(L\).

For such an \(L\) and selector, Corollary 8.5a.7s gives some
\[
G\in\mathcal G_L
\]
contained in the selector. By construction the selector contains no pair
from \(\mathcal G_L\), while every member of \(\mathcal G_L\) has size at
least \(2\). Therefore this \(G\) has size at least \(3\). \(\square\)

Thus the live product debt cannot be discharged by pair barriers at late
levels. Any final positive proof must rule out rank-\(\ge3\) promoted
edges on pair-avoiding selectors, while any negative construction must make
those higher-rank edges persistent and arithmetic, not just abstractly
available.

### Corollary 8.5a.7x: Pair-free high-rank debt has unbounded second excess

In the remaining \(k=2\) counterexample case, for every \(D\) and every
\(L_0\) there are a threshold \(L\ge L_0\), an infinite selector
\[
Y=\{y_s:s\in I\},\qquad y_s\in F_s,
\]
and an edge
\[
G=\{g_1<\cdots<g_r\}\in\mathcal G_L,\qquad G\subset Y,
\]
such that
\[
r\ge3
\]
and \(G\) has a witness \(v>L\) satisfying
\[
v>g_2+D. \tag{1}
\]

Proof. By Corollary 8.5a.7w, choose \(L_1\ge L_0\) and an infinite selector
\[
Y=\{y_s:s\in I\}
\]
with no pair from \(\mathcal G_{L_1}\). Since
\[
\mathcal G_L\subset\mathcal G_{L_1}\qquad(L\ge L_1),
\]
the same selector has no bad pair at any later threshold.

Fix \(D\). Suppose that, on this selector tail, bounded second-excess edges
formed a barrier at all later thresholds: for every infinite
\[
Z\subset Y
\]
and every \(L\ge L_1\), there were a finite
\[
H=\{h_1<h_2<\cdots<h_s\}\subset Z,\qquad s\ge2,
\]
and a witness \(u>L\) such that
\[
u\ge\max H-1,\qquad
u\notin3(A\setminus H),\qquad u\le h_2+D. \tag{2}
\]
The proof of Lemma 8.6a applies verbatim with the infinite reservoir \(Y\)
in place of the cofinite tail: the endpoints of \(H\) can be chosen outside
an arbitrary finite test set, and (2) is exactly the bounded
second-excess hypothesis. It would give tail reflection-recurrence and
hence a good infinite deletion, contradicting the counterexample
assumption.

Therefore there are an infinite \(Z\subset Y\) and a threshold
\[
L\ge L_1
\]
such that no finite subset of \(Z\) has a witness satisfying (2). Apply the
product-selector barrier, Corollary 8.5a.7s, to the selector \(Z\) at this
threshold \(L\). It gives
\[
G\in\mathcal G_L,\qquad G\subset Z.
\]
The set \(G\) is not a pair, because \(Y\) contains no pair from
\(\mathcal G_L\). Write \(G=\{g_1<\cdots<g_r\}\). Since no bounded
second-excess edge occurs in \(Z\) at threshold \(L\), any witness
\[
v>L,\qquad v\notin3(A\setminus G)
\]
certifying \(G\in\mathcal G_L\) must satisfy \(v>g_2+D\). Thus \(r\ge3\)
and (1) holds. \(\square\)

The remaining promoted edge must therefore be spread out: its witness is
not controlled by its second-smallest deleted color. This removes the
bounded-second-excess route of Lemma 8.6a from the pair-free selector
tail and leaves only genuinely large-spread high-rank barriers.

Warning: this large-spread high-rank shape is locally compatible. The
interval construction in Proposition 10.3g has
\[
F=\{X+2M,\ldots,X+2M+\lfloor(M-1)/2\rfloor\},
\qquad
w=3X+5M,
\]
so the second excess is
\[
w-(X+2M+1)=2X+3M-1.
\]
Lemma 10.3h shows that, inside the same covered interval-block model, every
coverage-compatible terminal-gap deletion has rank at least
\[
\lceil M/2\rceil.
\]
Thus Corollary 8.5a.7x identifies a genuine global barrier problem, not a
finite-window contradiction. A proof must still use the cross-packet
product demand, recurrence, or stage iteration; a counterexample would have
to code these large interval-like cuts into an unbounded selector barrier.

### Corollary 8.5a.7y: Minimal large-spread edges have the full terminal-gap normal form

In the remaining \(k=2\) counterexample case, for every \(D\) and every
\(L_0\) there are \(L\ge L_0\), an infinite selector
\[
Y=\{y_s:s\in I\},\qquad y_s\in F_s,
\]
a finite set
\[
F=\{f_1<\cdots<f_r\}\subset Y,
\]
and a witness \(v\) such that:

1. \(r\ge3\);
2. \(v>L\), \(v\ge\max F-1\), and
   \[
   v\notin3(A\setminus F); \tag{1}
   \]
3. \(F\) is inclusion-minimal for the fixed witness \(v\);
4. the second excess is large:
   \[
   v>f_2+D; \tag{2}
   \]
5. writing \(m_0=\min A\) and \(N_0\) for an order-2 threshold of \(A\),
   \[
   (A\setminus F)\cap(v-f_1-m_0,\ v-N_0]=\varnothing; \tag{3}
   \]
6. every retained \(e\in A\setminus F\) with \(v-e\ge N_0\) has every
   two-term representation of \(v-e\) from \(A\) meeting \(F\);
7. every \(f\in F\) is active: for some \(q_f\in\{1,2,3\}\) and retained
   elements \(c_{f,1},\ldots,c_{f,3-q_f}\in A\setminus F\),
   \[
   v=q_f f+c_{f,1}+\cdots+c_{f,3-q_f}. \tag{4}
   \]

Proof. Repeat the construction in the proof of Corollary 8.5a.7x with the
prescribed \(D,L_0\). First choose a pair-free selector tail. Since
bounded second-excess edges cannot form a barrier on that tail without
invoking Lemma 8.6a, there are an infinite subselector
\[
Z\subset Y
\]
and a threshold \(L\ge L_0\) such that no finite subset of \(Z\) has a
witness \(u>L\) bounded by its second-smallest element plus \(D\). The
product-selector barrier then gives an edge
\[
G\in\mathcal G_L,\qquad G\subset Y,
\]
with \(G\subset Z\), and a witness \(v>L\).

Shrink \(G\) inclusion-minimally while preserving the fixed
nonrepresentation
\[
v\notin3(A\setminus G).
\]
Call the resulting set \(F\). Since \(F\subset G\subset Y\), the same
witness satisfies \(v\ge\max F-1\). If \(|F|=2\), then \(F\) itself would
be a pair in \(\mathcal G_L\) contained in the pair-free selector \(Y\), a
contradiction. If \(|F|=1\), then \(F\) would be a singleton late-bad edge
in the singleton-free tail from Corollary 8.3b, again impossible after the
fresh packet construction. Thus \(|F|\ge3\).

The subselector \(Z\) was chosen so that no finite subset of \(Z\) has a
witness \(u>L\) with
\[
u\le h_2+D
\]
where \(h_2\) is its second-smallest element. Since \(F\subset Z\) and
\(v\) is a witness for \(F\), this gives (2).

The terminal gap (3) and the activity assertion (4) are the \(k=2\) case of
Lemma 10.3b applied to the inclusion-minimal witness \(v\). The vertex-cover
statement in item 6 is Lemma 10.1. \(\square\)

This is the current sharp normal form for the \(k=2\) obstruction: a
pair-free selector tail contains arbitrarily late inclusion-minimal active
holes of rank at least \(3\), with unbounded second excess and a terminal
retained gap. Pair subedges, bounded second-excess barriers, and nonminimal
inactive padding have all been removed.

### Example 8.5a.7z: Rank-three product terminal covers are locally compatible

The normal form in Corollary 8.5a.7y is not locally contradictory. Let
\[
A_0=\{1,3,4,5,8,10,11,12\}.
\]
Then
\[
[4,24]\subseteq2A_0.
\]
On the witness window
\[
[14,23],
\]
every singleton and every pair deletion from \(A_0\) still leaves full
three-fold coverage. However the three two-point packets
\[
F_1=\{4,10\},\qquad F_2=\{5,11\},\qquad F_3=\{8,12\}
\]
support a complete rank-three product cover: for every selector
\[
(x_1,x_2,x_3)\in F_1\times F_2\times F_3
\]
there is a witness \(v\in[14,23]\) such that, with
\[
F=\{x_1,x_2,x_3\},
\]
one has
\[
v\notin3(A_0\setminus F),
\]
the deletion \(F\) is inclusion-minimal for \(v\), and the finite terminal
gap
\[
(A_0\setminus F)\cap(v-\min F-1,\ v-4]=\varnothing. \tag{1}
\]
One possible witness table is:
\[
\begin{array}{c|c}
F & v\\ \hline
\{4,5,8\} & 19\\
\{4,5,12\} & 18\\
\{4,11,8\} & 17\\
\{4,11,12\} & 22\\
\{10,5,8\} & 21\\
\{10,5,12\} & 21\\
\{10,11,8\} & 23\\
\{10,11,12\} & 22
\end{array}
\]
The diagnostic
`EXPERIMENTS/product_rank3_terminal_cover.py` verifies these assertions
directly. The extra point \(24\in2A_0\) is the one-point positive-summand
buffer that a staged \(k=2\) construction would need if this window were
frozen below later elements.

Thus even the pair-free product-cover form of the remaining obstruction is
finite-window compatible. What is missing for a counterexample is not a
single product window, but an infinite staging that freezes such windows
below later elements and makes them an unbounded selector barrier while
preserving order-2 coverage.

### Warning 8.5a.7z.1: Disjoint rank-three product windows are not a barrier

Example 8.5a.7z cannot be iterated by simply placing disjoint copies on
successive packet windows. More generally, let
\[
W_1,W_2,\ldots
\]
be disjoint finite sets of packet indices, and suppose a support family
\[
\mathcal S
\]
has every member contained in one \(W_n\) and of size at least \(3\). Then
\(\mathcal S\) is not a weak barrier on
\[
\bigcup_n W_n.
\]
Indeed, choose a set
\[
I_n\subset W_n,\qquad |I_n|=\min(2,|W_n|)
\]
for each \(n\) with \(W_n\ne\varnothing\), and put
\[
I=\bigcup_n I_n.
\]
If infinitely many \(W_n\) are nonempty then \(I\) is infinite, but no
member of \(\mathcal S\) is contained in \(I\), because every member of
\(\mathcal S\) needs at least three indices from a single \(W_n\).

Thus a negative construction cannot be a disjoint sequence of finite
rank-three product gadgets. The supports of the promoted terminal cuts must
form a genuine cross-window front or weak barrier on packet indices. This
is the same global demand already encoded abstractly in Corollary
8.5a.7s, now applied to the concrete local model of Example 8.5a.7z.

### Diagnostic 8.5a.7z.2: The first fourth-packet extension search fails

The script `EXPERIMENTS/product_rank3_extension_search.py` tests the next
finite staging question for Example 8.5a.7z. Starting from
\[
A_0=\{1,3,4,5,8,10,11,12\}
\]
and packets
\[
\{4,10\},\qquad \{5,11\},\qquad \{8,12\},
\]
it tries to add a fourth two-point packet, together with a bounded number of
extra fillers, and requires:

1. all singleton and pair deletions remain three-fold covered on the
   witness window;
2. every choice of three of the four packets and one point from each has an
   inclusion-minimal terminal-gap witness;
3. the two-sum coverage has the one-point buffer required by Lemma 13.1d.

With
```
python3 881/EXPERIMENTS/product_rank3_extension_search.py --max-value 30 --max-fillers 2
```
the search checks \(20961\) candidates and finds no extension. This is only
bounded finite evidence. Its significance is that the first iteration
pressure appears immediately when one asks a rank-three product window to
coexist with all four possible three-packet subwindows while preserving
pair-harmlessness.

### Lemma 8.5a.7z.3: Common rank-three product witnesses have tiny outside fibers

Let \(A\) be an order-2 basis with threshold \(N_0\). Let
\[
P_1,\ P_2,\ P_3\subset A
\]
be pairwise disjoint two-point packets, say
\[
P_i=\{p_i^0,p_i^1\}.
\]
Suppose one integer \(v\) has the following common product-hole property:
for every selector
\[
x_i\in P_i\qquad(i=1,2,3),
\]
writing
\[
F=\{x_1,x_2,x_3\},
\]
one has
\[
v\notin3(A\setminus F). \tag{1}
\]
Then every retained point
\[
e\in A\setminus(P_1\cup P_2\cup P_3),\qquad v-e\ge N_0,
\]
satisfies
\[
v-e\in
\{p_1^0+p_1^1,\ p_2^0+p_2^1,\ p_3^0+p_3^1\}. \tag{2}
\]
In particular there are at most three such outside retained points \(e\).

Proof. Fix \(e\) as above. Since \(v-e\ge N_0\), choose a two-term
representation
\[
v-e=a+b,\qquad a,b\in A. \tag{3}
\]
For each selector \(F\), the point \(e\) is retained after deleting \(F\).
If the support \(\{a,b\}\) avoided \(F\), then
\[
v=e+a+b\in3(A\setminus F),
\]
contradicting (1). Hence the support of every representation (3) meets
every selector in
\[
P_1\times P_2\times P_3. \tag{4}
\]

A set of at most two points can meet every selector in this product only by
containing both points of one packet. Indeed, if it does not contain all of
any \(P_i\), choose \(x_i\in P_i\) outside the set for each \(i\); the
resulting selector avoids it. Therefore the support of (3) contains
\[
P_i
\]
for some \(i\in\{1,2,3\}\). Since the support has size at most two, this
means
\[
\{a,b\}=P_i
\]
as a multiset-free support, and hence
\[
v-e=p_i^0+p_i^1.
\]
This proves (2). The bound of three outside retained points follows because
each displayed sum determines \(e\) uniquely. \(\square\)

Thus a product-window construction with many old retained padders cannot
reuse one witness for an entire three-packet cube. The witnesses in any
iterable rank-three product barrier must be selector-specific, or at least
specific to very small subfamilies of selectors, so that the shifted
two-sum fibers \(v-e\) do not collapse to the three full packet-pair sums.

### Lemma 8.5a.7z.4: Shared witnesses force two-transversals

Let \(A\) be an order-2 basis with threshold \(N_0\). Let
\[
\mathcal C
\]
be a finite family of finite subsets of \(A\), and suppose one integer
\[
v
\]
has the common-hole property
\[
v\notin3(A\setminus F)\qquad(F\in\mathcal C). \tag{1}
\]
Let \(\mathcal T_2(\mathcal C)\) be the family of subsets
\[
H\subset A,\qquad |H|\le2,
\]
that meet every \(F\in\mathcal C\). Then every
\[
e\in A\setminus\bigcup_{F\in\mathcal C}F,\qquad v-e\ge N_0,
\]
has the following property: every two-term representation
\[
v-e=a+b,\qquad a,b\in A, \tag{2}
\]
has support containing a member of \(\mathcal T_2(\mathcal C)\). In
particular, the support itself satisfies
\[
\{a,b\}\in\mathcal T_2(\mathcal C). \tag{3}
\]
Suppose further that \(\mathcal C\) has no singleton transversal, i.e.
there is no \(h\in A\) with
\[
h\in F\qquad(F\in\mathcal C).
\]
Then every support in (2) has size two and is contained in the finite set
\[
U=\bigcup_{F\in\mathcal C}F.
\]
Consequently, if
\[
\Sigma_2(\mathcal C)=
\{h+h':\{h,h'\}\in\mathcal T_2(\mathcal C)\},
\]
then every such \(e\) satisfies
\[
v-e\in \Sigma_2(\mathcal C). \tag{4}
\]
In particular, the number of outside retained \(e\)'s with \(v-e\ge N_0\)
is at most
\[
|\Sigma_2(\mathcal C)|.
\]

Proof. Fix \(e\) and a representation (2). If the support
\[
H=\{a,b\}
\]
failed to meet some \(F\in\mathcal C\), then \(e,a,b\) would all be
retained after deleting \(F\), and
\[
v=e+a+b\in3(A\setminus F),
\]
contradicting (1). Thus \(H\in\mathcal T_2(\mathcal C)\). The containment
(3) follows.

Now assume there is no singleton transversal. Then \(H\) cannot have size
one. Also both points of \(H\) must lie in \(U\): a point outside \(U\)
meets no member of \(\mathcal C\), so if \(H\) contained such a point, the
other point of \(H\) would be a singleton transversal. Thus (4) follows
from (2). Since \(v\) is fixed, each possible value of \(v-e\) determines
\(e\) uniquely. \(\square\)

Lemma 8.5a.7z.3 is the no-singleton-transversal special case where
\(\mathcal C\) is the full selector cube of three two-point packets. Its
two-transversals are exactly the full pairs \(P_i\). The general form shows
the remaining witness-sharing obstruction precisely: outside a degenerate
common-point case, a witness can serve many selector deletions only if the
corresponding selector family has enough two-transversal sums to absorb all
old retained padders \(e\) below \(v-N_0\).

### Lemma 8.5a.7z.5: Common-point witness sharing forces shifted two-sum spikes

Let \(A\) be an order-2 basis with threshold \(N_0\). Let
\[
\mathcal C
\]
be a finite family of finite subsets of \(A\), and suppose one integer
\[
v
\]
has the common-hole property
\[
v\notin3(A\setminus F)\qquad(F\in\mathcal C). \tag{1}
\]
Put
\[
U=\bigcup_{F\in\mathcal C}F,\qquad K=\bigcap_{F\in\mathcal C}F.
\]
Let \(\mathcal T_2^0(\mathcal C)\) be the family of two-point
transversals
\[
H\subset U\setminus K,\qquad |H|=2,
\]
which meet every \(F\in\mathcal C\), and put
\[
\Sigma_2^0(\mathcal C)=\{\sum_{h\in H}h:H\in\mathcal T_2^0(\mathcal C)\}.
\]
Then every
\[
e\in A\setminus U,\qquad v-e\ge N_0, \tag{2}
\]
satisfies one of the following alternatives:

1. \(v-e\in\Sigma_2^0(\mathcal C)\);
2. there are \(c\in K\) and \(a\in A\) such that
   \[
   v-c=e+a. \tag{3}
   \]

Consequently, if \(R\) is a finite set of retained outside points satisfying
(2), then either
\[
|R|\le|\Sigma_2^0(\mathcal C)|
\]
or \(K\ne\varnothing\) and some \(c\in K\) satisfies
\[
r_{2,A}(v-c)\ge
\frac{|R|-|\Sigma_2^0(\mathcal C)|}{2|K|}, \tag{4}
\]
where \(r_{2,A}\) counts unordered two-term representations, with loops
allowed.

Proof. Fix \(e\) satisfying (2). Since \(v-e\ge N_0\), choose a two-term
representation
\[
v-e=a+b,\qquad a,b\in A. \tag{5}
\]
By Lemma 8.5a.7z.4, its support
\[
H=\{a,b\}
\]
meets every \(F\in\mathcal C\).

If \(H\cap K\ne\varnothing\), choose \(c\in H\cap K\). The other summand,
with the same value if (5) is a loop, gives (3). Suppose instead that
\[
H\cap K=\varnothing. \tag{6}
\]
Then \(H\subset U\). Indeed, a point outside \(U\) meets no member of
\(\mathcal C\); if such a point lay in \(H\), the other point of \(H\)
would have to meet every member of \(\mathcal C\), hence would lie in
\(K\), contradicting (6). Also \(H\) cannot be a singleton, since a
singleton transversal is exactly a point of \(K\). Thus \(H\) is a two-point
member of \(\mathcal T_2^0(\mathcal C)\), and
\[
v-e=a+b\in\Sigma_2^0(\mathcal C).
\]
This proves the dichotomy.

Now let \(R\) be finite. At most \(|\Sigma_2^0(\mathcal C)|\) elements
\(e\in R\) can satisfy the first alternative, because \(v-e\) determines
\(e\). For every remaining \(e\), choose one pair \((c_e,a_e)\) satisfying
(3). If \(K=\varnothing\) there are no remaining \(e\)'s. Otherwise, by
the pigeonhole principle, some \(c\in K\) occurs for at least
\[
\frac{|R|-|\Sigma_2^0(\mathcal C)|}{|K|}
\]
values of \(e\). These values yield representations
\[
v-c=e+a_e.
\]
One unordered representation of \(v-c\) can account for at most two choices
of \(e\), corresponding to the two elements of its support. Hence (4)
follows. \(\square\)

Thus the singleton-transversal exception in Lemma 8.5a.7z.4 is not free.
If many old retained padders lie below a shared witness and the selector
family has a common deleted point, then either the old padders are still
confined to finitely many non-common two-transversal shifts, or the common
deleted point carries a large two-sum representation spike at \(v-c\). A
counterexample must therefore make heavily shared witnesses either
selector-specific enough to avoid large outside fibers or compatible with
the high-multiplicity branches already isolated in Corollaries 3.4d and
8.5a.7f.

### Corollary 8.5a.7z.6: Shared witness classes have finite prefix capacity

Keep the hypotheses and notation of Lemma 8.5a.7z.5, and let
\[
R_v=A\cap[1,v-N_0]\setminus U.
\]
Then
\[
|R_v|\le |\Sigma_2^0(\mathcal C)|
      +2|K|\max_{c\in K} r_{2,A}(v-c), \tag{1}
\]
with the second term interpreted as \(0\) when \(K=\varnothing\).

Proof. If \(K=\varnothing\), Lemma 8.5a.7z.5 leaves only the
\(\Sigma_2^0(\mathcal C)\) alternative, and each sum value gives at most
one \(e\in R_v\).

If \(K\ne\varnothing\), let \(M=\max_{c\in K}r_{2,A}(v-c)\). If (1)
failed, then
\[
|R_v|-|\Sigma_2^0(\mathcal C)|>2|K|M,
\]
and Lemma 8.5a.7z.5 would give some \(c\in K\) with
\[
r_{2,A}(v-c)>
M,
\]
a contradiction. \(\square\)

Thus a witness value can be reused across a selector family only by paying
one of two explicit prices: a large non-common two-transversal sumset, or a
large two-sum spike at one of the common deleted colors. Since \(R_v\)
contains the old retained prefix below \(v-N_0\) outside the finite selector
union, this capacity inequality becomes stronger as the staged prefix below
the witness grows.

### Warning 8.5a.7z.7: Transversal constraints alone do not give selector escape

The shared-witness restrictions above do not by themselves rule out the
abstract product-selector barrier. Let
\[
P_i=\{p_i^0,p_i^1\}\qquad(i\ge1)
\]
be pairwise disjoint two-point packets. For each triple of indices
\[
i<j<\ell
\]
and each bit vector
\[
\varepsilon\in\{0,1\}^{\{i,j,\ell\}},
\]
let
\[
F_{\varepsilon}=
\{p_i^{\varepsilon_i},p_j^{\varepsilon_j},p_\ell^{\varepsilon_\ell}\},
\]
and group the two complementary selector triples
\[
\{F_{\varepsilon},F_{1-\varepsilon}\}
\]
as one formal witness class.

The resulting support family is pair-free and rank \(3\). Every infinite
packet selector contains one of its edges: choose any three selected packet
indices. However each two-edge complementary witness class has no singleton
transversal; its two-transversals are simply pairs choosing one point from
each of the complementary triples. Hence Lemma 8.5a.7z.4 is compatible with
the abstract barrier.

This example is not an arithmetic construction. It shows only that the
next step cannot be a pure diagonal or compactness argument from
two-transversal constraints to an escaping selector. A proof must use
additional arithmetic pressure, such as Corollary 8.5a.7z.6 forcing witness
reuse to consume old prefix capacity, or it must rule out the fully
selector-specific reflected-front construction where essentially every
selector edge receives its own private witness.

### Target 8.5a.7z.8: Rule out selector-specific reflected fronts

After Lemmas 8.5a.7z.4--8.5a.7z.5 and Corollary 8.5a.7z.6, the remaining
negative construction route for \(k=2\) has the following form. One chooses
fresh packet blocks
\[
P_i
\]
and a genuine front \(\mathcal B\) on their indices, with all edges of rank
at least \(3\). For each
\[
I\in\mathcal B
\]
and each selector
\[
\sigma\in\prod_{i\in I}P_i,
\]
one assigns a nearly private witness
\[
w_{I,\sigma}
\]
to the deletion
\[
F_{I,\sigma}=\{\sigma(i):i\in I\}.
\]
For every old retained padder \(e\) below \(w_{I,\sigma}-N_0\), the
vertex-cover condition from Lemma 10.1 requires every two-sum
representation of
\[
w_{I,\sigma}-e
\]
to meet \(F_{I,\sigma}\). Thus each such row is either a deleted-pair
exception
\[
w_{I,\sigma}-e\in F_{I,\sigma}+F_{I,\sigma}, \tag{1}
\]
or it has a deleted gate
\[
\gamma_{I,\sigma}(e)\in F_{I,\sigma}
\]
and a retained mirror
\[
w_{I,\sigma}-e-\gamma_{I,\sigma}(e)
  \in A\setminus F_{I,\sigma}. \tag{2}
\]
The \(F+F\) exception rows are the same finite exception mass isolated in
Lemma 8.4c and Corollary 8.4c.1; on large active old tests, a surviving
front must therefore produce many retained-mirror rows unless the edge rank
itself grows fast enough to absorb the exceptions.
The witness must be private enough that every three-term representation of
\(w_{I,\sigma}\) uses a point of \(F_{I,\sigma}\), while restoring any one
point of \(F_{I,\sigma}\) repairs the witness.

This route evades the shared-witness lemmas by making the classes
\(\mathcal C_v\) very small. It also evades the disjoint-window warning by
using a true front \(\mathcal B\), so every infinite packet selector
contains some protected edge. Therefore a final positive proof must show
that such reflected front data cannot be staged indefinitely: either the
gate maps \(\gamma_{I,\sigma}\) repeat over a finite palette and trigger the
certificate/recurrent-color machinery, or the mirrors in (2) force pair
cylinders, bounded second-excess edges, or large shifted spikes with stable
finite overlap. Conversely, a counterexample would have to supply a finite
extension lemma producing this data while keeping singleton and pair
deletions harmless and freezing all older witnesses below later stages.

### Diagnostic 8.5a.7z.9: The seed product cover is not a retained-mirror front

The script `EXPERIMENTS/selector_reflected_front_search.py` tests the
reflected-front bookkeeping in Target 8.5a.7z.8 on fixed finite windows.
For Example 8.5a.7z, the default run finds terminal gate-map candidates for
all eight selector triples:
```
python3 881/EXPERIMENTS/selector_reflected_front_search.py
```
However, if every old padder row is required to have a retained mirror,
```
python3 881/EXPERIMENTS/selector_reflected_front_search.py --require-retained-mirrors
```
only four candidates remain, and the missing selectors are
\[
(4,5,12),\ (10,5,8),\ (10,5,12),\ (10,11,8),\ (10,11,12).
\]
Adding the requirement that every deleted gate be active through retained
mirrors,
```
python3 881/EXPERIMENTS/selector_reflected_front_search.py --require-retained-mirrors --require-all-gates-active
```
leaves only three selector triples.

Thus Example 8.5a.7z is a terminal product-cover warning, not yet a finite
model of the stricter reflected-front skeleton. Several of its selector
witnesses rely essentially on rows with
\[
w-e\in F+F,
\]
so an iterable reflected-front construction would need either ranks large
enough to absorb these \(F+F\) exception rows or additional retained mirrors
that do not repair the private holes.

### Lemma 8.5a.7z.10: Retained-mirror rows compress to one-gate or two-gate spikes

Let \(A\) be an order-2 basis with threshold \(N_0\). Let \(F\subset A\)
be finite of size \(r\), put \(C=A\setminus F\), and suppose
\[
w\notin3C.
\]
Let
\[
R(F,w)=\{e\in C:e\le w-N_0,\ w-e\notin F+F\}.
\]
Assume that for every \(e\in R(F,w)\) one has chosen a gate
\[
\gamma(e)\in F
\]
with
\[
w-e-\gamma(e)\in C. \tag{1}
\]
If, for some \(M\), a gate \(f\in F\) has a fiber
\[
U_0=\{e\in R(F,w):\gamma(e)=f\}
\]
of size
\[
|U_0|>rM+|F+F|, \tag{2}
\]
then there is a subset \(U\subset U_0\) of size \(M\) satisfying one of the
following alternatives:

1. **unique-gate spike:**
   \[
   r_{2,A}(u+f)=1\qquad(u\in U),
   \]
   with the unique representation \(u+f\);
2. **shifted-overlap spike:** there is a fixed \(g\in F\setminus\{f\}\)
   such that
   \[
   U+f-g\subset C.
   \]

Consequently, if
\[
|R(F,w)|>r(rM+|F+F|),
\]
then some gate \(f\in F\) satisfies (2), and the same conclusion holds.

Proof. First observe that every row in \(U_0\) is private for \(f\):
\[
u+f\notin2C\qquad(u\in U_0). \tag{3}
\]
Indeed, if \(u+f=c_1+c_2\) with \(c_1,c_2\in C\), then (1) gives
\[
w=(w-u-f)+c_1+c_2\in3C,
\]
contradicting the witness.

Discard the rows with
\[
u+f\in F+F.
\]
There are at most \(|F+F|\) such rows, so by (2) more than \(rM\) rows
remain. For a remaining row \(u\), either \(u+f\) has the unique unordered
two-term representation \(u+f\) in \(A\), or it has another representation.
The latter representation cannot lie in \(2C\), by (3), and cannot use
\(f\) with complementary summand \(u\), because that is the trivial
representation. Hence it uses some
\[
g\in F\setminus\{f\}.
\]
Since the row \(u+f\notin F+F\) was not discarded, the complementary
summand is in \(C\), giving
\[
u+f-g\in C.
\]

If at least \(M\) of the remaining rows are unique, take those for \(U\).
Otherwise more than
\[
(r-1)M
\]
rows have a shifted-overlap witness \(g\in F\setminus\{f\}\), and one fixed
\(g\) occurs on at least \(M\) rows. This proves the dichotomy. The final
assertion follows by pigeonholing \(R(F,w)\) among the \(r\) gates.
\(\square\)

Thus a selector-specific reflected front cannot merely produce many
retained mirrors without creating lower-rank structure. On every edge with
a large retained-mirror row set, either a single deleted gate carries a
large unique-gate packet, or a pair of deleted gates carries a large
shifted-overlap packet. The current gap is that these one- and two-gate
spikes are not themselves late-bad singleton or pair edges: the original
witness may still be repaired by other active colors in \(F\). A final
positive proof must promote such spike supports into recurrent certificates
or genuine pair-cylinder debt; a counterexample must keep the resulting
gates and shifts moving cofinally.

### Diagnostic 8.5a.7z.11: Seed spike supports do not promote at the same witness

The reflected-front diagnostic now reports, for each unique-gate or
shifted-overlap branch from Lemma 8.5a.7z.10, whether the same witness is
already a hole after deleting only the corresponding singleton or pair.
On the strict seed run
```
python3 881/EXPERIMENTS/selector_reflected_front_search.py --require-retained-mirrors --require-all-gates-active
```
all reported promotion tests are false:
\[
\texttt{singleton\_hole\_at\_witness=False},\qquad
\texttt{pair\_hole\_at\_witness=False}.
\]
With the nearby scan
```
python3 881/EXPERIMENTS/selector_reflected_front_search.py --require-retained-mirrors --require-all-gates-active --promotion-radius 5
```
the strict retained-mirror candidates still have no singleton or pair holes
within distance \(5\) of their witnesses. If the retained-mirror and
all-gates-active restrictions are dropped, nearby pair holes do appear in
the seed set, but only in the later \((10,11,12)\) selector cases and at
new targets such as \(26,27,28\), not at the original terminal witnesses.

The companion script
```
python3 881/EXPERIMENTS/selector_pair_promotion_scan.py --require-retained-mirrors --require-all-gates-active --promotion-window nearby --nearby-radius 5
```
aggregates the shifted-overlap branches and records the actual repairs
after deleting each pair. In the strict run it finds \(6\) directed
shifted-overlap branches, no pair holes at the original witness or in the
nearby window, and each repair uses the remaining active color of the
selector. In the broader default run it finds \(34\) directed branches, no
pair holes on the original witness window \([14,23]\), and nearby holes
only in the later \((10,11,12)\) cases at \(26,27,28\).

This is expected because the seed window was chosen so that every singleton
and pair deletion remains harmless on the witness window. It is still a
useful check: Lemma 8.5a.7z.10 produces low-rank spike supports, but those
supports do not automatically inherit the original terminal hole. The
missing promotion step must therefore use recurrence across many witnesses,
stable finite palettes, or an additional argument forcing the remaining
active colors in \(F\setminus\{f,g\}\) to become irrelevant.

### Diagnostic 8.5a.7z.12: A range-separated spike need not promote to pair debt

The script `EXPERIMENTS/spike_no_promotion_gadget.py` gives an explicit
finite model of the promotion failure. With scale \(N=1000\), shift
\(h=7\), witness
\[
w=100000,
\]
and deleted set
\[
F=\{f,g,k\}=\{10007,10000,20000\},
\]
it chooses rows
\[
U=\{1,4,9,16,25,36\}
\]
and retained mirrors
\[
w-u-f\qquad(u\in U),
\]
together with shifted-overlap rows
\[
u+f-g=u+h\in A.
\]
Thus the pair \(\{f,g\}\) carries a six-row shifted-overlap spike:
\[
u+f=g+(u+h),\qquad w=f+u+(w-u-f).
\]
The script verifies all of the following finite facts:

1. \(w\notin3(A\setminus F)\);
2. restoring any one of \(f,g,k\) repairs \(w\), so \(F\) is
   inclusion-minimal for this witness;
3. deleting any pair from \(F\) still leaves a representation of \(w\);
4. the terminal retained gap above \(w-\min F-\min A\) is empty.

In particular, the shifted-overlap pair \(\{f,g\}\) is not a bad pair at
the same witness; deleting \(\{f,g\}\) leaves the \(k\)-repair. This
diagnostic is not an additive basis construction. Its role is to show that
the local promotion
\[
\text{large shifted-overlap spike}\Rightarrow\text{late-bad pair}
\]
is false without an additional recurrence or barrier argument.

### Example 8.5a.7z.12a: Arbitrarily large nonpromoting shifted spikes

The preceding diagnostic is not an isolated numerical accident. For every
finite nonempty set
\[
U\subset\mathbb N
\]
and every nonzero positive shift \(h\), choose \(N\) so large that
\[
N>10(\max U+h+1).
\]
Put
\[
w=100N,\qquad f=10N+h,\qquad g=10N,\qquad k=20N,
\]
\[
F=\{f,g,k\},
\]
and
\[
C=U\cup(U+h)\cup\{90N-h-u:u\in U\}\cup\{37N,43N\}.
\]
Let
\[
A_0=C\cup F.
\]
Then:

1. \(w\notin3C\);
2. \(F\) is inclusion-minimal for the witness \(w\);
3. deleting any two points of \(F\) still leaves a representation of \(w\)
   from \(A_0\);
4. the pair \(\{f,g\}\) carries a shifted-overlap spike on \(U\):
   \[
   w=f+u+(90N-h-u),\qquad u+f=g+(u+h)\qquad(u\in U);
   \]
5. the retained terminal interval
   \[
   (w-\min F-\min A_0,\ w-1]
   \]
   is disjoint from \(C\).

Proof. The repair identities in (4) are immediate, and they also show that
restoring \(f\) repairs \(w\). Restoring \(g\) repairs \(w\) by
\[
w=g+(u+h)+(90N-h-u)\qquad(u\in U),
\]
and restoring \(k\) repairs \(w\) by
\[
w=k+37N+43N. \tag{1}
\]
Thus \(F\) is inclusion-minimal once \(w\notin3C\) is proved. Moreover,
after deleting \(\{f,g\}\), (1) remains; after deleting \(\{f,k\}\), the
\(g\)-repair remains; after deleting \(\{g,k\}\), the \(f\)-repair remains.
This proves (2) and (3), assuming (1).

It remains to check that \(w\notin3C\). Let
\[
B=\max U+h.
\]
The set \(C\) is contained in the union of the low interval \([1,B]\), the
two middle points
\[
37N,\quad43N,
\]
and the high interval
\[
[90N-h-\max U,\ 90N-h-\min U].
\]
A sum using at least two high terms exceeds \(w\), while a sum using one
high term and one middle term also exceeds \(w\). A sum using one high term
and two low terms is at most
\[
90N-h-\min U+2B<92N<w,
\]
by the choice of \(N\). Thus no representation of \(w\) uses a high term.

Without high terms, a sum with at most one middle term is less than
\[
43N+2B<44N.
\]
A sum with two middle terms has middle-part coefficient in
\[
\{74,80,86\}N.
\]
Adding one low term cannot reach \(100N\), because the only positive gap
below \(100N\) that is smaller than \(N\) would have to occur among these
coefficients, and none does. A sum of three middle terms has coefficient in
\[
\{111,117,123,129\}N,
\]
which again never equals \(100N\). This proves \(w\notin3C\).

Finally, \(\min A_0=\min U\) and \(\min F=g=10N\). The left endpoint of the
terminal interval is
\[
w-g-\min U=90N-\min U.
\]
Every high retained point is at most
\[
90N-h-\min U<90N-\min U,
\]
and all other retained points are far below. Hence the displayed terminal
interval is disjoint from \(C\). \(\square\)

Thus the nonpromotion obstruction can have arbitrarily large shifted fibers
even in the terminal-gap normal form. The finite local data from Lemma
8.5a.7z.10 cannot by itself produce pair-cylinder debt; the proof must use
global repetition, palette stabilization, or some additional pressure from
the product-selector barrier.

This example also isolates what it does **not** do. It is very far from a
finite stage of an order-2 basis. With the notation above and
\[
B=\max U+h,
\]
all elements of \(A_0\) below \(9N\) lie in \([1,B]\). Hence
\[
2A_0\cap(2B,\ 10N)=\varnothing. \tag{2}
\]
Thus the construction has a macroscopic two-sum coverage gap before even
reaching the first deleted gate. The example only disproves a local
promotion lemma; a counterexample stage would still have to add enough
coverage fillers to bridge such gaps without repairing the protected
rank-three witnesses or creating stable finite-palette spikes.

### Diagnostic 8.5a.7z.12b: Low-interval fillers repair private sums

The simplest way to fill the gap (2) is also immediately dangerous. In the
notation of Example 8.5a.7z.12a, suppose a retained low interval
\[
[1,R]
\]
is adjoined to \(C\). If
\[
2R\ge f+u
\]
for some \(u\in U\), then \(w\) is repaired without any deleted gate. Indeed
choose \(a,b\in[1,R]\) with \(a+b=f+u\). The retained mirror
\[
w-f-u=90N-h-u
\]
belongs to \(C\), so
\[
w=a+b+(w-f-u).
\]
In particular, the first private spike row \(u_0=\min U\) is repaired as
soon as
\[
R\ge \left\lceil{f+u_0\over2}\right\rceil.
\]

The script `spike_interval_filler_pressure.py` verifies this threshold in
the default finite instance \(N=1000,h=7,U=\{1,4,9,16,25,36\}\). With the
minimal middle repair packet \(\{37N,43N\}\), \(R=5003\) leaves the witness
unrepaired, while \(R=5004\) gives
\[
100000=5004+5004+89992.
\]
Thus the no-promotion spike gadget cannot be turned into a stage merely by
adding a long retained interval through the first private sums; such
fillers repair the very witness they are meant to protect.

### Diagnostic 8.5a.7z.12c: The first coverage gap is bridgeable

The previous diagnostic should not be overread. The first two-sum coverage
gap in Example 8.5a.7z.12a can be bridged locally without repairing the
protected witness, as long as the retained fillers stay out of the private
two-sums and out of the middle-packet complements of \(w\).

The script `spike_safe_filler_profile.py` verifies this in the same finite
instance \(N=1000,h=7,U=\{1,4,9,16,25,36\}\). It adjoins to the retained
set the low band
\[
[1,5003]
\]
and the upper band
\[
[10044,15000]\setminus\{14000\}.
\]
The low band stops just before its two-sum interval reaches the first
private spike sum \(10008\). The upper band starts just after the last
private spike sum \(10043\). The point \(14000\) is removed because
\[
100000=43000+43000+14000.
\]
With these fillers, the full set \(C\cup F\) has continuous two-sum
coverage from \(2\) through \(30000\), while the retained two-sumset still
misses every private spike sum
\[
10008,10011,10016,10023,10032,10043,
\]
and
\[
100000\notin3C.
\]

Thus the local no-promotion gadget is not defeated merely by asking for
some initial order-2 coverage. What remains missing from a genuine stage is
the frozen-witness requirement: the declared coverage endpoint must pass
the witness, or later elements below \(w\) may repair it. Once one tries to
cover that far, every retained filler \(e\le w-N_0\) forces the shifted
target \(w-e\) to be covered only through deleted gates, returning exactly
to the reflected-front and compressed-spike obligations of Lemma
8.5a.7z.10.

### Corollary 8.5a.7z.12d: Frozen filler blocks force compressed spikes

Let \(A\) be an order-2 basis with threshold \(N_0\). Let \(F\subset A\)
be finite of size \(r\), put \(C=A\setminus F\), and suppose
\[
w\notin3C.
\]
Let \(I\subset C\) be finite and satisfy
\[
e\le w-N_0,\qquad w-e\notin F+F\qquad(e\in I). \tag{1}
\]
If
\[
|I|>r(rM+|F+F|),
\]
then some gate \(f\in F\) and some \(U\subset I\) of size \(M\) satisfy one
of the two alternatives from Lemma 8.5a.7z.10:

1. \(r_{2,A}(u+f)=1\) for every \(u\in U\);
2. there is a fixed \(g\in F\setminus\{f\}\) such that
   \[
   U+f-g\subset C.
   \]

Proof. For each \(e\in I\), condition (1) gives \(w-e\ge N_0\), so choose
a two-term representation
\[
w-e=a_e+a'_e,\qquad a_e,a'_e\in A.
\]
If both summands lay in \(C\), then adding \(e\) would put \(w\) in \(3C\),
contrary to the hypothesis. Since \(w-e\notin F+F\), the representation
cannot use two summands from \(F\). Hence it uses exactly one point
\[
\gamma(e)\in F
\]
and one point \(w-e-\gamma(e)\in C\). Thus \(I\subset R(F,w)\) with a gate
map on the restricted row set \(I\). By pigeonhole, some \(f\in F\) has
more than \(rM+|F+F|\) rows of \(I\) assigned to it. The proof of Lemma
8.5a.7z.10 applied to this restricted fiber gives the claimed subset
\(U\subset I\) and compressed-spike alternative.
\(\square\)

This is the formal version of the stage burden exposed by Diagnostic
8.5a.7z.12c. Initial fillers can bridge early two-sum gaps while the witness
lies far beyond the coverage endpoint. Once the endpoint is pushed past the
witness, any large safe filler block below the witness is no longer inert:
it supplies a large reflected row set, and therefore either falls into the
stable finite-palette closures or joins the moving compressed-spike front of
Target 8.5a.7z.14.

In particular, a genuinely one-gate terminal construction is not a new
remaining route for \(k=2\). If \(F=\{f\}\) gives infinitely many late
singleton holes, Corollaries 8.3 and 8.3b put the basis in the already
closed reflection-recurrent case, or else remove all but finitely many such
singletons from the counterexample tail. The surviving one-gate-looking
objects are only unique-gate fibers inside larger active edges \(F\), where
other active colors may repair the singleton deletion. Those are exactly
the unique-gate branch in Lemma 8.5a.7z.10, not a finite-accelerator
shortcut.

### Lemma 8.5a.7z.12e: One-step safe filler criterion

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let \(p\notin2A\). A single retained filler
\[
x\notin A
\]
can be adjoined so that
\[
p\in2(A\cup\{x\}),\qquad w\notin3(C\cup\{x\})
\]
only if
\[
x\in X_p:=\{p-a:a\in A,\ p-a>0\}\cup
\begin{cases}
\{p/2\},&p\text{ even},\\
\varnothing,&p\text{ odd},
\end{cases}
\tag{1}
\]
and
\[
w-x\notin2C,\qquad w-2x\notin C,\qquad 3x\ne w. \tag{2}
\]
Conversely, any \(x\in X_p\setminus A\) satisfying (2) gives such a
one-point safe extension.

Proof. The condition \(p\in2(A\cup\{x\})\) while \(p\notin2A\) means that
some representation of \(p\) uses \(x\). This is exactly (1): either
\[
p=x+a\quad(a\in A)
\]
or \(p=x+x\). Since \(w\notin3C\), the only new ways to put \(w\) in
\[
3(C\cup\{x\})
\]
are
\[
w=x+c_1+c_2,\qquad w=2x+c,\qquad w=3x
\]
with \(c,c_1,c_2\in C\). These are excluded exactly by (2). \(\square\)

### Lemma 8.5a.7z.12e': Next-gap finite batches reduce to one or two points

Let \(C,F,A,w,p\) be as in Lemma 8.5a.7z.12e, with
\[
p\notin2A,\qquad w\notin3C.
\]
Suppose \(S\subset\mathbb N\setminus A\) is finite and
\[
p\in2(A\cup S),\qquad w\notin3(C\cup S). \tag{1}
\]
Then either:

1. there is \(x\in S\) such that \(x\) is a one-point safe extension
   covering \(p\), as in Lemma 8.5a.7z.12e; or
2. there are \(x,y\in S\), possibly equal only if the representation uses
   two copies of the same new value, such that
   \[
   x+y=p,\qquad w\notin3(C\cup\{x,y\}). \tag{2}
   \]

Consequently, if neither a one-point safe extension nor a two-point safe
batch exists for the next gap \(p\), then no finite retained batch can cover
\(p\) while preserving \(w\notin3C\).

Proof. Since \(p\notin2A\), any representation of \(p\) from \(A\cup S\)
uses at least one point of \(S\). If it uses exactly one new point \(x\),
then \(p=x+a\) for some \(a\in A\). The second part of (1) implies
\[
w\notin3(C\cup\{x\}),
\]
so Lemma 8.5a.7z.12e applies. If the representation uses two new points
\(x,y\), then \(x+y=p\), and again (1) implies (2), because
\[
C\cup\{x,y\}\subset C\cup S.
\]
This proves the dichotomy and the final assertion. \(\square\)

### Lemma 8.5a.7z.12e'': Reflected next-gap blockers

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let
\[
p\notin2A,\qquad d=w-p.
\]
Assume that
\[
d\in C \tag{1}
\]
and that for every \(a\in A\) such that
\[
x=p-a>0,\qquad x\notin A,
\]
one has
\[
d+a\in2C. \tag{2}
\]
Then no finite retained batch
\[
S\subset\mathbb N\setminus A
\]
can satisfy both
\[
p\in2(A\cup S)
\]
and
\[
w\notin3(C\cup S).
\]

Proof. Suppose such an \(S\) existed. By Lemma 8.5a.7z.12e', either there
is a one-point safe extension \(x\in S\) covering \(p\), or there is a
two-point safe batch \(x,y\in S\) with \(x+y=p\).

In the first case, \(p=x+a\) for some \(a\in A\), with \(x=p-a>0\) and
\(x\notin A\). By (2), write
\[
d+a=c_1+c_2,\qquad c_1,c_2\in C.
\]
Then
\[
w=p+d=x+a+d=x+c_1+c_2\in3(C\cup\{x\}),
\]
contradicting safety. In the second case, (1) gives
\[
w=p+d=x+y+d\in3(C\cup\{x,y\}),
\]
again contradicting safety. Therefore no such \(S\) exists. \(\square\)

### Corollary 8.5a.7z.12e''': Deleted-gate reflection is the only extra check

In the setting of Lemma 8.5a.7z.12e'', write
\[
A=C\cup F
\]
with \(C\) retained and \(F\) deleted. If
\[
d=w-p\in C \tag{1}
\]
and
\[
d+f\in2C\qquad(f\in F), \tag{2}
\]
then no finite retained batch can cover the next gap \(p\) while preserving
\[
w\notin3C.
\]

Proof. Lemma 8.5a.7z.12e'' requires \(d+a\in2C\) for every old summand
\[
a\in A
\]
that could pair with a new point to cover \(p\). For \(a\in C\), this is
automatic from (1), since
\[
d+a\in C+C=2C.
\]
For \(a\in F\), it is exactly (2). Thus Lemma 8.5a.7z.12e'' applies.
\(\square\)

### Corollary 8.5a.7z.12g: Fixed-rank reflected blocker defects are bounded

Assume now that \(A\) is an order-\(2\) basis with threshold \(N_0\), that
\[
F\subset A
\]
is finite, and put
\[
C=A\setminus F.
\]
Let
\[
w\notin3C.
\]
If \(T\subset C\) is finite and satisfies
\[
w-\max T\ge N_0,\qquad T+F\subseteq2C, \tag{1}
\]
then
\[
|T|\le |F+F|. \tag{2}
\]

In particular, for a fixed deleted packet \(F\), there are at most
\[
|F+F|
\]
retained complements \(d=w-p\in C\), with \(p\ge N_0\), for which
\[
d+F\subseteq2C.
\]
For every such complement whose \(p=w-d\) is a genuine next gap of \(2A\),
Corollary 8.5a.7z.12e''' gives a reflected finite-batch blocker.

Proof. The bound is exactly Corollary 8.4c.1 applied to the test set
\[
T.
\]
The final assertion is Corollary 8.5a.7z.12e''' with \(d=w-p\). \(\square\)

### Corollary 8.5a.7z.12g.1: Retained-defect gaps require private gates

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let
\[
d\in C,\qquad p=w-d.
\]
If
\[
p=f+c,\qquad f\in F,\quad c\in C, \tag{1}
\]
then necessarily
\[
d+f\notin2C. \tag{2}
\]
Consequently, if
\[
d+F\subseteq2C \tag{3}
\]
and
\[
p\notin F+F, \tag{4}
\]
then
\[
p\notin2A.
\]

Proof. If (1) holds and \(d+f=c_1+c_2\) with \(c_1,c_2\in C\), then
\[
w=d+p=d+f+c=c_1+c_2+c\in3C,
\]
contrary to the hypothesis. This proves (2).

For the consequence, \(p\notin C+C\), since otherwise \(w=d+p\in3C\). The
condition (3) and the first part rule out \(p\in F+C\), while (4) rules out
\(p\in F+F\). Hence \(p\notin2A\). \(\square\)

### Lemma 8.5a.7z.12h: One-sided pair-saturation blockers

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C,\qquad p\notin2A.
\]
Let
\[
X_p=\{p-a:a\in A,\ p-a>0\}\cup
\begin{cases}
\{p/2\},&p\text{ even},\\
\varnothing,&p\text{ odd}.
\end{cases}
\]
Assume:

1. for every \(x\in X_p\setminus A\),
   \[
   w-x\in2C; \tag{1}
   \]
2. for every split
   \[
   x+y=p,\qquad 1\le x<y,\qquad x,y\notin A,
   \]
   at least one of
   \[
   w-x\in2C,\qquad w-y\in2C \tag{2}
   \]
   holds.

Then no finite retained batch \(S\subset\mathbb N\setminus A\) can satisfy
\[
p\in2(A\cup S),\qquad w\notin3(C\cup S).
\]

Proof. By Lemma 8.5a.7z.12e', any such finite batch contains either a
one-point repair \(x\in X_p\setminus A\) of the gap \(p\), or a two-point
repair \(x+y=p\) with \(x,y\notin A\). In the one-point case, (1) gives
\[
w=x+c_1+c_2
\]
with \(c_1,c_2\in C\), contradicting \(w\notin3(C\cup S)\). In the
two-point case, (2) gives the same contradiction using whichever of
\[
x,\ y
\]
has its complement in \(2C\). \(\square\)

### Lemma 8.5a.7z.12h.1: One-point shadows are external translate absorption

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
let
\[
w\notin3C,\qquad p\notin2A,\qquad d=w-p.
\]
Let \(T\subset A\) be a finite set of old summands such that
\[
p-a>0,\qquad p-a\notin A\qquad(a\in T). \tag{1}
\]
Then the one-new candidates
\[
x_a=p-a\qquad(a\in T)
\]
are all blocked by the pair-saturation condition
\[
w-x_a\in2C \tag{2}
\]
if and only if
\[
d+T\subseteq2C. \tag{3}
\]

Consequently, one-sided saturation has only two local forms:

1. if \(d\in C\), then retained old summands are reflected automatically,
   and only deleted old summands need the extra checks of Corollary
   8.5a.7z.12e''';
2. if \(d\notin C\), then the obstruction is not a retained-row wall but an
   external translate absorption
   \[
   T+d\subseteq2C.
   \]

Proof. For each \(a\in T\),
\[
w-x_a=w-(p-a)=w-p+a=d+a.
\]
Thus (2) is exactly (3). The two local forms are just the alternatives
\[
d\in C,\qquad d\notin C.
\]
In the first alternative, \(d+a\in2C\) is automatic for every \(a\in C\),
and the only nonautomatic old summands are the deleted ones \(a\in F\).
The second alternative is precisely an absorbed translate by a center not
available as a retained row. \(\square\)

### Corollary 8.5a.7z.12h.2: Escape-set form of one-sided saturation

Keep the notation of Lemma 8.5a.7z.12h.1. Define the old-row escape set
\[
R=\{a\in A:p-a>0,\ p-a\notin A,\ d+a\notin2C\}
\]
and the split escape set
\[
E=\{z\in[1,p-1]\setminus A:d+z\notin2C\}.
\]
Assume:

1. \(R=\varnothing\);
2. there are no \(x<y\) in \(E\) with \(x+y=p\);
3. if \(p\) is even and \(p/2\notin A\), then at least one of
   \[
   d+p/2\in2C,\qquad d\in C,\qquad 3p/2=w \tag{1}
   \]
   holds.

Then no finite retained batch \(S\subset\mathbb N\setminus A\) can satisfy
\[
p\in2(A\cup S),\qquad w\notin3(C\cup S).
\]

Proof. By Lemma 8.5a.7z.12e', it is enough to rule out one-point repairs
and two-point repairs of \(p\).

A one-point repair using an old summand has the form
\[
p=x+a,\qquad a\in A,\quad x=p-a\notin A.
\]
Since \(R=\varnothing\), it has \(d+a\in2C\), equivalently
\[
w-x=d+a\in2C,
\]
so it repairs the witness and is unsafe. The only one-point repair not of
this form is the double repair \(p=x+x\). If it exists, then \(x=p/2\notin
A\), and condition (3) is exactly one of the three obstructions
\[
w-x\in2C,\qquad w-2x\in C,\qquad 3x=w
\]
from Lemma 8.5a.7z.12e.

Finally, a two-point repair has
\[
x+y=p,\qquad x,y\notin A.
\]
If \(x<y\), condition (2) says at least one of \(x,y\) is not in \(E\), so
one of
\[
d+x\in2C,\qquad d+y\in2C
\]
holds. Equivalently, one of
\[
w-y\in2C,\qquad w-x\in2C
\]
holds, and the two-point repair is unsafe. The case \(x=y\) is the
one-point double repair already handled. \(\square\)

### Warning 8.5a.7z.12h.3: Large escape sets need not contain complementary pairs

Corollary 8.5a.7z.12h.2 cannot be closed by a cardinality lower bound on
the split escape set alone. Any set
\[
E\subset(p/2,p)
\]
has no two distinct elements summing to \(p\), regardless of its size.
More generally, if \(E\subset[1,p-1]\setminus A\) has no complementary
pair, then every low escape
\[
z\in E,\qquad z<p/2,
\]
has its complement \(p-z\) blocked in exactly one of two ways:
\[
p-z\in A
\]
or
\[
p-z\notin A,\qquad d+p-z\in2C.
\]

Thus a proof must force low escape mass whose complements are not already
old elements and are not absorbed by \(2C\). It is not enough to show that
the escape set is large.

Proof. If \(z\in E\), \(z<p/2\), and \(p-z\notin A\), then the absence of a
complementary pair in \(E\) forces \(p-z\notin E\). By the definition of
\[
E=\{y\in[1,p-1]\setminus A:d+y\notin2C\},
\]
this is exactly \(d+p-z\in2C\). \(\square\)

### Warning 8.5a.7z.12h.4: Interval-stage coverage does not balance the escape set

The missing hypothesis in Warning 8.5a.7z.12h.3 is not supplied by ordinary
initial interval coverage, even together with a genuine inclusion-minimal
terminal hole.

Let \(L\ge2\) and choose \(N>3L\). Put
\[
C=[1,L]\cup[N,N+L-1],
\]
\[
p=2L+1,\qquad q=N+2L,\qquad F=\{p,q\},
\]
\[
A=C\cup F,\qquad d=2N+L-2,\qquad w=p+d=2N+3L-1.
\]
Then
\[
[2,p-1]=[2,2L]\subseteq2A,
\]
because the low interval \([1,L]\) contributes all sums up to \(2L\), while
\[
p\notin2A.
\]
Indeed, two low terms sum to at most \(2L\), and every term outside
\([1,L]\) is already larger than \(p\).

Moreover
\[
w\notin3C.
\]
The possible three-sum ranges from \(C\) are
\[
[3,3L],\quad [N+2,N+3L-1],\quad
[2N+1,2N+3L-2],\quad [3N,3N+3L-3],
\]
and \(w=2N+3L-1\) lies strictly between the third and fourth ranges because
\(N>3L\). The two deleted gates are active:
\[
w=p+N+(N+L-2)=q+1+(N+L-2),
\]
with the displayed retained summands in \(C\). Hence \(F\) is
inclusion-minimal for this hole.

For every old summand \(a\in A\) with
\[
p-a>0,\qquad p-a\notin A,
\]
one has \(a\in[1,L]\), and therefore
\[
d+a\in[2N+L-1,2N+2L-2]\subseteq2C.
\]
Thus the old-row escape set \(R\) of Corollary 8.5a.7z.12h.2 is empty.

On the other hand,
\[
[1,p-1]\setminus A=\{L+1,\ldots,2L\},
\]
and for every such \(z\),
\[
d+z\in[2N+2L-1,2N+3L-2],
\]
which is disjoint from \(2C\). Hence the split escape set is exactly
\[
E=\{L+1,\ldots,2L\}.
\]
It has no complementary pair summing to \(p=2L+1\), since it lies entirely
above \(p/2\). Thus a proof forcing safe two-point repairs must use a
balance, recurrence, or staging hypothesis beyond initial interval coverage
and minimal terminal-hole structure.

The script `EXPERIMENTS/shadow_escape_counterexample.py` verifies this
family; for example, \(L=5,N=20\) gives
\[
C=\{1,2,3,4,5,20,21,22,23,24\},\quad F=\{11,30\},
\]
\[
p=11,\quad d=43,\quad w=54,\quad E=\{6,7,8,9,10\}.
\]

### Warning 8.5a.7z.12h.4a: Shadow complements need not be covered runways

The high-sided shadow example can be tuned so that the retained complements
of the shadows are numerous, but their future targets remain almost entirely
uncovered by the old full set. Thus Corollary 8.5a.7z.12h.9 genuinely needs
a large covered-runway hypothesis.

Let \(L\ge2\), choose \(N>4L\), and put
\[
C=[1,L]\cup[N,N+L-1],
\]
\[
p=2L+1,\qquad q=N+3L-2,\qquad F=\{p,q\},
\]
\[
A=C\cup F,\qquad d=2N+L-2,\qquad w=p+d=2N+3L-1.
\]
As in Warning 8.5a.7z.12h.4,
\[
[2,p-1]\subseteq2A,\qquad p\notin2A,\qquad w\notin3C,
\]
and there are no old-row escapes. The deleted gates are active because
\[
w=p+N+(N+L-2)=q+1+N.
\]
The split escape set is still
\[
E=\{L+1,\ldots,2L\}\subset(p/2,p),
\]
with no complementary pair.

Now take its retained complement runway
\[
X=p-E=\{1,\ldots,L\}\subset C.
\]
Only the first row has its future target covered by the old full set:
\[
w-1=q+N\in2A.
\]
For \(2\le x\le L\),
\[
w-x\in[2N+2L-1,\ 2N+3L-3],
\]
which lies strictly between the retained high-high interval
\[
[2N,\ 2N+2L-2]\subset2C
\]
and the \(q\)-high interval
\[
[2N+3L-2,\ 2N+4L-3]\subset q+C.
\]
The remaining \(F+F\) and low-involving ranges are outside this interval
when \(N>4L\). Hence
\[
\{x\in X:w-x\in2A\}=\{1\}.
\]
Thus the large shadow-complement block falls into the old full two-sum gap
alternative of Corollary 8.5a.7z.12h.8, not into the covered-runway
compression of Corollary 8.5a.7z.12h.9.

The same computation explains why this local cartridge does not itself
build a selector counterexample. If a shadow point
\[
z\in E
\]
is promoted into \(A\) as a retained point, then
\[
w-z=d+(p-z)\in2C,
\]
because \(p-z\in[1,L]\). Hence
\[
w=z+(w-z)\in3(C\cup\{z\}),
\]
so the old witness is immediately repaired. A promoted shadow can preserve
the witness only by joining the deleted packet for that witness. Therefore
the two-interval cartridge converts promoted shadows into packet debt; by
itself it supplies local whole-cut structure, not a cross-window selector
barrier.

The script `EXPERIMENTS/shadow_escape_counterexample.py` verifies this
variant with
`--q-policy sparse-covered`; for example \(L=5,N=25\) gives
\[
q=38,\qquad E=\{6,7,8,9,10\},\qquad X=\{5,4,3,2,1\},
\]
and reports that the covered complement runway has size \(1\), while every
promoted shadow point repairs \(w\) if retained.

### Lemma 8.5a.7z.12h.5: Safe fillers create future-defect debt

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let \(x\in C\) and put
\[
p=w-x.
\]
Assume
\[
x+F\subseteq2C \tag{1}
\]
and
\[
p\notin F+F. \tag{2}
\]
Then
\[
p\notin2A,
\]
and no finite retained batch can cover \(p\) while preserving
\[
w\notin3C.
\]

Proof. This is Corollary 8.5a.7z.12g.1 with \(d=x\), followed by Corollary
8.5a.7z.12e''' for the resulting gap \(p=w-x\). \(\square\)

Thus a retained filler added safely below a fixed witness is not inert. If
the stage later needs to cover the gap \(w-x\), it must keep a private
deleted-gate incidence
\[
x+f\notin2C
\]
available for some \(f\in F\), or else change the active packet/witness
before reaching that gap. Otherwise \(x\) becomes the retained defect of a
reflected wall.

### Lemma 8.5a.7z.12h.6: Surviving future defects create private-gate fibers

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let \(X\subset C\) be finite and assume that for each \(x\in X\):

1. the later target
   \[
   p_x=w-x
   \]
   is not a retained two-sum:
   \[
   p_x\notin2C; \tag{1}
   \]
2. it is not a deleted-pair exception:
   \[
   p_x\notin F+F; \tag{2}
   \]
3. it is covered by the full old packet:
   \[
   p_x\in2A. \tag{3}
   \]

Then every \(x\in X\) has at least one deleted gate \(f\in F\) such that
\[
w-x-f\in C,\qquad x+f\notin2C. \tag{4}
\]
Consequently, some \(f\in F\) supports a fiber
\[
X_f=\{x\in X:w-x-f\in C,\ x+f\notin2C\}
\]
with
\[
|X_f|\ge |X|/|F|. \tag{5}
\]

Proof. Fix \(x\in X\). By (3), choose a two-term representation
\[
p_x=s_1+s_2,\qquad s_i\in A.
\]
It cannot use two retained summands by (1), and it cannot use two deleted
summands by (2). Hence it uses exactly one deleted gate \(f\in F\) and one
retained summand \(c\in C\), so
\[
w-x=p_x=f+c,
\]
or \(c=w-x-f\in C\). If \(x+f\in2C\), say \(x+f=c_1+c_2\), then
\[
w=x+f+c=c_1+c_2+c\in3C,
\]
contrary to the hypothesis. This proves (4). Pigeonholing the chosen gates
over \(F\) gives (5). \(\square\)

Thus any stage that keeps many retained fillers \(x\) alive until their
future defects \(w-x\) must create a large private-gate fiber. This is the
same row pattern compressed by Lemma 8.5a.7z.10: after large enough tests,
one either gets a unique-gate packet or a shifted-overlap packet, unless the
active gates and row tests move cofinally.

### Corollary 8.5a.7z.12h.7: Future-defect trichotomy

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
For \(x\in C\), put
\[
p_x=w-x.
\]
Assume
\[
p_x\notin F+F. \tag{1}
\]
Then exactly one of the following can happen:

1. \(p_x\notin2A\); in this case \(p_x\) is an old full two-sum gap.
2. \(p_x\in2A\); in this case there is a deleted gate \(f\in F\) such that
   \[
   w-x-f\in C,\qquad x+f\notin2C. \tag{2}
   \]

In particular, if
\[
x+F\subseteq2C, \tag{3}
\]
then only the first alternative can hold. If later \(p_x\) is the next gap
to be covered while the same witness and packet are frozen, Lemma
8.5a.7z.12h.5 turns it into a reflected finite-batch wall.

Proof. Since \(x\in C\) and \(w\notin3C\), one cannot have
\[
p_x\in2C,
\]
for then \(w=x+p_x\in3C\). If \(p_x\in2A\), condition (1) and
\[
p_x\notin2C
\]
force every two-term representation of \(p_x\) from \(A\) to use exactly
one element of \(F\) and one element of \(C\). Choosing such a
representation gives
\[
p_x=f+c,\qquad f\in F,\quad c\in C.
\]
Then \(c=w-x-f\). If \(x+f\in2C\), adding \(c\) would put \(w\) in \(3C\),
so \(x+f\notin2C\). This proves (2).

If (3) holds, (2) is impossible, and therefore \(p_x\notin2A\). The final
sentence is Lemma 8.5a.7z.12h.5. \(\square\)

### Corollary 8.5a.7z.12h.8: Fixed-witness runway dichotomy

Let \(C,F\subset\mathbb N\) be finite and disjoint, put \(A=C\cup F\), and
suppose
\[
w\notin3C.
\]
Let \(X\subset C\) be finite and assume
\[
w-x\notin F+F\qquad(x\in X). \tag{1}
\]
For each \(x\in X\), put \(p_x=w-x\), and define
\[
G=\{x\in X:p_x\notin2A\}. \tag{2}
\]
Then either \(G\) is large, or one deleted gate carries a large private
fiber: more precisely, there is \(f\in F\) such that
\[
\left|\{x\in X\setminus G:w-x-f\in C,\ x+f\notin2C\}\right|
\ge \frac{|X|-|G|}{|F|}. \tag{3}
\]
In particular, if all future targets are already covered by the full old
packet,
\[
w-X\subseteq2A, \tag{4}
\]
then some \(f\in F\) supports a private fiber of size at least
\[
|X|/|F|. \tag{5}
\]

Proof. Apply Corollary 8.5a.7z.12h.7 to each \(x\in X\setminus G\). Since
\[
p_x=w-x\in2A
\]
and \(p_x\notin F+F\), that corollary supplies at least one gate
\[
f_x\in F
\]
with
\[
w-x-f_x\in C,\qquad x+f_x\notin2C.
\]
Pigeonholing the map \(x\mapsto f_x\) over \(F\) gives (3). If (4) holds,
then \(G=\varnothing\), giving (5). \(\square\)

Thus a long fixed-witness coverage runway has only two ways to avoid the
reflected-wall outcome: leave many future targets uncovered by the old full
set, or create a large private-gate fiber. The latter is precisely the
input to the compressed-spike reduction of Lemma 8.5a.7z.10.

### Corollary 8.5a.7z.12h.9: Covered runways compress to spikes

Let \(A\) be an order-\(2\) basis with threshold \(N_0\). Let
\[
F\subset A,\qquad |F|=r,
\]
put \(C=A\setminus F\), and suppose
\[
w\notin3C.
\]
Let \(X\subset C\) be finite and assume:

1. the rows are active for the order-\(2\) threshold,
   \[
   x\le w-N_0\qquad(x\in X); \tag{1}
   \]
2. they are not deleted-pair exceptions,
   \[
   w-x\notin F+F\qquad(x\in X); \tag{2}
   \]
3. all but \(G\subset X\) have future targets already covered by the old
   full packet,
   \[
   w-x\in2A\qquad(x\in X\setminus G). \tag{3}
   \]

If for some \(M\)
\[
|X|-|G|>r(rM+|F+F|), \tag{4}
\]
then there are a gate \(f\in F\) and a set
\[
U\subset X\setminus G,\qquad |U|=M,
\]
satisfying one of the two alternatives from Lemma 8.5a.7z.10:

1. **unique-gate spike:**
   \[
   r_{2,A}(u+f)=1\qquad(u\in U);
   \]
2. **shifted-overlap spike:** there is \(g\in F\setminus\{f\}\) such that
   \[
   U+f-g\subset C.
   \]

Proof. For each \(x\in X\setminus G\), hypotheses (1) and (2) put
\[
x\in R(F,w)
\]
in the notation of Lemma 8.5a.7z.10. Corollary 8.5a.7z.12h.8 gives a gate
\[
f\in F
\]
whose private fiber
\[
U_0=\{x\in X\setminus G:w-x-f\in C,\ x+f\notin2C\}
\]
has size at least
\[
\frac{|X|-|G|}{r}.
\]
By (4), this fiber satisfies
\[
|U_0|>rM+|F+F|.
\]
For all rows in \(U_0\), the condition \(w-x-f\in C\) is exactly the gate
condition required by Lemma 8.5a.7z.10, and \(U_0\subset R(F,w)\). Extend
the choice \(\gamma(x)=f\) on \(U_0\) to any valid gate map on \(R(F,w)\);
such an extension exists because, for every \(e\in R(F,w)\), the assumptions
that \(A\) is an order-\(2\) basis, \(e\le w-N_0\), \(w-e\notin F+F\), and
\(w\notin3C\) rule out both \(F+F\) and \(2C\) representations of \(w-e\).
The resulting \(f\)-fiber contains \(U_0\), so the fiber form of Lemma
8.5a.7z.10 gives the claimed subset \(U\) and one of the two spike
alternatives. \(\square\)

Thus a fixed witness cannot have a long covered runway without immediately
feeding the stable-spike closure machinery. The only remaining runway
escape is to leave many \(w-x\) as old full two-sum gaps, or to keep the
row tests, gates, and witnesses moving before any finite test exceeds the
threshold in (4).

The hypothesis is intentionally reflected, not merely metric. A coarse
coverage threshold such as \(2A\) covering past \(0.6w\) cannot replace it:
for \(C=[1,L]\), \(F=\varnothing\), and \(w=3L+4\), one has
\[
w\notin3C,\qquad 2C=[2,2L],
\]
so coverage reaches asymptotic ratio \(2/3\) of \(w\), but the next gap
\[
p=2L+1
\]
has the safe one-point filler \(x=L+1\), since
\[
w-x=2L+3\notin2C,\qquad w-2x=L+2\notin C,\qquad 3x\ne w.
\]

### Diagnostic 8.5a.7z.12f: Safe extension stalls below the witness

The script `spike_safe_extension_search.py` applies Lemma 8.5a.7z.12e to
the safe filler profile from Diagnostic 8.5a.7z.12c. It checks whether the
stalled next gap can be covered by a safe two-point batch \(x+y=p\), and
optionally allows such two-point batches as moves earlier in the beam
search. To keep the beam search finite, its default scale is \(N=100\), with
the same rows
\[
U=\{1,4,9,16,25,36\},
\]
deleted gates
\[
F=\{1000,1007,2000\},
\]
and witness
\[
w=10000.
\]
The initial safe filler profile has full two-sum coverage through \(3000\).
With beam \(8\), the one-point extension search keeps \(w\notin3C\) and
extends coverage only to \(6488\), then stalls at the next gap \(6489\).
It reports \(1031\) possible one-point blockers for that next gap, all
unsafe because the candidate lies in \(w-2C\); \(16\) also have the
double-candidate obstruction \(w-2x\in C\). It finds no safe two-point
batch for the next gap. With beam \(32\), the best endpoint improves only
to \(6501\), stalling at \(6502\) with the same obstruction type. At scale
\(N=200\), beam \(8\) similarly extends coverage from \(6000\) to \(12947\),
again far below the witness \(20000\); the next gap has \(2061\) unsafe
one-point blockers and no safe two-point batch.
Allowing two-point batches earlier improves the endpoint only modestly:
beam \(8\) reaches \(6505\), and beam \(32\) reaches \(6578\). Both runs
again stall with all one-point blockers lying in \(w-2C\) and no safe
two-point batch for the final gap. At scale \(N=200\), allowing pair
batches with beam \(8\) reaches \(12980<20000\), again with the same final
obstruction.
The scale-\(100\), beam-\(8\), pair-batch run also prints the exact
reflected blocker certificate from Lemma 8.5a.7z.12e'':
\[
d=w-p=3494\in C,
\]
and all \(1034\) one-point candidates \(x=p-a\) satisfy
\[
d+a\in2C.
\]
By Corollary 8.5a.7z.12e''', this certificate has a smaller core:
\[
d+1000,\quad d+1007,\quad d+2000
\]
all lie in \(2C\). Once \(d\) itself is retained, every retained old
summand \(a\in C\) reflects automatically through the pair \(d+a\).
Thus two-new representations are blocked by \(d\in C\), while one-new
representations are blocked by the reflected two-sum condition. The script
prints
\[
\texttt{no\_finite\_batch\_by\_12e\_prime=True}
\]
for this state.
The seed-geometry parameters in the same script also allow the initial
upper retained band to be varied. At scale \(100\), with pair batches and
beam \(8\), interval upper endpoints \(1200,1400,1600,1800\) all end in
the same kind of reflected finite-batch blocker, with best cover endpoints
\[
6465,\ 6506,\ 6200,\ 6550
\]
respectively. Extending the initial upper band safely by a greedy rule does
not evade the obstruction: upper stop \(2500\) reaches \(6898\), and upper
stops \(3200\) or \(5000\) have initial coverage \(6899\) and immediately
stall at \(6900\), again with
\[
d=w-p=3100\in C,\qquad d+\{1000,1007,2000\}\subset2C.
\]
The adjacent greedy-safe endpoint \(3000\) is a useful warning: it has the
same initial coverage and stalls at the same gap \(6900\), with
\[
d=3100\notin C.
\]
There the full reflected-complement certificate of Lemma 8.5a.7z.12e''
does not apply, but the script still reports no safe one-point or two-point
batch. It prints the stronger one-sided saturation certificate from Lemma
8.5a.7z.12h:
\[
2312\text{ one-point candidates saturated, and }1138/1138
\text{ two-point splits saturated}.
\]
Thus Lemma 8.5a.7z.12e'' captures the cleanest wall, not the whole
pair-saturation obstruction measured by Lemmas 8.5a.7z.12e' and
8.5a.7z.12h.
The shadow-translation summary for this endpoint shows the normal form of
Lemma 8.5a.7z.12h.1:
\[
d=3100\notin C,\qquad d\in2C,\qquad d+\{1000,1007,2000\}\subset2C,
\]
and \(2311\) old rows satisfy
\[
d+a\in2C
\]
for the associated one-new candidates \(p-a\). Of these rows, \(2308\) are
retained and \(3\) are the deleted gates. The obstruction is therefore a
large external translate absorbed into \(2C\), not a retained-defect wall.
The escape-set summary of Corollary 8.5a.7z.12h.2 says the same thing from
the opposite side: there are no old-row escapes, the split escape set has
\[
2312
\]
points but no complementary pair summing to \(6900\), and the half-candidate
\(3450\) is saturated.
Warning 8.5a.7z.12h.3 explains why this is locally easy: only two escape
points lie below \(p/2=3450\), namely
\[
2600,\quad 3200,
\]
and their complements
\[
4300,\quad 3700
\]
are already retained old points. The rest of the escape set lies above
\(p/2\), where it cannot contain a complementary pair internally.
Lemma 8.5a.7z.12h.5 gives the staging interpretation. In the endpoint
\(2500\) greedy-safe run, the final defect
\[
d=3101
\]
was not part of the seed: it was the first retained filler added by the
beam search. When the moving gap reached
\[
p=w-d=6899,
\]
the same filler had become a retained defect and satisfied
\[
d+\{1000,1007,2000\}\subset2C,
\]
so the reflected wall closed. In the default endpoint \(1500\) run, the
same phenomenon occurs later: the final defect \(3494\) was added at step
\(63\).
The reusable sweep
```
python3 881/EXPERIMENTS/spike_safe_extension_search.py --scale 100 --beam 8 --steps 400 --allow-pairs --upper-policy greedy-safe --sweep-upper-stops 2400 2500 2600 2700 2800 2900 3000 3050 3100 3150 3200
```
shows the transition is not isolated: every listed endpoint has
\[
\texttt{safe\_one}=0,\qquad \texttt{safe\_two}=0,
\]
all one-point reflected counts saturated, and the one-sided two-point split
ratio saturated. The retained-defect flag switches from false to true near
the endpoint \(3100\), but the finite-batch obstruction is present on both
sides of that switch.
The optional blocker-avoidance mode
```
python3 881/EXPERIMENTS/spike_safe_extension_search.py --scale 100 --beam 8 --steps 400 --allow-pairs --avoid-reflected-blockers
```
filters out any state whose next gap already has the reflected certificate
of Lemma 8.5a.7z.12e''. It reaches essentially the same place, covering only
through \(6503\). At the stopping step there are \(128\) raw safe one- or
two-point extensions, but all \(128\) are filtered because they create a
reflected next-gap blocker. The current unfiltered next gap still has safe
one-point and two-point repairs, so
\[
\texttt{no\_finite\_batch\_by\_12e\_prime=False}
\]
there. The obstruction is that taking any available next safe move appears
to enter the reflected-blocker regime.

By Lemma 8.5a.7z.12e', the absence of both one-point and two-point safe
gap-fillers means that no finite retained batch can cover that particular
next gap while preserving the witness. Thus the finite stall is not merely a
greedy artefact at the final step; escaping it requires reaching a different
state earlier, changing the active packet, or abandoning this local spike
layout.

This is finite evidence, not a proof. Its value is that it identifies the
local pressure precisely: once safe fillers make \(2C\) dense near the
complements of the next possible gap-fillers, the witness-free condition
blocks every one-point retained extension. Allowing pair batches shows that
small coordinated moves do not obviously evade this pressure. The
finite-batch reduction sharpens the last-step obstruction, but a genuine
staged counterexample could still reach a different state before the stall,
change the active gate packet, or use a different cross-window design.

The blocker-avoidance run narrows that escape: it is not enough merely to
avoid ending at a reflected blocker; at least in this finite profile, the
available next safe moves themselves generate reflected blockers. A
successful stage would need more global foresight, a different filler
geometry, or moving active witnesses rather than a local safe-band
extension.

### Target 8.5a.7z.12i: Convert one-sided shadows into retained structure

Corollary 8.5a.7z.12g bounds the clean retained-defect wall at fixed rank,
but Lemma 8.5a.7z.12h exposes a broader escape. A terminal stage can have a
next gap \(p\) for which many potential fillers
\[
x\notin A
\]
are blocked only because
\[
w-x\in2C. \tag{1}
\]
These \(x\)'s are ordinary gaps of the current stage, not retained rows, so
Corollary 8.4c.1 and Lemma 8.5a.7z.10 do not apply directly.
On the other hand, Corollary 8.5a.7z.12g.1 shows that any moving-packet
attempt to cover a retained-defect gap \(p=w-d\) through a deleted gate
\[
p=f+c
\]
must prebuild a private incidence
\[
d+f\notin2C.
\]

Thus the next local-to-global target is:

* either prove that repeated one-sided shadow sets
  \[
  Y\subset[1,p]\setminus A,\qquad w-Y\subset2C,
  \]
  forced by order-2 coverage stages can be converted, using the
  representations of the \(Y\)-values from the full basis, into large
  retained-row tests, stable compressed spikes, or genuine pair-cylinder
  debt; or
* construct a stage system where the shadow sets stay in ordinary gaps of
  \(A\), move cofinally with the witnesses, and still leave enough safe
  fillers to complete order-2 coverage.

This is the precise remaining local obstruction after the reflected
defect-wall simplification: the problem has shifted from retained
reflected rows to nonretained shadow fillers.

### Corollary 8.5a.7z.13: Stable compressed spikes collapse to certificates

Work in the remaining \(k=2\) counterexample case. Fix a finite row test
\[
T_0\subset A,
\]
a finite gate palette
\[
P\subset A,
\]
and a finite shift palette
\[
H\subset\mathbb Z\setminus\{0\}.
\]
Then the following two alternatives are impossible for arbitrarily large
centers.

1. There are arbitrarily large \(m\), some \(f\in P\), and
   \(U\subset T_0\) such that
   \[
   m-U\subset A,\qquad r_{2,A}(u+f)=1\quad(u\in U),
   \]
   and
   \[
   |U|>\beta_f(T_0),
   \]
   where \(\beta_f(T_0)\) is as in Corollary 8.5a.7k.
2. There are arbitrarily large \(m\), some \(h\in H\), and
   \(U\subset T_0\) such that
   \[
   m-U\subset A,\qquad U+h\subset A,
   \]
   and
   \[
   |U|>\gamma_h(T_0),
   \]
   where \(\gamma_h(T_0)\) is as in Corollary 8.5a.7l.

Proof. The first alternative is exactly the hypothesis of Corollary
8.5a.7k for the finite palette \(P\) and test \(T_0\); it gives an infinite
deletion whose complement is an order-3 basis, contradicting the remaining
counterexample case. The second alternative is exactly Corollary 8.5a.7l
for the finite shift palette \(H\) and test \(T_0\), and gives the same
contradiction. \(\square\)

Combined with Lemma 8.5a.7z.10, this says that a selector-specific
reflected front can survive only if its compressed spike data also escapes:
the row sets cannot recur inside any fixed finite \(T_0\) with gates in a
fixed finite \(P\) or shifts in a fixed finite \(H\) while exceeding the
corresponding independence thresholds. Thus the remaining obstruction is
not just selector-specific; it is selector-specific with cofinally moving
row tests, gate palettes, and shift palettes, unless one can promote the
spike supports to genuine late-bad pair debt.

### Target 8.5a.7z.14: Close the moving compressed-spike front

At this point the remaining \(k=2\) obstruction has the following sharper
form. A counterexample must produce, cofinally in every fresh packet tail,
finite product windows whose selector edges \(F\) have terminal witnesses
\(w\) as in Corollary 8.5a.7y, and whose retained-mirror rows from
Lemma 8.5a.7z.10 yield large compressed spikes. For these spikes, all of
the following escape conditions must hold simultaneously:

1. **No pair promotion:** the one- and two-gate spike supports do not form a
   product-covering family of genuine late-bad singleton or pair edges,
   or Corollary 8.5a.7v and the singleton reductions would close the case.
2. **No stable finite palettes:** for every fixed finite row test
   \(T_0\), gate palette \(P\), and shift palette \(H\), the compressed
   spikes inside \(T_0\) with gates in \(P\) or shifts in \(H\) stay below
   the thresholds \(\beta_f(T_0)\) and \(\gamma_h(T_0)\), or Corollary
   8.5a.7z.13 gives a recurrent certificate.
3. **No disjoint local windows:** the active supports cannot live in
   disjoint finite windows, by Warning 8.5a.7z.1; they must form a genuine
   cross-window front on packet indices.
4. **Coverage without terminal repair:** the extra retained fillers needed
   for order-2 stage coverage must do more than bridge the initial two-sum
   gaps from Example 8.5a.7z.12a and Diagnostic 8.5a.7z.12c. They must
   push the declared endpoint past the protected witnesses without entering
   the terminal gaps, repairing those witnesses, or creating stable
   compressed spikes.
5. **No fixed-witness runway:** by Corollary 8.5a.7z.12h.9, if one witness
   \(w\) and one deleted packet \(F\) remain frozen while many retained
   fillers \(x\) have their future targets \(w-x\) covered by the old full
   set, then the runway crosses the explicit threshold
   \(|X|-|G|>|F|(|F|M+|F+F|)\) and compresses to a unique-gate or
   shifted-overlap spike. If instead many such targets remain uncovered, the
   stage has not supplied the required order-2 coverage. Hence a surviving
   construction must reset witnesses, packets, or row tests cofinally before
   a long fixed runway forms.

Thus the final problem is no longer a local terminal-hole problem. It is a
global recurrence-versus-staging problem for moving compressed spikes: prove
that product-selector pressure forces one of the forbidden stabilizations
above, or construct a staged basis where the row tests, gates, shifts,
mirrors, and coverage fillers all escape cofinally while the active
supports remain a true deletion barrier.

### Target 8.5a.7h: From large private fibers to recurrent colors

After Corollaries 8.5a.7f--8.5a.7f.1 and Examples 8.5a.7g and 8.5a.7m,
the remaining \(k=2\) problem can be stated more sharply. In every tail and
outside every finite core, a counterexample must produce arbitrarily large
sets
\[
U
\]
and centers
\[
m=w-f
\]
with
\[
m-U\subset A,\qquad U+f\cap2(A\setminus F)=\varnothing. \tag{1}
\]
If a fixed finite test set \(T_0\) had the property that every large subset
of \(T_0\) contains a certificate triple, then repeated occurrences of
(1) inside \(T_0\) would give a recurrent certificate and hence a good
deletion by Corollary 2.3c. Therefore a surviving counterexample must make
these large private fibers escape every fixed certificate-rich test set.

Corollary 8.5a.7f.1 further says that these escaping fibers may be taken in
one of two more rigid forms: either \(u+f\) is uniquely represented in the
full basis for all \(u\in U\), or a fixed retained shifted overlap
\(U+f-g\subset A\setminus F\) appears for a second deleted color \(g\).
Lemma 8.5a.7i adds that, if the shifted fiber is also certificate-free, it
must be independent for the shift \(h=f-g\), and Lemma 8.5a.7j gives the
analogous gate-difference independence for unique-gate fibers. Corollaries
8.5a.7k--8.5a.7l then rule out any recurrence over fixed finite palettes of
gates or shifts unless the reflected fibers stay inside the corresponding
certificate-free independence numbers. Corollary 8.5a.7n sharpens this
inside a counterexample: for each fixed finite test and finite gate or shift
palette, the oversized recurrent fibers have bounded reflection centers.
Corollary 8.5a.7o adds the cofinal form: the forced bad edges may be chosen
outside any finite gate palette and avoiding any finite set of shifts among
their deleted colors. Corollary 8.5a.7p also lets the retained fiber rows
avoid any prescribed finite row core, and Corollary 8.5a.7q does the same
for the retained mirror set \(m-U\). The precise missing step is to show
that these bounded-center, cofinally moving-palette, moving-row/mirror, or
independence-number escapes are impossible under the cross-packet selector
obligation of Corollaries 8.5a.7r--8.5a.7t and the counting pressure of
Lemma 8.5a.7u, with Corollary 8.5a.7v ruling out the pair-cylinder
subcover, Corollary 8.5a.7w forcing rank-\(\ge3\) selector debt cofinally,
and Corollary 8.5a.7x forcing that debt to have unbounded second excess, or
Corollary 8.5a.7y putting the surviving edges in the full minimal
terminal-gap normal form. Example 8.5a.7z shows that this final local
product-window form is itself compatible, so the missing step must use
infinite staging, recurrence, or cross-window product pressure; otherwise
one must construct a staged basis in which the fibers \(U\), mirrors
\(m-U\), centers \(m\), shifts \(h\), and active colors \(f,g\) all escape
while maintaining order-2 coverage and arbitrarily late finite product
covers whose pair subfamilies are selector-avoidable and whose high-rank
edges are minimal large-spread terminal cuts whose supports form a genuine
cross-window weak barrier rather than disjoint local gadgets. Diagnostic
8.5a.7z.2 shows that even the first bounded fourth-packet extension of the
small local model is nontrivial, and Lemma 8.5a.7z.3 shows that common
three-packet witness layers have only tiny outside retained fibers. Lemma
8.5a.7z.4 gives the general witness-sharing constraint in terms of
two-transversals of selector families. This is now the active form of the
certificate-free obstruction; it is stronger than mobile injectivity and
weaker than finite recurrent Sidon coloring.

### Target 8.5a.8: Trace-section dichotomy

The remaining recursive target is the following dichotomy for prefix-fronts
with active traces \(\tau(S)\ni\max S\).

Assume bounded-depth finite palettes, finite moving-label palettes, and
pure terminal gating have all been ruled out by Lemmas 8.5a.3--8.5a.6.
If finite protected tests are still colorable by active trace elements at
unbounded depth, then one should prove that either:

1. a proper prefix section \(\mathcal F_s\) inherits the same active-trace
   private-color obstruction, with induced traces
   \[
   \tau_s(G)=\tau(s\cup G)\setminus s;
   \]
2. after thinning, all unboundedness is first-coordinate coded: for each
   fixed first point \(a\), the section \(\mathcal F_{\{a\}}\) has bounded
   active nonterminal depth, and the bound tends to infinity only as
   \(a\to\infty\).

The second alternative is an enumerated-Schreier shell rather than a new
front-rank phenomenon. A final positive proof would combine this dichotomy
with the enumerated-Schreier obstruction results in Section 13. A
counterexample would have to realize the mobile injective coloring
arithmetically while evading that shell analysis.

### Lemma 8.5a.8a: Abstract section-depth dichotomy

Let \(P=\{p_1<p_2<\cdots\}\) be infinite and let \(\mathcal F\) be a
prefix-front on \(P\). Let
\[
\delta:\mathcal F\to\mathbb N
\]
be any obstruction statistic. For an initial segment \(s\) of a member of
\(\mathcal F\), with no proper initial segment already in \(\mathcal F\),
write
\[
\mathcal F_s=\{G\subset P_s:s\cup G\in\mathcal F\},
\qquad P_s=\{p\in P:p>\max s\},
\]
and let
\[
\delta_s(G)=\delta(s\cup G).
\]
If \(\delta\) is unbounded on every tail of \(P\), then one of the following
two alternatives holds:

1. **section descent:** there is a one-point prefix \(a\in P\) such that
   \(\delta_{\{a\}}\) is unbounded on every tail of \(P_{\{a\}}\);
2. **first-coordinate shell:** for every \(a\in P\), the statistic
   \(\delta_{\{a\}}\) is bounded on some tail of \(P_{\{a\}}\), but these
   tail bounds are unbounded as \(a\) ranges through \(P\).

More explicitly, in the second alternative there is a tail
\[
Q=\{q_1<q_2<\cdots\}\subset P
\]
and integers \(D_i\to\infty\) such that, for each \(i\), all sufficiently
late edges of the section \(\mathcal F_{\{q_i\}}\) have
\[
\delta_{\{q_i\}}(G)\le D_i,
\]
while no single \(D\) bounds \(\delta\) on all late front edges over \(Q\).

Proof. If the first alternative holds, there is nothing to prove. Otherwise,
for each \(a\in P\) there are a tail
\[
P(a)\subset P_{\{a\}}
\]
and a finite bound \(D(a)\) such that every \(G\in\mathcal F_{\{a\}}\) with
\[
G\subset P(a)
\]
satisfies
\[
\delta_{\{a\}}(G)\le D(a). \tag{1}
\]
Build \(Q=\{q_1<q_2<\cdots\}\) recursively. Having chosen
\[
q_1<\cdots<q_i,
\]
choose the remaining tail inside
\[
P(q_1)\cap\cdots\cap P(q_i).
\]
This diagonal thinning ensures that, for each fixed \(q_i\), all sufficiently
late section edges over \(Q\) satisfy (1) with bound \(D(q_i)\).

Because \(\delta\) is unbounded on every tail of the original \(P\), it is
still unbounded on the tail \(Q\). Therefore the sequence of section bounds
\[
D(q_i)
\]
cannot be bounded: if \(D(q_i)\le D\) eventually, then every sufficiently
late front edge over \(Q\) would have first element \(q_i\) in the eventual
range and would satisfy \(\delta\le D\), contradicting unboundedness on
tails. Passing to a subsequence gives \(D(q_i)\to\infty\). \(\square\)

This is only bookkeeping, but it fixes the recursive shape of Target
8.5a.8. A counterexample whose active-trace statistic does not descend to a
proper section must be first-coordinate coded: every fixed first point has
only bounded late complexity, and the bound escapes solely by moving the
first point. The remaining arithmetic task is to convert that shell into
one of the Section 13 first-prefix configurations, or to show that the
conversion can fail in a genuine order-\(2\) basis.

### Lemma 8.5a.8b: Bounded first sections thin to generalized prefix links

Let \(P\subset\mathbb N\) be infinite. For finite
\[
F\subset P
\]
and integers \(w\), let \(\mathcal P(F,w)\) be any property. Suppose that
for every \(a\in P\) there is a finite rank bound
\[
q(a)\ge1
\]
such that for every infinite
\[
Y\subset P\cap(a,\infty)
\]
and every \(L\), there are
\[
G\subset Y,\qquad 1\le |G|\le q(a),
\]
and \(w>L\) with
\[
\mathcal P(\{a\}\cup G,w). \tag{1}
\]
Then there are an infinite sequence
\[
Q=\{a_1<a_2<\cdots\}\subset P
\]
and ranks
\[
1\le r_i\le q(a_i)
\]
such that, for every \(i\) and every \(L\), there is \(J_i(L)>i\) with the
following property: every
\[
H\in[\{a_j:j\ge J_i(L)\}]^{r_i}
\]
has a witness \(w>L\) satisfying
\[
\mathcal P(\{a_i\}\cup H,w). \tag{2}
\]

Proof. We use the proof of Lemma 8.5a in each first section, allowing rank
\(1\). For a fixed \(a\), fixed \(L\), and \(1\le s\le q(a)\), color
\[
[Y]^s
\]
according to whether some \(w>L\) satisfies \(\mathcal P(\{a\}\cup H,w)\).
The hypothesis says the union over \(s\le q(a)\) has no infinite independent
set. The same induction on \(q(a)\) as in Lemma 8.5a gives an infinite
\[
Y_L\subset Y
\]
and a rank \(s(L)\le q(a)\) such that every \(s(L)\)-subset of \(Y_L\) has a
witness \(>L\). Apply this successively for \(L=1,2,\ldots\), each time
inside the infinite set obtained at the previous step, to get nested
infinite sets. Diagonalizing through those nested sets and passing to an
infinite subsequence on which \(s(L)\) is constant gives an infinite
\[
Y(a)\subset Y
\]
and a rank \(r(a)\le q(a)\) such that, for every \(L\), all sufficiently late
\[
r(a)\text{-subsets of }Y(a)
\]
have witnesses \(>L\).

Now build \(Q\) recursively. Choose \(a_1\in P\). Apply the preceding
paragraph to the section above \(a_1\), obtaining an infinite tail \(Y(a_1)\)
and rank \(r_1\). Choose
\[
a_2\in Y(a_1),
\]
apply the section argument inside the tail of \(Y(a_1)\) above \(a_2\), and
continue. At stage \(i\), the future sequence is chosen inside the tail
where the section conclusion for \(a_i\) holds. Therefore, for each fixed
\(i\), all sufficiently late \(r_i\)-subsets of the final sequence \(Q\)
have the required witnesses \(>L\), proving (2). \(\square\)

Thus the no-section-descent case is not an arbitrary weak barrier. After
thinning, it has complete prefix links of finite but moving ranks \(r_i\):
the first point \(a_i\) is linked to every sufficiently late \(r_i\)-subset
of the remaining tail. The first Schreier shell is the special case
\(r_i=i\). Section 13 now rules out the fixed-first, fixed-rank shell when
the associated witnesses shrink to inclusion-minimal traces that keep the
fixed first point. What remains to finish the recursive proof is the
promotion step: in each section, nonminimal traces must either descend to a
proper tail section or supply exactly the full active shell forbidden by
Corollaries 13.1l.2b--13.1l.2f.

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

### Corollary 10.2c: Singleton \(k=3\) debt is \(2A\)-recurrent

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(3\), with
threshold \(N_0\). Suppose infinitely many \(b\in A\) are singleton
late-bad at order \(4\): either \(A\setminus\{b\}\) is not an order-\(4\)
basis, or it is an order-\(4\) basis with no threshold below \(b\). Then
for every finite
\[
T\subset A
\]
and every \(L\), there are such a singleton \(b\notin T\), a witness
\[
w_b=b+d_b,
\]
and a center \(d_b>L\) such that
\[
d_b-T\subset 2A. \tag{1}
\]

If the singleton is a genuine order-\(4\) failure, \(w_b\) may be chosen
arbitrarily large outside \(4(A\setminus\{b\})\). If it is a delayed
threshold failure, \(w_b\) may be chosen with
\[
w_b\ge b-1,\qquad w_b\notin4(A\setminus\{b\}).
\]
In either case the corresponding centers \(d_b=w_b-b\) are unbounded along
the chosen singleton failures.

Proof. The delayed-threshold case is exactly Lemma 10.2b with \(k=3\):
after choosing \(b\) outside \(T\), it gives \(d_b-T\subset2A\) and
unbounded \(d_b\).

For a genuine order-\(4\) failure, choose
\[
w_b>\max\{L+b+\max T,\ \max T+N_0\}
\]
with \(w_b\notin4(A\setminus\{b\})\), and put \(d_b=w_b-b\). For each
\(t\in T\), the number \(w_b-t\) is at least \(N_0\), so it has a
three-term representation from \(A\). If any such representation avoided
\(b\), then adding \(t\) would put \(w_b\) in \(4(A\setminus\{b\})\).
Therefore every representation of \(w_b-t\) uses \(b\); removing one copy
of \(b\) gives
\[
d_b-t=w_b-b-t\in2A.
\]
The choice of \(w_b\) gives \(d_b>L\). Since \(w_b\) can be taken
arbitrarily large, these centers are unbounded. \(\square\)

Thus the higher-order analogue of Corollary 8.3b cannot be obtained from
the singleton argument alone. For \(k=2\), (1) is actual
reflection-recurrence in \(A\), and Theorem 8.2 constructs a good deletion.
For \(k=3\), (1) is only reflection-recurrence in the lower sumset \(2A\).
Using such a mirror in the repair identities costs two retained summands,
which exhausts the one extra summand available when passing from order
\(3\) to order \(4\).

### Warning 10.2d: \(2A\)-recurrence need not compress to \(A\)-recurrence

The obstruction in Corollary 10.2c is not just the parity example from
Warning 10.2b'. For every \(q\ge3\), let
\[
A_q=q\mathbb N\cup\{1,2,\ldots,q-1\}.
\]
Then \(A_q\) is an asymptotic basis of order \(2\), hence also of order
\(3\), and
\[
2A_q
\]
is cofinite. Consequently, for every finite \(T\subset A_q\), all
sufficiently large \(d\) have
\[
d-T\subset2A_q. \tag{1}
\]
However \(A_q\) is not finitely reflection-recurrent in \(A_q\). Indeed,
for \(T=\{1,2\}\), if
\[
m-1,\ m-2\in A_q
\]
and \(m\) is large, then both \(m-1\) and \(m-2\) must be divisible by
\(q\), impossible.

Nor is there a fixed finite catalyst \(c\) that compresses (1) to
\[
d-T-c\subset A_q
\]
for all large \(d\) and \(T=\{1,2\}\). For large values membership in
\(A_q\) means congruence \(0\pmod q\), so this would require
\[
d-1-c\equiv d-2-c\equiv0\pmod q,
\]
again impossible.

Thus lower-sumset recurrence is genuinely weaker than the reflection
recurrence used by Theorem 2.3. The modular finite catalysts can repair
each shifted residue separately in \(2A_q\), but they do not provide a
single \(A_q\)-valued reflected pattern.

This warning is not a counterexample to the problem. For instance, when
\[
q=3,\qquad A_3=3\mathbb N\cup\{1,2\},
\]
deleting
\[
B=6\mathbb N
\]
leaves
\[
C=\{1,2\}\cup\{6j+3:j\ge0\},
\]
and \(C\) is an order-\(4\) basis by residues modulo \(6\): four copies of
\(\{1,2,3\}\) represent every residue modulo \(6\), and the \(3\)-residue
class is cofinite in \(C\). The example only shows that a proof must use
more than raw \(2A\)-mirror recurrence.

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

### Proposition 11.1: Finite accelerators over a cofinite lattice component

Let \(d\ge1\), let \(D\subseteq\mathbb N\) be cofinite, let
\[
F\subset\mathbb N
\]
be finite, and put
\[
A=F\cup dD.
\]
Fix \(k\ge1\). Suppose that for every residue
\[
\rho\in\mathbb Z/d\mathbb Z
\]
there are elements
\[
f_{\rho,1},\ldots,f_{\rho,j_\rho}\in F
\]
not necessarily distinct,
and an integer \(L_\rho\ge2\) such that
\[
j_\rho+L_\rho=k+1
\]
and
\[
f_{\rho,1}+\cdots+f_{\rho,j_\rho}\equiv \rho\pmod d. \tag{1}
\]
Then there is an infinite \(B\subset dD\subset A\) such that
\[
A\setminus B
\]
is an asymptotic basis of order \(k+1\).

Proof. We first choose an infinite sparse set \(P\subset D\) whose
complement \(D'=D\setminus P\) is an asymptotic basis of every order
\(L\ge2\). Since \(D\) is cofinite, choose two elements
\[
s,\ s+2\in D
\]
large enough that all sufficiently large integers lie in \(D\). Let
\[
P=\{2^i:i\ge i_0\}\subset D
\]
with \(2^{i_0}>s+2\), and put \(D'=D\setminus P\). For every sufficiently
large \(M\), at least one of
\[
M-s,\qquad M-(s+2)
\]
is not a power of two, since two powers of two differ by \(2\) only in the
exceptional pair \(2,4\). Taking \(M\) large also puts that difference in
\(D\). Hence
\[
M\in2D'
\]
for all sufficiently large \(M\). For \(L>2\), subtract \((L-2)s\) and pad
with \(L-2\) copies of \(s\), so \(D'\) is an asymptotic basis of every
order \(L\ge2\).

Now let
\[
B=dP.
\]
Then \(B\subset dD\subset A\) is infinite, and
\[
A\setminus B=F\cup dD'.
\]
Let \(n\) be sufficiently large and let \(\rho\equiv n\pmod d\). Choose the
data from (1). Then
\[
Q={n-(f_{\rho,1}+\cdots+f_{\rho,j_\rho})\over d}
\]
is a sufficiently large positive integer. Since \(L_\rho\ge2\) and \(D'\)
is an order-\(L_\rho\) asymptotic basis, write
\[
Q=d_1+\cdots+d_{L_\rho},\qquad d_i\in D'.
\]
Therefore
\[
n=f_{\rho,1}+\cdots+f_{\rho,j_\rho}
  +dd_1+\cdots+dd_{L_\rho}
\]
is a \((k+1)\)-term representation from \(A\setminus B\). Thus
\(A\setminus B\) is an order-\((k+1)\) basis. \(\square\)

Example 11 is the case \(d=k\), \(D=\mathbb N\), and \(F=\{1\}\): for
\(\rho=r\in\{0,\ldots,k-1\}\), take \(j_\rho=r\) copies of \(1\) and
\[
L_\rho=k+1-r\ge2.
\]
The proposition also explains why finite residue accelerators are not by
themselves a negative mechanism: once the residue repair can be arranged
with at least two lattice terms, the sparse deletion above absorbs the
accelerator. The next corollary shows that this condition is automatic when
\(F\cup dD\) is already an order-\(k\) basis.

### Corollary 11.1a: Cofinite lattice accelerators are always positive

Let \(d\ge1\), let \(D\subseteq\mathbb N\) be cofinite, let \(F\subset
\mathbb N\) be finite, and put
\[
A=F\cup dD.
\]
If \(A\) is an asymptotic basis of order \(k\), then there is an infinite
\[
B\subset dD
\]
such that \(A\setminus B\) is an asymptotic basis of order \(k+1\).

Proof. We verify the residue hypothesis of Proposition 11.1. Fix a residue
\[
\rho\in\mathbb Z/d\mathbb Z.
\]
Choose \(n\equiv\rho\pmod d\) so large that \(n\in kA\) and \(n\) is larger
than every \(k\)-term sum using only elements of \(F\). In any
representation
\[
n=a_1+\cdots+a_k,\qquad a_i\in A,
\]
at least one summand lies in \(dD\). Let \(j_\rho\) be the number of
summands lying in \(F\), and let
\[
L'_\rho=k-j_\rho\ge1
\]
be the number of lattice summands. The sum of the \(F\)-summands is
congruent to \(\rho\pmod d\), since all lattice summands are \(0\pmod d\).
For Proposition 11.1 use these \(j_\rho\) finite summands and set
\[
L_\rho=L'_\rho+1\ge2.
\]
Then \(j_\rho+L_\rho=k+1\), and the required congruence holds. Proposition
11.1 gives the desired infinite deletion. \(\square\)

Thus the finite-accelerator warning in Attempt 17 can only be relevant for
thin non-accelerator components, not for components that are cofinite in an
arithmetic progression.

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

### Diagnostic 13.1j.1: Arbitrary prefix ranks can bypass finite Schreier stalls

The generalized shell from Lemma 8.5a.8b is weaker than the first-Schreier
schedule tested in Lemma 13.1j. The mode
`schreier_stage_search.py --general-prefix-diagnostic` checks whether a
finite protected window has an ordering
\[
v_1,\ldots,v_n
\]
and ranks \(\rho_i\) such that each \(v_i\) links to every
\(\rho_i\)-subset of its remaining tail.

On the P6 stalled window
\[
A=\{1,2,4,5,8,10,15,18,19,30,38,40,43,44\},
\]
with protected vertices
\[
(10,15,18,19,30,38),
\]
the first-Schreier order still fails, but with no tail slack the generalized
test succeeds:
\[
\text{order}=(10,38,15,18,19,30),\qquad
\rho=(1,4,2,2,1).
\]
The rank \(4\) link at the second prefix uses the entire remaining tail
\[
\{15,18,19,30\}.
\]
When the diagnostic requires even one unused tail vertex after every prefix
link,
\[
\texttt{--min-tail-slack 1},
\]
the same finite window has no generalized shell. Thus arbitrary finite ranks
can hide finite stalls by using near-terminal tail cuts. The infinite
problem must distinguish genuine moving-rank prefix links, with tail slack
cofinally, from such finite end-of-tail artefacts.

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

## Corollary 13.1l.2a: Fixed-prefix high-center finite-rank links are impossible

Work in the \(k=2\) case, and suppose \(A\) is a counterexample to the
desired order-3 deletion conclusion, with order-2 threshold \(N_0\). Fix
\[
d\in A,\qquad r\ge1,
\]
and let \(Y\subset A\setminus\{d\}\) be infinite. It is impossible that, for
every finite nonempty
\[
T\subset A\setminus\{d\}
\]
and every \(M\), there are
\[
H=\{h_1<\cdots<h_r\}\subset Y\setminus T
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad w-z>M\quad(z\in\{d\}\cup H), \tag{1}
\]
and
\[
w\notin3(A\setminus(\{d\}\cup H)). \tag{2}
\]

Proof. Suppose such data exist. Fix a finite nonempty test set \(T\) and a
parameter \(M\), and put
\[
F=\{d\}\cup H.
\]
For each \(t\in T\), the integer \(w-t\) has a two-term representation from
\(A\), and every such representation meets \(F\), otherwise (2) would be
repaired by adding \(t\). Hence the endpoint list
\[
L(t)=\{z\in F:w-t-z\in A\}
\]
is nonempty.

First suppose that there are a finite \(T_0\) and arbitrarily large \(M\)
for which some admissible data satisfying (1)--(2) have endpoint lists such
that every choice function
\[
\chi(t)\in L(t)\qquad(t\in T_0)
\]
has a fiber containing a certificate triple
\[
e,y_1,y_2,\qquad y_1,y_2\ne e,\qquad y_1+y_2-e\in A.
\]
For each such \(M\), choose any endpoint-list choice. One of the finitely
many certificate triples in \(T_0\) recurs for arbitrarily large \(M\), and
if its fiber is labeled by \(z\in F\), then
\[
w-z-\{e,y_1,y_2\}\subset A.
\]
By (1), the centers \(w-z\) tend to infinity. Thus this fixed certificate
triple is reflection-recurrent, and Corollary 2.3c gives a good infinite
deletion, contradicting the counterexample assumption.

Therefore, in a counterexample, for every finite nonempty
\(T\subset A\setminus\{d\}\) and every \(M\), after increasing \(M\) if
necessary, we may choose data
satisfying (1)--(2) whose endpoint lists admit a choice function with every
fiber certificate-free. Label the endpoint
\[
d
\]
by \(0\), and label the ordered elements \(h_i\) by \(i\). The centers
\[
m_i=w-h_i\quad(1\le i\le r),\qquad m_0=w-d
\]
are all \(>M\), and the chosen list coloring satisfies
\[
m_{\chi(t)}-t\in A\qquad(t\in T)
\]
with certificate-free fibers. This is exactly the finite moving-label Sidon
palette forbidden by Lemma 8.5a.6, applied to the cofinite set
\[
A\setminus\{d\}.
\]
This final contradiction proves the corollary. \(\square\)

Thus generalized prefix-link shells from Lemma 8.5a.8b cannot keep a fixed
first point while placing the witness far above every endpoint in the linked
tail set. A surviving moving-rank shell must have bounded-center debt:
inside each fixed first section, some linked endpoint remains close to the
witness cofinally, or the endpoint lists compactify to a forbidden recurrent
Sidon coloring.

## Corollary 13.1l.2b: Generalized prefix links have endpoint-close debt

Work in the \(k=2\) counterexample setting of Corollary 13.1l.2a. Fix
\[
d\in A,\qquad r\ge1,
\]
and an infinite set
\[
Y\subset A\setminus\{d\}.
\]
Then there are a finite nonempty set
\[
T_*\subset A\setminus\{d\}
\]
and a constant
\[
M_*
\]
with the following property. Whenever
\[
H\in[Y\setminus T_*]^r
\]
and
\[
w-\max T_*\ge N_0,\qquad
w\notin3(A\setminus(\{d\}\cup H)), \tag{1}
\]
one has
\[
\min_{z\in\{d\}\cup H}(w-z)\le M_*. \tag{2}
\]
Consequently, suppose a Lemma 8.5a.8b shell supplies, for this fixed
first point \(d\) and rank \(r\), witnesses for every sufficiently late
\[
H\in[Y]^r
\]
with arbitrarily large \(w\). Then, after increasing the requested witness
height past
\[
\max T_*+N_0\quad\text{and}\quad d+M_*,
\]
every sufficiently late linked edge has a witness \(w\) and a moving
endpoint
\[
h\in H
\]
such that
\[
w-h\le M_*. \tag{3}
\]
If the witness is inclusion-minimal in the deleted packet and \(h\) is an
active endpoint, then also
\[
w-h\in2A,
\]
so (3) is a genuine finite-width endpoint window rather than merely a
failure of high-centering.

Proof. If no such nonempty \(T_*,M_*\) existed, then for every finite
nonempty
\[
T\subset A\setminus\{d\}
\]
and every \(M\) there would be
\[
H\subset Y\setminus T,\qquad |H|=r,
\]
and a witness \(w\) satisfying
\[
w-\max T\ge N_0,\qquad
w-z>M\quad(z\in\{d\}\cup H),
\]
as well as
\[
w\notin3(A\setminus(\{d\}\cup H)).
\]
This is exactly the high-center finite-rank configuration forbidden by
Corollary 13.1l.2a. Hence \(T_*,M_*\) exist, and (2) is just the negation
written out.

Now apply the generalized prefix-link shell with the height parameter
\[
L>\max\{\max T_*+N_0,\ d+M_*\}.
\]
For all sufficiently late \(H\in[Y]^r\), the shell gives a witness
\[
w>L
\]
satisfying (1). Since \(w-d>M_*\), the endpoint realizing (2) cannot be
\(d\); it is some \(h\in H\), proving (3). If \(h\) is active in an
inclusion-minimal hole, then restoring \(h\) repairs the hole, so
\[
w=h+a_1+a_2
\]
with \(a_1,a_2\in A\), equivalently \(w-h\in2A\). \(\square\)

Thus the generalized shell left by Lemma 8.5a.8b has only one remaining
fixed-section escape: the witness must track one of the moving tail
endpoints within a bounded window. If these debt endpoints can be placed at
a fixed ordered position with arbitrarily large gaps below them, Lemma
8.2c''' converts the shell back into the fractional recurrent-cluster
branch. The unresolved part is therefore a moving-position, bounded-window
debt shell in which finite tests must keep finding large certificate-free
subsets.

## Corollary 13.1l.2c: Fixed-position debt is fractional recurrence

Let \(A\) be an order-\(2\) basis with threshold \(N_0\). Fix
\[
d\in A,\qquad r\ge1,\qquad 1\le j\le r,\qquad D\ge d,
\]
and let \(Y\subset A\setminus\{d\}\) be infinite. Suppose that for every
finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(L\), there are
\[
H=\{h_1<\cdots<h_r\}\subset Y\setminus T
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad
w-\max\{d,h_1,\ldots,h_{j-1}\}>L,\qquad
w\le h_j+D, \tag{1}
\]
and
\[
w\notin3(A\setminus(\{d\}\cup H)). \tag{2}
\]
Then for every finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(L_0\), there are
\[
U\subset T,\qquad |U|\ge |T|/j,
\]
and a center \(m>L_0\) such that
\[
m-U\subset A. \tag{3}
\]
If, moreover, some finite
\[
T_0\subset A\cap(D,\infty)
\]
has no certificate-free subset of size at least \(|T_0|/j\), then there is
an infinite \(B\subset A\) such that
\[
A\setminus B
\]
is an order-\(3\) basis.

Proof. Apply Lemma 8.2c''' with
\[
f_0=d,\qquad f_i=h_i\quad(1\le i\le r).
\]
The hypotheses (1)--(2) are exactly the intermediate endpoint-excess
hypotheses of that lemma. Its conclusion gives (3), and its final
certificate-density clause gives the good infinite deletion. \(\square\)

Thus the endpoint-close debt from Corollary 13.1l.2b can remain genuinely
new only if the ordered debt position refuses to stabilize in a form with
arbitrarily large lower gaps, or if every finite test set contains large
certificate-free pieces at the corresponding fractional scale. This is the
same certificate-free recurrent-cluster obstruction already isolated after
Lemma 8.6c, now forced inside each fixed first-section prefix shell.

## Corollary 13.1l.2d: Active fixed-section debt stabilizes by Ramsey

Let \(A\) be an order-\(2\) basis with threshold \(N_0\) and minimum
\[
m_0=\min A.
\]
Fix
\[
d\in A,\qquad r\ge1,
\]
and an infinite ordered tail
\[
Y=\{y_1<y_2<\cdots\}\subset A\setminus\{d\}.
\]
Suppose there is a constant \(M\) such that, for every \(L\), all
sufficiently late
\[
H=\{h_1<\cdots<h_r\}\in[Y]^r
\]
have a witness \(w>L\) satisfying
\[
w\notin3(A\setminus(\{d\}\cup H)), \tag{1}
\]
every endpoint of \(\{d\}\cup H\) is active for this witness, and
\[
\min_{1\le s\le r}(w-h_s)\le M. \tag{2}
\]
Then there are an infinite tail
\[
Y'\subset Y
\]
and an index
\[
1\le j\le r
\]
such that the hypotheses of Corollary 13.1l.2c hold on \(Y'\) with
\[
D=\max\{M,d\}.
\]
In particular, the shell forces fractional reflection-recurrence at scale
\[
|U|\ge |T|/j,
\]
and any finite test set with no certificate-free subset of that size gives
an infinite \(B\subset A\) for which \(A\setminus B\) is an order-\(3\)
basis.

Proof. For each integer \(n\), restrict to a tail of \(Y\) on which every
\(r\)-set has a witness \(w>n\) satisfying (1)--(2). For each such
\(H=\{h_1<\cdots<h_r\}\), choose one witness and color \(H\) by the least
index \(s\) for which
\[
w-h_s\le M.
\]
Ramsey's theorem gives an infinite subtail on which this color is constant.
Iterating for \(n=1,2,\ldots\) gives nested infinite tails and colors
\[
j_n\in\{1,\ldots,r\}.
\]
Choose an infinite sequence
\[
n_1<n_2<\cdots
\]
on which \(j_{n_t}=j\) is constant, and diagonalize through the
corresponding nested tails. The resulting infinite set
\[
Y'\subset Y
\]
has the following property: for every \(t\), all sufficiently late
\[
H\in[Y']^r
\]
have a witness \(w>n_t\) satisfying (1)--(2) whose least debt position is
\[
j.
\]

We verify Corollary 13.1l.2c. Fix a finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and a parameter \(L\). Choose \(t\) with
\[
n_t>\max T+N_0.
\]
The stabilized color-\(j\) conclusion holds on a tail of \(Y'\) for this
\(t\). Now choose
\[
H=\{h_1<\cdots<h_r\}
\]
from that tail, disjoint from \(T\), with
\[
h_j-\max\{d,h_1,\ldots,h_{j-1}\}>L. \tag{3}
\]
This is possible because \(Y'\) is infinite; when \(j=1\), the maximum in
(3) is just \(d\). Let \(w\) be the stabilized witness for \(H\). Then
\[
w-\max T\ge N_0,
\]
and the color condition gives
\[
w\le h_j+M\le h_j+D. \tag{4}
\]
Because \(h_j\) is active, restoring it gives a representation of \(w\)
using \(h_j\), so
\[
w-h_j\in2A
\]
and hence \(w\ge h_j+2m_0\). Combining this with (3) yields
\[
w-\max\{d,h_1,\ldots,h_{j-1}\}>L.
\]
Together with (1) and (4), these are exactly the hypotheses of Corollary
13.1l.2c on \(Y'\). The fractional recurrence and deletion conclusions
therefore follow from that corollary. \(\square\)

Consequently, an active fixed-rank prefix shell cannot use merely
``moving'' bounded endpoint debt as a new escape: after thinning, the debt
position stabilizes. What remains in a \(k=2\) counterexample is the
certificate-free fractional branch, or links that are not full-rank
inclusion-minimal and hence should descend to smaller active traces.

## Corollary 13.1l.2e: Full active prefix shells are fractional

Work in the \(k=2\) counterexample setting, and fix
\[
d\in A,\qquad r\ge1,
\]
and an infinite ordered tail
\[
Y=\{y_1<y_2<\cdots\}\subset A\setminus\{d\}.
\]
Suppose that, for every \(L\), all sufficiently late
\[
H\in[Y]^r
\]
have a witness \(w>L\) such that
\[
w\notin3(A\setminus(\{d\}\cup H)),
\]
and the whole packet
\[
\{d\}\cup H
\]
is inclusion-minimal for this witness. Then there are a constant
\[
D
\]
and an index
\[
1\le j\le r
\]
such that, for every finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(L_0\), there are
\[
U\subset T,\qquad |U|\ge |T|/j,
\]
and a center \(m>L_0\) satisfying
\[
m-U\subset A. \tag{1}
\]
Consequently, if some finite \(T_0\subset A\cap(D,\infty)\) has no
certificate-free subset of size at least \(|T_0|/j\), then there is an
infinite \(B\subset A\) such that
\[
A\setminus B
\]
is an order-\(3\) basis.

Proof. Apply Corollary 13.1l.2b to the fixed \(d,r,Y\). It gives a finite
nonempty test set \(T_*\) and a bound \(M_*\). Discard finitely many
points of \(Y\) so that the remaining tail is disjoint from \(T_*\). If a
height parameter \(L\) is raised above
\[
\max T_*+N_0\quad\text{and}\quad d+M_*,
\]
then every sufficiently late linked packet has a witness \(w>L\) and some
tail endpoint \(h\in H\) with
\[
w-h\le M_*.
\]
Because the packet is inclusion-minimal, every endpoint in it is active
for \(w\). Thus the hypotheses of Corollary 13.1l.2d hold with
\[
M=M_*.
\]
That corollary gives an infinite subtail, an index \(j\), and the
hypotheses of Corollary 13.1l.2c with
\[
D=\max\{M_*,d\}.
\]
Applying Corollary 13.1l.2c gives (1) and the stated deletion consequence.
\(\square\)

Thus a fixed first point with a fixed rank is no longer a live
full-active shell unless the fractional branch from Corollary 13.1l.2c
can persist. The next corollary closes that branch when it comes from a
fixed ordered endpoint position: the endpoint lists use only finitely many
earlier labels, so they either produce a recurrent certificate directly or
fall under Corollary 8.5a.4.

## Corollary 13.1l.2f: Fixed-depth endpoint debt is impossible

Work in the \(k=2\) counterexample setting. Fix
\[
d\in A,\qquad r\ge1,\qquad 1\le j\le r,\qquad D\ge d,
\]
and let \(Y\subset A\setminus\{d\}\) be infinite. It is impossible that for
every finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(M\), there are
\[
H=\{h_1<\cdots<h_r\}\subset Y\setminus T
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad
w-\max\{d,h_1,\ldots,h_{j-1}\}>M,\qquad
w\le h_j+D, \tag{1}
\]
and
\[
w\notin3(A\setminus(\{d\}\cup H)). \tag{2}
\]

Proof. Suppose such data exist. Fix a finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and a parameter \(M\), and choose admissible \(H,w\). Put
\[
\Delta=\{d\}.
\]
For each \(t\in T\), the integer \(w-t\) has a two-term representation
from \(A\), and every such representation must meet
\[
\{d\}\cup H,
\]
otherwise adding \(t\) would contradict (2). No representation of \(w-t\)
can use \(h_\ell\) with \(\ell\ge j\), since
\[
w-t-h_\ell\le h_j+D-t-h_\ell\le D-t<0.
\]
Thus the endpoint list
\[
L(t)=\{d:w-t-d\in A\}\cup
\{\ell\in\{1,\ldots,j-1\}:w-t-h_\ell\in A\}
\]
is nonempty.

First suppose there are a finite nonempty \(T_0\subset A\cap(D,\infty)\)
and arbitrarily large \(M\) for which some admissible \(H,w\) have endpoint
lists on \(T_0\) such that every choice function
\[
\chi(t)\in L(t)\qquad(t\in T_0)
\]
has a fiber containing a certificate triple. If the recurring fiber is
labeled by \(d\), then the centers \(w-d\) reflect that triple; if it is
labeled by \(\ell<j\), then the centers \(w-h_\ell\) do. In both cases
(1) makes the centers tend to infinity. Since \(T_0\) contains only
finitely many triples and the label set is finite, pass to an unbounded
subsequence on which both the certificate triple and its label are fixed.
That fixed certificate triple is reflection-recurrent. Corollary 2.3c gives
a good infinite deletion, contradicting the counterexample assumption.

Therefore, in a counterexample, for every finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(M\), after increasing \(M\) if necessary, we may choose
admissible data whose endpoint lists admit a choice function with every
fiber certificate-free. Label \(d\) by itself and label \(h_\ell\) by the
position \(\ell\) for \(1\le\ell<j\). The centers
\[
w-d,\qquad w-h_\ell\quad(1\le\ell<j)
\]
are all \(>M\), and the chosen coloring reflects each row \(t\) by its
label with certificate-free fibers. This is exactly the finite-depth
section list-coloring forbidden by Corollary 8.5a.4, with
\[
\Delta=\{d\}.
\]
The contradiction proves the corollary. \(\square\)

## Corollary 13.1l.2f.1: Variable-rank bounded depth is impossible

Work in the \(k=2\) counterexample setting. Fix
\[
d\in A,\qquad j\ge1,\qquad D\ge d,
\]
and let \(Y\subset A\setminus\{d\}\) be infinite. It is impossible that for
every finite nonempty
\[
T\subset A\cap(D,\infty)
\]
and every \(M\), there are an integer
\[
r\ge j,
\]
a set
\[
H=\{h_1<\cdots<h_r\}\subset Y\setminus T,
\]
and a witness \(w\) such that
\[
w-\max T\ge N_0,\qquad
w-\max\{d,h_1,\ldots,h_{j-1}\}>M,\qquad
w\le h_j+D, \tag{1}
\]
and
\[
w\notin3(A\setminus(\{d\}\cup H)). \tag{2}
\]

Proof. The proof of Corollary 13.1l.2f did not use the total rank \(r\)
except to ensure that the endpoints
\[
h_1,\ldots,h_{j-1},h_j
\]
exist. For \(t\in T\), every representation of \(w-t\) must meet
\[
\{d\}\cup H,
\]
and (1) rules out every endpoint \(h_\ell\) with \(\ell\ge j\) because
\[
w-t-h_\ell\le h_j+D-t-h_\ell\le D-t<0.
\]
Thus all endpoint lists use the same finite palette
\[
\{d,1,\ldots,j-1\},
\]
independent of \(r\). The recurrent-certificate alternative and the
finite-depth list-coloring contradiction from Corollary 8.5a.4 are
therefore identical to the proof of Corollary 13.1l.2f. \(\square\)

Thus, in the unbounded-rank fixed-first branch of Target 13.1l.2k, no
bounded ordered depth can keep bounded endpoint excess. For every fixed
\[
j,D,
\]
a surviving construction must eventually have witnesses with
\[
w-h_j>D
\]
whenever the earlier endpoints are far below the witness. Equivalently,
the active endpoint that remains close to the witness, if one exists, must
move to unbounded ordered depth inside the suffix.

Combining Corollaries 13.1l.2b--13.1l.2f.1, a fixed first point and fixed
rank cannot support a full inclusion-minimal generalized prefix-link shell
in a \(k=2\) counterexample. High-center witnesses are forbidden by
13.1l.2a; bounded active endpoint debt stabilizes by 13.1l.2d; and the
resulting fixed-depth endpoint lists are forbidden by 13.1l.2f--13.1l.2f.1.
Hence the only remaining prefix-front escape is genuine active-trace
descent before a fixed full packet is obtained, or unbounded rank/section
depth escaping every fixed first-section rank.

## Lemma 13.1l.2g: Nonminimal prefix links descend to active traces

Work in the \(k=2\) counterexample setting. Fix
\[
d\in A,\qquad r\ge1,
\]
and an infinite ordered tail
\[
Y=\{y_1<y_2<\cdots\}\subset A\setminus\{d\}.
\]
Suppose that, for every \(L\), all sufficiently late
\[
H=\{h_1<\cdots<h_r\}\in[Y]^r
\]
have a witness \(w>L\) with
\[
w\notin3(A\setminus(\{d\}\cup H)). \tag{1}
\]
For each such pair \((H,w)\), shrink
\[
\{d\}\cup H
\]
inclusion-minimally for the same witness, and record the position pattern
\[
P\subseteq\{0,1,\ldots,r\},
\]
where \(0\in P\) means \(d\) remains in the active trace and
\[
i\in P\quad(1\le i\le r)
\]
means \(h_i\) remains.

After passing to an infinite subtail and to cofinally many height
parameters, this pattern is constant. If the constant pattern contains
\[
0
\]
and at least one moving position, then it yields a full inclusion-minimal
prefix shell with the same fixed first point \(d\) and rank
\[
s=|P|-1
\]
on a further sparse subtail; this rank is at most \(r\), and is strictly
smaller unless the original packet was already full-active. If
\(P=\{0\}\), then \(d\) itself has arbitrarily large one-point holes. If
\(0\notin P\), the obstruction has descended to an active trace wholly
inside the tail, with the old fixed prefix point \(d\) inactive.

Proof. For each integer \(n\), restrict to a tail of \(Y\) on which (1)
holds with witnesses \(w>n\). Choose one witness for each \(H\), shrink it
inclusion-minimally, and color \(H\) by the resulting subset
\[
P(H)\subseteq\{0,\ldots,r\}.
\]
There are only finitely many colors. Ramsey's theorem gives an infinite
subtail with constant color. Iterating over \(n=1,2,\ldots\), then passing
to an infinite subsequence of height parameters on which the color is the
same, and diagonalizing through the nested tails, gives an infinite
\[
Y'\subset Y
\]
and a fixed pattern \(P\) such that, for every selected height parameter,
all sufficiently late \(r\)-sets from \(Y'\) have an inclusion-minimal
subhole in exactly the positions \(P\).
Discard the finitely many selected height parameters below an order-\(3\)
threshold for \(A\). Since \(A\) is an order-\(2\), hence order-\(3\),
basis, the minimal trace is then nonempty, so \(P\ne\varnothing\).

Assume first that
\[
P=\{0,p_1,\ldots,p_s\},\qquad 1\le p_1<\cdots<p_s\le r,
\]
with \(s\ge1\). Choose a further subtail
\[
Z=\{z_1<z_2<\cdots\}\subset Y'
\]
so sparse that between any two consecutive points of \(Z\), and before the
first point under consideration, there are enough unused points of \(Y'\)
to fill all nonactive positions required by \(P\), including the positions
after the last active point. Concretely, when given a sufficiently late
\[
S=\{z_{i_1}<\cdots<z_{i_s}\}\in[Z]^s,
\]
we can choose filler points from \(Y'\setminus Z\) so that, in the ordered
\[
r\text{-set }H=\{h_1<\cdots<h_r\},
\]
one has
\[
h_{p_\ell}=z_{i_\ell}\qquad(1\le\ell\le s).
\]
The fixed-pattern conclusion supplies a witness \(w\) whose
inclusion-minimal active trace is exactly
\[
\{d\}\cup S.
\]
Thus, for every selected height parameter, every sufficiently late
\[
S\in[Z]^s
\]
has a witness for which \(\{d\}\cup S\) is inclusion-minimal. This is the
claimed full active prefix shell of rank \(s\), since the selected height
parameters are unbounded and therefore dominate any prescribed \(L\).

If \(P=\{0\}\), the same argument gives arbitrarily large witnesses
\[
w\notin3(A\setminus\{d\}),
\]
so the obstruction is a one-point failure for \(d\). Finally, if
\[
0\notin P,
\]
then every inclusion-minimal trace obtained after thinning lies entirely in
the moving tail \(Y'\). The fixed prefix point \(d\) is inactive for those
holes, so the obstruction has passed to a proper tail trace rather than to
a fixed first-section shell. \(\square\)

Consequently, in the no-section-descent alternative of Lemma 8.5a.8a, a
fixed first-section generalized prefix link cannot survive by hiding behind
nonminimal packets. Either its active trace keeps the fixed first point and
shrinks to a full active fixed-rank shell, forbidden by Corollaries
13.1l.2b--13.1l.2f, or the active trace drops the fixed first point and
the obstruction has genuinely descended to the tail section.

## Lemma 13.1l.2h: Endless section descent is impossible in a prefix-front

Let \(P\) be infinite and let \(\mathcal F\) be a prefix-front on \(P\).
For every finite initial segment \(s\) of a member of \(\mathcal F\), with
no proper initial segment already in \(\mathcal F\), let \(\mathcal F_s\)
be the section from Lemma 8.5a.2p. Suppose each nonempty section carries an
obstruction statistic
\[
\delta_s:\mathcal F_s\to\mathbb N
\]
such that, whenever \(\delta_s\) is unbounded on every tail of the section
ground set, the first-coordinate shell alternative of Lemma 8.5a.8a is
impossible for that section.

Then \(\delta_\varnothing\) is not unbounded on every tail of \(P\).

Proof. Suppose \(\delta_\varnothing\) is unbounded on every tail. By Lemma
8.5a.8a and the assumed impossibility of the first-coordinate shell
alternative in the root section, there is a first point
\[
a_1\in P
\]
such that the section over
\[
s_1=\{a_1\}
\]
has \(\delta_{s_1}\) unbounded on every tail. Since no initial segment of
\(s_1\) lies in \(\mathcal F\), Lemma 8.5a.2p makes this a prefix-front
section.

Repeat inside that section. Having chosen
\[
s_m=\{a_1<\cdots<a_m\}
\]
with no initial segment in \(\mathcal F\) and with \(\delta_{s_m}\)
unbounded on every tail, the shell alternative is again impossible by
hypothesis, so Lemma 8.5a.8a gives
\[
a_{m+1}>a_m
\]
such that \(\delta_{s_{m+1}}\) is unbounded on every tail for
\[
s_{m+1}=s_m\cup\{a_{m+1}\}.
\]

This constructs an infinite increasing set
\[
X=\{a_1<a_2<\cdots\}\subset P
\]
none of whose finite initial segments lies in \(\mathcal F\). That
contradicts the defining property of a prefix-front, which assigns a
finite initial segment of \(X\) to \(\mathcal F\). Therefore the root
statistic cannot be unbounded on every tail. \(\square\)

Thus, once the arithmetic work rules out the first-coordinate shell
alternative in every active-trace section, the recursive front obstruction
collapses. Lemma 13.1l.2g supplies the needed bridge for fixed-rank prefix
links: nonminimality is either genuine section descent or a smaller full
active shell, and the latter is already forbidden.

## Proposition 13.1l.2i: Conditional recursive closure of the \(k=2\) front

Work in the remaining \(k=2\) counterexample setting after Corollary 8.3b,
and let \(\mathcal H_3\) be the active-trace weak barrier from Corollary
3.1c.3, equipped with the inclusion-minimal witnesses and terminal-gap
normal form from Lemma 8.4b. Suppose the following section-local promotion
principle holds.

For every prefix-front section arising from \(\mathcal H_3\), if its
active-trace obstruction statistic is unbounded on every tail and does not
descend to a proper tail section, then after thinning it satisfies the
generalized prefix-link conclusion of Lemma 8.5a.8b with the property
\[
\mathcal P(\{d\}\cup H,w):
\quad
w\notin3(A\setminus(\{d\}\cup H)),
\]
and with inclusion-minimal shrinks handled exactly as in Lemma 13.1l.2g.

Then no \(k=2\) counterexample exists.

Proof. Assume a counterexample exists. Corollary 3.1c.3 supplies the
active-trace weak barrier, and the remaining obstruction statistic is
unbounded on every tail by the reductions leading to Target 8.5a.8. Apply
Lemma 13.1l.2h to the corresponding prefix-front sections.

It remains only to verify the hypothesis of Lemma 13.1l.2h: the
first-coordinate shell alternative is impossible in every section. By the
section-local promotion principle, any such shell thins to the generalized
prefix-link form of Lemma 8.5a.8b. Lemma 13.1l.2g then says that its
inclusion-minimal traces either descend to a proper tail section, contrary
to being in the no-descent alternative, or keep the fixed first point and
produce a full active fixed-rank prefix shell. The latter is forbidden by
Corollaries 13.1l.2b--13.1l.2f. Hence the shell alternative is impossible
in every section.

Lemma 13.1l.2h now rules out unboundedness of the root obstruction
statistic, contradicting the active-trace barrier supplied by the
counterexample. Therefore, under the stated promotion principle, the
desired infinite deletion exists. \(\square\)

This proposition isolates the exact remaining \(k=2\) proof obligation.
The fixed-rank arithmetic shell has been closed; what is not yet proved in
this workspace is the section-local promotion principle connecting the
private-color normal form of Proposition 8.4f and Corollaries
8.5a.7f--8.5a.7y to the abstract shell/descent dichotomy in every recursive
section.

## Corollary 13.1l.2j: Bounded active fixed sections must descend

Work in the \(k=2\) counterexample setting. Fix \(d\in A\). It is
impossible that there are an infinite tail
\[
P\subset A\cap(d,\infty)
\]
and a bound \(q\) such that, for every infinite
\[
Y\subset P
\]
and every \(L\), there are
\[
H\subset Y,\qquad 1\le |H|\le q,
\]
and a witness \(w>L\) for which
\[
F=\{d\}\cup H
\]
is inclusion-minimal and
\[
w\notin3(A\setminus F). \tag{1}
\]

Proof. Apply the fixed-first Ramsey argument used in Lemma 8.5a.8b to the
property
\[
\mathcal P(\{d\}\cup H,w):
\quad
\{d\}\cup H\text{ is inclusion-minimal for }w
\text{ and }w\notin3(A\setminus(\{d\}\cup H)).
\]
Since the rank is bounded by \(q\), that argument gives an infinite subtail
and a fixed rank
\[
1\le r\le q
\]
such that, for every \(L\), every sufficiently late
\[
H\in[P]^r
\]
has a witness \(w>L\) for which \(\{d\}\cup H\) is inclusion-minimal and
satisfies (1). This is exactly the full active fixed-rank prefix shell
forbidden by Corollaries 13.1l.2b--13.1l.2f. \(\square\)

Therefore, in any recursive section of a \(k=2\) counterexample, a fixed
first point cannot support bounded-rank active traces that keep that first
point. Such a section must either descend to traces omitting the fixed
first point, or have unbounded active suffix rank on every tail. This is
the remaining distinction needed to turn Proposition 13.1l.2i from a
conditional closure into an unconditional \(k=2\) proof.

### Target 13.1l.2k: Fixed first point with unbounded active suffix rank

The remaining section-local gap is now precise. Fix a first point
\[
d\in A
\]
in a recursive section. After removing the genuine descent branch, every
sufficiently late inclusion-minimal active trace in that section contains
\[
d.
\]
Corollary 13.1l.2j rules out the case where the suffix
\[
F\setminus\{d\}
\]
has bounded size on some tail. Thus a surviving section must satisfy:
for every infinite tail \(Y\) and every \(q,L\), there is an
inclusion-minimal hole
\[
F=\{d\}\cup H,\qquad H\subset Y,\qquad |H|>q,
\]
with witness \(w>L\) and
\[
w\notin3(A\setminus F). \tag{1}
\]

This is not yet a fixed-rank prefix shell. Proposition 8.4f gives the
private-color normal form for each such \(F,w\), but its quantifiers are
unanchored:
\[
\forall T,\ \forall X,\ \forall L,\ \exists F\subset X.
\]
It does not by itself give a bounded
\[
q(d)
\]
or a complete link over all \(q(d)\)-subsets of a tail. Nor does Lemma
13.1l.2g help before such a fixed-rank packet has been promoted; that lemma
only shrinks a packet after the complete prefix-link structure is already
available.

Therefore the final \(k=2\) promotion problem is to show that the
unbounded-rank fixed-first traces in (1) force one of the already closed
private-color alternatives: a finite moving-label palette, a recurrent
certificate, a bounded-rank active subtrace still containing \(d\), or a
proper tail descent after all.

### Diagnostic 13.1l.2k.1: Local fixed-first unbounded rank is compatible

Target 13.1l.2k cannot be closed from inclusion-minimality alone. For every
\[
r\ge2
\]
and every
\[
N>4r,
\]
put
\[
d=1,\qquad H=\{N+1,\ldots,N+r\},
\]
\[
w=N+2r+2,
\]
and
\[
C=\{2,3,\ldots,2r\}\cup\{N+2r\}.
\]
Let
\[
F=\{d\}\cup H,\qquad A=C\cup F.
\]
Then
\[
w\notin3C. \tag{1}
\]
Indeed, any three-sum from the low interval \([2,2r]\) is at most
\[
6r<w,
\]
while any three-sum using the high retained point \(N+2r\) is at least
\[
N+2r+4>w.
\]
On the other hand, restoring any one element of \(F\) repairs the hole. For
\[
d=1
\]
one has
\[
w=1+1+(N+2r),
\]
and for
\[
h=N+i,\qquad 1\le i\le r,
\]
one has
\[
w=h+2+(2r-i),
\]
with
\[
2r-i\in[2,2r]
\]
except in the harmless endpoint \(r=1\), which we excluded. Thus
\[
F
\]
is inclusion-minimal for the witness \(w\). The suffix \(H\) can be placed
arbitrarily far out by increasing \(N\), and its rank \(r\) is arbitrary.

The script
`EXPERIMENTS/fixed_first_unbounded_rank_model.py` verifies this family; for
example `--rank 12 --start 80` gives
\[
F=\{1,81,\ldots,92\},\qquad w=106,
\]
with every restored endpoint repairing \(w\).

This is not a counterexample stage. The same diagnostic reports that the
initial two-sum coverage ends at
\[
4r,
\]
leaving a large gap before the suffix \(H\). Moreover, the final part of
that gap is poisoned. If one tries to add a retained filler
\[
x\in[N-2r+2,N],
\]
then
\[
w-x\in[2r+2,4r]\subset2\{2,\ldots,2r\},
\]
so
\[
w\in3(C\cup\{x\}).
\]
Thus the very fillers that would naturally help cover the interval just
before \(H\) by two-sums also repair the protected witness.

This identifies the actual burden in Target 13.1l.2k. A proof must use
global order-\(2\) coverage, recurrence across sections, or selector
pressure to show that the required coverage fillers cannot always be routed
around these poisoned intervals; it cannot use only the local fact that a
fixed first point belongs to arbitrarily large inclusion-minimal holes.

### Diagnostic 13.1l.2k.2: Fixed-first star cuts can have mobile singleton labels

The preceding interval model has many repeated repair labels. The
unbounded-rank branch can also be locally compatible with completely
mobile labels.

Let
\[
r\ge1,\qquad R>2r,
\]
and choose \(N\) much larger than \(rR\). Put
\[
d=1,\qquad w=10N,
\]
\[
h_i=N+iR,\qquad u_i=r+i,\qquad
q_i=9N-r-i(R+1)\qquad(1\le i\le r).
\]
Define
\[
H=\{h_1,\ldots,h_r\},
\]
\[
C=\{u_i,q_i:1\le i\le r\}\cup\{4N,6N-1\},
\]
and
\[
F=\{d\}\cup H,\qquad A=C\cup F.
\]
By range separation,
\[
w\notin3C.
\]
The only sums near \(10N\) are deliberately placed on the wrong side:
\[
4N+(6N-1)+u_i>10N,
\]
whereas
\[
q_i+u_j+u_k<10N
\]
for \(N\) large, and all other combinations of the ranges
\[
U=\{u_i\},\quad Q=\{q_i\},\quad \{4N\},\quad \{6N-1\}
\]
are far below or far above \(10N\).

Restoring the fixed endpoint repairs \(w\):
\[
w=d+4N+(6N-1).
\]
Restoring \(h_i\) repairs \(w\):
\[
w=h_i+u_i+q_i.
\]
Thus \(F\) is inclusion-minimal for \(w\), with arbitrary suffix rank.

Now look at the retained test rows \(u_i\). For a moving label \(h_j\),
\[
w-u_i-h_j=9N-r-i-jR.
\]
This can equal \(q_k=9N-r-k(R+1)\) only if
\[
(j-k)R=k-i.
\]
Since \(|k-i|<R\), this forces \(j=k=i\). It cannot equal any \(u_k\),
\(4N\), or \(6N-1\) by range separation. Hence the row \(u_i\) is served
by exactly one moving label, namely \(h_i\). The endpoint-label fibers are
singletons, so finite-palette and certificate-density arguments see no
repeated label.

The mode
`EXPERIMENTS/fixed_first_unbounded_rank_model.py --model star`
verifies this model; for example `--rank 5 --start 1000 --spacing 20`
prints singleton private labels
\[
6\mapsto1020,\quad 7\mapsto1040,\quad \ldots,\quad 10\mapsto1100.
\]

Thus Target 13.1l.2k cannot be closed by asking only for color reuse inside
one finite hole. A proof must force reuse, bounded subtraces, or tail
descent across many holes and many sections, using the global barrier and
coverage requirements.

### Corollary 13.1l.2k.3: Fixed-first star cuts must be cross-promoted

An attempted \(k=2\) counterexample cannot realize Target 13.1l.2k by
placing independent fixed-first star cuts in disjoint suffix blocks.

More precisely, suppose a tail is partitioned into finite disjoint blocks
\[
P_1,P_2,\ldots
\]
and every active edge in the fixed first section has the form
\[
\{d\}\cup H,
\]
where
\[
H\subset P_s
\]
for some \(s\), and
\[
|H|\ge2.
\]
Then these local section edges are not a weak barrier in the section above
\(d\). Choose one element
\[
p_s\in P_s
\]
from each block. The infinite suffix selector
\[
B=\{p_s:s\ge1\}
\]
contains no \(H\), since it meets each block in only one point. Equivalently,
the full deletion
\[
\{d\}\cup B
\]
contains no active edge of the displayed local form.

Thus the star-cut diagnostics above can matter only if their active
endpoints are promoted across blocks: labels or suffix endpoints from one
stage must become part of later active traces often enough that every
infinite selector contains an entire active trace. This is the precise
cross-block wiring requirement left by Target 13.1l.2k.

### Lemma 13.1l.2k.4: Sparse fixed-prefix tails force large fibers

Let \(A\subseteq\mathbb N\) be an order-\(2\) basis with threshold \(N_0\).
Fix
\[
d\in A,\qquad D\ge0,
\]
and a function
\[
\Phi:\mathbb N_{\ge1}\to\mathbb N.
\]
Then there is an infinite set
\[
B=\{b_1<b_2<\cdots\}\subset A\cap(d,\infty)
\]
with the following property. No finite nonempty
\[
H\subset B,\qquad r=|H|,
\]
with
\[
F=\{d\}\cup H,\qquad C=A\setminus F,
\]
has a witness \(w\) satisfying:

1. \(w\notin3C\);
2. \(w\ge\max H-D\);
3. the active retained rows
   \[
   R(F,w)=\{e\in C:\ e\le w-N_0,\ w-e\notin F+F\}
   \]
   admit a private-color assignment
   \[
   \chi:R(F,w)\to F
   \]
   with
   \[
   w-e-\chi(e)\in C,\qquad e+\chi(e)\notin2C
   \]
   for every \(e\in R(F,w)\), and with every fiber satisfying
   \[
   |\chi^{-1}(f)|\le\Phi(r)\qquad(f\in F).
   \]

Proof. If such \(F,w,\chi\) exist, every element
\[
e\in A\cap[1,w-N_0]
\]
falls into one of three classes:

* \(e\in F\), giving at most \(r+1\) choices;
* \(e\in C\) and \(w-e\in F+F\), giving at most
  \[
  |F+F|\le (r+1)(r+2)/2
  \]
  choices;
* \(e\in R(F,w)\), giving at most
  \[
  (r+1)\Phi(r)
  \]
  choices by the fiber bound.

Hence
\[
A(w-N_0)\le r+1+\frac{(r+1)(r+2)}2+(r+1)\Phi(r). \tag{1}
\]
Choose \(b_r\in A\cap(d,\infty)\) strictly increasing and so far out that
\[
A(b_r-D-N_0)>
r+1+\frac{(r+1)(r+2)}2+(r+1)\Phi(r) \tag{2}
\]
for every \(r\ge1\). This is possible because \(A(x)\to\infty\).

If \(H\subset B\) has size \(r\), then
\[
\max H\ge b_r.
\]
Condition (2) for the witness gives
\[
w-N_0\ge b_r-D-N_0.
\]
Together with (2), this contradicts the capacity bound (1). \(\square\)

In a \(k=2\) counterexample, apply this lemma inside the fixed-first
section. Any sufficiently late inclusion-minimal trace
\[
F=\{d\}\cup H,\qquad H\subset B,
\]
has \(w\ge\max H-1\) by the terminal normal form, and Lemma 8.4c supplies
private colors for all rows outside the \(F+F\) exception set. Therefore,
for every prescribed rank function \(\Phi\), some active color in
\(\{d\}\cup H\) must serve more than \(\Phi(|H|)\) retained rows. The
singleton-label star cuts from Diagnostic 13.1l.2k.2 are consequently not
iterable inside a sparse selector tail; a surviving cross-promoted
construction must create large private fibers attached to a fixed or moving
active endpoint.

### Corollary 13.1l.2k.5: Fixed-first unbounded rank feeds large private fibers

Work in the actual \(k=2\) Target 13.1l.2k branch coming from the
active-trace normal form of Corollary 3.1c.3, so the witnesses satisfy
\[
w\ge\max H-1
\]
for traces
\[
F=\{d\}\cup H.
\]
Then for every finite
\[
E\subset A\cap(d,\infty),
\]
every \(M\), and every \(L_0\), there are:

* a finite nonempty
  \[
  H\subset A\setminus(E\cup\{d\});
  \]
* an inclusion-minimal trace
  \[
  F=\{d\}\cup H
  \]
  and witness \(w>L_0\) with
  \[
  w\notin3(A\setminus F),\qquad w\ge\max H-1;
  \]
* an active color
  \[
  f\in F;
  \]
* a set
  \[
  U\subset A\setminus F,\qquad |U|=M,
  \]

such that, putting
\[
C=A\setminus F,\qquad m=w-f,
\]
one has
\[
m-U\subset C,\qquad u+f\notin2C\quad(u\in U). \tag{1}
\]

Proof. Apply Lemma 13.1l.2k.4 with
\[
D=1,\qquad \Phi(r)=M-1,
\]
choosing the sparse set \(B\) inside
\[
A\setminus(E\cup\{d\})
\]
and above \(L_0+1\). The Target 13.1l.2k branch applied to the infinite
tail \(B\) gives an inclusion-minimal
\[
F=\{d\}\cup H,\qquad H\subset B,
\]
with witness
\[
w>L_0,\qquad w\ge\max H-1,\qquad w\notin3(A\setminus F).
\]
For every retained row
\[
e\in R(F,w)
\]
from Lemma 13.1l.2k.4, Lemma 8.4c supplies at least one private color
\[
f\in F
\]
with
\[
w-e-f\in C,\qquad e+f\notin2C.
\]
Choose one such color for each row. If every color fiber had size at most
\[
M-1,
\]
then \(F,w\) would contradict the defining property of the sparse tail
from Lemma 13.1l.2k.4. Hence some color \(f\in F\) has a fiber of size at
least \(M\). Taking any \(M\)-element subset of that fiber gives \(U\), and
(1) follows. \(\square\)

Thus Target 13.1l.2k has been reduced to the same large-private-fiber
normal form as Corollary 8.5a.7f, now inside a fixed-first section. The
remaining obstruction is not an unbounded-rank star cut with singleton
labels; it is a cross-promoted large-fiber construction whose gates, row
sets, and shifted overlaps must still evade the stable-palette closures
from Corollaries 8.5a.7k--8.5a.7l and 8.5a.7z.13.

### Corollary 13.1l.2l: Finite-prefix fixed-rank shells are impossible

Work in the \(k=2\) counterexample setting. Fix a finite nonempty prefix
\[
\Delta\subset A,
\]
a rank
\[
r\ge1,
\]
and an infinite tail
\[
Y\subset A\setminus\Delta.
\]
It is impossible that, for every \(L\), all sufficiently late
\[
H=\{h_1<\cdots<h_r\}\in[Y]^r
\]
have a witness \(w>L\) such that
\[
F=\Delta\cup H
\]
is inclusion-minimal for \(w\) and
\[
w\notin3(A\setminus F). \tag{1}
\]

Proof. Suppose such a shell exists. First, the high-center alternative is
impossible. Indeed, if for every finite nonempty
\[
T\subset A\setminus\Delta
\]
and every \(M\) there were admissible \(H,w\) with
\[
w-\max T\ge N_0,\qquad w-z>M\quad(z\in\Delta\cup H), \tag{2}
\]
then the endpoint lists
\[
L_w(t)=\{z\in\Delta\cup H:w-t-z\in A\}\qquad(t\in T)
\]
would be nonempty. If, on some fixed finite \(T_0\), every choice function
from these lists had a fiber containing a certificate triple for
arbitrarily large \(M\), one fixed triple and one fixed label position
would recur with centers \(w-z\to\infty\), giving a good deletion by
Corollary 2.3c. Otherwise the lists are choice-colorable into
certificate-free fibers for every finite \(T\) and arbitrarily large
centers. The fixed labels from \(\Delta\) together with the \(r\) ordered
moving labels from \(H\) form a finite moving-label palette, contradicting
Lemma 8.5a.6. Thus there are a finite nonempty \(T_*\) and \(M_*\) such
that every sufficiently high admissible witness has
\[
\min_{z\in\Delta\cup H}(w-z)\le M_*. \tag{3}
\]

Choose the shell height \(L\) above
\[
\max T_*+N_0,\qquad \max\Delta+M_*.
\]
Then (3) is realized by a moving endpoint in \(H\). Color each sufficiently
late \(H\) by the least index \(j\) with
\[
w-h_j\le M_*.
\]
Ramsey thinning and diagonalization over increasing heights give an
infinite subtail and a fixed index \(j\) such that every sufficiently late
\[
H=\{h_1<\cdots<h_r\}
\]
has an admissible witness with
\[
w\le h_j+M_* \tag{4}
\]
and all fixed-prefix and earlier moving centers arbitrarily large. Taking
the points of \(H\) with a large gap below \(h_j\), and using
inclusion-minimality of \(h_j\) to get
\[
w-h_j\in2A,
\]
gives
\[
w-f>M\quad(f\in\Delta\cup\{h_1,\ldots,h_{j-1}\})
\]
for any prescribed \(M\).

Now apply the endpoint-list argument at this fixed depth \(j\). For
\[
T\subset A\cap(M_*,\infty)\setminus\Delta,
\]
every representation of \(w-t\) must meet \(F\), and (4) rules out every
endpoint \(h_\ell\) with \(\ell\ge j\). Hence the lists use only the finite
palette
\[
\Delta\cup\{1,\ldots,j-1\}.
\]
As above, non-colorability gives a recurrent certificate and a good
deletion; persistent certificate-free colorability contradicts Corollary
8.5a.4. This contradiction proves the corollary. \(\square\)

This is the finite-prefix version needed for cross-promoted star cuts. If
successive promotions keep accumulating a finite fixed prefix while the
next suffix rank is bounded, the resulting fixed-rank shell is already
impossible. The only remaining cross-promoted branch must therefore make
the active suffix rank unbounded at every finite prefix depth, or else
drop some fixed prefix point and descend.

### Corollary 13.1l.2m: Surviving promoted fronts have unbounded rank in every section

Let \(\mathcal F\) be a prefix-front of inclusion-minimal active traces
arising in the \(k=2\) counterexample setting. Suppose that in a section
with finite fixed prefix
\[
\Delta
\]
the active traces all keep \(\Delta\), and write the moving suffix of an
edge as
\[
H\subset P_\Delta.
\]
If there are an infinite tail
\[
Y\subset P_\Delta
\]
and a bound \(q\) such that every infinite
\[
Z\subset Y
\]
contains a section edge
\[
\Delta\cup H
\]
with
\[
H\subset Z,\qquad 1\le |H|\le q,
\]
then the \(k=2\) counterexample is impossible.

Proof. Apply the bounded-rank Ramsey thinning used in Lemma 8.5a.8b to the
section property
\[
\mathcal P(\Delta\cup H,w):
\quad
\Delta\cup H\text{ is inclusion-minimal for }w,\quad
w\notin3(A\setminus(\Delta\cup H)).
\]
Since \(|H|\le q\), after thinning there are an infinite subtail and a
fixed rank
\[
1\le r\le q
\]
such that every sufficiently late
\[
H\in[Y]^r
\]
has a witness \(w\) with \(\mathcal P(\Delta\cup H,w)\), with arbitrarily
large \(w\). This is exactly the finite-prefix fixed-rank shell forbidden
by Corollary 13.1l.2l. \(\square\)

Consequently, a cross-promoted \(k=2\) counterexample cannot merely carry a
finite prefix through a bounded-rank suffix front. In every finite-prefix
section that does not drop some fixed prefix point, the suffix ranks must
be unbounded on every tail. This is the abstract front-theoretic core left
after the fixed-rank and star-cut reductions.

### Diagnostic 13.1l.2m.1: The remaining abstract shape is higher-front rank

The script `EXPERIMENTS/front_barrier_diagnostics.py` records the finite
shadow of this last abstract possibility. On the ordered set
\[
\{2,3,\ldots\},
\]
let
\[
\mathcal B_2=\{\{x_1<\cdots<x_m\}:m=x_2\}.
\]
Every infinite tail has an initial segment in \(\mathcal B_2\), but fixing
only the first point does not bound the suffix rank; the second point
controls the edge size. The diagnostic on
\[
(2,3,\ldots,12)
\]
finds no finite barrier failure at the tested length and no first-Schreier
subbarrier on tails of sizes \(3,\ldots,6\).

Thus Corollary 13.1l.2m is sharp as a front-theoretic statement. A final
positive proof cannot rely on abstract prefix-front combinatorics alone:
it must use additive structure from the large private fibers, terminal
gaps, or two-sum coverage to rule out higher-front rank such as
\(\mathcal B_2\), or else build a genuine integer construction realizing
that higher-front wiring.

### Corollary 13.1l.2n: Finite-prefix active suffix fronts cannot persist

Work in the \(k=2\) counterexample setting. Fix a finite nonempty prefix
\[
\Delta\subset A
\]
and an infinite tail \(P\subset A\) above \(\Delta\). Let \(\mathcal E\) be
a prefix-front on \(P\). Suppose that, for every
\[
H\in\mathcal E,
\]
there is a witness \(w_H\) such that
\[
F_H=\Delta\cup H
\]
is inclusion-minimal for \(w_H\) and
\[
w_H\ge\max H-1,\qquad
w_H\notin3(A\setminus F_H). \tag{1}
\]
Then the suffix ranks
\[
|H|\qquad(H\in\mathcal E)
\]
are not unbounded on every tail of \(P\).

Proof. Suppose, to the contrary, that \(|H|\) is unbounded on every tail of
\(P\). Apply Lemma 13.1l.2h to the prefix-front \(\mathcal E\), with
\[
\delta_s(G)=|G|
\]
in each section. It is enough to verify that the first-coordinate shell
alternative of Lemma 8.5a.8a is impossible in every section.

Consider any section with finite suffix prefix \(s\). The fixed prefix in
the original active trace is
\[
\Delta_s=\Delta\cup s.
\]
If the first-coordinate shell alternative held in this section, then for
some first point \(a\) of the section the further section over \(s\cup\{a\}\)
would have bounded suffix rank on a tail. Equivalently, there would be an
infinite tail \(Y\) and a bound \(q\) such that every infinite
\[
Z\subset Y
\]
contains an active trace
\[
\Delta_s\cup\{a\}\cup H
\]
with
\[
H\subset Z,\qquad |H|\le q.
\]
Taking \(Z\) arbitrarily far out makes the corresponding witnesses
arbitrarily large, by (1).
Corollary 13.1l.2m, applied with finite prefix
\[
\Delta_s\cup\{a\},
\]
rules this out: a bounded-rank suffix front over a finite fixed prefix
Ramsey-thins to the finite-prefix fixed-rank shell forbidden by Corollary
13.1l.2l.

Thus the shell alternative is impossible in every section. Lemma
13.1l.2h then says that the root statistic \(|H|\) cannot be unbounded on
every tail, contradicting the assumption. \(\square\)

This closes the purely front-theoretic cross-promotion route once the
promoted suffixes themselves form a prefix-front over a finite fixed prefix.
At this point the apparent remaining promotion problem is the passage from
the weak private-color barrier to a prefix-front of active suffix traces.

### Corollary 13.1l.2o: Finite-prefix weak active barriers cannot persist

Work in the \(k=2\) counterexample setting. Fix a finite nonempty prefix
\[
\Delta\subset A
\]
and an infinite tail \(P\subset A\) above \(\Delta\). There is no weak
barrier \(\mathcal B\) of nonempty finite suffixes \(H\subset P\) such
that every \(H\in\mathcal B\) has a witness \(w_H\) for which
\[
F_H=\Delta\cup H
\]
is inclusion-minimal and
\[
w_H\ge\max H-1,\qquad
w_H\notin3(A\setminus F_H). \tag{1}
\]

Proof. Suppose such \(\mathcal B\) exists. By Lemma 3.1c.4, after thinning
to an infinite \(Q\subset P\) there is a prefix-front
\[
\mathcal E\subset\mathcal B\cap[Q]^{<\omega}
\]
of actual suffix traces, with the same witnesses. If the ranks \(|H|\) for
\(H\in\mathcal E\) are unbounded on every tail of \(Q\), then Corollary
13.1l.2n gives a contradiction.

It remains to consider the case where some infinite tail \(Y\subset Q\)
has bounded ranks. Then there is \(q\) such that every infinite
\[
Z\subset Y
\]
contains a front edge \(H\in\mathcal E\) with
\[
H\subset Z,\qquad |H|\le q.
\]
Since (1) gives \(w_H\ge\max H-1\), taking \(Z\) arbitrarily far out gives
arbitrarily large witnesses. Corollary 13.1l.2m, applied to the section
with fixed prefix \(\Delta\), rules this out. Thus both alternatives are
impossible. \(\square\)

Thus the promotion gap after Corollary 13.1l.2n is not a separate
combinatorial obstruction: weak barriers of actual active traces can be
thinned to actual prefix-fronts, and finite-prefix active suffix barriers
are then excluded by the bounded-rank/unbounded-rank dichotomy.

### Theorem 13.1l.2p: The answer is yes for \(k=2\)

Let \(A\subseteq\mathbb N\) be an asymptotic basis of order \(2\). Then
there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
asymptotic basis of order \(3\).

Proof. Suppose, for contradiction, that no such \(B\) exists. Corollary
8.3b gives a finite exceptional set \(E\subset A\) such that every
singleton deletion above \(E\) is an order-\(3\) basis with a threshold
below the deleted element. Let \(N_3\) be an order-\(3\) threshold for
\(A\), and pass to the infinite tail
\[
P=A\cap(\max(E\cup\{N_3\}),\infty).
\]
For every \(a\in P\), the singleton \(\{a\}\) is not late-bad at order
\(3\).

The proof of Corollary 3.1c.3 applies on this tail, because every infinite
subset of \(P\) still contains a late-bad finite subset. It gives a weak
barrier
\[
\mathcal H_3
\]
of inclusion-minimal active traces \(F\subset P\), each with a witness
\[
w_F\ge\max F-1,\qquad w_F\notin3(A\setminus F). \tag{1}
\]
Moreover each such \(F\) is late-bad. Since no singleton in \(P\) is
late-bad, every \(F\in\mathcal H_3\) has
\[
|F|\ge2. \tag{2}
\]

By Lemma 3.1c.4, after thinning to an infinite \(Q\subset P\) there is a
prefix-front
\[
\mathcal F\subset\mathcal H_3\cap[Q]^{<\omega}
\]
of actual active traces, retaining the witnesses (1). Let
\[
q=\min Q,\qquad Q^+=Q\cap(q,\infty).
\]
Because \(\mathcal F\) is a prefix-front, every infinite \(Z\subset Q^+\)
has an initial segment in the infinite set
\[
\{q\}\cup Z.
\]
By (2), that initial segment cannot be the singleton \(\{q\}\). Hence the
suffix family
\[
\mathcal B_q
=\{H\subset Q^+:\{q\}\cup H\in\mathcal F\}
\]
is a weak barrier of nonempty finite suffixes on \(Q^+\). For each
\(H\in\mathcal B_q\), the trace
\[
\{q\}\cup H
\]
is inclusion-minimal and has a witness satisfying (1), with
\[
w_H\ge\max H-1.
\]
This is exactly the finite-prefix weak active suffix barrier forbidden by
Corollary 13.1l.2o with \(\Delta=\{q\}\). The contradiction proves the
theorem. \(\square\)

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

Warning 8.5a.7c shows that this remains true even after the new mirrors are
included among the current retained test rows: a range-separated packet can
gate \(e\) and \(q_e\) through the same moving color while keeping that
two-point fiber certificate-free. Hence the local mirror rows alone do not
force recurrence or a Schreier prefix link.

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

The companion diagnostic `EXPERIMENTS/robust_residue_patterns.py` shows
that this residue obstruction is not isolated to \(k=3\). With default
bounds it finds, for example,
\[
k=4,\qquad G=\mathbb Z/6\mathbb Z,\qquad S=\{0,1\},\qquad f=3,
\]
where
\[
5S=G,\qquad 4(S\cup\{f\})=G,
\]
but deleting either residue in \(S\) leaves a five-fold hole even with the
booster retained. The same two-residue modulo-\(6\) pattern recurs for
\(k=5,6,7\), with the parity of the missing residues changing with \(k\).
Thus the higher-order obstruction is genuinely lower-sumset/residue-level:
finite residues can protect adjacent-order holes once \(k\ge3\). The
unresolved part is still the integer lift, where deleting one integer does
not delete its whole residue class and central quotient representations
replace the missing representative.

### Lemma 16.0: Finite-core one-marker coverage repairs finite marker deletions

Let \(r\ge1\), let \(C\subset\mathbb N\) be finite, and let
\[
M\subset\mathbb N
\]
be infinite. Suppose there is \(N_0\) such that
\[
[N_0,\infty)\subset M+rC. \tag{1}
\]
Then for every finite \(F\subset M\), all sufficiently large integers lie
in
\[
2(M\setminus F)+rC\subset (r+2)((C\cup M)\setminus F). \tag{2}
\]

Proof. Put
\[
S=rC.
\]
This set is finite. Fix finite \(F\subset M\). Since \(M\) is infinite, for
every sufficiently large \(n\) we may choose
\[
p\in M\setminus F
\]
with
\[
p\le n-N_0
\]
and
\[
p\notin n-F-S.
\]
The last condition means that no representation
\[
n-p=f+s,\qquad f\in F,\ s\in S,
\]
is possible. By (1), since \(n-p\ge N_0\), write
\[
n-p=m'+s,\qquad m'\in M,\ s\in S.
\]
The avoidance condition forces \(m'\notin F\). Hence
\[
n=p+m'+s\in2(M\setminus F)+S=2(M\setminus F)+rC.
\]
This is contained in \((r+2)((C\cup M)\setminus F)\), proving (2).
\(\square\)

Consequently, a higher-order counterexample cannot be obtained by taking a
finite core \(C\), an infinite marker set \(M\), and relying on eventual
order-\(k\) coverage of the form
\[
M+(k-1)C.
\]
Any finite deletion from the marker set is eventually repaired at order
\(k+1\) by two retained markers and \(k-1\) core terms. In particular, for
\(k=3\), the robust residue booster lift cannot use fixed finite-core
coverage \(M+2C\); it must use moving finite cores, collective cross-stage
barriers, or endpoint-local witnesses outside this one-marker coverage
regime.

### Lemma 16.0a: Finite-core one-marker coverage admits a good infinite deletion

Let \(S\subset\mathbb N\) be finite and nonempty, and let
\[
M\subset\mathbb N
\]
be infinite. Suppose there is \(N_0\) such that
\[
[N_0,\infty)\subset M+S. \tag{1}
\]
Then there is an infinite
\[
B\subset M
\]
such that all sufficiently large integers lie in
\[
2(M\setminus B)+S. \tag{2}
\]

In particular, if \(C\) is finite, \(r\ge1\), \(S=rC\), and
\[
[N_0,\infty)\subset M+rC,
\]
then for \(A=C\cup M\) there is an infinite \(B\subset M\) such that
\[
A\setminus B
\]
is an asymptotic basis of order \(r+2\).

Proof. Enlarge \(N_0\) if necessary so that \(N_0\ge1\). We recursively choose
\[
b_1<b_2<\cdots,\qquad b_j\in M,
\]
so that, writing \(F_j=\{b_1,\ldots,b_j\}\),
\[
\bigl|(M\setminus F_j)\cap[1,b_j-N_0]\bigr|>|F_j+S|. \tag{3}
\]
This is possible because \(|F_j+S|\le j|S|\), while \(M\) has arbitrarily
many elements below a sufficiently late choice of \(b_j-N_0\).

Fix \(j\), and choose
\[
G_j\subset(M\setminus F_j)\cap[1,b_j-N_0]
\]
with
\[
|G_j|>|F_j+S|. \tag{4}
\]
We claim that every \(n\ge b_j\) lies in
\[
G_j+(M\setminus F_j)+S. \tag{5}
\]
Indeed, for every \(p\in G_j\) one has \(n-p\ge N_0\). At most
\(|F_j+S|\) choices of \(p\in G_j\) can lie in the finite forbidden set
\[
n-F_j-S.
\]
By (4), choose
\[
p\in G_j\setminus(n-F_j-S).
\]
Then (1) gives
\[
n-p=m+s,\qquad m\in M,\ s\in S.
\]
The avoidance condition forces \(m\notin F_j\). Hence
\[
n=p+m+s\in G_j+(M\setminus F_j)+S,
\]
proving (5).

Let
\[
B=\{b_1,b_2,\ldots\}.
\]
For \(n\ge b_1\), let \(j\) be maximal with \(b_j\le n\). By (5), write
\[
n=p+m+s
\]
with \(p\in G_j\), \(m\in M\setminus F_j\), and \(s\in S\). Since
\[
p\le b_j-N_0\le b_j
\]
and \(p\notin F_j\), the element \(p\) is not \(b_j\) or any later deleted
marker. Also \(m<n\), because \(s\ge1\) and \(p\ge1\); maximality of \(j\)
therefore prevents \(m\) from being a later deleted marker. Thus
\[
p,m\in M\setminus B,
\]
and \(n\in2(M\setminus B)+S\). This proves (2). The final assertion is the
special case \(S=rC\). \(\square\)

Therefore finite-core one-marker coverage is incompatible with a negative
answer in the stronger infinite-deletion sense, not merely after each
fixed finite marker deletion. The deleted markers can be chosen sparsely so
that every finite prefix is repaired below its largest deleted marker.

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
The script's `--high-excess` diagnostic checks the construction-side escape
suggested by Lemma 16.4: require
\[
w-b-2m_0\ge\max C
\]
so old retained padders do not enter the old-gate shadow interval. In the
same third-stage seed, the only singleton candidates with coverage buffer
are again \(41\) and \(43\), and neither has any high-excess pair witness
against the old elements. Thus the current seed has no high-excess
one-point continuation; escaping the shadow-row stall would require a
larger prepared block or a different seed.

### Target 16.2: Moving-core domination is the remaining \(k=3\) lift

After Lemma 16.0, a \(k=3\) negative construction cannot have one finite
core \(C\) and one infinite marker set \(M\) whose tail coverage is
\[
M+2C.
\]
The only residue-booster lift still compatible with the stage criterion is
a moving-core collective barrier. A sufficient form is already Proposition
13.1e with \(k=3\): construct finite stages \(A_s\), increments
\[
P_s=A_s\setminus A_{s-1},
\]
and endpoints \(N_s\to\infty\) such that future elements are larger than
\(N_s\),
\[
[N_{s-1}+1,N_s]\subseteq3A_s
\]
with the positive-summand buffer from Lemma 13.1d, and for every old-new
pair
\[
a\in A_{s-1},\qquad b\in P_s
\]
there is a frozen witness
\[
w_{s,a,b}\le N_s,\qquad
w_{s,a,b}\notin4(A_s\setminus\{a,b\}). \tag{1}
\]

For such a witness, Lemma 10.1 says that every retained padder \(p\) with
\[
w_{s,a,b}-p\ge N_0
\]
has all three-term representations of \(w_{s,a,b}-p\) meeting
\[
\{a,b\}. \tag{2}
\]
Thus the moving-core lift is not merely a coverage problem. It must build
large finite blocks in which each new \(b\) simultaneously makes
\(\{a,b\}\) a vertex cover for the relevant three-representation
hypergraphs for many old \(a\)'s and many retained padders \(p\). The
third-stage robust-booster failure in Diagnostic 16.1 is exactly a finite
shadow of (2): candidate new points extend \(3A_s\)-coverage, but fail the
old-pair domination requirements.

The next dichotomy to prove is therefore:

* either the moving core is sufficiently reusable that finite deletions are
  eventually repaired at order \(4\), generalizing Lemma 16.0 from a fixed
  finite \(2C\) to the moving two-core actually used in the stages;
* or the stages contain an unbounded finite vertex-cover domination system
  of the form (2). Such a system would be the genuine higher-order analogue
  of the \(k=2\) active-trace barriers, and is the remaining candidate
  counterexample mechanism.

### Lemma 16.3: Pair witnesses force old-gate \(2A\)-shadows

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Let
\[
a<b
\]
be elements of \(A\), put
\[
C=A\setminus\{a,b\},
\]
and suppose
\[
w\notin4C. \tag{1}
\]
Then every retained padder
\[
p\in C,\qquad w-p\ge N_0,
\]
has the following properties.

1. Every three-term representation of \(w-p\) from \(A\) uses \(a\) or
   \(b\).
2. If
   \[
   p>w-b-2m_0, \tag{2}
   \]
   then no such representation can use \(b\). Hence every representation
   uses \(a\), and
   \[
   w-a-p\in2(A\setminus\{b\}). \tag{3}
   \]
3. Consequently
   \[
   C\cap(w-a-2m_0,\ w-N_0]=\varnothing. \tag{4}
   \]

Proof. If a three-term representation of \(w-p\) avoided both \(a\) and
\(b\), then adding the retained padder \(p\) would give
\[
w\in4C,
\]
contrary to (1). This proves (1) in the list above.

If a representation of \(w-p\) uses \(b\), its other two summands are at
least \(m_0\), so
\[
w-p\ge b+2m_0,
\]
or equivalently
\[
p\le w-b-2m_0.
\]
Thus under (2) every representation must use \(a\) and avoid \(b\). Removing
one copy of \(a\) gives (3).

If \(p>w-a-2m_0\), then a representation using \(a\) is also impossible,
and a representation using \(b\) is already impossible because \(b>a\). This
contradicts the order-\(3\) basishood of \(A\) whenever \(w-p\ge N_0\).
Therefore no such \(p\in C\) exists, proving (4). \(\square\)

Thus an old-new pair witness with \(b\) much larger than \(a\) has a long
intermediate region
\[
(w-b-2m_0,\ w-a-2m_0]
\]
where every retained padder must be handled by the old endpoint \(a\) alone,
creating forced \(2A\)-shadow rows (3). The robust-booster third-stage
failure is exactly the finite manifestation of this pressure: candidate
new elements can extend three-fold coverage, but cannot simultaneously give
all old endpoints the required \(2A\)-shadow rows before the terminal gap.

### Corollary 16.4: Pair-witness shadow prefilter

Keep the hypotheses of Lemma 16.3, and assume also that
\[
a+2m_0\ge N_0. \tag{0}
\]
If \(w\) is a valid pair witness for \(\{a,b\}\), meaning
\[
w\notin4(A\setminus\{a,b\}),
\]
then, with \(C=A\setminus\{a,b\}\), the following two necessary conditions
hold:

1. **terminal gap**
   \[
   C\cap(w-a-2m_0,\ w-N_0]=\varnothing; \tag{1}
   \]
2. **old-gate shadow rows**
   \[
   w-a-p\in2(A\setminus\{b\}) \tag{2}
   \]
   for every
   \[
   p\in C\cap(w-b-2m_0,\ w-a-2m_0].
   \]

Proof. The terminal gap is Lemma 16.3(3). For the shadow rows, every
\[
p\in C\cap(w-b-2m_0,\ w-a-2m_0]
\]
satisfies \(p>w-b-2m_0\) and \(p\le w-a-2m_0\). If also \(w-p<N_0\), then
\[
w-p\ge a+2m_0\ge N_0,
\]
contradiction. Thus \(w-p\ge N_0\), so Lemma 16.3(2) applies and gives
(2). \(\square\)

The script `EXPERIMENTS/pair_shadow_rows.py` uses (1)--(2) as a finite
prefilter on the robust-booster third stage. For candidates \(b=41,43\),
most old-pair witness candidates are rejected by a missing old-gate shadow
row, and the high candidates for larger old endpoints are rejected by the
terminal gap. The few remaining rejected candidates have ordinary
four-term repairs not detected by this necessary test.
Its row-load mode also applies Corollary 16.6b to the non-singleton
fragment of this failed stage. For both \(b=41\) and \(b=43\), only the old
endpoints
\[
5,\ 20,\ 30
\]
have non-singleton pair witnesses in the checked window; after choosing one
endpoint for each distinct witness value, two witnesses remain. The
reflected rows have total size \(5\) for \(b=41\) and \(6\) for \(b=43\),
with union size equal to total size and maximum overlap \(1\). Thus this
small seed does not exhibit a reusable high-overlap row bank; it fails
before enough old endpoints even enter the non-singleton branch.

### Corollary 16.5: Pair witnesses impose reflected two-sum rows

Keep the hypotheses of Lemma 16.3, and put
\[
d=w-a.
\]
Then every valid pair witness \(w\notin4(A\setminus\{a,b\})\) has
\[
\{p\in C\cap(d-(b-a)-2m_0,\ d-2m_0]:w-p\ge N_0\}
\subseteq d-2(A\setminus\{b\}). \tag{1}
\]
Equivalently,
for every finite
\[
T\subset C
\]
such that
\[
w-b-2m_0<t\le w-a-2m_0,\qquad w-t\ge N_0
\]
for all \(t\in T\), one has
\[
d-T\subseteq2(A\setminus\{b\}). \tag{2}
\]
Moreover
\[
C\cap(d-2m_0,\ w-N_0]=\varnothing. \tag{3}
\]

Consequently, if the same new point \(b\) is to support pair witnesses
\[
w_i\notin4(A\setminus\{a_i,b\})
\]
against many old endpoints \(a_i<b\), then with \(d_i=w_i-a_i\) it must
simultaneously realize the reflected rows
\[
d_i-T_i\subseteq2(A\setminus\{b\}) \tag{4}
\]
for every retained row set
\[
T_i\subset
C_i\cap(d_i-(b-a_i)-2m_0,\ d_i-2m_0],
\qquad C_i=A\setminus\{a_i,b\},
\]
that lies below the threshold cut \(w_i-T_i\ge N_0\).

Proof. Formula (1) is only Lemma 16.3(2) rewritten with
\[
d=w-a.
\]
Indeed, a retained padder in the displayed interval is too large for \(b\)
to occur in any three-term representation of \(w-p\), so every such
representation uses \(a\), and removing \(a\) gives \(d-p\in2(A\setminus
\{b\})\). The finite-set version (2) is the same statement applied to
each \(t\in T\). Formula (3) is Lemma 16.3(3). Applying these conclusions
separately to each old endpoint \(a_i\) proves the simultaneous condition
(4). \(\square\)

This corollary is a capacity test, not an impossibility theorem. It says
that a moving-core construction cannot treat an old-new pair witness as a
purely local four-sum hole: before the terminal gap begins, every retained
padder in the old-gate interval must be mirrored into the lower sumset
\(2(A\setminus\{b\})\). Thus the surviving \(k=3\) construction route
requires many compatible shifted copies of retained row sets in a lower
sumset while still preserving the order-3 coverage interval.

### Lemma 16.6: One nondegenerate witness serves at most four old endpoints

Let \(A\subseteq\mathbb N\), and fix
\[
b\in A,\qquad w\in\mathbb N.
\]
Put
\[
U_b(w)=\{a\in A\setminus\{b\}:w\notin4(A\setminus\{a,b\})\}.
\]
If
\[
w\in4(A\setminus\{b\}), \tag{1}
\]
then
\[
|U_b(w)|\le4. \tag{2}
\]
More precisely, \(U_b(w)\) is contained in the support of every
four-term representation of \(w\) from \(A\setminus\{b\}\).

Proof. Let
\[
w=x_1+x_2+x_3+x_4,\qquad x_i\in A\setminus\{b\},
\]
be any representation supplied by (1), and let
\[
R=\{x_1,x_2,x_3,x_4\}
\]
be its support. If \(a\in U_b(w)\) and \(a\notin R\), then this same
representation lies in \(4(A\setminus\{a,b\})\), contradicting the
definition of \(U_b(w)\). Hence \(U_b(w)\subseteq R\), and \(|R|\le4\).
\(\square\)

Thus a single witness value \(w\) can certify the pairs \(\{a,b\}\) for
many old endpoints only if it is already a singleton-\(b\) four-fold hole,
\[
w\notin4(A\setminus\{b\}).
\]
After excluding that degenerate branch, one fixed \(w\) accounts for at
most four old endpoints. A moving-core pair construction with one new
point \(b\) and many old endpoints must therefore either create many
distinct witness values, each with its own terminal gap and row-reflection
burden from Corollary 16.5, or rely heavily on singleton-\(b\) holes. The
latter branch is exactly where the \(k=3\) singleton analysis only gives
\(2A\)-recurrence rather than \(A\)-recurrence.

### Corollary 16.6a: Non-singleton domination needs linearly many witnesses

Let \(A\subseteq\mathbb N\), let \(b\in A\), and let
\[
O\subset A\setminus\{b\}
\]
be finite. Suppose that for every \(a\in O\) one has chosen a witness
\[
w_a\notin4(A\setminus\{a,b\})
\]
which is not a singleton-\(b\) hole, meaning
\[
w_a\in4(A\setminus\{b\}). \tag{1}
\]
Then the set of distinct witness values satisfies
\[
\bigl|\{w_a:a\in O\}\bigr|\ge\left\lceil{|O|\over4}\right\rceil. \tag{2}
\]

Proof. For each fixed witness value \(w\), Lemma 16.6 says that the set of
old endpoints \(a\in O\) with \(w_a=w\) has size at most \(4\). Summing over
the distinct values gives (2). \(\square\)

Thus a cross-stage pair construction for \(k=3\) has a rigid dichotomy. If
new elements have cofinally many singleton-\(b\) witnesses, the construction
has fallen into the adjacent-order singleton branch of Attempt 15 and
Corollary 10.2c. If singleton-\(b\) witnesses are eventually absent, then
each new point must carry linearly many different pair witnesses against
the old stage, and each distinct witness brings its own Corollary 16.5
terminal-gap and reflected-row burden.

### Corollary 16.6b: Batched non-singleton witnesses carry row load

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Fix
\[
b\in A
\]
and a finite set
\[
O\subset A\setminus\{b\}.
\]
For each \(a\in O\), suppose there is a non-singleton pair witness
\[
w_a\notin4(A\setminus\{a,b\}),\qquad
w_a\in4(A\setminus\{b\}). \tag{1}
\]
Put
\[
d_a=w_a-a
\]
and
\[
T_a=\{p\in A\setminus\{a,b\}:
d_a-(b-a)-2m_0<p\le d_a-2m_0,\ w_a-p\ge N_0\}. \tag{2}
\]
Then there is a set
\[
O'\subset O,\qquad |O'|\ge\left\lceil{|O|\over4}\right\rceil, \tag{3}
\]
such that the witness values \(w_a\), \(a\in O'\), are distinct and
\[
d_a-T_a\subseteq2(A\setminus\{b\}) \qquad(a\in O'). \tag{4}
\]

Moreover, for \(X\subset O'\), define the reflected-row multiplicity
\[
\mu_X=\max_r |\{a\in X:r\in d_a-T_a\}|.
\]
If \(\mu_X\ge1\), then
\[
\left|2(A\setminus\{b\})\cap\bigcup_{a\in X}(d_a-T_a)\right|
\ge {1\over\mu_X}\sum_{a\in X}|T_a|. \tag{5}
\]

Proof. Choose \(O'\) by selecting one endpoint \(a\) for each distinct
witness value occurring among the \(w_a\)'s. Lemma 16.6 says that any fixed
non-singleton witness value can serve at most four endpoints, so (3)
follows. For each \(a\in O'\), Corollary 16.5 gives (4), because \(T_a\)
is exactly the threshold-restricted old-gate row set.

For (5), count incidences
\[
(a,r),\qquad a\in X,\quad r\in d_a-T_a.
\]
There are \(\sum_{a\in X}|T_a|\) such incidences, and each reflected value
\(r\) is counted at most \(\mu_X\) times. Since all reflected values lie in
\(2(A\setminus\{b\})\) by (4), the displayed lower bound follows.
\(\square\)

This is still only a necessary condition. The rows in (4) give
\[
w_a=a+p+x+y,
\]
with \(x,y\in A\setminus\{b\}\), and therefore still use the deleted old
gate \(a\). For the actual pair deletion \(\{a,b\}\), they certify the
domination of the shifted targets \(w_a-p\), not a repair of \(w_a\). The
next possible positive obstruction is therefore a finite-window or
bounded-overlap theorem: if the non-singleton rows cannot be made empty by
high excess, then a stage must place a large amount of row load inside
\(2(A\setminus\{b\})\), and one would need to show that sufficiently large
overlap creates a reusable finite row bank covered by Lemma 16.0a.

### Diagnostic 16.7: High-excess singleton pair stages are locally compatible

The obstruction in Corollary 16.5 is not, by itself, a local impossibility.
The script `EXPERIMENTS/high_excess_pair_seed_search.py` searches for
singleton \(k=3\) stages in which one new point \(b\) has pair witnesses
against every old endpoint \(a\), and every such witness satisfies
\[
w-b-2m_0\ge\max A_{\rm old}. \tag{1}
\]
Condition (1) makes the old-padder part of the Corollary 16.4 shadow
interval empty.

The first small seed found is
\[
A_{\rm old}=\{1,2,3,4\},\qquad N=4,\qquad b=8.
\]
Here \(3A_{\rm old}\) covers from \(3\) through \(12\), while
\[
3(A_{\rm old}\cup\{8\})
\]
covers through \(20\). The stage can declare endpoint \(17\), leaving the
two-point positive-summand buffer, and has high-excess pair witnesses
\[
\begin{array}{c|c}
a & w\\ \hline
1 & 17\\
2 & 17\\
3 & 15\\
4 & 14
\end{array}
\]
with \(w\notin4((A_{\rm old}\cup\{8\})\setminus\{a,8\})\).

The greedy high-excess singleton chain then adds \(19\) at the next stage,
declaring endpoint \(29\) with coverage through \(31\), and stalls at the
third stage:
\[
\{1,2,3,4\}\to\{1,2,3,4,8\}
\to\{1,2,3,4,8,19\}.
\]
The shared witnesses \(17\) for \(b=8\) and \(29\) for \(b=19\) are
singleton-new holes, so this small chain mostly illustrates the
singleton branch of the dichotomy above rather than a nondegenerate
many-witness pair mechanism.

The same script also requires witnesses to be non-singleton-new, i.e.
\[
w\in4(A_s\setminus\{b\}).
\]
The first such high-excess seed is
\[
A_{\rm old}=\{1,2,3,6\},\qquad N=7,\qquad b=9,
\]
with old coverage through \(15\), declared endpoint \(19\), coverage
through \(21\), and witnesses
\[
\begin{array}{c|c}
a & w\\ \hline
1 & 19\\
2 & 17\\
3 & 17\\
6 & 17
\end{array}
\]
all still represented after deleting \(b\) alone. This non-singleton
high-excess singleton chain stalls immediately at the next stage. Hence
the nondegenerate branch is also locally possible, but already in the
smallest examples it demands multiple old-endpoint witnesses inside a very
short buffer.

Finally, the script's `--block` mode asks whether these two stalled seeds
can be continued by a high-excess block of at most three new elements, with
candidate values up to \(100\). It checks \(57155\) three-point blocks after
\[
\{1,2,3,4,8,19\}
\]
and \(85320\) three-point blocks after
\[
\{1,2,3,6,9\},
\]
finding no continuation. This remains finite evidence only, but it shows
that the immediate stall is not just an artefact of insisting on one new
point at the next step.

Thus the high-excess escape is genuinely locally compatible, but the
observed finite chain still has the same rapid endpoint/buffer exhaustion
seen in the robust-booster searches. Any counterexample along this route
would need a non-greedy or larger-block high-excess design, not just a
single prepared marker at each stage.

### Diagnostic 16.8: General \(k=3\) pair stages reach depth four

The robust-booster pair search is not the only finite source of \(k=3\)
pair barriers. The script `EXPERIMENTS/k3_pair_stage_dfs.py` removes the
modulo-\(10\) residue restriction and searches directly for finite stages
satisfying Proposition 13.1e with \(k=3\). With default bounds it finds,
for example, the four-stage chain
\[
\{1,2,3,4\}
\to\{1,2,3,4,7\}
\to\{1,2,3,4,7,17\}
\to\{1,2,3,4,7,17,27\}
\to\{1,2,3,4,7,17,27,37\},
\]
with declared endpoints
\[
15,\ 26,\ 36,\ 46
\]
and three-fold coverage through
\[
18,\ 28,\ 38,\ 48,
\]
respectively. Every old-new pair at each stage has a frozen four-fold
witness below the declared endpoint.

The apparent arithmetic-progression continuation is false. Although
\[
\{1,2,3,4,7\}\pmod {10}
\]
has three-fold residue sumset equal to all of \(\mathbb Z/10\mathbb Z\),
adding \(47\) after the depth-four chain gives coverage through \(58\) but
does not give pair witnesses for all old endpoints below the natural
endpoint \(56\). A bounded search through candidate values \(120\) and
increments of size at most \(3\) finds no next stage from the depth-four
chain.

This diagnostic is important in both directions. It shows that \(k=3\)
cross-stage pair barriers are not merely an artefact of the robust residue
booster seed; unrestricted integer stages have more room. But the first
visible pattern collapses exactly when it becomes eventually periodic, in
line with Proposition 7.1 and the finite-core/periodic repair results.

### Lemma 16.9: Singleton-new holes have exact \(2A\)-row normal form

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Fix \(b\in A\), put
\[
C=A\setminus\{b\},
\]
and suppose
\[
w=b+d\notin4C. \tag{1}
\]
Then every retained padder
\[
p\in C,\qquad w-p\ge N_0,
\]
satisfies
\[
w-p\in3A\setminus3C,\qquad d-p\in2A,\qquad p\le d-2m_0. \tag{2}
\]
Consequently,
\[
C\cap(d-2m_0,\ w-N_0]=\varnothing \tag{3}
\]
and
\[
d-\bigl(C\cap[1,w-N_0]\bigr)\subseteq2A. \tag{4}
\]

Proof. Since \(w-p\ge N_0\), order-\(3\) basishood gives \(w-p\in3A\). If
\[
w-p\in3C,
\]
then \(w=p+(w-p)\in4C\), contradicting (1). Thus every three-term
representation of \(w-p\) from \(A\) uses \(b\), and removing one copy of
\(b\) gives
\[
d-p=w-b-p\in2A.
\]
Any representation using \(b\) has sum at least \(b+2m_0\), so
\[
w-p\ge b+2m_0,
\]
or \(p\le d-2m_0\). This proves (2), and (3)--(4) follow immediately.
\(\square\)

This is the exact singleton analogue of Lemma 16.3. It sharpens Corollary
10.2c from finite reflected tests to the whole retained prefix below
\(w-N_0\), but it also pinpoints the failure of the positive route: the
rows land only in \(2A\), and the resulting identity
\[
w=p+b+x+y
\]
still uses the deleted element \(b\). These rows certify domination of the
shifted targets \(w-p\), not a repair of the singleton hole after deleting
\(b\). In the high-excess regime
\[
d-2m_0\ge\max A_s
\]
inside a finite stage, the terminal gap condition (3) is vacuous on the
current stage, and the remaining requirement is precisely a moving
two-sum row bank
\[
d-(A_s\setminus\{b\})\subseteq2A_s
\]
together with the privacy condition \(b+d\notin4(A_s\setminus\{b\})\).
Lemma 16.0a rules out only fixed finite row banks; it does not rule out a
moving two-core that changes from stage to stage.

Thus the singleton-new branch now has a concrete negative target: construct
finite stages \(A_s\), endpoints \(N_s\to\infty\), and increments \(P_s\)
such that
\[
[N_{s-1}+1,N_s+2m_0]\subseteq3A_s,
\]
future elements exceed \(N_s\), and every new \(b\in P_s\) has a frozen
high-excess singleton witness
\[
w_b=b+d_b\le N_s,\qquad d_b-2m_0\ge\max A_s,\qquad
w_b\notin4(A_s\setminus\{b\}).
\]
If such stages also give every element of the final union a later frozen
singleton witness, the final set would be an order-\(3\) basis that is
ordinary minimal at order \(4\), and hence a counterexample to the broader
deletion theorem. The remaining obstruction is exactly to supply the moving
\(2A_s\)-row banks while avoiding one-other-marker plus three-old repairs.

The diagnostic `EXPERIMENTS/singleton_high_excess_stage_search.py` searches
this target directly. It finds the first tiny stage
\[
\{1,2,3,4\}\to\{1,2,3,4,8\},
\]
where the singleton witness
\[
w_8=18
\]
has \(w_8-8-2=8=\max A_s\), the declared endpoint is \(18\), and
three-fold coverage runs through \(20\). The next step stalls even when
allowing blocks of size at most \(3\) with candidate values up to \(150\):
the script checks \(132\) one-point, \(8646\) two-point, and \(374660\)
three-point candidate increments without finding a continuation. Thus the
strict singleton-high-excess target is locally nonempty but much tighter
than the pair-high-excess diagnostics.

### Lemma 16.10: The interval-marker singleton seed does not one-marker iterate

Let \(L\ge4\), put
\[
I_L=[1,L]\cap\mathbb N,\qquad b=2L,\qquad A_1=I_L\cup\{b\}.
\]
Then \(A_1\) has a singleton-high-excess stage witness
\[
w_b=4L+2.
\]
Indeed,
\[
[3,5L]\subseteq3A_1,\qquad w_b\notin4(A_1\setminus\{b\}),
\]
and
\[
w_b-b-2=2L=\max A_1.
\]

However this interval-marker seed cannot be continued by one later marker
in the same strict singleton-high-excess form. More precisely, let
\[
x>w_b,\qquad A_2=A_1\cup\{x\}.
\]
If a next stage using only the new marker \(x\) had a singleton-high-excess
witness \(w_x=x+d_x\), then
\[
w_x-x-2\ge\max A_2=x,
\]
so
\[
w_x\ge2x+2. \tag{1}
\]
But \(3A_2\) has a gap after the main one-\(x\) range:
\[
3A_2\cap[x+3L+1,\ x+4L-1]=\varnothing. \tag{2}
\]
Since \(L\ge4\), this gap is nonempty; since \(x>w_b=4L+2\), it lies after
the previous endpoint and before the required endpoint
\[
w_x+2\ge2x+4.
\]
Thus the positive-summand buffer
\[
[w_b+1,\ w_x+2]\subseteq3A_2
\]
cannot hold.

Proof. The coverage assertion for \(A_1\) follows from the intervals
\[
3I_L=[3,3L],\qquad
b+2I_L=[2L+2,4L],\qquad
2b+I_L=[4L+1,5L],
\]
which are contiguous for \(L\ge4\). Since \(A_1\setminus\{b\}=I_L\), one
has
\[
4(A_1\setminus\{b\})=[4,4L],
\]
so \(w_b=4L+2\) is private after deleting \(b\). The high-excess equality
is immediate.

For the non-iteration claim, any three-sum from \(A_2\) that uses no copy
of \(x\) is at most
\[
3b=6L<x+3L
\]
because \(x>4L+2\). Any three-sum with exactly one copy of \(x\) is
\[
x+s,\qquad s\in2A_1.
\]
The two-sum set of \(A_1\) is
\[
2A_1=[2,3L]\cup\{4L\};
\]
therefore the one-\(x\) sums cover \([x+2,x+3L]\) and the isolated point
\(x+4L\), but they miss the whole interval in (2). A three-sum with at
least two copies of \(x\) is at least
\[
2x+1.
\]
Hence (2) is absent from \(3A_2\). The high-excess condition gives (1), so
any buffered stage declaring a point at or above \(w_x\) would have to cover
across this gap, impossible.
\(\square\)

This explains why the strict singleton-high-excess diagnostic stalls
immediately after the seed \(\{1,2,3,4,8\}\): the seed is the case \(L=4\)
of the interval-marker family. A successful singleton-high-excess
counterexample cannot simply repeat one marker over a dense initial
interval; it needs multi-marker blocks that bridge the one-marker coverage
gap without repairing the singleton witnesses.

### Lemma 16.11: Next interval-marker stages require a one-new bridge block

Keep \(L\ge4\) and
\[
A_1=[1,L]\cup\{2L\}
\]
as in Lemma 16.10, with previous endpoint
\[
N_1=4L+2.
\]
Let \(P\) be a nonempty finite block with
\[
x=\min P>N_1,
\]
and put
\[
A_2=A_1\cup P.
\]
If the next stage is to give the smallest new element \(x\) a strict
singleton-high-excess witness while satisfying the positive-summand buffer,
then the whole bridge interval
\[
J_x=[x+3L+1,\ 2x]\cap\mathbb N \tag{1}
\]
must satisfy
\[
J_x\subseteq P+\bigl([2,3L]\cup\{4L\}\bigr). \tag{2}
\]

Proof. A strict singleton-high-excess witness for \(x\) has the form
\[
w_x=x+d_x
\]
with
\[
d_x-2\ge\max A_2\ge x,
\]
so
\[
w_x+2\ge2x+4. \tag{3}
\]
The positive-summand buffer therefore requires
\[
[N_1+1,\ 2x]\subseteq3A_2. \tag{4}
\]
Because \(x>4L+2\), the interval \(J_x\) is nonempty and lies above the
old three-sum range:
\[
x+3L+1>7L+3>6L=\max 3A_1.
\]
For any \(n\in J_x\), a three-term representation from \(A_2\) cannot use
two elements of \(P\), since two such elements and one positive summand
already sum to at least
\[
2x+1>n.
\]
Thus every representation of \(n\) uses exactly one element of \(P\) and
two elements of \(A_1\). Finally
\[
2A_1=[2,3L]\cup\{4L\},
\]
so (2) follows. \(\square\)

Thus any attempt to continue the interval-marker singleton seed must build
a genuine bridge block \(P\). The block must cover the long interval
\([x+3L+1,2x]\) by translates of the old two-sum set before the smallest
new marker's high-excess witness can even be placed. This bridge burden is
separate from the privacy burden \(w_x\notin4(A_2\setminus\{x\})\), and in
finite searches the two demands conflict quickly.

### Diagnostic 16.12: A prepared moving row-bank marker exists

The strict singleton-high-excess target is not locally impossible after the
first interval-marker seed if one allows a prepared old block. The script
`EXPERIMENTS/row_collision_scanner.py` records the following stage. Let
\[
A_0=\{1,2,3,4,8,19,20,28\},\qquad N_0=32.
\]
Then
\[
[3,44]\subseteq3A_0.
\]
Adjoin
\[
b=33,\qquad A_1=A_0\cup\{33\}.
\]
Now
\[
[3,76]\subseteq3A_1,
\]
so the interval
\[
[N_0+1,74+2]=[33,76]
\]
has the required positive-summand buffer. The new marker has the
singleton-high-excess witness
\[
w=73=33+40,
\]
with
\[
w\notin4(A_1\setminus\{33\}),\qquad w-33-2=38\ge33=\max A_1.
\]

The moving row bank for \(d=40\) is explicit:
\[
\begin{array}{c|c|c}
p & d-p & \text{row}\\ \hline
1&39&19+20\\
2&38&19+19\\
3&37&4+33\\
4&36&8+28\\
8&32&4+28\\
19&21&1+20\\
20&20&1+19\\
28&12&4+8
\end{array}
\]
The only row that uses \(33\) is the \(p=3\) row. This is harmless: if a
row is \(33\)-dependent it does not contribute to a repair after deleting
\(33\).

The useful collision test is the following. Let \(C=A\setminus\{b\}\) and
\[
w=b+d.
\]
If for some retained padder \(p\in C\) both
\[
d-p\in2C,\qquad b+p\in2C, \tag{1}
\]
then
\[
w=(d-p)+(b+p)\in4C,
\]
so \(w\) is repaired after deleting \(b\). Therefore a viable singleton
row bank must avoid the collision set
\[
\{p:d-p\in2C\}\cap\{p:b+p\in2C\},
\]
except that a row \(d-p\in2A\setminus2C\) may be \(b\)-dependent and hence
does not create a retained repair. In the prepared marker above, the
scanner reports all eight required rows, no retained collisions, and one
\(b\)-dependent row.

This example is only a prepared-marker template, not an iterable
counterexample stage. The elements \(19,20,28\) are doing bridge and row-bank
work but are not themselves protected by singleton witnesses below the
declared endpoint. A staged counterexample would need to add such fillers
only after arranging their own future witnesses, or protect them by a
collective barrier.

The follow-up diagnostic
`EXPERIMENTS/prepared_marker_followup_search.py` tests exactly this caveat.
Starting from
\[
A_1=\{1,2,3,4,8,19,20,28,33\},\qquad N_1=74,
\]
it asks whether any of
\[
19,\ 20,\ 28,\ 33,\ 8
\]
can be given a frozen order-\(4\) singleton witness at the next bounded
stage after adjoining a block of size at most \(3\) with candidate values
up to \(180\). It finds none; the stricter high-excess version also finds
none for blocks of size at most \(2\) up to \(150\). Thus the prepared
marker demonstrates local row-bank feasibility, but its fillers appear
hard to protect even one step later.

The same diagnostic now records the strongest failed declaration windows.
For every tested target \(q\in\{19,20,28,33,8\}\), the best ordinary
failure is obtained after adding \((75,77,85)\): the window \([85,131]\)
has all \(47\) values in \(4A\), but all \(47\) also lie in
\(4(A\setminus\{q\})\). The first repairs are already witnessed by
\[
85=1+84,\quad 86=1+85,\quad 87=1+86,\quad 88=1+87,\quad 89=1+88
\]
with the tails in \(3(A\setminus\{q\})\). In the strict high-excess search,
the best two-point failure \((75,81)\) similarly has every value of
\([81,97]\) represented and poisoned, with no low-excess private leftovers.

### Lemma 16.13: Retained padders poison singleton candidate intervals

Let \(S\subset\mathbb N\) be finite, let \(q\in S\), and put
\[
C=S\setminus\{q\}.
\]
If \(p\in C\) and integers \(R\ge q\) satisfy
\[
[q-p,\ R-p]\subseteq3C, \tag{1}
\]
then
\[
[q,R]\subseteq4C. \tag{2}
\]
In particular, no singleton witness for deleting \(q\) can lie in
\([q,R]\).

Proof. For every \(v\in[q,R]\), condition (1) gives
\[
v-p\in3C.
\]
Since \(p\in C\), we get
\[
v=p+(v-p)\in4C,
\]
proving (2). \(\square\)

This is the singleton \(k=3\) analogue of Lemma 13.1h. A filler inserted to
bridge a moving row bank is not inert: once it is promoted and one tries to
give it its own singleton witness, old retained padders combine with the
current three-sum coverage to poison whole intervals of candidates.
Therefore a staged singleton-high-excess construction must not only build
row banks for new markers; it must also leave shifted three-sum gaps for
every filler when that filler later becomes protected.

### Lemma 16.14: Singleton privacy is exactly a shifted three-sum gap

Let \(S\subset\mathbb N\) be finite, let \(q\in S\), put
\[
C=S\setminus\{q\},
\]
and let \(w\in\mathbb N\). Then
\[
w\notin4C
\]
if and only if
\[
w-p\notin3C\qquad(p\in C). \tag{1}
\]
Consequently, if \(w\in4S\setminus4C\), then every retained padder
\(p\in C\) makes \(w-p\) a three-sum hole after deleting \(q\).

Proof. If \(w-p\in3C\) for some \(p\in C\), then
\[
w=p+(w-p)\in4C.
\]
Conversely, if \(w\in4C\), choose any one summand \(p\in C\) from a
four-term representation of \(w\) in \(C\). The other three summands show
\[
w-p\in3C.
\]
This proves the equivalence. \(\square\)

Thus Lemma 16.13 is not, by itself, an iteration obstruction. It is the
forward direction of the exact characterization above, applied on a whole
interval for one fixed padder. The current singleton-high-excess stage
hypotheses give \(3S\)-coverage and the Lemma 16.9 rows
\[
d-p\in2S,
\]
but they do not give \(3C\)-coverage after deleting the target \(q\). The
interval-marker seed in Lemma 16.10 is the basic witness to this gap:
with
\[
S=[1,L]\cup\{2L\},\qquad q=2L,\qquad C=[1,L],
\]
the value \(w=4L+2\) is a high-excess singleton witness, yet
\[
w\notin4C
\]
because all shifted values \(w-p\), \(p\in C\), escape \(3C=[3,3L]\).
The obstruction to the next one-marker stage is therefore the coverage gap
from Lemma 16.10, not poisoning alone.

### Lemma 16.15: Collision avoidance forces one-term reflected rows

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\).
Fix \(q\in A\), put
\[
C=A\setminus\{q\},
\]
and suppose
\[
w=q+d\notin4C. \tag{1}
\]
If \(p\in C\) satisfies
\[
w-p\ge N_0,\qquad q+p\in2C, \tag{2}
\]
then
\[
d-q-p\in A. \tag{3}
\]
Equivalently, every two-term representation of the forced row \(d-p\) from
\(A\) uses \(q\).

Proof. By Lemma 16.9, the first condition in (2) gives
\[
d-p\in2A. \tag{4}
\]
If \(d-p\in2C\), then the second condition in (2) gives
\[
w=q+d=(q+p)+(d-p)\in4C,
\]
contradicting (1). Hence
\[
d-p\in2A\setminus2C. \tag{5}
\]
Choose a two-term representation \(d-p=x+y\) from \(A\). Since it is not a
representation from \(C\), at least one of \(x,y\) is \(q\). Removing that
copy of \(q\) gives
\[
d-p-q\in A,
\]
which is (3). \(\square\)

Thus a singleton row bank has a rigid dichotomy on every retained padder
\(p\) below the threshold cut. If \(q+p\notin2C\), then \(q+p\) is a
low-count translate row pinned by \(q\). If \(q+p\in2C\), then the row
\(d-p\) cannot be retained, so the bank must reflect \(p\) all the way back
to the one-term value \(d-q-p\in A\). A moving singleton counterexample
must keep both alternatives from stabilizing into the finite
reflection-recurrence criteria of Theorem 2.3.

### Lemma 16.16: High blocks cannot one-new promote old fillers

Let \(S\subset\mathbb N\) be finite, let \(q\in S\), and let
\[
P\subset\mathbb N
\]
be finite and nonempty with
\[
x=\min P>4\max S.
\]
Put
\[
A'=S\cup P,\qquad C=A'\setminus\{q\}.
\]
Suppose
\[
4\max S<w<2x+\min S \tag{1}
\]
and
\[
w\in4A'\setminus4C. \tag{2}
\]
Then there is \(p\in P\) such that
\[
w-p\in3S\setminus3(S\setminus\{q\}). \tag{3}
\]
In particular, the old stage \(S\) already had a three-term private hole
for \(q\), namely \(w-p\).

Proof. Since \(w\in4A'\) and \(w>4\max S\), no four-term representation of
\(w\) from \(A'\) can use only elements of \(S\). Since \(w<2x+\min S\),
no such representation can use two elements of \(P\). Hence every
four-term representation of \(w\) from \(A'\) uses exactly one element
\(p\in P\), and the other three summands lie in \(S\). Thus
\[
w-p\in3S.
\]
If \(w-p\in3(S\setminus\{q\})\), then this same retained three-term
representation, together with the retained element \(p\), gives
\[
w\in4C,
\]
contradicting (2). Therefore (3) holds. \(\square\)

This rules out a basic delayed-filler repair strategy. A later high block
cannot create an adjacent one-new singleton witness for an old filler \(q\)
unless \(q\) already had a lower-order private three-sum hole in the old
stage. To protect genuinely unprotected fillers, a staged construction must
either use witnesses in the two-new range, where the positive buffer and
Lemma 16.14 poisoning become active, or use collective barriers rather than
singleton promotion.

### Lemma 16.17: Singleton row banks split into reflection and unique-gate rows

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\).
Fix \(q\in A\), put
\[
C=A\setminus\{q\},
\]
and suppose
\[
w=q+d\notin4C. \tag{1}
\]
Let \(T\subset C\) be finite and satisfy
\[
w-p\ge N_0\qquad(p\in T). \tag{2}
\]
Define
\[
T_{\rm ref}=\{p\in T:q+p\in2C\},\qquad
T_{\rm uniq}=T\setminus T_{\rm ref}.
\]
Then
\[
d-q-T_{\rm ref}\subseteq A, \tag{3}
\]
and, for every \(p\in T_{\rm uniq}\), the only unordered two-term
representation of \(q+p\) from \(A\) is
\[
q+p=q+p. \tag{4}
\]
In particular, at least one of the two alternatives has size
\[
|T_{\rm ref}|\ge |T|/2,\qquad |T_{\rm uniq}|\ge |T|/2. \tag{5}
\]

Proof. For \(p\in T_{\rm ref}\), Lemma 16.15 applies directly and gives
\[
d-q-p\in A.
\]
This proves (3).

Now let \(p\in T_{\rm uniq}\). Since \(p\in C\), the displayed sum
\[
q+p
\]
is a two-term representation from \(A\). If there were any two-term
representation of \(q+p\) from \(C\), then \(q+p\in2C\), contradicting
\(p\notin T_{\rm ref}\). Hence every two-term representation from \(A\)
uses \(q\). The complementary summand is then forced to be \(p\), so the
unordered representation is unique. This proves (4). The size alternative
(5) is the pigeonhole principle. \(\square\)

Thus singleton \(k=3\) row banks do not remain amorphous. On every finite
test set below the threshold cut, either a positive proportion of rows give
actual one-term reflection in \(A\), or a positive proportion give unique
two-sum translates pinned by the deleted gate \(q\). A positive proof would
need to stabilize one of these two moving structures into a fixed
certificate or absorption pattern; a negative construction must keep both
the reflected rows and the unique-gate rows moving beyond every finite
test.

### Lemma 16.18: The row-bank split is collision-complete

Keep the hypotheses of Lemma 16.17. Define
\[
T_A=\{p\in T:d-p\notin2C\},\qquad
T_U=\{p\in T:q+p\notin2C\}.
\]
Then
\[
T=T_A\cup T_U, \tag{1}
\]
\[
d-q-T_A\subseteq A, \tag{2}
\]
and, for every \(p\in T_U\), the translate \(q+p\) has the unique
unordered two-term representation
\[
q+p=q+p \tag{3}
\]
from \(A\). Consequently at least one of
\[
|T_A|\ge |T|/2,\qquad |T_U|\ge |T|/2 \tag{4}
\]
holds.

Proof. Let \(p\in T\). Lemma 16.9 gives \(d-p\in2A\). If
\[
d-p\notin2C,
\]
then every two-term representation of \(d-p\) from \(A\) uses \(q\), and
therefore \(d-q-p\in A\). This proves (2).

If \(q+p\notin2C\), then the same argument as in Lemma 16.17 proves that
the gate representation \(q+p\) is the unique two-term representation from
\(A\), giving (3).

It remains to prove (1). If some \(p\in T\) lay outside both \(T_A\) and
\(T_U\), then
\[
d-p\in2C,\qquad q+p\in2C.
\]
Adding these two retained two-sums gives
\[
w=q+d=(q+p)+(d-p)\in4C,
\]
contradicting the privacy assumption. Thus every \(p\in T\) lies in
\(T_A\cup T_U\). The half-density alternative (4) follows from
\[
|T|\le |T_A|+|T_U|.
\]
\(\square\)

This is the exact finite-row form behind the collision scanner. A private
singleton row bank can fail to be reflected only by making the corresponding
gate translate uniquely represented; it can fail to be unique-gate only by
making the reflected row \(q\)-dependent. The two failures cannot occur on
the same retained padder.

### Lemma 16.19: Bounded reflected centers force unique-gate rows

Keep the hypotheses of Lemma 16.18, and put
\[
m=d-q,\qquad m_0=\min A.
\]
Then
\[
T\cap(m-m_0,\infty)\subseteq T_U. \tag{1}
\]
Equivalently, every tested row \(p\in T\) with
\[
p>m-m_0
\]
has \(q+p\) uniquely represented in \(2A\) by the gate pair \(q+p\).

Proof. If \(p\in T_A\), Lemma 16.18 gives
\[
m-p=d-q-p\in A.
\]
Since every element of \(A\) is at least \(m_0\), this implies
\[
p\le m-m_0.
\]
Therefore no \(p>m-m_0\) lies in \(T_A\). Lemma 16.18 gives
\[
T=T_A\cup T_U,
\]
so every such \(p\) belongs to \(T_U\), and the unique-gate conclusion is
Lemma 16.18(3). \(\square\)

Thus the reflected half of a singleton row bank is useful only when the
secondary center \(m=d-q\) moves beyond the finite test rows. If \(m\) is
bounded while the tested padders move into the tail, the entire tested
bank becomes a unique-gate packet. A positive proof can therefore split the
singleton branch into two cleaner subproblems: unbounded actual reflections
against finite tests, or arbitrarily late moving unique-gate packets.

### Corollary 16.20: Large reflected singleton rows collapse to certificates

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis. Suppose there is a
finite set
\[
T_0\subset A
\]
such that every subset
\[
U\subset T_0,\qquad |U|\ge |T_0|/2,
\]
contains elements
\[
e,y_1,y_2,y_3\in U,\qquad y_i\ne e,
\]
with
\[
y_1+y_2-e\in A,\qquad y_1+y_2+y_3-2e\in A. \tag{1}
\]
Assume further that for every \(L\) there are \(q\in A\), a private
singleton witness
\[
w=q+d\notin4(A\setminus\{q\}),
\]
and a set
\[
U_L\subset T_0,\qquad |U_L|\ge |T_0|/2,
\]
such that
\[
d-q>L,\qquad d-q-U_L\subset A. \tag{2}
\]
Then there is an infinite \(B\subset A\) such that \(A\setminus B\) is an
order-\(4\) asymptotic basis.

Proof. Put
\[
m_L=d-q.
\]
By (1), each \(U_L\) contains a certificate tuple
\[
e,y_1,y_2,y_3
\]
satisfying the two displayed identities. By (2), the center \(m_L\)
reflects this tuple into \(A\). Since \(T_0\) is finite and \(m_L\) can be
made arbitrarily large, one fixed certificate tuple is reflected by
arbitrarily large centers. Lemma 2.3b, with \(k=3\), applies to this fixed
tuple and gives an infinite deletion whose complement is an order-\(4\)
basis. \(\square\)

Consequently, if the singleton-row-bank branch is to support a \(k=3\)
counterexample, then for every finite test \(T_0\) with small
certificate-free independence, the reflected half of Lemma 16.18 cannot
occur with unbounded centers on at least half of \(T_0\). Combined with
Lemma 16.19, the only remaining singleton escape is a moving unique-gate
packet, or reflected packets contained inside large certificate-free
subsets of every finite test.

### Corollary 16.21: Singleton counterexamples force unique-gate half-packets

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let \(T_0\subset A\) be finite and
satisfy the balanced half-certificate hypothesis of Corollary 16.20.
Then there is \(L_0\) such that the following cannot occur for any
\(L\ge L_0\):

* \(q\in A\), \(w=q+d\notin4(A\setminus\{q\})\);
* \(w-p\ge N_0\) for every \(p\in T_0\), where \(N_0\) is an order-\(3\)
  threshold for \(A\);
* with \(C=A\setminus\{q\}\) and
  \[
  T_A=\{p\in T_0:d-p\notin2C\},
  \]
  one has
  \[
  d-q>L,\qquad |T_A|\ge |T_0|/2. \tag{1}
  \]

Consequently, every sufficiently large-secondary-center singleton row bank
over \(T_0\) has a unique-gate half-packet:
\[
\bigl|\{p\in T_0:q+p\notin2(A\setminus\{q\})\}\bigr|\ge |T_0|/2. \tag{2}
\]

Proof. If the forbidden data existed for arbitrarily large \(L\), then
Lemma 16.18 would give
\[
d-q-T_A\subset A
\]
with \(|T_A|\ge |T_0|/2\) and \(d-q\to\infty\). Corollary 16.20 would
therefore produce an infinite deletion whose complement is an order-\(4\)
basis, contrary to the hypothesis on \(A\). This proves the first
assertion. For \(L\ge L_0\), Lemma 16.18 gives the cover
\[
T_0=T_A\cup T_U,\qquad T_U=\{p\in T_0:q+p\notin2C\}.
\]
Since \(|T_A|<|T_0|/2\), the half-packet bound (2) follows. \(\square\)

This is a usable singleton-branch normal form. Once a finite balanced
certificate test has been found, any surviving singleton private witnesses
with large secondary center must present many unique-gate translates
\(q+p\). If the secondary center is not large, Lemma 16.19 already gives
unique-gate rows on late tests. Thus the unresolved singleton escape is
not generic row-bank recurrence; it is moving unique-gate arithmetic.

### Corollary 16.22: Unique-gate half-packets are gate-independent

Let \(A\subseteq\mathbb N\), let \(q\in A\), and let
\[
U\subset A\setminus\{q\}.
\]
Suppose that for every \(p\in U\) the only unordered two-term
representation of \(q+p\) from \(A\) is the gate pair \(q+p\); equivalently
\[
q+p\notin2(A\setminus\{q\}). \tag{1}
\]
Then
\[
(U+q-U)\cap A\subset\{q\}. \tag{2}
\]
Equivalently, for distinct \(p,r\in U\),
\[
p+q-r\notin A. \tag{3}
\]

Proof. This is Lemma 8.5a.7j with \(f=q\). Explicitly, if distinct
\(p,r\in U\) and
\[
x=p+q-r\in A,
\]
then
\[
q+p=r+x
\]
is a two-term representation of \(q+p\) from \(A\). It is not the gate
pair \(\{q,p\}\): equality would force either \(r=p\) or \(r=q\), both
impossible. This contradicts (1). \(\square\)

Combining this with Corollary 16.21, a hypothetical \(k=3\) counterexample
has the following sharper singleton normal form. Over every finite
balanced certificate test \(T_0\), every sufficiently large-secondary-center
singleton row bank contains a set
\[
U\subset T_0,\qquad |U|\ge |T_0|/2,
\]
which is \(q\)-independent in the sense of (2). For bounded secondary
centers, Lemma 16.19 gives the same conclusion on all tested rows beyond
the bounded threshold. Thus the singleton branch has been reduced from
generic private row banks to moving gate-independent packets, unless the
finite tests themselves contain large balanced-certificate-free halfsets.

### Example 16.23: Dense tests still allow bounded-center unique-gate packets

The gate-independence normal form is not contradicted by balanced
certificate density alone. Let \(L\ge4\),
\[
A_L=[1,L]\cup\{2L\},\qquad q=2L,\qquad d=2L+2,\qquad w=q+d=4L+2,
\]
and put
\[
U=[1,L]\subset A_L\setminus\{q\}.
\]
Then
\[
[3,5L]\subseteq3A_L,\qquad w\notin4(A_L\setminus\{q\}), \tag{1}
\]
and for every \(p\in U\),
\[
w-p\in3A_L,\qquad q+p\notin2(A_L\setminus\{q\}). \tag{2}
\]
Moreover
\[
(U+q-U)\cap A_L=\{q\}. \tag{3}
\]
Thus \(U\) is a full unique-gate, \(q\)-independent packet even though
the dense set \(U\) contains the balanced \(k=3\) certificate
\[
e=1,\qquad y_1=y_2=y_3=2,
\]
for which
\[
y_1+y_2-e=3\in A_L,\qquad
y_1+y_2+y_3-2e=4\in A_L.
\]

Proof. The coverage and privacy assertions in (1) are exactly the
interval-marker calculation from Lemma 16.10:
\[
3[1,L]=[3,3L],\quad 2L+2[1,L]=[2L+2,4L],\quad
4L+[1,L]=[4L+1,5L],
\]
and
\[
4(A_L\setminus\{q\})=4[1,L]=[4,4L],
\]
so \(w=4L+2\) is private after deleting \(q\). For \(p\in[1,L]\),
\[
w-p\in[3L+2,4L+1]\subset[3,5L]\subseteq3A_L.
\]
Also
\[
2(A_L\setminus\{q\})=2[1,L]=[2,2L],
\]
whereas \(q+p\in[2L+1,3L]\), proving the unique-gate condition (2).
Finally
\[
U+q-U=[L+1,3L-1],
\]
whose intersection with \([1,L]\cup\{2L\}\) is exactly \(\{2L\}\). This
proves (3). \(\square\)

This example is only local. Lemma 16.10 proves that the same one-marker
interval construction cannot iterate: the next marker would need to cover
the bridge interval \([x+3L+1,2x]\). Its role here is to calibrate the
remaining positive route. A proof must use the global iteration and
threshold constraints of singleton barriers, not just the existence of
balanced certificates inside the tested rows.

### Lemma 16.24: Late rows above a singleton center are gate-independent

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Fix \(q\in A\), put \(C=A\setminus\{q\}\), and suppose
\[
w=q+d\notin4C. \tag{1}
\]
Let
\[
T\subset C
\]
be finite and satisfy
\[
w-p\ge N_0,\qquad p>d-q-m_0 \qquad(p\in T). \tag{2}
\]
Then
\[
(T+q-T)\cap A\subset\{q\}. \tag{3}
\]

More generally, if the same witness is known to lie below a declared bound
\[
w\le W, \tag{4}
\]
then every finite
\[
T\subset\{p\in C:\ p>W-2q-m_0,\ w-p\ge N_0\}
\]
satisfies (3).

Proof. The first assertion is Lemma 16.19 followed by Corollary 16.22.
Indeed, condition (2) puts every \(p\in T\) above the secondary-center
threshold
\[
d-q-m_0.
\]
Lemma 16.19 therefore says that every \(p\in T\) lies in the unique-gate
branch:
\[
q+p\notin2C.
\]
Corollary 16.22 applied with \(U=T\) gives (3).

For the declared-bound version, (4) gives
\[
d-q=w-2q\le W-2q.
\]
Thus \(p>W-2q-m_0\) implies \(p>d-q-m_0\), and the first assertion applies.
\(\square\)

In particular, if a finite stage declares all witnesses below \(W\), then
any target \(q>W/2\) has no reflected rows at all in the active retained
range: every retained padder below the threshold cut is forced into a
\(q\)-independent unique-gate packet. This is the additive pressure that a
bridge block must evade when it tries to protect elements near the top of
the same declaration window.

### Corollary 16.25: Exact finite singleton witness window

Let \(S\subset\mathbb N\) be finite, let \(q\in S\), and put
\[
C=S\setminus\{q\}.
\]
For any finite interval \(I\subset\mathbb N\), the set of values in \(I\)
that are represented from \(4S\) but remain private after deleting \(q\) is
exactly
\[
\left(I\cap4S\right)\setminus\bigcup_{p\in C}(p+3C). \tag{1}
\]
Equivalently, \(q\) has an order-\(4\) singleton witness in \(I\) if and
only if the set in (1) is nonempty.

If one also requires strict high excess inside the finite stage, with
\[
m_0=\min S,\qquad M=\max S,
\]
then the admissible witness set is
\[
\left\{w\in (I\cap4S)\setminus\bigcup_{p\in C}(p+3C):
        w-q-2m_0\ge M\right\}. \tag{2}
\]

Proof. A value \(w\in I\cap4S\) is a singleton witness for deleting \(q\)
exactly when
\[
w\notin4C.
\]
By Lemma 16.14 this is equivalent to
\[
w-p\notin3C\qquad(p\in C),
\]
or
\[
w\notin\bigcup_{p\in C}(p+3C).
\]
This proves (1). Adding the displayed high-excess inequality gives (2).
\(\square\)

Thus every finite continuation search can be read as a shifted-cover
problem: the coverage block must make the stage's \(3S\)-sumset long
enough, but the same retained elements shift \(3C\) across the candidate
windows for later promoted fillers. The interval-marker and prepared-marker
diagnostics are both instances of this exact criterion.

### Lemma 16.26: Simultaneous gate-independent targets are Sidon-scale

Let \(P\subset\mathbb N\) be finite, and let \(Q\subset P\). Suppose that
for every \(q\in Q\),
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap P\subset\{q\}. \tag{1}
\]
Put
\[
m=|P|,\qquad t=|Q|,\qquad D=\max P-\min P.
\]
Then
\[
t(m-t)+\binom t2\le 2D+1. \tag{2}
\]
In particular, if \(m\ge2\) and \(t\ge m/2\), then
\[
{3m^2\over8}-{m\over4}\le 2D+1. \tag{3}
\]

Proof. Consider the unordered two-element subsets of \(P\) that meet
\(Q\). There are
\[
t(m-t)+\binom t2
\]
of them. We claim that their sums are all distinct.

Suppose two distinct such pairs have the same sum. Choose one pair and
write it as
\[
\{q,p\},\qquad q\in Q,\quad p\in P\setminus\{q\}.
\]
Let the other pair be \(\{r,s\}\). If \(q\in\{r,s\}\), then equality of
sums forces the other endpoint to be \(p\), so the two pairs were the same,
contrary to choice. Thus \(r,s\in P\setminus\{q\}\). From
\[
q+p=r+s
\]
we get
\[
p+q-r=s\in P.
\]
Also \(r\ne p\), since \(r=p\) would imply \(s=q\). Therefore (1) fails
for this \(q\). This contradiction proves the claim.

All these distinct sums lie in the interval
\[
[2\min P,2\max P],
\]
which has \(2D+1\) integer points. This proves (2). If \(m\ge2\) and
\(t\ge m/2\), then
\[
t(m-t)+\binom t2
=tm-{t^2\over2}-{t\over2}
\]
is at least its value at \(t=m/2\) on the interval \(m/2\le t\le m\), namely
\[
{3m^2\over8}-{m\over4}.
\]
This gives (3). \(\square\)

Combined with Lemma 16.24, this gives a concrete obstruction to protecting
many elements of one finite bridge block in the same bounded declaration
window. If a set \(Q\) of targets all have singleton witnesses below
\(W\), and a common retained block \(P\) lies above each threshold
\[
W-2q-\min A,
\]
then \(P\) must obey the Sidon-scale bound (2). Thus a bridge block that
is dense enough to cover a long interval by translates cannot also make a
positive proportion of its own elements late-row gate-independent, unless
the protected targets or the active row ranges escape this common-window
configuration.

### Lemma 16.27: Large interval-marker bridges cannot be half protected in one window

Let \(L\ge4\), and put
\[
D_L=2([1,L]\cup\{2L\})=[2,3L]\cup\{4L\}.
\]
Let
\[
x\ge100L^2
\]
and let
\[
P\subset[x,2x-2]\cap\mathbb N
\]
be finite. Suppose the interval-marker bridge interval
\[
J=[x+3L+1,2x]\cap\mathbb N \tag{1}
\]
is covered by one bridge element and two old terms:
\[
J\subset P+D_L. \tag{2}
\]
Then no subset
\[
Q\subset P,\qquad |Q|\ge |P|/2,
\]
can satisfy
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap P\subset\{q\}
        \qquad(q\in Q). \tag{3}
\]

Proof. Write \(m=|P|\). Each \(p\in P\) contributes at most \(3L\) points
to \(J\) through \(p+D_L\): the interval \(p+[2,3L]\) has \(3L-1\) points,
and \(p+4L\) contributes at most one more point. Since
\[
|J|=x-3L,
\]
the cover (2) gives
\[
m\ge {x-3L\over3L}. \tag{4}
\]
Because \(x\ge100L^2\) and \(L\ge4\), in particular \(x\ge12L\), so
\[
m\ge {x\over4L}. \tag{5}
\]

If \(Q\) satisfying (3) existed, Lemma 16.26 would give, with
\[
D=\max P-\min P\le x-2,
\]
the bound
\[
{3m^2\over8}-{m\over4}\le2D+1\le2x-3. \tag{6}
\]
The function
\[
u\mapsto {3u^2\over8}-{u\over4}
\]
is increasing for \(u\ge1\), and (5) gives \(m\ge x/(4L)\ge1\). Hence the
left side of (6) is at least
\[
{3x^2\over128L^2}-{x\over16L}.
\]
Since \(x\ge100L^2\) and \(L\ge4\), this is at least
\[
{300\over128}x-{1\over64}x>2x,
\]
contradicting (6). \(\square\)

By Lemma 16.11, any large continuation of the interval-marker seed must
produce exactly a cover of the form (2) for the smallest new element. Lemma
16.27 says that such a bridge block cannot also have a same-window
unique-gate half-packet over its own bridge rows. Therefore an iterable
singleton construction based on interval-marker bridges must either keep
the next bridge near the \(O(L^2)\) finite range, protect substantially
fewer than half of the bridge elements at that stage, or arrange staggered
witness windows so that the active row ranges do not share one dense block.

### Corollary 16.28: Abstract bridge covers are Sidon-limited

Let \(P,D\subset\mathbb N\) be finite, and let \(J\subset\mathbb N\) be an
interval of length
\[
R=|J|.
\]
Suppose
\[
J\subset P+D. \tag{1}
\]
Let \(Q\subset P\), \(|Q|\ge |P|/2\), and suppose that for every \(q\in Q\),
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap P\subset\{q\}. \tag{2}
\]
Put
\[
H=|D|,\qquad \Delta=\max P-\min P.
\]
If \(R\ge H\), then
\[
{3R^2\over8H^2}-{R\over4H}\le2\Delta+1. \tag{3}
\]

Proof. Write \(m=|P|\). Since each translate \(p+D\) contains at most
\(H\) points of \(J\), the cover (1) gives
\[
mH\ge R,\qquad m\ge R/H. \tag{4}
\]
If \(m=1\), then \(R\le H\), so the assumption \(R\ge H\) gives \(R=H\);
then the left side of (3) is \(1/8\), while the right side is at least
\(1\). Thus assume \(m\ge2\).

Lemma 16.26 gives
\[
{3m^2\over8}-{m\over4}\le2\Delta+1. \tag{5}
\]
The function \(u\mapsto3u^2/8-u/4\) is increasing for \(u\ge1\), and
\(R/H\ge1\). Combining (4) and (5) proves (3). \(\square\)

This is the reusable finite pressure behind Lemma 16.27. To build a
same-window singleton bridge, one pays for interval coverage by making
\(|P|\) large relative to \(|D|\), while simultaneous gate-independence
forces \(P\) to have Sidon-scale size inside its diameter. Any construction
route using dense translate covers must therefore explain which hypothesis
of Corollary 16.28 fails: the protected targets are sparse, the active row
sets differ, or the witness windows are staggered.

### Corollary 16.29: Same-window singleton protection forces bridge pressure

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Let
\[
P\subset A
\]
be finite, let \(D\subset\mathbb N\) be finite, and let \(J\) be an interval
of length \(R\) such that
\[
J\subset P+D. \tag{1}
\]
Let \(Q\subset P\), \(|Q|\ge |P|/2\), and suppose there is a common bound
\[
W
\]
such that for every \(q\in Q\) there is a singleton private witness
\[
w_q=q+d_q\le W,\qquad w_q\notin4(A\setminus\{q\}), \tag{2}
\]
and every other bridge element is an active late row for that witness:
\[
w_q-p\ge N_0,\qquad p>W-2q-m_0
        \qquad(q\in Q,\ p\in P\setminus\{q\}). \tag{3}
\]
Put
\[
H=|D|,\qquad \Delta=\max P-\min P.
\]
If \(R\ge H\), then
\[
{3R^2\over8H^2}-{R\over4H}\le2\Delta+1. \tag{4}
\]

Proof. Fix \(q\in Q\). Lemma 16.24, applied to the finite set
\[
T=P\setminus\{q\},
\]
uses (2)--(3) to give
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap A\subset\{q\}.
\]
Since \(P\subset A\), this implies the gate-independence condition
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap P\subset\{q\}.
\]
This holds for every \(q\in Q\). Corollary 16.28 now applies to the bridge
cover (1) and gives (4). \(\square\)

Thus every attempted singleton stage using one bounded witness window has
a numerical certificate of failure: if its translate cover violates (4),
then either fewer than half of the bridge block can be protected in that
window, or some protected target must keep many bridge rows below the
late-row threshold in (3). This isolates the remaining singleton escape as
a genuinely staggered-window construction rather than a same-window bridge.

### Diagnostic 16.30: The first interval bridge shows sparse protection debt

The enhanced script
`EXPERIMENTS/interval_marker_next_block_search.py` now records, for every
eligible block, how many new elements have strict singleton witnesses below
the declared endpoint and how many of those lie in the common-row pressure
range of Corollary 16.29.

For the first interval-marker seed
\[
[1,4]\cup\{8\},
\]
the default bounded search checks all next blocks of size at most \(6\) with
candidate values through \(50\). It finds no strict singleton continuation.
More specifically, the best eligible block of size \(6\) is
\[
P=(19,25,26,39,43,44),
\]
with coverage through \(97\) and declared endpoint \(95\). Among these six
new elements, only
\[
19,\ 39
\]
have strict singleton witnesses below \(95\), namely witnesses \(65\) and
\(87\), and only \(39\) lies in the common-row pressure range from
Corollary 16.29.

This remains finite evidence only, but it clarifies the failure mode. The
search is not merely failing to find represented values; most bridge
fillers are deferred immediately, and the few protected fillers do not form
a half-packet in the same-window pressure regime. Thus the next singleton
construction target is not an ordinary bridge block, but a mechanism for
staggering the future witness windows of the deferred fillers while still
maintaining the order-\(3\) coverage buffer.

### Corollary 16.31: Deferred fillers force singleton recurrence or a nonsingleton front

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let
\[
X\subset A
\]
be infinite. Then one of the following alternatives holds:

1. infinitely many \(x\in X\) have singleton late-bad deletions at order
   \(4\), i.e. \(\{x\}\) is late-bad in the sense of Corollary 3.1b with
   \(h=4\);
2. there is an infinite
   \[
   Y\subset X
   \]
   such that the order-\(4\) late-bad subsets of \(Y\) form a nonsingleton
   weak barrier. Equivalently, every infinite \(Z\subset Y\) contains a
   finite late-bad set \(F\subset Z\) with \(|F|\ge2\). Passing to the
   prefix-front supplied by Lemma 3.1c.1 gives a nonsingleton late-bad
   prefix-front on \(Y\).

Proof. Let \(\mathcal L_4\) be the family of order-\(4\) late-bad finite
sets. By Corollary 3.1c, \(\mathcal L_4\) is a weak barrier on \(A\).
If alternative 1 fails, then only finitely many elements of \(X\) are
singleton late-bad. Remove them and call the remaining infinite set \(Y\).
For every infinite \(Z\subset Y\), Corollary 3.1c gives a finite
\[
F\subset Z,\qquad F\in\mathcal L_4.
\]
No singleton subset of \(Y\) lies in \(\mathcal L_4\), by construction, so
\(|F|\ge2\). Thus the restricted late-bad family is a nonsingleton weak
barrier on \(Y\). Lemma 3.1c.1 turns it into a prefix-front, and its
members are still late-bad. Since each contains a nonsingleton late-bad
subset, every front member has size at least \(2\). \(\square\)

Consequently, deferred bridge fillers cannot simply disappear from the
problem. Along any infinite supply of deferred fillers, either the
singleton analysis recurs at later windows, or the construction has entered
the nonsingleton active-trace/front regime. This is exactly the dichotomy
left by the interval-marker diagnostics: same-window singleton protection
is sparse, so an infinite counterexample must pay either with repeated
staggered singleton windows or with collective cross-window barriers.

### Diagnostic 16.32: The first deferred bridge block does not heal one step later

The script `EXPERIMENTS/interval_marker_deferred_followup.py` starts from
the best debt block in Diagnostic 16.30,
\[
S=\{1,2,3,4,8,19,25,26,39,43,44\},
\]
with previous endpoint \(95\), and tests the deferred targets
\[
25,\ 26,\ 43,\ 44.
\]
For each target it tries to add a later block of size at most \(2\), with
candidate values through \(150\), and asks for either an ordinary
singleton witness or a strict high-excess singleton witness.

No target is protected in this bounded search. In every case the strongest
failed window is obtained after adding
\[
(96,99),
\]
where the window
\[
[99,132]
\]
has all \(34\) values represented in \(4S'\), but all \(34\) also lie in
\[
4(S'\setminus\{q\})
\]
for the tested target \(q\). The first poison examples are
\[
99=1+98,\quad 100=1+99,\quad 101=1+100,
\]
with the tails in \(3(S'\setminus\{q\})\).

Thus the simplest staggered repair of the first interval bridge debt
inherits the same shifted-cover poisoning as the same-window attempt. This
does not rule out longer staggered constructions, but it shows that a
successful construction must do more than postpone each deferred filler by
one small bridge block.

### Corollary 16.33: Boundedly many staggered windows are Sidon-limited

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis with threshold \(N_0\)
and minimum \(m_0\). Let \(P,D\subset\mathbb N\) be finite and nonempty,
with
\[
P\subset A,
\]
and let \(J\) be an interval of length
\[
R=|J|
\]
such that
\[
J\subset P+D. \tag{1}
\]
Let \(Q\subset P\), and suppose
\[
|Q|\ge\beta |P|,\qquad 0<\beta\le1. \tag{2}
\]
Assume that \(Q\) is partitioned into at most \(s\) classes
\[
Q=Q_1\cup\cdots\cup Q_s
\]
with the following property. For each \(i\) there is a bound \(W_i\) such
that every \(q\in Q_i\) has a singleton private witness
\[
w_q=q+d_q\le W_i,\qquad w_q\notin4(A\setminus\{q\}), \tag{3}
\]
and every other bridge element is an active late row for that witness:
\[
w_q-p\ge N_0,\qquad p>W_i-2q-m_0
        \qquad(q\in Q_i,\ p\in P\setminus\{q\}). \tag{4}
\]
Put
\[
H=|D|,\qquad \Delta=\max P-\min P,\qquad \gamma={\beta\over s}.
\]
Assume also that
\[
{R\over H}\ge {1\over4\gamma-2\gamma^2}. \tag{5}
\]
Then
\[
\left(\gamma-{\gamma^2\over2}\right){R^2\over H^2}
   -{R\over2H}
\le 2\Delta+1. \tag{6}
\]

Proof. Some class \(Q_i\) has size
\[
t=|Q_i|\ge {|Q|\over s}\ge\gamma |P|. \tag{7}
\]
For every \(q\in Q_i\), Lemma 16.24 applied with the bound \(W_i\) and the
row set \(P\setminus\{q\}\) gives
\[
\bigl((P\setminus\{q\})+q-(P\setminus\{q\})\bigr)\cap P\subset\{q\}.
\]
Lemma 16.26 therefore gives
\[
t(|P|-t)+\binom t2\le2\Delta+1. \tag{8}
\]
Writing \(m=|P|\), the left side of (8) is
\[
tm-{t^2\over2}-{t\over2}.
\]
Since \(t\ge\gamma m\) and \(t\le m\),
\[
t\left(m-{t\over2}\right)\ge
\gamma m\left(m-{\gamma m\over2}\right)
=\left(\gamma-{\gamma^2\over2}\right)m^2,
\]
and also \(-t/2\ge-m/2\). Hence
\[
\left(\gamma-{\gamma^2\over2}\right)m^2-{m\over2}
   \le 2\Delta+1. \tag{9}
\]
The bridge cover (1) gives \(mH\ge R\), so \(m\ge R/H\). By (5), the
function
\[
u\mapsto\left(\gamma-{\gamma^2\over2}\right)u^2-{u\over2}
\]
is increasing for all \(u\ge R/H\). Thus (9) implies (6). \(\square\)

For fixed \(s\) and fixed positive density \(\beta\), inequality (6)
eventually fails for interval bridges whose length is large compared with
\(|D|^2\) and whose bridge block has only linear diameter. Therefore a
staggered singleton construction cannot protect a positive-density part of
each dense bridge block using only boundedly many witness windows. The
remaining singleton escape must use unboundedly many staggered windows,
vanishing protected density per bounded window family, or pass to the
nonsingleton-front alternative of Corollary 16.31.

### Corollary 16.34: Large interval bridges have vanishing bounded-window protection

Fix \(L\ge4\), put
\[
D_L=[2,3L]\cup\{4L\},
\]
and let
\[
x_\nu\to\infty,\qquad {x_\nu\over L^2}\to\infty.
\]
For each \(\nu\), let
\[
P_\nu\subset[x_\nu,2x_\nu-2]\cap A
\]
cover the interval-marker bridge
\[
[x_\nu+3L+1,2x_\nu]\subset P_\nu+D_L. \tag{1}
\]
Fix \(s\ge1\) and \(\beta>0\). Then, for all sufficiently large \(\nu\),
there is no subset
\[
Q_\nu\subset P_\nu,\qquad |Q_\nu|\ge\beta |P_\nu|,
\]
that can be protected by at most \(s\) common-row singleton witness windows
in the sense of Corollary 16.33.

Proof. In Corollary 16.33 take
\[
R_\nu=x_\nu-3L,\qquad H=|D_L|=3L,\qquad
\Delta_\nu\le x_\nu-2.
\]
For fixed \(s,\beta\), the number
\[
\gamma={\beta\over s}
\]
is fixed and positive. The monotonicity condition (5) of Corollary 16.33
holds for all sufficiently large \(\nu\), since \(R_\nu/H\to\infty\).
If such a \(Q_\nu\) existed, Corollary 16.33 would give
\[
\left(\gamma-{\gamma^2\over2}\right){(x_\nu-3L)^2\over9L^2}
   -{x_\nu-3L\over6L}
\le 2x_\nu-3. \tag{2}
\]
The left side is
\[
\asymp_{\beta,s}{x_\nu^2\over L^2},
\]
whereas the right side is \(O(x_\nu)\). Since \(x_\nu/L^2\to\infty\), (2)
fails for all sufficiently large \(\nu\). \(\square\)

Thus an interval-marker singleton construction with genuinely large bridge
gaps cannot use any fixed finite menu of witness windows to protect a
positive fraction of each bridge block. In the singleton branch, the
remaining large-bridge escape is now sharply constrained: every bounded
window family has vanishing protected density, so a counterexample must
encode its protection debt across unboundedly many windows or hand it to a
nonsingleton prefix-front.

### Corollary 16.35: The nonsingleton handoff can be made active

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis, and let \(X\subset A\) be infinite.
Suppose that only finitely many elements of \(X\) are singleton late-bad at
order \(4\). Then there are an infinite
\[
Q\subset X
\]
and a prefix-front
\[
\mathcal F\subset[Q]^{<\omega}
\]
such that every \(F\in\mathcal F\) has \(|F|\ge2\) and has an associated
witness \(w_F\) with the following properties. Put
\[
C_F=A\setminus F.
\]
Then
\[
w_F\ge\max F-1,\qquad w_F\notin4C_F, \tag{1}
\]
\(F\) is inclusion-minimal for the nonrepresentation in (1), every
\(f\in F\) is active in an order-\(4\) repair after the other points of
\(F\) are restored, and for every retained padder
\[
e\in C_F,\qquad w_F-e\ge N_0,
\]
where \(N_0\) is an order-\(3\) threshold for \(A\), the set \(F\)
intersects every three-term representation of \(w_F-e\) from \(A\).

Proof. Remove the finitely many singleton late-bad elements from \(X\), and
call the remaining infinite set \(Y\). By Corollary 16.31, the order-\(4\)
late-bad subsets of \(Y\) form a nonsingleton weak barrier. For every
late-bad \(S\subset Y\), choose a witness
\[
w_S\ge\max S-1,\qquad w_S\notin4(A\setminus S),
\]
using an arbitrarily large hole if \(A\setminus S\) is not an order-\(4\)
basis, and using the delayed-threshold witness otherwise. Shrink \(S\)
inclusion-minimally for this same witness, and call the shrink \(F_S\).

The family of all such \(F_S\) is still a weak barrier on \(Y\), since
\(F_S\subset S\). It has no singleton member. Indeed, if
\[
F_S=\{q\},
\]
then the same witness satisfies
\[
w_S\ge\max S-1\ge q-1
\]
and is missing from \(4(A\setminus\{q\})\). Hence either
\(A\setminus\{q\}\) is not an order-\(4\) basis, or every order-\(4\)
threshold for it is \(>w_S\), and therefore at least \(q\). Thus
\(\{q\}\) would be singleton late-bad in \(Y\), a contradiction.

Lemma 3.1c.4 now thins this weak barrier to a prefix-front
\(\mathcal F\) of actual inclusion-minimal traces on an infinite
\(Q\subset Y\), retaining the same witnesses. The activity of every
deleted point is the inclusion-minimal repair conclusion of Lemma 10.3b
with \(k=3\). The final vertex-cover assertion is Lemma 10.1, again with
\(k=3\). \(\square\)

Thus the handoff in Corollary 16.31 is not merely a front of padded
late-bad sets. Once singleton late-bad points have been exhausted, the
remaining \(k=3\) obstruction may be studied as a genuine nonsingleton
prefix-front of active order-\(4\) holes.

### Corollary 16.36: Bounded-depth nonsingleton debt lands in \(2A\)

Keep the notation of Corollary 16.35. Let
\[
F=\{f_1<\cdots<f_r\}\in\mathcal F
\]
have witness \(w=w_F\), and suppose \(r\ge j\ge2\) and
\[
w\le f_j+D \tag{1}
\]
for some \(D\ge0\). If \(T\subset A\setminus F\) is finite and satisfies
\[
\min T>D,\qquad w-\max T\ge N_0, \tag{2}
\]
then there are an index \(i<j\) and a subset
\[
U\subset T,\qquad |U|\ge {|T|\over j-1},
\]
such that
\[
w-f_i-U\subseteq2A. \tag{3}
\]

Proof. This is Lemma 10.4 specialized to \(k=3\), with the active trace
\(F\), witness \(w\), ordered depth \(j\), and test set \(T\). The
nonrepresentation \(w\notin4(A\setminus F)\) forces every three-term
representation of \(w-t\), \(t\in T\), to use a point of \(F\). Condition
(1) and \(\min T>D\) rule out every endpoint \(f_\ell\) with
\(\ell\ge j\). Pigeonholing among \(f_1,\ldots,f_{j-1}\) gives (3).
\(\square\)

This is the precise point where the \(k=2\) finite-prefix closure cannot be
quoted for the \(k=3\) nonsingleton front. In the \(k=2\) proof the
corresponding bounded-depth rows land in \(A\) itself, producing
reflection-recurrence and fixed certificates. Here they land only in
\(2A\). Any closure of the nonsingleton handoff must either convert these
\(2A\)-valued mirrors into usable \(A\)-mirrors with the four-term budget,
or show that the front is forced into a different branch such as
unbounded ordered depth, unbounded-window singleton coding, or a genuinely
higher-rank collective construction.

### Lemma 16.37: Nonsingleton \(2A\)-rows have a collision split

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite and nonempty, put
\[
C=A\setminus F,
\]
and suppose
\[
w\notin4C. \tag{1}
\]
Fix \(f\in F\), put
\[
m=w-f,
\]
and let \(U\subset C\) be finite with
\[
m-U\subseteq2A. \tag{2}
\]
Define
\[
U_{\rm row}=\{u\in U:m-u\notin2C\},\qquad
U_{\rm gate}=\{u\in U:f+u\notin2C\}. \tag{3}
\]
Then
\[
U=U_{\rm row}\cup U_{\rm gate}. \tag{4}
\]
Consequently at least one of these two sets has size at least
\[
{|U|\over2}. \tag{5}
\]

Moreover, for every \(u\in U_{\rm row}\), every two-term representation of
\(m-u\) from \(A\) meets \(F\). If in addition
\[
m-u\notin F+F,
\]
then there are
\[
g\in F,\qquad c\in C
\]
such that
\[
m-u=g+c. \tag{6}
\]
For every \(u\in U_{\rm gate}\), every two-term representation of
\(f+u\) from \(A\) meets \(F\).

Proof. Suppose \(u\in U\) lies outside both sets in (3). Then
\[
m-u\in2C,\qquad f+u\in2C.
\]
Adding these two retained two-sums gives
\[
w=f+m=(f+u)+(m-u)\in4C,
\]
contradicting (1). This proves (4), and (5) is immediate.

For \(u\in U_{\rm row}\), condition (2) gives \(m-u\in2A\), while the
definition of \(U_{\rm row}\) says \(m-u\notin2C\). Hence every two-term
representation of \(m-u\) from \(A\) uses at least one element of \(F\).
If \(m-u\notin F+F\), such a representation cannot use two elements of
\(F\), so it has the form (6).

The assertion for \(U_{\rm gate}\) is identical: \(f+u\) has the displayed
two-term representation from \(A\), and \(f+u\notin2C\), so every
two-term representation from \(A\) must meet \(F\). \(\square\)

For singleton traces this reduces to Lemma 16.18: the row-dependent branch
reflects through the deleted gate, while the gate branch gives a unique
two-sum translate. For nonsingleton traces the same collision argument
only gives a finite deleted-color palette. Thus a bounded-depth
nonsingleton front must still solve a genuine coloring problem: either many
\(2A\)-rows are forced through deleted colors in \(F\), or many gate
translates \(f+u\) are forced through the same finite deleted palette.

### Corollary 16.38: Large row-dependent packets force certificates

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let \(T_0\subset A\) be finite, and
let \(s\ge1\) have the following certificate property: every subset
\[
V\subset T_0,\qquad |V|\ge s,
\]
contains elements
\[
e,y_1,y_2,y_3\in V,\qquad y_i\ne e,
\]
such that
\[
y_1+y_2-e\in A,\qquad y_1+y_2+y_3-2e\in A. \tag{1}
\]
Fix \(r\ge1\). Then there is \(L_0\) such that the following data do not
exist for any \(L\ge L_0\):

* a finite set \(F\subset A\) with \(1\le |F|\le r\);
* a point \(f\in F\), a witness \(w\notin4(A\setminus F)\), and
  \(m=w-f\);
* a set \(U\subset T_0\setminus F\) with
  \[
  m-U\subseteq2A,\qquad m-\max F>L; \tag{2}
  \]
* the row-dependent set from Lemma 16.37,
  \[
  U_{\rm row}=\{u\in U:m-u\notin2(A\setminus F)\},
  \]
  satisfying
  \[
  |U_{\rm row}|>|F+F|+|F|(s-1). \tag{3}
  \]

Proof. Suppose such data exist for arbitrarily large \(L\). Put
\[
C=A\setminus F.
\]
For \(u\in U_{\rm row}\), Lemma 16.37 says that every two-term
representation of \(m-u\) from \(A\) meets \(F\). At most \(|F+F|\) values
of \(u\) have
\[
m-u\in F+F,
\]
because the map \(u\mapsto m-u\) is injective. By (3), after discarding
these exceptional rows, more than \(|F|(s-1)\) values remain. For each
remaining \(u\), choose a representation
\[
m-u=g_u+c_u,\qquad g_u\in F,\quad c_u\in C.
\]
Pigeonholing over the at most \(|F|\) colors \(g_u\), there are
\[
g\in F,\qquad V\subset T_0,\qquad |V|\ge s,
\]
such that
\[
m-g-V\subset C\subset A. \tag{4}
\]
The center
\[
M=m-g
\]
satisfies
\[
M\ge m-\max F>L.
\]

By the certificate property of \(T_0\), the set \(V\) contains a tuple
\[
e,y_1,y_2,y_3
\]
satisfying (1). Since \(T_0\) is finite and the displayed data exist for
arbitrarily large \(L\), one fixed certificate tuple occurs with centers
\[
M\to\infty
\]
and
\[
M-\{e,y_1,y_2,y_3\}\subset A
\]
by (4). Lemma 2.3b with \(k=3\) gives an infinite deletion whose complement
is an order-\(4\) basis, contradicting the hypothesis on \(A\). \(\square\)

Thus, in a \(k=3\) counterexample, bounded-rank nonsingleton fronts cannot
put a large row-dependent packet over any finite test that is certificate
dense at the corresponding scale. After Lemma 16.37, the remaining
bounded-depth nonsingleton escape must either keep the row-dependent packet
below this finite-color threshold, make the finite tests contain large
certificate-free subsets, or concentrate in the gate-dependent branch.

### Lemma 16.39: Gate-dependent packets are finite-palette independent

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite and nonempty, and
put
\[
C=A\setminus F.
\]
Fix \(f\in F\), and let \(U\subset C\) satisfy
\[
f+u\notin2C\qquad(u\in U). \tag{1}
\]
Then
\[
(U+f-U)\cap A\subseteq F. \tag{2}
\]
Equivalently, if \(u,v\in U\) and
\[
u+f-v\in A,
\]
then \(u+f-v\in F\).

Proof. Suppose
\[
x=u+f-v\in A\setminus F
\]
for some \(u,v\in U\). Since \(v\in U\subset C\) and \(x\in C\), we get
\[
f+u=x+v\in2C,
\]
contradicting (1). Therefore no such \(x\) lies in \(A\setminus F\), which
is exactly (2). \(\square\)

For \(|F|=1\), this is Corollary 16.22. For nonsingleton traces the
forbidden translate set is allowed to hit the finite active palette \(F\),
so the surviving gate branch is not ordinary Sidon independence. It is a
finite-palette independence condition:
\[
U+f-U
\]
must avoid the retained set \(C\). A positive proof must either turn this
finite-palette avoidance into a density or coverage contradiction, or show
that a counterexample can stage these avoided difference translates without
breaking order-\(3\) coverage.

### Lemma 16.40: Retained intervals crush finite-palette gates

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, put
\[
C=A\setminus F,
\]
and fix \(f\in F\). Let \(U\subset C\) be finite and suppose
\[
(U+f-U)\cap A\subseteq F. \tag{1}
\]
If there is \(u_0\in U\) such that
\[
f+U-u_0\subseteq A, \tag{2}
\]
then
\[
|U|\le |F|. \tag{3}
\]
In particular, if \(u_0=\min U\) and
\[
[f,\ f+\max U-\min U]\subseteq A, \tag{4}
\]
then (3) holds.

Proof. By (1) and (2),
\[
f+U-u_0\subseteq F.
\]
The map
\[
u\mapsto f+u-u_0
\]
is injective on \(U\), so \(|U|\le |F|\). If (4) holds with
\(u_0=\min U\), then \(f+U-u_0\) lies in the interval in (4), and hence
in \(A\); this is (2). \(\square\)

Thus a large gate-dependent packet cannot sit inside a block whose
differences from one row are absorbed by an actual interval of \(A\) above
the gate. Any counterexample using the finite-palette gate branch must keep
the translates \(f+U-u_0\) outside the retained set for every possible row
anchor \(u_0\), except at the finitely many active colors in \(F\).

### Lemma 16.41: Finite-palette gates sparsify every anchored shadow

Keep the hypotheses of Lemma 16.40. Then for every anchor \(u_0\in U\),
\[
\bigl|(f+U-u_0)\cap A\bigr|\le |F|. \tag{1}
\]
Equivalently,
\[
\bigl|(f+U-u_0)\setminus A\bigr|\ge |U|-|F|. \tag{2}
\]
In particular, if \(U\) has diameter
\[
\Delta_U=\max U-\min U,
\]
then \(A\) has at most \(|F|\) points in each finite shadow
\[
f+U-u_0\subseteq[f-\Delta_U,\ f+\Delta_U]. \tag{3}
\]

Proof. Lemma 16.39 gives
\[
(U+f-U)\cap A\subseteq F.
\]
Since
\[
f+U-u_0\subset U+f-U,
\]
we have
\[
(f+U-u_0)\cap A\subseteq F.
\]
This proves (1), because the right side has size at most \(|F|\). The map
\[
u\mapsto f+u-u_0
\]
is injective, so \(|f+U-u_0|=|U|\), giving (2). Finally (3) is the range
bound for \(u,u_0\in U\). \(\square\)

The script `EXPERIMENTS/finite_palette_gate_pressure.py` verifies this
shadow-count statement on exhaustive finite toy windows. This lemma shows
why the finite-palette gate branch is a genuine sparse-shadow problem, not
a Sidon problem: collisions among sums inside \(U\) are allowed, but every
anchored difference translate must be almost entirely absent from the
retained set.

### Corollary 16.42: Gate packets avoid anchored copies of finite tests

Keep the hypotheses of Lemma 16.41. Then for every finite test
\[
T\subset A
\]
and every anchor \(u_0\in U\),
\[
\bigl|U\cap(u_0+T-f)\bigr|\le |F|. \tag{1}
\]
Equivalently, if \(V\subset U\) and
\[
f+V-u_0\subset A,
\]
then \(|V|\le |F|\).

In particular, if \(A\) contains an interval \(I\) and \(U\) contains the
anchored translate
\[
u_0+I-f,
\]
then
\[
|I|\le |F|. \tag{2}
\]

Proof. The map
\[
u\mapsto f+u-u_0
\]
sends \(U\cap(u_0+T-f)\) injectively into
\[
(f+U-u_0)\cap A.
\]
Lemma 16.41 bounds this latter set by \(|F|\), proving (1). The equivalent
form is the same statement with
\[
T=f+V-u_0.
\]
Taking \(T=I\) gives (2). \(\square\)

Thus a finite-palette gate packet can be dense internally only if it avoids
aligned copies of every dense finite piece of \(A\). In particular, an
interval-marker bridge cannot place a large gate-dependent packet inside a
translate of the old interval block; it must either be arithmetically
misaligned with that old block, keep the active palette large, or leave the
finite-palette branch.

### Corollary 16.43: Bounded-rank packets reduce to gate shadows

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let \(T_0\subset A\) be finite and
let \(s\ge1\) be such that every subset of \(T_0\) of size at least \(s\)
contains a \(k=3\) certificate tuple as in Corollary 16.38. Fix \(r\ge1\).
Then there is \(L_0\) such that the following holds for all \(L\ge L_0\).

Suppose
\[
F\subset A,\qquad 1\le |F|\le r,\qquad f\in F,
\]
\[
C=A\setminus F,\qquad w\notin4C,\qquad m=w-f,
\]
and
\[
U\subset T_0\setminus F,\qquad m-U\subseteq2A,\qquad m-\max F>L. \tag{1}
\]
Define
\[
R_F=|F+F|+|F|(s-1)
\]
and
\[
U_{\rm gate}=\{u\in U:f+u\notin2C\}. \tag{2}
\]
Then
\[
|U_{\rm gate}|\ge |U|-R_F. \tag{3}
\]
Moreover
\[
(U_{\rm gate}+f-U_{\rm gate})\cap A\subseteq F, \tag{4}
\]
and for every finite \(T\subset A\) and every anchor \(u_0\in U_{\rm gate}\),
\[
\bigl|U_{\rm gate}\cap(u_0+T-f)\bigr|\le |F|. \tag{5}
\]

Proof. Take \(L_0\) from Corollary 16.38 for the fixed \(T_0,s,r\). Under
the displayed hypotheses, Lemma 16.37 gives
\[
U=U_{\rm row}\cup U_{\rm gate},
\]
where
\[
U_{\rm row}=\{u\in U:m-u\notin2C\}.
\]
Corollary 16.38 forbids
\[
|U_{\rm row}|>R_F
\]
for \(L\ge L_0\). Hence
\[
|U_{\rm gate}|\ge |U|-|U_{\rm row}|\ge |U|-R_F,
\]
which proves (3). Statement (4) is Lemma 16.39 applied to
\(U_{\rm gate}\), and (5) is Corollary 16.42. \(\square\)

Thus bounded-rank, bounded-depth nonsingleton \(k=3\) debt has a sharp
finite-test normal form. Over certificate-dense tests, all rows beyond a
bounded finite-color allowance must become gate-dependent; those rows then
avoid every anchored copy of every finite \(A\)-test. A remaining
counterexample must therefore make the gate-shadow packet move away from
all dense old pieces of \(A\), use tests with large certificate-free
subsets, or escape bounded rank/depth.

### Lemma 16.44: Intervals have \(k=3\) certificate threshold three

Let
\[
I=[a,L]\cap\mathbb N
\]
be a nonempty interval, and suppose \(A\) contains \(I\). Every subset
\[
V\subset I,\qquad |V|\ge3,
\]
contains a \(k=3\) certificate tuple
\[
e,y_1,y_2,y_3\in V,\qquad y_i\ne e,
\]
with
\[
y_1+y_2-e\in A,\qquad y_1+y_2+y_3-2e\in A. \tag{1}
\]

Proof. It is enough to prove the claim for a three-point subset
\[
\{a_0<b_0<c_0\}\subset V.
\]
Put
\[
d=b_0-a_0,\qquad h=c_0-b_0.
\]
Choose
\[
e=b_0,\qquad y_1=a_0,\qquad y_2=c_0.
\]
Then
\[
y_1+y_2-e=a_0+h\in[a_0,c_0]\subset I. \tag{2}
\]
If
\[
h\ge d,
\]
take \(y_3=a_0\). Then
\[
y_1+y_2+y_3-2e=a_0+h-d,
\]
which lies in \([a_0,c_0]\), hence in \(I\).

If instead
\[
h<d,
\]
take \(y_3=c_0\). Then
\[
y_1+y_2+y_3-2e=a_0+2h\in I.
\]
Indeed \(a_0\le a_0+2h<c_0\), since \(h<d\).
In both cases (1) holds. \(\square\)

### Corollary 16.45: Interval tests force bounded-rank gate shadows

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let \(T_0\subset A\) be an interval.
Fix \(r\ge1\). Then there is \(L_0\) such that the conclusion of Corollary
16.43 holds for \(T_0\) with
\[
s=3,\qquad R_F=|F+F|+2|F|. \tag{1}
\]
In particular, if \(|F|\le r\), then all but at most
\[
{r(r+1)\over2}+2r \tag{2}
\]
rows of \(U\) lie in the finite-palette gate-shadow branch.

Proof. Lemma 16.44 says that every three-point subset of \(T_0\) contains
the \(k=3\) certificate tuple required by Corollary 16.38. Apply Corollary
16.43 with \(s=3\). Since
\[
|F+F|\le {|F|(|F|+1)\over2},
\]
the uniform bound (2) follows from (1). \(\square\)

Thus interval row tests leave very little room for bounded-rank
row-dependent debt. A bounded-rank nonsingleton obstruction over an
interval must put almost every tested row into the finite-palette gate
branch, where Corollary 16.42 forbids aligned copies of the same interval.

### Lemma 16.46: Same-interval finite-palette gates are bounded

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and let
\[
I=[a,b]\cap\mathbb N\subset A
\]
be an interval. Fix
\[
f\in F\cap I,
\]
and let \(U\subset I\setminus F\) satisfy
\[
(U+f-U)\cap A\subseteq F. \tag{1}
\]
Then
\[
|U|\le2|F|. \tag{2}
\]

Proof. If \(U=\varnothing\), there is nothing to prove. Put
\[
u_-=\min U,\qquad u_+=\max U.
\]
By Corollary 16.42 with \(T=I\) and anchor \(u_-\),
\[
|U\cap(u_-+I-f)|\le |F|. \tag{3}
\]
Since \(f\in I\), the interval \(u_-+I-f\) contains
\[
[u_-,\ u_-+b-f].
\]
Thus (3) bounds the lower part
\[
U_-=U\cap[u_-,\ u_-+b-f].
\]

Similarly, Corollary 16.42 with anchor \(u_+\) gives
\[
|U\cap(u_++I-f)|\le |F|.
\]
The interval \(u_++I-f\) contains
\[
[u_++a-f,\ u_+],
\]
so the upper part
\[
U_+=U\cap[u_++a-f,\ u_+]
\]
has size at most \(|F|\).

The two displayed intervals cover \(U\). Indeed, if they did not, then
\[
u_-+b-f<u_++a-f,
\]
or \(u_+-u_->b-a\), impossible because \(U\subset I=[a,b]\). Therefore
\[
U=U_-\cup U_+,
\]
and (2) follows. \(\square\)

### Corollary 16.47: Same-interval bounded-rank packets are bounded

In the setting of Corollary 16.45, assume in addition that the active color
\[
f\in F
\]
belongs to the interval \(T_0\). Then, for all sufficiently large \(L\),
every packet \(U\) satisfying the hypotheses of Corollary 16.45 has
\[
|U|\le |F+F|+4|F|. \tag{1}
\]
In particular, if \(|F|\le r\), then
\[
|U|\le {r(r+1)\over2}+4r. \tag{2}
\]

Proof. Corollary 16.45 leaves at most \(|F+F|+2|F|\) rows outside the
gate-dependent set \(U_{\rm gate}\). Since \(f\in T_0\) and
\[
U_{\rm gate}\subset T_0,
\]
Lemma 16.46 gives
\[
|U_{\rm gate}|\le2|F|.
\]
Adding the two bounds proves (1), and (2) follows from
\[
|F+F|\le {|F|(|F|+1)\over2}.
\]
\(\square\)

Thus a bounded-rank nonsingleton obstruction cannot keep its active color
inside the same dense interval that supplies the tested rows. A large
interval-test packet must either use active colors outside that interval,
move to certificate-free noninterval tests, or escape bounded rank/depth.

### Lemma 16.48: Near-interval finite-palette gates are edge-bounded

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and let
\[
I=[a,b]\cap\mathbb N\subset A
\]
be an interval. Fix \(f\in F\), and let \(U\subset I\setminus F\) satisfy
\[
(U+f-U)\cap A\subseteq F. \tag{1}
\]
If \(f<a\), put
\[
\delta=a-f.
\]
Then
\[
|U|\le \delta+|F|. \tag{2}
\]
If \(f>b\), put
\[
\delta=f-b.
\]
Then again
\[
|U|\le \delta+|F|. \tag{3}
\]

Proof. Assume first \(f<a\), and suppose \(U\ne\varnothing\). Let
\[
u_-=\min U.
\]
By Corollary 16.42 with \(T=I\) and anchor \(u_-\),
\[
|U\cap(u_-+I-f)|\le |F|. \tag{4}
\]
Since
\[
u_-+I-f=[u_-+\delta,\ u_-+b-f]
\]
and \(u_-\ge a>f\), the upper endpoint is at least \(b\). Hence (4) bounds
all rows of \(U\) in
\[
[u_-+\delta,\ b].
\]
The remaining rows lie in
\[
[u_-,\ u_-+\delta-1],
\]
which has \(\delta\) integer points. This proves (2).

The case \(f>b\) is symmetric. Let \(u_+=\max U\). Corollary 16.42 with
anchor \(u_+\) bounds
\[
U\cap(u_++I-f).
\]
Here
\[
u_++I-f=[u_+-(f-a),\ u_+-\delta],
\]
and because \(u_+\le b<f\), the lower endpoint is at most \(a\). Thus all
rows of \(U\) in
\[
[a,\ u_+-\delta]
\]
contribute at most \(|F|\), while the remaining rows lie in the
\(\delta\)-point interval
\[
[u_+-\delta+1,\ u_+].
\]
This proves (3). \(\square\)

### Corollary 16.49: Large interval packets force far gates or unbounded rank

In the setting of Corollary 16.45, suppose \(T_0=[a,b]\cap\mathbb N\) is an
interval, \(|F|\le r\), \(M\ge0\), and
\[
U\subset T_0
\]
satisfies the hypotheses of Corollary 16.45 for some active color
\[
f\in F.
\]
For all sufficiently large \(L\), if
\[
|U|>{r(r+1)\over2}+4r+M,
\]
then either
\[
f<a-M-r
\]
or
\[
f>b+M+r. \tag{1}
\]

Proof. By Corollary 16.45, all but at most
\[
{r(r+1)\over2}+2r
\]
rows of \(U\) lie in \(U_{\rm gate}\). Hence
\[
|U_{\rm gate}|>M+2r. \tag{2}
\]
If \(f\in T_0\), Corollary 16.47 gives
\[
|U|\le {r(r+1)\over2}+4r,
\]
contradicting the displayed lower bound. Thus \(f\notin T_0\).

Assume \(f<a\). Lemma 16.48 applied to the gate-dependent packet
\(U_{\rm gate}\) gives
\[
|U_{\rm gate}|\le a-f+|F|\le a-f+r.
\]
Together with (2), this forces
\[
a-f>M+r,
\]
or \(f<a-M-r\). The case \(f>b\) is identical. \(\square\)

The quantifier in Corollary 16.49 is deliberately coarse: its role is to
show that large bounded-rank interval packets cannot use active colors at
bounded distance from the tested interval. After the row-dependent
allowance is removed, any surviving finite-palette gate must be far outside
the interval, so the next obstruction must use long-range gate shadows
rather than same-block or near-block geometry.

### Lemma 16.50: Retained subintervals exclude gate rows

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and put
\[
C=A\setminus F.
\]
Let
\[
J=[\alpha,\beta]\cap\mathbb N\subset C
\]
be a retained interval, let \(f\in F\), and let \(U\subset C\) satisfy
\[
f+u\notin2C\qquad(u\in U). \tag{1}
\]
Then
\[
U\cap(2J-f)=\varnothing. \tag{2}
\]
Equivalently,
\[
U\cap[2\alpha-f,\ 2\beta-f]=\varnothing. \tag{3}
\]

Proof. If \(u\in U\cap(2J-f)\), then
\[
f+u\in2J\subseteq2C,
\]
contradicting (1). Since \(2J=[2\alpha,2\beta]\), (3) is the interval
form. \(\square\)

### Corollary 16.51: Far gates must avoid retained two-sum bands

Let \(I=[a,b]\cap\mathbb N\), let \(J=[\alpha,\beta]\cap\mathbb N\), and
suppose
\[
J\subset I\cap(A\setminus F).
\]
Let \(f\in F\), and let \(U\subset I\) satisfy
\[
f+u\notin2(A\setminus F)\qquad(u\in U). \tag{1}
\]
Then
\[
|U|\le |I\setminus[2\alpha-f,\ 2\beta-f]|. \tag{2}
\]
In particular, if
\[
2\alpha-b\le f\le2\beta-a, \tag{3}
\]
then \(U=\varnothing\).

Proof. Lemma 16.50 says that \(U\) is disjoint from the band
\[
[2\alpha-f,\ 2\beta-f].
\]
Since \(U\subset I\), (2) follows. Condition (3) is exactly the assertion
that the band covers all of \(I=[a,b]\), giving \(U=\varnothing\).
\(\square\)

Thus the far-gate escape in Corollary 16.49 is not arbitrary. If the tested
interval contains a long retained subinterval \(J\), then every active gate
whose translate \(2J-f\) crosses the tested interval kills the gate packet
there. Surviving large packets must place \(f\) so far away that
\[
2J-f
\]
misses most of the row interval, or else arrange that deletion holes
fragment every long retained subinterval of the test block.

### Lemma 16.52: Finite deletions leave a long retained run

Let
\[
I=[a,b]\cap\mathbb N
\]
be an interval of length
\[
n=b-a+1,
\]
and let \(F\subset I\) have \(|F|\le r\). Then \(I\setminus F\) contains an
interval \(J\) of length at least
\[
\left\lceil {n-r\over r+1}\right\rceil. \tag{1}
\]

Proof. The \(r\) deleted points split the \(n-|F|\) retained points of
\(I\setminus F\) into at most \(|F|+1\le r+1\) consecutive runs. One run
has length at least
\[
\left\lceil {n-|F|\over |F|+1}\right\rceil.
\]
For \(0\le t\le r\), the function
\[
{n-t\over t+1}
\]
is decreasing in \(t\). Therefore this lower bound is at least (1).
\(\square\)

### Corollary 16.53: Retained runs impose gate exclusion bands

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite with
\[
|F|\le r,
\]
and let
\[
I=[a,b]\cap\mathbb N\subset A
\]
have length \(n\). Then there is a retained interval
\[
J=[\alpha,\beta]\cap\mathbb N\subset I\cap(A\setminus F)
\]
of length
\[
\ell=\beta-\alpha+1\ge\left\lceil {n-r\over r+1}\right\rceil. \tag{1}
\]
For every \(f\in F\) and every gate-dependent packet
\[
U\subset I,\qquad f+u\notin2(A\setminus F)\quad(u\in U),
\]
one has
\[
|U|\le n-\Lambda(f), \tag{2}
\]
where
\[
\Lambda(f)=
\left|
[a,b]\cap[2\alpha-f,\ 2\beta-f]
\right|. \tag{3}
\]
In particular, if \(|U|>n-M\), then
\[
\Lambda(f)<M. \tag{4}
\]
If also
\[
M\le2\ell-1,
\]
then the band \(2J-f\) has length at least \(M\), and (4) forces
\[
f<2\alpha-b+M-1
\quad\text{or}\quad
f>2\beta-a-M+1. \tag{5}
\]

Proof. Lemma 16.52 gives \(J\). Corollary 16.51 says that \(U\) is
disjoint from the band
\[
[2\alpha-f,\ 2\beta-f].
\]
Inside \(I\), this removes exactly \(\Lambda(f)\) possible row positions,
so (2) follows. If \(|U|>n-M\), then (2) gives \(\Lambda(f)<M\).

Finally assume \(M\le2\ell-1\). The intersection in (3) then has at least
\(M\) points unless the left endpoint of the band lies after the first
\(M-1\) points of \(I\), or the right endpoint lies before the last
\(M-1\) points of \(I\). Written out, these two alternatives are exactly
(5). \(\square\)

Thus a large gate packet over an interval cannot merely put its active
color far from the interval endpoints. It must avoid the exclusion band of
some long retained run left after deleting \(F\). For bounded rank, that
run has length comparable to \(|I|/(r+1)\), so a packet occupying almost all
of \(I\) forces each active gate outside a long forbidden interval.

### Lemma 16.54: Finite interval deletions leave a central two-sum band

Let
\[
I=[a,b]\cap\mathbb N
\]
have length
\[
n=b-a+1,
\]
and let \(F\subset I\) have \(|F|\le r\). Put
\[
C=I\setminus F.
\]
If \(n>2r\), then
\[
[2a+2r,\ 2b-2r]\cap\mathbb N\subseteq2C. \tag{1}
\]

Proof. Fix
\[
t\in[2a+2r,\ 2b-2r].
\]
The number of ordered pairs
\[
(x,y)\in I^2,\qquad x+y=t,
\]
is
\[
N(t)=\min(b,t-a)-\max(a,t-b)+1.
\]
For \(t\le a+b\), this is \(t-2a+1\), while for \(t\ge a+b\), it is
\[
2b-t+1.
\]
The displayed range for \(t\) gives
\[
N(t)\ge2r+1.
\]
Each deleted point \(z\in F\) occurs in at most two ordered pairs
\[
(z,t-z),\qquad(t-z,z).
\]
Thus the deleted points destroy at most \(2|F|\le2r\) ordered
representations. At least one ordered representation remains with both
coordinates in \(C\), so \(t\in2C\). \(\square\)

The script `EXPERIMENTS/interval_central_sum_band.py` exhaustively checks
this band inclusion for small intervals and deletion ranks.

### Corollary 16.55: Central two-sum bands exclude gate rows

Let
\[
I=[a,b]\cap\mathbb N\subset A
\]
have length \(n\), let \(F\subset A\) satisfy
\[
|F\cap I|\le r,
\]
and put
\[
C=A\setminus F.
\]
Assume \(n>2r\), and let
\[
U\subset I\setminus F,\qquad f\in F,
\]
satisfy
\[
f+u\notin2C\qquad(u\in U). \tag{1}
\]
Then
\[
U\cap[2a+2r-f,\ 2b-2r-f]=\varnothing. \tag{2}
\]
Consequently
\[
|U|\le
\left|I\setminus[2a+2r-f,\ 2b-2r-f]\right|. \tag{3}
\]

Proof. Lemma 16.54 applied to the interval deletion \(F\cap I\) gives
\[
[2a+2r,\ 2b-2r]\subseteq2(I\setminus F)\subseteq2C.
\]
If \(u\) lay in the interval in (2), then
\[
f+u\in[2a+2r,\ 2b-2r]\subseteq2C,
\]
contradicting (1). This proves (2), and (3) follows from
\(U\subset I\). \(\square\)

### Corollary 16.56: Large interval gate packets force far active colors

Keep the hypotheses of Corollary 16.55. Let \(M\ge0\) be an integer. If
\[
|U|>2M,
\]
then
\[
f<a+2r-M
\quad\text{or}\quad
f>b-2r+M. \tag{1}
\]
Equivalently, if
\[
a+2r-M\le f\le b-2r+M,
\]
then every gate-dependent packet \(U\subset I\) has size at most \(2M\).

Proof. If
\[
a+2r-M\le f\le b-2r+M,
\]
then the forbidden interval in Corollary 16.55 contains
\[
[a+M,\ b-M]\cap\mathbb N.
\]
Only the first \(M\) and last \(M\) positions of \(I\) can remain, and in
particular no more than \(2M\) positions remain. Corollary 16.55 gives
\(|U|\le2M\). Taking the contrapositive proves (1). \(\square\)

Thus the far-gate branch is also sharply constrained by ordinary interval
two-sum coverage. Once only boundedly many active colors are deleted from a
long interval, the central two-sum band is retained; any gate whose
translate sends many rows into that band is impossible. A large bounded-rank
interval packet must place its active color outside the corresponding
central gate range, not merely outside the original interval.

### Corollary 16.57: Bounded-rank interval packets force central escape

In the setting of Corollary 16.45, suppose
\[
T_0=I=[a,b]\cap\mathbb N
\]
is an interval of length \(n>2r\), \(|F|\le r\), and
\[
U\subset I
\]
satisfies the hypotheses of Corollary 16.45 for an active color
\[
f\in F.
\]
Put
\[
B_r={r(r+1)\over2}+2r.
\]
For all sufficiently large witness parameters \(L\), if \(M\ge0\) and
\[
|U|>B_r+2M, \tag{1}
\]
then
\[
f<a+2r-M
\quad\text{or}\quad
f>b-2r+M. \tag{2}
\]

Proof. Corollary 16.45 leaves at most \(B_r\) rows outside the
finite-palette gate-dependent branch. Thus the gate-dependent subpacket
\[
U_{\rm gate}\subset U
\]
satisfies
\[
|U_{\rm gate}|\ge |U|-B_r>2M.
\]
For every \(u\in U_{\rm gate}\),
\[
f+u\notin2(A\setminus F).
\]
Corollary 16.56 applied to \(U_{\rm gate}\), with
\[
C=A\setminus F,
\]
gives (2). \(\square\)

### Corollary 16.58: Dense bounded-rank interval packets have linearly far gates

Fix \(r\ge1\) and \(0<\eta\le1\). In the setting of Corollary 16.57,
there is \(N=N(r,\eta)\) such that whenever \(I=[a,b]\cap\mathbb N\) has
length \(n\ge N\) and
\[
|U|\ge\eta n, \tag{1}
\]
then, for all sufficiently large witness parameters \(L\),
\[
f<a-{\eta n\over4}
\quad\text{or}\quad
f>b+{\eta n\over4}. \tag{2}
\]

Proof. Let
\[
B_r={r(r+1)\over2}+2r.
\]
Choose \(N\) so large that \(n\ge N\) implies
\[
n>2r,\qquad
{\eta n-B_r-1\over2}\ge{\eta n\over3}+1,\qquad
2r\le{\eta n\over12}. \tag{3}
\]
Set
\[
M=\left\lfloor{\eta n-B_r-1\over2}\right\rfloor .
\]
Then \(M\ge\eta n/3\), and (1) gives
\[
|U|\ge\eta n>B_r+2M.
\]
Corollary 16.57 yields
\[
f<a+2r-M
\quad\text{or}\quad
f>b-2r+M.
\]
By (3),
\[
M-2r\ge{\eta n\over4},
\]
which is exactly (2). \(\square\)

### Corollary 16.59: Pointwise gate-distance controls interval packet size

In the setting of Corollary 16.57, put
\[
B_r={r(r+1)\over2}+2r
\]
and define the central gate distance
\[
D_I(f;r)=\max\{0,\ a+2r-f,\ f-b+2r\}. \tag{1}
\]
For all sufficiently large witness parameters \(L\),
\[
|U|\le B_r+2D_I(f;r). \tag{2}
\]
In particular, if
\[
a+2r\le f\le b-2r,
\]
then \(|U|\le B_r\).

Proof. Let \(D=D_I(f;r)\). By definition of \(D\),
\[
a+2r-D\le f\le b-2r+D. \tag{3}
\]
If \(|U|>B_r+2D\), Corollary 16.57 with \(M=D\) gives
\[
f<a+2r-D
\quad\text{or}\quad
f>b-2r+D,
\]
contradicting (3). Hence (2) holds. The final assertion is the case
\(D=0\). \(\square\)

The script `EXPERIMENTS/interval_gate_profile.py` exhaustively checks the
interval-only version of (2), before adding the bounded row-dependent
allowance \(B_r\), on small translated intervals.

### Lemma 16.60: Finite gate palettes have additive interval profile

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and put
\[
C=A\setminus F.
\]
Let
\[
I=[a,b]\cap\mathbb N\subset A
\]
have length \(n>2r\), and assume
\[
|F\cap I|\le r.
\]
Let \(P\subset F\) be finite. For each \(f\in P\), let
\[
U_f\subset I\setminus F
\]
satisfy
\[
f+u\notin2C\qquad(u\in U_f). \tag{1}
\]
Then
\[
\left|\bigcup_{f\in P}U_f\right|
\le
2\sum_{f\in P}D_I(f;r), \tag{2}
\]
where
\[
D_I(f;r)=\max\{0,\ a+2r-f,\ f-b+2r\}.
\]

Proof. Corollary 16.55 applied to each \(f\in P\) gives
\[
U_f\cap[2a+2r-f,\ 2b-2r-f]=\varnothing. \tag{3}
\]
Equivalently, \(U_f\) lies outside the translate of the central retained
two-sum band by \(-f\). Since the definition of \(D_I(f;r)\) gives
\[
a+2r-D_I(f;r)\le f\le b-2r+D_I(f;r),
\]
Corollary 16.56, with \(M=D_I(f;r)\), gives
\[
|U_f|\le2D_I(f;r). \tag{4}
\]
Summing (4) over \(f\in P\) and using the union bound proves (2).
\(\square\)

### Corollary 16.61: Coordinated interval covers need total far-gate distance

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Let
\[
I=[a,b]\cap\mathbb N\subset A
\]
have length \(n>2r\), let \(F\subset A\) satisfy \(1\le|F|\le r\), and let
\[
P\subset F.
\]
For each \(f\in P\), suppose \(U_f\subset I\) satisfies the hypotheses of
Corollary 16.45 for the active color \(f\), with witness parameter
sufficiently large for the fixed interval \(I\) and rank bound \(r\).
Then
\[
\left|\bigcup_{f\in P}U_f\right|
\le
|P|B_r+2\sum_{f\in P}D_I(f;r), \tag{1}
\]
where
\[
B_r={r(r+1)\over2}+2r.
\]
Consequently, for every \(0<\eta\le1\) there is \(N=N(r,\eta)\) such that
if \(n\ge N\) and
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{2}
\]
then some \(f\in P\) satisfies
\[
D_I(f;r)\ge{\eta n\over4r}. \tag{3}
\]
For the same \(N\), this implies
\[
f<a-{\eta n\over8r}
\quad\text{or}\quad
f>b+{\eta n\over8r}. \tag{4}
\]

Proof. For each \(f\in P\), Corollary 16.45 leaves at most \(B_r\) rows of
\(U_f\) outside the gate-dependent packet
\[
U_{f,{\rm gate}}=\{u\in U_f:f+u\notin2(A\setminus F)\}.
\]
Applying Lemma 16.60 to the family \(U_{f,{\rm gate}}\) gives
\[
\left|\bigcup_{f\in P}U_{f,{\rm gate}}\right|
\le
2\sum_{f\in P}D_I(f;r).
\]
Adding the at most \(|P|B_r\) row-dependent exceptions proves (1).

Choose \(N\) so large that \(n\ge N\) implies
\[
rB_r\le{\eta n\over2}
\quad\text{and}\quad
2r\le{\eta n\over8r}. \tag{5}
\]
If (2) holds, then (1) and \(|P|\le r\) give
\[
\sum_{f\in P}D_I(f;r)
\ge {\,\eta n-|P|B_r\,\over2}
\ge{\eta n\over4}.
\]
Since \(|P|\le r\), one \(f\in P\) satisfies (3).

Finally, if \(D_I(f;r)\ge\eta n/(4r)\), then by definition of \(D_I\)
either
\[
a+2r-f\ge{\eta n\over4r}
\]
or
\[
f-b+2r\ge{\eta n\over4r}.
\]
Using (5) yields (4). \(\square\)

### Corollary 16.62: Near-gate dense covers force rank growth

Keep the setting of Corollary 16.61. Suppose that
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n \tag{1}
\]
for some \(0<\eta\le1\), and that every active color in \(P\) has central
gate distance at most \(\Delta\):
\[
D_I(f;r)\le\Delta\qquad(f\in P). \tag{2}
\]
Then, for all sufficiently large witness parameters,
\[
\eta n\le rB_r+2r\Delta, \tag{3}
\]
where
\[
B_r={r(r+1)\over2}+2r.
\]
In particular, if
\[
\Delta\le{\eta n\over4r}, \tag{4}
\]
then
\[
r^3+5r^2\ge \eta n. \tag{5}
\]

Proof. Corollary 16.61 gives
\[
\left|\bigcup_{f\in P}U_f\right|
\le |P|B_r+2\sum_{f\in P}D_I(f;r).
\]
Using \(|P|\le|F|\le r\) and (2), this gives
\[
\eta n\le rB_r+2r\Delta,
\]
which is (3). If (4) holds, then
\[
rB_r\ge{\eta n\over2}.
\]
Since
\[
rB_r={r^3+5r^2\over2},
\]
we get (5). \(\square\)

Thus a dense bounded-depth interval cover cannot hide all active colors
near the central gate range unless the deletion rank grows at least on the
cubic scale dictated by (5). This does not close the unbounded-rank branch,
but it removes the possibility that growing rank is merely cosmetic: near
gates must carry genuinely increasing active traces.

### Lemma 16.63: Cross-interval retained bands exclude dense gate packets

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and put
\[
C=A\setminus F.
\]
Let
\[
I=[a,b]\cap\mathbb N
\]
have length \(n\), and let
\[
J=[\alpha,\beta]\cap\mathbb N\subset C
\]
have length \(\ell=\beta-\alpha+1\). Fix \(f\in F\), and let
\[
U\subset I\cap C
\]
satisfy
\[
f+u\notin2C\qquad(u\in U). \tag{1}
\]
If \(1\le M\le\min\{n,2\ell-1\}\) and
\[
|U|>n-M, \tag{2}
\]
then
\[
f<2\alpha-b+M-1
\quad\text{or}\quad
f>2\beta-a-M+1. \tag{3}
\]

Proof. By Lemma 16.50,
\[
U\cap[2\alpha-f,\ 2\beta-f]=\varnothing. \tag{4}
\]
Suppose neither inequality in (3) holds. Then
\[
2\alpha-f\le b-M+1,\qquad 2\beta-f\ge a+M-1. \tag{5}
\]
The interval
\[
K=[2\alpha-f,\ 2\beta-f]
\]
has length \(2\ell-1\ge M\). Since \(M\le n\), the two inequalities in
(5) say that \(K\) does not start after the last possible \(M\)-point
subinterval of \(I\), and does not end before the first possible
\(M\)-point subinterval of \(I\). To spell out the interval geometry, write
\(K=[L,R]\). If \(L<a\), then \(R\ge a+M-1\) and \(b\ge a+M-1\), so
\[
|I\cap K|\ge M.
\]
If \(R>b\), then \(L\le b-M+1\) and \(a\le b-M+1\), so again
\[
|I\cap K|\ge M.
\]
In the remaining case \(a\le L\le R\le b\), the intersection is all of
\(K\), whose length is at least \(M\). Hence \(|I\cap K|\ge M\) in every
case.
Thus (4) leaves at most \(n-M\) points of \(I\) available for \(U\),
contradicting (2). \(\square\)

### Corollary 16.64: Positive-density packets avoid deep cross-block overlap

Keep the setting of Lemma 16.63, and let \(0<\eta\le1\). Put
\[
M_\eta=\lfloor(1-\eta)n\rfloor+1. \tag{1}
\]
If
\[
M_\eta\le2\ell-1
\]
and
\[
|U|\ge\eta n, \tag{2}
\]
then
\[
f<2\alpha-b+M_\eta-1
\quad\text{or}\quad
f>2\beta-a-M_\eta+1. \tag{3}
\]

Proof. Since
\[
n-M_\eta<\eta n,
\]
condition (2) gives \(|U|>n-M_\eta\). Lemma 16.63 applies with
\(M=M_\eta\). \(\square\)

### Lemma 16.65: Clustered palettes have a common cross-band exclusion

Keep the notation of Lemma 16.63, but let \(P\subset F\) be nonempty. For
each \(f\in P\), let
\[
U_f\subset I\cap C
\]
satisfy
\[
f+u\notin2C\qquad(u\in U_f). \tag{1}
\]
Put
\[
f_-=\min P,\qquad f_+=\max P,\qquad s=f_+-f_-.
\]
Then
\[
\bigcup_{f\in P}U_f
\]
is disjoint from the common band
\[
K_P=[2\alpha-f_-,\ 2\beta-f_+]\cap\mathbb N. \tag{2}
\]
Here \(K_P\) is interpreted as empty if its left endpoint exceeds its right
endpoint.
Consequently
\[
\left|\bigcup_{f\in P}U_f\right|
\le n-|I\cap K_P|. \tag{3}
\]
If \(1\le M\le\min\{n,2\ell-1-s\}\) and
\[
\left|\bigcup_{f\in P}U_f\right|>n-M, \tag{4}
\]
then
\[
f_-<2\alpha-b+M-1
\quad\text{or}\quad
f_+>2\beta-a-M+1. \tag{5}
\]

Proof. For each \(f\in P\), Lemma 16.50 gives
\[
U_f\cap[2\alpha-f,\ 2\beta-f]=\varnothing. \tag{6}
\]
Since \(f_-\le f\le f_+\), the common band \(K_P\) is contained in every
interval in (6). Hence each \(U_f\), and therefore their union, is disjoint
from \(K_P\). This proves (2) and (3).

Now assume \(M\le\min\{n,2\ell-1-s\}\) and (4). By (3),
\[
|I\cap K_P|<M. \tag{7}
\]
The band \(K_P\) has length
\[
2\ell-1-s\ge M.
\]
Write \(K_P=[L,R]\). If neither inequality in (5) holds, then
\[
L=2\alpha-f_-\le b-M+1,
\qquad
R=2\beta-f_+\ge a+M-1.
\]
The same interval-geometry argument used in Lemma 16.63 gives
\[
|I\cap K_P|\ge M,
\]
contradicting (7). Thus (5) holds. \(\square\)

### Corollary 16.66: Dense cross-block palette packets need spread or an extreme gate

Keep the setting of Lemma 16.65, and let \(0<\eta\le1\). Put
\[
M_\eta=\lfloor(1-\eta)n\rfloor+1.
\]
If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{1}
\]
then at least one of the following holds:
\[
s>2\ell-1-M_\eta, \tag{2}
\]
\[
f_-<2\alpha-b+M_\eta-1, \tag{3}
\]
or
\[
f_+>2\beta-a-M_\eta+1. \tag{4}
\]

Proof. If (2) fails, then
\[
M_\eta\le2\ell-1-s.
\]
Also \(M_\eta\le n\). Since \(n-M_\eta<\eta n\), (1) gives
\[
\left|\bigcup_{f\in P}U_f\right|>n-M_\eta.
\]
Lemma 16.65 with \(M=M_\eta\) yields (3) or (4). \(\square\)

### Corollary 16.67: Blocker windows localize dense far-gate packets

Let \(A\subseteq\mathbb N\), let \(F\subset A\) be finite, and put
\[
C=A\setminus F.
\]
Let
\[
I=[a,b]\cap\mathbb N
\]
have length \(n\). Fix \(0<\eta\le1\), and put
\[
M_\eta=\lfloor(1-\eta)n\rfloor+1.
\]
Let \(\mathcal J\) be a finite family of retained intervals
\[
J=[\alpha_J,\beta_J]\cap\mathbb N\subset C
\]
with lengths
\[
\ell_J=\beta_J-\alpha_J+1
\]
satisfying
\[
M_\eta\le2\ell_J-1. \tag{1}
\]
For each \(J\in\mathcal J\), define its blocker window
\[
W_J(\eta,I)
=
[2\alpha_J-b+M_\eta-1,\ 2\beta_J-a-M_\eta+1]\cap\mathbb N. \tag{2}
\]

If \(f\in F\) and \(U\subset I\cap C\) satisfy
\[
f+u\notin2C\qquad(u\in U),\qquad |U|\ge\eta n, \tag{3}
\]
then
\[
f\notin \bigcup_{J\in\mathcal J}W_J(\eta,I). \tag{4}
\]
Equivalently, any prescribed candidate gate set
\[
G\subseteq\bigcup_{J\in\mathcal J}W_J(\eta,I)
\]
supports no \(\eta\)-dense gate-dependent packet over \(I\).

Moreover, let \(P\subset F\) be nonempty and let \(U_f\subset I\cap C\)
be gate-dependent packets for \(f\in P\). Put
\[
f_-=\min P,\qquad f_+=\max P,\qquad s=f_+-f_-.
\]
If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{5}
\]
then for every \(J\in\mathcal J\) at least one of the following holds:
\[
s>2\ell_J-1-M_\eta, \tag{6}
\]
\[
f_-<2\alpha_J-b+M_\eta-1, \tag{7}
\]
or
\[
f_+>2\beta_J-a-M_\eta+1. \tag{8}
\]
In particular, if for some \(J\in\mathcal J\) the whole palette lies in
\[
W_J(\eta,I)
\]
and
\[
s\le2\ell_J-1-M_\eta,
\]
then (5) is impossible.

Proof. The single-gate assertion is Corollary 16.64 applied to each
\[
J\in\mathcal J.
\]
Indeed, (3) forces \(f\) to lie outside the window (2) for every such
\(J\), proving (4).

For the palette assertion, apply Corollary 16.66 to each \(J\in\mathcal J\).
It gives precisely the alternatives (6), (7), and (8). If one blocker
window contains the whole palette and the span bound also holds, then
neither (7) nor (8) nor (6) can hold, contradicting the alternatives.
\(\square\)

### Corollary 16.68: Dense bounded palettes have a localized blocker escape

Keep the notation of Corollary 16.67. Let \(r\ge1\), let \(P\subset F\)
be nonempty with
\[
|P|\le r,
\]
and for each \(f\in P\) let \(U_f\subset I\cap C\) satisfy
\[
f+u\notin2C\qquad(u\in U_f). \tag{1}
\]
Fix \(0<\eta\le1\), put
\[
\delta={\eta\over r},
\qquad
M_\delta=\lfloor(1-\delta)n\rfloor+1,
\]
and suppose every retained interval \(J\in\mathcal J\) satisfies
\[
M_\delta\le2\ell_J-1. \tag{2}
\]
If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{3}
\]
then there is \(f\in P\) such that
\[
|U_f|\ge\delta n \tag{4}
\]
and
\[
f\notin\bigcup_{J\in\mathcal J}W_J(\delta,I), \tag{5}
\]
where
\[
W_J(\delta,I)
=
[2\alpha_J-b+M_\delta-1,\ 2\beta_J-a-M_\delta+1]\cap\mathbb N.
\]
Consequently, if
\[
P\subseteq\bigcup_{J\in\mathcal J}W_J(\delta,I), \tag{6}
\]
then (3) is impossible.

Proof. Since
\[
\sum_{f\in P}|U_f|\ge\left|\bigcup_{f\in P}U_f\right|\ge\eta n
\]
and \(|P|\le r\), some \(f\in P\) satisfies
\[
|U_f|\ge{\eta n\over r}=\delta n.
\]
Apply the single-gate part of Corollary 16.67 with density \(\delta\) to
this \(f\) and \(U_f\). Assumption (2) is exactly the retained-length
hypothesis for that density, and the conclusion is (5). If (6) held, this
same \(f\) would both lie in and outside the blocker union, a contradiction.
\(\square\)

Thus a far-gate packet cannot be dense in a tested interval while an old
retained interval has a doubled band deeply overlapping that test. Any
block construction that pays the linear far-gate cost from Corollary 16.61
must also place those gates outside the overlap windows generated by every
large retained interval in earlier or later blocks.

Corollary 16.66 is the palette version: a dense coordinated far-gate packet
against one retained interval must either spread its active colors across
almost the full doubled length of that interval or put one extreme active
color outside the corresponding overlap window.

Corollary 16.67 packages the usable obstruction for staged constructions:
each retained interval contributes a forbidden affine window for dense gate
packets over the tested block, and clustered finite palettes cannot hide
inside any one of those windows.
Corollary 16.68 removes the clustering assumption at the cost of the
expected \(1/r\) density loss: a dense bounded palette has one active color
that must escape all blocker windows at density \(\eta/r\).

### Lemma 16.69: Auxiliary intervals give robust blocker cores

Let \(A\subseteq\mathbb N\), let \(F\subset A\) satisfy \(|F|\le r\), and
put
\[
C=A\setminus F.
\]
Let
\[
I=[a,b]\cap\mathbb N
\]
have length \(n\), and let
\[
K=[c,d]\cap\mathbb N\subset A
\]
have length \(m=d-c+1\). Put
\[
\ell_0=\left\lceil {m-r\over r+1}\right\rceil. \tag{1}
\]
Fix \(0<\delta\le1\), and set
\[
M_\delta=\lfloor(1-\delta)n\rfloor+1. \tag{2}
\]
Assume
\[
1\le M_\delta\le2\ell_0-1. \tag{3}
\]
Define the robust blocker core of \(K\) against \(I\) at density \(\delta\)
and rank \(r\) by
\[
R_K(\delta,I;r)=
[\,2(d-\ell_0+1)-b+M_\delta-1,
  2(c+\ell_0-1)-a-M_\delta+1\,]\cap\mathbb N. \tag{4}
\]
If \(f\in F\) and \(U\subset I\cap C\) satisfy
\[
f+u\notin2C\qquad(u\in U),\qquad |U|\ge\delta n, \tag{5}
\]
then
\[
f\notin R_K(\delta,I;r). \tag{6}
\]

Proof. Apply Lemma 16.52 to the deletion \(F\cap K\) inside the interval
\(K\). Since \(|F\cap K|\le |F|\le r\), the set \(K\setminus F\) contains
a retained subinterval
\[
J=[\alpha,\beta]\cap\mathbb N\subset C
\]
of length \(\ell\ge\ell_0\). Since \(J\subset K\), we have
\[
c\le\alpha\le\beta\le d.
\]
The blocker window from Corollary 16.67 for this \(J\) and density
\(\delta\) is
\[
W_J(\delta,I)=
[2\alpha-b+M_\delta-1,\ 2\beta-a-M_\delta+1]\cap\mathbb N. \tag{7}
\]
Every length-\(\ell\) subinterval of \(K\) satisfies
\[
\alpha\le d-\ell+1\le d-\ell_0+1,\qquad
\beta\ge c+\ell-1\ge c+\ell_0-1.
\]
Therefore
\[
2\alpha-b+M_\delta-1
\le
2(d-\ell_0+1)-b+M_\delta-1,
\]
and
\[
2\beta-a-M_\delta+1
\ge
2(c+\ell_0-1)-a-M_\delta+1.
\]
Thus
\[
R_K(\delta,I;r)\subseteq W_J(\delta,I). \tag{8}
\]
Condition (3) gives \(M_\delta\le2\ell-1\), so Corollary 16.67 applied to
the single retained interval \(J\) says that a \(\delta\)-dense
gate-dependent packet cannot have \(f\in W_J(\delta,I)\). Inclusion (8)
proves (6). \(\square\)

### Corollary 16.70: Bounded palettes must escape robust blocker cores

Keep the setting of Lemma 16.69. Let \(P\subset F\) be nonempty with
\[
|P|\le r,
\]
and for each \(f\in P\) let \(U_f\subset I\cap C\) satisfy
\[
f+u\notin2C\qquad(u\in U_f). \tag{1}
\]
Fix \(0<\eta\le1\), put
\[
\delta={\eta\over r},
\qquad
M_\delta=\lfloor(1-\delta)n\rfloor+1,
\]
and suppose \(M_\delta\le2\ell_0-1\). If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{2}
\]
then some \(f\in P\) satisfies
\[
f\notin R_K(\delta,I;r). \tag{3}
\]
Consequently, if
\[
P\subseteq R_K(\delta,I;r),
\]
then (2) is impossible.

Proof. Pigeonhole as in Corollary 16.68: from (2) and \(|P|\le r\), some
\(f\in P\) has
\[
|U_f|\ge\delta n.
\]
Lemma 16.69 applied to this \(f\) and \(U_f\) gives (3). \(\square\)

### Lemma 16.71: Robust blocker core length

In the setting of Lemma 16.69, the interval \(R_K(\delta,I;r)\) has length
\[
\max\{0,\ n-2M_\delta+4\ell_0-2m\}. \tag{1}
\]
Equivalently, the robust blocker core is nonempty exactly when
\[
n-2M_\delta+4\ell_0-2m\ge1. \tag{2}
\]

Proof. The left and right endpoints in (4) of Lemma 16.69 are
\[
L=2(d-\ell_0+1)-b+M_\delta-1
\]
and
\[
R=2(c+\ell_0-1)-a-M_\delta+1.
\]
If \(R<L\), the intersection with \(\mathbb N\) is empty. Otherwise its
length is
\[
R-L+1.
\]
Using
\[
d=c+m-1,\qquad b=a+n-1,
\]
we compute
\[
R-L+1=n-2M_\delta+4\ell_0-2m.
\]
This proves (1), and (2) is the nonemptiness criterion. \(\square\)

Thus robust auxiliary blockers are strongest when the retained-run
guarantee \(\ell_0\) is a large fraction of the auxiliary interval length
and the required packet density is high enough that \(M_\delta\) is small.
For low-density packets or high deletion rank, the robust core may be empty;
then the proof must use more detailed information about the actual retained
run, not just the rank bound.

### Corollary 16.72: Short auxiliary intervals give linear robust cores

Fix \(r\ge1\) and \(1/2<\delta\le1\). In the setting of Lemma 16.69, there
is a constant \(C_r\), depending only on \(r\), with the following
properties.

If \(r=1\), then
\[
|R_K(\delta,I;1)|\ge (2\delta-1)n-C_1. \tag{1}
\]
If \(r\ge2\) and
\[
m\le { (2\delta-1)(r+1)\over4(r-1)}\,n, \tag{2}
\]
then
\[
|R_K(\delta,I;r)|\ge {2\delta-1\over2}\,n-C_r. \tag{3}
\]
Consequently, under either hypothesis, the robust blocker core is nonempty
for all sufficiently large \(n\).

Proof. By Lemma 16.71 and the estimates
\[
M_\delta\le(1-\delta)n+1,\qquad
\ell_0\ge {m-r\over r+1},
\]
we get
\[
|R_K(\delta,I;r)|
\ge
(2\delta-1)n-2-{4r\over r+1}
-{2(r-1)\over r+1}m, \tag{4}
\]
with the convention that the right side is a lower bound for the
nonnegative length.

For \(r=1\), the coefficient of \(m\) in (4) is zero, giving (1) with any
\[
C_1\ge4.
\]
For \(r\ge2\), condition (2) makes the \(m\)-term in (4) at most
\[
{2\delta-1\over2}\,n.
\]
Taking, for instance,
\[
C_r=2+{4r\over r+1}
\]
proves (3). \(\square\)

Thus fixed-rank dense far-gate packets cannot freely use earlier or later
intervals whose lengths are a sufficiently small fixed fraction of the
tested interval. Such an auxiliary block contributes a forbidden active-gate
interval of length linear in \(n\), independent of the exact deleted
positions inside that block.

### Corollary 16.73: Robust cores block bounded-rank interval packets

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Fix \(r\ge1\) and \(0<\eta\le1\).
Put
\[
B_r={r(r+1)\over2}+2r,\qquad \delta={\eta\over2r}. \tag{1}
\]
There is \(N=N(r,\eta)\) such that the following holds whenever
\[
I=[a,b]\cap\mathbb N\subset A
\]
has length \(n\ge N\).

Let \(F\subset A\) satisfy \(1\le|F|\le r\), let \(P\subset F\), and let
\[
K=[c,d]\cap\mathbb N\subset A
\]
have length \(m\). Define
\[
\ell_0=\left\lceil {m-r\over r+1}\right\rceil,
\qquad
M_\delta=\lfloor(1-\delta)n\rfloor+1,
\]
and assume
\[
M_\delta\le2\ell_0-1. \tag{2}
\]
Suppose also that
\[
P\subseteq R_K(\delta,I;r). \tag{3}
\]
For each \(f\in P\), let \(U_f\subset I\) satisfy the hypotheses of
Corollary 16.45 for the active color \(f\), with witness parameter
sufficiently large for the fixed interval \(I\) and rank bound \(r\). Then
\[
\left|\bigcup_{f\in P}U_f\right|<\eta n. \tag{4}
\]

Proof. Choose \(N\) so large that
\[
rB_r\le{\eta n\over2}\qquad(n\ge N). \tag{5}
\]
Assume, for contradiction, that
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n. \tag{6}
\]
For each \(f\), Corollary 16.45 leaves at most \(B_r\) rows outside the
gate-dependent packet
\[
U_{f,{\rm gate}}=\{u\in U_f:f+u\notin2(A\setminus F)\}.
\]
Therefore
\[
\left|\bigcup_{f\in P}U_{f,{\rm gate}}\right|
\ge
\eta n-|P|B_r
\ge{\eta n\over2}. \tag{7}
\]
Since \(|P|\le r\), one \(f\in P\) has
\[
|U_{f,{\rm gate}}|\ge{\eta n\over2r}=\delta n. \tag{8}
\]
Lemma 16.69, applied to \(U_{f,{\rm gate}}\), says
\[
f\notin R_K(\delta,I;r).
\]
This contradicts (3). \(\square\)

### Corollary 16.74: Actual blocker-window covers block bounded-rank packets

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Fix \(r\ge1\) and \(0<\eta\le1\).
Put
\[
B_r={r(r+1)\over2}+2r,\qquad \delta={\eta\over2r}. \tag{1}
\]
There is \(N=N(r,\eta)\) such that the following holds whenever
\[
I=[a,b]\cap\mathbb N\subset A
\]
has length \(n\ge N\).

Let \(F\subset A\) satisfy \(1\le|F|\le r\), put \(C=A\setminus F\), and
let \(P\subset F\). Let \(\mathcal J\) be a finite family of retained
intervals
\[
J=[\alpha_J,\beta_J]\cap\mathbb N\subset C
\]
whose lengths \(\ell_J\) satisfy
\[
M_\delta=\lfloor(1-\delta)n\rfloor+1\le2\ell_J-1. \tag{2}
\]
For each \(J\), let
\[
W_J(\delta,I)
=
[2\alpha_J-b+M_\delta-1,\ 2\beta_J-a-M_\delta+1]\cap\mathbb N.
\]
Assume
\[
P\subseteq\bigcup_{J\in\mathcal J}W_J(\delta,I). \tag{3}
\]
For each \(f\in P\), let \(U_f\subset I\) satisfy the hypotheses of
Corollary 16.45 for the active color \(f\), with witness parameter
sufficiently large for the fixed interval \(I\) and rank bound \(r\). Then
\[
\left|\bigcup_{f\in P}U_f\right|<\eta n. \tag{4}
\]

Proof. Choose \(N\) so large that
\[
rB_r\le{\eta n\over2}\qquad(n\ge N).
\]
If (4) failed, then as in the proof of Corollary 16.73 the union of the
gate-dependent subpackets
\[
U_{f,{\rm gate}}=\{u\in U_f:f+u\notin2(A\setminus F)\}
\]
would have size at least \(\eta n/2\). Hence one \(f\in P\) would satisfy
\[
|U_{f,{\rm gate}}|\ge{\eta n\over2r}=\delta n. \tag{5}
\]
Corollary 16.67, applied at density \(\delta\), says that this \(f\) cannot
belong to
\[
\bigcup_{J\in\mathcal J}W_J(\delta,I),
\]
contradicting (3). \(\square\)

### Corollary 16.75: Majority-color packets avoid robust cores

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Fix \(r\ge1\) and
\[
{1\over2}<\theta\le1.
\]
Put
\[
\delta={\theta+1/2\over2}. \tag{1}
\]
There is \(N=N(r,\theta)\) such that the following holds whenever
\[
I=[a,b]\cap\mathbb N\subset A
\]
has length \(n\ge N\).

Let \(F\subset A\) satisfy \(1\le|F|\le r\), let \(f\in F\), and let
\[
K=[c,d]\cap\mathbb N\subset A
\]
have length \(m\). Define
\[
\ell_0=\left\lceil {m-r\over r+1}\right\rceil,
\qquad
M_\delta=\lfloor(1-\delta)n\rfloor+1,
\]
and assume
\[
M_\delta\le2\ell_0-1. \tag{2}
\]
If \(U\subset I\) satisfies the hypotheses of Corollary 16.45 for the
active color \(f\), with witness parameter sufficiently large for the fixed
interval \(I\) and rank bound \(r\), and
\[
|U|\ge\theta n, \tag{3}
\]
then
\[
f\notin R_K(\delta,I;r). \tag{4}
\]

Proof. Let
\[
B_r={r(r+1)\over2}+2r.
\]
Choose \(N\) so large that
\[
B_r\le(\theta-\delta)n\qquad(n\ge N). \tag{5}
\]
By Corollary 16.45, all but at most \(B_r\) rows of \(U\) lie in the
gate-dependent packet
\[
U_{\rm gate}=\{u\in U:f+u\notin2(A\setminus F)\}.
\]
Using (3) and (5),
\[
|U_{\rm gate}|\ge |U|-B_r\ge\delta n.
\]
Lemma 16.69 applied to \(U_{\rm gate}\) gives (4). \(\square\)

Combining this with Corollary 16.72, a fixed-rank single-color packet of
density \(>1/2\) cannot keep its active color inside the linear robust core
created by any sufficiently short auxiliary interval. The remaining
bounded-rank interval obstruction must either split its density among many
colors, keep every color below majority density, or place a majority color
outside all such robust cores.

### Lemma 16.76: No-majority dense palettes have two sizeable colors

Let \(I\) be a finite set with \(|I|=n\), let \(P\) be a finite index set
with
\[
2\le |P|\le r,
\]
and let
\[
U_f\subset I\qquad(f\in P).
\]
Fix \(0<\theta<\eta\le1\). If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n \tag{1}
\]
and
\[
|U_f|<\theta n\qquad(f\in P), \tag{2}
\]
then there are distinct \(f,g\in P\) such that
\[
|U_f|\ge{\eta n\over r},\qquad
|U_g|\ge{(\eta-\theta)n\over r-1}. \tag{3}
\]

Proof. Choose \(f\in P\) with \(|U_f|\) maximal. Since
\[
\sum_{h\in P}|U_h|\ge\left|\bigcup_{h\in P}U_h\right|\ge\eta n,
\]
we have
\[
|U_f|\ge{\eta n\over |P|}\ge{\eta n\over r}. \tag{4}
\]
By (2),
\[
\sum_{h\in P\setminus\{f\}}|U_h|
\ge \eta n-|U_f|
> \eta n-\theta n=(\eta-\theta)n.
\]
Hence some \(g\ne f\) satisfies
\[
|U_g|\ge {(\eta-\theta)n\over |P|-1}
\ge {(\eta-\theta)n\over r-1}.
\]
Together with (4), this proves (3). \(\square\)

### Corollary 16.77: No-majority bounded-rank packets give two gate fibers

Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. Fix \(r\ge2\) and
\[
0<\theta<\eta\le1.
\]
There is \(N=N(r,\eta,\theta)\) such that the following holds whenever
\[
I=[a,b]\cap\mathbb N\subset A
\]
has length \(n\ge N\).

Let \(F\subset A\) satisfy \(1\le|F|\le r\), let \(P\subset F\) have
\[
2\le |P|\le r,
\]
and for each \(f\in P\) let \(U_f\subset I\) satisfy the hypotheses of
Corollary 16.45 for the active color \(f\), with witness parameter
sufficiently large for the fixed interval \(I\) and rank bound \(r\).
Assume
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n \tag{1}
\]
and
\[
|U_f|<\theta n\qquad(f\in P). \tag{2}
\]
Then there are distinct \(f,g\in P\) such that their gate-dependent
subpackets
\[
U_{h,{\rm gate}}=\{u\in U_h:h+u\notin2(A\setminus F)\}\qquad(h\in P)
\]
satisfy
\[
|U_{f,{\rm gate}}|\ge{\eta n\over2r},\qquad
|U_{g,{\rm gate}}|\ge{(\eta-\theta)n\over2(r-1)}. \tag{3}
\]

Proof. Let
\[
B_r={r(r+1)\over2}+2r.
\]
Choose \(N\) so large that for \(n\ge N\),
\[
B_r\le{\eta n\over2r}
\quad\text{and}\quad
B_r\le{(\eta-\theta)n\over2(r-1)}. \tag{4}
\]
Lemma 16.76 gives distinct \(f,g\in P\) with
\[
|U_f|\ge{\eta n\over r},\qquad
|U_g|\ge{(\eta-\theta)n\over r-1}. \tag{5}
\]
Corollary 16.45 leaves at most \(B_r\) rows of each \(U_h\) outside the
corresponding gate-dependent subpacket. Combining this with (4) and (5)
gives (3). \(\square\)

The finite script `EXPERIMENTS/density_split_check.py` checks Lemma 16.76
on small universes by enumerating subset families.

### Corollary 16.78: No-majority interval packets force two far gates

Keep the setting and hypotheses of Corollary 16.77. Then, after increasing
\(N=N(r,\eta,\theta)\) if necessary, there are distinct \(f,g\in P\) such
that
\[
D_I(f;r)\ge{\eta n\over4r},\qquad
D_I(g;r)\ge{(\eta-\theta)n\over4(r-1)}, \tag{1}
\]
where
\[
D_I(h;r)=\max\{0,\ a+2r-h,\ h-b+2r\}.
\]
In particular, for all sufficiently large \(n\), the same two colors
satisfy
\[
f<a-{\eta n\over8r}
\quad\text{or}\quad
f>b+{\eta n\over8r}, \tag{2}
\]
and
\[
g<a-{(\eta-\theta)n\over8(r-1)}
\quad\text{or}\quad
g>b+{(\eta-\theta)n\over8(r-1)}. \tag{3}
\]

Proof. Corollary 16.77 gives distinct \(f,g\) with
\[
|U_{f,{\rm gate}}|\ge{\eta n\over2r},\qquad
|U_{g,{\rm gate}}|\ge{(\eta-\theta)n\over2(r-1)}.
\]
Corollary 16.56, equivalently the no-row-allowance case used in Lemma
16.60, gives
\[
|U_{h,{\rm gate}}|\le2D_I(h;r)
\]
for each active color \(h\). This proves (1).

If \(D_I(f;r)\ge \eta n/(4r)\), then either
\[
a+2r-f\ge{\eta n\over4r}
\]
or
\[
f-b+2r\ge{\eta n\over4r}.
\]
Increasing \(N\) so that \(2r\le\eta n/(8r)\) gives (2). The proof of (3)
is identical, increasing \(N\) further so that
\[
2r\le {(\eta-\theta)n\over8(r-1)}.
\]
\(\square\)

Thus the no-majority bounded-rank interval branch is not just a diffuse
many-color escape. It must produce at least two active colors at linear
distance from the tested interval, each carrying a positive-density
finite-palette gate shadow.

### Corollary 16.79: Dense bounded-rank interval packets have a two-way normal form

Fix \(r\ge2\) and \(1/2<\eta\le1\), and put
\[
\theta={\eta+1/2\over2},\qquad
\delta={\theta+1/2\over2}. \tag{1}
\]
Let \(A\subseteq\mathbb N\) be an order-\(3\) basis for which no infinite
deletion leaves an order-\(4\) basis. There is \(N=N(r,\eta)\) such that
the following holds whenever
\[
I=[a,b]\cap\mathbb N\subset A
\]
has length \(n\ge N\).

Let \(F\subset A\) satisfy \(1\le|F|\le r\), let \(P\subset F\) be nonempty,
and let
\[
K=[c,d]\cap\mathbb N\subset A
\]
be an auxiliary interval. Define
\[
\ell_0=\left\lceil {m-r\over r+1}\right\rceil,\qquad m=d-c+1,
\]
and
\[
M_\delta=\lfloor(1-\delta)n\rfloor+1.
\]
Assume
\[
M_\delta\le2\ell_0-1. \tag{2}
\]
For each \(f\in P\), let \(U_f\subset I\) satisfy the hypotheses of
Corollary 16.45 for the active color \(f\), with witness parameter
sufficiently large for the fixed interval \(I\) and rank bound \(r\). If
\[
\left|\bigcup_{f\in P}U_f\right|\ge\eta n, \tag{3}
\]
then at least one of the following alternatives holds.

1. There is \(f\in P\) such that
\[
|U_f|\ge\theta n
\quad\text{and}\quad
f\notin R_K(\delta,I;r). \tag{4}
\]
2. There are distinct \(f,g\in P\) such that
\[
D_I(f;r)\ge{\eta n\over4r},\qquad
D_I(g;r)\ge{(\eta-\theta)n\over4(r-1)}. \tag{5}
\]

In particular, in the second alternative both active colors are a linear
distance outside the tested interval, as quantified in Corollary 16.78.

Proof. If some \(f\in P\) satisfies \(|U_f|\ge\theta n\), Corollary 16.75
gives
\[
f\notin R_K(\delta,I;r),
\]
after increasing \(N\) to meet its threshold. This is alternative 1.

Otherwise \(|U_f|<\theta n\) for all \(f\in P\). Since \(\theta<\eta\),
condition (3) forces \(|P|\ge2\). Corollary 16.78, again after increasing
\(N\), gives alternative 2. \(\square\)

The script `EXPERIMENTS/cross_interval_band_profile.py` checks the
interval-overlap inequality behind Lemma 16.63 on separated, nested, and
translated finite interval pairs, and also checks the common-band palette
geometry from Lemma 16.65.
The script `EXPERIMENTS/blocker_window_diagnostic.py` checks the finite
blocker-window package, including the robust-core formula in Lemma 16.69
against all deletions up to a prescribed rank in small auxiliary intervals.

The bounded-rank nonsingleton interval obstruction is now forced into a
long-range regime. Positive-density row packets over an interval cannot be
served by a finite active palette near that interval: after the bounded
row-dependent allowance is removed, the central retained two-sum band pushes
at least one active gate a linear distance outside the block, and a
coordinated finite palette must pay a linear total gate-distance cost. The
remaining escape must therefore either make the packet density vanish, let
the deletion rank grow with the interval, or coordinate genuinely far gates
across separated blocks.

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
Proposition 11.1 and Corollary 11.1a give the cofinite-lattice version of
the same warning: if the non-accelerator component is cofinite in a lattice,
then any finite accelerator that makes the set an order-\(k\) basis still
admits a sparse deletion leaving an order-\((k+1)\) basis. Thus any
finite-accelerator counterexample must use a genuinely sparse component
with shifted witnesses robust against all accelerator sums.

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
* Warning 8.5a.1b shows that even the active-last reduction from Lemma
  3.1c.2 does not give pure section descent: a second-element front can
  carry pair active traces \(\{x_2,\max S\}\) while all filler rows are
  last-gated at unbounded depth.
* Lemma 8.5a.2p extends the section operation to prefix-fronts, which is
  the actual object produced by Lemma 3.1c.1; no inclusion-antichain
  property is needed for recursive prefix analysis.
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
* Corollary 8.5a.5 rules out the pure terminal-color version of the
  last-gated escape: if the moving last endpoint reflects every protected
  finite test with unbounded centers, Theorem 2.3 gives a good deletion.
* Lemma 8.5a.6 generalizes the compactness obstruction: any fixed finite
  palette of moving labels with unbounded reflection centers and
  certificate-free fibers gives finitely many recurrent Sidon colors,
  impossible by Lemma 8.6g''''.2.
* Warning 8.5a.7 records the remaining mobile-injective escape: protected
  test points may be assigned to distinct moving active endpoints, so no
  finite palette or pure terminal recurrence appears.
* Example 8.5a.7b shows this escape is locally arithmetic, not merely
  formal: parity interval blocks have inclusion-minimal odd holes and a
  perfect matching from retained even rows to distinct deleted odd colors.
* Warning 8.5a.7c separates mobile-injective matchings from the
  enumerated-Schreier route: range-separated private packets can be
  inclusion-minimal and anti-hereditary, with no complete prefix-link
  shadow unless used colors are promoted to future barrier vertices. The
  parity interval blocks strengthen this separation: for ranks at least
  four they have collective mobile-injective holes but no possible first
  Schreier pair-link vertex.
* Warning 8.5a.7d adds the block-selector obstruction: independent
  mobile-injective packets are not a barrier, since an infinite selector can
  take one vertex from each packet and contain no whole non-singleton edge.
* Lemma 8.5a.7e adds a density-capacity obstruction: for any fixed fiber
  bound \(L\), a sparse deletion can avoid every late mobile packet whose
  rank-\(r\) private coloring serves at most \(L\) rows per active color.
  Thus a genuine counterexample must force unbounded private-color fibers
  or \(F+F\)-exception mass at ambient scale.
* Lemma 8.5a.7e' strengthens this to arbitrary rank-controlled bounds
  \(\Phi(|F|)\), so sparse deletion also avoids packets whose color fibers
  are only polynomial, exponential, or otherwise prescribed functions of
  the deleted rank.
* Corollary 8.5a.7f turns this into a positive structural demand:
  remaining counterexamples have arbitrarily large private reflected
  fibers \(U\) for a single active color, with \(m-U\subset A\) and
  \(U+f\) still excluded from \(2(A\setminus F)\).
* Corollary 8.5a.7f.1 splits those fibers into two rank-free branches:
  after passing to a large subfiber, either \(u+f\) has unique full
  representation for every row, or all rows have the same retained shifted
  overlap \(U+f-g\subset A\setminus F\) with another deleted color \(g\).
* Lemma 8.5a.7i shows that certificate-free retained shifted-overlap
  fibers are independent for their own shift. Hence a fixed-shift reflected
  fiber that is too large inside a finite \(h\)-linked test set gives a
  recurrent certificate triple and a good deletion.
* Lemma 8.5a.7j gives the analogous independence graph for unique-gate
  fibers: if \(r_{2,A}(u+f)=1\) on \(U\), then no two distinct rows satisfy
  \(u+f-v\in A\). Thus unique-gate fibers are independent in the
  gate-difference graph.
* Corollaries 8.5a.7k--8.5a.7l package the finite-palette consequence:
  recurring reflected fibers using only fixed finite gate or shift palettes
  either stay inside the corresponding certificate-free independence
  numbers, or produce a recurrent certificate triple and hence a good
  deletion.
* Example 8.5a.7g shows that these large fibers are locally compatible:
  a range-separated two-color packet can make one active color carry an
  arbitrarily large certificate-free private fiber.
* Example 8.5a.7m shows the same for the unique-gate branch: by moving the
  gate into a fresh range, a large private fiber can have
  \(r_{2,A}(u+f)=1\) for every row and still be certificate-free.
* Corollary 8.5a.7n records the counterexample consequence: over any fixed
  finite test and finite gate or shift palette, oversized unique-gate or
  shifted-overlap fibers can occur only at bounded reflection centers.
* Corollary 8.5a.7o strengthens the moving-palette conclusion: when
  extracting the forced large fiber, the deleted edge can be chosen outside
  any prescribed finite gate palette and with its pairwise deleted-color
  differences avoiding any prescribed finite shift palette.
* Corollary 8.5a.7p adds row-core avoidance: after increasing the requested
  fiber size by a finite amount, the retained fiber \(U\) may also be chosen
  outside any prescribed finite set of old rows.
* Corollary 8.5a.7q adds mirror-core avoidance: the retained mirror set
  \(m-U\) can simultaneously be kept outside any prescribed finite old
  mirror core.
* Corollary 8.5a.7r records the promoted-edge debt: after building disjoint
  fresh private packets, every infinite selector choosing one deleted color
  from each packet contains arbitrarily late bad edges spanning multiple
  packets.
* Corollary 8.5a.7s projects this debt to packet indices: the supports of
  realized cross-packet bad edges form a non-singleton weak barrier for each
  witness threshold, while the actual color edges form a stronger
  product-selector barrier.
* Corollary 8.5a.7t adds a compactness consequence: inside every infinite
  packet tail and for every witness threshold, some finite packet window is
  already completely product-covered by realized cross-packet bad edges.
* Lemma 8.5a.7u adds the finite selector-cylinder count: a complete product
  cover has total weight at least \(1\), so avoiding supports below rank
  \(q\) in packets of size at least \(m\) requires at least \(m^q\) realized
  bad edges in the same finite window.
* Corollary 8.5a.7v rules out the pair-cylinder subcase: if bad pairs alone
  product-covered every fresh-packet selector tail, the existing pair
  barrier/list-color machinery would give a good deletion.
* Corollary 8.5a.7w records the resulting cofinal high-rank debt: for
  arbitrarily large thresholds there is a pair-avoiding selector that still
  contains a promoted bad edge, hence one of rank at least \(3\).
* Corollary 8.5a.7x strengthens this on a pair-free selector tail: bounded
  second-excess high-rank barriers would invoke Lemma 8.6a, so the forced
  rank-\(\ge3\) edge can be taken with arbitrarily large excess over its
  second-smallest deleted color.
* Corollary 8.5a.7y shrinks the forced large-spread edge
  inclusion-minimally and imports the terminal-gap, shifted vertex-cover,
  and active-repair normal forms from Lemmas 10.1 and 10.3b.
* Example 8.5a.7z gives a finite full product-window model of the final
  local shape: three two-point packets whose eight selector triples all
  have inclusion-minimal terminal-gap witnesses, while all singleton and
  pair deletions are harmless on the same window.
* Warning 8.5a.7z.1 notes that disjoint repetitions of such rank-three
  windows do not form a weak barrier: an infinite packet set can keep at
  most two indices from each window and avoid all rank-\(\ge3\) supports.
* Diagnostic 8.5a.7z.2 records a bounded failed extension search: no fourth
  two-point packet with up to two fillers through \(30\) extends the small
  rank-three product terminal window while preserving all three-packet
  product requirements and pair-harmlessness.
* Lemma 8.5a.7z.3 proves that a single witness cannot cover a whole
  three-packet selector cube in the presence of many retained outside
  padders: all shifted two-sums \(v-e\) must collapse to the three full
  packet-pair sums.
* Lemma 8.5a.7z.4 generalizes this: if one witness is shared by a selector
  family, every shifted two-sum support for an outside retained padder must
  be a two-transversal of that selector family.
* Lemma 8.5a.7z.5 handles shared witness classes with common deleted
  points: outside padders either use non-common two-transversal sums or
  force shifted two-sum spikes at a common color.
* Corollary 8.5a.7z.6 turns this into a prefix-capacity inequality for
  shared witness classes, while Warning 8.5a.7z.7 records that the
  transversal constraints alone cannot produce an escaping selector against
  fully selector-specific rank-three fronts.
* Target 8.5a.7z.8 isolates that last route: a counterexample must stage a
  selector-specific reflected front whose old padders are either \(F+F\)
  exceptions or are assigned to moving deleted gates and retained mirrors
  without creating recurrent finite palettes, pair cylinders, or stable
  shifted spikes.
* Diagnostic 8.5a.7z.9 shows that the seed terminal product cover is not
  yet such a retained-mirror front: strict retained-mirror requirements
  leave only a few selector triples.
* Lemma 8.5a.7z.10 compresses large retained-mirror row sets into
  lower-rank spike supports: either one gate has many unique rows, or a
  fixed pair of gates has many shifted-overlap rows. The unresolved
  promotion is from those spike supports to recurrent certificates or
  genuine late-bad pair debt.
* Diagnostic 8.5a.7z.11 verifies on the seed window that this compression
  does not imply same-witness singleton or pair holes; the pair-promotion
  scan also confirms that strict shifted-overlap branches are repaired by
  the remaining active selector color and have no nearby pair holes.
* Diagnostic 8.5a.7z.12 gives a range-separated finite gadget where a
  shifted-overlap pair spike is repaired by a third active color, so local
  spike support does not imply pair debt.
* Example 8.5a.7z.12a makes that obstruction arbitrary-size: terminal
  rank-three holes can carry shifted-overlap spikes of any finite size
  while all pair deletions inside the active triple remain harmless at the
  same witness.
* Diagnostic 8.5a.7z.12b shows that the most direct coverage filler,
  adjoining a retained low interval, repairs the protected witness exactly
  when its two-sum interval reaches a private spike sum.
* Diagnostic 8.5a.7z.12c shows that the initial coverage gap can still be
  bridged locally by safe retained bands; the unresolved burden is pushing
  coverage past the witness while keeping every shifted terminal target
  gated by deleted colors.
* Corollary 8.5a.7z.12d records the resulting formal pressure: any large
  retained filler block below a frozen witness feeds directly into the
  compressed-spike dichotomy of Lemma 8.5a.7z.10.
* Lemma 8.5a.7z.12e and Diagnostic 8.5a.7z.12f isolate the next local
  obstruction: one-point retained fillers that would cover the next gap
  may all lie in \(w-2C\), so each would repair the protected witness; in
  the tested scaled profiles even two-point batches do not cover the stalled
  gap safely, which by Lemma 8.5a.7z.12e' blocks every finite batch at that
  final state.
* Lemma 8.5a.7z.12e'' packages the exact reflected blocker certificate:
  if \(d=w-p\in C\) and \(d+a\in2C\) for every old summand \(a\) that would
  make a one-new representation of the gap, then no finite retained batch
  can cover that gap safely.
* Corollaries 8.5a.7z.12e''' and 8.5a.7z.12g sharpen the reflected wall:
  once \(d\) is retained, only the deleted gates need separate reflection
  checks, but at fixed deleted rank a whole retained-defect wall has size
  at most \(|F+F|\).
* Corollary 8.5a.7z.12g.1 isolates the moving-packet escape: a retained
  defect \(d=w-p\) can be covered through a deleted gate \(p=f+c\) only if
  \(d+f\notin2C\), so every such escape needs private gate incidences.
* Lemma 8.5a.7z.12h records the broader one-sided saturation wall seen in
  nearby seed profiles, where \(d\) need not be retained but every one-new
  repair and one side of every two-new split already hits \(w\) with a
  retained pair.
* Lemma 8.5a.7z.12h.1 rewrites the one-point part exactly as external
  translate absorption \(d+T\subseteq2C\) for the old summand rows whose
  candidates \(p-a\) are outside the current set.
* Corollary 8.5a.7z.12h.2 gives the complementary escape-set form: a safe
  two-point repair requires a complementary pair inside
  \(\{z\notin A:d+z\notin2C\}\), and a safe old-summand repair requires an
  old row \(a\) with \(d+a\notin2C\).
* Warning 8.5a.7z.12h.3 records that large escape sets alone are harmless:
  they may lie almost entirely above \(p/2\), with the few low escapes
  having complements already in \(A\) or absorbed by \(2C\).
* Warning 8.5a.7z.12h.4 shows that even initial interval coverage and a
  genuine inclusion-minimal terminal hole do not balance the escape set:
  a two-interval model has \(E=\{L+1,\ldots,2L\}\) and no complementary
  pair for \(p=2L+1\).
* Warning 8.5a.7z.12h.4a tunes that model so the retained complements of the
  shadows form a large block but almost all future targets \(w-x\) are still
  old full two-sum gaps. Promoting a shadow as retained repairs the witness,
  so the cartridge creates deleted-packet debt rather than a selector
  barrier.
* Lemma 8.5a.7z.12h.5 records the future-defect debt of safe fillers:
  once a retained filler \(x\) has \(x+F\subset2C\), the later gap
  \(w-x\) is a reflected finite-batch wall unless the active packet or
  witness changes first.
* Lemma 8.5a.7z.12h.6 gives the complementary survival route: if many
  retained fillers are to survive until their future defects under the same
  witness and packet, they must form large private-gate fibers
  \(w-x-f\in C,\ x+f\notin2C\), feeding back into Lemma 8.5a.7z.10.
* Corollary 8.5a.7z.12h.7 packages the resulting trichotomy for a retained
  filler \(x\): either \(w-x\) is still an old full two-sum gap, or \(x\)
  belongs to a private-gate fiber, or, when all gates are absorbed, the
  future target \(w-x\) is a reflected wall.
* Corollary 8.5a.7z.12h.8 aggregates this over finite filler tests:
  under one frozen witness and deleted packet, either many future targets
  \(w-x\) remain old full two-sum gaps, or one gate supports a private
  fiber of size comparable to the test size.
* Corollary 8.5a.7z.12h.9 combines that fixed-witness runway dichotomy with
  Lemma 8.5a.7z.10: once the covered part of the runway exceeds
  \(|F|(|F|M+|F+F|)\), it contains an \(M\)-row unique-gate spike or
  shifted-overlap spike.
* Target 8.5a.7z.12i isolates the new local-to-global gap: one-sided
  shadows may live on nonretained filler candidates \(x\notin A\), so the
  retained-row bounds do not yet force compressed spikes or pair debt.
* Corollary 8.5a.7z.13 closes the stable compressed-spike case by invoking
  the existing finite gate- and shift-palette certificate lemmas.
* Target 8.5a.7z.14 is the resulting live normal form: any counterexample
  must stage a cross-window selector front of moving compressed spikes,
  with no pair promotion, no stable finite palettes, and enough coverage
  fillers to avoid the two-sum gaps in the local no-promotion gadgets.
  Corollary 8.5a.7z.12h.8 now adds that those fillers cannot form long
  fixed-witness runways: such a runway either leaves old two-sum gaps or
  creates a large private-gate fiber.
* Lemma 8.5a.8a isolates the abstract front recursion: an unbounded
  obstruction statistic either descends to a one-point section or becomes a
  first-coordinate shell with finite section bounds diverging along the
  first coordinate.
* Lemma 8.5a.8b turns bounded first-coordinate section barriers into
  generalized complete prefix-link shells: after thinning, each first point
  \(a_i\) links to every sufficiently late \(r_i\)-subset of the remaining
  tail, for some finite moving rank \(r_i\).
* Target 8.5a.7h identifies the current live obstruction: large private
  fibers in the gate-independent unique branch or shift-independent
  shifted-overlap branch must escape every fixed finite palette cofinally,
  every fixed certificate-rich test set, every finite row or mirror core,
  or every unbounded recurrent center set while still creating arbitrarily
  late finite product covers of promoted cross-packet edges.
* Target 8.5a.8 isolates the trace-section dichotomy needed to finish the
  recursive front strategy: either the mobile active-color obstruction
  descends to a proper section, or it is first-coordinate Schreier-coded and
  must be handled by the Section 13 shell analysis.
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
* Proposition 11.1 extends this to finite accelerators over a cofinite
  lattice component whenever every residue has a \((k+1)\)-term residue
  representation using at least two lattice summands.
* Corollary 11.1a observes that this residue condition is automatic if the
  finite accelerator over the cofinite lattice component is already an
  order-\(k\) basis.
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
* Corollary 13.1l.2a extends the endpoint-list obstruction from pairs to
  fixed finite ranks under a high-center hypothesis: a fixed first point
  cannot link to arbitrary \(r\)-subsets with witnesses far above every
  endpoint, since the lists either yield a recurrent certificate or a
  forbidden finite moving-label Sidon palette.
* Corollary 13.1l.2b records the exact negated quantifier: for each fixed
  first point, rank, and tail, some finite test set and constant force every
  sufficiently high linked hole to have bounded excess over one endpoint;
  in a generalized prefix-link shell, this endpoint is a moving tail point.
* Corollary 13.1l.2c specializes Lemma 8.2c''' to prefix shells: if that
  bounded endpoint debt sits at a fixed ordered tail position while the
  witness is arbitrarily far above all earlier endpoints, then the shell
  gives fractional reflection-recurrence, and certificate-dense finite
  tests already yield a good deletion.
* Corollary 13.1l.2d adds the Ramsey step for active fixed-rank links:
  bounded moving-endpoint debt stabilizes at one ordered position on an
  infinite tail, so full-rank inclusion-minimal prefix shells reduce to
  the fractional certificate-free branch or to smaller active traces.
* Corollary 13.1l.2e packages the fixed-section conclusion: a fixed first
  point and fixed rank with full inclusion-minimal packets cannot be a new
  shell obstruction; it yields fractional reflection-recurrence unless the
  active trace descends to a proper subpacket.
* Corollary 13.1l.2f closes the fixed-depth fractional alternative: the
  endpoint rows use only the finite palette of earlier labels, so they
  either force a recurrent certificate or violate Corollary 8.5a.4's
  finite moving-label obstruction.
* Corollary 13.1l.2f.1 extends this to variable total rank at fixed
  ordered depth: a surviving unbounded-rank fixed-first trace must push any
  endpoint-close debt to unbounded suffix depth.
* Lemma 13.1l.2g handles nonminimal fixed-rank prefix links: after Ramsey
  thinning the inclusion-minimal active trace has a fixed position pattern;
  if it contains the fixed first point it reblocks to a smaller full active
  prefix shell, and otherwise it is genuine tail-section descent.
* Lemma 13.1l.2h gives the abstract well-foundedness closure: if every
  section rules out its first-coordinate shell alternative, endless
  section descent contradicts the prefix-front property.
* Proposition 13.1l.2i states the conditional recursive \(k=2\) closure:
  once the private-color normal form is promoted section-locally to the
  shell/descent dichotomy, the fixed-rank shell results and well-foundedness
  rule out a counterexample.
* Corollary 13.1l.2j proves the bounded fixed-section part of that
  promotion principle: bounded active suffix rank keeping a fixed first
  point promotes to a forbidden full active fixed-rank shell.
* Target 13.1l.2k isolates the only remaining fixed-section escape:
  unbounded-rank inclusion-minimal traces that keep the fixed first point
  on every tail, without yet promoting to a bounded active subtrace or
  proper tail descent.
* Diagnostic 13.1l.2k.1 gives an arbitrary-rank finite model with fixed
  first point \(1\) and far suffix endpoints, proving that local
  inclusion-minimality alone cannot close Target 13.1l.2k; global
  order-\(2\) coverage or recurrence must be used.
* Diagnostic 13.1l.2k.2 strengthens this with a star-cut model whose
  retained test rows have singleton moving-label fibers, so finite-palette
  recurrence cannot be forced inside one hole.
* Corollary 13.1l.2k.3 records that such star cuts are selector-avoidable
  when placed independently in disjoint blocks; a counterexample needs
  cross-block promotion of labels into later active traces.
* Lemma 13.1l.2k.4 gives the fixed-prefix sparse-tail analogue of Lemma
  8.5a.7e': in a sparse suffix selector, every fixed-prefix trace must
  have a private-color fiber larger than any prescribed function of its
  suffix rank.
* Corollary 13.1l.2k.5 converts that counting pressure back into the
  large-private-fiber normal form: fixed-first unbounded-rank sections
  must produce arbitrarily large private reflected row sets for some active
  endpoint.
* Corollary 13.1l.2l proves the finite-prefix fixed-rank shell closure
  needed for cross-promoted star cuts: a finite fixed prefix plus bounded
  suffix rank still collapses to recurrent certificates or the finite
  moving-label obstruction.
* Corollary 13.1l.2m extracts the abstract consequence: every surviving
  finite-prefix section that keeps its prefix must have unbounded moving
  suffix rank on every tail.
* Diagnostic 13.1l.2m.1 identifies the remaining abstract shape with
  higher-front rank, exemplified by the second-element front; the final
  step must use additive structure beyond prefix-front combinatorics.
* Corollary 13.1l.2n closes the case where cross-promoted large fibers
  produce a genuine prefix-front of active suffix traces over a finite
  fixed prefix.
* Lemma 3.1c.4 and Corollary 13.1l.2o close the weak-to-front promotion
  gap for finite-prefix active suffixes: every weak barrier of actual
  traces thins to an actual prefix-front, and then bounded ranks fall to
  Corollary 13.1l.2m while unbounded ranks fall to Corollary 13.1l.2n.
* Theorem 13.1l.2p combines Corollary 8.3b with this weak-to-front closure
  to prove the \(k=2\) case: after singleton traces are removed, the first
  section of the actual active prefix-front is a forbidden finite-prefix
  weak active suffix barrier.
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
  packets can satisfy Lemma 8.4c row-by-row, even after folding current
  mirrors into the same certificate-free color fibers, but every mirror
  later promoted into the protected tail inherits new poisoned pair
  intervals from old retained endpoints.
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
* Lemma 16.0 and Lemma 16.0a rule out fixed finite-core one-marker lifts:
  if the tail is covered by \(M+rC\) with finite \(C\), then finite marker
  deletions are eventually repaired by two retained markers, and one can
  choose an infinite sparse marker deletion that remains an order-\(r+2\)
  basis.
* Diagnostic 16.1 records that the robust-booster pair-stage lift stalls at
  the third stage because singleton candidates \(41,43\) extend coverage but
  fail simultaneous pair witnesses against many old elements; the obstruction
  is domination, not coverage alone.
* Target 16.2 and Lemmas 16.3--16.6b isolate the current \(k=3\)
  moving-core target: after finite-core marker coverage is ruled out, every
  old-new pair witness must either be eventually repaired or force old-gate
  \(2A\)-shadow rows \(w-a-p\in2(A\setminus\{b\})\) across the interval
  where the new endpoint \(b\) is too large to participate; the finite
  prefilter rejects most robust-booster third-stage candidates by missing
  shadow rows, and after excluding singleton-new holes each new point needs
  linearly many distinct witnesses and reflected row load against the old
  stage.
* Diagnostic 16.7 shows the high-excess escape is locally compatible:
  \(\{1,2,3,4\}\) can add \(8\) with high-excess pair witnesses for all old
  endpoints and a two-point buffer, but the greedy singleton chain stalls
  after adding \(19\).
* Diagnostic 16.8 shows unrestricted \(k=3\) pair stages can reach depth
  four without the robust residue booster, but the first periodic-looking
  chain still has no bounded next stage.
* Lemma 16.9 gives the exact singleton-new normal form: singleton order-4
  holes force \(2A\)-valued reflected rows and a terminal gap, but those
  rows still use the deleted singleton and do not repair the hole.
* Lemma 16.10 proves that the interval-marker family
  \([1,L]\cup\{2L\}\) supplies strict singleton-high-excess first stages but
  cannot be iterated by one later marker, because the required next witness
  lies beyond a three-sum coverage gap.
* Lemma 16.11 shows what a multi-marker continuation would have to do:
  the next block must cover a long bridge interval by one new element plus
  two old interval-marker terms before singleton privacy is even tested.
* Diagnostic 16.12 gives a prepared one-marker moving row-bank example:
  fillers can bridge the coverage gap and support a high-excess singleton
  witness, but those fillers are not protected in the same stage.
* The prepared-marker follow-up search finds no bounded next-stage
  singleton protection for the row-bank fillers \(19,20,28\), reinforcing
  the coverage/privacy conflict for filler promotion.
* Lemma 16.13 explains the follow-up failure mode: retained padders shift
  three-sum coverage into whole intervals of repaired order-\(4\)
  candidates, so extending coverage can itself destroy singleton privacy.
* Lemma 16.14 records the exact singleton criterion \(w\notin4C\) iff
  every retained shift \(w-p\) is outside \(3C\); poisoning requires
  complement-side three-sum coverage and is not automatic from row banks.
* Lemma 16.15 sharpens the row-bank collision test: if \(q+p\in2C\), then
  privacy forces the row \(d-p\) to be \(q\)-dependent, giving a genuine
  one-term reflected row \(d-q-p\in A\).
* Lemma 16.16 shows that later high blocks cannot one-new promote an old
  unprotected filler: any adjacent private witness translates an old
  three-sum private hole for that filler.
* Lemma 16.17 splits singleton row banks into two half-density branches:
  actual one-term reflected rows in \(A\), or unique two-sum translates
  pinned by the deleted gate.
* Lemma 16.18 makes that split collision-complete: every retained padder
  is in at least one of the reflected-row or unique-gate alternatives,
  because otherwise the two retained two-sums repair the private witness.
* Lemma 16.19 shows that bounded secondary centers \(d-q\) force all
  sufficiently late tested rows into the unique-gate alternative; actual
  reflected-row recurrence requires \(d-q\) to move past the finite tests.
* Corollary 16.20 shows that unbounded reflected singleton rows over a
  finite test with no balanced certificate-free halfset give a fixed
  recurrent \(k=3\) certificate tuple and therefore a good order-\(4\)
  deletion.
* Corollary 16.21 turns this around inside a hypothetical \(k=3\)
  counterexample: over every finite balanced certificate test, large
  secondary-center singleton row banks must contain a unique-gate
  half-packet.
* Corollary 16.22 applies the unique-gate independence lemma to those
  half-packets: if \(U\) is the unique-gate set, then
  \((U+q-U)\cap A\subset\{q\}\). The remaining singleton escape is
  therefore moving \(q\)-independent arithmetic, or large
  balanced-certificate-free halfsets in every finite test.
* Example 16.23 shows that balanced certificate density alone does not
  rule out unique-gate packets: the interval-marker seed
  \([1,L]\cup\{2L\}\) has a full \(q\)-independent unique-gate packet on
  \([1,L]\). The obstruction to this local model is its failure to
  iterate, not a finite certificate contradiction.
* Lemma 16.24 packages the bounded-window consequence: if
  \(w=q+d\le W\) is a singleton private witness, then every active retained
  row above \(W-2q-\min A\) is forced into a \(q\)-independent unique-gate
  packet. In particular targets above \(W/2\) impose independence on their
  whole active retained range.
* Corollary 16.25 records the exact finite singleton witness-window
  criterion used by the diagnostics: the private candidates for \(q\) in
  an interval \(I\) are precisely
  \((I\cap4S)\setminus\bigcup_{p\in S\setminus\{q\}}(p+3(S\setminus\{q\}))\),
  with the high-excess inequality imposed afterward.
* Lemma 16.26 separates the one-gate and many-target cases: if many targets
  in one finite block are simultaneously gate-independent over the same
  active rows, then all unordered sums from pairs meeting those targets are
  distinct, giving the Sidon-scale bound
  \(t(m-t)+\binom t2\le2(\max P-\min P)+1\).
* Lemma 16.27 applies this to the interval-marker bridge from Lemma 16.11:
  once the smallest new marker \(x\) is beyond \(100L^2\), a bridge block
  covering \([x+3L+1,2x]\) cannot have a gate-independent half-packet over
  its own bridge rows. Any iterable singleton bridge must therefore be
  near-range, sparse-protected, or staggered-window.
* Corollary 16.28 records the abstract inequality: if an interval \(J\) of
  length \(R\) is covered by \(P+D\), and a half of \(P\) is simultaneously
  gate-independent over \(P\), then
  \(3R^2/(8|D|^2)-R/(4|D|)\le2(\max P-\min P)+1\).
* Corollary 16.29 connects this back to actual singleton witnesses: if
  half of a bridge block has private witnesses below one common bound and
  the other bridge elements are active late rows, then the same bridge
  inequality must hold. Violating it forces sparse protection or staggered
  witness windows.
* Diagnostic 16.30 records the first interval-marker bridge debt under the
  enhanced search: among all size-\(\le6\) candidate blocks through \(50\),
  the best size-\(6\) block protects only two elements, and only one lies
  in the common-row pressure range. The finite obstruction is immediate
  deferred filler protection, not lack of four-sum representation.
* Corollary 16.31 routes deferred fillers back into the global barrier
  structure: any infinite deferred set either has infinitely many singleton
  late-bad elements, so the singleton analysis recurs at later windows, or
  contains a nonsingleton late-bad prefix-front.
* Diagnostic 16.32 tests the first staggered repair of the interval-marker
  debt block and finds no bounded one-step singleton protection for the
  deferred fillers \(25,26,43,44\); the best next window is completely
  represented but completely poisoned.
* Corollary 16.33 shows that boundedly many staggered windows do not evade
  the same pressure: if a positive-density subset of one bridge block is
  protected using at most \(s\) common-row windows, then one window contains
  a fixed positive fraction and satisfies a Sidon-scale bridge inequality.
  Thus the singleton escape requires unboundedly many windows, vanishing
  per-window density, or a nonsingleton front.
* Corollary 16.34 specializes this to large interval-marker bridges:
  whenever \(x/L^2\to\infty\), every fixed finite family of staggered
  windows protects only a vanishing fraction of the bridge block. The only
  singleton escape left there is unbounded-window coding or a
  nonsingleton-front handoff.
* Corollary 16.35 upgrades that handoff: after deleting finitely many
  singleton late-bad points, the nonsingleton alternative thins to an
  actual prefix-front of inclusion-minimal active order-\(4\) traces, with
  witnesses \(w_F\ge\max F-1\) and the full three-term vertex-cover
  condition from Lemma 10.1.
* Corollary 16.36 records the exact limitation of importing the \(k=2\)
  front closure: bounded ordered-depth debt in such a \(k=3\) front gives
  fractional reflected rows only in \(2A\), not in \(A\). The unresolved
  nonsingleton branch must therefore convert \(2A\)-mirrors into usable
  four-term repairs or escape through unbounded depth/rank.
* Lemma 16.37 gives the corresponding nonsingleton collision split: a
  \(2A\)-row attached to a deleted color \(f\) either is not retained in
  \(2C\), hence all its two-sum representations meet the finite deleted
  palette \(F\), or the gate translate \(f+u\) is not retained in \(2C\).
  Unlike the singleton case, this yields finite-color dependence rather
  than a unique gate.
* Corollary 16.38 closes the large row-dependent part of that finite-color
  branch at bounded rank: over any finite test whose large subsets contain
  a \(k=3\) certificate tuple, too many row-dependent \(2A\)-rows force an
  actual \(A\)-reflected certificate and hence a good order-\(4\) deletion
  by Lemma 2.3b.
* Lemma 16.39 handles the other half of the split: a large gate-dependent
  packet is independent modulo the finite deleted palette,
  \((U+f-U)\cap A\subseteq F\). This is the nonsingleton replacement for
  the singleton unique-gate condition of Corollary 16.22.
* Lemma 16.40 gives the first finite-palette gate pressure: if one anchored
  translate \(f+U-u_0\) lies in \(A\), then finite-palette independence
  injects \(U\) into \(F\). Large gate packets must therefore avoid retained
  intervals above the gate.
* Lemma 16.41 strengthens this to a shadow-count statement: every anchored
  translate \(f+U-u_0\) contains at most \(|F|\) points of \(A\). The
  surviving gate branch is therefore a sparse-shadow problem, verified in
  finite toy windows by `EXPERIMENTS/finite_palette_gate_pressure.py`.
* Corollary 16.42 rewrites that sparse-shadow pressure in the form needed
  for block constructions: \(U\) cannot contain more than \(|F|\) points of
  any anchored copy \(u_0+T-f\) of a finite test \(T\subset A\). In
  particular it cannot contain a long translate of an old interval block.
* Corollary 16.43 combines the row and gate halves: over a
  certificate-dense finite test, every bounded-rank packet beyond the
  finite row-dependent allowance is forced into the gate-shadow branch and
  inherits the anchored-copy bound.
* Lemma 16.44 proves that intervals are certificate-dense at the strongest
  useful finite scale: every three-point subset of an interval contains a
  \(k=3\) certificate tuple. Corollary 16.45 therefore specializes the
  bounded-rank normal form to interval tests, leaving only
  \(|F+F|+2|F|\) row-dependent exceptions before the gate-shadow branch
  takes over.
* Lemma 16.46 bounds finite-palette gate packets lying in the same interval
  as their active gate by \(2|F|\), using the two anchored shadows from the
  minimum and maximum packet rows. Corollary 16.47 combines this with the
  interval-test normal form: same-interval bounded-rank packets have size
  at most \(|F+F|+4|F|\).
* Lemma 16.48 handles active gates just outside an interval: if the gate is
  at distance \(\delta\) from the interval, the finite-palette gate packet
  has size at most \(\delta+|F|\). Corollary 16.49 combines this with the
  interval-test normal form, forcing any large bounded-rank interval packet
  to use active colors far outside the tested interval.
* Lemma 16.50 adds the retained two-sum pressure on those far gates:
  a retained subinterval \(J\) forbids every gate row in \(2J-f\).
  Corollary 16.51 says a gate whose band \(2J-f\) covers the tested interval
  supports no gate packet there at all.
* Lemma 16.52 notes that a rank-\(r\) deletion leaves a retained interval
  of length at least \(\lceil(n-r)/(r+1)\rceil\) inside any \(n\)-point
  interval. Corollary 16.53 uses that run to give a quantitative exclusion
  band for every finite-palette gate packet over the interval.
* Lemma 16.54 gives the stronger central two-sum version: deleting at most
  \(r\) points from an interval leaves the band
  \([2a+2r,2b-2r]\) inside the retained two-sumset. Corollaries
  16.55--16.56 translate this into a central gate exclusion range for
  gate-dependent interval packets.
* Corollaries 16.57--16.59 combine that central exclusion with the
  bounded-rank row allowance from Corollary 16.45: any positive-density
  bounded-rank interval packet must use an active gate a linear distance
  outside the tested interval, and more generally packet size is bounded by
  the gate's distance from the central gate range.
* Lemma 16.60 and Corollary 16.61 extend the same estimate to a finite
  active palette: a bounded-rank family of interval packets covering a
  positive fraction of the interval forces linear total distance from the
  central gate range, hence at least one linearly far active color. Thus the
  remaining interval obstruction must have vanishing packet density, growing
  deletion rank, or coordinated far-gate structure across separated blocks.
* Corollary 16.62 quantifies the growing-rank alternative: if a dense
  interval cover keeps all active colors near the central gate range, then
  the deletion rank must satisfy \(r^3+5r^2\ge\eta n\) at interval length
  \(n\). Hence near-gate rank growth is forced on a genuine cubic scale,
  not merely by front padding.
* Lemma 16.63 and Corollary 16.64 give the cross-block retained-band
  version needed for genuinely far gates: a positive-density gate packet in
  one interval is impossible whenever the doubled band of any retained
  interval elsewhere overlaps the test interval deeply. Far-gate
  constructions must avoid all of these overlap windows, not only the
  central two-sum band of the tested block itself.
* Lemma 16.65 and Corollary 16.66 upgrade this to coordinated finite
  palettes: if the active colors are clustered, their shifted doubled bands
  have a common forbidden core. A dense cross-block packet therefore forces
  either palette spread on the scale of the retained interval or an extreme
  active color outside the overlap window.
* Corollary 16.67 packages finite blocker families: every retained interval
  contributes a forbidden affine gate window for dense packets over the test
  interval, and clustered finite palettes cannot be contained in any one
  blocker window unless their span exceeds the retained interval's doubled
  length allowance.
* Corollary 16.68 removes clustering by pigeonholing: an \(\eta\)-dense
  packet carried by at most \(r\) active colors has one \(\eta/r\)-dense
  color, which must avoid every blocker window at that smaller density.
* Lemma 16.69 and Corollary 16.70 make blocker windows independent of the
  actual deletion pattern inside an auxiliary interval \(K\): deleting at
  most \(r\) points leaves a retained run, and the intersection of all
  possible blocker windows from such runs is a robust forbidden gate core.
  Bounded palettes carrying dense packets must have at least one active
  color outside this core.
* Lemma 16.71 gives the exact core length
  \(\max\{0,n-2M_\delta+4\ell_0-2m\}\). This records when the robust
  blocker is genuinely present and when the argument must use the actual
  retained run rather than only the rank-\(r\) guarantee.
* Corollary 16.72 converts that exact formula into an asymptotic tool:
  for fixed \(r\) and density \(\delta>1/2\), every auxiliary interval
  whose length is a sufficiently small fixed fraction of the tested
  interval supplies a robust blocker core of linear length.
* Corollary 16.73 folds the bounded-rank row allowance back in: if all
  active colors of a bounded-rank interval packet lie in such a robust core,
  then the packet cannot cover a fixed positive fraction of the tested
  interval once the interval is long enough.
* Corollary 16.74 gives the corresponding non-robust but often nonempty
  finite-window form: if actual retained intervals supply blocker windows
  covering the active palette, then bounded-rank interval packets using
  that palette cannot be dense.
* Corollary 16.75 records the stronger majority-color route: a single
  active color carrying density \(>1/2\) avoids robust cores directly,
  without the \(1/r\) density loss from palette pigeonholing.
* Lemma 16.76 and Corollary 16.77 make the complementary no-majority branch
  explicit: a dense bounded palette whose individual color fibers all stay
  below a chosen threshold must contain two distinct positive-density
  gate-dependent fibers. The remaining non-majority obstruction is therefore
  at least a two-color gate-shadow problem.
* Corollary 16.78 adds the interval geometry to that two-color branch:
  those two positive-density gate fibers force two active colors a linear
  distance outside the tested interval.
* Corollary 16.79 packages the bounded-rank dense interval normal form for
  densities \(>1/2\): either a majority color escapes every relevant robust
  core, or two active colors are linearly far from the tested interval.
* Attempt 17 records that adding a finite accelerator to a minimal
  order-\((k+1)\) basis is not a shortcut to a counterexample; the witnesses
  must survive every accelerator shift, which is again the collective
  barrier problem.
