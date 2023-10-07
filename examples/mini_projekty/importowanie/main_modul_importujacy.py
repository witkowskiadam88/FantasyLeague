
from modul_importowany2 import odejmij  # importowanie z modulu modul_importowany2 tylko funkcji odejmij
from modul_importowany1 import liczba1 # importowanie zmiennej
import modul_importowany3  # w ten sposob importujemy caly modul, ale by wywolac funkcje lub zmienne, trzeba je przywolac
#przez podanie nazwy modulu i po kropce nazwe zmiennej lub funkcji: modul_importowany3.przywitaj_sie()

print(odejmij(4, 2))
print(liczba1)
modul_importowany3.przywitaj_sie()
print(modul_importowany3.liczba3)