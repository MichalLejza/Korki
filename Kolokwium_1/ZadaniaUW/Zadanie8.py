# Zadanie 8
# Napisz funkcję data_filter(data: dict) -> dict, która na podstawie zbioru data (słownik w formacie
# identycznym jak w zadaniu 6) utworzy i zwróci nowy słownik w formacie:
# {‘WARSZOWICE’:[54.1, 31.0, 47.8, 102.7, 51.9, 120.2, 238.0, 126.7, 109.2, 26.8, 55.1, 28.3],
# ‘CHAŁUPKI’:[46.3, 36.8, 42.7, 64.4, 39.7, 72.2, 175.9, 66.8, 111.2, 27.2, 22.7, 28.2],
# ‘WISŁA WIELKA’:[59.9, 40.1, 67.3, 110.9, 57.5, 155.0, 280.8, 165.5, 156.3, 23.6, 45.4, 38.3],
# ‘SEJNY’:[26.1, 27.5, 41.2, 22.2, 67.6, 49.1, 110.3, 118.3, 128.3, 38.2, 38.9, 30.3]},
# przy czym w słowniku tym znajdą się dane wyłącznie dla tych stacji, dla których zbiór wartości będzie
# kompletny (sumy opadów zmierzono we wszystkich miesiącach roku).


def data_filter(slownik: dict) -> dict:
    nowy_slownik: dict = {}
    for element in slownik:
        if len(slownik[element]) == 12:
            nowy_slownik[element] = slownik[element]
    return nowy_slownik

