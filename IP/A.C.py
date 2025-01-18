from math import log
from sympy import symbols, simplify, expand


def aitkens_table(x, y, target_x):
    """
    Create the Aitken interpolation table.

    Args:
        x: List of x values.
        y: List of y values.
        target_x: The x value at which the interpolation is evaluated.

    Returns:
        2D list representing the Aitken table and the interpolated value.
    """
    n = len(x)
    table = [[0] * n for _ in range(n)]

    # Fill the first column with y values
    for i in range(n):
        table[i][0] = y[i]

    # Fill the table using Aitken's formula
    for j in range(1, n):
        for i in range(n - j):
            xi, xj = x[i], x[i + j]
            table[i][j] = (
                (target_x - xj) * table[i][j - 1]
                - (target_x - xi) * table[i + 1][j - 1]
            ) / (xi - xj)

    return table, table[0][n - 1]


def format_table(table):
    """
    Format the Aitken table for display.

    Args:
        table: 2D list representing the Aitken table.

    Returns:
        Formatted string representation of the table.
    """
    formatted = ""
    for row in table:
        formatted += (
            "\t".join(f"{value:.10f}" if value != 0 else "" for value in row) + "\n"
        )
    return formatted


def construct_lagrange_basis(x_values, i):
    """
    Construct the Lagrange basis polynomial for index i.
    """
    x = symbols("x")
    numerator = 1
    denominator = 1

    for j in range(len(x_values)):
        if j != i:
            numerator *= x - x_values[j]
            denominator *= x_values[i] - x_values[j]

    return numerator / denominator


def aitkens_interpolation(x_values, y_values, x):
    """
    Calculate f(x) using Aitken's interpolation scheme.

    Args:
        x_values: List of x values.
        y_values: List of y values.
        x: The value at which the interpolation is evaluated.

    Returns:
        The interpolated value at x, a simplified polynomial, and the Aitken table.
    """
    table, interpolated_value = aitkens_table(x_values, y_values, x)

    # Construct the interpolating polynomial using Lagrange form
    x_sym = symbols("x")
    polynomial_expr = 0

    for i in range(len(x_values)):
        basis = construct_lagrange_basis(x_values, i)
        polynomial_expr += y_values[i] * basis

    # Simplify and expand the polynomial
    simplified_polynomial = simplify(expand(polynomial_expr))

    return interpolated_value, simplified_polynomial, table


# Example usage
if __name__ == "__main__":
    # TODO
    # Input values
    x_values = [1, 2, 5, 10]
    y_values = [-19, -32, 25, 800]  # Corresponding y values for f(x)

    # Point to evaluate
    x = 6

    # Calculate f(x)
    result, polynomial, table = aitkens_interpolation(x_values, y_values, x)

    print("Aitken Table:")
    print(format_table(table))
    print(f"\nAitken Polynomial (Simplified): {polynomial}")
    print(f"\nf({x}) = {result}")
