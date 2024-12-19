class Czlowiek:
    def __init__(self, Imie, Nazwisko, Pesel, MiejsceUrodzin):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.Pesel = Pesel
        self.MiejsceUrodzin = MiejsceUrodzin
        self.Wzrost = 0.0
        self.Wiek = 0

    def PoliczWiek(self) -> int:
        return 2024 - self.Wiek

    def UstawImie(self, noweImie):
        self.Imie = noweImie


class Nauczyciel(Czlowiek):
    def __init__(self, Imie, Nazwisko, Pesel, MiejsceUrodzin):
        super().__init__(Imie, Nazwisko, Pesel, MiejsceUrodzin)
        self.UstawImie('Anna')

    def DodajOcene(self , ocena):
        print(f'Nauczyciel {self.Imie} {self.Nazwisko} wystawił ocenę {ocena}')


class Uczen(Czlowiek):
    def __init__(self, Imie, Nazwisko, Pesel, MiejsceUrodzin):
        super().__init__(Imie, Nazwisko, Pesel, MiejsceUrodzin)

    def PokazOcenę(self):
        print(f'Uczen {self.Imie} {self.Nazwisko} próbuje wyszukać ocenę')


class Dyrektor(Czlowiek):
    def __init__(self, Imie, Nazwisko, Pesel, MiejsceUrodzin):
        super().__init__(Imie, Nazwisko, Pesel, MiejsceUrodzin)

    def DodajNauczyciela(self):
        print(f'Dyrektor {self.Imie} {self.Nazwisko} dodaje nauczyciela')

    def UstawImie(self, noweImie):
        self.Imie = noweImie
        print("Klasa Dyrektor zmienia imie")


czlowiek = Czlowiek("Jan", "Kowalski", "12345678901", "Warszawa")
nauczyciel = Nauczyciel("Jan", "Kowalski", "12345678901", "Warszawa")
nauczyciel.DodajOcene(5)