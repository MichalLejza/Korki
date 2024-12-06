
# Zadanie 6
# W module funkcje.py napisz funkcję station_dict(lista), która na podstawie listy 2D w formacie:
# [['WARSZOWICE', '2001', '01', '54.1']
# ['WARSZOWICE', '2001', '02', '31.0']
# ['WARSZOWICE', '2001', '03', '47.8']
# ['STARY FOLWARK', '2001', '12', '30.1']]
# utworzy słownik w formacie:
# {‘WARSZOWICE’:[54.1, 31.0, 47.8, 51.9, 102.7, 120.2, 238.0, 126.7, 109.2, 26.8, 55.1, 28.3],
# ‘CHAŁUPKI’:[46.3, 36.8, 42.7, 64.4, 39.7, 72.2, 175.9, 66.8, 111.2, 27.2, 22.7, 28.2],
# ‘WISŁA WIELKA’:[59.9, 40.1, 67.3, 110.9, 57.5, 155.0, 280.8, 165.5, 156.3, 23.6, 45.4, 38.3],
# ‘SEJNY’:[26.1, 27.5, 41.2, 22.2, 67.6, 49.1, 110.3, 118.3, 128.3, 38.2, 38.9, 30.3]}
from funkcje import *


lista: list = file_to_list('opady.csv', ';', 'utf-8')
slownik: dict = station_dict(lista)
print(slownik)
