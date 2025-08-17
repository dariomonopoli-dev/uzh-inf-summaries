def newton_method(f, x0, f_prime=None, tolerance=1e-10, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)

        if f_prime:
            fpx = f_prime(x)
        else:
            h = 1e-6
            fpx = (f(x + h) - f(x)) / (h)

        if fpx == 0:
            raise ValueError(
                "Derivative is zero. No solution found."
            )  # Avoid division by zero in the next step

        next_x = x - fx / fpx  # formula for newton method
        if abs(next_x - x) < tolerance:
            return round(
                next_x, 10
            )  # Return the value rounded to 10 decimal places, converging to the tolerance
        x = next_x

    raise RuntimeError("Maximum iterations reached. No convergence.")


def func(x):
    return x**3 + x - 81


def derivative_func(x):
    return 3 * x**2 + 1


initial_guess = 4
root = newton_method(func, initial_guess, f_prime=derivative_func)
print(root)


# Solution: 4.2497168558
