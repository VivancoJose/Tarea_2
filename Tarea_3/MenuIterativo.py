# Crear un programa que muestre un Menú Interactivo
# con los siguientes ejercicios:

from math import pi, trunc
from os import system, name

def MenuPrincipal():
    """Clase que nos presenta el menu principal

    Returns:
        op = devuelve la opcion seleccionada
    """

    print('''
           Menu Iterativo: 
          1. F. Escribir Centrado()
          2. F.Es Multiplo
          3. F.Temperatura Media
          4. F.Convertir espaciado
          5. F.Calcular Maximo y Minimo
          6. F.Calcular area y permitro de una Circunferencia
          7. F.Login
          8. F.Factorial de un numero
          9. F.Calcular MCD
          10.F. Calculo de segundos y horas
          11.F. Dia Juliano
          12.F.\Validar Fecha
          13.F. Fracciones
          14. F.SALIR
          ''')
    op = input("Por favor digite su opcion: \n ")
    return op


def MenuHoras():
    print(".:Calcularsegundos y horas:.")
    print(" 1. Horas a segundos")
    print(" 2. Segundos a horas")
    print(" X. Retornar Menu Principal")
    opcion = input("Seleccione su opcion: ")
    return opcion

def borrarPantalla():
    if name == "posix":
        system ("clear")
    elif ((name == "ce" or name == "nt") or name == "dos"):
        system ("cls")


# Ejercicio 01
def EscribirCentrado():
    cadena = input("Por favor digite la cadena: \n ")
    columnas = 80
    aux = (columnas - len(cadena)) // 2
    espacios = " " * aux
    print(espacios+cadena)

# Ejercicio 02
def EsMultiplo():
    try:
        num1 = int(input("Por favor digite el numero 1: "))
        num2 = int(input("Por favor digite el numero 2: "))
        if num1 % num2 == 0:
            print(f"El numero {num1} es multiplo de {num2}")
        else:
            print(f"El numero {num1} NO es multiplo de {num2}")
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

# Ejercicio 03
def TemperaturaMedia():
    try:
        num_dias = int(input("Por favor digite el numero de dias a ingresar: "))
        tem_max = 0
        tem_min = 1000
        tem_aux = 0
        for cont in range(1, num_dias+1):
            tem_aux = int(input(f"Temperatura dia {cont}: "))
            tem_max = max(tem_max, tem_aux)
            tem_min = min(tem_min, tem_aux)
        print(f"La temperatura maxima es: {tem_max}")
        print(f"La temperatura minima es: {tem_min}")
        print(f"La temperatura media es: {(tem_max + tem_min) / 2}")
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

# Ejercicio 04
def ConvertirEspaciado():
    cadena = input("Por favor digite la cadena: ")
    print("Cadena Inicial: \n", cadena)
    print("Resultado de la Cadena: \n", " ".join(cadena))

# Ejercicio 05
def CalcularMaxMin(lista_num):
    num_max = 0
    num_min = 1000
    for i,dato in enumerate(lista_num):
        num_max = max(num_max, dato)
        num_min = min(num_min, dato)
    print(f"La lista es: {lista_num}")
    print(f"El valor maximo es: {num_max}")    
    print(f"El valor minimo es: {num_min}")    

# Ejercicio 06
def areaPerimetroCircunferencia():
    try:
        radio = float(input("Por favor digite el radio de la circunferencia: "))
        areaC = (radio ** 2) * pi
        periC = radio * 2 * pi
        print(f"El area es: {round(areaC,4)}")
        print(f"El permitero es: {round(periC,4)}")
    except Exception as e:
        print("El valor no ingresado no es valido")

# Ejercicio 07
def Login():
    usuario = "usuario1"
    clave = "asdasd"
    intento=1
    while intento <= 3:
        usr_aux = input("Digitar el usuario: ")
        pas_aux = input("Digitar la clave: ")
        if (usuario == usr_aux and clave == pas_aux):
            print("Acceso correcto!!")
            return
        else:
            print("Credenciales incorrectas, intente de nuevo!!")
            intento += 1
    if intento > 3:
        print("Ha superado los intentos permitidos, Adios")
    

# Ejercicio 08
def Factorial():
    try:
        num = int(input("Digite el número a calcular: "))
        aux = 1
        for factor in range(1, num+1):
            aux = factor * aux
        print(f"El factorial de {num} es:", aux)
    except Exception as e:
        print("El valor ingresado es erroneo") 

