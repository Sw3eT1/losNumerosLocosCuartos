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
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.\n")

while True:
    tol_input = input("Podaj żądaną dokładność (np. 0.0001): ").strip()
    try:
        tol = float(tol_input)
        if tol > 0:
            break
        else:
            print("Dokładność musi być dodatnią liczbą większą od zera.")
    except ValueError:
        print("Wprowadź poprawną liczbę zmiennoprzecinkową.")

while True:
    lowerInterval = input("Podaj dolna wartosc przedzialu").strip()
    try:
        lowerInterval = float(lowerInterval)
        break
    except ValueError:
        print("Wprowadź poprawną liczbę zmiennoprzecinkową.")

while True:
    higherInterval = input("Podaj gorna wartosc przedzialu").strip()
    try:
        higherInterval = float(higherInterval)
        break
    except ValueError:
        print("Wprowadź poprawną liczbę zmiennoprzecinkową.")

while True:
    numberOfRectangles = input("Podaj ilosc podzialu przedzialow").strip()
    try:
        numberOfRectangles = int(numberOfRectangles)
        break
    except ValueError:
        print("Wprowadź poprawną liczbę calkowita.")

print("\nObliczanie metodą Simpsona...")
simpson_result, simpson_nodes = simpson_infinite(func,lowerInterval, higherInterval, numberOfRectangles, tol)
print(f"Wynik całkowania (Simpson): {simpson_result:.10f}")

print("\nObliczanie metodą Gaussa-Laguerre...")
gauss_result, gauss_nodes = gauss_laguerre_iterated(func, tol)
print(f"Wynik całkowania (Gauss-Laguerre): {gauss_result:.10f}")

print("\nRóżnica między metodami:", abs(simpson_result - gauss_result))

print("\nRysowanie wykresu funkcji i jej funkcji ważonej...")
rysuj_calkowanie(func, simpson_nodes, gauss_nodes, przedzial=(0, 10))