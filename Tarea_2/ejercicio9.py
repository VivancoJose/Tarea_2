#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
#  Calcula el área de un círculo de 5 de radio:

from math import pi

def area_circulo(radio):
    return pi * radio**2

area_circulo(5)