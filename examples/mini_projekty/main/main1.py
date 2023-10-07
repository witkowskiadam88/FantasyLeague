
#struktura funkcji:
def main():
# kod funkcji
    return "sasas"

if __name__=="__main__":
    main()


#Interpreter pythona podczas uruchamiania skryptu plików źródłowych tworzy kilka zmiennych, w tym zmienną
#o nazwie __name__. Czyli ta zmienna tworzy się zawsze.
#Jesli uruchamiany plik jest plikiem głównym, czyli nie jest imporotwany, przywolywany przez zaden inny plik,
#to zmienna __name__ przyjmuje wartosc __main__.

#plik glowny ----| [dla tego pliku __name__ = __main__]
#                |
#                plik 2(przywolywany, importowany etc)----|  [dla tego pliku __name__ != __main__]
#                                                         |
#                                                         |
#                                                  plik 3 (przywolywany, importowany etc) [dla tego pliku __name__ != __main__]
# a wiec warunek if __name__=="__main__" jest prawdziwy tylko, jesli uruchamiany plik jest plikiem głównym,
# czyli dy zmienna __name__ przyjmuje wartosć __main__.
#wtedy to wykona sie kod funkcji main