import random

# 1. Zmienne
# liczby całkowite (int)
zmiennaCalkowita1: int = 0
zmiennaCalkowita2: int = -784
zmiennaCalkowita3: int = 48239

# liczby zmiennoprzecinkowe (float)
zmiennaPrzecinkowa1: float = 0.0
zmiennaPrzecinkowa2: float = 0.25
zmiennaPrzecinkowa3: float = 8.432
zmiennaPrzecinkowa4: float = -42.41
zmiennaPrzecinkowa5: float = 54

# liczby urojone (complex)
zmiennaUrojona1: complex = 2 + 2j
zmiennaUrojona2: complex = -2 + 2j
zmiennaUrojona3: complex = 2
zmiennaUrojona4: complex = -2
zmiennaUrojona5: complex = -432 - 41j

# wartości Logiczne (bool)
wartoscTrue: bool = True
wartoscFalse: bool = False

# wartości typu None
wartoscNone: None = None

# ciągi znaków (string) lub (str)
ciagZnakow1: str = "Hello World"
ciagZnakow2: str = 'a'
ciagZnakow3: str = 'Hello World'
ciagZnakow4: str = "Hello World\nGoodbye World"

# sprawdzanie typów zmiennych
print(type(zmiennaCalkowita1))
print(type(zmiennaCalkowita2))
print(type(zmiennaUrojona1))
print(type(wartoscTrue))
print(type(wartoscNone))

# 2. Operatory
zmiennaPierwsza = 32
zmiennaDruga = 10

# dodawanie
wynikDodawania = zmiennaPierwsza + zmiennaDruga
# dodanie do zmiennej liczby
zmiennaPierwsza += 10
zmiennaPierwsza = zmiennaPierwsza + 10

# odejmowanie
wynikOdejmowania = zmiennaPierwsza - zmiennaDruga
# odjęcie od zmiennej liczby
zmiennaPierwsza -= 10
zmiennaPierwsza = zmiennaPierwsza + 10

# mnożenie
wynikMnozenia = zmiennaPierwsza * zmiennaDruga
# pomnożenie zmiennej o liczbę
zmiennaPierwsza *= 2
zmiennaPierwsza = zmiennaPierwsza * 2

# dzielenie całkowite
wynikDzielenia = zmiennaPierwsza / zmiennaDruga
# podzielenie zmiennej o liczbę
zmiennaPierwsza /= 2
zmiennaPierwsza = zmiennaPierwsza / 2

# dzielenie pełne
wynikDzieleniaPelnego = zmiennaPierwsza // zmiennaDruga
# podzielenie pełne zmiennej o liczbę
zmiennaPierwsza //= 2
zmiennaPierwsza = zmiennaPierwsza // 2

# modulo
wynikModulo = zmiennaPierwsza % zmiennaDruga

# potęgowanie
wynikPotegowania = zmiennaPierwsza ** zmiennaDruga
# zmienna do potęgi danej liczby, np.2
zmiennaPierwsza **= 2
zmiennaPierwsza = zmiennaPierwsza ** 2

# inkrementacja
zmiennaPierwsza += 1

# dekrementacja
zmiennaPierwsza -= 1

# porównywanie zmiennych
# mniejsze lub większe
zmiennaPierwszaWieksza = zmiennaPierwsza > zmiennaDruga
zmiennaPierwszaMniejsza = zmiennaPierwsza < zmiennaDruga

# mniejsze równe, większe równe
zmiennaPierwszaWiekszaRowna = zmiennaPierwsza >= zmiennaDruga
zmiennaPierwszaMniejszaRowna = zmiennaPierwsza <= zmiennaDruga

# zmienna w zakresie liczbowym
zmiennaPierwszaWZakresie = 10 < zmiennaPierwsza < 20

# 3. Instrukcje Sterowania przepływem
# if-elif-else
zmiennaPrzykladowa1: int = 5
if zmiennaPrzykladowa1 > 6:
    print("Zmienna jest mniejsza od 6")
elif zmiennaPrzykladowa1 > 4:
    print("Zmienna jest mniejsza od 4")
elif zmiennaPrzykladowa1 > 2:
    print("Zmienna jest mniejsza od 2")
else:
    print("Zmienna jest bardzo mała")

