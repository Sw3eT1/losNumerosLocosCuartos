import numpy as np
from math import exp

def simpson_weighted(f, a, b, n):
    if n % 2 == 1:
        n += 1
    deltaX = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = [f(xi) * exp(-xi) for xi in x]
    S = fx[0] + fx[-1] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2])
    return deltaX * S / 3, list(x)

def simpson_infinite(f, start, n_per_iter, tol, max_iter=100):
    total = 0.0
    all_nodes = []
    prev_total = None

    for i in range(max_iter):
        a = i * n_per_iter
        b = (i + 1) * n_per_iter
        part, nodes = simpson_weighted(f, a, b, n_per_iter)
        total += part
        all_nodes.extend(nodes)

        if prev_total is not None and abs(total - prev_total) < tol:
            break
        prev_total = total

    return total, all_nodes
