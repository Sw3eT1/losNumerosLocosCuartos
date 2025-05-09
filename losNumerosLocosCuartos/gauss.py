from scipy.special import roots_laguerre

def gauss_laguerre(f, n):
    nodes, weights = roots_laguerre(n)
    value = sum(w * f(x) for x, w in zip(nodes, weights))
    return value, list(nodes)

def gauss_laguerre_iterated(f, tol, max_n=5):
    prev = None
    all_nodes = []

    for n in range(2, max_n + 1):
        val, nodes = gauss_laguerre(f, n)
        print(f"Gauss nodes for n={n}: {nodes}")
        all_nodes.extend(nodes)

        if prev is not None and abs(val - prev) < tol:
            return val, all_nodes

        prev = val

    return val, all_nodes
