# Exact computation

`compute_451.py` uses the exact forbidden blocks
`[mp+1,mp+k]`.  At each step it chooses a block containing the current
candidate whose right endpoint is farthest right.  That block certifies every
skipped integer.  For the first 50 values it also runs an independent direct
candidate scan.

Reproduce the checked table and certificates:

```sh
python3 computational/compute_451.py 50 \
  --certificates computational/certificates > computational/values_1_50.tsv
python3 computational/verify_451.py computational/certificates
```

The verifier does not trust a supplied prime list: it independently tests
every integer in `(k,2k)` for primality, checks that the certificate blocks
cover every candidate without a gap, and checks the terminal residues.

Finite certificates prove only their stated values; they do not establish an
asymptotic.

Run the independent segmented implementation and hardened negative tests:

```sh
python3 computational/segmented_451.py 50
python3 -O computational/test_451.py
```

`test_451.py` cross-checks modular jumping, direct scanning, and segmented
block marking through $k=50$, and confirms that a forged certificate with a
fractional multiplier is rejected even when Python assertions are disabled.

The optional anchored Fourier falsification experiment is reproduced by:

```sh
python3 computational/fourier_discrepancy.py \
  --ks 5,10,20,40,80 --H 10000 --order 4 \
  --search-limit 100000 --detail-k 80 --top-modes 10 \
  > computational/fourier_output.tsv
```

The recorded run completed in 0.95 seconds.  Its internal assertions check
the residue formulation, local Fourier inversion, conjugate cancellation,
and agreement between the singleton Fourier contribution and direct counting.
The output is diagnostic evidence only.
