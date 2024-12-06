
# Zadanie 9
# Wykorzystaj dane z pliku ‘opady.csv’ oraz funkcje:
# station_dict (patrz zad. 6.), data_filter (patrz zad. 8.) i srednia (patrz zad. 3.)
# do napisania funkcji mean_by_month(data: dict, month: int) -> float zwracającej średnią wartość
# opadu we wszystkich posterunkach opadowych w wybranym miesiącu 2001 roku (argument month).


from funkcje import *


def mean_by_month(data: dict, month: int) -> float:
    suma_opady = 0.0
    for miasto in data:
        suma_opady += data[miasto][month - 1]
    return suma_opady / len(data)
