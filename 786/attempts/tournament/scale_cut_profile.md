# A multiscale prime-profile lemma

This note isolates a genuinely bounded-overlap version of the scale-cut
argument.  It applies to a completely additive map
\(f:\mathbb N\to\mathbb Q\), a nonzero target \(t\), and

\[
 A=\{n\le N:f(n)=t\},\qquad D=N-|A|.
\]

The conclusion is that a hypothetical \(D=o(N)\) forces the prime weights
to vanish, in harmonic measure, throughout every fixed middle range
\(N^\alpha<p\le N^{1-3\alpha}\).  The proof uses two different disjoint
edge packings.  No assertion about the values of the small cofactors is
needed.

## Statement

Fix \(0<\alpha<1/20\), put \(L=\lfloor\log _2N\rfloor\),
\(y=N^\alpha\), and

\[
 B_i=(2^i,2^{i+1}],\qquad
 {\cal P}_i=\{p\text{ prime}:p\in B_i\}.
\]

Suppose \(D=o(N)\).  For every index

\[
 \alpha L+O(1)\le i\le(1-3\alpha)L-O(1)
\]

choose a most frequent value \(c_i\) among \(\{f(p):p\in{\cal P}_i\}\).
Then

\[
 \sum_{N^\alpha<p\le N^{1-3\alpha}\atop f(p)\ne0}\frac1p=o(1).       \tag{1}
\]

More quantitatively, before the final stability step one has

\[
 \sum_i\sum_{p\in{\cal P}_i\atop f(p)\ne c_i}\frac1p
       \ll_\alpha \frac DN+o(1),                                    \tag{2}
\]

and, on

\[
 I=[\alpha L+O(1),(1-3\alpha)L/2-O(1)]\cap\mathbb Z,
\]

both profile equations

\[
 c_i+c_j=c_{i+j},\qquad c_i+c_j=c_{i+j+1}                            \tag{3}
\]

hold for all but \(o(L^2)\) pairs \((i,j)\in I^2\).  Bad input or
output bands are included among these exceptional pairs.

## 1. Modalization by lifted prime pairs

Let \(M_i\) be the size of the largest weight class in \({\cal P}_i\),
and let \(P_i=|{\cal P}_i|\).  The primes in the band can be partitioned
so as to contain at least

\[
 q_i\ge \frac{P_i-M_i-1}{2}
\]

disjoint pairs \(\{p,q\}\) with \(f(p)\ne f(q)\).  (If the largest
class has size at least \(P_i/2\), match it to the other classes; if not,
greedily match two currently largest distinct classes.)

For every such pair and every \(y\)-smooth integer

\[
 d\le N/2^{i+1},
\]

join \(pd\) to \(qd\).  The two endpoints cannot both lie in \(A\),
because their \(f\)-values differ by \(f(p)-f(q)\).

All these edges, over all pairs and bands, are vertex-disjoint.  Indeed,
every prime in question is bigger than \(y\), whereas \(d\) has no prime
factor bigger than \(y\).  Unique factorization therefore recovers from
an endpoint its unique large-prime signature and then its cofactor.

For the indicated range of \(i\), the standard fixed-\(u\) smooth-number
estimate gives, uniformly,

\[
 \Psi(N/2^{i+1},y)\ge \kappa_\alpha N/2^i                         \tag{4}
\]

for some \(\kappa_\alpha>0\).  Consequently

\[
 D\ge \kappa_\alpha N\sum_i\frac{q_i}{2^i}.
\]

Since \(p\asymp2^i\) in the band, this proves (2).

Choose a number \(\eta_N\downarrow0\) so slowly that
\(D/(\eta_NN)\to0\).  Call a band good when
\(M_i\ge(1-\eta_N)P_i\).  The prime number theorem and (2) show that all
but \(o(L)\) middle bands are good.

## 2. A globally disjoint prime--semiprime packing

Take good \(i,j\in I\).  Fixed positive subintervals of the two dyadic
prime bands give

\[
 \gg_\alpha \frac{2^{i+j}}{L^2}
\]

products \(pq\), with \(f(p)=c_i,f(q)=c_j\), in each of the numerical
bands \(B_{i+j}\) and \(B_{i+j+1}\).  For example, primes in
\((2^i,5\cdot2^i/4]\) and \((2^j,5\cdot2^j/4]\) give products in the
first product band, while primes in
\((3\cdot2^i/2,7\cdot2^i/4]\) and
\((3\cdot2^j/2,7\cdot2^j/4]\) give products in the second.  PNT supplies
the required counts, and the \(o(1)\) nonmodal fraction cannot remove a
fixed positive subinterval.  When \(i=j\), discard squares and use
unordered pairs.

Suppose, for \(e\in\{0,1\}\), that

\[
 c_i+c_j\ne c_{i+j+e}.                                               \tag{5}
\]

Reserve

\[
 r_{i,j,e}=\left\lfloor a_\alpha 2^{i+j+e}/L^2\right\rfloor
\]

