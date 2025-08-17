from fractions import Fraction


def arctan(x):
    sum = x
    k = 0
    T = x
    while True:
        k += 1
        T = -(x**2) * T
        add_to_sum = Fraction(T, (2 * k + 1))
        sum += add_to_sum
        if abs(add_to_sum) < Fraction(1, 10**1000):
            break
    return sum  # final sum


pi = 4 * (arctan(Fraction(1, 2)) + arctan(Fraction(1, 3)))

print(str(int((10**1000) * (pi - int(pi))))[910:926])
