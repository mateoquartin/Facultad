#Se ingresan 5 notas de N alumnos, calcular y mostrar las dos peores notas de ellos. 
#Datos de entrada N

n = int(input("ingresar cantidad de alumnos: "))
for i in range (n):
    nombre = input("ingresar nombre: ")
    nota1 = int(input("ingresar nota:"))
    nota2 = int(input("ingresar nota:"))
    if nota1 < nota2:
        peor_nota1 = nota1
        peor_nota2 = nota2
    else:
        peor_nota1 = nota2
        peor_nota2 = nota1

    for j in range (2):
        nota = int(input("ingresar nota: "))
        if nota < peor_nota1:
            peor_nota2 = peor_nota1
            peor_nota1 = nota
        else:
            if nota < peor_nota2:
                peor_nota = nota
    print ("las peores notas de {} son {} y {}".format(nombre, peor_nota1, peor_nota2))


