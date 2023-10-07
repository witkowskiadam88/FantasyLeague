
import random

tab=[]

def losowanie(ile_liczb, zakres_dol, zakres_gora):

    for liczba in range(ile_liczb):
        wylosowana_liczba = random.randint(zakres_dol, zakres_gora)
        tab.append(wylosowana_liczba)
    return tab


def sortowanie_babelkowe():
    krok2 = 0
    krok = 0
    for krok2 in range(0, len(tab) - 1):
        for krok in range(0, len(tab) - 1):
            if tab[krok] > tab[krok + 1]:
                tab[krok + 1], tab[krok] = tab[krok], tab[krok + 1]
    return tab

print("liczby nieposortowane",losowanie(5, 0, 100))

sortowanie_babelkowe()
print("liczby posortowane",sortowanie_babelkowe())