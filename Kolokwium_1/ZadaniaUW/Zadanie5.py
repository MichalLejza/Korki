# Zadanie 5
# Przejdź do modułu zad_02.py, a następnie na podstawie listy result z zadania 2 utwórz słownik,
# którego kluczami będą nazwy stacji, a wartościami roczne sumy opadów w tych stacjach.

from Zadanie2 import *


lista_z_liniami = otworz_plik('opady.csv')
oczyszczona = podziel_elementy(lista_z_liniami)
suma_opady = policz_opady_dla_kazdego_miasta(oczyszczona)
print(suma_opady)

slownik: dict = {}

for element in suma_opady:
    miasto: str = element[0]
    opady: float = element[1]
    slownik[miasto] = opady

print(slownik)
