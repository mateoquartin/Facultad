n=int(input("ingresar cantidad de relevamientos: "))
infra=[None]*(n*3)
rank=[]
for i in range(0,n*3,3):
    infra[i]=str(input("Ingrese patente: "))
    infra[i+1]=str(input("Ingrese DNI: "))
    code=str(input("Ingrese el tipo de infraccion: "))
    code=code.upper()
    infra[i+2]=code
x="ALCO"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
x="REVE"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
x="SEGU"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
x="CINTU"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
x="CEL"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
x="CEDU"
c=0
B=False
for i  in range(2,n*3,3):
    if x==infra[i]:
        c=c+1
        B=True
if B:
    rank.append(x)
    rank.append(c)
for i in range(1,len(rank)-2,2):
    for j in range(i+2,len(rank),2):
        if rank[i]<rank[j]:
            aux=rank[i]
            rank[i]=rank[j]
            rank[j]=aux
            aux1=rank[i-1]
            rank[i-1]=rank[j-1]
            rank[j-1]=aux1
print("COdigo de infraccion y sus repeticiones ordenadas de menor a mayor: ")
print(rank)