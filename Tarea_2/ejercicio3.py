#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
numero = 0
suma = 0
while numero <= 100:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)

