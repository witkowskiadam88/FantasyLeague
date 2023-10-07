
#funkcja main wykonuje sie dopiero jesli warunek if __name__ == "__main__".

print("pies")

def main():
    print("kot")

if __name__ == "__main__":
    main()

print("chomik")

#najpierw wykona sie pies, potem kot, bo if jest w drugiej kolejnosci a na koncu chomik