# operator ternarny (skrócoy if-else)
zmiennaPrzykladowa5: int = 10
wynik = "Liczba jest większa od 10" if zmiennaPrzykladowa5 > 10 else "Liczba jest mniejsza od 10"

# 4. Pętle
# pętla for od zera do liczby w nawiasach range
for liczba in range(10):
    print("Obrót pętli: ", liczba)

# pętla for od liczby do liczby w nawiasach range
for liczba in range(2, 10):
    print("Obrót pętli: ", liczba)

# pętla for od liczby do liczby w nawiasach ale inkrementuje o ostatnią liczbę w nawiasach range
for liczba in range(2, 10, 2):
    print("Obrót pętli: ", liczba)

przykladowyNapis: str = "Hello World"

# pętla for od 0 do długości napisu. indeks to tylko liczba (index)
for index in range(len(przykladowyNapis)):
    print(przykladowyNapis[index])

# pętla for od 0 do długości napisu. element to litera w napisie (character)
for element in przykladowyNapis:
    print(element)

# pętla while
zmiennaPrzykladowa6: int = 0
while zmiennaPrzykladowa6 < 10:
    print("Obrót pętli: ", zmiennaPrzykladowa6)
    zmiennaPrzykladowa6 += 1

# 5. Losowanie liczb
# randomowa liczba od zakresu z zakresu [0, 1)
randomowaLiczbaOdZeraDoJeden: float = random.random()
print(randomowaLiczbaOdZeraDoJeden)

# randomowa liczba całkowita z zakresu [X, Y)
randomowaLiczbaCalkowita: int = random.randint(1, 10)
print(randomowaLiczbaCalkowita)

# randomowa liczba zmiennoprzecinkowa z zakresu [X, Y)
randomowaLiczbaZmiennoPrzecinkowa: float = random.uniform(1.5, 5.5)
print(randomowaLiczbaZmiennoPrzecinkowa)

# randomowa liczba całkowita z zakresu [X, Y) ale z krokiem danym
randomowaLiczbaOdDoZKrokiem: int = random.randrange(0, 20, 2)
print(randomowaLiczbaOdDoZKrokiem)

# randomowa liczba z listy
przykladowaLista1: list[int] = [1, 2, 3, 4, 5]
randomowyElementZListy: int = random.choice(przykladowaLista1)
print(randomowyElementZListy)

# K randomowych liczb z danego zbioru liczb
randomowyZbiorKLiczbZlisty: list = random.sample([1, 2, 3, 4, 5], 3)
print(randomowyZbiorKLiczbZlisty)

# 6. Input/Output
# wyświetlanie na ekranie
print("Coś")
print(1)
print("Napis z liczbą: " + str(9))
print("Napis z liczbą: ", 9)
print("Napis ale nie idziemy do nowej linii", end="")

# pobieranie danych z terminala
zmiennaNapisowa1: str = input("Podaj jakiś input, będzie to poprostu napis: ")
zmiennaPrzykladowa7: int = int(input("Podaj zmienną całkowitą: "))
zmiennaPrzykladowa8: float = float(input("Podaj zmienną przecinkową"))

# 7. Listy
# deklarowanie list
# pusta lista:
przykladowaLista2: list = []

# lista z podanymi liczbami
przykladowaLista3: list[int] = [1, 2, 3, 4, 5]

# lista z wygenerowanymi liczbami przez pętle enhanced for
przykladowaLista4: list[int] = [liczbaLubElement for liczbaLubElement in range(1, 6)]

# zmiana poszczególnych wartości w liście
przykladowaLista4[0] = 10
przykladowaLista4[1] = 9
przykladowaLista4[-1] = -89
przykladowaLista4[-2] = -31

# odczytywanie wartości z listy
elementPierwszy: int = przykladowaLista4[0]
elementDrugi: int = przykladowaLista4[1]
elementOstatni: int = przykladowaLista4[-1]
elementPrzedostatni: int = przykladowaLista4[-2]

# przechodzenie po liście po indeksach
for index in range(len(przykladowaLista4)):
    print("Element pod indexem: " + str(index) + "wynosi: " + str(przykladowaLista4[index]))

# przechodzenie po liście ale po wartościach:
for element in przykladowaLista4:
    print("Element listy: " + str(element))

