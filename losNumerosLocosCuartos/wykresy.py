import numpy as np
import matplotlib.pyplot as plt
from math import exp

def rysuj_calkowanie(f, simpson_nodes, gauss_nodes, przedzial=(0, 10), n_points=1000):
    x = np.linspace(przedzial[0], przedzial[1], n_points)
    y = [f(xi) for xi in x]
    y_weighted = [f(xi) * exp(-xi) for xi in x]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Rysowanie funkcji ważonej
    ax.plot(x, y_weighted, label=r"$e^{-x} \cdot f(x)$", color="black", linewidth=2)

    # -- Simpson --
    simpson_x = np.array(simpson_nodes)
    simpson_y = [f(xi) * exp(-xi) for xi in simpson_x]
    ax.scatter(simpson_x, simpson_y, color="blue", zorder=5, label="Węzły Simpsona")
    ax.fill_between(simpson_x, simpson_y, color="blue", alpha=0.2, label="Obszar Simpsona")

    # -- Gauss-Laguerre --
    gauss_x = np.array(gauss_nodes)
    gauss_y = [f(xi) * exp(-xi) for xi in gauss_x]
    ax.scatter(gauss_x, gauss_y, color="green", marker="x", zorder=5, label="Węzły Gaussa-Laguerre")
    ax.fill_between(gauss_x, gauss_y, color="green", alpha=0.2, label="Obszar Gaussa")

    ax.set_title("Porównanie całkowania metodą Simpsona i Gaussa-Laguerre'a")
    ax.set_xlabel("x")
    ax.set_ylabel(r"$e^{-x} \cdot f(x)$")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
