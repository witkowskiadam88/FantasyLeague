
print("========zaokraglanie int==========")

def zaokraglij_int(liczba1):
    print(f"zaokraglona {liczba1} uzywajac funckji 'int' wynosi =", int(liczba1))

zaokraglij_int(6.1)
zaokraglij_int(6.5)
zaokraglij_int(6.9)
zaokraglij_int(7.0)
print("czyli int zaokragla w dol")


print("\n========zaokraglanie round==========")

def zaokraglij_round(liczba2):
    print(f"zaokraglona {liczba2} uzywajac funckji 'round' wynosi =", round(liczba2))

zaokraglij_round(6.1)
zaokraglij_round(6.5)
zaokraglij_round(6.6)
zaokraglij_round(6.9)
zaokraglij_round(6.9)
print("czyli int zaokragla w klasycznie/ matematycznie")

print("\n========zaokraglanie round do x miejsc po przecinku==========")

def zaokraglij_round_2(liczba3, ile_miejsc_po_przecinku):
    print(f"zaokraglona {liczba3} do {ile_miejsc_po_przecinku} miejsc po przecinku, uzywajac funckji 'round' wynosi =", round(liczba3, ile_miejsc_po_przecinku))

zaokraglij_round_2(6.12, 1)
zaokraglij_round_2(6.49, 1)
zaokraglij_round_2(6.643, 2)
zaokraglij_round_2(6.986, 2)
zaokraglij_round_2(7.00157, 4)
print("czyli int zaokragla w klasycznie/ matematycznie")