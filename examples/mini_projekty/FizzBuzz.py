print("FizzBuzz polega na tym, ze gdy liczba jest podzielna przez 3 to printujemy Fizz,"
      "gdy liczba jest podzielna przez 5 to Buzz, a gdy przez 3 i 5 to FizzBuzz")

for i in range (3,100):
    if i%3==0 and i%5==0:
        print(f"liczba {i} jest podzielna przez 3 i 5, wiec mowie: FizzBuzz")
    else:
        if i%3==0:
            print(f"liczba {i} jest podzielna przez 3, wiec mowie: Fizz")
        else:
            if i%5==0:
                print(f"liczba {i} jest podzielna przez 5, wiec mowie: Buzz")



