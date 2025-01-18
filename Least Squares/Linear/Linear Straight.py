import math
import pandas as pd
import numpy as np

pd.set_option("display.float_format", lambda x: "{:.10f}".format(x))

# Data points
data = [(0, -1), (2, 5), (5, 12), (7, 20)]

# Extract X and Y values
X = [point[0] for point in data]
Y = [point[1] for point in data]

# Calculate intermediate values
X2 = [x**2 for x in X]
Y2 = [y**2 for y in Y]
XY = [x * y for x, y in zip(X, Y)]

# Create a table of values
data_table = pd.DataFrame({"X": X, "Y": Y, "X^2": X2, "Y^2": Y2, "XY": XY})

# Calculate sums and add them as a new row
sums = data_table.sum()
data_table.loc["Sum"] = sums

# Number of data points
n = len(data)

# Calculate parameters using sums
sum_X = sums["X"]
sum_Y = sums["Y"]
sum_XY = sums["XY"]
sum_X2 = sums["X^2"]
sum_Y2 = sums["Y^2"]

# Calculate a1 and a0
a1 = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X**2)
a0 = (sum_Y / n) - a1 * (sum_X / n)

# Calculate correlation coefficient
r = (n * sum_XY - sum_X * sum_Y) / math.sqrt(
    (n * sum_X2 - sum_X**2) * (n * sum_Y2 - sum_Y**2)
)

# Print the table with sums included
print("\nData Table:")
print(data_table)

# Print results
print("\nResults:")
print(f"a0 = {a0:.10f}")
print(f"a1 = {a1:.10f}")
print(f"r = {r:.10f}")
print(f"\nBest fit line: Y = {a0:.10f} + {a1:.10f}X")

# Calculate fitted Y values
Y_fitted = [a0 + a1 * x for x in X]

# Print the original and fitted values
print("\nOriginal y values:")
for val in Y:
    print(f"{val:.10f}", end=" ")
print("\nFitted y values:")
for val in Y_fitted:
    print(f"{val:.10f}", end=" ")
