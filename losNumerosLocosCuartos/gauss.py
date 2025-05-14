from scipy.special import roots_laguerre

def gauss_laguerre(f, n):
    nodes, weights = roots_laguerre(n)
    value = sum(w * f(x) for x, w in zip(nodes, weights))
    return value, list(nodes)

def gauss_laguerre_multiple_n_with_tol(f, n_values, tol):
    results = {}
    nodes_list = []  # Lista do przechowywania węzłów dla wszystkich n

    prev_val = None

    for n in n_values:
        val, nodes = gauss_laguerre(f, n)
        print(f"Wynik całkowania Gauss-Laguerre dla n={n}: {val:.10f}")
        results[n] = (val, nodes)
        nodes_list.append(nodes)  # Dodanie węzłów do listy

        if prev_val is not None and abs(val - prev_val) < tol:
            print(f"Osiągnięto dokładność {tol} dla n={n}. Zatrzymuję dalsze liczenie.")
            break

        prev_val = val

    return results, nodes_list  # Zwrócenie wyników oraz listy węzłów
