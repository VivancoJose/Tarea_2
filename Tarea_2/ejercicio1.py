# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

numero_1 =float (input (" Ingrese el primmer numero : \n"))
numero_2 =float (input (" Ingres el segundo numero : \n"))

print(" ¿Qué quieres hacer? \n, 1.sumar los dos numeros \n, 2.restar los dos numemros \n, 3.mostrar una multiplicacion de los numeros \n")
#            0                        1                              2                               3
numero_3 =float (input (" introduzca una opcion : \n"))

if numero_3 == 1:
    print(f"La suma de", numero_1, "+" ,numero_2, "es", numero_1 + numero_2)
elif  numero_3 == 2:
    print(f"La resta de",numero_1, "-" ,numero_2, "es", numero_1 - numero_2)
elif  numero_3 == 3:
    print(f"El producto de",numero_1, "*" ,numero_2, "es", numero_1 * numero_2)
else:
    print("La opcion elegida es incorrecta")

