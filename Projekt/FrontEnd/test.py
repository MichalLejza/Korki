import tkinter as tk
from Projekt.Obliczenia.obliczenia import zmien_napis_na_listy, policz_wynik


def on_button_click():
    button.config(bg="green")
    znaki, liczby = zmien_napis_na_listy(T.get("1.0", tk.END))
    dzialanie = T.get("1.0", tk.END)
    T.delete("1.0", tk.END)
    root.config(bg="red")
    T.insert(tk.END, dzialanie + ' = ' + str(policz_wynik(znaki, liczby)))

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Przycisk w Tkinter")
root.geometry('520x300')

T = tk.Text(root, height = 5, width = 52)
T.pack()

# Tworzenie przycisku
button = tk.Button(root, text="Kliknij mnie", command=on_button_click, bg="red", fg="white", padx=20, pady=10)
button.pack(pady=20)

# Uruchomienie pętli głównej
root.mainloop()
