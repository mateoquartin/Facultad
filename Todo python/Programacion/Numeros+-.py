a = int(input("ingresar un numero A: "))
b = int(input("ingresar un numero B: "))
c = int(input("ingresar un numero C: "))
vec = [a, b, c]
if a < b and b < c:
    print ("los numeros estan ordenados de menor a mayor ")
if a > b and b > c:
    print("los numeros estan ordenados de mayor a menor ")
else:
    print ("los numeros no estan ordenados de ninguna manera")
print (vec)
