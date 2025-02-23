import tkinter as tk
from Projekt.Obliczenia.obliczenia import zmien_napis_na_listy, policz_wynik


def klik_rowna_sie():
    znaki, liczby = zmien_napis_na_listy(pole_tekstowe_z_dzialaniem.get("1.0", tk.END))
    pole_tekstowe_z_dzialaniem.delete("1.0", tk.END)
    pole_tekstowe_z_dzialaniem.insert(tk.END, str(policz_wynik(znaki, liczby)))

def klik_jeden():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '1')

def klik_dwa():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '2')

def klik_trzy():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '3')

def klik_cztery():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '4')

def klik_piec():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '5')

def klik_szesc():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '6')

def klik_dodaj():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '+')

def klik_odejmij():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '-')

def klik_mnoz():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '*')

def klik_dziel():
    pole_tekstowe_z_dzialaniem.insert(tk.END, '/')

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Kalkulator naukowy")
root.geometry('520x300')

pole_tekstowe_z_dzialaniem = tk.Text(root, height = 1, width = 52)
pole_tekstowe_z_dzialaniem.pack()

button_jeden = tk.Button(root, text='1', command=klik_jeden ,bg="green", fg="black", padx=20, pady=10)
button_jeden.place(x=10, y=100)

button_dwa = tk.Button(root, text='2', command=klik_dwa ,bg="red", fg="white", padx=20, pady=10)
button_dwa.place(x=100, y=100)

button_trzy = tk.Button(root, text='3', command=klik_trzy ,bg="red", fg="white", padx=20, pady=10)
button_trzy.place(x=190, y=100)

button_cztery = tk.Button(root, text='4', command=klik_cztery ,bg="red", fg="white", padx=20, pady=10)
button_cztery.place(x=10, y=160)

button_piec = tk.Button(root, text='5', command=klik_piec ,bg="red", fg="white", padx=20, pady=10)
button_piec.place(x=100, y=160)

button_szesc = tk.Button(root, text='6', command=klik_szesc ,bg="red", fg="white", padx=20, pady=10)
button_szesc.place(x=190, y=160)

button_dodaj = tk.Button(root, text='+', command=klik_dodaj ,bg="red", fg="white", padx=20, pady=10)
button_dodaj.place(x=10, y=220)

button_odejmij = tk.Button(root, text='-', command=klik_odejmij ,bg="red", fg="white", padx=20, pady=10)
button_odejmij.place(x=60, y=220)

button_mnoz = tk.Button(root, text='*', command=klik_mnoz ,bg="red", fg="white", padx=20, pady=10)
button_mnoz.place(x=110, y=220)

button_dziel = tk.Button(root, text='/', command=klik_dziel ,bg="red", fg="white", padx=20, pady=10)
button_dziel.place(x=160, y=220)

button_wynik = tk.Button(root, text='=', command=klik_rowna_sie, bg="red", fg="white", padx=20, pady=10)
button_wynik.place(x=210, y=220)

# Uruchomienie pętli głównej
root.mainloop()
