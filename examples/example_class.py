class Obywatel():
    def imie(self, imie_obywatela):
        print(f"Mam na imie {imie_obywatela}")

    def nazwisko(self, nazwisko_obywatela):
        print(f"Mam na nazwisko {nazwisko_obywatela}")

    def wiek(self):
        print(f"Mam {self.wiek_obywatela} lata")

    def zawod(self):
        print("Tester")

obywatel1 = Obywatel()
obywatel1.imie("Adam")
obywatel1.nazwisko("Witkowski")
obywatel1.wiek_obywatela = "34"
obywatel1.wiek()
obywatel1.zawod()
print(obywatel1.imie)

