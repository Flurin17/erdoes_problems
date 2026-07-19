# Bounded-budget avoidance and a uniform nonzero-level gap

This note isolates a zero-prime construction that is uniform in a grading
which may depend on \(N\).  It has two consequences.

1. Subject to the standard Halász--Ruzsa exact-atom theorem stated below,
   there are absolute constants \(\delta>0\) and \(N_0\) such that, for every
   completely additive \(f:\mathbb N\to\mathbb Q\), every nonzero
   \(t\in\mathbb Q\), and every \(N\geq N_0\),
   \[
      |\{n\leq N:f(n)=t\}|\leq (1-\delta)N.             \tag{1}
   \]
2. Using only the already audited \(N/\log N\) bound and elementary prime
   estimates, one obtains the unconditional quantitative estimate
   \[
      N-|\{n\leq N:f(n)=t\}|
        \gg \frac{N\log\log\log N}{\log N}.             \tag{2}
   \]

The first statement is the decisive finite obstruction for the
repetition-allowed reading of Problem 786.  The sole externally cited input
in its proof is displayed explicitly in Section 4.

Throughout, a prime \(p\) is **active** if \(f(p)\ne0\).  An integer is
**\(f\)-free** if none of its prime divisors is active.  Every \(f\)-free
integer \(n\) satisfies \(f(n)=0\).

## 1. Harmonic mass of integers avoiding a prime set

### Lemma 1 (harmonic avoidance)

Let \(\mathcal S\) be a set of primes and let \(x\geq2\).  Suppose
\[
 H_x:=\sum_{\substack{p\leq x\\p\in\mathcal S}}\frac1p\leq H
\]
and \(x\log x\geq 2H+4\).  Then
\[
 \sum_{\substack{n\leq x\\p\mid n\Rightarrow p\notin\mathcal S}}\frac1n
 \geq c\,e^{-2H}\frac{\log x}{H+1}                    \tag{3}
\]
for an absolute \(c>0\).

#### Proof

Put \(d=2H+4\) and \(\sigma=1+d/\log x\).  If
\(\mathcal S_x=\mathcal S\cap[2,x]\), then
\[
 F(\sigma):=\sum_{\substack{n\geq1\\p\mid n\Rightarrow p\notin\mathcal S_x}}
 n^{-\sigma}
 =\zeta(\sigma)\prod_{p\in\mathcal S_x}(1-p^{-\sigma}).
\]
Since \(-\log(1-u)\leq2u\) for \(0\leq u\leq1/2\),
\[
 \prod_{p\in\mathcal S_x}(1-p^{-\sigma})\geq e^{-2H}.
\]
Also \(\zeta(\sigma)\geq1/(\sigma-1)=\log x/d\).  On the other hand,
\[
 \sum_{n>x}n^{-\sigma}
 \leq x^{-\sigma}+\int_x^\infty u^{-\sigma}\,du
 =\frac{e^{-d}}x+e^{-d}\frac{\log x}{d}.
\]
The second term is only an \(e^{-4}\) fraction of the preceding lower
bound for \(F(\sigma)\), and the first is no larger under the displayed
hypothesis on \(x\).  Thus
\[
 \sum_{\substack{n\leq x\\p\mid n\Rightarrow p\notin\mathcal S_x}}n^{-\sigma}
 \geq c e^{-2H}\frac{\log x}{H+1}.
\]
For \(n\leq x\), avoiding \(\mathcal S_x\) is the same as avoiding
\(\mathcal S\), and \(n^{-1}\geq n^{-\sigma}\).  This proves (3). \(\square\)

## 2. A zero-heavy band and a many-factor convolution

### Lemma 2 (band convolution with arbitrary anchors)

There are absolute constants \(a_0,\varepsilon_0,c,C>0\) with the following
property.  Let \(0<a\leq a_0\), assume
\[
 a^2\log N\longrightarrow\infty,                       \tag{4}
\]
and suppose
\[
 \sum_{\substack{N^a<p\leq N^{2a}\\f(p)\ne0}}\frac1p
 \leq\varepsilon_0.                                    \tag{5}
\]
For every \(f\)-free anchor \(z\leq N^{a/100}\), there are at least
\[
 \exp\!\left[-\frac C a\log\frac{2}{a}\right]
 \frac{N}{z\log N}                                     \tag{6}
\]
distinct \(f\)-free integers \(n\leq N\) of the form
\[
 n=zq_1\cdots q_r,qquad N^a<q_s\leq N^{2a},            \tag{7}
\]
where the \(q_s\) are distinct zero-weight primes.  The families in (7)
belonging to different anchors are disjoint.

