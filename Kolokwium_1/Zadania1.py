import os

# Zadanie 1
# W pliku 'nazwiska.txt' w każdej linii zapisano małymi literami imię i nazwisko jednej osoby
# rozdzielone średnikiem:
# jan;kot
# marek;lis
# anna;kuna
# jacek;borsuk
# lew;lew
# Napisz program, który:
# 1. wczyta dane z pliku i zapisze je w postaci listy, której elementami będą obiekty str
# odpowiadające kolejnym liniom pliku:
# ['jan;kot\n', 'marek;lis\n', 'anna;kuna\n', …, 'lew;lew']
# 2. stosując metody klasy str utworzy na podstawie powyższej listy nową listę postaci:
# ['Jan Kot', 'Marek Lis', 'Anna Kuna', …, 'Lew Lew']
# 3. zapisze elementy listy z punktu drugiego w pliku 'osoby.txt' (każdy element powinien być
# zapisany w osobnym wierszu)
# 4. utworzy listę wszystkich osób posortowaną alfabetycznie według nazwiska



# Zadanie 2
# Plik 'opady.csv' przechowuje dane na temat miesięcznych sum opadów atmosferycznych w 2001 roku
# zanotowanych we wszystkich posterunkach IMGW. Dane zapisane są w formacie:
# 'NAZWA STACJI,rok,miesiąc,suma_opadu\n’
# Napisz progam, który wczyta dane z pliku, a następnie na ich podstawie obliczy roczną sumę opadu
# i zapisze wynik w postaci listy result: list[list[str,float]]:
# [['Warszowice', 991.8]
# ['Chałupki', 687.8]
# ['Wisła Wielka', 1140.7]
# ['Goczałkowice-Zdrój', 930.6]
# ['Sejny', 671.9]]
# Zwróć uwagę na formatowanie obiektów str i zaokrąglenie obiektów float w liście wynikowej.



# Zadanie 3
# Napisz funkcję srednia(data: list[float]), która jako argument przyjmie listę przechowującą zbiór
# wartości liczbowych, a następnie obliczy i zwróci wartość średniej arytmetycznej tego zbioru.



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



# Zadanie 5
# Przejdź do modułu zad_02.py, a następnie na podstawie listy result z zadania 2 utwórz słownik,
# którego kluczami będą nazwy stacji, a wartościami roczne sumy opadów w tych stacjach.



# Zadanie 6
# W module funkcje.py napisz funkcję station_dict(lista), która na podstawie listy 2D w formacie:
# [['WARSZOWICE', '2001', '01', '54.1']
# ['WARSZOWICE', '2001', '02', '31.0']
# ['WARSZOWICE', '2001', '03', '47.8']
# ['STARY FOLWARK', '2001', '12', '30.1']]
# utworzy słownik w formacie:
# {‘WARSZOWICE’:[54.1, 31.0, 47.8, 102.7, 51.9, 120.2, 238.0, 126.7, 109.2, 26.8, 55.1, 28.3],
# ‘CHAŁUPKI’:[46.3, 36.8, 42.7, 64.4, 39.7, 72.2, 175.9, 66.8, 111.2, 27.2, 22.7, 28.2],
# ‘WISŁA WIELKA’:[59.9, 40.1, 67.3, 110.9, 57.5, 155.0, 280.8, 165.5, 156.3, 23.6, 45.4, 38.3],
# ‘SEJNY’:[26.1, 27.5, 41.2, 22.2, 67.6, 49.1, 110.3, 118.3, 128.3, 38.2, 38.9, 30.3]}



# Zadanie 7
# Napisz funkcję show_rain(data: dict, station: str, month: int) -> float|str, która na podstawie nazwy
# stacji przekazanej w argumencie station, oraz numeru miesiąca (1 – 12) zwróci ze zbioru data
# (słownik w formacie identycznym jak w zadaniu 6) wartość miesięcznej sumy opadu w wybranym
# miesiącu na tej stacji, lub ‘brak danych’, jeżeli stacja o podanej nazwie nie występuje w słowniku
# data.



# Zadanie 8
# Napisz funkcję data_filter(data: dict) -> dict, która na podstawie zbioru data (słownik w formacie
# identycznym jak w zadaniu 6) utworzy i zwróci nowy słownik w formacie:
# {‘WARSZOWICE’:[54.1, 31.0, 47.8, 102.7, 51.9, 120.2, 238.0, 126.7, 109.2, 26.8, 55.1, 28.3],
# ‘CHAŁUPKI’:[46.3, 36.8, 42.7, 64.4, 39.7, 72.2, 175.9, 66.8, 111.2, 27.2, 22.7, 28.2],
# ‘WISŁA WIELKA’:[59.9, 40.1, 67.3, 110.9, 57.5, 155.0, 280.8, 165.5, 156.3, 23.6, 45.4, 38.3],
# ‘SEJNY’:[26.1, 27.5, 41.2, 22.2, 67.6, 49.1, 110.3, 118.3, 128.3, 38.2, 38.9, 30.3]},
# przy czym w słowniku tym znajdą się dane wyłącznie dla tych stacji, dla których zbiór wartości będzie
# kompletny (sumy opadów zmierzono we wszystkich miesiącach roku).



# Zadanie 9
# Wykorzystaj dane z pliku ‘opady.csv’ oraz funkcje:
# station_dict (patrz zad. 6.), data_filter (patrz zad. 8.) i srednia (patrz zad. 3.)
# do napisania funkcji mean_by_month(data: dict, month: int) -> float zwracającej średnią wartość
# opadu we wszystkich posterunkach opadowych w wybranym miesiącu 2001 roku (argument month).