# Projekt Informatyczny: System Zarządzania Osobami w Szkole

# Temat zadania:
# Stwórz system zarządzania osobami w szkole z wykorzystaniem dziedziczenia w Pythonie.
# System ma pozwalać na przechowywanie informacji o podstawowych cechach osoby oraz
# specyficznych cechach uczniów i nauczycieli.

# Specyfikacja projektu:

# Klasa bazowa: Osoba
# Atrybuty:
# - imie (imię Osoby, np. "Jan")
# - nazwisko (nazwisko Osoby, np. "Kowalski")
# - wiek (wiek Osoby, np. 30)
# Metody:
# - przedstaw_sie() - wypisuje informacje o imieniu, nazwisku i wieku.

# Klasa pochodna: Uczen Dziedziczy z klasy Osoba.
# Dodatkowe atrybuty:
# - klasa (klasa szkolna, np. "4B")
# - srednia_ocen (średnia ocen ucznia, np. 4.5)
# Metody:
# - przedstaw_sie() - rozszerza metodę z klasy Osoba, dodając informację o klasie i średniej ocen.
# Klasa pochodna: Nauczyciel Dziedziczy z klasy Osoba.
# Dodatkowe atrybuty:
# - przedmiot (nauczany przedmiot, np. "Matematyka")
# - stawka_godzinowa (stawka godzinowa nauczyciela, np. 50 zł/h)
# Metody:
# - przedstaw_sie() - rozszerza metodę z klasy Czlowiek, dodając informację o nauczanym przedmiocie i stawce godzinowej.

# Wymagania funkcjonalne:
# Program powinien umożliwiać:
# Tworzenie obiektów klasy Osoba, Uczen oraz Nauczyciel.
# Wyświetlanie szczegółowych informacji o obiektach za pomocą metody przedstaw_sie().
