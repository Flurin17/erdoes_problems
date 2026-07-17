# Coupled-recurrence sign route

For three consecutive Farey vectors,
\[
P_{i+1}=k_iP_i-P_{i-1},\qquad
k_i=\left\lfloor\frac{n+b_{i-1}}{b_i}\right\rfloor.
\]
In an admissible block, orient each adjacent comparison in product order as (U) (both coordinates rise) or (D) (both fall). Direct substitution gives
\[
U\to D:k_i=1,qquad D\to U:k_i\ge3,qquad
D\to D:k_i=2,qquad U\to U:k_i\ge2. \tag{1}
\]
For example, in the only non-immediate case (D\to D), if (k_i\ge3), denominators (B,b,d) obey (B=k_ib-d\ge(k_i-1)b), while the floor formula gives (n+B<(k_i+1)b). Hence (n<2b), but then (B\ge2b>n), impossible.

These restrictions give a finite-state description of the four-defect construction, whose layer word is a truncated (F_4) pattern. They have not yet yielded a sharp global charge: long (U\to U) stretches with varying (k_i\), and transitions among many growing defect layers, are not controlled tightly enough by (1) alone.
