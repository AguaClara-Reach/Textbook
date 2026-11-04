"""Plot residual-solids production and aluminum fraction versus turbidity."""

import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, NullFormatter


# Preliminary values from Residuals_Generation_and_Management.rst.
K_T_C = 0.001  # kg/(m^3 NTU)
Y_AL = 78 / 27  # kg Al(OH)3 per kg Al
D_DOM = 0.001  # kg Al/m^3
K_T_D = 0.001  # kg Al/(m^3 NTU^(1/3))

MIN_TURBIDITY = 1  # NTU; a logarithmic axis cannot include zero
MAX_TURBIDITY = 600  # NTU
NUMBER_OF_POINTS = 501
EXAMPLE_TURBIDITY = 50  # NTU


def calculate_solids_production(turbidity):
    """Return suspended-solids, coagulant, and total production in kg/m^3."""
    suspended_solids = K_T_C * turbidity
    aluminum_dose = D_DOM + K_T_D * turbidity ** (1 / 3)
    coagulant_solids = Y_AL * aluminum_dose
    total_solids = suspended_solids + coagulant_solids
    return suspended_solids, coagulant_solids, total_solids


def calculate_aluminum_mass_fraction(turbidity):
    """Return coagulant-derived elemental Al per mass of dry residual solids."""
    aluminum_dose = D_DOM + K_T_D * turbidity ** (1 / 3)
    _, _, total_solids = calculate_solids_production(turbidity)
    return aluminum_dose / total_solids


def format_decimal_tick(value, _position):
    """Format logarithmic major ticks as decimals rather than powers of ten."""
    if value == 0:
        return "0"
    return f"{value:.6f}".rstrip("0").rstrip(".")


def create_turbidity_values():
    """Return logarithmically spaced turbidity values over the plot range."""
    log_minimum = math.log10(MIN_TURBIDITY)
    log_maximum = math.log10(MAX_TURBIDITY)
    return [
        10
        ** (
            log_minimum
            + (log_maximum - log_minimum) * index / (NUMBER_OF_POINTS - 1)
        )
        for index in range(NUMBER_OF_POINTS)
    ]


def format_log_axes(axis, ylabel):
    """Apply the shared textbook formatting for logarithmic plots."""
    axis.set(
        xlim=(MIN_TURBIDITY, MAX_TURBIDITY),
        xlabel="Average raw-water turbidity (NTU)",
        ylabel=ylabel,
    )
    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_xticks([1, 10, 100, 600])
    axis.set_xticklabels(["1", "10", "100", "600"])
    axis.yaxis.set_major_formatter(FuncFormatter(format_decimal_tick))
    axis.grid(True, which="both", alpha=0.3)


def create_solids_production_figure():
    """Create and save the residual-solids production figure."""
    turbidity = create_turbidity_values()
    components = [calculate_solids_production(value) for value in turbidity]
    suspended_solids = [component[0] for component in components]
    coagulant_solids = [component[1] for component in components]
    total_solids = [component[2] for component in components]

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(
        turbidity,
        total_solids,
        linewidth=2.4,
        linestyle="--",
        label="Total solids",
    )
    axis.plot(
        turbidity,
        suspended_solids,
        linewidth=2.4,
        label="Raw water suspended solids",
    )
    axis.plot(
        turbidity,
        coagulant_solids,
        linewidth=2.4,
        label="Coagulant precipitate",
    )

    _, _, example_total = calculate_solids_production(EXAMPLE_TURBIDITY)
    axis.vlines(
        EXAMPLE_TURBIDITY,
        ymin=suspended_solids[0],
        ymax=example_total,
        color="black",
        linestyle=":",
        linewidth=1.8,
        zorder=4,
    )
    axis.hlines(
        example_total,
        xmin=MIN_TURBIDITY,
        xmax=EXAMPLE_TURBIDITY,
        color="black",
        linestyle=":",
        linewidth=1.8,
        zorder=4,
    )
    axis.plot(
        EXAMPLE_TURBIDITY,
        example_total,
        marker="o",
        markersize=6,
        color="black",
        zorder=5,
    )
    axis.annotate(
        f"50 NTU: $C_s$ = {example_total:.4f} kg/m³",
        xy=(EXAMPLE_TURBIDITY, example_total),
        xytext=(1.5, example_total * 1.15),
        fontsize=10,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.8},
    )
    format_log_axes(axis, "Solids production, $C_s$ (kg/m³)")
    axis.legend(frameon=False)
    figure.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "Images"
        / "residuals_solids_production.png"
    )
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    return output_path


def create_aluminum_mass_fraction_figure():
    """Create and save the residual-solids aluminum mass-fraction figure."""
    turbidity = create_turbidity_values()
    aluminum_mass_fraction = [
        calculate_aluminum_mass_fraction(value) for value in turbidity
    ]

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(
        turbidity,
        aluminum_mass_fraction,
        linewidth=2.4,
        label="Coagulant-derived elemental aluminum",
    )
    format_log_axes(
        axis,
        r"Aluminum mass fraction, $w_{\mathrm{Al,res}}$ (kg Al/kg dry solids)",
    )
    axis.set_yticks([0.02, 0.05, 0.1, 0.2, 0.3])
    axis.yaxis.set_major_formatter(FuncFormatter(format_decimal_tick))
    axis.yaxis.set_minor_formatter(NullFormatter())
    axis.legend(frameon=False)
    figure.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "Images"
        / "residuals_aluminum_mass_fraction.png"
    )
    figure.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    return output_path


if __name__ == "__main__":
    print(create_solids_production_figure())
    print(create_aluminum_mass_fraction_figure())
