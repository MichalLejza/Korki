def join_data(input_file1: str, input_file2: str, output_file: str):
    zawartosc_stratigrapthy: list = []

    with open(input_file1, 'r', encoding='UTF-8') as plik:
        for linia in plik:
            linia_clear = linia.replace('\n', '')
            zawartosc_stratigrapthy.append(linia_clear)
    plik.close()

    print(zawartosc_stratigrapthy)

    zawartosc_depth: dict = {}

    with open(input_file2, 'r', encoding='UTF-8') as plik:
        for linia in plik:
            elementy: list = linia.split(',')
            elementy[1] = elementy[1].replace('\n', '')
            zawartosc_depth[elementy[0]] = elementy[1]
    plik.close()

    print(zawartosc_depth)

    zawartosc_do_output: list = []

    for linia in zawartosc_stratigrapthy:
        elementy: list = linia.split(',')
        print(elementy)
        nazwa_odwiertu = elementy[0] #
        print(nazwa_odwiertu)
        glebokosc_odwiertu = zawartosc_depth[nazwa_odwiertu] if nazwa_odwiertu in zawartosc_depth else '-'
        print(glebokosc_odwiertu)
        linia.replace('\n', '')
        zawartosc_do_output.append(linia + ',' + glebokosc_odwiertu + '\n')

    with open(output_file, 'w', encoding='UTF-8') as plik:
        for linia in zawartosc_do_output:
            plik.write(linia)
    plik.close()


join_data('stratigraphy.txt', 'depth.txt', 'output.txt')