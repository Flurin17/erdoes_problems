# Finite active-prime chains and smooth-number deletion

Let \(A\subset[1,N]\) be repetition-allowed PLR, let \(m=N-|A|\), and let
\(f(a)=1\) be its rational completely additive grading.

If \(f(p)\neq0\), a fixed level meets each \(p\)-adic chain at most once.
There are \(N-\lfloor N/p\rfloor\) such chains, so
\[
 m\geq\left\lfloor\frac Np\right\rfloor. \tag{1}
\]
Put
\[
 y=\left\lfloor\frac{N}{m+1}\right\rfloor.
\]
Equation (1) forces \(f(p)=0\) for every \(p\leq y\). Thus every \(y\)-smooth
integer has grading zero and lies outside \(A\):
\[
 \boxed{m\geq\Psi(N,y)}. \tag{2}
\]

Using the standard fixed-\(u\) Dickman asymptotic, (2) implies
\[
 m_N=o(N)\quad\Longrightarrow\quad m_N=N^{1-o(1)}.
\]
Indeed, \(m_N\leq N^{1-\eta}\) would give
\(y_N\geq\tfrac12N^\eta\) and then
\(m_N\geq(\rho(2/\eta)+o(1))N\), a contradiction.

This still allows \(m_N=N/\log N\); it does not settle the finite question.
