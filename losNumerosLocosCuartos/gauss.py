from scipy.special import roots_laguerre

def gauss_laguerre(f, n):
    nodes, weights = roots_laguerre(n)
    value = sum(w * f(x) for x, w in zip(nodes, weights))
    return value, list(nodes)

def gauss_laguerre_multiple_n_with_tol(f, n_values, tol):
    results = {}
    prev_val = None

    for n in n_values:
        val, nodes = gauss_laguerre(f, n)
        print(f"Wynik całkowania Gauss-Laguerre dla n={n}: {val:.10f}")
        results[n] = (val, nodes)

        if prev_val is not None and abs(val - prev_val) < tol:
            print(f"Osiągnięto dokładność {tol} dla n={n}. Zatrzymuję dalsze liczenie.")
            break

        prev_val = val

    return results
