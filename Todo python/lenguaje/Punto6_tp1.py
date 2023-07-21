    # Escriba un programa que para dos matrices A y B de números enteros de dimensiones MxN, realice la
# suma o el producto de las matrices (a elección del usuario) y las cargue en otra matriz C.
# Utilizar funciones y/o procedimientos para:
# cargar las matrices
# realizar la suma
# realizar el producto
# mostrar en pantalla una matriz 
  
def carga_matrices(matri,fila,columna):
    for k in range(fila):
        for j in range(columna):
            print("Ingresar el elemento [",k+1,",",j+1,"] de la matriz:")
            matri[k][j]= int(input())
    
def mostrar_matrices(matri1,fila1,columna1):
    for k in range(fila1):
        print()
        for j in range(columna1):
            print(matri1[k][j],"    ", end="")    
    
def suma_de_matrices(ma1,ma2,fila2,columna2):
    matrizC = []
    for k in range(fila2):
        matrizC.append([None]*columna2)
    for k in range(fila2):
        for j in range(columna2):
            matrizC[k][j] = ma1[k][j] + ma2[k][j]
    return mostrar_matrices(matrizC,fila2,columna2)
        
def producto_de_matrices(ma3,ma4,fila3,columna3):
    matrizD = []
    for k in range(fila3):
        matrizD.append([0]*columna3)
    for k in range(fila3):
        for j in range(columna3):
            for l in range(columna3):
                matrizD[k][j] += ma3[k][l] * ma4[l][j]
        return mostrar_matrices(matrizD,fila3,columna3)

while True:     
    decision = str(input("¿Desea ingresar al programa? : ")).lower().strip()
    if decision == "si":
        decision1 = int(input("Opciones del menú: 1=Sumar Matrices; 2=Multiplicar Matrices : "))
        filass = int(input("Ingresar el tamaño de la fila de la matriz:"))
        columnass = int(input("I    ngresar el tamaño de la columna de la matriz:"))
        matrizA = []
        matrizB = []
        for k in range(filass):
            matrizA.append([None]*columnass)
            matrizB.append([None]*columnass)
        print("Carga de Matriz A")
        carga_matrices(matrizA,filass,columnass)
        print("Carga de Matriz B")
        carga_matrices(matrizB,filass,columnass)
        if decision1 == 1:
            suma_de_matrices(matrizA,matrizB,filass,columnass)
        else:
            producto_de_matrices(matrizA,matrizB,filass,columnass)
    else:
        break