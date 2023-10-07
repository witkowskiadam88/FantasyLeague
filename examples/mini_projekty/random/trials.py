tab=[30, 37, 34, 12, 4]


krok = 0
krok2 = 0
for krok2 in range(0,len(tab)-1):
    for krok in range(0,len(tab)-1):
        if tab[krok] > tab[krok+1]:
            tab[krok+1], tab[krok] = tab[krok], tab[krok+1]
            print(tab)