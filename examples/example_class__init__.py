class Czlowiek:

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie   #zmienna imie (bez self) odnosi sie do argumentu fukncji specjalnej, czyli do argumentow funckji __init__
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstawSie(self, powitanie = "Czesc"):
        return powitanie + " mam na imie " + self.imie + " a na nazwisko " + self.nazwisko + ". Mam " + str(self.wiek) + " lata."

osoba1 = Czlowiek("Adam", "Witkowski", 34)  # gdyby nie bylo konstruktora __init__, to nie moglibysmy odwolac sie do zmiennej imie, nazwisko
                                            #,wiek podczas towrzenia instacji/obiektu. Trzeba by bylo nadawac wartosc argumentu imie poprzez metoda klasy
osoba2 = Czlowiek("Monika", "Witkowska", 32)

print(osoba1.przedstawSie())
print(osoba2.przedstawSie("Witam"))