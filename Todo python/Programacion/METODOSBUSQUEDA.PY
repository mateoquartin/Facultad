#Búsqueda secuencial mejorada
#No necesito ordenar la lista, si los números se repiten me devuelve la primera posición del número

n=int(input("Dimension A: "))
a=[None]*n

for i in range(n):
    a[i]=int(input("Ingrese nro: "))
print (a)

buscado=int(input("numero buscado: "))
i=0
b=0

while (i<n  and b==0):
    if a[i]==buscado:
        print("El número buscado ", buscado," se encuentra en la posición ",i+1)
        b=1
    else:
        i=i+1

if b==0:
    print("no se encontró buscado, posición: ", -1)

#Búsqueda secuencial simple 
#Ahora si me interesa saber cuáles son las posiciones ocupadas en el caso de tener una lista con repetidos desarrollo el algoritmo de búsqueda secuencial utilizando un ciclo sin condición.

n=int(input("Dimension A: "))
a=[None]*n

for i in range(n):
    a[i]=int(input("Ingrese nro: "))
    
print (a)
buscado=int(input("numero buscado: "))
b=0

for i in range(n):
    if a[i]==buscado:
        print("El número buscado ", buscado," se encuentra en la posición ",i)
        b=1
if b==0:
    print("no se encontró buscado, posición: ", -1)

#Búsqueda binaria
#Tenemos que tener la lista ordenada y nuestro espacio de búsqueda se irá achicando a segmentos cada vez menores de la lista original. La idea es descartar segmentos de la lista donde el valor seguro que no puede estar:
#1.	Consideramos como segmento inicial de búsqueda a la lista completa.
#2.	Analizamos el punto medio del segmento (el valor central), si es el valor buscado, devolvemos el índice del punto medio.
#3.	Si el valor central es mayor al buscado, podemos descartar el segmento que está desde el punto medio hacia la a derecha.
#4.	Si el valor central es menor al buscado, podemos descartar el segmento que está desde el punto medio hacia la izquierda.
#5.	Una vez descartado el segmento que no nos interesa, volvemos a analizar el segmento restante, de la misma forma.
#6.	Si en algún momento el segmento a analizar tiene longitud 0 o negativa significa que el valor buscado no se encuentra en la lista.
#Para señalar la porción del segmento que se está analizando a cada paso, utilizaremos dos variables (izq y der) que contienen la posición de inicio y la posición de fin del segmento que se está considerando.
#De la misma manera usaremos la variable medio para contener la posición del punto medio del segmento.

n=int(input("Dimension A: "))
a=[None]*n

for i in range(n):
    a[i]=int(input("Ingrese nro: "))
for i in range(n-1):  
  for j in range(i+1,n,1):
    if (a[i]>a[j]):
      aux = a[i]
      a[i]=a[j]
      a[j]=aux
      
print (a)
buscado=int(input("numero buscado: "))
izq=0
der=n-1
b=0
while (izq<=der and b==0):
    m=(izq + der)//2
    if a[m]==buscado:
        print("El número buscado ", buscado," se encuentra en la posición ",m)
        b=1
    else:
        if (buscado> a[m]):
            izq=m+1
        else:
            der=m-1
if b==0:
    print("no se encontró buscado, posición: ", -1)
