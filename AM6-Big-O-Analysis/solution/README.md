# Big-O analysis reference

Use this separate key after an independent attempt at the starter worksheet.
The following bounds use its explicit positive-input, independent-variable model.
Theta describes tight growth and therefore implies the corresponding O bound.

### P1: 12n^2 + n

Theta(n^2). The quadratic term dominates the linear term; its constant coefficient does not change growth.

### P2: n - sqrt(n) + 0

Theta(n). The square-root term grows more slowly than n. For sufficiently large n, subtraction still leaves growth proportional to n.

### P3: 11,000,000n + 5

Theta(n). A fixed multiplier and a fixed additive constant do not change linear growth.

### P4: 1,000,000n - 1,000,000

Theta(n). For sufficiently large n the linear term dominates the subtracted constant.

### P5: 1,234,567 + 6 - 5

Theta(1). No input size appears; the value is a fixed constant.

### P6: log_2(n) + 2

Theta(log n). The logarithm grows while the additive constant stays fixed; a fixed log base changes only a factor.

### P7: n + log_2(n)

Theta(n). The linear term dominates the logarithmic term.

### P8: 1 + 2 + ... + n

Theta(n^2). The sum is n(n+1)/2, whose dominant term is quadratic. This is growth of the expression, not the cost of evaluating a closed form.

### P9: 3 log_2(n) + m^2

Theta(log n + m^2). n and m are independent. Neither term can be discarded without an additional relationship between them.

### P10: T(n) = 1 + T(n/2), T(1) = 0; n = 2^k

Theta(log n). After k halvings the argument is 1, so T(n)=k=log_2(n). The base-case value is zero.

## Verification discussion

For P8, summing n values in a loop takes linear additions, while the value of
that sum grows quadratically. Evaluating its closed form takes a fixed number
of arithmetic operations in this introductory model; those are different
questions. For P10 with arbitrary integer sizes and floor-halving, count halvings
until the input reaches 1; the asymptotic class stays logarithmic.
