import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data points (x, y)
x_data = np.array([1, 2, 4, 5])
y_data = np.array([7, 19, 67, 103])

# Compute required columns
x2 = x_data**2
x3 = x_data**3
x4 = x_data**4
xy = x_data * y_data
x2y = x2 * y_data

# Create a DataFrame for the table
data = {
    "x": x_data,
    "y": y_data,
    "x^2": x2,
    "x^3": x3,
    "x^4": x4,
    "xy": xy,
    "x^2y": x2y,
}

df = pd.DataFrame(data)

# Add sums row
sums = {
    "x": np.sum(x_data),
    "y": np.sum(y_data),
    "x^2": np.sum(x2),
    "x^3": np.sum(x3),
    "x^4": np.sum(x4),
    "xy": np.sum(xy),
    "x^2y": np.sum(x2y),
}

df.loc["Sum"] = sums

# Print the table with values and sums
print(df)

# Fit a second-degree polynomial (parabola) to the data
coefficients = np.polyfit(x_data, y_data, 2)

# Coefficients a0, a1, a2
a2, a1, a0 = coefficients

print(f"\nFitted coefficients: a0 = {a0:.4f}, a1 = {a1:.4f}, a2 = {a2:.4f}")

# Generate x values for plotting the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)

# Calculate the corresponding y values from the fitted polynomial
# y_fit = a0 + a1 * x_fit + a2 * x_fit**2

# Plot the data points and the fitted curve
# plt.scatter(x_data, y_data, color="red", label="Data points")
# plt.plot(
#     x_fit,
#     y_fit,
#     label=f"Fitted parabola: $y = {a0:.2f} + {a1:.2f}x + {a2:.2f}x^2$",
#     color="blue",
# )
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.grid(True)
# plt.title("Second Degree Parabola Fit")
# plt.show()
