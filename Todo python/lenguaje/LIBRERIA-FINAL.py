   #MATRICES
from random import *

def matriz_inicial (filas, columnas): #Genera una matriz rellena de 0
    matriz = [0]* filas
    for i in range(filas):
        matriz[i] = [0]*columnas
    return matriz

def llenarmat (matriz): # Rellena la matriz con numeros aleatorios
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if matriz[i][j]==0:
        matriz[i][j]= randint(2,20)
  return matriz

def buscar_columna( tabla , nom_col ): #Sirve para encontrar un numero de columna en base al encabezado
    for i in range(len(tabla[0])):    
        if tabla[0][i] == nom_col:
            return i
    return -1 

# en tabla va la matriz y en nom_col va el elemento que esta en la columna que estoy buscando
# te devuelve el numero de columna en el que esta nom_col, y si no estuviese devuelve -1

def print_tabla( lista ):  #me permite printear una matriz en forma de tabla sin importar los elementos
    for fila in lista:      
        for dato in fila:   
            print(dato, end='\t')  
                            
        print()

#Puedo jugar con los espacios antes del /t ('   /t') para que los elementos esten mas o menos separados. Y puedo separar mas una fila que otra 

def contador (matriz):    #cuenta las veces que se repite un mismo elemento dentro de una matriz
    cont= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==1 or matriz [i][j]=='1' :
                ventas+=1
    return (cont)

def retornar_columna( datos , nom_col ): #devuelve una columna en forma de lista.
    col = buscar_columna(datos , nom_col )
    if col == -1:
        return None
    
    resp = []
    for i in range(len(datos)):   
        resp.append( datos[i][col] )
    
    return resp

#En nom_col debo poner el primer elemento de la columna que quiero

def filtrar_columnas( datos , columnas ): #me devuelve una matriz unicamente con las columnas que me interesan.

    ## Primero tengo que buscar la posición de las columnas de interés
    cols = []   ## Acá guardo las columnas de interés
    for col in columnas:
        col_num = buscar_columna( datos, col )
        if col_num == -1:
            return None
        cols.append(col_num)

    res = []
    for i in range(len(datos)):     ## Para cada fila, incluyendo el encabezado
        fila = []
        for c in cols:
            fila.append( datos[i][c] )
        res.append( fila )
    
    return res

#En datos va la matriz y en columnas va una lista con los primeros elementos de cada columna que quiero

def ordenar_por_col_asc( datos ):  #ordena la matriz por el valor de una columna de menor a mayor
    ln = len(datos)  
    hubo_cambio = True
    i = 0  
    while hubo_cambio and i < ln:
        hubo_cambio = False
        for j in range(ln - 1):  
            if( datos[j][0]>datos[j+1][0] ):
                hubo_cambio = True
                datos[j+1] , datos[j] = datos[j] , datos[j+1]                               
        i+=1
    return datos

def filtrar_filas_comp_col( datos, col_nom , oper , val ): # Arma una nueva matriz fitrando las filas por columna
    OPERACIONES_VALIDAS = [ '<', '>', '==', '!=', '<=', '>=' ] 
    if oper not in OPERACIONES_VALIDAS:
        return None

    col_num = buscar_columna(datos , col_nom )
    if col_num == -1:
        return None
    
    res = [ datos[0] ]      ## Copio el encabezado
    for i in range(1,len(datos)):
        valor = datos[i][col_num]
        if( oper == '==' and ( valor == val ) ):
            res.append( datos[i] )
        elif( oper == '!=' and ( valor != val ) ):
            res.append( datos[i] )
        elif( oper == '<' and ( valor < val ) ):
            res.append( datos[i] )
        elif( oper == '>' and ( valor > val ) ):
            res.append( datos[i] )
        elif( oper == '>=' and ( valor >= val ) ):
            res.append( datos[i] )
        elif( oper == '<=' and ( valor <= val ) ):
            res.append( datos[i] )
    
    return res

#En datos va la matriz, en col_nom va el primer elemento de la columna en la que voy a filtrar
#En val va el valor que voy a poner como filtro y en oper la operacion (si quiero que sea menor, mayor o igual a val)

def ordenar_por_col_desc( lista): #Ordena la matriz por el valor de una columna de mayor a menor
    ln = len(lista)
    hubo_cambio = True
    i=0   
    while hubo_cambio and i < ln:
        hubo_cambio = False
        for  j in range(0, ln-i-1): 
            if lista[j][0] < lista[j+1][0] :
                hubo_cambio = True
                lista[j] , lista[j+1] = lista[j+1] , lista[j]                                               
        i+=1
    return lista 