Here and below (4) means that the assertion is used along a range in which
the left side tends to infinity.  Equivalently, there is an absolute
threshold in (4), depending only on the fixed constants in the proof.

#### Proof

Use base-two logarithms in this proof and put \(L=\log_2N\).  Apart from
two endpoint cells, split \((N^a,N^{2a}]\) into
\[
 D_j=(2^j,2^{j+1}],\qquad aL+2\leq j\leq2aL-2.
\]
The ordinary dyadic prime estimate gives
\[
 |D_j\cap\mathbb P|\geq c_0\frac{2^j}{j}.              \tag{8}
\]
Call \(j\) good when at least half this lower bound consists of zero-weight
primes.  A bad cell contributes \(\gg1/(aL)\) to (5).  Taking
\(\varepsilon_0\) sufficiently small, all but at most \(\eta aL\) cells
are good, where \(\eta>0\) is a sufficiently small fixed constant.

Fix a small \(\theta>0\).  Every integer
\[
 h\in[(3-\theta)aL,(3+\theta)aL]                       \tag{9}
\]
then has at least \(c_1aL\) ordered representations
\(h=j_1+j_2\) by good indices.  Before the bad indices are removed, the
admissible \(j_1\)'s form an interval of length
\((1-\theta)aL-O(1)\); each bad index destroys at most two
representations.

Set
\[
 k=\left\lfloor\frac1{3a}+\frac12\right\rfloor,qquad r=2k,
 \qquad T_z=\lfloor\log_2(N/z)\rfloor-r.                \tag{10}
\]
We choose \(a_0\ll\theta\).  To check the moving center exactly, write
\(e=3ak-1\), so \(|e|\leq3a/2\), and
\(b=\log_2z/L\leq a/100\).  Then
\[
 \frac{T_z}{k}-3aL
 =3aL\left(\frac{1-b+O(1/L)}{1+e}-1\right)-2
 =O(a^2L)+O(1).                                        \tag{11}
\]
Thus, after decreasing \(a_0\), the center \(T_z/k\) lies inside (9)
with margin at least \(c_2aL\).  Moreover
\[
 \frac{aL}{k}\asymp a^2L\longrightarrow\infty.         \tag{12}
\]
Choose the first \(k-1\) values \(h_i\) in an integer interval of radius
\(c_3aL/k\) about \(T_z/k\), with \(c_3\) sufficiently small.  Their
forced last value \(h_k=T_z-\sum_{i<k}h_i\) remains in (9).  Hence there
are at least
\[
 \left(\frac{c_4aL}{k}\right)^{k-1}                   \tag{13}
\]
such \(h\)-tuples and at least
\[
 (c_1aL)^k\left(\frac{c_4aL}{k}\right)^{k-1}           \tag{14}
\]
ordered good-index tuples with total sum \(T_z\).

If \(Z_j\) is the number of zero-weight primes in a good cell, then
\[
 Z_j\geq c_5\frac{2^j}{aL}.                            \tag{15}
\]
Condition (12) implies \(\min Z_j\gg r\).  The primes can therefore be
chosen successively and distinctly, at a cost at most \(2^{-r}\).  For
each index tuple the number of ordered prime tuples is at least
\[
 \left(\frac{c_6}{aL}\right)^r2^{T_z}.                 \tag{16}
\]
Multiplying (14) and (16), and dividing by at most \(r!\) ordered
realizations of one squarefree product, leaves
\[
 \frac{2^{T_z}}{aL}\exp[-C_0r\log(r+2)].               \tag{17}
\]
Since \(2^{T_z}\geq N/(2^{r+1}z)\) and \(r\asymp1/a\), (17) implies
(6).  The definition of \(T_z\) also gives
\(zq_1\cdots q_r\leq N\).

All factors of \(z\) are at most \(N^{a/100}\), whereas all selected
primes exceed \(N^a\).  Consequently \(z\) is recovered from (7) as its
entire prime-power part supported below \(N^{a/100}\).  This proves
disjointness across anchors.  Every factor in (7) is a zero-weight prime,
so every constructed integer is \(f\)-free. \(\square\)

## 3. Bounded reciprocal budget forces a positive zero density

### Proposition 3

For every fixed \(K<\infty\) there are constants \(c_K>0\) and \(N_K\)
such that, whenever
\[
 \sum_{\substack{p\leq N\\f(p)\ne0}}\frac1p\leq K,     \tag{18}
\]
at least \(c_KN\) integers \(n\leq N\) are \(f\)-free.

