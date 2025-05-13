import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

def rysuj_calkowanie(f, a,b,n_points=1001):  # nieparzysta liczba punktów
    x_min, x_max = (a,b)
    x = np.linspace(x_min, x_max, n_points)
    fx = f(x)

    # Całkowanie od x[0] do x[i] w sposób zoptymalizowany
    F = np.array([simpson(fx[:i+1], x[:i+1]) if i >= 2 else 0 for i in range(len(x))])

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, F, label=r"$F(x) = \int f(x)\,dx$", color="darkred", linewidth=2)

    ax.set_title("Zcałkowana funkcja pierwotna (metoda Simpsona)")
    ax.set_xlabel("x")
    ax.set_ylabel(r"$F(x)$")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
