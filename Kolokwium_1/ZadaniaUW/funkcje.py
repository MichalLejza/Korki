def srednia(data: list[float]) -> float:
    return sum(data) / len(data)


def file_to_list(plik: str, sep: str, enc: str) -> list[list]:
    lista = []
    with open(plik, 'r', encoding=enc) as file:
        for linia in file:
            lista.append(linia)
    file.close()

    result = []
    for element in lista:
        elementy = element.split(sep)
        miasto = elementy[0]
        rok = elementy[1]
        miesic = elementy[2]
        opady = elementy[3]
        opady = opady.replace('\n', '')
        result.append([miasto, rok, miesic, opady])
    return result


def station_dict(lista: list) -> dict:
    slownik: dict = {}

    for element in lista:
        miasto = element[0]
        opady = element[3]
        if miasto in slownik:
            slownik[miasto].append(opady)
        else:
            slownik[miasto] = []
            slownik[miasto].append(opady)

    return slownik

def data_filter(slownik: dict) -> dict:
    nowy_slownik: dict = {}
    for element in slownik:
        if len(slownik[element]) == 12:
            nowy_slownik[element] = slownik[element]
    return nowy_slownik