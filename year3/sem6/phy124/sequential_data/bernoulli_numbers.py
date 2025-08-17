from fractions import Fraction


def compute_factorials(n):
    factorials = [1] * (n + 1)
    for i in range(1, n + 1):
        factorials[i] = Fraction(factorials[i - 1] * i, 1)
    return factorials


def bernoulli_numbers(n):
    factorials = compute_factorials(n + 1)
    B = [Fraction(0, 1)] * (n + 1)
    B[0] = Fraction(1, 1)  # B_0
    for i in range(1, n + 1):  # Update B_i for i = 1, 2, ... , n
        formula = 0
        # Iterate up to i (from 0 until n-1 included): this performs the sum
        for k in range(i):
            formula += (factorials[i] * B[k]) / (factorials[k] * factorials[i - k + 1])
        B[i] = -formula
    return B[-1]


print(bernoulli_numbers(56))
