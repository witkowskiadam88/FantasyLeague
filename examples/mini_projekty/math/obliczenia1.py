import math

print("===========potega==============")
def potega(podstawa, wykladnik):
    print(f"{podstawa}^{wykladnik}=", math.pow(podstawa, wykladnik))

potega(2,3)
potega(2,1.3)
potega(8,1/2)  # potega 8 ^1/2 to 2 to pierwiastek

print("\n========pierwiastek===========")

def pierwiastek(liczba):
    print(f"pierwiastek kwadratowy z {liczba}=", math.sqrt(liczba))

pierwiastek(25)
pierwiastek(24)

