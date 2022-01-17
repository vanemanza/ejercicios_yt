"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
 Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generador(n, caracter):
    return caracter * n 

test1 = generador(5, 'x')
test2 = generador(2, 'pe')
test3 = generador(1, 'a c')
test4 = generador(2, 'k')
test5 = generador(1, 'c k')


print(test1)
print(test2)
print(test3)
print(test4)
print(test5)