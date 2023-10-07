import random

gracze_lista = ["Adam", "Monika", "Leon", "Pola"]
wygrane_lista = [1000, 10000, 100000, 1000000]
for gracz in gracze_lista:
    wygrana = random.choice(wygrane_lista)
    print(f"{gracz} wygral:", wygrana, "pln")