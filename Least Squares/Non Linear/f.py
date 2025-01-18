import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

pd.set_option("display.float_format", lambda x: "{:.10f}".format(x))


#!! Define the function y = x/(a+bx)
def model_function(x, a, b):
    return x / (a + b * x)


# Data points
x_data = np.array([2, 5, 10, 20])
y_data = np.array([2, -1, -0.66666666, -0.57142857])

# For the linear transformation, we use 1/y = (a/x) + b
# This transforms to the form: 1/y = a(1/x) + b
y_reciprocal = 1 / y_data
x_reciprocal = 1 / x_data

# Calculate additional columns for the table
xy = x_reciprocal * y_reciprocal
x_squared = x_reciprocal**2

# Create a table of values
data_table = pd.DataFrame(
    {
        "x": x_data,
        "y": y_data,
        "X=1/x": x_reciprocal,
        "Y=1/y": y_reciprocal,
        "XY=(1/x)(1/y)": xy,
        "X^2=(1/x)^2": x_squared,
    }
)

# Calculate sums and add them as a new row
sums = data_table.sum()
data_table.loc["Sum"] = sums

# Calculate A0 and A1 using the transformed data
n = len(x_data)
sum_x = sums["X=1/x"]
sum_y = sums["Y=1/y"]
sum_xy = sums["XY=(1/x)(1/y)"]
sum_x2 = sums["X^2=(1/x)^2"]

A1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
A0 = (sum_y - A1 * sum_x) / n

# Use curve_fit to find the best-fit parameters
params, covariance = curve_fit(model_function, x_data, y_data)

# Extract the parameters a and b
a, b = params

# Print the results with 10 decimal places
print(f"The best-fit parameters are:")
print(f"a = {a:.10f}")
print(f"b = {b:.10f}")
print(f"A0 = {A0:.10f}")
print(f"A1 = {A1:.10f}")

# Print the table with sums included
print("\nData Table:")
print(data_table)

# Test the model with the fitted parameters
y_fitted = model_function(x_data, a, b)

# Print the original and fitted values with 10 decimal places
print("\nOriginal y values:")
for val in y_data:
    print(f"{val:.10f}", end=" ")
print("\nFitted y values:")
for val in y_fitted:
    print(f"{val:.10f}", end=" ")