def diagonales(matriz):  #Devuelve dos listas con los elementos de las dos diagonales de la matriz
    listad1=[]
    listad2=[]
    a = len(matriz)-1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                listad1.append(matriz[i][j])
            if (i+j)==a:
                listad2.append(matriz[i][j])

def ordenar( lista ):  #ordena una lista de menor a mayor
    ln = len(lista)
    for i in range(ln):   
        for j in range(ln-i-1): 
            if( lista[j]>lista[j+1] ):
                aux = lista[j]                                      
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

def ordenaralf(lista): #en orden alfabetico
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

def agarrar_ultimo(lista): #Printea el ultimo elemnto de una lista, puedo printear los ultimos n elementos cambiando la funcion
    print (lista[-1:])
    return

def maximodiv (a,b):  #sirve para obtener el maximo divisor comun entre dos numeros
    diva = []
    divb = []
    divcom = []
    for i in range (1,(a +1)):
        if a % i == 0:
            diva.append(i)
    for j in range (1,(b +1)):
        if b % j == 0:
            divb.append(j)
    for i in range (len(diva)):
        if diva[i] in divb :
            divcom.append(diva[i])
    menor = -10000
    for i in range (len(divcom)):
        if divcom[i]>menor :
            menor = divcom[i]
    return menor

#Ejemplo de validacion con try y except

#n = int(input('Ingrese un numero entre 2 y 10 : '))

def validacion ():
    try:
        col = (int(input('Ingrese un numero de columna : ')))
        while col < 0  :
            col = (int(input('Ingrese un numero de columna valido : ')))
    except:
        col = -1
    return col 

#col = -1 
#while col <  0 :
    #col = validacion()

def frase_a_lista (frase): #transforma una frase en una lista, con todas las palabras como elementos de la lista
    palabra = ''
    lista = []
    print(len(frase))
    for i in range(len(frase)):
        #print(i)
        if frase[i] != ' ' :
            #palabra += mayuscula(frase[i])
            palabra += frase[i]
        if frase [i] == ' ' or i == (len(frase)-1) :
            #print(i)
            lista.append(palabra)
            palabra = ''
    print(lista)
    return lista

#Si uso mayuscula arma la lista con todas las palabras en mayuscula

def mayuscula(c):#convierte una letra minuscula a mayuscula.
 #Deja igual cualquier otro símbolo.
 if c >='a' and c <='z':
    c = chr(ord(c)-ord('a')+ord('A'))
 return c

def minuscula(c):#convierte una letra mayuscula a minuscula.
 #Deja igual cualquier otro símbolo.
 if c >='A' and c <='Z':
    c = chr(ord(c)-ord('A')+ord('a'))
 return c  

def pasaraminusculas (letra): #convierte una letra mayuscula a minuscula
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(minusculas)):
        if (letra==mayusculas[i]):
            letra = minusculas[i]
    return letra

def esMayuscula (letra):
    mayuscula = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if (letra in mayuscula):
        return True
    else:
        return False

def hacerMinuscula (palabra): #pasa una palabra a minusculas
    nueva = ''
    for letra in palabra:
        if esMayuscula(letra):
            letra = pasaraminusculas(letra)
        nueva+=letra
    return nueva


def mayor_y_menor (matriz) :  #devuelve el mayor y el menor valor de una matriz numerica
    for i in range (len(matriz)) :
        for j in range (len(matriz[i])) :
            if matriz[i][j] > mayor :
                mayor = matriz[i][j]
            if matriz [i][j]<menor :
                menor = matriz[i][j]
    print('La matriz es la siguiente : ')
    for i in matriz :
        print(i)
    print()
    print ('El mayor numero de la matriz es : ',mayor,'.Y el menor es',menor)

def definirmatriz (matriz):  #pone indices en una matriz, en este caso jugadores en columnas y numero de ronda en filas.
    matriz [0][0] = 'Rondas'
    for j in range(1,len(matriz[0])):
        matriz[0][j] = ('Jugador ' + str(j)) 
    for i in range(len(matriz)):
        if i != 0 :
            matriz[i][0] = i
    return matriz

def sumacolumnas (matriz):  #devuelve una lista con la suma de cada columna de una matriz numerica
    sumas = []
    for j in range(len(matriz[0])) :
        suma = 0
        for i in range ((len(matriz))):
            suma += matriz[i][j]
        sumas.append(suma)
    return sumas

def palindromo(palabra) :
    v = 0
    if palabra == palabra[::-1] :
        v = 1
    return (v)

