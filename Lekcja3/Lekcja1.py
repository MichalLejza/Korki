# Wstęp do funkcji

# podstawowa definicja funkcji
def DowolnaNazwaFunkcjiCoTylkoChcesz():
    pass


# co funkcja zwraca
# liczbe
# liste
# krotke
# obiekt
# albo nic

# przykład prostej funkcji
def funkcja():
    print("Program teraz jest w funkcji")


# przykład funkkcji z argumentem
def funkcjaDruga(argument):
    print("Program jest teraz w drugiej funkcji i zaraz wypiszę argument")
    print(argument)


def Suma(liczbaPierwsza, liczbaDruga):
    suma = liczbaPierwsza + liczbaDruga
    return suma


wynikFunkcjiSuma = Suma(10, 15)
print(wynikFunkcjiSuma)


# przykład funkcji z podanymi tyapmi argumentów i typem zwracanym
def funkcjaDobrzeNapisana(liczbaPierwsza: int, liczbaDruga: int) -> int:
    suma: int = liczbaDruga + liczbaPierwsza
    return suma


def proceduraDobrzeNapisana(liczbaPierwsza: int, liczbaDruga: int) -> None:
    suma: int = liczbaDruga + liczbaPierwsza
    print(suma)


# wczesne wychodzenie z funkcji
def funckjaNWM(argument):
    argument += 2
    argument *= 2
    argument += 2
    return
