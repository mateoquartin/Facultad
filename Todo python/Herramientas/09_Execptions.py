### exceptions ###

numeroUno = 5
numeroDos = 2
numeroDos = "2"

#numeroDos = "2"
# Siempre si hay un try hay un except
# try except
try:
    print (numeroUno + numeroDos)
except:
    # Se ejecuta si se produce una exepción
    print ("se a procucido un error")


# try except else
try:
    print (numeroUno + numeroDos)
except:
    print ("se a procucido un error")
else: # Opcional 
    # Se ejecuta si no se produce una exepción 
    print ("la ejecucion continua correctamente")
finally: # Opcional 
    # Se ejecuta siempre 
    print("la ejecucion continua")

# Excepciones por tipo 

try:
    print (numeroUno + numeroDos)
    print ("No se a producido un error")
except ValueError:
    print ("se a procucido un ValueError")
except TypeError:
    print ("se a procucido un TypeError")

# Captura de la informacion de la excepcion

try:
    print (numeroUno + numeroDos)
    print ("No se a producido un error")
except ValueError as error: #error es el nombre de una variable que contiene la informacion de la excepcion
    print (error)
except Exception as exception: # En el caso de que no sea ValueError se ejecuta siempre pasa a Exception
    print (exception)



