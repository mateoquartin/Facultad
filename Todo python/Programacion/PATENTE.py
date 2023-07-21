#PATENTE
from re import I


n = int(input("Patentes 0km: "))
tam = n*3
v = [None]*tam
v_reclamos = []

for i in range(0,tam,3):
    v[i]=str(input("Ingrese Nombre y Apellido: "))
    v[i]=v[i].upper()
    v[i+1]=str(input("Ingresar Dni: "))
    nums_p=v[i+1][-3:]
    e=v[i].find(" ",0,len(v[i])-1)
    E=v[i][e+1]
    L=v[i][-1:]
    patente = "R"+E+" "+nums_p+" "+L+"A"
    v[i+2]=patente 

i=2
while i<=tam-3: 
    j=i+3
    while j<=tam:
        if v[i]==v[j]:
            v_reclamos.append(v[j-2])
            v_reclamos.append(v[j-1])
            v_reclamos.append(v[j])
            for k in range(j,tam,-3):
                v[j]=v[j+3]
                v[j-1]=v[j+2]
                v[j-2]=v[j+1]
            tam=tam-3
        else:
            j=j+3
    i=i+3

for i in range (0,tam):
    print (v[i])

print (v_reclamos)