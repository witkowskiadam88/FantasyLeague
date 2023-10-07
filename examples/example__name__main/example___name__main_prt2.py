import example__name__main_imported_module_prt1

example__name__main_imported_module_prt1.main()

#jesli importujemy caly modul " example__name__main_imported_module_prt1" to sie wykonuje, ale ze jest w tym importowanym
#module warunek: if __name__ == "__main__":
#                      main()
#to po zaimportowaniu go nie jest on spelniony, wiec wywolanie funkcji main() odbedzie sie dopiero jesli
#wywolamy ta fukcje.