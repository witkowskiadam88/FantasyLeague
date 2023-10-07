class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("nazywam sie " + self.imie)

    @classmethod
    def nowyczlowiek(cls, imie):
        return cls(imie)

czlowiek1 = Czlowiek("Adam")
czlowiek1.przedstaw()   # w metodzie obiektowej tworzymy obiekt przez klase, nie przez metode

czlowiek2 = Czlowiek.nowyczlowiek("Monika")  # w metodzie klasowej tworzymy obiekt przez metode klasowa nowyczlowiek
czlowiek2.przedstaw() # uwaga, wywolujemy metode przedstaw sie, nie nowyczlowiek.
#metoda klasowa to metoda na klasie Czlowiek. parametr cls pozwala odwolac sie do argumentu imie nalezacy do klasy Czlowiek
#metoda klasowa pozwala nam na wykonywaniu operacji na metodach danje klasy. Tworzymy obiekt przez metode klasowa nowyczlowiek.
