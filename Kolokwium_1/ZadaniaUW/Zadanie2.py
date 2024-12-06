from typing import List, Any


# Zadanie 2
# Plik 'opady.csv' przechowuje dane na temat miesięcznych sum opadów atmosferycznych w 2001 roku
# zanotowanych we wszystkich posterunkach IMGW. Dane zapisane są w formacie:
# 'NAZWA STACJI,rok,miesiąc,suma_opadu\n’
# Napisz progam, który wczyta dane z pliku, a następnie na ich podstawie obliczy roczną sumę opadu
# i zapisze wynik w postaci listy result: list[list[str,float]]:
# [['Warszowice', 991.8]
# ['Chałupki', 687.8]
# ['Wisła Wielka', 1140.7]
# ['Goczałkowice-Zdrój', 930.6]
# ['Sejny', 671.9]]
# Zwróć uwagę na formatowanie obiektów str i zaokrąglenie obiektów float w liście wynikowej.

def otworz_plik(sciezka_do_pliku: str) -> list[str]:
    lista = []
    with open(sciezka_do_pliku, 'r', encoding='utf-8') as plik:
        for linia in plik:
            lista.append(linia)
    plik.close()
    return lista


def podziel_elementy(lista: list[str]) -> list[list]:
    miasta_opady = []
    for element in lista:
        elementy: list = element.split(';')
        elementy[-1] = elementy[-1].replace('\n', '')
        miasta_opady.append(elementy)
    return miasta_opady


def policz_opady_dla_kazdego_miasta(lista: list[list]) -> list[list[Any]]:
    opady = []
    miasto_opady: dict = {}
    for element in lista:
        miasto = element[0]
        opady_wartosc = float(element[3])
        if miasto in miasto_opady:
            miasto_opady[miasto] += opady_wartosc
        else:
            miasto_opady[miasto] = 0
    for miasto, opady_wartosc in miasto_opady.items():
        temp = [miasto, opady_wartosc]
        opady.append(temp)
    return opady


lista_z_liniami = otworz_plik('opady.csv')
oczyszczona = podziel_elementy(lista_z_liniami)
suma_opady = policz_opady_dla_kazdego_miasta(oczyszczona)