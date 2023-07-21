filas = int(input("ingresar numero de filas: "))
columnas = int(input("ingresar numero de columnas: "))
suma = 0
matrix = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = input("Ingrese el elemento en la posición ({}, {}): ".format(i, j))
        fila.append(elemento)
    matrix.append(fila)

m = len(matrix)
print (m)