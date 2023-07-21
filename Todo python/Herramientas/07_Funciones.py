### funciones ###

def my_funcion():
    print("esto es una funcion")

my_funcion()

def sum_two_values(first_numer, second_numer):
    suma = first_numer + second_numer
    print (suma)

sum_two_values(5,6) #es necesario darle siempre los parametros que pide la funcion 
sum_two_values ("5","7")
sum_two_values (6.4, 4.5)

def sum_two_values_with_return(first_numer , second_numer):
    my_sum = first_numer + second_numer
    return my_sum


my_result = sum_two_values (6.4, 4.5) #Como no tiene ningun "return" dentro de la funcion printea None
print(my_result)

my_result = sum_two_values_with_return(4,5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Quartin",name =  "Mateo") #siempre agarra el valor que tiene la funcion indicada no importa el nombre (si no pones el valor, los agarra en orden)

def sum_two_values_with_default (name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

sum_two_values_with_default ("Mateo","Quartin" )
sum_two_values_with_default ("Mateo","Quartin", "Cachete" )

def print_texts(*text):
    print(text)

print_texts("hola","python", "mateo")

def print_texts(*texts):
    for text  in texts:
        print(text.upper())

print_texts("hola","python", "mateo")

