#  10.11.24
#  Struktury Danych wbudowane w pythona

# 1. Listy
lista = [1, 2, 3, 4, 5, 6]
#        0  1  2  3  4  5
lista[0] = 10

# Uporządkowona
# Modyfikowalna (mutable)
lista[1] = 11
lista.append(7)
lista.pop(0)
# Elementy mogą się powtarzać
lista1 = [1, 1, 1, 1, 1, 1, 1]
# Dostęp jest indeksowalny

# 2. Krotki
x: tuple = (1, 2, 3, 4, 5, 6)
#           0  1  2  3  4  5
# Uporządkowana
element = x[0]
# Niemodyfikowana (unmutable)

# Elementy mogą się powtarzać
x1: tuple = (1, 1, 1, 1, 1, 1, 1)

# Dostęp jest indeksowalny
r = x[1]

# Bardziej wydajna niż lista

# 3. Sety
zbior = {1, 2, 3, 4, 5, 6}

przyklad = [1, 4, 5, 2, 2, 1, 3, 9, 8, 7, 10, 10, 2, 1, 4893284910]
# lista = [_, 3, 3, _, _, _, _]


# Nieuporządkowana
zbior2 = set()
zbior2.add(1)
zbior2.add(2)
zbior2.add(-2)

# Modyfikowalna (Mutable)
# Elementy się nie powtarzają
# Wspiera operacje matematyczne
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

suma = set1 | set2
print(suma)

roznica = set1 - set2
print(roznica)

czescwpolna = set1 & set2
print(czescwpolna)

fyeuw = set1 ^ set2
print(fyeuw)


# Nie indexowana
set1 = {1, 2, 3, 4, 5, 6}
for element in set1:
    print(element)

czyJestJeden = 1 not in set1
print(czyJestJeden)

# 4. Słowniki
lista = [1, 2, 3, 4, 5, 6]
#       "jeden", "dwa", "trzy" .... "szesc"

lista[0] = 467823

slownik = {"Jeden": 1, "Dwa": 2, "Trzy": 3}
print(slownik["Jeden"])
slownik["Jeden"] = 90
print(slownik["Jeden"])

slownik1 = {0: 0, 1: 1, 2: 2, 3: 3}
print(slownik1)

slownik1["Jeden"] = 90
print(slownik1)

slownik1["Jeden"] = 748432
print(slownik1)

slownik2 = {0: 0, 1: 1, 2: 2, 3: 3}
print(slownik2)

del slownik2[0]
print(slownik2)

usuniete = slownik2.pop(1)
print(usuniete)
print(slownik2)

# Nieuporządkowane
# Modyfikowalna (Mutable)
# Przechowuje pary klucz-wartość
# Klucze są unikalne

# Inne Struktury
# 5. Zbiory niezmienne
# Niezmienna wersja zbioru
# Po utworzeniu nie można dodawać ani usuwać elementów.

# Typy Sekwencyjne
# 6. łancuchy znaków String
# Niepodzielna sekwencja znaków, niemutowalna.

# 7. Zakresy range()
# Generuje sekwencję liczb, często używaną do iteracji.
# Tworzenie: zakres = range(5) # 0, 1, 2, 3, 4
