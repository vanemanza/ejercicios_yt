import numpy as np

"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los 
números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería 
devolver 24.
"""

def suma(*args):
    return sum(*args)

test = suma([1,2,3,4])    
print(test)


def multiplicar(*args):
    return np.prod(*args)

test2 = multiplicar([1,2,3,4]) 
print(test2)
