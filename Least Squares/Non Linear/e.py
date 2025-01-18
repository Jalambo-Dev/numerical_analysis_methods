import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

pd.set_option("display.float_format", lambda x: "{:.8f}".format(x))


#!! Define the function y = a * e^(b * x)
def model_function(x, a, b):
    return a * np.exp(b * x) 

# TODO
# Data points
x_data = np.array([1.0, 3.0, 5.0, 7.0, 9.0])
y_data = np.array([2.473, 6.722, 18.274, 49.673, 135.026])

# Transform y_data to ln(y_data)
ln_y_data = np.log(y_data)

# Use curve_fit to find the best-fit parameters
params, covariance = curve_fit(model_function, x_data, y_data)

# Extract the parameters a and b
a, b = params
ln_a = np.log(a)  # Calculate ln(a)

# Calculate additional columns for the table
x_squared = x_data**2
xy = x_data * ln_y_data

# Create a table of values
data_table = pd.DataFrame(
    {
        "X": x_data,
        "Y": y_data,
        "ln(Y)": ln_y_data,
        "X^2": x_squared,
        "XY": xy,
    }
)

# Calculate sums and add them as a new row
sums = data_table.sum()
data_table.loc["Sum"] = sums

# Calculate A0 and A1
n = len(x_data)
sum_x = sums["X"]
sum_y = sums["ln(Y)"]
sum_xy = sums["XY"]
sum_x2 = sums["X^2"]

A1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
A0 = (sum_y - A1 * sum_x) / n

# Print the results with 10 decimal places
print(f"The best-fit parameters are:")
print(f"a = {a:.8f}")
print(f"b = {b:.8f}")
# print(f"ln(a) = {ln_a:.8f}")
print(f"A0 = {A0:.8f}")
print(f"A1 = {A1:.8f}")

# Print the table with sums included
print("\nData Table:")
print(data_table)

# Test the model with the fitted parameters
y_fitted = model_function(x_data, a, b)

# Print the original and fitted values with 10 decimal places
print("\nOriginal y values:")
for val in y_data:
    print(f"{val:.8f}", end=" ")
print("\nFitted y values:")
for val in y_fitted:
    print(f"{val:.8f}", end=" ")
