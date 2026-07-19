# A Poisson--Dirichlet atom-gap obstruction

## Result

Let \((X_i)\) have law \(\operatorname{PD}(1)\), with
\(X_i>0\) and \(\sum_iX_i=1\) almost surely.  The proposed statement

\[
 \sup_w \Pr\!\left(\sum_i w(X_i)=1\right)<1                 \tag{1}
\]

is **false for measurable profiles**, even if the identity profile itself
is excluded and absolute convergence is required.  Fix
\(1/2<b<b+h<1\), and put

\[
 w_{b,h}(x)=
 \begin{cases}
  0,&b<x<b+h,\\
  x,&\text{otherwise}.
 \end{cases}                                                \tag{2}
\]

Then

\[
 \boxed{
 \Pr\!\left(\sum_iw_{b,h}(X_i)=1\right)
   =1-\log\frac{b+h}{b}\longrightarrow1\quad(h\downarrow0).}
                                                                    \tag{3}
\]

Thus the supremum in (1) is exactly \(1\) for any class containing these
measurable (indeed piecewise-linear) profiles.  This is not the irrelevant
phenomenon of a large atom at zero: the atom in (3) is already at the
nonzero target \(1\), so zero has not been rescaled.

For the narrower class of *rational-valued constant step functions*, (2)
is not admissible.  The arguments below prove that no individual such
profile can have probability one, and give the explicit lower bound

\[
 \sup_{w\text{ rational step}}
 \Pr\!\left(\sum_iw(X_i)=1\right)
 \geq 0.8284995068\ldots .                                  \tag{4}
\]

They do **not** prove that this narrower supremum is less than one.  A
continuum route must state that restriction and prove a uniform, rather
than pointwise, stability theorem before using it in the finite problem.

## 1. The exact counterexample

The first correlation formula for \(\operatorname{PD}(1)\) is

\[
 \mathbb E\sum_i g(X_i)=\int_0^1g(x)\,\frac{dx}{x}           \tag{5}
\]

for every nonnegative measurable \(g\).  There can be at most one
component in \(B=(b,b+h)\subset(1/2,1)\).  Therefore

\[
 \Pr(\text{some }X_i\in B)
 =\mathbb E\#\{i:X_i\in B\}
 =\int_b^{b+h}\frac{dx}{x}
 =\log\frac{b+h}{b}.                                        \tag{6}
\]

The series in (2) is unproblematic:

\[
 \sum_i|w_{b,h}(X_i)|\leq\sum_iX_i=1.                       \tag{7}
\]

If no component lies in \(B\), the statistic is exactly
\(\sum_iX_i=1\).  If the unique component \(X_j\) lies in \(B\), the
statistic is \(1-X_j<1\).  This proves (3).  Taking rational \(b=2/3\)
and rational \(h\downarrow0\) shows that rational breakpoints do not repair
(1); what matters is whether the class forbids the identity slope outside
the steps.

For every \(h>0\), (2) differs from every scalar multiple of the identity
on a set of positive measure.  Excluding only the exact identity, or even
all profiles almost everywhere proportional to it, is therefore
insufficient for a uniform gap.

## 2. Exact split--merge and deletion identities

Choose two components independently by size bias.  If they are distinct,
merge them; if they are the same, split that component at an independent
uniform point.  This split--merge kernel preserves \(\operatorname{PD}(1)\).
For a profile \(w\), write

\[
 D_w=\{(x,y):x>0,\ y>0,\ x+y<1,
               \ w(x+y)\ne w(x)+w(y)\}.                    \tag{8}
\]

The probability of a defective merge is exactly \(|D_w|\), Lebesgue
measure on the triangle.  Indeed, the second correlation density
\((xy)^{-1}\) is cancelled by the size-biasing factors \(xy\).  The
probability of a defective split is also \(|D_w|\): the one-point density
\(dz/z\), the repeated-selection factor \(z^2\), and the uniform split
parameter \(u\) give measure \(z\,dz\,du=dx\,dy\) under
\((x,y)=(uz,(1-u)z)\).  Hence

\[
 \Pr(\text{one split--merge move changes the statistic})=2|D_w|. \tag{9}
\]

If \(E_w=\{\sum_iw(X_i)=1\}\) has probability \(1-\varepsilon\),
stationarity and the union bound show that the old and new partitions both
belong to \(E_w\) with probability at least \(1-2\varepsilon\).  Thus

\[
 |D_w|\leq\varepsilon.                                      \tag{10}
\]

For (2), a defect requires at least one of \(x,y,x+y\) to belong to
\(B\), and consequently

\[
 |D_{w_{b,h}}|
 \leq 2\int_B(1-x)\,dx+\int_Bx\,dx
 \leq3h.                                                     \tag{11}
\]

Thus exact Cauchy defects may have vanishing measure while the profile is
not the identity.  Split--merge invariance has no uniform leverage without
a quantitative separation hypothesis.

There is also a useful exact multiscale form of size-biased deletion.  For
\(s>0\), define

\[
 F_s=\sum_iw(sX_i),\qquad q_s(t)=\Pr(F_s=t),
 \qquad m(s)=\sup_tq_s(t).                                  \tag{12}
\]

The deleted component of the mass-\(s\) partition is uniform on \((0,s)\),
and the remaining partition is an independent scaled PD partition.
Therefore

\[
 q_s(t)=\frac1s\int_0^s q_{s-x}(t-w(x))\,dx,                \tag{13}
\]

and in particular

\[
 m(s)\leq\frac1s\int_0^s m(y)\,dy.                         \tag{14}
\]

If \(q_1(1)=1-\varepsilon\), (13) gives the exact propagation bound

