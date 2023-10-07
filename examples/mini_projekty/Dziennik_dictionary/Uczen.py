
class Uczen:
    def __init__(self, imie, nazwisko, wiek, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.klasa = klasa

    def przedstaw_sie(self):
        return (f"jestem {self.imie} {self.nazwisko}, mam {self.wiek} lat i chodze do klasy {self.klasa}")



