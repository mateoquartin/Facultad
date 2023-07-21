# Cargar la matriz
m = int(input("Ingrese el número de filas (M): "))
n = int(input("Ingrese el número de columnas (N): "))

matriz = []
for i in range(m):
    fila = []
    for j in range(n):
        elemento = int(input(f"Ingrese el elemento ({i}, {j}): "))
        fila.append(elemento)
    matriz.append(fila)

# Inicializar listas para almacenar las sumas de las diagonales
diagonales = []
for _ in range(m + n - 1):
    diagonales.append(0)

# Sumar las diagonales
for i in range(m):
    for j in range(n):
        diagonales[i - j + n - 1] += matriz[i][j]

# Mostrar los resultados
for k, suma in enumerate(diagonales):
    print(f"Suma de la diagonal {k + 1}: {suma}")
