
def while_function(a,b):
    while a<b:
        print(f"{a} jest mniejsze od {b}")
        b -= 1
    else:
        print(f"{a} nie jest wieksze od {b}, koniec petli while")

while_function(1,10)