#### Proof

Fix the constants from Lemma 2.  Starting with a sufficiently small fixed
\(a_*=2^{-i_0-1}<a_0\), consider the disjoint bands
\[
 (N^{a_i},N^{2a_i}],\qquad a_i=2^{-i-1},quad
 i=i_0,i_0+1,\ldots .                                  \tag{19}
\]
Among the first
\(s=\lceil(K+1)/\varepsilon_0\rceil\) bands, one has active reciprocal
mass at most \(\varepsilon_0\).  Its exponent satisfies
\[
 a_K^*:=2^{-i_0-s-1}\leq a\leq a_* .                  \tag{20}
\]
For fixed \(K\), condition (4) holds when \(N\) is sufficiently large.

Put \(x=N^{a/100}\).  Lemma 1 and (18) give
\[
 \sum_{\substack{z\leq x\\z\ \mathrm{is}\ f\text{-free}}}\frac1z
 \geq c e^{-2K}\frac{a\log N}{K+1}.                  \tag{21}
\]
Apply Lemma 2 to every anchor in (21).  Its disjointness assertion permits
summation, and yields at least
\[
 \frac{N}{\log N}
 \exp\!\left[-\frac Ca\log\frac2a\right]
 \sum_{\substack{z\leq x\\z\ \mathrm{is}\ f\text{-free}}}\frac1z
 \geq c_KN,                                            \tag{22}
\]
where (20) makes the final constant positive and dependent only on \(K\).
\(\square\)

## 4. The standard exact-atom input and an absolute gap

We use the following theorem as a **standard external input**.  Its exact
uniformity is important here.

### Halász--Ruzsa exact-atom theorem

There is an absolute constant \(C_{HR}\) such that, for every
integer-valued strongly additive function \(g\) and every \(x\geq2\),
\[
 Q_x(g):=\max_{u\in\mathbb Z}\frac1x
       |\{n\leq x:g(n)=u\}|
 \leq C_{HR}\left(1+
       \sum_{\substack{p\leq x\\g(p)\ne0}}\frac1p\right)^{-1/2}. \tag{HR}
\]

Here strongly additive means
\(g(n)=\sum_{p\mid n}g(p)\), without prime-power multiplicity.

### Proposition 4 (uniform nonzero-level gap)

Assuming (HR), there are absolute \(\delta>0\) and \(N_0\) for which
(1) holds.

#### Proof

Suppose otherwise.  There would be \(N_j\to\infty\), completely additive
\(f_j:\mathbb N\to\mathbb Q\), and nonzero \(t_j\) such that
\[
 \frac1{N_j}|\{n\leq N_j:f_j(n)=t_j\}|\longrightarrow1. \tag{23}
\]
Let \(m_j\) be the size of the complementary set and let \(y_j\) be the
least active prime at most \(N_j\).  For any active prime \(p\), each
\(p\)-adic chain
\[
 u,up,up^2,\ldots,qquad p\nmid u,
\]
contains at most one member of a fixed level, because consecutive values
differ by the nonzero quantity \(f_j(p)\).  There are
\(N_j-\lfloor N_j/p\rfloor\) such chains with a member at most \(N_j\).
Consequently
\[
 m_j\geq\lfloor N_j/p\rfloor,
 \qquad y_j\geq\frac{N_j}{m_j+1}\longrightarrow\infty. \tag{24}
\]
If there is no active prime, (23) is impossible because \(t_j\ne0\).

Define the strongly additive function
\[
 g_j(n)=\sum_{p\mid n}f_j(p).
\]
The functions \(f_j\) and \(g_j\) agree unless \(n\) is divisible by
\(p^2\) for an active prime \(p\).  By (24), the exceptional proportion is
at most
\[
 \sum_{p\geq y_j}\frac1{p^2}=o(1).                    \tag{25}
\]
Thus \(Q_{N_j}(g_j)\to1\).  Only finitely many rational values \(g_j(p)\),
\(p\leq N_j\), occur, so multiplying by a common denominator produces an
integer-valued strongly additive function without changing its atoms or
its active primes.  Applying (HR), we conclude that
\[
 H_j:=\sum_{\substack{p\leq N_j\\f_j(p)\ne0}}\frac1p\leq K_0            \tag{26}
\]
for some absolute \(K_0\) and every sufficiently large \(j\).

Proposition 3 now supplies at least \(c_{K_0}N_j\) \(f_j\)-free integers.
They all have value zero and hence all lie outside the nonzero level
\(t_j\), contradicting (23). \(\square\)

