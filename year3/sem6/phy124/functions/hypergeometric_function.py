def F(a, b, c, z, eps=1e-16):
    # Initialization step
    T = 1
    F = 1
    k = 1

    # Computation of series
    while abs(T) > eps:
        T *= ((a + (k - 1)) * (b + (k - 1))) / ((c + (k - 1)) * k) * z
        F += T
        k += 1

    return F


print("F(1, 1, 2, -0.211836) =", round(F(1, 1, 2, -0.211836), 6))

# Result is 0.907006
