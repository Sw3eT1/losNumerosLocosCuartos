import numpy as np
import matplotlib.pyplot as plt
from math import exp

def rysuj_calkowanie(f, simpson_nodes, gauss_nodes, przedzial=(0, 10), n_points=1000):
    x_min, x_max = przedzial
    x = np.linspace(x_min, x_max, n_points)
    y_weighted = [f(xi) * exp(-xi) for xi in x]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y_weighted, label=r"$e^{-x} \cdot f(x)$", color="black", linewidth=2)

    # Filtruj węzły do przedziału rysowania
    simpson_x = [xi for xi in simpson_nodes if x_min <= xi <= x_max]
    simpson_y = [f(xi) * exp(-xi) for xi in simpson_x]
    ax.scatter(simpson_x, simpson_y, color="blue", zorder=5, label="Węzły Simpsona")
    ax.fill_between(simpson_x, simpson_y, color="blue", alpha=0.2)

    gauss_x = [xi for xi in gauss_nodes if x_min <= xi <= x_max]
    gauss_y = [f(xi) * exp(-xi) for xi in gauss_x]
    ax.scatter(gauss_x, gauss_y, color="green", marker="x", zorder=5, label="Węzły Gaussa-Laguerre")
    ax.fill_between(gauss_x, gauss_y, color="green", alpha=0.2)

    ax.set_title("Porównanie całkowania: Simpson vs Gauss-Laguerre")
    ax.set_xlabel("x")
    ax.set_ylabel(r"$e^{-x} \cdot f(x)$")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
