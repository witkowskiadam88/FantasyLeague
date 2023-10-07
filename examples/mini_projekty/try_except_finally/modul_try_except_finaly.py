
class Dzielenie:

    @staticmethod
    def podziel(liczba_a, liczba_zero):
        return liczba_a/liczba_zero


# dzielenie1 = Dzielenie(5, 0)
# dzielenie2 = Dzielenie(6, 2)

try:
    print(Dzielenie.podziel(5,0))
except ZeroDivisionError:
    print("nie mozna dzielic przez 0. wykonaj ponowne obliczenie dla innej wartosci")
    print(Dzielenie.podziel(6,2))

#========inna metoda ===========

#zastosowanie except z ":" oznacza, ze przyjmie kazdy blad, bez jego definiowania

class Dodawanie:
    def __init__(self, liczba_jakas, nieliczba):
        self.liczba_jakas = liczba_jakas
        self.nieliczba = nieliczba

    def dodaj(self):
        return self.liczba_jakas + self.nieliczba

wynik1 = Dodawanie(5, "sasa")
wynik2 = Dodawanie(5, 6)


try:
    print(wynik1.dodaj())
except:
    print("jesli sie wydrukowalem, to znaczy ze jest jakis blad",   wynik2.dodaj())

try:
    print(wynik1.dodaj())
finally:
    print("lecimy dalej")   # po finally wszystko sie wykona, blad z try nie zatrzymuje skryptu