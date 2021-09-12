#Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
suma = 0
numero = int(input("¿Cuántos números quieres introducir? \n ") )
for i in range(numero):
    suma += float(input("Introduce un número: ") )
print("Se han introducido",numero,"números que en total han sumado",suma,"y la media es",suma/numero)