## 5. Moving-budget tracking: a three-logarithm bound

This section does not use (HR).  Its input is the already proved uniform
estimate
\[
 X-|\{n\leq X:F(n)=u\}|\geq cX/\log X                \tag{27}
\]
for every completely additive rational \(F\) and every nonzero \(u\).

Let
\[
 m=N-|\{n\leq N:f(n)=t\}|,qquad
 R=\frac{m\log N}{N},                                  \tag{28}
\]
where \(t\ne0\).  Rescaling permits us to take \(t=1\).  Let \(M\) be
the largest power of two below \(\sqrt{N/2}\), and put
\[
 H=\sum_{\substack{p\leq M\\f(p)\ne0}}\frac1p.
\]
The largest-prime row charge gives
\[
 H\leq C_0(R+1).                                       \tag{29}
\]
For completeness, for each power \(C_j=2^j\leq M\) take
\[
 P_j=(N/(2C_j),N/C_j]\cap\mathbb P.
\]
All products \(pk\), \(p\in P_j\), \(k\leq C_j\), are jointly distinct
and have unique largest prime factor \(p>M\).  If \(f(p)=1\), every active
prime cofactor \(q\leq C_j\) produces an error.  If \(f(p)\ne1\), (27),
applied after rescaling to the nonzero target \(1-f(p)\), produces
\(\gg C_j/\log C_j\) errors, which is at least a constant multiple of the
number of active primes at most \(C_j\).  Since
\(|P_j|\gg N/(C_j\log N)\), summing the disjoint rows and reversing the
\((j,q)\)-sum proves (29), up to an absorbed absolute additive constant.

We claim that
\[
 R\gg L_3:=\log\log\log N.                             \tag{30}
\]
Suppose, to the contrary, that \(R<\gamma L_3\), where \(\gamma>0\) is a
sufficiently small absolute constant.  Repeat the band selection (19), now
with
\[
 s=\lceil(H+1)/\varepsilon_0\rceil.
\]
One selected band has active reciprocal mass at most \(\varepsilon_0\) and
an exponent satisfying
\[
 e^{-C_1(H+1)}\leq a<a_0.                              \tag{31}
\]
From (29)--(31),
\[
 a\geq \exp[-C_2\gamma L_3]
       = (\log\log N)^{-C_2\gamma},
\]
so in particular \(a^2\log N\to\infty\), as required in Lemma 2.

Set \(x=N^{a/100}<M\).  Lemma 1, with the active primes at most \(M\),
gives
\[
 \sum_{\substack{z\leq x\\z\ \mathrm{is}\ f\text{-free}}}\frac1z
 \geq c e^{-2H}\frac{a\log N}{H+1}.                  \tag{32}
\]
There is no distinction here between avoiding active primes up to \(M\)
and being \(f\)-free, because every prime factor of \(z\leq x\) is below
\(M\).  Summing Lemma 2 over these disjoint anchors yields
\[
 \frac mN
 \geq c\frac{a e^{-2H}}{H+1}
       \exp[-Cr\log(r+2)],
 \qquad r\asymp a^{-1}.                                \tag{33}
\]
Equations (29), (31), and (33) imply, after changing absolute constants,
\[
 \frac mN\geq \exp\{-\exp[C_3(R+1)]\}.                \tag{34}
\]
Under \(R<\gamma L_3\), the exponent on the right of (34) is at most
\[
 C(\log\log N)^{C_3\gamma}.
\]
Choose \(\gamma\) so that \(C_3\gamma<1/2\).  For sufficiently large
\(N\), (34) then gives
\[
 \frac mN\geq\exp[-(\log\log N)^{2/3}],               \tag{35}
\]
whereas (28) and the supposition give
\[
 \frac mN<\frac{\gamma\log\log\log N}{\log N}
 =\exp[-\log\log N+o(\log\log N)].                    \tag{36}
\]
Equations (35) and (36) contradict one another.  This proves (30), and
substitution into (28) proves (2). \(\square\)

## Dependency ledger

- Lemmas 1 and 2 and Proposition 3 are proved here from Euler products,
  ordinary dyadic prime estimates, and unique factorization.
- Proposition 4 depends on the explicitly stated standard theorem (HR).
- The quantitative estimate (2) is independent of (HR); it uses the
  previously audited uniform estimate (27).
- The center and rounding conditions needed for a growing number of
  factors are exactly \(a\ll\theta\) and \(a^2\log N\to\infty\), both
  recorded in (11)--(12) and verified in the moving-budget regime.
