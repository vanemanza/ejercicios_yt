"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo 
aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def palindromo(string):
    return string == string[::-1]

test1 = palindromo('radar')
test2 = palindromo('vanesa')
test3 = palindromo('neuquen')

print(test1)
print(test2)
print(test3)