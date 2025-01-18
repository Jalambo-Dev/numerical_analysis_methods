import numpy as np


def gauss_forward_central_difference(x, y, value):
    n = len(x)
    delta = np.zeros((n, n))
    delta[:, 0] = y

    # Construct the difference table
    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    # Display the difference table
    print("Difference Table:")
    for i in range(n):
        print(f"{x[i]:.2f}", end="\t")
        for j in range(n - i):
            print(f"{delta[i, j]:.4f}", end="\t")
        print()

    # Calculate the interpolated value
    p = (value - x[n // 2]) / (x[1] - x[0])
    result = delta[n // 2, 0]
    u_term = p
    fact = 1
    for i in range(1, n):
        if i % 2 == 1:
            result += u_term * delta[n // 2 - (i // 2)][i]
        else:
            result += u_term * delta[n // 2 - (i // 2)][i]
        fact *= i
        u_term *= (p**2 - (i // 2) ** 2) / fact

    # Construct the polynomial equation
    polynomial = f"{delta[n // 2, 0]:.4f}"
    u_term = p
    fact = 1
    for i in range(1, n):
        term = f"{delta[n // 2 - (i // 2)][i]:.4f}"
        if i % 2 == 1:
            polynomial += f" + {term}*u"
        else:
            polynomial += f" + {term}*u^2"
        fact *= i
        u_term *= (p**2 - (i // 2) ** 2) / fact

    print(f"Polynomial Equation: {polynomial}")

    return result, delta


# Example usage
x = [0, 4, 8, 12, 16]
y = [14, 24, 32, 35, 40]
value = 9

result, delta = gauss_forward_central_difference(x, y, value)
print(f"The interpolated value at {value} is {result:.8f}")

print()
