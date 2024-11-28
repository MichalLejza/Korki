import random
from math import sqrt

# funkcja print z dodatkami
print("Hello World", end=" ")
print("Hello World")
# typ danych: None

# typ danych: string

napis: str = "Napis"
napis1: str = 'Napis'

lista: list = [1, 2, 3]
pierwszyElement = lista[0]
lista[0] = 4

# immutable
# nie można modyfikować napisu


# zakres liczbowy
zmienna = 9
if zmienna < 10:
    if zmienna > 5:
        print("zmienna jest mniejsza od 10 ale wieksza od 5")

if 5 < zmienna < 10:
    print("zmienna jest mniejsza od 10 ale wieksza od 5")

# operator ternarny

zmienna1 = 10
if zmienna1 > 10:
    print("zmienna jest większa od 10")
else:
    print("zmienna nie jest większa od 10")

napisDoWydruku = "Zmienna jest większa od 10" if zmienna1 > 10 else "Zmienna nie jest większa od 10"
print(napisDoWydruku)

print("Zmienna jest większa od 10" if zmienna1 > 10 else "Zmienna nie jest większa od 10")

# tworzenie pętli przypomnienie

# tworzenie funkcji przypomnienie


def przyblizeniePi():
    punktyWKole = 0
    punktywszystkie = 0
    for i in range(50000):
        # x1 i y1 to są współrzędne punktu
        x1 = random.uniform(-1, 1)
        y1 = random.uniform(-1, 1)
        odleglosc = sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
        if odleglosc < 1:
            punktyWKole += 1
        punktywszystkie += 1
    liczbaPi = 4 * (punktyWKole / punktywszystkie)
    print(liczbaPi)


przyblizeniePi()

# 0 i 1 i każda następna to suma dwóch poprzednich
# 1, 2, 3, 5, 8, 13, 21




