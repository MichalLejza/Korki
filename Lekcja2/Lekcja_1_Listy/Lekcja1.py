# Lista

zmienna1 = 2
zmienna2 = 3
zmienna3 = 4

# definicja pustej listy

lista: list = []
print(lista)

# definicja listy z elementami

lista1 = [1, 2, 3]

# dostęp do wartości w liście
print(lista1[0])
print(lista1[1])
print(lista1[2])

print(lista1[-1])
print(lista1[-2])
print(lista1[-3])

# dodawanie elemetów do listy
lista1.append([10, 11, 12])
print(lista1)
lista1.extend([4, 5, 6])
print(lista1)

# usuwanie elementów z listy

lista1.pop(-1)
print(lista1)

# przydatne funkcje list
# zliczanie danego elementu

lista2 = [1, 2, 4, 5, 5, 2, 3, 9, 8, 7, 6, 6, 6, 1]
x = lista2.count(5)
print(x)

# czyszczenie listy

lista1.clear()
print(lista1)

# sortowanie listy

lista2.sort()
print(lista2)

# odwracanie listy

lista2.reverse()
print(lista2)

# definicja list comprehension

lista3 = [i + i for i in range(10)]

lista31 = []
for i in range(10):
    lista31.append(i + i)

print(lista31)
print(lista3)

# lista wielu różnych typów
# lista list (wielowymiarowe listy)

lista4 = []
for i in range(10):
    listaDodajemy = []
    for j in range(10):
        listaDodajemy.append(j)
    lista4.append(listaDodajemy)


lista4[0][0] = 9
for i in range(10):
    print(lista4[i])


lista5 = [[i for i in range(10)] for j in range(10)]

# lista różnych typów zmiennych !!!

lista6 = [1, 2, 'Napis', 9.0, 2+2j]
print(lista6)


