# Zadanie 1
# W pliku 'nazwiska.txt' w każdej linii zapisano małymi literami imię i nazwisko jednej osoby
# rozdzielone średnikiem:
# jan;kot
# marek;lis
# anna;kuna
# jacek;borsuk
# ...
# lew;lew

# Napisz program, który:
# 1. wczyta dane z pliku i zapisze je w postaci listy, której elementami będą obiekty str
# odpowiadające kolejnym liniom pliku:
# ['jan;kot\n', 'marek;lis\n', 'anna;kuna\n', …, 'lew;lew']

# 2. stosując metody klasy str utworzy na podstawie powyższej listy nową listę postaci:
# ['Jan Kot', 'Marek Lis', 'Anna Kuna', …, 'Lew Lew']

# 3. zapisze elementy listy z punktu drugiego w pliku 'osoby.txt' (każdy element powinien być
# zapisany w osobnym wierszu)

# 4. utworzy listę wszystkich osób posortowaną alfabetycznie według nazwiska


def pierwszy_podpunkt(sciezka_do_pliku: str) -> list[str]:
    lista_z_liniami = []
    with open(sciezka_do_pliku, 'r', encoding='utf-8') as ofejkwof:
        for linia in ofejkwof:
            lista_z_liniami.append(linia)
    ofejkwof.close()
    return lista_z_liniami


def drugi_podpunkt(lista: list) -> list[str]:
    nowa_lista = []
    for linia in lista:
        godnosc: list = linia.split(';')

        imie: str = godnosc[0]
        nazwisko: str = godnosc[1]

        imie: str = imie.capitalize()
        nazwisko: str = nazwisko.capitalize()

        nazwisko: str = nazwisko.replace('\n', '')
        nowa_lista.append(imie + ' ' + nazwisko)
    return nowa_lista


def trzeci_podpunkt(sciezka_do_pliku: str, lista: list[str]):
    with open(sciezka_do_pliku, 'w', encoding='utf-8') as plik:
        for element in lista:
            plik.write(element + '\n')
    plik.close()


def czwarty_podpunkt(lista: list[str]) -> list[str]:
    nowa_lista = []
    for element in lista:
        podzielone: list = element.split(' ')
        nowa_lista.append(podzielone)
    nowa_lista.sort(key=lambda x: x[1])

    for i in range(len(nowa_lista)):
        imie_i_nazwisko: list = nowa_lista[i]
        imie: str = imie_i_nazwisko[0]
        nazwisko: str = imie_i_nazwisko[1]
        nowa_lista[i] = imie + ' ' + nazwisko
    return nowa_lista


lista_linie: list = pierwszy_podpunkt("nazwiska.txt")
nowa_lista_linie: list = drugi_podpunkt(lista_linie)
trzeci_podpunkt('osoby.txt', nowa_lista_linie)
posortowana_lista: list = czwarty_podpunkt(nowa_lista_linie)
print(posortowana_lista)
