### Listas ###

my_list = []

my_other_list = []
    
print(len(my_list))

my_list = [35, 50, 10, 63, 15, 74]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.74, "mateo", "quartin"]
print(my_other_list)

print(my_other_list[0])

print(my_other_list.count(35)) # Sirve para ver cuantas veces se repite en la lista4

edad, altura, nombre, apellido = my_other_list
print (altura)


print(my_other_list + my_list)

my_other_list.append("marina")
print(my_other_list)

my_other_list.insert(1, "azul") # Insertamos en la posicion que queremos y desplazamos todo
print(my_other_list)  

my_other_list.remove("azul") # Eliminamos de la lista al elemento
print(my_other_list)

print(my_other_list.pop()) # Por defecto va eliminar al ultimo elemento de la lista 
print(my_other_list)


popito = my_other_list.pop(2) # Es para eliminarlo 
print(popito)
print(my_other_list)

del my_other_list [2] # Usamos del para eliminar el elemento dentro de la posicion a diferencia del remove que elimina sabiendo el elemento dentro
print (my_other_list)

my_new_list = my_list.copy()

my_list.clear() # Con clear limpiamos toda la lista
print(my_list)

my_new_list.reverse()

print(my_new_list) # Con reverse damos vuelta la lista 

my_new_list.sort() # Con sort ordenamos la lista en este caso por orden numerico
print(my_new_list)