\[
 \int_0^1(1-m(y))\,dy\leq\varepsilon.                       \tag{15}
\]

Thus a putative near-counterexample in a restricted step class has a highly
concentrated statistic at almost every smaller total mass, although its
modal value may depend on the mass.  For a finite rational-valued step
profile which vanishes near zero, every \(F_s\) is countably valued; enumerate
the resulting countable value group and choose the first modal value
\(\tau(s)\).  This makes the choice measurable, and it is unique whenever
\(m(s)>1/2\).  From (13), the set of
\(y\in(0,s)\) on which

\[
 \tau(s)\ne \tau(y)+w(s-y)                                  \tag{16}
\]

has measure at most \(2s(1-m(s))\): on a mismatch the queried child atom
has probability at most \(1-m(y)\) when \(m(y)>1/2\), and at most
\(1/2\) otherwise.  Integrating in \(s\) and using (15) gives

\[
 \left|\{(x,y):x,y>0,\ x+y<1,
       \tau(x+y)\ne\tau(y)+w(x)\}\right|
 \leq2\varepsilon.                                         \tag{17}
\]

Transposing \(x,y\) in (17) shows that
\(w(x)-\tau(x)\) is almost constant on most admissible pairs; after adding
that constant, \(\tau\) is an approximate Cauchy profile.  This identifies
the missing narrow-class lemma precisely.  It does not contradict (2):
there \(w\) is an arbitrarily small perturbation of the exact Cauchy
profile \(x\).

## 3. Classification of probability-one functionals

Split--merge invariance does give a pointwise equality classification.

**Lemma.**  Let \(w:(0,1]\to\mathbb R\) be measurable and suppose that
\(\sum_i|w(X_i)|<\infty\) almost surely.  If

\[
 \sum_iw(X_i)=c_0\qquad\text{almost surely},                 \tag{18}
\]

then there is a constant \(c\) such that \(w(x)=cx\) for
Lebesgue-almost every \(x\), and \(c_0=c\).

**Proof.**  Apply one stationary split--merge move to a partition satisfying
(18).  Both the old and new statistics equal \(c_0\), so (9) implies
\(|D_w|=0\), or

\[
 w(x+y)=w(x)+w(y)quad\text{for almost every }(x,y)\text{ with }x+y<1.
                                                                    \tag{19}
\]

The measurable almost-everywhere Cauchy lemma on an interval gives a
constant \(c\) with \(w(x)=cx\) almost everywhere.  One standard proof
uses Fubini to alter \(w\) on a null set so that the translation identity
holds on a dense full-measure subgroup, then invokes the fact that every
measurable additive function is linear.

A Lebesgue-null set is also null for \(dx/x\) on each \([1/k,1]\).
Formula (5) and a countable union show that almost surely no PD component
belongs to the exceptional set.  Hence
\(\sum_iw(X_i)=c\sum_iX_i=c\), proving \(c_0=c\). \(\square\)

In particular, an almost surely constant value \(1\) forces
\(w(x)=x\) almost everywhere.  If \(w\) is rational-valued almost
everywhere, this is impossible, because for \(c\ne0\) the set
\(\{x:cx\in\mathbb Q\}\) is countable.  Thus every fixed rational-valued
step profile with a well-defined sum has atom probability strictly less
than one.  This pointwise conclusion is much weaker than a uniform gap.

## 4. A rational-step atom of size \(0.828499\ldots\)

For \(2<u<3\), take the rational-valued one-step profile

\[
 w_u(x)=\mathbf1_{x>1/u}.                                    \tag{20}
\]

Its sum is the number \(N_u\) of PD components exceeding \(1/u\), and
\(N_u\in\{0,1,2\}\).  Formula (5) gives

\[
 \mathbb EN_u=\log u.                                       \tag{21}
\]

Let \(\rho(u)=\Pr(N_u=0)\), the Dickman largest-component function.  Its
deletion recurrence is

\[
 \rho(u)=1\ (0\leq u\leq1),
 \qquad u\rho'(u)=-\rho(u-1)\ (u>1).                        \tag{22}
\]

Since \(N_u\leq2\), (21) and total probability give

\[
 \Pr(N_u=1)=2-2\rho(u)-\log u.                              \tag{23}
\]

On \(2<u<3\), (22) yields

\[
 \frac d{du}\Pr(N_u=1)
 =\frac{2\rho(u-1)-1}{u}
 =\frac{1-2\log(u-1)}u.                                    \tag{24}
\]

The unique maximum is at \(u_*=1+\sqrt e\), with

\[
 \Pr(N_{u_*}=1)
 =2-2\rho(1+\sqrt e)-\log(1+\sqrt e)
 =0.828499506858\ldots .                                    \tag{25}
\]

If rational breakpoints are demanded, approximate \(u_*\) by rationals;
continuity gives the same supremal lower bound.  Any theorem for constant
rational steps can therefore have universal gap at most
\(0.171500493142\ldots\).

## 5. Consequence for the finite route

The \(\operatorname{PD}(1)\) limit forgets the microscopic deficit
\(1-\log n/\log N\).  The identity profile records only the deterministic
macroscopic conservation law \(\sum_iX_i=1\), and (2) shows that even a
nonidentity profile can exploit it with probability arbitrarily close to
one.  Hence no unrestricted measurable-profile atom gap can prove a finite
density gap.

A viable continuum lemma must at least do one of the following:

1. restrict to constant rational-valued step profiles and prove a uniform
   quantitative stability theorem for that nonclosed class;
2. impose a fixed quantitative distance from every scalar multiple of
   \(x\); or
3. retain the second-order size budget discarded by the PD limit.

The pointwise equality classification in Section 3 is not a substitute for
any of these uniform statements.
