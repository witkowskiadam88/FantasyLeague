
class Animal:
    def __init__(self,name, age):
        self.name = name   # przypisujemy zmiennej self.imie imie z argumentu metody init(konstruktora)
        self.age = age

class Dog(Animal):   #klasa Dog bedzie dzieciczyc z klasy Animal wszystkie wlasciwosci, wszystko co ta klasa posiada
    def voice(self):
        print("szczekam")

class Wolf(Dog):  # Wolf dzieciczy wszsyto to co ma Dog oraz to co ma funkcja bazowa Animal
    def getVoice(self):
        super().voice()  #funkcja super szuka w klasach bazowych meotd ktore podamy po kropce. Klasy bazowe to wszystkie te po ktorych dziedziczymy

dog = Dog("Burek", 5)
print(dog.name)
print(dog.age)
dog.voice()
print("------wilk----------")
wilk = Wolf("wilczek", 6)
print("wilk o imieniu " + wilk.name + " ma " + str(wilk.age) + "lat oraz wydaje dzwiek: ")
wilk.getVoice()
