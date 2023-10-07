
# ===========metoda statyczna============

class Czlowiek:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def opowiedz_o_sobie(self):
        return (f"Czesc, jestem czlowiekiem numer 1, nazywam sie {self.imie} {self.nazwisko} i mam {self.wiek} lat")

    @staticmethod   # nie ma parametru self ani konstruktora __init__
    def powiedz_co_lubisz(lubie):
        return (f"lubie {lubie}")


print(Czlowiek.powiedz_co_lubisz("jeść")) #to metoda statyczna, wiec nie musimy tworzyc obektu
#print(Czlowiek.opowiedz_o_sobie("Adam", "Witkowski", 34)) #to metoda obiektowa, wiec musimy tworzyc obiekt, wiec w tej postaci sie nie wykona
czlowiek1 = Czlowiek("Adam", "Witkowski", 34) #tworzymy obiekt, by skoryzstac z metody opowiedz_o_sobie, ktora jest metoda obiektowa
print(czlowiek1.opowiedz_o_sobie())  # wykonujemy operacje print na metodzie klasowej

####=====WNIOSEK!!!!!!============#####
#metoda statyczna jest to po prostu metoda w obrebie klasy, ktora chcemy wykonywac bez tworzenia wczesniej obiektu.
#Mozemy wykonac ta metode poza klasa bez tworzenia obiektu.
#metoda statyczna zawsze wymaga najpierw utworzenia obiektu