def tomarpalindromos (lista) : #Pasa todas las palabras de una lista a minuscula y luego arma una lista con las que sean palindromos 
    listanueva = []
    listapalindromos = []
    for i in range(len(lista)):
        palabra = lista[i]
        min = ''
        for j in range(len(palabra)) :
            min += minuscula(palabra[j])
        listanueva.append(min)
    for i in range(len(listanueva)) :
        if palindromo(listanueva[i]) == 1  :
            listapalindromos.append(listanueva[i])
    print(listapalindromos)

def completartablero (matriz) :  #Buscaminas. Con los try y excpet puedo salir de la matriz sin que salte out of range
    for i in range (len(matriz)) :
        for j in range (len(matriz[i])) :
            if matriz[i][j] == 'B' :
                try:
                    if matriz [i][j+1] != 'B' :
                            matriz[i][j+1] += 1
                except:
                    None
                try:
                    if matriz [i][j-1] != 'B' :
                            matriz[i][j-1] += 1
                except :
                    None
                try:
                    if matriz [i+1][j] != 'B' :
                        matriz[i+1][j] += 1
                except:
                    None
                try:
                    if matriz [i-1][j] != 'B' and i !=0 :
                        matriz[i-1][j] += 1
                except:
                    None
                try:
                    if matriz [i+1][j+1] != 'B' :
                        matriz[i+1][j+1] += 1
                except :
                    None
                try:
                    if matriz [i+1][j-1] != 'B' :
                        matriz[i+1][j-1] += 1
                except:
                    None
                try:
                    if matriz [i-1][j+1] != 'B' and i != 0 :
                        matriz[i-1][j+1] += 1
                except:
                    None
                try:
                    if matriz [i-1][j-1] != 'B' and i !=0 :
                        matriz[i-1][j-1] += 1
                except:
                    None
    return matriz

def matrices(matriz) :  #Escribe todas las submatrices de 3x3 de una matriz cuadrada cuyos elementos sumados dan 45
    for i in matriz :
        print (i)
    for i in range (len(matriz)) :
        #print (matriz[i])
        for j in range ((len(matriz)-2)) : #Resto 2 al buscar submatrices de 3x3
            lista = []
            lista1 = []
            lista2 = []
            c=[]
            if matriz [i][j] + matriz [i][j+1] + matriz [i][j+2] + matriz [i-1][j] + matriz [i-1][j+1] + matriz [i-1][j+2] + matriz [i-2][j] + matriz [i-2][j+1] + matriz [i-2][j+2] == 45 :
                lista2.append(matriz [i-2][j])
                lista2.append(matriz [i-2][j+1])
                lista2.append(matriz [i-2][j+2])
                c.append(lista2)
                lista1.append(matriz [i-1][j])
                lista1.append(matriz [i-1][j+1])
                lista1.append(matriz [i-1][j+2])
                c.append(lista1)
                lista.append(matriz [i][j])
                lista.append(matriz [i][j+1])
                lista.append(matriz [i][j+2])
                c.append(lista)
                print()
                for j in c :
                    print (j)

def primo(num) : #Determina si un numero es primo
    cont = 0
    v= 0
    for i in range (1,num+1) :
        if num%i == 0 :
            cont+=1
    if cont == 2 :
        v = 1
    return v

def factoresprimos (num):  #Devuelve una lista con los factores primos de un numero expresados como potencias
    factores = []
    divisores = []
    lista = []
    for i in range (1,num+1) :
        if num % i == 0 and primo(i) == 1 :
            divisores.append(i)
            cont = 'si' 
            contador = 0
            while cont == 'si' :
                if num % i == 0 and primo(i) == 1 :
                    num = num//i
                    contador +=1
                    factores.append(i)
                else:
                    cont = 'no'
    #print(factores)
    #print(divisores)
    for i in range (len(divisores)) :
        palabra = str(divisores[i])
        conta = 0
        for j in range(len(factores)):
            if divisores[i] == factores[j] :
                conta += 1
        if conta > 1 :
            #print(conta)
            palabra += '^'
            palabra += str(conta)
            lista.append(palabra)
        elif conta == 1 :
            lista.append(palabra)
        print(lista)

# La lista factores devuelve una lista con todos los factores primos, repitiendo los que se repiten.

