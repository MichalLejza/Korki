
# Zadanie 9
# Wykorzystaj dane z pliku ‘opady.csv’ oraz funkcje:
# station_dict (patrz zad. 6.), data_filter (patrz zad. 8.) i srednia (patrz zad. 3.)
# do napisania funkcji mean_by_month(data: dict, month: int) -> float zwracającej średnią wartość
# opadu we wszystkich posterunkach opadowych w wybranym miesiącu 2001 roku (argument month).

from funkcje import station_dict, data_filter, file_to_list, srednia


def mean_by_month(data: dict, month: int) -> float:
    opady_w_miesiacu = []
    for miasto, lista_opadow in data.items():
        opady = lista_opadow[month - 1]
        opady_w_miesiacu.append(opady)
    average = srednia(opady_w_miesiacu)
    return average


lista: list = file_to_list('opady.csv', ';', 'utf-8')
slownik: dict = station_dict(lista)
filtered_slownik: dict = data_filter(slownik)
srednia_opadow = mean_by_month(filtered_slownik, 1)
print(filtered_slownik)
print(srednia_opadow)
