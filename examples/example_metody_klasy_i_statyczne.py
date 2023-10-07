
class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("nazywam sie" + self.imie)

try:
    print(Czlowiek.przedstaw())  # metoda przedstaw nie nalezy do klasy czlowiek, nalezy do obiektu. wywola sie blednie
    print("nie wyprintuje sie, bo sie nie wykonalem") #metoda przedstaw wywola sie dopiero po wywolaniu obiektu do ktorego nalezy

except:
    print("asdsad")

print("---------------METODA KLASY------------------------")

class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("nazywam sie " + self.imie)

    @classmethod
    def nowyczlowiek(cls, imie):
        return cls(imie)

osoba1 = Czlowiek.nowyczlowiek("Adam")  # tworzymy obiekt inaczej, poprzez metode klasy.
osoba1.przedstaw()
osoba2 = osoba1.nowyczlowiek("Marek")   # mozna utworzyc nowy obiekt na bazie juz istniejacego obiektu
osoba2.przedstaw()

print("\n---------------METODA STATYCZNA------------------------")

class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    @staticmethod
    def przywitaj(arg):
        print("czesc " + arg)

Czlowiek.przywitaj("kolego")  # metoda statyczna zadziala nawet bez utworzenia obiektu
