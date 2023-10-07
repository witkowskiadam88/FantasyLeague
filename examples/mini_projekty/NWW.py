print("Obliczanie Najmniejszej Wspolnej Wielokrotnej\n")
print("Podaj liczby A i B, dla których obliczę NWW")

print("A = ", end = "")
A = int(input())

print("B = ", end = "")
B = int(input())

i = 1
while i%A != 0 or i%B != 0:
    i = i + 1

print(f"NWW liczby A={A} i B={B} wynosi {i}")