#Ejercicio 09
def Mcd():
    try:
        num_may = int(input("Digite el número mayor: "))
        num_men = int(input("Digite el número menor: "))
        resto = 0
        if num_men > num_may:
            num_men, num_may = num_may, num_men
        while num_may % num_men != 0:
            num_men, num_may = num_may % num_men, num_men
        print(f"El MCD es: {num_men}") 
    except Exception as e:
        print("El valor ingresado es erroneo") 

#Ejercicio 10
def TiempoSegundos():
    try:
        hora = int(input("Ingrese las horas: "))
        min = int(input("Ingrese los minutos: "))
        seg = int(input("Ingrese los segundos: "))
        seg01 = seg + (min *60) + (hora*3600)
        print(f"Los valores ingresados (hh:mm:ss): {hora}:{min}:{seg} dan {seg01} segundos")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")

def SegundosTiempo():
    try:
        segs = int(input("Ingrese los segundos: "))
        auxseg = 0
        if segs >= 3600:
            horas = segs // 3600
            auxseg = segs % 3600
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 60 and segs < 3600):
            horas = 0
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 0 and segs < 60):
            horas = 0
            mins = 0
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{segs}")
        else:
            print("Valores ingresados erroneos")
    except Exception as e:
        print("Los valores ingresados no son admitidos..")
    
#Ejercicio 11

#Ejercicio 12
def AnioBisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
        return False
    elif anio % 4 == 0 and anio % 100 != 0: 
        return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
        return True


def ValidaFecha(dd,mm,aa):
    lista_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if AnioBisiesto(aa):
        lista_mes[1] = 29
        
    if len(str(aa))==4:
        if mm in range(1,12):
            if (dd > 0 and dd <= lista_mes[mm-1]):
                return True
    else:
        return False  

# Contenido generla del menu 
activo = True
while activo:
    devuelve = MenuPrincipal()
    print("\n")
    if devuelve == "1":
        borrarPantalla()
        print(".:Escribir Centrado:.")
        EscribirCentrado()
    elif devuelve == "2":
        borrarPantalla()
        print(".:Validar Multiplo:.")
        EsMultiplo()
    elif devuelve == "3":
        borrarPantalla()
        print(".:Temperatura Media:.")
        TemperaturaMedia()
    elif devuelve == "4":
        borrarPantalla()
        print(".:Convertir espaciado:.")
        ConvertirEspaciado()
    elif devuelve == "5":
        borrarPantalla()
        print(".:Calcular Maximo y Minimo:.")
        num = input("Digite los valores numéricos de la lista, separada por , (coma): ")
        lista_valores = list(map(int, num.split(',')))
        CalcularMaxMin(lista_valores)
    elif devuelve == "6":
        borrarPantalla()
        print(".:Calcular Area y Perimetro de la Circunferencia:.")
        areaPerimetroCircunferencia()
    elif devuelve == "7":
        borrarPantalla()
        print(".:Validacion de credenciales:.")
        Login()
    elif devuelve == "8":
        borrarPantalla()
        print(".:Calcular el factorial de un numero:.")
        Factorial()
    elif devuelve == "9":
        borrarPantalla()
        print(".:Calcular el MCD de 2 numeros:.")
        Mcd()
    elif devuelve == "10":
        borrarPantalla()
        while True:
            op10=MenuHoras()
            if op10 == "1":
                print(".::Horas a Segundos::.")
                TiempoSegundos()
            elif op10 == "2":
                print(".::Segundos a Horas::.")
                SegundosTiempo()
            elif (op10 == "X" or op10 == "x"):
                borrarPantalla()
                break   
    elif devuelve == "11":
        pass
    elif devuelve == "12":
        borrarPantalla()
        try:
            print(".:Valida Fecha:.")
            yy = int(input("Digite el año: "))
            mm= int(input("Digite el mes: "))
            dd = int(input("Digite el dia: "))
            if ValidaFecha(dd,mm,yy):
                print(f"La fecha ingresada es correcta: {dd}/{mm}/{yy}")
            else:
                print(f"La fecha ingresada no es correcta: {dd}/{mm}/{yy}")
        except Exception as e:
            print("Los valores ingresados no son admitidos..")
    elif devuelve == "13":
        pass   
    elif devuelve == 14:
        borrarPantalla()
        activo = False
    else:
        print("Envie una opcion que este en el rango de los literales dados")
