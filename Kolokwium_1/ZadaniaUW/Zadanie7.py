
# Zadanie 7
# Napisz funkcję show_rain(data: dict, station: str, month: int) -> float|str, która na podstawie nazwy
# stacji przekazanej w argumencie station, oraz numeru miesiąca (1 – 12) zwróci ze zbioru data
# (słownik w formacie identycznym jak w zadaniu 6) wartość miesięcznej sumy opadu w wybranym
# miesiącu na tej stacji, lub ‘brak danych’, jeżeli stacja o podanej nazwie nie występuje w słowniku
# data.
from funkcje import *


def show_rain(data: dict, station: str, month: int) -> float | str:
    if station not in data:
        return 'brak danych'

    opady: list = data[station]
    opady_danego_miesiaca = opady[month - 1]
    return opady_danego_miesiaca



lista: list = file_to_list('opady.csv', ';', 'utf-8')
slownik: dict = station_dict(lista)
print(slownik)
opady = show_rain(slownik, 'Warszawa', 2)
print(opady)


