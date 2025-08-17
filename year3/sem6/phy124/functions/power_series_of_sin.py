from math import pi


def f1(n):
    return (-1) ** n


def f2(n):
    return 2 * n + 1


def f3(x, n):
    return x**n


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def sin(x):
    res = 0
    n = 0
    while True:
        formula = (f1(n) * f3(x, f2(n))) / factorial(f2(n))
        res += formula
        n += 1

        if abs(formula) < 1e-08:
            return res


print(sin(pi / 7))

# Don't we need to specify the number of iterations as a function parameter? Here I supposed it to be 10
# Output of this code: 0.43388374
