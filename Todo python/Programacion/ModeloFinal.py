#Dada una lista de N elementos, desplazar todos los elementos de la lista  a la derecha de una posicion, pero dejando intacto
#el intervalo interior viene dado por 2 numeros ingresados al "final" e "inicial" 

vec1 = []

n = int(input("ingresar cantidad de numeros:"))
comienzo = int(input("ingresar numero comienzo"))
final = int(input("ingresar numero final:"))

for i in range (n):
    vec1.append(int(input("ingresar numero: ")))
    
print (vec1)