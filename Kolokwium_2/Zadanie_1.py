# Zadanie 1.
# 1.1 Utwórz klasę o nazwie Restaurant. Metoda __init__() w tej klasie powinna przyjmować i
# przypisywać do instancji klasy cztery atrybuty: name, menu_type, open oraz close przechowujące
# odpowiednio nazwę restauracji, typ serwowanej kuchni, godzinę otwarcia i godzinę zamknięcia.
# Utwórz metodę o nazwie describe() wyświetlającą nazwę restauracji i typ kuchni oraz metodę
# working_hours() wyświetlającą informację o godzinach otwarcia restauracji.
# Utwórz obiekt klasy Restaurant i wyświetl jego atrybuty oraz wywołaj jego metody
# 1.2 Utwórz trzy różne instancje klasy Restaurant, a następnie dla każdego z nich wywołaj metodę
# describe().
# 1.3 Utwórz klasę User, która będzie przechowywała imię, nazwisko i wiek użytkownika. Klasa
# powinna zawierać także metodę describe() wyświetlającą informacje o użytkowniku na
# podstawie atrybutów oraz metodę greet() wyświetlającą spersonalizowane powitanie
# użytkownika.

class Restaurant:
    def __init__(self, name: str, menu_type: str, open: str, close: str):
        """
        Konstruktor Klasy. Wywołuje się w momencie stworzenia obiektu np. restauracja_1 =
        Restaurant(name='Pizza Hut', menu_type='Włoska', open='11:00', close='22:00').
        W nawiasach są argumenty które potem przypisujemy do odpowiednich atrybutów niżej
        przu użyciu słowa self.
        :param name:
        :param menu_type:
        :param open:
        :param close:
        """
        self.name = name
        self.menu_type = menu_type
        self.open = open
        self.close = close

    def describe(self) -> None:
        print("Opis Restauracji: ")
        print(f'Nazwa: {self.name}')
        print(f'Typ kuchni: {self.menu_type}')

    def working_hours(self) -> None:
        print("Godziny otwarcia restauracji: ")
        print(f'Godzina otwarcia: {self.open}')
        print(f'Godzina zamknięcia: {self.close}')


class User:
    def __init__(self, imie: str, nazwisko: str, wiek: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def describe(self) -> None:
        print(f'Imie: {self.imie}')
        print(f'Nazwisko: {self.nazwisko}')
        print(f'Wiek: {self.wiek}')

    def greet(self) -> None:
        print(f'Witaj {self.imie} {self.nazwisko}!')

