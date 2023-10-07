import random

def dodawanie(liczba1,liczba2):
    suma = liczba1 + liczba2
    return(suma)
#
# print(dodawanie(5,10))
#
#
# for i in range (1,10):
#     if i % 2 == 0:
#         print(i,"parzysta")
#     else:
#         print(i,"nieparzysta")
#
# for i in range(0,10):
#     losowa=random.randint(0,100)
#     print(losowa)


def losowanie(ile_losowan_min, ile_losowan_max, dolna_granica, gorna_granica):
    for i in range(ile_losowan_min,ile_losowan_max):
        losowa=random.randint(dolna_granica,gorna_granica)
    return losowa


print(losowanie(0,5,1,100))


# def porownanie_losowanych_liczb(losowa):
#     if losowa % 2 == 0:
#         print(losowa,"parzysta")
#     else:
#         print(losowa,"nieparzysta")
#     return