def carga_matriz(matriz, filas, columnas):
    matriz = []
    for i in range (filas):
        matriz.append([None]*columnas)
    for i in range (filas):
        for j in range (columnas):
            valor = input("ingresar valor en la fila {} y columna {}: ".format(i+1,j+1))
            matriz[i][j] = valor
    for filas in matriz:
        print(filas)

opcion = int(input("ingresar la opcion a realizar"))
if opcion == 1:
    carga_matriz