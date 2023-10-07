x =40   #global variable

def f():
    x=20  #enclosing variable

    def g():
        x=10   #local variable
        print(x)