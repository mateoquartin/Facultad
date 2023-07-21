#mayor de tres numeros 
"""
print("ingresa 3 numeros")
X=int(input("ingresa un numero:"))
Y=int(input("ingresa otro numero:"))
Z=int(input("ingresa otro numero:"))
may=0
if X<Y:
    may=Y
else: 
    may=X
if may<Z:
    may=Z    
print("El numero mas alto de los 3 es el:",may)
"""
#Crear un programa que determine el valor máximo entre 10 números utilizando las 
#funciones/procedimientos del ejercicio anterior
"""
#mayor de 10 numeros
def mayor(a,b):
    if a>b:
        may=a
    else:
        may=b
    return may

x=int(input("ingresa un numero: "))
c=10
for i in range (c):
    y=int(input("ingresa un numero: "))
    m=mayor(x,y)
    print("el numero mayor es: ",m)
    x=m
print("fin")
"""
#ejercicio 3
#Crear un programa que:
#a) cargue dos vectores A y B, con N y M números enteros respectivamente
#b) calcular la suma de los números cargados en cada vector.
#c) si N y M son iguales, realice la suma de los vectores. Mostrar el vector resultante
#¿Cuántas funciones y/o procedimientos son necesarios para resolver este problema?



#ejercicio 4
#Crear un programa que cargue una o más oraciones y luego indique la suma total de vocales y
#consonantes:
#- Crear dos funciones, una para contar las vocales y otra para contar las consonantes que tiene
#cada palabra.
#- Cada función tomará como parámetro una palabra.
#- En el programa principal mostrar la cantidad total de vocales y la cantidad total de consonantes
#en el texto de entrada

def vocales(palabra):
    total=0
    todaslasvocales='A,a,á,E,é,e,I,í,i,O,ó,o,U,ú,u'
    for i in (palabra):
        if i in todaslasvocales:
            total=total+1
    return total

def consonantes2(palabra):
    total= len(palabra)-vocales(palabra)
    return total

texto=input("Ingresar texto: ").lower()
print("cantidad de vocales", vocales(texto))
print("cantidad de consonantes", consonantes2(texto))

'''
#capicua
def capicua(numero):
    aux=0
    temp=numero
    while numero>0:
        d= numero % 10
        aux=aux*10+d
        numero=numero/10
    if aux==temp:
        x=True
    else: x=False
    return x
'''