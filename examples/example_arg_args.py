

def function(*args):
    for i in args:
        print(f"kolejny argument z {args} to {i}")

function(1,2,3,4)

#*args - name args is just a random name, "*" is the thing.
#**kwargs - "**" znaczy, ze mozemy wprawdzic dowolna ilosc KeyWordow jako argumenty funkcji, np:

def function_kwargs(**kwargs):
    for i in kwargs:
        print(kwargs.items())

function_kwargs(Imie = "Adam",Nazwisko = "Witkowski")