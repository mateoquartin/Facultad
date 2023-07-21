### Sets ###
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario 

my_other_set = {"mateo", "quartin", 20, 1.75}
print(type(my_other_set))


print(len(my_other_set))

my_other_set.add("Tinchito") # añadimos al set
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Tinchito")
print(my_other_set) # No admite elementos  repetidos

print("tinchito" in my_other_set)
print("Tinchito" in my_other_set)

my_other_set.remove("Tinchito")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

 
del my_other_set # Borramos entero al set

my_set = {"marina", "farfan", 56}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"matematica", "lenguaje", "quimica"}

my_new_set = my_set.union(my_other_set) #forma de unir sets
print(my_new_set)

print(my_set.difference(my_other_set))  



