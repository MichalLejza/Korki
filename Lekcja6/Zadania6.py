# 14.11.24
# Zadania Klasy

# Zadanie 1: Tworzenie Prostej Klasy
# Opis: Stwórz klasę Samochód, która będzie miała dwa atrybuty instancji:
# marka oraz model. Dodaj metodę opis, która zwróci tekst w formacie "Marka Model".
# Przykład użycia:

# auto = Samochód("Toyota", "Corolla")
# print(auto.opis())  # Powinno wyświetlić: Toyota Corolla


# Zadanie 2: Dodawanie Atrybutu Klasy
# Opis: Dodaj do klasy Samochód atrybut klasy liczba_kół, który będzie wynosił 4
# (zakładamy, że każdy samochód ma 4 koła). Napisz metodę pokaż_koła, która wyświetli,
# ile kół ma samochód.
# Przykład użycia:

# auto = Samochód("Honda", "Civic")
# print(auto.liczba_kół)  # Powinno wyświetlić: 4


# Zadanie 3: Tworzenie Metod Instancji i Statycznych
# Opis: W klasie Samochód dodaj metodę instancji przyspiesz, która przyjmuje
# parametr prędkość i wyświetla komunikat "Samochód przyspiesza do X km/h",
# gdzie X to wartość parametru. Następnie dodaj metodę statyczną info, która
# wyświetli komunikat "Samochód to pojazd lądowy".
# Przykład użycia:

# auto = Samochód("Mazda", "CX-5")
# auto.przyspiesz(80)  # Powinno wyświetlić: Samochód przyspiesza do 80 km/h
# Samochód.info()      # Powinno wyświetlić: Samochód to pojazd lądowy


# Zadanie 4: Tworzenie Alternatywnego Konstruktora
# Opis: Dodaj do klasy Samochód metodę klasy z_domyslną_marką, która przyjmuje
# parametr model i tworzy obiekt Samochód o marce "Nieznana", ale z podanym
# modelem. Użyj dekoratora @classmethod.
# Przykład użycia:

# auto = Samochód.z_domyslną_marką("Model S")
# print(auto.opis())  # Powinno wyświetlić: Nieznana Model S


# Zadanie 5: Tworzenie Listy Obiektów
# Opis: Stwórz listę obiektów klasy Samochód, gdzie każdy obiekt ma inną markę
# i model. Napisz pętlę, która przejdzie przez listę i wyświetli opis każdego samochodu.
# Przykład użycia:

# auta = [Samochód("Ford", "Mustang"), Samochód("BMW", "X3"), Samochód("Audi", "A4")]
# for auto in auta:
#     print(auto.opis())
# # Powinno wyświetlić:
# # Ford Mustang
# # BMW X3
# # Audi A4
