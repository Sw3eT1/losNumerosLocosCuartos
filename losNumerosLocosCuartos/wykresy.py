import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def rysuj_calkowanie(f, przedzial=(0, 10), n_points=1000):
    x_min, x_max = przedzial
    x = np.linspace(x_min, x_max, n_points)
    fx = f(x)

    # Obliczanie funkcji pierwotnej (całki) w każdym punkcie metodą Simpsona
    F = np.zeros_like(x)
    for i in range(2, len(x)):  # zaczynamy od 2 punktów, bo Simpson potrzebuje co najmniej 2
        F[i] = simpson(fx[:i+1], x[:i+1])

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, F, label=r"Zcałkowana funkcja $F(x) = \int f(x)\,dx$", color="darkred", linewidth=2)

    ax.set_title("Zcałkowana funkcja pierwotna (metoda Simpsona)")
    ax.set_xlabel("x")
    ax.set_ylabel(r"$F(x)$")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
