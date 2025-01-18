from math import log
from sympy import symbols, simplify


def divided_difference_table(x, y):
    """
    Create the divided difference table for backward differences.

    Args:
        x: List of x values.
        y: List of y values.

    Returns:
        2D list representing the divided difference table.
    """
    n = len(x)
    table = [[0] * n for _ in range(n)]

    # Fill the first column with y values
    for i in range(n):
        table[i][0] = y[i]

    # Fill the rest of the table
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table


def format_table(table):
    """
    Format the divided difference table for display.

    Args:
        table: 2D list representing the divided difference table.

    Returns:
        Formatted string representation of the table.
    """
    formatted = ""
    for row in table:
        formatted += (
            "\t".join(f"{value:.10f}" if value != 0 else "" for value in row) + "\n"
        )
    return formatted


def newtons_backward_polynomial(x_values, y_values, x):
    """
    Calculate f(x) using Newton's Backward Divided Difference Formula.

    Args:
        x_values: List of x values.
        y_values: List of y values.
        x: The value at which the polynomial is evaluated.

    Returns:
        The value of the polynomial at x and the polynomial representation.
    """
    n = len(x_values)
    table = divided_difference_table(x_values, y_values)

    # Extract the last row of coefficients for backward differences
    coefficients = [table[n - 1 - i][i] for i in range(n)]

    # Construct the polynomial as a symbolic expression
    x_sym = symbols("x")
    polynomial_expr = coefficients[0]
    product_term = 1

    # Use backward differences (starting from the last point)
    for i in range(1, n):
        product_term *= x_sym - x_values[n - i]
        polynomial_expr += coefficients[i] * product_term

    # Simplify the polynomial expression
    simplified_polynomial = simplify(polynomial_expr)

    # Evaluate the polynomial at x
    result = float(simplified_polynomial.subs(x_sym, x))

    return result, simplified_polynomial, table


# Example usage
if __name__ == "__main__":
    # TODO
    # Input values
    x_values = [-1, 0, 3, 6, 7]
    y_values = [3, -6, 39, 822, 1611]  # Corresponding y values for f(x)

    # Point to evaluate
    x = 5

    # Calculate f(x)
    result, polynomial, table = newtons_backward_polynomial(x_values, y_values, x)

    print("Divided Difference Table:")
    print(format_table(table))
    print(f"\nNewton Backward Polynomial (Simplified): {polynomial}")
    print(f"\nf({x}) = {result}")
