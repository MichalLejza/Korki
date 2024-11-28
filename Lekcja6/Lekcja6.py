# 14.11.24
# Klasy

# Postać
# poziom życia
# poziom ataku
# zaopatrzenie
# imie
# maksymalny poziom statystyki
# ubiór

# Komis Samochodowy
# Ogólnie Samochód to jest klasa -> mogą być nazwa samochodu, model, rocznik itp.
# Indywidualny dany Samochód danej marki, modelu itp... To obiekt tej klasy


# 1. Wprowadzenie do Programowania Obiektowego (OOP)
# Programowanie Obiektowe (Object-Oriented Programming, OOP) to paradygmat
# programowania, który organizuje kod wokół obiektów i klas. OOP skupia się
# na odwzorowaniu realnego świata poprzez tworzenie obiektów, które mogą mieć
# swoje właściwości (atrybuty) i zachowania (metody).

# Podstawowe zasady OOP: abstrakcja, enkapsulacja, dziedziczenie i polimorfizm.
# Abstrakcja: Pozwala na skupienie się na istotnych właściwościach obiektów,
# pomijając mniej istotne detale. Dzięki abstrakcji możemy stworzyć klasy
# reprezentujące ogólne pojęcia, jak np. Samochód czy Zwierzę.
#
# Enkapsulacja: Polega na ukrywaniu szczegółów implementacyjnych wewnątrz
# obiektu i udostępnianiu jedynie tych, które są niezbędne. W Pythonie
# enkapsulację osiągamy poprzez stosowanie prywatnych atrybutów lub metod.
#
# Dziedziczenie: Pozwala na tworzenie nowych klas bazujących na już
# istniejących, co pozwala na wielokrotne wykorzystanie kodu. Klasa
# pochodna (subklasa) może dziedziczyć atrybuty i metody klasy bazowej.
#
# Polimorfizm: Daje możliwość używania tego samego interfejsu w różnych
# kontekstach. Polimorfizm pozwala na używanie różnych klas w ten sam sposób,
# jeśli implementują one te same metody

# Dlaczego warto stosować klasy i obiekty.

class PostacWGrze:
    maksymalnyPoziom = 99

    def __init__(self, imie, atak, zycie):
        self.imie = imie
        self.atak = atak
        self.zycie = zycie

    def wypiszInformacje(self):
        print("Informacje o postaci:")
        print(f"Imie: {self.imie}")
        print(f"Atak: {self.atak}")
        print(f"Zycie: {self.zycie}")
        print(f"Max Poziom: {self.maksymalnyPoziom}")

    def podniesPoziomAtaku(self):
        self.atak = self.atak + 1

    def zmienImie(self, noweImie):
        self.imie = noweImie


geralt = PostacWGrze("Geralt", 20, 100)
geralt.wypiszInformacje()
geralt.zmienImie("Yennefer")
geralt.wypiszInformacje()


# 2. Definiowanie Klas i Obiektów
# Klasy to szablony, na podstawie których tworzone są obiekty.
# W Pythonie klasę definiujemy za pomocą słowa kluczowego class.
# Każdy obiekt jest instancją klasy, co oznacza, że ma dostęp do jej atrybutów i metod.

# Słowo kluczowe class, struktura klasy.
class Samochod:
    # Konstruktor klasy (metoda __init__ omówiona w punkcie 3)
    liczba_kol = 4  # atrybut klasy

    def __init__(self, marka, model, rok):
        self.marka = marka  # atrybut instancji
        self.model = model  # atrybut instancji
        self.rok = rok  # atrybut instancji

    def opis(self):  # Metoda instancji
        return f"{self.marka} {self.model}"

    @classmethod
    def marka_ogolna(cls, model):
        return cls("Ogólna marka", model, 2022)

    @staticmethod
    def oblicz_spalanie(dystans, paliwo):
        return dystans / paliwo


# Tworzenie instancji (obiektów) klasy.
moj_samochod = Samochod("Toyota", "Corolla", 2022)
print(moj_samochod.marka)  # Wynik: Toyota

# 3. Inicjalizacja Obiektów
# Metoda __init__() i jej rola w inicjalizacji obiektów.
# Aby zainicjalizować obiekt (czyli przypisać mu konkretne wartości atrybutów),
# korzystamy z metody specjalnej __init__(), która jest wywoływana automatycznie
# podczas tworzenia instancji klasy. Jest to tzw. konstruktor, który pozwala na
# nadanie wartości początkowych atrybutom obiektu.

# Argument self i jego znaczenie.
# W __init__ i innych metodach klasy self to pierwszy parametr, który zawsze odnosi się do instancji danej klasy.
# self pozwala na dostęp do atrybutów i metod obiektu zdefiniowanych w klasie.
# self nie musi być nazwany właśnie tak, ale jest to konwencja w Pythonie.

auto = Samochod("Ford", "Mustang", 2023)
print(f"Samochód: {auto.marka} {auto.model} ({auto.rok})")  # Wynik: Samochód: Ford Mustang (2023)

# 4. Atrybuty i Metody
# W klasach w Pythonie rozróżniamy atrybuty oraz metody, które mogą
# być związane z konkretną instancją (obiektem) lub z samą klasą.

