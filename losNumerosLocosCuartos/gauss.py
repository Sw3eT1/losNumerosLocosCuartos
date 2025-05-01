from scipy.special import roots_laguerre

def gauss_laguerre(f, n):
    nodes, weights = roots_laguerre(n)
    value = sum(w * f(x) for x, w in zip(nodes, weights))
    return value, list(nodes)

def gauss_laguerre_iterated(f, tol):
    prev = None
    all_nodes = []

    for n in range(2, 6):
        val, nodes = gauss_laguerre(f, n)
        all_nodes.extend(nodes)

        if prev is not None and abs(val - prev) < tol:
            return val, all_nodes

        prev = val

    return val, all_nodes
