import math

class Figura:
    def __init__(self, nazwa, kolor):
        self.nazwa = nazwa
        self.kolor = kolor

    def napisz(self):
        return (f"Czesc, jestem  {self.nazwa} i mam kolor {self.kolor}")


class Kwadrat(Figura): # dziedziczymy z klasy Fugura wszsytko
    pass

    def pole_kwadrat(self, bok_a, bok_b): #dopiero w tej metodzie dodajemy nowe argumenty. Czyli sa definiowane dopiero tam gdzie je uzywamy.
        pole_kwadrat = bok_a * bok_b
        return (f"Jestem {self.nazwa} i mam pole o powierczhni równej {pole_kwadrat}")


kwadrat = Kwadrat("kwadrat", "czerwony") #uwaga, obiekt kadrat nie moze dostac argumentow klasy Kwadrat, bo nie zostaly zdefiniowane konstruktorem __init__
# w tej klasie. Mozemy je przypisac dopiero przez metode, ale sam obiekt ich nei posaida.
print(kwadrat.napisz())
print(kwadrat.pole_kwadrat(4, 5))
print(kwadrat.pole_kwadrat(6, 5))




