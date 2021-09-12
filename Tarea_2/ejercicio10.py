#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

#Si el primer número es mayor que el segundo, debe devolver 1.
#Si el primer número es menor que el segundo, debe devolver -1.
#Si ambos números son iguales, debe devolver un 0.
#Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    return 0

print(relacion(5, 10), relacion(10, 5), relacion(5, 5))