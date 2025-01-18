from math import e, log
from sympy import symbols, simplify, prod


def lagrange_interpolation(data_points, eval_at=None):
    """

    Compute the Lagrange interpolation polynomial for given data points

    and optionally evaluate it at a specific point.

    Parameters:

    - data_points: List of (x, f(x)) tuples.
    - eval_at: Point to evaluate the polynomial (optional).

    Returns:

    - A dictionary with:
      - 'polynomial': The symbolic Lagrange interpolation polynomial.
      - 'steps': Detailed step-by-step computation as a string.
      - 'evaluation': The value of the polynomial at eval_at (if provided).
    """

    x = symbols("x")
    n = len(data_points)

    P_x = 0  # Initialize the polynomial

    steps = []  # Store detailed steps as a list of strings

    steps.append("### Step-by-Step Construction of Lagrange Polynomial ###")

    for i, (xi, fxi) in enumerate(data_points):

        steps.append(f"\nStep {i + 1}: Constructing L_{i}(x)")

        steps.append(f"Data point: x_{i} = {xi:.8f}, f(x_{i}) = {fxi:.8f}")

        # Compute the Lagrange basis polynomial L_i(x)

        terms = []  # Store individual terms for clarity

        for j, (xj, _) in enumerate(data_points):

            if j != i:

                term = (x - xj) / (xi - xj)

                terms.append(term)

                steps.append(
                    f"  Term for j = {j}: (x - {xj:.8f}) / ({xi:.8f} - {xj:.8f}) = {term}"
                )

        # Multiply all terms to get L_i(x)

        L_i = prod(terms)

        L_i = simplify(L_i)  # Simplify L_i(x)

        steps.append(f"  L_{i}(x) (simplified) = {L_i}")

        # Add the term to the polynomial

        contribution = fxi * L_i

        P_x += contribution

        steps.append(
            f"  Contribution to P(x): f(x_{i}) * L_{i}(x) = {fxi:.8f} * {L_i} = {contribution}"
        )

    # Simplify the polynomial

    P_x = simplify(P_x)

    steps.append(f"\nLegrange's Interpolation Polynomial\nP(x) = {P_x}")

    result = {"polynomial": P_x, "steps": "\n".join(steps)}

    if eval_at is not None:

        # Evaluate the polynomial at the given point

        steps.append(f"\nEvaluation at x = {eval_at:.8f}")

        value = P_x.subs(x, eval_at)

        steps.append(f"P({eval_at:.8f}) = {value:.8f}")

        result["evaluation"] = value

    return result


# Example usage

if __name__ == "__main__":

    # Given data points

    data_points = [(1,1), (4, 256), (5,625)]

    # Point to evaluate

    eval_at = 2

    # Perform Lagrange interpolation

    result = lagrange_interpolation(data_points, eval_at=eval_at)

    # Output detailed steps

    print(result["steps"])

    # Output results

    if "evaluation" in result:
        print(f"f({eval_at:.8f}) = {result['evaluation']:.8f}")
