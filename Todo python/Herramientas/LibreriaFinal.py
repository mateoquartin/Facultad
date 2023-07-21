### STRINGS ###

my_string = "Mi estrings"

my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Sumamos string

miString = "hola este es un string \nCon salto de lindea" # El \n es para saltar una linea en el texto mostrado
print(miString)

mi_string_tabulacion = "\tEsto es un string con tabulacion" # Con el \t hacemos una tabulacion en el texto mostrado
print(mi_string_tabulacion)

# Formateo

nombre, apellido, edad = "Mateo", "Quartin", 19

print("mi nombre es {} y mi apellido es {} y tengo {} años".format(nombre, apellido, edad))
print("mi nombre es %s y mi apellido es %s teniendo una edad %d" %(nombre, apellido, edad))
print(f"mi nombre es {nombre} y mi apellido es {apellido} y tengo {edad}")

# Desempaquetado de caracteres

lenguaje = "python"
a, b, c, d, e, f = "python"

print(a)
print(f)

# Division

lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] # Si le quitamos la segunda va desde el numero que ponemos hasta el ultimo (el final empieza desde menos uno)
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # Va desde el ultimo hasta el principio
print(lenguaje_slice)   

# Reverse

lenguaje_slice = lenguaje[::-1] # Poniendo dos puntos y un -1 damos vuelta el string
print(lenguaje_slice)

# Funciones

print(lenguaje.capitalize()) #Pone la primera letra en mayuscula

print(lenguaje.upper()) # Pone todo el string en mayuscula

print(lenguaje.count("h")) # Cuentas cuantas letras tiene el string

print(lenguaje.isnumeric()) #comprueba si es un numero (en este caso no lo es)

print("5010".isnumeric()) #comprueba si es un numero (en este caso si )

print(lenguaje.lower()) #pasa a minuscula el string

print(lenguaje.upper().isupper()) #isupper es para comprobar si esta en mayuscula

print(lenguaje.startswith("py")) # indica si empieza o no asi el string

#######################################################################################################################

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

#########################################################################################################################################################

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



