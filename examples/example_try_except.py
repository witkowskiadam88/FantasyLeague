
x =10
y = 0

try:
    print(x + "string")
    print(x/y)
    print("to sie wykonalo")
except ZeroDivisionError:
    print("nie dzielimy przez 0")
except TypeError:
    print("uwaga, blad typow danych")


#funkcja wyjatku try zawiera w swoim ciele funkcje liczaca wynik z dzielenia przez 0.
#gdybysmy uruchomili dzielenie przez 0 to otrzymalibysmy blad o nazwie ZerDivisionError. Dlatego w except
#ustawiamy go jako akceptowalny wyjatek.

#----------drugi sposob----------

try:
    list = []
    print(list[1])
    print(x + "string")
    print(x/y)
    print("to sie wykonalo")
except (ZeroDivisionError, TypeError):
    print("\nblad typu danych lub dizelenie przez 0")
except:  # except z ":" akceptuje kazdy inny error ktory sie pojawi. nie trzeba go konkretnie precyzowac
    print("oraz inny blad zostal zaakceptowany")

#---------blok finally---------
print("-----------------------------------")
try:
    print(x/y)
finally:
    print(" mimo tego, ze nie udalo sie wykonac poprzednich funkcji prawildowo, wykonuje kolejny krok")
    #blok finally wykona sie obojetnie czy wczesniej funkcja try wykonalo sie z powodzeniem lub nie.
    #mozna np wykorzystac d oteardownow, czyli sprzataniu po testach, nawet jesli sa failed.
