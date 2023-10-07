from Dziennik_ucznia import *

#jest to tzw nested dictionary, czyli slownik ktory sklada sie z innych slownikow. Slownik "uczen nr 1" + slownik "uzen nr 2"


Dziennik_klasa_Ia = {"uczen_nr_1":
                         {"imie": uczen1.imie, "nazwisko": uczen1.nazwisko, "wiek": uczen1.wiek,
                          f"{matematyka.przedmiot}": matematyka_uczen1, f"{polski.przedmiot}": polski_uczen1},
                     "uczen_nr_2":
                         {"imie": uczen2.imie, "nazwisko": uczen2.nazwisko, "wiek": uczen2.wiek,
                          f"{matematyka.przedmiot}": matematyka_uczen2, f"{polski.przedmiot}": polski_uczen2}}


print("ssss", Dziennik_klasa_Ia["uczen_nr_2"]['imie'],Dziennik_klasa_Ia["uczen_nr_2"]['wiek'])



Dziennik_klasa_IIa = {}

