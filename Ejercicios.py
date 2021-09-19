#Ejercicio1: Verificar notas
#rango : 0 a 5 = perdiste el año
#rango : 6 a 7 = supletorio
#rango : 8  = bueno
#rango : 9 = muy bueno
#rango : 10 = sobresaliente

"""""nota_final = float (input ("Ingresa la nota de tu examen:"))

if nota_final >= 0 and nota_final <= 5:
    print("Perdiste de año")
elif nota_final >= 6 and nota_final <= 7:
    print("Te vas a supletorio")
elif nota_final == 8:
    print("Bueno")
elif nota_final == 9:
    print("Muy bueno")
elif nota_final == 10:
    print("Sobresaliente")
else :
    print("La opcion enviada no existe.")

##Ejercicio2: para determinar si un numero  es par o impar 
#pedirle al usuario el ingreso de un numero por teclado
#verificar si el numero ingresado es par o impar y presentar el mensaje en pantalla 
#operadores de comparacion : MOD, resto.

Programa_1 = int (input ("Ingrese un numero : \n"))
if Programa_1 % 2 == 0:
    print(f"el numero {Programa_1} es par ")
else:
    print(f"el numero {Programa_1} es impar ")



print("----------------------while-------------------------")
contador = 0
while contador < 7: 
    contador += 1
    if contador == 3:
        continue
    print(contador)"""


#ejercicio poo

from typing import Sized


print("---------------Ejercicio de programacion orientada a objetos--------------------")

class rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcula_area (self):
        return self.base * self.altura

salir = True
while (salir):

    base = float(input("Ingrese el valor de la base : \n"))
    altura= float(input("Ingrese el valor de la altura : \n"))

#primera instancia del rectangulo
rectangulo_1 = rectangulo(base, altura)
area_rectangulo = rectangulo_1.calcula_area()
print(f"el area del rectangulo de {base} *{altura} = {area_rectangulo}  ")

print("Quiere seguir calculando: \n")
print ("1. Si") 
print ("2. No") 
opcion = float(input("eloga la opcion : \n"))
if opcion == 2:
    salir = False
else: 
    base = float(input("Ingrese el valor de la base : \n"))
    altura= float(input("Ingrese el valor de la altura : \n"))
