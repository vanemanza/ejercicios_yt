"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en 
común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    return [True for x in lista1  for y in lista2 if x == y] 
   
l1 = ['a', 'b', 'c']
  
l2 = ['d', 'b', 'e'] 

test = superposicion(l1, l2)
print(test)

'Chau todo muy lendo pero me voy a cocinar :('