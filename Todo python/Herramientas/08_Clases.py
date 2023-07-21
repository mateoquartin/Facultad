### Clases ###

class MyEmpyPerson:
    pass 

print(MyEmpyPerson)
print(MyEmpyPerson())

class Person:
    def __init__(self,name, surname, alias = "sin alias"): #constructor de clase (siempre tiene que ir el self)
        self.full_name = f"{name} {surname} ({alias})"
    
    def caminar (self):
        print( f"{self.full_name}persona esta camiando")

    def saltar (self):
        print(f"{self.full_name} esta saltando")

my_person = Person("mateo","quartin")
my_other_person = Person ("martin", "quartin", "tincho")

print(my_person.full_name)
my_person.caminar()
my_person.saltar()

print(my_other_person.full_name)
my_other_person.saltar()
my_other_person.full_name = "Mateo esta idiota"
print(my_other_person.full_name)