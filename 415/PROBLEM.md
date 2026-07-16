# Erdős Problem #415

Source: <https://www.erdosproblems.com/415>  
Fetched from the site's LaTeX-source view on 2026-07-16.

## Verbatim statement

For any $n$ let $F(n)$ be the largest $k$ such that any of the $k!$ possible ordering patterns appears in some sequence of $\phi(m+1),\ldots,\phi(m+k)$ with $m+k\leq n$. Is it true that
\[
F(n)=(c+o(1))\log\log\log n
\]
for some constant $c$? Is the first pattern which fails to appear always
\[
\phi(m+1)>\phi(m+2)>\cdots>\phi(m+k)?
\]
Is it true that the “natural” ordering which mimics what happens to $\phi(1),\ldots,\phi(k)$ is the most likely to appear?

## Source ambiguity

“Any of the $k!$ possible ordering patterns appears” is ambiguous in isolation. The nontrivial intended reading appears to be that **every** one of the $k!$ patterns occurs somewhere up to $n$. This must be treated as an explicit normalization, not silently substituted into the verbatim statement.

## Initial goal

Determine the correct scale and constant for $F(n)$ by building residue/prime-factor prescriptions for arbitrary patterns and matching them with an obstruction.
