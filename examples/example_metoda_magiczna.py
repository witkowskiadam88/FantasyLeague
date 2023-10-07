print("definicja metody magicznej __add__: Python’s object.__add__(self, other) method returns a new object that represents the sum of two objects.")

import math

class Punkt2D:
    def __init__(self, x, y):   #metoda __init__ jest metoda magiczna, jak kazda zaczynajaca i konczaca sie na "__"
        self.x = x
        self.y = y
        self.c = math.sqrt(x**2 + y**2)

    def __add__(self, drugi):
        return Punkt2D(self.x + drugi.x, self.y + drugi.y)  # self w tym miejscu odwoluje sie do calej klasy.
                                       #__add__ do pierwszego obiektu doda drugi obiekt, oraz d

p1 = Punkt2D(2, 5)
p2 = Punkt2D(5, 6)
p3 = Punkt2D(1,1)

p3 = p1 + p2 + p3  # obiekt classy p1 i p2 nie ma zdefiniowanego typu zmiennej, dlatego python nie bedzie potrafil
               # wykonac rownania p3. Potrzebna jest definicja typu zmiennej, np poprzez metoda magiczna __add__
print(float(p3.x))  # tutaj wykonuje sie tylko dodawanie punktow (2,5) + (5,6) = (7,11)
print(p3.y)

#-------------------------------
print("\n prostszy przyklad metody magicznej __add__\n")


class Data:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Data(self.value + other.value)


a = Data(40)
b = Data(2)
c = a + b
print(c.value)