# Atrybuty instancji i atrybuty klasy.
# Atrybuty instancji to zmienne, które są specyficzne dla danego obiektu
# (instancji klasy). Są definiowane zwykle wewnątrz metody __init__, używając self.
# Każdy obiekt może mieć różne wartości dla tych atrybutów, co oznacza,
# że mogą one różnić się między instancjami tej samej klasy.
auto1 = Samochod("Toyota", "Corolla", 2024)
auto2 = Samochod("Honda", "Civic", 2021)
print(auto1.marka)  # Wynik: Toyota
print(auto2.marka)  # Wynik: Honda
# W powyższym przykładzie marka i model są atrybutami instancji, przypisanymi do konkretnego obiektu auto1 lub auto2.

# Atrybuty klasy są wspólne dla wszystkich instancji danej klasy.
# Są definiowane bezpośrednio w klasie (poza metodą __init__) i są
# współdzielone przez wszystkie obiekty tej klasy.
# Możemy uzyskać do nich dostęp za pomocą nazwy klasy (ClassName.attribute)
# lub przez self.attribute, ale zmiana wartości przez instancję może prowadzić
# do utworzenia nowego atrybutu instancji o tej samej nazwie.
print(auto1.liczba_kol)  # Wynik: 4
print(auto2.liczba_kol)  # Wynik: 4
print(Samochod.liczba_kol)  # Wynik: 4
# W tym przypadku liczba_kół jest atrybutem klasy, współdzielonym przez wszystkie obiekty klasy Samochód.

# Metody instancji, atrybuty obiektowe oraz metody klasy.
# Metody instancji operują na danych konkretnego obiektu (instancji) i mają dostęp do self.
# Są to najczęściej stosowane metody w klasach, ponieważ pozwalają na pracę z danymi konkretnej instancji.
print(auto1.opis())

# @classmethod oraz @staticmethod – kiedy i jak je stosować.
# Metody klasy mają dostęp do samej klasy (nie do instancji) i korzystają z argumentu
# cls, który jest odniesieniem do klasy, podobnie jak self jest odniesieniem do instancji.
# Metody klasy są oznaczane dekoratorem @classmethod. Są często używane do tworzenia
# alternatywnych konstruktorów (np. metod tworzących instancje klasy na podstawie danych wejściowych).

auto = Samochod.marka_ogolna("Sedan")
print(auto.marka)  # Wynik: Ogólna marka

# Metody statyczne to metody, które nie mają dostępu ani do instancji (self),
# ani do klasy (cls). Są to zwykłe funkcje, które są umieszczone wewnątrz klasy
# ze względu na logiczne powiązanie.
# Używamy dekoratora @staticmethod do oznaczenia metod statycznych. Metody te
# nie modyfikują stanu klasy ani instancji, ale mogą być przydatne do wykonania
# operacji związanych z klasą.

# Użycie metody statycznej
print(Samochod.oblicz_spalanie(100, 5))  # Wynik: 20.0

# Enkapsulacja
# Atrybuty prywatne (np. _nazwa i __nazwa).
# Użycie metod getter i setter.


# Dziedziczenie
# Tworzenie klas bazowych i klas pochodnych.
# Użycie super() do dziedziczenia i rozszerzania funkcjonalności klasy bazowej.
# Modyfikacja i nadpisywanie metod.


# Polimorfizm i Przeładowanie Metod
# Definicja polimorfizmu i jego znaczenie w OOP.
# Przykłady nadpisywania metod.


# Metody Specjalne (Magic Methods)
# __str__() i __repr__() do wyświetlania obiektów.
# __len__(), __getitem__(), __setitem__() i inne metody specjalne.

class Pies:
    def __init__(self, rasa, kolor, rokUrodzenia):
        self.rasa = rasa
        self.kolor = kolor
        self.rokUrodzenia = rokUrodzenia

    def opiszPsa(self):
        print(f"Pies {self.rasa} {self.kolor}")

    def __str__(self):
        return f"Pies {self.rasa} {self.kolor}"

    def __repr__(self):
        pass

    def __len__(self):
        pass


class Macierz:
    def __init__(self, liczbaWierszy, liczbaKolumn):
        self.liczbaWierszy = liczbaWierszy
        self.liczbaKolumn = liczbaKolumn
        self.tablica = [[0 for _ in range(liczbaKolumn)] for _ in range(liczbaWierszy)]

    def wypiszMacierz(self):
        for i in range(self.liczbaWierszy):
            for j in range(self.liczbaKolumn):
                print(self.tablica[i][j], end=" ")
            print()
        print()

    def __eq__(self, other):
        if self.liczbaWierszy == other.liczbaWierszy and self.liczbaKolumn == other.liczbaKolumn:
            return True
        else:
            return False

    def dodajMacierz(self, macierz):
        if self == macierz:
            for i in range(self.liczbaWierszy):
                for j in range(self.liczbaKolumn):
                    self.tablica[i][j] += macierz.tablica[i][j]
        else:
            print("Wymiary sie nie zgadzają")


macierz1 = Macierz(2, 2)
macierz2 = Macierz(3, 3)

macierz1.wypiszMacierz()
macierz2.wypiszMacierz()

macierz2.dodajMacierz(macierz1)
macierz2.wypiszMacierz()



# Kompozycja i Agregacja
# Różnica między kompozycją a dziedziczeniem.
# Jak tworzyć klasy składające się z innych klas.


# Przykłady Zastosowania Klas
# Proste przykłady klas reprezentujących realne obiekty,
# np. klasę Samochód, Osoba lub BankAccount.