# dodawanie pojedynczego elementów do listy
przykladowaLista4.append(6)

# dodawanie kilku elementów (podanych w liście) do listy
przykladowaLista4.extend([1, 2, 3, 4, 5])

# usuwanie elementu z listy
przykladowaLista4.pop(-1)
przykladowaLista4.pop(0)

# sortowanie listy
przykladowaLista4.sort()

# odwrananie listy
przykladowaLista4.reverse()

# czyszczenie całej listy
przykladowaLista4.clear()


# 9. Funkcje nic nie zwracające
# deklarowanie funkcji bez argumentów:
# pamiętaj o nawiasach i dwukropku na końcu!
def przykladowaFunkcja1():
    pass


# deklarowanie funkcji z jednym argumentem:
def przykladowaFunkcja2(argumentPierwszy: int):
    pass


# deklarowanie funkcji z dwoma argumentemi:
def przykladowaFunkcja3(argumentPierwszy: int, drugiArgument: float):
    pass


# 10. Funkcje zwracające jakiś element
# deklaracja funkcji bez argumentów
def przykladowaFunkcja4() -> int:
    return 1


# deklaracja funkcji z jednym argumentem:
def przykladowaFunkcja5(argumentPierwszy: int) -> int:
    return argumentPierwszy * 2


# deklaracja funkcji z dwoma argumentami:
def przykladowaFunkcja6(argumentPierwszy: int, argumentDrugi: int) -> int:
    return argumentDrugi * argumentPierwszy


# 11. Funkcja zagnieżdżona
def funkcja_zewnetrzna(x):
    def funkcja_wewnetrzna(y):
        return x + y

    return funkcja_wewnetrzna


def funkcjaPierwsza(argument: int) -> None:
    def funkcjaDruga(arg: int) -> int:
        return arg ** 2

    print(funkcjaDruga(arg=argument))


# 12. Napisy
# deklarowanie napisu pustego
napis1: str = ""
napis2: str = ''

# deklarowanie napisu nie pustego
napis3: str = "Napis"
napis4: str = 'Napis'

# łącznie napisów
napisPolaczony: str = "Hehe" + " HAHA"

# pobieranie znaku z określonego miejsca:
char: str = napis1[0]

# pobieranie napisu od użytkownika
napisOdUsera: str = input("Tu możesz coś wpisać ale nie musisz")

# metody do napisu
napis = "Przykładowy napis"
# Zwraca nowy napis z wszystkimi literami w małych literach.
napis: str = napis.lower()

# Zwraca nowy napis z wszystkimi literami w dużych literach.
napisUpper: str = napis.upper()

# Zwraca nowy napis z pierwszą literą dużą, a pozostałymi małymi.
napisPierwszaDuza: str = napis.capitalize()

# Zwraca nowy napis z każdą pierwszą literą w słowie dużą.
napisWszystkieSlowaZDuzej: str = napis.title()

# Usuwa białe znaki z początku i końca napisu.
napisBezSpacjiZprzoduIZTylu: str = napis.strip()

# Usuwa białe znaki tylko z początku napisu
napisBezSpacjiZPrzodu: str = napisPierwszaDuza.lstrip()

# Usuwa białe znaki tylko z końca napisu.
napisBezSpacjiZtylu: str = napis.rstrip()

# Łączy elementy iterowalnego obiektu (np. listy) w jeden napis, używając napisu jako separatora.
napisPolaczonyOSlowa: str = napis.join([" Pierwsze", " Slowo", " Drugie", " Slowo"])

# Dzieli napis na listę podnapisów według separatora sep (domyślnie białe znaki).
rozdzielonyNapis: list = napis.split(" ")

# Zwraca indeks pierwszego wystąpienia podnapisu sub lub -1, jeśli nie znaleziono.
indexPodnapisuLubLitery: int = napis.find("P")

# Zastępuje wszystkie wystąpienia old napisem new i zwraca nowy napis.
napisPodmieniony: str = napis.replace("P", "R")

# Zwraca liczbę wystąpień podnapisu sub w napisie.
ileDanegoPodnapisu: int = napis.count("P")

# Zwraca True, jeśli wszystkie znaki w napisie są literami.
wszystkieZnakiToLitery: bool = napis.isalpha()

