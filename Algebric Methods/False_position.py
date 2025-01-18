from decimal import Decimal, getcontext
import math

# Set high precision for calculations
getcontext().prec = 15


def convert_to_decimal(value):
    """Convert input to Decimal with high precision"""
    return Decimal(str(value))


# Define the function to find the root of
def f(x):
    """Example function: x^3.4 + 7*x^0.25 - 1200"""
    return (
        (x ** convert_to_decimal("3.4"))
        + (7 * (x ** convert_to_decimal("0.25")))
        - convert_to_decimal("1200")
    )


# Input parameters with Decimal conversion
a = convert_to_decimal("8")  # Starting point of the interval
b = convert_to_decimal("9")  # Ending point of the interval
tolerance = convert_to_decimal("1e-6")  # Desired accuracy


def regula_falsi(f, a, b, tol=convert_to_decimal("1e-3")):
    """Regula-Falsi (False Position) method to find the root with Decimal precision"""
    # Ensure f(a) and f(b) have opposite signs
    print(f"Initial interval:\n\ta = {a}, f(a) = {f(a)}\n\tb = {b}, f(b) = {f(b)}")

    if f(a) * f(b) >= 0:
        return f"Invalid interval; f(a) and f(b) must have opposite signs."

    iteration = 1  # Step counter for iteration

    while True:
        # Calculate the point using Regula-Falsi formula
        numerator = f(b) * (b - a)
        denominator = f(b) - f(a)

        # Avoid division by zero
        if denominator == 0:
            raise ValueError("Denominator became zero during calculation")

        x_new = b - (numerator / denominator)
        f_x_new = f(x_new)

        # Print current step information with high precision
        print(f"Iteration {iteration}:")
        print(f"\ta = {a}, f(a) = {f(a)}")
        print(f"\tb = {b}, f(b) = {f(b)}")
        print(f"\tx_{iteration} = {x_new}, f(x_{iteration}) = {f_x_new}")

        # Check if x_new is close enough to the root
        if abs(f_x_new) < tol:
            return x_new

        # Update the interval based on the sign of f(x_new)
        if f(a) * f_x_new < 0:
            b = x_new
        else:
            a = x_new

        iteration += 1


# Find the root
try:
    root = regula_falsi(f, a, b, tolerance)
    print("\nThe root is approximately:", root)

except Exception as e:
    print(f"An error occurred: {e}")
