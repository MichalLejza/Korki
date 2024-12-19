# Lekcja 8 28.11.24
# Dziedziczenie klas

# Klasa bazowa
# Klasa bazowa (ang. base class lub parent class) to klasa, która
# jest podstawą dla innych klas. Udostępnia atrybuty i metody, które
# mogą być dziedziczone przez klasy pochodne. Dzięki klasom bazowym można
# ponownie wykorzystać kod, unikając duplikacji.

class Pojazd:
    def __init__(self, marka, model, max_speed):
        self.marka = marka
        self.model = model
        self.max_speed = max_speed

    @staticmethod
    def bazowa():
        print("Metoda dla klasy Pojazd: ")
        print("Ta metoda może byc wywołana tylko w tej klasie i ewentualnie w klasach pochodnych")

    def opis(self):
        print("Metoda dla klasy Pojazd: ")
        print(f"Marka: {self.marka}, model: {self.model}, max_speed: {self.max_speed}")


# Klasa Pochodna
# Klasa pochodna (ang. derived class lub child class) to klasa,
# która dziedziczy cechy i metody z klasy bazowej. Może również
# dodawać własne atrybuty i metody lub zmieniać istniejące metody klasy bazowej.

class Motocykl(Pojazd):
    def __init__(self, marka, model, max_speed):
        super().__init__(marka, model, max_speed)
        self.typ = 'Motocykl'

    @staticmethod
    def pochodna():
        print("Metoda dla klasy Motocykl: ")
        print("Ta metoda może byc wywołana tylko w tej klasie i ewentualnie w klasach pochodnych")

    def opis(self):
        print("Metoda dla klasy Motocykl: ")
        print(f"Typ: {self.typ}, Marka: {self.marka}, model: {self.model}, max_speed: {self.max_speed}")


m1 = Motocykl('BMW', 'jakies', '260')
m1.bazowa()
m1.pochodna()
m1.opis()

# Jak działa dziedziczenie w Pythonie
# Dziedziczenie w Pythonie to mechanizm pozwalający jednej klasie (klasie pochodnej)
# korzystać z atrybutów i metod zdefiniowanych w innej klasie (klasie bazowej).
# Dzięki temu klasy pochodne mogą:
# - Ponownie wykorzystywać istniejący kod, co zmniejsza jego duplikację.
# - Rozszerzać lub zmieniać funkcjonalność klasy bazowej, tworząc bardziej specjalistyczne klasy.

# Cechy dziedziczenia:
# - Relacja "jest rodzajem": Klasa pochodna jest szczególnym
#   przypadkiem klasy bazowej (np. pies jest rodzajem zwierzęcia).
# - Hierarchia klas: Klasy bazowe mogą mieć wiele klas pochodnych.
# - Mechanizm super(): Pozwala odwoływać się do klasy bazowej w klasie pochodnej.

# Jak tworzyć klasy bazowe i pochodne
# Klasa bazowa to zwykła klasa, która definiuje wspólne cechy i metody dla innych klas.
# Jest tworzona przy użyciu słowa kluczowego class.
# Klasa pochodna jest tworzona poprzez podanie klasy bazowej w nawiasach podczas deklaracji.
# Klasa pochodna automatycznie dziedziczy metody i atrybuty klasy bazowej.

# Jak korzystać z metod i atrybutów w klasach dziedziczących
# 1. Klasa pochodna może używać wszystkich metod zdefiniowanych w klasie bazowej bez ich redefiniowania.
# 2. Klasa pochodna może definiować nowe metody i atrybuty, które nie istnieją w klasie bazowej.
# 3. Klasa pochodna może nadpisać metodę z klasy bazowej, dodając do niej nowe zachowanie.
#    Używa się wtedy funkcji super() do wywołania oryginalnej metody klasy bazowej.
# 4. Atrybuty klasy bazowej mogą być używane i modyfikowane w klasie pochodnej.

# Jak nadpisywać metody w klasach pochodnych
# Przesłanianie metod (ang. method overriding) polega na nadpisywaniu
# metod zdefiniowanych w klasie bazowej w klasie pochodnej. Dzięki temu
# klasa pochodna może zmienić zachowanie metody klasy bazowej w celu
# dostosowania jej do swoich potrzeb.
