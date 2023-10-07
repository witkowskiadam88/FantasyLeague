
from gracz_modul import Gracz

gracz1 = Gracz("Adam", "Witkowski", 0, None, None)
gracz1.wygraj()
gracz2 = Gracz("Monika", "Witkowska", 0, None, None)
gracz2.wygraj()

gracz1.kup_za_wygrana()
gracz2.kup_za_wygrana()

print(gracz1.opis())
print(gracz2.opis())