# Zwraca True, jeśli wszystkie znaki w napisie są cyframi.
wszystkieZnakiToCyfry: bool = napis.isdigit()

# Zwraca True, jeśli wszystkie znaki w napisie są literami lub cyframi.
wszystkieZnakitoCyfryLubLitery: bool = napis.isalnum()

# Zwraca True, jeśli wszystkie litery w napisie są małe.
wszystkieZnakiMale: bool = napis.islower()

# Zwraca True, jeśli wszystkie litery w napisie są duże.
wszystkieZnakiDuze: bool = napis.isupper()

# Zwraca True, jeśli wszystkie znaki w napisie to białe znaki.
wszystkieZnakiToSpacje: bool = napis.isspace()


# 13. Pozostałe własności funkcji
# argumenty pozycyjne
# Argumenty pozycyjne to wartości przekazywane do funkcji
# w odpowiedniej kolejności. Są wymagane, jeśli funkcja nie
# definiuje wartości domyślnych dla argumentów.

def dodaj(pierwszy, drugi):
    return pierwszy + drugi


wynik = dodaj(pierwszy=3, drugi=5)
print(wynik)  # Wyświetli: 8


# zwracanie wartości
# Funkcje w Pythonie mogą zwracać wartość za pomocą
# słowa kluczowego return. Bez return funkcja zwraca None.

def pomnoz(pierwszy, drugi):
    return pierwszy * drugi


wynik = pomnoz(4, 6)
print(wynik)  # Wyświetli: 24

# zmienne lokalne i globalne
# Zmienne utworzone wewnątrz funkcji są lokalne, czyli
# dostępne tylko w obrębie tej funkcji. Zmienne globalne
# można modyfikować wewnątrz funkcji używając słowa kluczowego global.

licznik = 0  # Zmienna globalna


def zwieksz():
    global licznik
    licznik += 1


zwieksz()
print(licznik)  # Wyświetli: 1


# funkcje zafnieżdżone
# Funkcje w Pythonie mogą być definiowane wewnątrz innych funkcji.
# Funkcja zagnieżdżona ma dostęp do zmiennych funkcji zewnętrznej.

def zewnetrzna():
    x = 10

    def wewnetrzna():
        return x + 5

    return wewnetrzna()


wynik = zewnetrzna()
print(wynik)  # Wyświetli: 15


# Rekurencja
# Rekurencja to technika, gdzie funkcja wywołuje samą siebie.
# Jest często stosowana do rozwiązywania problemów, które można
# podzielić na mniejsze podproblemy, np. obliczanie silni.


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


wynik = silnia(5)
print(wynik)  # Wyświetli: 120


# 14. Krotki
# definicja
# Krotka to niezmienialna (immutable) sekwencja elementów.
# Po utworzeniu krotki nie można zmienić jej zawartości ani
# kolejności elementów.

# tworzenie krotki
krotka1: tuple = (1, 2, 3)
krotka2: tuple = (4,)
krotka3: tuple = 1, 2, 3

# dostęp do elementów
pierwszyElementKrotki = krotka1[0]
ostatniElementKrotki = krotka1[-1]
print(krotka1[0])

# niezmienność
# Elementy krotki nie mogą być modyfikowane po utworzeniu.
# Z tego powodu krotki są użyteczne do przechowywania danych,
# które powinny pozostać stałe.

# operacje na krotkach
sumaKrotek = krotka1 + krotka2
print(sumaKrotek)

powielonaKrotka = krotka1 * 3
print(powielonaKrotka)

# rozpakowywanie krotek
a, b, c = krotka1

# przydatne funkcje i metody
# ilość elementów w krotce
len(krotka1)
# wartość najmniejsza
najmniejsza = min(krotka1)
# wartość największa
najwieksza = max(krotka1)
# liczba wystąpień danego elementu
ilosc = krotka1.count(1)
# index pierwszego wystapienia elementu
index = krotka1.index(1)


# 15. Zbiory
# definicja
# Zbiór to nieuporządkowana kolekcja unikalnych elementów.
# Nie zawiera duplikatów, a elementy nie są uporządkowane.

