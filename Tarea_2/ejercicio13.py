# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
#  La primera con los números pares, y la segunda con los números impares:

numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(*args):
    lista = sorted(args)
    pares = []
    impares = []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares

pares, impares = separar(*numeros)
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]