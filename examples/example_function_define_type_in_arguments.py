#            okreslamy, ze files musza byc lista integerow, a funckja zwroci liste skladajaca sie z samych integerow
#wywolanie funkcji bedzie bledne, jesli wprowadzona wartosc zmiennej "name" bedzie inna niz string
def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting("Adam"))