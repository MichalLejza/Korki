import re


def zmien_napis_na_listy(napis: str) -> tuple:
    """
    '-3+4+5+10*100' -> ['-', '+', '+', '+', '*'] i [3, 4, 5, 10, 100]
    Jan,Kowalski,costam -> [Jan Kowalski costam] -> split(',')
    +, -, *, /
    :param napis:
    :return:
    """

    lista_liczby = re.split('[+-/*]', napis)
    if lista_liczby[0] == '':
        lista_liczby[0] = '0'
    lista_liczby = [int(liczba) for liczba in lista_liczby]

    znaki_lista = [znak for znak in napis if znak in '+-/*']
    return znaki_lista, lista_liczby

def policz_wynik(znaki: list, liczby: list) -> float:
    """
    90 + 60 - 30 * 10 / 6
    ['+', '-', '*', '/']
    [90, 60, 30, 10, 6]
    :param znaki:
    :param liczby:
    :return:
    """
    # szuakmy dzielenia
    index = 0
    for znak in znaki:
        if znak == '/':
            liczba1 = liczby[index]
            liczba2 = liczby[index + 1]
            wynik = podziel(liczba1, liczba2)
            liczby[index] = wynik
            liczby.pop(index + 1)
            znaki.pop(index)
        index += 1

    # szukamy mnożenia
    index = 0
    for znak in znaki:
        if znak == '*':
            liczba1 = liczby[index]
            liczba2 = liczby[index + 1]
            wynik = pomnoz(liczba1, liczba2)
            liczby[index] = wynik
            liczby.pop(index + 1)
            znaki.pop(index)
        index += 1

        # szukamy odejmowania
    index = 0
    for znak in znaki:
        if znak == '-':
            liczba1 = liczby[index]
            liczba2 = liczby[index + 1]
            wynik = odejmij(liczba1, liczba2)
            liczby[index] = wynik
            liczby.pop(index + 1)
            znaki.pop(index)
        index += 1

        # szukamy dodawania
    index = 0
    for znak in znaki:
        if znak == '+':
            liczba1 = liczby[index]
            liczba2 = liczby[index + 1]
            wynik = dodaj(liczba1, liczba2)
            liczby[index] = wynik
            liczby.pop(index + 1)
            znaki.pop(index)
        index += 1

    return liczby[0]


def dodaj(liczba1, liczba2):
    return liczba1 + liczba2

def odejmij(liczba1, liczba2):
    return liczba1 - liczba2

def pomnoz(liczba1, liczba2):
    return liczba1 * liczba2

def podziel(liczba1, liczba2):
    return liczba1 / liczba2

