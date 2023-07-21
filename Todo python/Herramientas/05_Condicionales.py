### Condicionales ###
 
my_condicion = False

if my_condicion: # Es lo mismo que if my_condicion == True
    print ("Se ejecuta la condicion del if")

my_condicion = 5 * 5

if my_condicion == 11:
    print ("Se ejecuta la segunda condicion del if")

if my_condicion <= 10:
    print("es menor o igual que diez")
else:
    print("es mayor que diez ")

if my_condicion > 10 and my_condicion < 20:
    print("el numero es mayor a 10 y menor que 20 ")
elif my_condicion == 25:
    print("el numero es igual a 25")
else:
    print("el numero esta por debajo de 10 o por encima de 20")

my_string = "Mateo Quartin" # Un string vacio es False por defecto
if my_string:
    print("mi cadena de texto no es vacia")



print("la ejecucion continua")
