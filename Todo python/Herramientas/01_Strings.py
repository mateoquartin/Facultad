

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


Hola = "Mateo"
print(len(Hola))

