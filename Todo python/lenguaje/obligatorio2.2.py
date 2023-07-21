import csv
import datetime
import os

def menu():
    print("BIENVENIDO AL MENÚ")
    print("1. Registrar nueva factura")
    print("2. Eliminar factura")
    print("3. Mostrar facturas de un cliente")
    print("4. Mostrar facturas ordenadas por fecha")
    print("5. Salir")

def registrar_factura():
    fecha_valida = False
    while not fecha_valida:
        fecha_input = input("Ingrese la fecha de la factura (formato dia/mes/año): ")
        try:
            fecha = datetime.datetime.strptime(fecha_input, '%d/%m/%Y')
            fecha_valida = True
        except ValueError:
            print("La fecha ingresada no es válida. Por favor ingrese una fecha coherente")
    numero = input("Ingrese el número de factura: ")
    nombre = input("Ingrese el nombre del cliente: ")
    monto = input("Ingrese el monto de la factura: ")

    with open("facturas_v3.txt", "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([fecha.strftime('%d/%m/%Y'), numero, nombre, monto])
        print("Factura registrada exitosamente!")

def eliminar_factura():
    numero = input("Ingrese el número de factura a eliminar: ")

    with open("facturas_v3.txt", "r") as file:
        reader = csv.reader(file, delimiter=";")
        facturas = list(reader)

    with open("facturas_v3.txt", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        eliminado = False
        for factura in facturas:
            if factura[1] == numero:
                eliminado = True
            else:
                writer.writerow(factura)

        if eliminado:
            print("Factura eliminada exitosamente!")
        else:
            print("No se encontró la factura indicada.")

def mostrar_facturas_cliente():
    nombre = input("Ingrese el nombre del cliente a buscar: ").lower() # Convertir a minúsculas

    with open("facturas_v3.txt", "r") as file:
        reader = csv.reader(file, delimiter=";")
        facturas = list(reader)

    facturas_cliente = []
    for factura in facturas:
        if factura[2].lower() == nombre: # Convertir a minúsculas
            facturas_cliente.append(factura)

    if facturas_cliente:
        facturas_cliente.sort(key=lambda x: int(x[1]))
        print("Facturas encontradas:")
        for factura in facturas_cliente:
            print(f"Fecha: {factura[0]}, Número: {factura[1]}, Monto: {factura[3]}")
    else:
        print("No se encontraron facturas para el cliente indicado.")

def mostrar_facturas_fecha():
    with open("facturas_v3.txt", "r") as file:
        reader = csv.reader(file, delimiter=";")
        facturas = list(reader)

    facturas.sort(key=lambda x: datetime.datetime.strptime(x[0], '%d/%m/%Y'))

    print("Facturas ordenadas por fecha:")
    for factura in facturas:
        print(f"Fecha: {factura[0]}, Número: {factura[1]}, Cliente: {factura[2]}, Monto: {factura[3]}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_factura()
        elif opcion == "2":
            eliminar_factura()
        elif opcion == "3":
            mostrar_facturas_cliente()
        elif opcion== "4":
                mostrar_facturas_fecha()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
