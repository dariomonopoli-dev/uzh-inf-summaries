def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def lowest_prime_divisor(n):
    if is_prime(n):
        return n
    i = 2
    while i <= n:  # iterate through all possible divisors from 2 to n
        if n % i == 0:
            return i
        i += 1


def conway_fib(N):
    f = [4, 3]
    for n in range(2, N + 1):
        next_num = f[n - 1] + f[n - 2]
        if is_prime(next_num):
            f.append(next_num)
        else:
            prime_divisor = lowest_prime_divisor(next_num)
            f.append(next_num // prime_divisor)
    return f


print("22th element:", conway_fib(22)[-1])