def factores (num):  #Devuelve una lista con los factores de un numero expresados como potencias
    factores = []
    divisores = []
    lista = []
    for i in range (1,num+1) :
        if num % i == 0 :
            divisores.append(i)
            cont = 'si' 
            contador = 0
            while cont == 'si' :
                if num % i == 0 and primo(i) == 1 :
                    num = num//i
                    contador +=1
                    factores.append(i)
                else:
                    cont = 'no'
    #print(factores)
    #print(divisores)
    for i in range (len(divisores)) :
        palabra = str(divisores[i])
        conta = 0
        for j in range(len(factores)):
            if divisores[i] == factores[j] :
                conta += 1
        if conta > 1 :
            #print(conta)
            palabra += '^'
            palabra += str(conta)
            lista.append(palabra)
        elif conta == 1 :
            lista.append(palabra)
        print(lista)

def sumadiv (num): #Esta funcion sirve para contar la suma de los divisores de un numero
  suma=0
  i=1
  while i<num:
    if (num%i==0):
      suma +=i
    i+=1
  return suma
   
#ARCHIVOS 

# Funcion que arme una matriz con cada renglon del archivo como fila
# Funcion que transforme el archivo en un str
# Funcion que arme una lista con los elementos del archivo
# Funcion que arme una lista con cada renglon del archivo como elemento

def split( s , c ): #con esta funcion split, delimito 2 condiciones c y d osea puede ser una , y un \n
    res = []
    last_no_c = 0
    for i in range(len(s)): 
        if s[i] == c:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
    if len(s)>last_no_c:
        res.append(s[last_no_c:])
    return res

def split2( s , c ,d): #con esta funcion split, delimito 2 condiciones c y d osea puede ser una , y un \n
    res = []
    last_no_c = 0
    for i in range(len(s)): 
        if s[i] == c:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
        if s[i] == d:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
    if len(s)>last_no_c:
        res.append(s[last_no_c:])
    return res

def split3( s , c ,d ,f): #con esta funcion split, delimito 2 condiciones c y d osea puede ser una , y un \n
    res = []
    last_no_c = 0
    for i in range(len(s)): 
        if s[i] == c:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
        if s[i] == d:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
        if s[i] == f:
            if i-last_no_c>0:
                res.append(s[last_no_c:i])
            last_no_c=i+1
    if len(s)>last_no_c:
        res.append(s[last_no_c:])
    return res

def armartexto(archivo) : # Transforma cada palabra del archivo en un elemento de una lista 
    fd = open(archivo,'r')
    texto = fd.read()
    texto1 = split3(texto, '\n' , ',',' ')
    fd.close()
    return(texto1)

#Importantisimo ver el split, si es un solo renglon no hace falta el '\n.

def matrizarchivo( archivo ): #arma una matriz con cada renglon del archivo como fila 
    fd = open(archivo, 'r' )
    matriz = []
    header = True
    line =1
    while line :
        line = fd.readline()
        if line != '':
            matriz.append( split2( line[:len(line)-1] , ' ',',' ) )
    fd.close()
    return matriz

def armarlista(archivo) : # Transforma cada palabra del archivo en un elemento de una lista 
    fd = open(archivo,'r')
    texto = fd.read()
    texto1 = split(texto, '\n' )
    fd.close()
    return(texto1)

# Todas estas funciones son muy similares, lo que va variando es el split

def escribirmatriz (fname, contenido):  #Crea un archivo en el que escribe una matriz
    fd=open(fname ,'w')
    for i in range(len(contenido)):
        for j in range(len(contenido[i])):
            fd.write(str(contenido[i][j]))
        fd.write('\n')
    fd.close()

def join(c, lista): # Transforma una lista en str separando sus elementos por lo que ponga en c (suele ser un espacio)
    res=''
    ll = len(lista)
    for i in range(ll):
        res+= str(lista[i])
        if(i+1<ll):
            res+=c
    return res

def format_contenido(matriz): #Formatea el contenido de una matriz para poder escribirlo en un archivo
    cont = []
    #cont.append(str(len(matriz)) + ' ' + str(len(matriz[0])) + '\n' )
    for fila in matriz:
        cont.append(join(' ', fila) + '\n')
    return cont

def creararchivo(fname, matriz): #recibe una matriz y la escribe en un archivo
    contenido = format_contenido(matriz)
    fd=open(fname ,'w')
    for linea in contenido:
        fd.write(linea)
    fd.close()

def archivolista (fname, lista) : #recibe una lista y la escribe en un archivo separando sus elementos por un espacio
    contenido = join(' ',lista)
    fd=open(fname ,'w')
    for linea in contenido:
        fd.write(linea)
    fd.close()

def strarchivo(fname, matriz): #recibe un str y lo escribe tal cual en un archivo   
    fd=open(fname ,'w')
    for linea in matriz:
        fd.write(linea)
    fd.close()


