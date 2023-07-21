# Lucas Cenzano 44661963 

def cargar_matriz():
    matriz = []
    n = int(input("Ingrese la cantidad de electrodomésticos: "))
    for i in range(n):
        nombre = input("Ingrese el nombre del electrodoméstico: ")
        proveedor = input("Ingrese el proveedor del electrodoméstico: ")
        while True:
            try:
                precio = int(input("Ingrese el precio del electrodoméstico: "))
                if precio < 0:
                    print("El precio no puede ser negativo")
                else:
                    break
            except ValueError:
                print("El precio debe ser un número.")
        while True:
            try:
                stock = int(input("Ingrese la cantidad en stock del electrodoméstico: "))
                if stock < 0:
                    print("El stock no puede ser negativo ")
                else:
                    break
            except ValueError:
                print("El stock debe ser un número entero.")
        matriz.append([nombre, proveedor, str(precio), str(stock)])
    mostrar_matriz(matriz)
    return matriz


def agregar_electrodomestico(m):
    n = int(input("¿Cuanros elecrodomesticos desea agregar?"))
    for i in range(n):
        nombre = input("Ingrese el nombre del electrodoméstico: ")
        proveedor = input("Ingrese el proveedor del electrodoméstico: ")
        while True:
            try:
                precio = int(input("Ingrese el precio del electrodoméstico: "))
                if precio < 0:
                    print("El precio no puede ser negativo")
                else:
                    break
            except ValueError:
                print("El precio debe ser un número.")
        while True:
            try:
                stock = int(input("Ingrese la cantidad en stock del electrodoméstico: "))
                if stock < 0:
                    print("El stock no puede ser negativo ")
                else:
                    break
            except ValueError:
                print("El stock debe ser un número entero.")
        m.append([nombre, proveedor, str(precio), str(stock)])
    mostrar_matriz(m)
    return m

def eliminar_electrodomestico(m):
    nombre = input("Ingrese el nombre que desea eliminar: ")
    proveedor = input("Ingrese el nombre del proveedor que desea eliminar: ")
    for i in range(len(m)):
        if m[i][0] == nombre and m[i][1] == proveedor:
            del m [i] #elimina la fila deseada
    mostrar_matriz(m)
    return m
        
def mostrar_matriz(m):
    for fila in m:
        for valor in fila:
            print(valor, end=" ")
        print()

def modificar_precio(m):
    nombre = input("Ingrese el nombre que desea modificar el precio: ")
    proveedor = input("Ingrese el nombre del proveedor que desea modificar el precio: ")
    for i in range(len(m)):
        if m[i][0] == nombre and m[i][1] == proveedor:
            precio = int(input("Ingrese el precio nuevo: "))
            m[i][2] = str(precio)
    mostrar_matriz(m)
    return m

def modificar_stock(m):
    nombre = input("Ingrese el nombre que desea modificar el stock: ")
    proveedor = input("Ingrese el nombre del proveedor que desea modificar el stock: ")
    for i in range(len(m)):
        while m[i][0] == nombre and m[i][1] == proveedor:
            stock = int(input("Ingrese el stock nuevo: "))
            if stock < 0:
              print("El stock es negativo !! ")
              break
            else:
                m[i][3] = str(stock)
            break
    mostrar_matriz(m)
    return m

def mostrar_sinstock(m):
    print("Electrodomésticos sin stock :")
    for electrodomestico in m:
        stock = int(electrodomestico[3])
        if stock == 0:
            print(f"Nombre: {electrodomestico[0]}, Proveedor: {electrodomestico[1]}, Precio: {electrodomestico[2]}, Stock: {electrodomestico[3]}")

def mostrar_ordenados(m):
    for i in range(len(m)-1):
        for j in range(i+1,len(m)):
            for h in range (3):
                if(m[j][0] < m[i][0]):
                    aux = m[i][h]
                    m[i][h]=m[j][h]
                    m[j][h]=aux
    mostrar_matriz(m)
    
matriz = []
while True:
    print("---- Menú ----")
    print("1. Cargar matriz")
    print("2. Agregar electrodomesticos")
    print("3. Eliminar electrodomesticos")
    print("4. Modificar el precio de un electrodomestico")
    print("5. Modificar el stock")
    print("6. Mostrar electrodomésticos sin stock")
    print("7. Mostrar electrodomesticos ordenados por nombre ")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        matriz = cargar_matriz()
    elif opcion == "2":
        matriz= agregar_electrodomestico(matriz)
    elif opcion == "3":
        matriz = eliminar_electrodomestico(matriz)
    elif opcion == "4":
        matriz = modificar_precio(matriz)
    elif opcion == "5":
        matriz = modificar_stock(matriz)
    elif opcion == "6":
        mostrar_sinstock(matriz)
    elif opcion == "7":
        mostrar_ordenados(matriz)
    elif opcion == "0":
        break