import numpy as np


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def newtons_backward_interpolation(x_values, y_values, x_target):
    n = len(x_values)

    difference_table = np.zeros((n, n))
    difference_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            difference_table[i][j] = (
                difference_table[i][j - 1] - difference_table[i - 1][j - 1]
            )

    print("\nDifference Table (Backward):")
    for i in range(n):
        print(f"x = {x_values[i]:.8f}", end="\t")
        for j in range(i + 1):
            print(f"{difference_table[i][j]:.8f}", end="\t")
        print()

    h = x_values[1] - x_values[0]

    p = (x_target - x_values[-1]) / h
    interpolated_value = y_values[-1]
    p_term = 1

    for i in range(1, n):
        p_term *= p + (i - 1)
        term = (difference_table[n - 1][i]) / factorial(i)
        interpolated_value += p_term * term

    return f"{interpolated_value:.8f}"


def newtons_backward_polynomial(x_values, y_values):
    n = len(x_values)
    difference_table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            difference_table[i][j] = (
                difference_table[i][j - 1] - difference_table[i - 1][j - 1]
            )

    h = x_values[1] - x_values[0]
    polynomial = f"{y_values[-1]}"

    p_term = ""
    for i in range(1, n):
        p_term += f"(x - {x_values[-1]})" if i == 1 else f" * (x - {x_values[-i]})"
        term = (difference_table[n - 1][i]) / (factorial(i) * (h**i))
        polynomial += f" + {term} * {p_term}"

    return polynomial


if __name__ == "__main__":
    x = [1, 3, 5, 7]
    y = [24, 120, 336, 720]
    x_to_find = 8

    result = newtons_backward_interpolation(x, y, x_to_find)
    print(f"\nInterpolated value at x = {x_to_find} (Backward): {result}")
    polynomial = newtons_backward_polynomial(x, y)
    print(f"\nNewton's Backward Interpolation Polynomial: {polynomial}")
