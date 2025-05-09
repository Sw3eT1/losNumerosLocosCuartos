import numpy as np
from gauss import gauss_laguerre_iterated
from simpson import simpson_infinite
from wykresy import rysuj_calkowanie

functions = {
    "1": ("x", lambda x: x),
    "2": ("x^2", lambda x: x**2),
    "3": ("sin(x)", lambda x: np.sin(x)),
    "4": ("cos(x)", lambda x: np.cos(x)),
    "5": ("e^(-x) * x^2", lambda x: np.exp(-x) * x**2)
}

print("Wybierz funkcję do całkowania:")
for key, (desc, _) in functions.items():
    print(f"{key}: {desc}")

while True:
    choice = input("Twój wybór (1-5): ").strip()
    if choice in functions:
        desc, func = functions[choice]
        break
    print("Nieprawidłowy wybór. Spróbuj ponownie.")

tol = float(input("Podaj żądaną dokładność (np. 0.0001): ").strip())
lower = float(input("Podaj dolną wartość przedziału do rysowania: ").strip())
upper = float(input("Podaj górną wartość przedziału do rysowania: ").strip())
n_rects = int(input("Podaj ilość podziału przedziałów (np. 3): ").strip())

print("\nObliczanie metodą Simpsona...")
simpson_result, simpson_nodes = simpson_infinite(func, 0, n_rects, tol)
print(f"Wynik całkowania (Simpson): {simpson_result:.10f}")

print("\nObliczanie metodą Gaussa-Laguerre...")
gauss_result, gauss_nodes = gauss_laguerre_iterated(func, tol)
print(f"Wynik całkowania (Gauss-Laguerre): {gauss_result:.10f}")

print(f"\nRóżnica między metodami: {abs(simpson_result - gauss_result):.10f}")

print("\nRysowanie wykresu funkcji i jej funkcji ważonej...")
rysuj_calkowanie(func, simpson_nodes, gauss_nodes, przedzial=(lower, upper))
