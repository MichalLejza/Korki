# 10.11.24

# Zadanie 1: Tłumacz liczb na słowa
# Utwórz słownik, który będzie tłumaczył cyfry (0–9) na
# odpowiadające im słowa, np. 0 – „zero”, 1 – „jeden”, itp.
# Napisz program, który poprosi użytkownika o podanie cyfry, a
# następnie zwróci odpowiednie słowo. Jeśli użytkownik poda coś
# spoza zakresu, wyświetl komunikat "Nieznana cyfra".
#
# Przykładowe dane wejściowe i wyjściowe:
#
# Wejście: 2
# Wyjście: dwa

def Zadanie1():
    slownik_cyfr = {
        0: "Zero",
        1: "Jeden",
        2: "Dwa",
        3: "Trzy",
        4: "Cztery",
        5: "Piec",
        6: "Szesc",
        7: "Siedem",
        8: "Osiem",
        9: "Dziewiec"
    }

    while True:
        liczbaPobrana = int(input("Podaj liczbe do tlumaczenia: "))
        # klucz = slownik_cyfr[liczbaPobrana]
        klucz = slownik_cyfr.get(liczbaPobrana, "Ni ma")
        print(klucz)


Zadanie1()


# Zadanie 2: Książka telefoniczna
# Opis: Utwórz prostą książkę telefoniczną jako słownik, w
# którym kluczami będą imiona, a wartościami – numery telefonów.
# Program powinien umożliwiać dodawanie nowych kontaktów oraz
# wyszukiwanie numeru na podstawie imienia.
#
# Przykładowe dane wejściowe i wyjściowe:
#
# Wejście: Imię: Jan, Numer: 123456789
# Zapytanie: Podaj imię, aby znaleźć numer
# Wyjście: Numer telefonu dla Jan: 123456789

def Zadanie2():
    pass

# Zadanie 3: Liczenie wystąpień słów
# Opis: Napisz program, który zliczy wystąpienia słów w zdaniu
# podanym przez użytkownika. Użyj słownika, gdzie kluczami będą
# słowa, a wartościami – liczba ich wystąpień.
#
# Przykładowe dane wejściowe i wyjściowe:
#
# Wejście: ala ma kota ala ma psa
# Wyjście: {'ala': 2, 'ma': 2, 'kota': 1, 'psa': 1}


def Zadanie3():
    pass

# Zadanie 4: Aktualizacja zapasów
# Opis: Załóżmy, że prowadzisz mały sklep i masz słownik z
# ilościami dostępnych produktów. Program powinien umożliwiać
# zwiększanie lub zmniejszanie liczby zapasów produktu. Jeśli
# produkt nie istnieje, dodaj go do słownika.
#
# Przykładowe dane wejściowe i wyjściowe:
#
# Wejście: Produkt: jabłko, Ilość: 10
# Wyjście: {'jabłko': 10}


def Zadanie4():
    pass

# Zadanie 5: Rejestr ocen
# Opis: Utwórz słownik, w którym kluczami będą imiona uczniów,
# a wartościami – listy ich ocen. Program powinien umożliwiać
# dodanie nowej oceny do listy dla danego ucznia oraz obliczanie
# średniej ocen dla wybranego ucznia.
#
# Przykładowe dane wejściowe i wyjściowe:
#
# Wejście: Uczeń: Anna, Ocena: 5
# Wyjście: Oceny Anny: [5, 4, 3]
# Średnia ocen Anny: 4.0


def Zadanie5():
    pass


# Zadanie 6: Two Sum
# Napisz funkcję two_sum(nums, target), która przyjmuje:
#
# listę liczb całkowitych nums, oraz
# liczbę całkowitą target.
# Cel: Funkcja powinna znaleźć dwa różne indeksy elementów w nums,
# które sumują się do wartości target, i zwrócić te indeksy w postaci listy [index1, index2].
#
# Założenia:
#
# Każde wejście ma dokładnie jedno rozwiązanie.
# Tego samego elementu nie można użyć dwa razy.
# Indeksy mogą być zwrócone w dowolnej kolejności.
# Przykłady
# Wejście: nums = [2, 7, 11, 15], target = 9
#
# Wyjście: [0, 1]
# Wyjaśnienie: nums[0] + nums[1] = 2 + 7 = 9
# Wejście: nums = [3, 2, 4], target = 6
#
# Wyjście: [1, 2]
# Wyjaśnienie: nums[1] + nums[2] = 2 + 4 = 6

