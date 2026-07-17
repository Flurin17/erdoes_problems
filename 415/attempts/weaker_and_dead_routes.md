# Route tournament: weaker and eliminated mechanisms

The table records the first exact failure, not merely a low confidence score.

| Route | Valid content | First failure or reason it loses | Weakest repair |
|---|---|---|---|
| Parity pairing | A decreasing block forces $\log_3 n\ge(\log2/2+o(1))k$. | This is only linear in $k$ and is dominated by primorial propagation, which gives $k\log_3k$. | Use a primorial multiple early in the block and propagate its entire loss. |
| Odd-term averaging | Gives a valid coefficient involving $\sum_{p>2}w_p/p$. | Recurrent odd-prime contributions cancel under even--odd pairing; the resulting constant is not sharp. | Pair equal-length even and odd progressions, or use Route B. |
| Prescribed divisors without avoidance | CRT forces chosen primes into selected shifts. | Extra unprescribed primes can reduce a would-be large totient by arbitrarily large total weight along the CRT progression. | Prescribe or avoid every prime through a cutoff and prove a rough-tail bound. |
| Ordering only $\phi(t)/t$ | Correctly orders normalized totients. | It need not order raw totients: $phi(3)=\phi(4)=2$ although the normalized ratios differ. | Require the exact margin $L_i-L_j>\log((m+i)/(m+j))$. |
| Pairwise-coprime divisor architecture | Generalized CRT compatibility is transparent. | Robustness against arbitrary cofactors can force quadratic rank gaps and is far too expensive. | Use full cutoff control, where the remaining cofactor error is $O(1/\log y)$. |
| Nested prime sets | Produces ordered normalized products abstractly. | A prime can divide two shifts only if it divides their difference; literal nesting is incompatible for private primes $>k$. | Use disjoint private prime blocks. |
| Independent random supports | Suggests pattern frequencies. | Shifted divisibility events are not independent: one residue modulo $p$ selects an entire residue-class footprint. | Use the exact Haar-profinite residue model of Route C. |
| Signature/entropy counting | Bounds the number of coarse prime-incidence signatures. | One signature may realize many permutations; assuming multiplicity one is the first invalid inference. | Bound compatible linear extensions inside every signature, which did not improve the sharp obstruction. |
| Small-prime phase minimax | Gives an exact continuous top-up problem. | Its finite maximizer need not be decreasing; at $k=4$ a nonmonotone order costs more in the relaxation. It also omits raw-$\phi$ factor corrections. | Treat it as an auxiliary optimization only; use Route B for the universal lower bound. |
| Prime-tuple/linear-form cofactors | Would make cofactors especially clean. | Simultaneous primality of the required linear forms invokes an unproved prime-tuples hypothesis. | The deterministic all-primes-through-$y$ construction avoids any primality conjecture. |

## Surviving route ranking

1. **Full-control CRT construction:** uniform over all permutations, sharp
   through the linear term in $k$ on the $\log_3M_k$ scale.
2. **Primorial-propagation obstruction:** architecture-independent and matches
   the construction using only the decreasing pattern.
3. **Profinite frequency theorem:** independent resolution of the fixed-$k$
   frequency question and a $k=3$ natural-order counterexample.
4. **Exact finite scan:** disproves finite decreasing extremality already at
   $k=4$ and supplies regression fixtures.
