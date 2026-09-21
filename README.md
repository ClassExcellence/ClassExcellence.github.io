# Linear algebra from scratch

Implementations of the core algorithms of linear algebra, written in pure Python
with **no NumPy and no library calls** — every routine builds on the ones below it.

I wrote these as a first-year mathematics student at the Université libre de
Bruxelles. The point was never to have a fast library; `numpy.linalg` already
exists and is better. The point was that I did not want to call `solve()` on a
system without knowing what happens inside it. So I implemented the row
operations, then elimination on top of them, then the permutation machinery that
the determinant needs.

The comments are in French, as they were when I wrote them.

## What is implemented

**Row operations** — the primitives everything else is built from.

| File | What it does |
|---|---|
| `rescale_row.py` | Multiplies a row by a scalar |
| `add_alpha_row_j_to_row_i.py` | Adds a multiple of one row to another |
| `swap_line_of_matrix.py` | Exchanges two rows |
| `renormalize.py` | Normalises pivots |
| `add lines.py` | Row addition |

**Elimination**

| File | What it does |
|---|---|
| `GAUSS ELIMINATION.py` | Gaussian elimination: reduces an augmented matrix by repeated row operations and solves the system |

**Permutations** — needed for determinants and the sign of a permutation.

| File | What it does |
|---|---|
| `my_permute.py` | Applies a permutation |
| `my_sign_perm.py` | Sign (parity) of a permutation |
| `my_cycles_perm.py` | Decomposition into disjoint cycles |
| `my_magic.py` | The major index: the sum of the positions where the permutation descends |

**Matrix utilities**

| File | What it does |
|---|---|
| `my_add_I_to_matrix.py` | Augments a matrix with the identity (the setup for inversion by elimination) |
| `my_extract_right_matrix.py` | Extracts the right-hand block after elimination — the inverse |

## Also in this repository

Gram–Schmidt orthogonalisation and QR decomposition, and eigenvalue and
diagonalisation routines.

## Running it

Python 3, no dependencies:

```bash
python3 gaussian_elimination.py
```

Each file ends with a small worked example so it can be run on its own.

## A note on the name "magic"

`my_magic` computes what is called the **major index** of a permutation,
written maj(σ): the sum of all positions *i* where σ(i) > σ(i+1). I did not
know the standard name when I wrote it.
