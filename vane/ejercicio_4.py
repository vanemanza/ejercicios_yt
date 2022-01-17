"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

def vocal(x):
    return x  in 'aeiou'

test1 = vocal('a')
test2 = vocal('f')
test3 = vocal('o')

print(test1)
print(test2)
print(test3)