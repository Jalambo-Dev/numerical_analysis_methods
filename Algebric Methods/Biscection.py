from cmath import e, pi
from math import sin, cos, exp, log


# Define the function you want to find the root of
def f(x):
    return 4 * exp(-x) * sin(x) - 1  # Example function; replace with any other function


# Input parameters
a = 0  # Starting point of the interval
b = 0.5  # Ending point of the interval
tolerance = 1e-3  # Desired accuracy


# Bisection method function to find the root
def bisection_method(f, a, b, tol=1e-3):
    # Ensure f(a) and f(b) have opposite signs
    print(
        f"Initial interval:\n\ta = {a}, f(a) = {f(a)}\n\tb = {b}, f(b) = {f(b)}\nThere's at least one root in the interval [{a},{b}]; 𝑓(a) and f(b) have opposite signs"
    )

    if f(a) * f(b) >= 0:
        return f"Invalid interval; f(a) = f({a}) and f(b) = f({b}) must have opposite signs."

    iteration = 1  # Step counter for iteration
    # Iterate until the desired tolerance is met
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        f_mid = f(midpoint)

        # Print current step information
        print(
            f"Iteration {iteration}, interval [{a}, {b}]:\n a = {a}, b = {b}, midpoint = {midpoint:.11f}, f(midpoint) = {f_mid:.11f}"
        )

        # Check if midpoint is close enough to the root
        if abs(f_mid) < tol:
            return round(midpoint, 3)

        # Narrow down the interval based on the sign
        if f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint

        iteration += 1

    # Return the midpoint as the approximate root
    return round((a + b) / 2, 3)


# Find the root
root = bisection_method(f, a, b, tolerance)
print("The root is approximately:", root)
