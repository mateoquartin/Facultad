filas = int(input("ingresar cantidad de filas: "))
columnas = int(input("ingresar cantidad de columnas: "))

matriz = []
for i in range (filas):
    matriz.append([None]*columnas)
for i in range (filas):
      for j in range (columnas):
            valor = input("ingresar un valor para la fila {} y la columna {}: ".format(i+1, j+1))
            matriz[i][j] = valor
for fila in matriz:
    print(fila)

