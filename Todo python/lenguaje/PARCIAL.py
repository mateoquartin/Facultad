
def cargar_matriz():
    autos = int(input("ingresa la cantidad de autos"))
    matriz = []
    for i in range (autos):
       nombre = input("ingresar apellido y nombre")
       provincia = input("ingresa la provincia")
       patente = str(input("ingresa la patente"))
       encontrado = False
       for autos in matriz:
            if patente in autos:
                encontrado = True
                print("la patente ya esta en el registro.")
            else:
                break
       while True:
            try:
                dni = int(input("ingrese el dni sin puntos ni coma"))
                if dni < 0:
                    print("el dni no puede ser negativo")
                else:
                    break
            except ValueError:
                print("el dni tiene que ser un numero")
       while True:
            try:
                modelo = int(input("Ingrese modelo"))
                if modelo < 0:
                    print("el modelo no puede ser negativo")
                else:
                    break
            except ValueError:
                print("El modelo debe ser un numero")
       matriz.append([patente, str(dni), nombre, str(modelo),provincia])
    mostrar_matriz(matriz)
    return(matriz)

def cargar_dominio(m):
    autos = int(input("ingresa la cantidad de autos que desea agregar: "))
    for i in range (autos):
        nombre = input("ingresar apellido y nombre")
        provincia = input("ingresa la provincia")
        patente = str(input("ingresa la patente"))
        encontrado = False
        for autos in m:
                if patente in autos:
                    encontrado = True
                    print("la patente ya esta en el registro.")
                else:
                    break
        while True:
                try:
                    dni = int(input("ingrese el dni sin puntos ni coma"))
                    if dni < 0:
                        print("el dni no puede ser negativo")
                    else:
                        break
                except ValueError:
                    print("el dni tiene que ser un numero")
        while True:
                try:
                    modelo = int(input("Ingrese modelo"))
                    if modelo < 0:
                        print("el modelo no puede ser negativo")
                    else:
                        break
                except ValueError:
                    print("El modelo debe ser un numero")
        m.append([patente, str(dni), nombre, str(modelo),provincia])
        mostrar_matriz(m)
        return(m)


def buscar_dominio(m):
    dato = input("ingrese el dato a buscar")
    filas_encontradas = []
    for i, fila in enumerate(m):
        if dato in fila:
            filas_encontradas.append(i)
    if filas_encontradas:
        print("el dato", dato,"no se encuentra en los dominios: " )
        for fila_encontrada in filas_encontradas:
            print(fila_encontrada + 1)
    else:
        print("el dato", dato, "no se encuentra en la matriz")
    mostrar_matriz(fila_encontrada)
    return(fila_encontrada)

def eliminar_patente(m):
    patente = input("Ingresar patente a buscar: ")
    for i in range (len(m)):
        if m[i][0] == patente:
            del m[i]
        else:
            print("Errror, la patente que desea eliminar no se encuentra ")
    mostrar_matriz(m)
    return(m)

def modifica_dominio(m):
    patente = input("Ingresar patente a buscar: ")
    for i in range (len(m)):
        if m[i][0] == patente:
            while True:
                try:
                    doc = int(input("ingresa el nuevo documento"))
                    if  doc < 0:
                        print("el documento no puede ser negativo")
                    else:
                        break
                except ValueError:
                    print("el dni tiene que ser un numero")
                m[i][1] = str(doc)
            m[i][2] = input("ingrese el nuevo apellido y nombre")
            while True:
                try:
                    model = int(input("ingresa el nuevo modelo"))
                    if  model < 0:
                        print("el modelo no puede ser negativo")
                    else:
                        break
                except ValueError:
                    print("el modelo tiene que ser un numero")
                m[i][3] = str(model)
            m[i][4] = input("ingresar la nueva localidad")
            mostrar_matriz(m)
            return m

    

def mostrar_matriz (m):
    for fila in (m):
        for valor in fila:
            print(valor, end=" ")
        print()

matriz = []
while True:
    print("~~~Bienvenido al menu~~~")
    print("1. Cargar la matriz con los dominios")
    print("2. Cargar nuevo dominio en la matriz")
    print("3. buscar un dominio por cualquier dato")
    print("4. eliminar un dominio de la lista")
    print("5. modificar un dominio")
    print("0. salir")
    opcion = input("ingresa una opcion: ")
    if opcion == "1":
        matriz = cargar_matriz()
    elif opcion == "2":
        matriz = cargar_dominio(matriz)
    elif opcion == "3":
        buscar_dominio(matriz)
    elif opcion == "4":
        matriz = eliminar_patente(matriz)
    elif opcion == "5":
        matriz = modifica_dominio(matriz)
    elif opcion == "0":
        break   
           

              
          
          
       
           
       
                  
    
    
                   
        

         
                   
        



