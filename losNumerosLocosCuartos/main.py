import numpy as np
from gauss import gauss_laguerre_multiple_n_with_tol
from simpson import simpson_infinite
from wykresy import rysuj_calkowanie

functions = {
    "1": ("x", lambda x: x),
    "2": ("x^2", lambda x: x**2),
    "3": ("sin(x)", lambda x: np.sin(x)),
    "4": ("cos(x)", lambda x: np.cos(x)),
    "5": ("e^(-x) * x^2", lambda x: np.exp(-x) * x**2)
}

# --- Wybór funkcji przez użytkownika ---
print("Wybierz funkcję do całkowania:")
for key, (desc, _) in functions.items():
    print(f"{key}: {desc}")

while True:
    choice = input("Twój wybór (1-5): ").strip()
    if choice in functions:
        desc, func = functions[choice]
        break
    print("Nieprawidłowy wybór. Spróbuj ponownie.")

# --- Parametry wejściowe ---
tol = float(input("Podaj żądaną dokładność (np. 0.0001): ").strip())
lower = float(input("Podaj dolną wartość przedziału do rysowania: ").strip())
upper = float(input("Podaj górną wartość przedziału do rysowania: ").strip())
n_rects = int(input("Podaj ilość podziału przedziałów (np. 3): ").strip())

# --- Simpson ---
print("\nObliczanie metodą Simpsona...")
simpson_result, simpson_nodes = simpson_infinite(func, n_rects, tol)
print(f"Wynik całkowania (Simpson): {simpson_result:.10f}")

# --- Gauss dla wielu n ---
print("\nObliczanie metodą Gaussa-Laguerre...")
gauss_n_values = [2, 3, 4, 5]
gauss_results,gauss_nodes = gauss_laguerre_multiple_n_with_tol(func, gauss_n_values, tol)

# Ostatni (najdokładniejszy) wynik do porównania i wykresu
gauss_final_n = max(gauss_results.keys())
gauss_final_val, gauss_final_nodes = gauss_results[gauss_final_n]
print(f"\nRóżnica między metodami: {abs(simpson_result - gauss_final_val):.10f}")
print(gauss_nodes)

# --- Wykres ---
print("\nRysowanie zcałkowanej funkcji pierwotnej...")
rysuj_calkowanie(func,simpson_nodes,gauss_nodes, przedzial=(lower, upper))