# FUNKCJE

# definicja funkcji - powtórzenie # f(x) f jest funkcją a x arhumentem funkcji
def nazwaFunkcji(argumenty: int, argument2: float) -> None:
    if argumenty > argument2:
        print()

# zastosowania funkcji w programowaniu

# Podstawowa składnia definiowania funkcji

# Słowo kluczowe def oraz składnia def funkcja():

# Nazwa funkcji i zasady jej tworzenia

# Przykład prostej funkcji bez parametrów i zwracania wartości

# Parametry pozycyjne


def funkcja2(argument1: int, argument2: int) -> int:
    return argument1 + argument2


wynik = funkcja2(1, 4)


def funkcja3(lista: list, argument: int) -> None:
    for i in range(len(list)):
        lista[i] *= argument


funkcja3([1, 2, 3], 5)
funkcja3(lista=[1, 2, 3], argument=5)
funkcja3(argument=3, lista=[1, 2, 3])


# Argumenty opcjonalne (wartości domyślne)

def funkcja4(argument1: int = 1, argument2: int = 1) -> None:
    print(argument1 + argument2)


zmienna1 = 9
funkcja4()


# Jak zwracać wartość z funkcji

def funkcja5(argument1: int = 1, argument2: int = 1) -> int:
    return argument1 + argument2


zmienna: int = funkcja5(argument1=1, argument2=2)

# Różnica między return a print


# Zwracanie wielu wartości (np. return a, b)
def funkcja6(argument1: int = 1, argument2: int = 1) -> tuple:
    return argument1, argument2, argument2 * 2


zmienna2 = funkcja5(1, 2)

zmiennaPierwsza, zmiennaDruga = funkcja6(3, 4)
# Zmienna lokalna vs. globalna

zmiennaX = 9  # zmienna globalna


def fun():
    zmiennaY = 10  # zmienna lokalna
    global zmiennaX
    zmiennaX = 5


# Funkcje zagnieżdżone (nested functions)

def funkcja7(argument1: int = 1, argument2: int = 1) -> None:
    zmiennaB = 10
    zmiennaA = 5

    def policzMiSume(x, y) -> int:
        return x + y

    wynikSuma = policzMiSume(zmiennaA, zmiennaB)
    print(wynikSuma)


x = 10

for i in range(x):
    print()
    print()
    print()


def funkncjaRekurencyjne(X):
    if X > 0:
        print(X)
        funkncjaRekurencyjne(X - 1)

funkncjaRekurencyjne()
