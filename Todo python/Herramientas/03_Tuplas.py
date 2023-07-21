### tuplas ###

my_tuple = tuple()
my_other_tuple = () # La tupla se crea con el parentesis 


my_tuple = (20, 1.74, "Mateo", "Quartin", "Quartin")
my_other_tuple = (30, 60, 19, 23)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[3])
print(my_tuple[-2]) # tiene la misma forma que las listas para ubicarse por dentro

print(my_tuple.count("Mateo")) # sirve para contar la cantidad de elementos dentro de la tupla

print(my_tuple.index("Quartin")) # nos dice en que indice esta el elemento 

# En las tuplas una ves definidas no se pueden modificar! 

my_suma_tupla = (my_tuple + my_other_tuple) # si se puede sumar las tuplas
print( my_suma_tupla)

print(my_tuple[1:3])

my_tuple = list(my_tuple)
print(my_tuple)

my_tuple[4] = "QuarProg"
my_tuple.insert(0, "Cars")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(my_tuple)

del my_tuple # Borramos toda la tupla

