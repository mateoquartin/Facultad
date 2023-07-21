def leer_archivo():
    """
    Lee el archivo 'padron.txt' y devuelve una lista de tuplas con los datos de los votantes.
    Cada tupla tiene la siguiente estructura:
    (DNI, apellido y nombre, partido, sexo, mesa)
    """
    votantes = []
    with open("padron.txt", "r") as archivo:
        for linea in archivo:
            dni = linea[0:8]
            apellido_nombre = linea[8:20]
            partido = linea[20:23]
            sexo = linea[23]
            mesa = linea[24:28]
            votante = (dni, apellido_nombre.strip(), partido, sexo, mesa)
            votantes.append(votante)
    return votantes

def cantidad_votantes(votantes):
    """
    Recibe una lista de tuplas con los datos de los votantes y devuelve la cantidad total de votantes.
    """
    return len(votantes)

def cantidad_votantes_genero(votantes):
    """
    Recibe una lista de tuplas con los datos de los votantes y devuelve la cantidad de votantes masculinos y femeninos.
    """
    votantes_masculinos = 0
    votantes_femeninos = 0
    for votante in votantes:
        if votante[3] == "m":
            votantes_masculinos += 1
        elif votante[3] == "f":
            votantes_femeninos += 1
    return votantes_masculinos, votantes_femeninos

def cantidad_votantes_partido(votantes, partido):
    """
    Recibe una lista de tuplas con los datos de los votantes y el nombre de un partido.
    Devuelve la cantidad de votantes que pertenecen a ese partido.
    """
    cantidad = 0
    for votante in votantes:
        if votante[2] == partido:
            cantidad += 1
    return cantidad

def generar_archivo_csv(votantes):
    """
    Recibe una lista de tuplas con los datos de los votantes.
    Genera un nuevo archivo de texto llamado 'padron.csv' con los mismos datos, separados por comas.
    """
    with open("padron.csv", "w") as archivo:
        for votante in votantes:
            linea = ",".join(votante) + "\n"
            archivo.write(linea)
def main():
    votantes = leer_archivo()
    while True:
        print("Seleccione una opción:")
        print("a. Cantidad de votantes")
        print("b. Cantidad de votantes femeninos y masculinos")
        print("c. Cantidad de votantes de un partido")
        print("d. Generar archivo CSV")
        print("e. Salir")
        opcion = input("Opción: ")
        if opcion == "a":
            print("Cantidad de votantes:", cantidad_votantes(votantes))
        elif opcion == "b":
            votantes_masculinos, votantes_femeninos = cantidad_votantes_genero(votantes)
            print("Cantidad de votantes masculinos:", votantes_masculinos)
            print("Cantidad de votantes femeninos:", votantes_femeninos)
        elif opcion == "c":
            partido = input("Ingrese el nombre del partido: ")
            cantidad = cantidad_votantes_partido(votantes, partido)
            print(f"Cantidad de votantes del partido {partido}: {cantidad}")
        elif opcion == "d":
            generar_archivo_csv(votantes)
            print("Archivo CSV generado correctamente.")
        elif opcion == "e":
            break
        else:
            print("Opción inválida.")
