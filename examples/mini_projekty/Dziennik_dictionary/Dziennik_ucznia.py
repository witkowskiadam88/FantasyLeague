from Obiekty import *

numer_ucznia = 0
Dziennik_klasa_Ia = {}

for uczen in tab_uczniowie:
    print(uczen.imie)
    numer_ucznia = numer_ucznia + 1
    Dziennik_klasa_Ia["imie"] = uczen.imie
    print(Dziennik_klasa_Ia)

matematyka_uczen1=[3,4,5]
polski_uczen1=[3,3]

matematyka_uczen2=[3,5,5]
polski_uczen2=[4,3]

# Dziennik_klasa_Ia = {"uczen_nr_1":
#                          {"imie": uczen1.imie, "nazwisko": uczen1.nazwisko, "wiek": uczen1.wiek,
#                           f"{matematyka.przedmiot}": matematyka_uczen1, f"{polski.przedmiot}": polski_uczen1},
#                      "uczen_nr_2":
#                          {"imie": uczen1.imie, "nazwisko": uczen1.nazwisko, "wiek": uczen1.wiek,
#                           f"{matematyka.przedmiot}": matematyka_uczen1, f"{polski.przedmiot}": polski_uczen1}}




