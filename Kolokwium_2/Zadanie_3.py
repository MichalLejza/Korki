from Zadanie_1 import Restaurant


# Zadanie 3
# 3.1 Budka z lodami to szczególny rodzaj restauracji. Utwórz klasę IceCreamStand dziedziczącą po
# klasie Restaurant. Do utworzonej klasy dodaj atrybut flavors przechowujący domyślnie listę trzech
# smaków. Następnie dodaj metodę add_flavor(), która rozszerzy tę domyślną listę o podany smak.
# Utwórz instancję klasy IceCreamStand i przetestuj działanie metody add_flavor().
# 3.2 Administrator to specjalny rodzaj użytkownika. Utwórz klasę Admin dziedziczącą po klasie User z
# zadania 1.3. Dodaj atrybut privileges przechowujący listę stringów z uprawnieniami
# administratora:
# ['może dodać post', 'może usunąć post', 'może zbanować użytkownika']
# W klasie Admin utwórz metodę show_privileges() wyświetlającą listę uprawnień administratora.
# Przetestuj działanie metody na instancji klasy Admin.
# 3.3 Zdefiniuj oddzielną klasę Privileges do której przenieś atrybut privileges i metodę
# show_privileges() z klasy Admin. Następnie w klasie Admin utwórz atrybut, który będzie
# przechowywał instancję klasy Privileges. Czy przy tak zmienionym kodzie można wywołać metodę
# show_privileges() dla instancji klasy Admin?

class IceCreamStand(Restaurant):
    def __init__(self, name: str, menu_type: str, open: str, close: str, flavors: list):
        super().__init__(close=close, open=open, name=name, menu_type=menu_type)
        self.flavors = flavors

    def add_flavour(self, smak: str) -> None:
        self.flavors.append(smak)


ics = IceCreamStand(name="Budka z lodami", menu_type="lody", open="10:00", close="21:00", flavors=["vanilla", "chocolate", "strawberry"])
ics.describe()
ics.working_hours()
print(ics.flavors)
ics.add_flavour('banana')
print(ics.flavors)




class Bazowa:
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2

    def print_argumenty(self):
        print("TUTAJ METODA Z KLASY BAZOWEJ")
        print(self.argument1, self.argument2)


class Pochodna(Bazowa):
    def __init__(self, argument1, argument2, argument3):
        super().__init__(argument1, argument2)
        self.argument3 = argument3

    def vhiwehviopw(self):
        print(self.argument1, self.argument2, self.argument3)

    # nadpisanie metody
    def print_argumenty(self):
        print("TUTAJ METODA Z KLASY POCHODNEJ")
        print(self.argument1, self.argument2, self.argument3)

pochodna = Pochodna(10, 2, 3)
pochodna.print_argumenty()
pochodna.vhiwehviopw()