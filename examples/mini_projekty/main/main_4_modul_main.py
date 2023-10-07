
from main_4_modul_import import aaa


aaa()  # ta funkcja sie printuje, bo ja zaimportowalismy i ma funkcje wykonujaca "print"
#wiec nie czeka na warunek if __name__ by sie wykonac, wystarczy ze ja przywolamy
# to co jest w main_4_modul_import pod warunkiem if __name__ nie wykonuje sie tutaj,
# bo nie spelnia tego warunku. main_4_modul_import jest modulem importowanym, czyli nie jest main.



def main(a,b):
    oblicz = a + b

    return oblicz

if __name__ == "__main":
    main()

print("oblicz wynosi", main(4,6))
