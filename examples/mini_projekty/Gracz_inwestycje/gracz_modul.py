
import random
from gracz_listy import *

class Gracz:
    def __init__(self, imie, nazwisko, budzet, wygrana, inwentarz):
        self.imie = imie
        self.nazwisko = nazwisko
        self.budzet = budzet
        self.wygrana = wygrana
        self.inwentarz = inwentarz

    def opis(self):
        return (f"{self.imie},{self.nazwisko},wygrana to:{self.wygrana}. Kupilem/ Kupilam za wygrana: {self.inwentarz}. Moj budzet wynosi teraz {self.budzet}")

    def wygraj(self):
        self.wygrana = random.choice(lista_wygrane)   # losuje wygrana
        self.budzet = self.wygrana + self.budzet    #wygrana dodaje sie do budzetu. Od tad kazdy obiekt na ktorym zostanie
        #uruchomiona ta metoda, bedzie mial zmieniona wartosc parametru budzet (powiekszona o wygrana)

    def kup_za_wygrana(self):
        for key, value in lista_inwentarz.items():
            if value < self.budzet:
                self.inwentarz = key
                self.budzet = self.budzet - value
            else:
                break

wygraj()