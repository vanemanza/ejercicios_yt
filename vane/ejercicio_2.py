"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def maximo(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


test1 = max(200,34,5)
test2 = max(-200,34,5)
test3 = max(5,6,89)

print(test1)
print(test2)
print(test3)