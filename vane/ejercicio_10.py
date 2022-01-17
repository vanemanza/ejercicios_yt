"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la 
pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******
"""

def procedimiento(lista):

    lista = [ ('*' * x ) for x in lista]
    for elem in lista:
        print(elem)
    

procedimiento([4, 9, 7])    
