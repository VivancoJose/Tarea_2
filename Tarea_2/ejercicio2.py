#Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar,
# debe repetise el proceso hasta que lo introduzca correctamente.

numero_1= 0
while numero_1 % 2 == 0:
    numero_1 =  int(input(" Ingrese un numero impar: \n") )

print("El numemro ue ha introducido es correcto")