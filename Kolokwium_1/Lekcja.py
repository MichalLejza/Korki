# Lekcja 28.11.24
# 1. Zmienne
# 1.1 liczby całkowite (int)
# 1.2 liczby zmiennoprzecinkowe (float)
# 1.3 liczby urojone (complex)
# 1.4 wartości Logiczne (bool)
# 1.5 wartości typu None
# 1.6 ciągi znaków (string) lub (str)
# 1.7 sprawdzanie typów zmiennych


# 2. Operatory
# 2.1 dodawanie
# 2.2 odejmowanie
# 2.3 mnożenie
# 2.4 dzielenie całkowite
# 2.5 dzielenie pełne
# 2.6 modulo
# 2.7 potęgowanie
# 2.8 inkrementacja
# 2.9 dekrementacja


# 3. Instrukcje Sterowania przepływem
# 3.1. if-elif-else
# 3.2 operator ternarny (skrócoy if-else)


# 4. Pętle
# 4.1 pętla for od zera do liczby w nawiasach range
# 4.2 pętla for od liczby do liczby w nawiasach range
# 4.3 pętla for od liczby do liczby w nawiasach ale inkrementuje o ostatnią liczbę w nawiasach range
# 4.4 pętla for od 0 do długości napisu. indeks to tylko liczba (index)
# 4.5 pętla for od 0 do długości napisu. element to litera w napisie (character)
# 4.6 pętla while


# 5. Input/Output
# 5.1 wyświetlanie na ekranie
# 5.2 pobieranie danych z terminala


# 6. Losowanie Liczb
# 6.1 randomowa liczba od zakresu z zakresu [0, 1)
zmienna: float = random.random()
print(zmienna)

# 6.2 randomowa liczba całkowita z zakresu [X, Y)
zmienna: int = random.randint(1, 10)
print(zmienna)

# 6.3 randomowa liczba zmiennoprzecinkowa z zakresu [X, Y)
zmienna: float = random.uniform(1.5, 5.5)
print(zmienna)

# 6.4 randomowa liczba całkowita z zakresu [X, Y) ale z krokiem danym
zmienna: int = random.randrange(0, 20, 2)
print(zmienna)

# 6.5 randomowa liczba z listy
lista: list[int] = [1, 2, 3, 4, 5]
zmienna: int = random.choice(lista)
print(zmienna)

# 6.6 K randomowych liczb z danego zbioru liczb
lista: list = random.sample([1, 2, 3, 4, 5], 3)
print(lista)


# 7. Listy
# 7.1 pusta lista
# 7.2 lista z podanymi liczbami
# 7.3 lista z wygenerowanymi liczbami przez pętle enhanced for
# 7.4 zmiana poszczególnych wartości w liście
# 7.5 odczytywanie wartości z listy
# 7.6 przechodzenie po liście po indeksach
# 7.7 przechodzenie po liście ale po wartościach:
# 7.8 dodawanie pojedynczego elementów do listy
# 7.9 dodawanie kilku elementów (podanych w liście) do listy
# 7.10. usuwanie elementu z listy
# 7.11 sortowanie listy
# 7.12 odwrananie listy
# 7.13 czyszczenie całej listy


# 8. Tuple
# 8.1. tworzenie krotki
# 8.2. dostęp do elementów
# 8.3. operacje na krotkach
# 8.4. rozpakowywanie krotek


# 9. Zbiory
# 9.1 tworzenie zbiorów
# 9.2 dodawanie elementów
# 9.3 usuwanie elementów
# 9.4 operacje na zbiorach
# 9.5 sprawdzanie przynależności
# 9.6 typy danych w zbiorze
# 9.7 coprehension zbioru
# 9.8 iteracja po zbiorze


# 10. Mapy
# 10.1 tworzenie słownika
# 10.2 dostęp do wartości
# 10.3 pobieranie wartości, drugi argument jest zwracany jeśli nie ma klucza
# 10.4 dodawanie i aktualizowanie kluczy
# 10.5 usuwanie kluczy
# 10.6 sprawdzanie obecności klucza
# 10.7 Iteracja po słowniku
# 10.8 Iteracja po kluczach
# 10.9 Iteracja po wartościach
# 10.10 Iteracja po parach klucz-wartość
# 10.11 Kopiowanie słownika


# 11. Funkcje
# 11.1 deklarowanie funkcji bez argumentów:
# 11.2 deklarowanie funkcji z argumentami:
# 11.3 return
# 11.4 funkcja zagnieżdżona
# 11.5 argumenty pozycyjne
# 11.6 zmienne lokalne i globalne


# 12. Napisy
# 12.1 deklarowanie napisu pustego
napis: str = ""
napis: str = ''

# 12.2 deklarowanie napisu nie pustego
napis: str = "Napis"
napis: str = 'Napis'

# łącznie napisów
napis: str = "Hehe" + " HAHA"

# pobieranie znaku z określonego miejsca:
char: str = napis[0]

# pobieranie napisu od użytkownika
napis: str = input("Tu możesz coś wpisać ale nie musisz")

# metody do napisu
napis = "Przykładowy napis"
# Zwraca nowy napis z wszystkimi literami w małych literach.
napis: str = napis.lower()

# Zwraca nowy napis z wszystkimi literami w dużych literach.
napis: str = napis.upper()

# Zwraca nowy napis z pierwszą literą dużą, a pozostałymi małymi.
napis: str = napis.capitalize()

# Zwraca nowy napis z każdą pierwszą literą w słowie dużą.
napis: str = napis.title()

# Usuwa białe znaki z początku i końca napisu.
napis: str = napis.strip()

# Usuwa białe znaki tylko z początku napisu
napis: str = napisPierwszaDuza.lstrip()

# Usuwa białe znaki tylko z końca napisu.
napis: str = napis.rstrip()

# Łączy elementy iterowalnego obiektu (np. listy) w jeden napis, używając napisu jako separatora.
napis: str = napis.join([" Pierwsze", " Slowo", " Drugie", " Slowo"])

# Dzieli napis na listę podnapisów według separatora sep (domyślnie białe znaki).
lista: list = napis.split(" ")

# Zwraca indeks pierwszego wystąpienia podnapisu sub lub -1, jeśli nie znaleziono.
zmienna: int = napis.find("P")

# Zastępuje wszystkie wystąpienia old napisem new i zwraca nowy napis.
napis: str = napis.replace("P", "R")

# Zwraca liczbę wystąpień podnapisu sub w napisie.
zmienna: int = napis.count("P")

# Zwraca True, jeśli wszystkie znaki w napisie są literami.
logiczna: bool = napis.isalpha()

# Zwraca True, jeśli wszystkie znaki w napisie są cyframi.
logiczna: bool = napis.isdigit()

# Zwraca True, jeśli wszystkie znaki w napisie są literami lub cyframi.
logiczna: bool = napis.isalnum()

# Zwraca True, jeśli wszystkie litery w napisie są małe.
logiczna: bool = napis.islower()

# Zwraca True, jeśli wszystkie litery w napisie są duże.
logiczna: bool = napis.isupper()

# Zwraca True, jeśli wszystkie znaki w napisie to białe znaki.
logiczna: bool = napis.isspace()
