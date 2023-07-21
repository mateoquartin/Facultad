def leer_archivo(nombre_archivo):
    votantes = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            dni = linea[0:8].strip()
            nombre = linea[8:20].strip()
            partido = linea[20:23].strip()
            sexo = 0 if linea[23] == 'm' else 1  # Convertir el valor del género a un valor numérico
            mesa = linea[24:28].strip()
            votante = {'dni': dni, 'nombre': nombre, 'partido': partido, 'sexo': sexo, 'mesa': mesa}
            votantes.append(votante)
    return votantes

# Procedimiento para imprimir la cantidad de votantes
def imprimir_cantidad_votantes(votantes):
    cantidad_votantes = len(votantes)
    print(f"La cantidad de votantes es: {cantidad_votantes}")

# Procedimiento para imprimir la cantidad de votantes por género
def cantidad_votantes_genero(votantes):

    votantes_masculinos = 0
    votantes_femeninos = 0
    for votante in votantes:
        if votante == "m":
            votantes_masculinos += 1
        elif votante == "f":
            votantes_femeninos += 1
    return votantes_masculinos, votantes_femeninos

# Procedimiento para imprimir la cantidad de votantes por partido
def imprimir_cantidad_votantes_partido(votantes):
    partido_solicitado = input("Ingrese el partido que desea consultar: ")
    cantidad_votantes_partido = sum(1 for votante in votantes if votante['partido'] == partido_solicitado)
    print(f"La cantidad de votantes del partido {partido_solicitado} es: {cantidad_votantes_partido}")

# Procedimiento para generar un nuevo archivo de texto con los datos separados por comas
def generar_archivo_comas(nombre_archivo_entrada, nombre_archivo_salida):
    votantes = leer_archivo(nombre_archivo_entrada)
    with open(nombre_archivo_salida, 'w') as archivo:
        for votante in votantes:
            linea = f"{votante['dni']},{votante['nombre']},{votante['partido']},{votante['sexo']},{votante['mesa']}\n"
            archivo.write(linea)
    print(f"Archivo generado con éxito: {nombre_archivo_salida}")

# Llamadas a las funciones y procedimientos
votantes = leer_archivo("padron.txt")
imprimir_cantidad_votantes(votantes)
cantidad_votantes_genero(votantes)
imprimir_cantidad_votantes_partido(votantes)
generar_archivo_comas("padron.txt", "padron_comas.txt")

def Menu():
    print("Menú:")
    print("1. Cantidad de votantes")
    print("2. Cantidad de votantes por género")
    print("3. Cantidad de votantes por partido")
    print("4. Generar archivo con campos separados por comas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
def main():
    while True:
        Menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            imprimir_cantidad_votantes()
        elif opcion == "2":
            imprimir_cantidad_votantes_genero()
        elif opcion == "3":
            imprimir_cantidad_votantes_partido()
        elif opcion== "4":
                generar_archivo_comas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")