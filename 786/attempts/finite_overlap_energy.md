# An \(N/\log N\) deletion lower bound

## Theorem

There is an absolute constant \(c>0\) such that every repetition-allowed PLR
set \(A\subset[1,N]\) satisfies
\[
 N-|A|\geq c\frac{N}{\log N} \tag{1}
\]
for all sufficiently large \(N\).

## Proof

By the grading theorem, \(A\) lies in the level \(f=1\) of a rational
completely additive function. Enlarge \(A\) to the full level
\[
 B=\{n\leq N:f(n)=1\}.
\]
This can only reduce the complement, so it suffices to prove (1) for
\(B\). Write \(E=[1,N]\setminus B\) and \(m=|E|\).

### Prime--cofactor rectangles

For \(C_j=2^j\), let
\[
 P_j=\left\{p\text{ prime}:\frac{N}{2C_j}<p\leq\frac{N}{C_j}\right\}.
\]
Take \(0\leq j\leq J\), where \(C_J\) is the largest power of two not
exceeding \(\sqrt N/4\). Put \(K_j=[1,C_j]\).

Every product \(pk\), \(p\in P_j\), \(k\in K_j\), is at most \(N\).
Moreover, the map \((p,k)\mapsto pk\) is injective across the union of all
these rectangles: every participating prime exceeds \(2\sqrt N>C_J\), so
\(pk=q\ell\) with distinct participating primes would force
\(p\mid\ell<p\).

Let
\[
 R_j=|P_j|,\qquad
 B_j=|\{(p,k)\in P_j\times K_j:pk\in E\}|.
\]
Global injectivity gives
\[
 \sum_{j=0}^J B_j\leq m. \tag{2}
\]
The prime number theorem in dyadic intervals gives an absolute \(c_0>0\)
such that, uniformly for these \(j\),
\[
 R_jC_j\geq c_0\frac{N}{\log N}. \tag{3}
\]

We use the following elementary rectangle fact. If a rectangle
\(P\times K\) has \(R\) rows, \(C\) columns, and \(B\) bad products, then
some \(a\in\mathbb Q\) satisfies
\[
 |\{k\in K:f(k)\neq1-a\}|\leq B/R. \tag{4}
\]
Indeed, choose a row with at most \(B/R\) bad entries. On every good entry,
\(f(p)+f(k)=1\), so its good columns all have the same value \(1-a\).

Fix an absolute \(\eta_0<1/3\). Assume for contradiction that
\[
 m\leq\varepsilon\frac{N}{\log N}, \tag{5}
\]
where \(\varepsilon>0\) will be an absolute sufficiently small constant.
Equations (2)--(5) imply
\[
 B_j/R_j\leq\eta C_j,\qquad
 \eta=\varepsilon/c_0\leq\eta_0. \tag{6}
\]
Let \(a_j\) be the row value supplied by (4). Adjacent cofactor intervals
\(K_j\subset K_{j+1}\) have at most
\[
 \eta C_j+\eta C_{j+1}=3\eta C_j
\]
exceptions to their two prescribed cofactor values. Since
\(\eta_0<1/3\), some \(k\in K_j\) has both prescribed values, and hence
\(a_j=a_{j+1}\).

For \(j=0\), \(K_0=\{1\}\). Since (4) has fewer than one exceptional column,
its sole column is nonexceptional. Thus
\(f(1)=0=1-a_0\), so \(a_0=1\).
It follows inductively that every \(a_j=1\). At the last scale,
\[
 Z:=\{k\leq C_J:f(k)=0\}
\]
therefore satisfies
\[
 |Z|\geq(1-\eta)C_J. \tag{7}
\]

### Multiplicative energy

Every product of two elements of \(Z\) is at most
\(C_J^2\leq N\), has grading zero, and hence lies in \(E\). Thus
\[
 m\geq|Z\cdot Z|. \tag{8}
\]

For \(M=C_J\), the number of solutions to
\[
 ab=cd,\qquad a,b,c,d\leq M,
\]
is at most
\[
 2M^2(1+\log M). \tag{9}
\]
To see this, write \(a=gr,c=gs\) with \((r,s)=1\). Then
\(b=sh,d=rh\), and \(g,h\leq M/\max(r,s)\). There are at most \(2q\)
pairs \((r,s)\) with \(\max(r,s)=q\), giving
\[
 \sum_{q\leq M}2q\left\lfloor\frac Mq\right\rfloor^2
 \leq2M^2\sum_{q\leq M}\frac1q.
\]

By Cauchy--Schwarz and (7)--(9),
\[
 m\geq|Z\cdot Z|
 \geq\frac{|Z|^4}{2M^2(1+\log M)}
 \geq c_1\frac{N}{\log N}, \tag{10}
\]
for an absolute \(c_1=c_1(\eta_0)>0\), because
\(C_J\asymp\sqrt N\).

Choose \(\varepsilon<\min(c_0\eta_0,c_1)\). Then (6) has
\(\eta\leq\eta_0\), while equations (5) and (10) contradict each other.
This proves (1).

## Scope and bottleneck

The proof uses only the exact grading theorem and the prime number theorem.
It still permits \(m=o(N)\), so the original finite question remains open.
The scale \(N/\log N\) is also the cost of cutting one prime--cofactor
incidence band; improving (1) requires using complete additivity across
multiple such cuts, not graph connectivity alone.
