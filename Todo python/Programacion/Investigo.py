'''''
#funciones
texto = 'mateo quartin es un alumno regular'
print (texto.find('morales')) #la funcion find se utiliza para saber la posicion en la cadena que contiene la variable de no estar en la cadena da un como resultado -1

fruta = 'MaTeo'
print(fruta.upper())#.upper convierte la cadena en mayusculas todas

len(fruta) # devuelve la cantidad de caracteres de la cadena 

#slice
mensaje = 'cachete'
print (mensaje [2:4]) #con los corchetes y indicando la posicion imprimo o me refiero a la posicion del str


frutilla = 'que hago de mi vida'

for i in range (len(frutilla)):
    print (frutilla[i])
    

vector1 = [1, 2, 3, 4, 5]
vector2 = [22, 34]
vector1.extend(vector2)
print (vector1 )#con el extend agrego los elementos de un vector en el otro
'''



vector1 = [1, 4, 3, 5, 2]
vector1.sort
print(vector1)