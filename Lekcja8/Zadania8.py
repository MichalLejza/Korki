# Zadanie 1: Zwierzaki w Zoo
# W zoo znajdują się różne zwierzęta. Każde zwierzę ma pewne wspólne cechy,
# takie jak imię i wiek, ale różne gatunki mają też unikalne właściwości.
# Twoim zadaniem jest utworzenie klasy bazowej Zwierze oraz dwóch klas pochodnych Ptak i Ssak.

# Klasa Zwierze powinna zawierać:
# - Konstruktor inicjujący atrybuty imię i wiek.
# - Metodę przedstaw_sie(), która wypisuje imię i wiek zwierzęcia.

# Klasa Ptak powinna dziedziczyć po klasie Zwierze i dodawać:
# - Atrybut kolor_pior, który przechowuje kolor piór ptaka.
# - Przeciążoną metodę przedstaw_sie(), która dodatkowo wypisze kolor piór.

# Klasa Ssak powinna dziedziczyć po klasie Zwierze i dodawać:
# - Atrybut ulubiony_pokarm, który przechowuje ulubiony pokarm ssaka.
# - Przeciążoną metodę przedstaw_sie(), która dodatkowo wypisze ulubiony pokarm.

class Zwierze:
    def __init__(self, imie: str, wiek: int):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam sie {self.imie} i mam {self.wiek} lat')


class Ptak(Zwierze):
    def __init__(self, imie: str, wiek: int, kolor_pior: str):
        super().__init__(imie, wiek)
        self.kolor_pior = kolor_pior

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moj kolor pioru to {self.kolor_pior}')


class Ssak(Zwierze):
    def __init__(self, imie: str, wiek: int, ulubiony_pokarm: str):
        super().__init__(imie, wiek)
        self.ulubiony_pokarm = ulubiony_pokarm

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moj ulubiony pokarm to {self.ulubiony_pokarm}')


zwierze1 = Zwierze('Pies', 5)
zwierze1.przedstaw_sie()

ptak1 = Ptak('Kaczka', 2, 'Czarny')
ptak1.przedstaw_sie()

ssak1 = Ssak('Kot', 4, 'Pedigree')
ssak1.przedstaw_sie()

# Zadanie 2: Pojazdy
# Stwórz system, który opisuje różne typy pojazdów. Każdy pojazd ma wspólne cechy,
# ale istnieją różne rodzaje pojazdów, które mają swoje unikalne właściwości.
#
# Utwórz klasę bazową Pojazd, która zawiera:
# - Konstruktor ustawiający atrybuty marka i prędkość_max.
# - Metodę opis(), która wypisuje markę i maksymalną prędkość pojazdu.

# Utwórz klasę Samochod, która dziedziczy po klasie Pojazd i dodaje:
# - Atrybut liczba_drzwi, który przechowuje liczbę drzwi samochodu.
# - Przeciążoną metodę opis(), która wypisuje również liczbę drzwi.

# Utwórz klasę Motocykl, która dziedziczy po klasie Pojazd i dodaje:
# - Atrybut rodzaj, który określa rodzaj motocykla (np. "sportowy", "turystyczny").
# - Przeciążoną metodę opis(), która wypisuje również rodzaj motocykla.