of the preceding modal semiprimes in \(B_{i+j+e}\), and the same number
of modal primes from \({\cal P}_{i+j+e}\).  Here \(a_\alpha>0\) is a
fixed sufficiently small constant.  There are only \(O(L)\) input pairs
with a given output index, whereas the output band contains
\(\gg2^{i+j+e}/L\) modal primes.  Hence the output primes can be allocated
disjointly over every failed equation.  The semiprime pools are already
disjoint after restricting to \(i\le j\), and the pools for \(e=0,1\)
are separated by product size.

Pair each reserved semiprime \(s=pq\) to a reserved prime \(r\), and for
every \(y\)-smooth

\[
 d\le N/2^{i+j+e+1}
\]

join \(sd\) to \(rd\).  Equation (5) says that each edge meets the
complement of \(A\).  More importantly, the full family is globally
vertex-disjoint: an endpoint has either one or two prime factors bigger
than \(y\), counted with multiplicity, and this large-prime signature
uniquely determines the reserved object and the smooth cofactor.

The largest output index is at most \((1-3\alpha)L+O(1)\), so (4), with
changed constants, again applies.  Each failed equation therefore
contributes \(\gg_\alpha N/L^2\) disjoint edges.  Thus

\[
 D\ge c_\alpha\frac{N}{L^2}\,
 \#\{\text{failed equations in (3) on good bands}\}.                \tag{6}
\]

Since only \(o(L)\) bands are bad, (6) proves (3).

## 3. The exact profile lemma

The elementary dense Pexider lemma needed here is the following.

**Dense interval Pexider lemma.**  Let \(I_n\) be integer intervals of
length \(\asymp n\), and let \(G\) be a torsion-free abelian group.  If
maps \(a:I_n\to G\) and \(b:I_n+I_n\to G\) obey

\[
 a_i+a_j=b_{i+j}
\]

outside \(o(n^2)\) pairs, then there are \(u,v\in G\otimes\mathbb Q\)
such that

\[
 a_i=ui+v\quad\text{for all but }o(n)\text{ indices},
 \qquad b_h=uh+2v\quad\text{for all but }o(n)\text{ indices}.         \tag{7}
\]

For completeness, one proof is the usual majority cleanup for the
Pexider equation.  After translating \(I_n\) to \([1,m]\), discard the
\(o(m)\) rows having more than \(o(m)\) failures.  Comparing two surviving
rows shows that, for all but \(o(m)\) shifts \(d\), the difference
\(a_{x+d}-a_x\) has one value for all but \(o(m)\) admissible \(x\).
Call that majority value \(U(d)\).  Comparing a shift \(d+e\) with the
two successive shifts \(d,e\) gives
\(U(d+e)=U(d)+U(e)\) outside \(o(m^2)\) admissible pairs.  A second
majority cleanup makes this identity exact after changing \(U\) at
\(o(m)\) arguments.  On an integer interval an exact additive map is
\(U(d)=ud\).  Substitution in the surviving rows gives (7).  Each cleanup
loses at most a fixed power of the original exceptional proportion, hence
still only \(o(m)\) points.

Apply the lemma to the first equation in (3).  It gives

\[
 c_i=ui+v\quad(i\in I),\qquad c_h=uh+2v\quad(h\in I+I)               \tag{8}
\]

apart from \(o(L)\) indices.  The shifted equation in (3) and (8) force
\(u=0\).  Finally, \(I\cap(I+I)\) has length \(\asymp L\) when
\(\alpha<1/7\).  On that overlap (8) assigns both \(v\) and \(2v\) to
all but \(o(L)\) indices, so \(v=0\).  Hence \(c_i=0\) on all but
\(o(L)\) bands in \(I\cup(I+I)\), which covers the whole middle range.
Together with (2) and Mertens/PNT band estimates, this proves (1).

## 4. What this does and does not finish

The lemma closes the precise multiscale overlap gap left by the earlier
one-scale \(N/\log N\) argument.  To turn it into a self-contained finite
constant-gap theorem, one still needs a uniform small-prime transfer:

1. primes above \(N^{1-3\alpha}\) divide at most
   \(( -\log(1-3\alpha)+o(1))N=O(\alpha N)\) integers;
2. by (1), active middle primes divide only \(o(N)\) integers;
3. the valuation vector at primes \(p\le N^\alpha\) is, by the fixed-\(u\)
   Kubilius fundamental lemma, within an error \(\varepsilon(1/\alpha)+o(1)\)
   of independent geometric valuations, where \(\varepsilon(u)\to0\);
4. every nonzero atom of an arbitrary rationally weighted independent
   geometric sum is at most \(1/2\).

Choosing \(\alpha\) small would then bound \(|A|/N\) away from one.  The
present note proves the new combinatorial/profile component; the stated
smooth-number lower bound and the final Kubilius transfer should be cited
or proved separately in any promoted proof.
