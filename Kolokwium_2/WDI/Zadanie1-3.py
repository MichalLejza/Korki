# W programie PyCharm utwórz nowy projekt w lokalizacji C:\wdi\kol_pn. W projekcie tym
# utwórz moduł zadania_nazwisko.py. W module utwórz zmienną user_dict, która będzie
# przechowywać słownik w postaci:
# {'cluster': 'blizzard', 'storm': 'rainfall'}
# Zadanie 1 (5 punktów).
# W słowniku user_dict pary klucz – wartość przechowują loginy i hasła użytkowników
# pewnego serwisu. Napisz program który:
# 1. Zapyta użytkownika o login.
# 2. Sprawdzi czy login występuje w słowniku.
# 3. Jeżeli login występuje w słowniku, program zapyta o hasło, przy czym użytkownik
# będzie miał tylko trzy próby na wpisanie prawidłowego hasła. Jeżeli użytkownik
# wpisze poprawne hasło w jednej z trzech dostępnych prób, program wyświetli
# spersonalizowane powitanie w serwisie (w treści powitania pojawi się odpowiedni
# login). W przeciwnym wypadku wyświetlony zostanie komunikat o przekroczeniu
# maksymalnej liczby prób i program zakończy działanie.
# 4. Jeżeli login nie występuje w słowniku, program wyświetli informację, że takie konto
# nie istnieje

# kluch = login, wartosc = haslo
user_dict: dict = {'Michal': '123', 'Krzysztof': '456', 'Jan': '789', 'Piotr': '111'}

login = input("Podaj login: ")

if login not in user_dict:
    print('Podane konto nie istnieje')
else:
    OG_haslo = user_dict[login] # faktyczne hasło do konta użytkownika
    max_ilosc_prob = 3
    licznik_do_liczenia_podejsc = 0

    for i in range(max_ilosc_prob):
        licznik_do_liczenia_podejsc += 1
        potencjalne_haslo = input("Podaj hasło: ")
        if potencjalne_haslo == OG_haslo:
            print(f'Witamy {login} w serwisie!')
            break

    if licznik_do_liczenia_podejsc == max_ilosc_prob:
        print('Przekroczono maksymalną liczbę prób')



# Zadanie 2

def add_user():
    podaj_znowu_login = True # wartosc do petli

    Login: str = '' # 'Piotr
    Password: str = '' # 'fgjiroehjviowe

    while podaj_znowu_login is True:
        nowy_login = input("Podaj login: ")
        if nowy_login not in user_dict:
            podaj_znowu_login = False
            Login = nowy_login

    podaj_znowu_haslo = True

    while podaj_znowu_haslo is True:
        nowe_haslo = input("Podaj hasło: ")
        if len(nowe_haslo) >= 8 and nowe_haslo.isalpha():
            podaj_znowu_haslo = False
            Password = nowe_haslo

    user_dict[Login] = Password


# Zadanie 3


def save_users(data: dict, file: str, enc: str='UTF-8'):
    with open(file, 'w', encoding=enc) as plik:
        for login, haslo in data.items():
            plik.write(login + ';' + haslo + '\n')
    plik.close()


def read_users(file: str, enc: str='UTF-8') -> dict:
    slownik: dict = {}

    with open(file, 'r', encoding=enc) as plik:
        for linia in plik:
            elementy: list = linia.split(';')
            elementy[1] = elementy[1].replace('\n', '')
            slownik[elementy[0]] = elementy[1]
    plik.close()

    return slownik

# save_users(user_dict, 'users.txt')

odczytany_slownik = read_users('users.txt')
print(odczytany_slownik)


