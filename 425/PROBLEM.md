# Erdős Problem #425

Source: <https://www.erdosproblems.com/425>  
Fetched from the site's LaTeX-source view on 2026-07-16. Status on the page: **OPEN**.

## Verbatim statement

Let $F(n)$ be the maximum possible size of a subset $A\subseteq\{1,\ldots,N\}$ such that the products $ab$ are distinct for all $a<b$. Is there a constant $c$ such that
\[
F(n)=\pi(n)+(c+o(1))n^{3/4}(\log n)^{-3/2}?
\]
If $A\subseteq \{1,\ldots,n\}$ is such that all products $a_1\cdots a_r$ are distinct for $a_1<\cdots<a_r$ then is it true that
\[
|A|\leq \pi(n)+O\!\left(n^{\frac{r+1}{2r}}\right)?
\]

## Source ambiguity

The source defines $F(n)$ using $A\subseteq\{1,\ldots,N\}$. This likely intends $n$, but solving work must record and justify the normalization rather than silently altering it.

The natural reading is that the map from unordered two-element subsets $\{a,b\}\subset A$ to $ab$ is injective. For the second question, work must specify whether $r$ is fixed and confirm that all products indexed by distinct $r$-subsets are pairwise distinct.

## Initial goal

Determine the second-order constant in the pair-product problem, or prove a structural reduction that identifies it; independently attack the stated general $r$-fold bound.
