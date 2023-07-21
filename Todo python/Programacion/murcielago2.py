codigo = ["M", "U", "R", "C", "I", "E", "L", "A", "G", "O"]
n = int(input("ingrese la cantidad de expositores: "))
tam = n * 4
v = [None] * (tam)
for k in range(0, 2*n, 2):
    v[k] = input("ingrese el Apellido en mayúsculas: ").upper()
    v[k+1] = input("ingrese el DN1: ")

print("Vector de Expositores: ", v)
k = 0
while k <= (tam - 4):
    usuario = v[k] + v[k+1][-2:]
    #generamos contraseña
    contraseña = ""
    for letra in v[k]:
        if letra in codigo:
            contraseña = contraseña + str(codigo.index(letra))
        else:
            contraseña = contraseña + letra
    contraseña = contraseña + str(v.index(v[k])//2)
    #insertamos usuario
    for i in range(tam-1, k+2, -1):
        v[i] = v[i-1]
    v[k+2] = usuario
    #insertamos contraseña
    for i in range(tam-1, k+3, -1):
        v[i] = v[i-1]
    v[k+3] = contraseña
    k = k + 4

print(v)