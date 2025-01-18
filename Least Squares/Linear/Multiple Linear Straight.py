import numpy as np
import pandas as pd

pd.set_option("display.float_format", lambda x: "{:.10f}".format(x))

# Data points: (X, Y, Z)
data = [(0, 0, 2), (1, 1, 4), (2, 3, 3), (4, 2, 16), (6, 8, 8)]

# Extract X, Y, Z values
X = np.array([point[0] for point in data])
Y = np.array([point[1] for point in data])
Z = np.array([point[2] for point in data])

# Number of data points
n = len(data)

# Compute intermediate values
X2 = X**2
Y2 = Y**2
XY = X * Y
XZ = X * Z
YZ = Y * Z

# Create a table of values
data_table = pd.DataFrame(
    {"X": X, "Y": Y, "Z": Z, "X^2": X2, "Y^2": Y2, "XY": XY, "XZ": XZ, "YZ": YZ}
)

# Calculate sums and add them as a new row
sums = data_table.sum()
data_table.loc["Sum"] = sums

# Extract sums for calculations
sum_X = sums["X"]
sum_Y = sums["Y"]
sum_Z = sums["Z"]
sum_X2 = sums["X^2"]
sum_Y2 = sums["Y^2"]
sum_XY = sums["XY"]
sum_XZ = sums["XZ"]
sum_YZ = sums["YZ"]

# Create matrix A
A = np.array([[n, sum_X, sum_Y], [sum_X, sum_X2, sum_XY], [sum_Y, sum_XY, sum_Y2]])

# Create vector B
B = np.array([sum_Z, sum_XZ, sum_YZ])

# Solve for coefficients [a0, a1, a2]
coefficients = np.linalg.solve(A, B)
a0, a1, a2 = coefficients

# Print the table with sums included
print("\nData Table:")
print(data_table)

# Print results
print("\nResults:")
print(f"a0 = {a0:.10f}")
print(f"a1 = {a1:.10f}")
print(f"a2 = {a2:.10f}")
print(f"\nEquation of the plane: Z = {a0:.10f} + {a1:.10f}X + {a2:.10f}Y")

# Calculate fitted Z values
Z_fitted = a0 + a1 * X + a2 * Y

# Print the original and fitted values
print("\nOriginal Z values:")
for val in Z:
    print(f"{val:.10f}", end=" ")
print("\nFitted Z values:")
for val in Z_fitted:
    print(f"{val:.10f}", end=" ")
