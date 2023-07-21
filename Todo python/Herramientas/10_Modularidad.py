

import Module #no se puede importar cosas que tengan numeros como primer caracters
Module.sum (5, 6, 7)
Module.printValue("MATEO QUARTIN")

from Module import printValue, sum # importa la funcion directamente 
Module.sum (5, 6, 7)
Module.printValue("MATEO QUARTIN")

import math #se importan todas las funciones de matematica (ejemplo )

print (math.pi)
print (math.pow(2,5))

from math import pi as pi_value # valor de pi renombrado

print (pi_value)