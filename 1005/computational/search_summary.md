# Exact-search summary

## Verification

On 2026-07-17, `search_a.py --self-test 40` passed every order (1\le n\le40). Implementation A then computed all (4\le n\le500) in 93.834 seconds and wrote `search_a_4_500.tsv`. Implementation B independently agreed with its quadratic oracle through order 25 while scanning through order 200.

Both implementations assert exact fraction order, reducedness, endpoint inclusion, and the displayed compatibility product. A additionally checks neighbor determinant one and denominator-sum (>n).

`verify_construction.py --max-n 500` independently enumerated every proposed four-defect block, checked every pair product, and verified its exact count formula for (16\le n\le500). This check supplements the symbolic proof.

## Selected exact values

| (n) | maximum cardinality | span | maximizing endpoints |
|---:|---:|---:|---|
| 50 | 54 | 53 | (9/10,28/29) |
| 100 | 107 | 106 | (19/20,58/59) |
| 200 | 214 | 213 | (39/40,118/119) |
| 500 | 534 | 533 | (99/100,298/299) |
| 1000 | 1067 | 1066 | (199/200,598/599) |
| 2000 | 2134 | 2133 | (399/400,1198/1199) |
| 5000 | 5334 | 5333 | (999/1000,2998/2999) |

The seven selected orders took 77.518 seconds. Their endpoint pattern led to the rigorously proved four-defect construction with constant (16/15). The table alone is not used as proof.

## Literal reading

Implementation B also calculates the literal-universal span as the minimum index gap of a bad pair minus one. It gives (U_4=2,U_5=3,U_6=3), agreeing with the hand checks in `NOTES.md`.
