# Zadanie 4
#  Utwórz w projekcie nowy moduł funkcje.py, do którego skopiuj funkcję srednia z zadania
# trzeciego
#  W module funkcje.py napisz funkcję file_to_list(plik, sep, enc), której argumentami będą:
# - plik – string przechowujący nazwę pliku
# - sep – string przechowujący symbol separatora danych
# - enc – string opisujący kodowanie pliku, któremu przypisz wartość domyślną ‘UTF-8’
# Funkcja na podstawie pliku wejściowego w formacie identycznym jak w zadaniach 1 i 2 ma
# utworzyć i zwrócić listę 2D przechowującą informację pozyskaną z pliku w formie stringów,
# np.:
# [['WARSZOWICE', '2001', '01', '54.1']
# ['WARSZOWICE', '2001', '02', '31.0']
# ['WARSZOWICE', '2001', '03', '47.8']
# ['STARY FOLWARK', '2001', '12', '30.1']]
#  Utwórz moduł zad_04.py do którego zaimportuj funkcję file_to_list(plik, sep, enc), a
# następnie użyj jej do utworzenia listy 2D na podstawie danych zapisanych w pliku opady.csv
from funkcje import file_to_list


lista: list = file_to_list('opady.csv', ';', 'utf-8')
print(lista)


