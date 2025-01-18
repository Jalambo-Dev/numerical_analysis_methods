import numpy as np


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def newtons_forward_interpolation(x_values, y_values, x_target):
    n = len(x_values)

    difference_table = np.zeros((n, n))
    difference_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            difference_table[i][j] = (
                difference_table[i + 1][j - 1] - difference_table[i][j - 1]
            )

    print("\nDifference Table:")
    for i in range(n):
        print(f"x = {x_values[i]:.8f}", end="\t")
        for j in range(n - i):
            print(f"{difference_table[i][j]:.8f}", end="\t")
        print()

    h = x_values[1] - x_values[0]

    p = (x_target - x_values[0]) / h
    interpolated_value = y_values[0]
    p_term = 1

    for i in range(1, n):
        p_term *= p - (i - 1)
        term = (difference_table[0][i]) / factorial(i)
        interpolated_value += p_term * term

    return f"{interpolated_value:.8f}"


def newtons_forward_polynomial(x_values, y_values):
    n = len(x_values)
    difference_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            difference_table[i][j] = (
                difference_table[i + 1][j - 1] - difference_table[i][j - 1]
            )

    h = x_values[1] - x_values[0]
    polynomial = f"{y_values[0]}"

    p_term = ""
    for i in range(1, n):
        p_term += f"(x - {x_values[0]})" if i == 1 else f" * (x - {x_values[i-1]})"
        term = (difference_table[0][i]) / (factorial(i) * (h**i))
        polynomial += f" + {term} * {p_term}"

    return polynomial


if __name__ == "__main__":
    x = [3, 4, 5, 6]
    y = [13, 21, 31, 43]
    x_to_find = 10

    result = newtons_forward_interpolation(x, y, x_to_find)
    print(f"\nInterpolated value at x = {x_to_find}: {result}")
    polynomial = newtons_forward_polynomial(x, y)
    print(f"\nNewton's Forward Interpolation Polynomial: {polynomial}")