# tworzenie zbiorów
zbior1 = {1, 2, 3}
zbior2 = set([4, 5, 6])
pusty_zbior = set()

print(zbior1)  # Wyświetli: {1, 2, 3}
print(zbior2)  # Wyświetli: {4, 5, 6}
print(pusty_zbior)  # Wyświetli: set()

# dodawanie elementów
zbior = {1, 2, 3}
zbior.add(4)
print(zbior)  # Wyświetli: {1, 2, 3, 4}

# usuwanie elementów
zbior = {1, 2, 3}
element = zbior.pop() # usuwa i zwraca losowy element
zbior.remove(2)
zbior.discard(5)  # Nie zgłosi błędu
print(zbior)      # Wyświetli: {1, 3}

# operacje na zbiorach
zbior1 = {1, 2, 3}
zbior2 = {3, 4, 5}

print(zbior1 | zbior2)  # Suma: {1, 2, 3, 4, 5}
print(zbior1 & zbior2)  # Część wspólna: {3}
print(zbior1 - zbior2)  # Różnica: {1, 2}
print(zbior1 ^ zbior2)  # Różnica symetryczna: {1, 2, 4, 5}

# sprawdzanie przynależności
zbior = {1, 2, 3}
print(2 in zbior)  # Wyświetli: True
print(4 in zbior)  # Wyświetli: False

# typy danych w zbiorze
# Zbiory mogą zawierać różne typy danych, ale elementy
# muszą być niemutowalne (niezmienne), np. liczby,
# łańcuchy znaków, krotki. Listy i zbiory nie mogą być elementami zbiorów.
zbior = {1, "tekst", (2, 3)}
print(zbior)  # Wyświetli: {1, 'tekst', (2, 3)}

# coprehension zbioru
kwadraty = {x**2 for x in range(5)}
print(kwadraty)  # Wyświetli: {0, 1, 4, 9, 16}

# iteracja po zbiorze
# Po zbiorze można iterować za pomocą pętli for. Ponieważ zbiory
# są nieuporządkowane, elementy mogą być przetwarzane w losowej
# kolejności, zależnej od implementacji.
zbior = {1, 2, 3, 4, 5}

for element in zbior:
    print(element)  # Wyświetli kolejno elementy, np.: 1, 2, 3, 4, 5


# 16. Słowniki
# definicja Słownika
# Słownik to kolekcja par klucz-wartość, gdzie każdy
# klucz jest unikalny. Struktura: {klucz1: wartość1, klucz2: wartość2, ...}.

# tworzenie słownika
slownik1: dict = {}
slownik2: dict = dict()
slownik3: dict = {"pierwszy": 1, "Drugi": 2, "Trzeci": 3}
slownik4: dict = {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}

# dostęp do wartości
element = slownik3["pierwszy"]
print(element["drugi"])

# pobieranie wartości, drugi argument jest zwracany jeśli nie ma klucza
element = slownik3.get("pierwszy", "Nie ma takiego klucza")

# dodawanie i aktualizowanie kluczy
slownik4[0] = [-1, -2, -3]

# usuwanie kluczy
del slownik3["pierwszy"]
wartosc = slownik4.pop(0)
slownik3.clear()

# sprawdzanie obecności klucza
slownik = {"a": 1, "b": 2, "c": 3}

print("a" in slownik)  # Wyświetli: True
print("d" in slownik)  # Wyświetli: False

# Iteracja po słowniku
slownik = {"a": 1, "b": 2, "c": 3}

# Iteracja po kluczach
for klucz in slownik:
    print(klucz)  # Wyświetli: a, b, c

# Iteracja po wartościach
for wartosc in slownik.values():
    print(wartosc)  # Wyświetli: 1, 2, 3

# Iteracja po parach klucz-wartość
for klucz, wartosc in slownik.items():
    print(klucz, wartosc)  # Wyświetli: a 1, b 2, c 3

# Kopiowanie słownika
slownik = {"a": 1, "b": 2}

# Kopiowanie za pomocą copy()
kopia1 = slownik.copy()

# Kopiowanie za pomocą dict()
kopia2 = dict(slownik)

print(kopia1)  # Wyświetli: {'a': 1, 'b': 2}
print(kopia2)  # Wyświetli: {'a': 1, 'b': 2}


# 17. Klasy
