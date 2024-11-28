# Lekcja 7
# 21.11.24

# Powtrórzenie klas
# atrybuty
# funkcje
# konstruktor

def vjio(x=None, y=None):
    pass


vjio(x=10)


class Dom:
    def __init__(self, x=None, y=None):
        self._liczbaPokoi = x
        self._dlugosc = 15
        self._wysokosc = 10
        self._metraz = y

    # setter
    def ustawLiczbePokoi(self, liczbaPokoi):
        if type(liczbaPokoi) is int:
            self._liczbaPokoi = liczbaPokoi
        else:
            print("To co podałeś to nie jest liczba")

    def zwrocMiLiczbePokoi(self):
        return self._liczbaPokoi

    @classmethod
    def funkcjaKlasowa(cls, a=None, b=None):
        pass

    @staticmethod
    def funkcjaStatytczna(a=None, b=None):
        print("2 + 2 = 4")

    def funkcja(self, a=None, b=None):
        self._liczbaPokoi = a
        self._dlugosc = b
        self._wysokosc = 10
        self._metraz = b
        print("Jestem teraz w funkcji")


dom1 = Dom(y=120, x=3)
dom1.ustawLiczbePokoi(liczbaPokoi="jhgiow")
liczba = dom1.zwrocMiLiczbePokoi()
print(liczba)

# Enkapsulacja
