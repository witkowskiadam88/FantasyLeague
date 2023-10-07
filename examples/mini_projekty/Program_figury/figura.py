import math

class Figura:
    def __init__(self, nazwa, kolor):
        self.nazwa = nazwa
        self.kolor = kolor

    def napisz(self):
        return (f"Czesc, jestem  {self.nazwa} i mam kolor {self.kolor}")


class Kwadrat(Figura): # dziedziczymy z klasy Fugura wszsytko, chyba ze dodajemy do klasy Kwadrat nowe arumenty, wtedy musimy podac
    #w init co dziedziczymy + nowe argumenty
    def __init__(self, nazwa, kolor, bok_a, bok_b): # argumenty nowej klasy Kwadrat
        super().__init__(nazwa, kolor)   # metoda super() wskazujemy co importujemy z klasy bazowej Figura i sa to argumenty konstruktora __init__ z klasy bazowej
        self.bok_a = bok_a
        self.bok_b = bok_b


    def pole_kwadrat(self, bok_a, bok_b):
        pole_kwadrat = bok_a * bok_b
        return (f"Jestem {self.nazwa} i mam pole o powierczhni równej {pole_kwadrat}")


kwadrat = Kwadrat("kwadrat", "czerwony", 4, 5)
print(kwadrat.napisz())
print(kwadrat.pole_kwadrat(4, 5))



# print(kwadrat.pole_kwadrat(4, 5))

    # def obwod_kwadrat(self, bok_a, bok_b):
    #     obwod_kwadrat = 2 * bok_a + 2 * bok_b
    #     return obwod_kwadrat

# class Kolo(Figura):
#     def __init__(self, nazwa, kolor, promien):
#         super().__init__(nazwa, kolor, promien)
#         self.promien = promien
#
#     def pole_kolo(self, promien):
#         pole_kolo = (math.pi * math.sqrt(promien))/2
#         return pole_kolo
#
#     def obwod_kolo(self, promien):
#         obwod_kolo = 2 * math.pi * promien
#         return obwod_kolo





