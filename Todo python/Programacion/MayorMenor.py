x = int(input("ingresar cantidad de numeros "))
n = int(input("ingresar numero: "))
may = n
min = n 
for i in range (x-1):
    m = int(input("ingresar un numero: "))
    if m > may:
        may = m
    if m < min:
        min = m

print ("el numero menor es: {}, y el mayor es: {}".format(min, may))
