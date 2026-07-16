# Erdős Problem #1005

Source: <https://www.erdosproblems.com/1005>  
Fetched from the site's LaTeX-source view on 2026-07-16.

## Verbatim statement

Let $a_1/b_1,a_2/b_2,\ldots$ be the Farey fractions of order $n\geq4$. Let $f(n)$ be the largest integer such that if $1\leq k<l\leq k+f(n)$ then $a_k/b_k$ and $a_l/b_l$ are similarly ordered—in other words,
\[
(a_k-a_l)(b_k-b_l)\geq0.
\]
Estimate $f(n)$—in particular, is there a constant $c>0$ such that $f(n)=(c+o(1))n$ for all large $n$?

## Source ambiguity

The statement does not explicitly place an existential quantifier on the starting index $k$, even though $f(n)$ is described as a longest run. The solving run must normalize the admissible Farey indices and endpoints and distinguish the existential-block interpretation from a universal interpretation.

## Initial goal

Translate similarly ordered runs into the geometry or recurrence of neighboring Farey fractions and determine matching linear upper and lower bounds, ideally with the constant.
