import time
matriz = []
def carga_matriz():
    matriz = []
    m = int(input("Ingrese la cantidad de electrodomésticos: "))
    for k in range(m):
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

def agregar_producto(b):
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
        b.append([nombre, proveedor, str(precio), str(stock)])
    mostrar_matriz(b)
    return b

def eliminar_producto(n):
    nombre = input("Ingrese el nombre que desea eliminar: ")
    proveedor = input("Ingrese el nombre del proveedor que desea eliminar: ")
    for i in range(len(n)):
        if n[i][0] == nombre and n[i][1] == proveedor:
            del n [i] 
    mostrar_matriz(n)
    return n

def mostrar_matriz(n):
    for fila in (n):
        for valor in fila:
            print(valor, end=" ")
        print()

def modificar_precio(n):
    nombre = input("Ingrese el nombre que desea modificar el precio: ")
    proveedor = input("Ingrese el nombre del proveedor que desea modificar el precio: ")
    for i in range(len(n)):
        if n[i][0] == nombre and n[i][1] == proveedor:
            precio = int(input("Ingrese el precio nuevo: "))
            n[i][2] = str(precio)
    mostrar_matriz(n)
    return n

def modificar_stock(n):
    nombre = input("Ingrese el nombre que desea modificar el stock: ")
    proveedor = input("Ingrese el nombre del proveedor que desea modificar el stock: ")
    for i in range(len(n)):
        while n[i][0] == nombre and n[i][1] == proveedor:
            stock = int(input("Ingrese el stock nuevo: "))
            if stock < 0:
              print("El stock es negativo !! ")
              break
            else:
                n[i][3] = str(stock)
            break
    mostrar_matriz(n)
    return n

def mostrar_sinstock(n):
    print("Electrodomésticos sin stock :")
    for electrodomestico in n:
        stock = int(electrodomestico[3])
        if stock == 0:
            print(f"Nombre: {electrodomestico[0]}, Proveedor: {electrodomestico[1]}, Precio: {electrodomestico[2]}, Stock: {electrodomestico[3]}")

def mostrar_Sordenados(n):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            for h in range (3):
                if(n[j][0] < n[i][0]):
                    aux = n[i][h]
                    n[i][h]=n[j][h]
                    n[j][h]=aux
    mostrar_matriz(n)


while True:
    print("~~~BIENVENIDO AL MENU DE CONTROL DE STOCK~~~")
    time.sleep(2)
    print("1.Cargar cantidad de estock y precio")
    print("2.Agregar nuevo electrodomestico")
    print("3.Eliminar electrodomestico a partir de nombre y proveedor")
    print("4.Modificar precio de un electrodomestico")
    print("5.Modificar stock de un electrodomestico determinado")
    print("6.Mostrar electrodomestico sin stock")
    print("7.Mostrar electrodomesticos ordenados por nombre")
    print("0.Salir")
    opcion = input("ingresa opcion a realizar: ")
    if opcion == "1":
        matriz = carga_matriz()
    elif opcion == "2":
        matriz = agregar_producto(matriz)
    elif opcion == "3":
        matriz = eliminar_producto(matriz)
    elif opcion == "4":
        matriz = modificar_precio(matriz)
    elif opcion == "5":
        matriz = modificar_stock(matriz)
    elif opcion == "6":
        mostrar_sinstock(matriz)
    elif opcion == "7":
        mostrar_Sordenados(matriz)
    elif opcion == "0":
        break

    

    
       

