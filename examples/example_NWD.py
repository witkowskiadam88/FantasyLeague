#funkcja zwraca najmnijeszy wspolny dzielnik dwoch liczb

def nwd(liczba_mniejsza, liczba_wieksza):
    i = 1
    while i <= liczba_mniejsza:
        i += 1
        if liczba_mniejsza%i == 0 and liczba_wieksza%i == 0:
            return i

print("nwd to", nwd(5,25))

