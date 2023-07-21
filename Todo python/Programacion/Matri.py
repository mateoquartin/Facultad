filas = int(input("ingresar numero de filas: "))
columnas = int(input("ingresar numero de columnas: "))
matrix = []
for i in range (filas):
    matrix.append([None]*columnas)
for i in range (filas):
    for j in range (columnas):
        valor = input("ingresar el valor para la fila{} y columna{}: ".format(i+1, j+1))
        matrix[i][j] = valor
print (matrix)

for i in range (filas):
    for j in range(columnas):
        if [i][j] == [1][1]:
            Suma1 = [i][j]
            print(Suma1)




