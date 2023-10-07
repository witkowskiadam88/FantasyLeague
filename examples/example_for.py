
print("funkcja zwroci tylko liczby parzyste oraz ich sume")

def parzyste(range_min, range_max):
    suma = 0
    tab = []
    for i in range(range_min,range_max):
        if i%2 == 0:
            suma += i
            tab.append(i)
        else:
            continue
    return tab, suma

print(parzyste(1,100))
