def decorator(function):   # decorator(function) - w tym miejscu argumentem funkcji decorator jest function
    def wrapper():
        print("---------")
        function()
        print("---------")
    return wrapper          #funkcja dekorator ma zwrocic wartosc funkcji wrapper

def przywitajSie():
    print("Hi gosciu ")

przywitajSie = decorator(przywitajSie)  # dekorujemy funkcje przywitaj sie funkcja wrapper, a wrapper to inaczej opakowanie, taki nalesnik,wrap
               # decorator(przywitajSie) - funkcja przywitajSie przyjmuje jako swoja wartosc funkcje decorator, a w funkcji decorator function staje sie funkcja przywitajSie
przywitajSie()

######################33
#drugi sposob dekorowania

@decorator   # odwolanie do funkcji decorator w postaci @decorator powoduje, ze funkcja ponizej zostanie nia od razu udekorowana
# i jest tym samym co : przywitajSie = decorator(przywitajSie)
def przywitajSie2():
    print("siemka")

przywitajSie2()
