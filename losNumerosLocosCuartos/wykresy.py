import numpy as np
import matplotlib.pyplot as plt
from math import exp
import matplotlib.cm as cm


def rysuj_calkowanie(f, simpson_nodes, gauss_nodes_list, przedzial=(0, 10), n_points=1000):
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

    # Kolory dla węzłów Gaussa-Laguerre w zależności od liczby węzłów
    color_map = cm.get_cmap("viridis", len(gauss_nodes_list))  # Możesz zmienić na inną paletę, np. "plasma", "inferno"

    # Teraz przechodzimy przez listę węzłów Gaussa-Laguerre i rysujemy je
    for i, gauss_nodes in enumerate(gauss_nodes_list):
        # Sortowanie węzłów, by były uporządkowane
        gauss_nodes_sorted = sorted(gauss_nodes)

        # Filtruj węzły do przedziału rysowania
        gauss_x = [xi for xi in gauss_nodes_sorted if x_min <= xi <= x_max]
        gauss_y = [f(xi) * exp(-xi) for xi in gauss_x]

        # Przypisujemy kolor na podstawie indeksu gauss_nodes
        color = color_map(i)

        # Połącz punkty Gaussa, używając plt.plot() i rysuj linię
        ax.plot(gauss_x, gauss_y, color=color, marker="x", zorder=5,
                label=f"Węzły Gaussa-Laguerre (n={len(gauss_nodes_sorted)})")
        ax.fill_between(gauss_x, gauss_y, color=color, alpha=0.2)

    ax.set_title("Porównanie całkowania: Simpson vs Gauss-Laguerre")
    ax.set_xlabel("x")
    ax.set_ylabel(r"$e^{-x} \cdot f(x)$")

    # Używamy set() do uniknięcia powtórzeń w legendzie
    handles, labels = ax.get_legend_handles_labels()
    unique_handles_labels = list(zip(*sorted(zip(handles, labels), key=lambda x: x[1])))
    ax.legend(*unique_handles_labels)

    ax.grid(True)
    plt.tight_layout()
    plt.show()
