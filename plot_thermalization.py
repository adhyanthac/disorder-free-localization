import numpy as np
import matplotlib.pyplot as plt


# ----- DATA: replace this section when your teammate provides real values -----

# Temporary data illustrating relaxation toward zero.
# These are synthetic values, not quantum-circuit results.
rng = np.random.default_rng(42) # 42 is a seed for reproducibility.

circuit_depths = np.arange(0, 51) # creates an array of integers from 0 to 50 (circuit depths)
expectation_values = np.exp(-circuit_depths / 10) 
expectation_values += rng.normal(0, 0.025, len(circuit_depths)) # adds small random noise to the expectation values

# Pauli-Z expectation values must lie between -1 and +1.
expectation_values = np.clip(expectation_values, -1, 1) # clips the expectation values to ensure they are within the range [-1, 1]
expectation_values[0] = 1.0 # The expectation value at depth 0 is set to 1.0, representing the initial state of the system.

using_placeholder_data = True


# ----- PLOTTING: keep this section when replacing the data -----

def plot_expectation_values(depths, values, placeholder=True):
    depths = np.asarray(depths, dtype=float)
    values = np.asarray(values, dtype=float)

    if depths.ndim != 1 or values.ndim != 1:
        raise ValueError("Depths and expectation values must be 1D arrays.")

    if len(depths) == 0 or len(depths) != len(values):
        raise ValueError("Provide the same nonzero number of depths and values.")

    if not np.all(np.isfinite(depths)) or not np.all(np.isfinite(values)):
        raise ValueError("All data must contain finite numbers.")

    if np.any(depths < 0):
        raise ValueError("Circuit depths cannot be negative.")

    if np.any((values < -1) | (values > 1)):
        raise ValueError("Pauli-Z expectation values must be between -1 and 1.")

    # Arrange points in increasing circuit-depth order.
    order = np.argsort(depths)
    depths = depths[order]
    values = values[order]

    fig, ax = plt.subplots(figsize=(9, 5)) # creates a graph and a set of subplots with a specified size

    # --- This is all graph styling and labeling, not quantum-circuit code. ---
    # Draws data points and connects them with lines
    ax.plot(
        depths,
        values,
        color="#0099AB",
        linewidth=2,
        marker="o",
        markersize=4,
        label="Synthetic placeholder data" if placeholder else "Circuit data",
    )

    ax.axhline(0, color="gray", linestyle="--", linewidth=1)

    ax.set_xlabel("Circuit depth", fontsize=12)
    ax.set_ylabel(
        r"Pauli-$Z$ expectation value $\langle Z\rangle$",
        fontsize=12,
    )
    ax.set_title(
        "Illustrative Relaxation — Placeholder Data"
        if placeholder
        else "Pauli-Z Expectation Value vs. Circuit Depth"
    )

    ax.set_ylim(-1.05, 1.05)
    ax.grid(alpha=0.25)
    ax.legend()

    fig.tight_layout()
    fig.savefig("thermalization_plot.png", dpi=300, bbox_inches="tight")
    plt.show()


# Runs the plotting function if this script is executed directly.
if __name__ == "__main__":
    plot_expectation_values(
        circuit_depths,
        expectation_values,
        placeholder=using_placeholder_data,
    )