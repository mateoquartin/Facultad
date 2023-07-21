### Loops ###

#While

my_condicion = 0


while my_condicion < 10:
    print(my_condicion)
    my_condicion += 1
if my_condicion == 10:
    print("mi condicion es igual a 10")
else:
    print("mi condicion es mayor a 10")

print("ya salio del bucle")
print(my_condicion)

while my_condicion < 20:
    my_condicion += 1
    if my_condicion == 15:
        print ("la condicion vale 15")
        break
    print(my_condicion)

#For 
my_list = [35, 50, 10, 63, 15, 74]
for element in my_list:
    print(element)

