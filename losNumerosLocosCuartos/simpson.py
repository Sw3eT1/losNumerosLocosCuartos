import numpy as np
from math import exp

def simpson_weighted(f, a, b, n):
    if n % 2 == 1: n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = [f(xi)*exp(-xi) for xi in x]
    S = fx[0] + fx[-1] + 4*sum(fx[1:-1:2]) + 2*sum(fx[2:-2:2])
    return h * S / 3, list(x)

def simpson_infinite(f, tol, delta=1.0):
    total = 0.0
    a = 0.0
    all_nodes = []
    prev_total = None

    while True:
        part, nodes = simpson_weighted(f, a, a + delta, 10)
        all_nodes.extend(nodes)
        total += part

        if prev_total is not None and abs(total - prev_total) < tol:
            break

        prev_total = total
        a += delta

    return total, all_nodes
