# -*- coding: utf-8 -*-

"""
Created on Sun Feb 20 12:19:28 2024

Escuela Politécnica Nacional
@author: Damian Hernandez
Topic: Proyecto App para calcular conductores eléctricos
"""

#Librerías

import numpy as np
# Define la tabla.
matriz = np.array([
    [507, 1000],
    [456, 900],
    [380, 750],
    [304, 600],
    [279, 550],
    [253, 500],
    [228, 450],
    [203, 400],
    [177, 350],
    [152, 300],
    [127, 250],
    [107.2,6],
    [85, 8],
    [67.4, 8],
    [53.4, 0],
    [42.4, 1],
    [33.6, 2],
    [26.7, 3],
    [21.2, 4],
    [16.8, 5],
    [13.3, 6],
    [10.6, 7],
    [8.34, 8],
    [6.62, 9],
    [5.26, 10],
    [4.15, 11],
    [3.31, 12],
    [2.63, 12],
    [2.08, 14],
    [1.65, 15],
    [1.31, 16],
    [1.04, 17],
    [0.8230, 18],
    [0.6530, 19],
    [0.519, 20],
    [0.412, 21],
    [0.3240, 22],
    [0.2590, 23],
    [0.2050, 24],
    [0.1630, 25],
    [0.1280, 26],
    [0.1020, 27],
    [0.0804, 28],
    [0.0646, 29],
    [0.0503, 30],
    [0.04, 31],
    [0.0320, 32], 
    [0.0252, 33],
    [0.020, 34],
    [0.0161, 35],
    [0.0123, 36],
    [0.010, 37],
    [0.00795, 38],
    [0.00632, 39]  
])
#variables 
redondeo : int
inominal : float
seccion : float 
calibre : int()
R : float
AV: float 
V: float 
L : float 
Rm: float
m : int

p_cobre: float = 0.01724
p_alum: float  =  0.028
#librerías


#Código principal
##Entrada de datos
print("Bienvenido Estimado usuario")

def suma():
    numero_valido1 = False
    while not numero_valido1:
        try:
            inominal = float(input("Introduce la corriente en amperios: "))
            numero_valido1 = True
        except ValueError:
            print("El valor ingresado no es un número.")
    
    print(f"Corriente : {inominal}")
    
    numero_valido2 = False
    while not numero_valido2:
        try:
            AV = float(input("Introduce la pérdida máxima de tensión en voltios: "))
            numero_valido2 = True
        except ValueError:
            print("El valor ingresado no es un número.")
    
    print(f" Pérdida máxima es: {AV}")
    
    
    numero_valido3 = False
    while not numero_valido3:
        try:
            V = float(input("Introduce la tensión nominal en voltios: "))
            numero_valido3 = True
        except ValueError:
            print("El valor ingresado no es un número.")
    
    print(f"tensión nominal: {V}")
    
    numero_valido4 = False
    while not numero_valido4:
        try:
            L = float(input("Introduce la longitud en metros: "))
            numero_valido4 = True
        except ValueError:
            print("El valor ingresado no es un número.")
    
    print(f"Longitud: {L}")
    
    """
    print(f" el valor de la corriente es  {inominal} amperios")
    print(f" pérdida de tensión máxima  {AV} ")
    print(f" el valor de la corriente es  {L} metros " )
    print(f" el valor de la corriente es  {V} voltios")
    """
    numero_valido = False
    while not numero_valido:
        try:
            numero = int(input("Ingrese un número (0 ó 1), 0 si es cobre ó 1 si es aluminio: "))
            if numero not in (0, 1):
                raise ValueError
            numero_valido = True
        except ValueError:
            print("El valor ingresado debe ser 0 o 1.")
    
    print(f"El número ingresado es: {numero}")
    
    m= numero
    print(m)
    
    #m = float(input("Si el material es cobre pon 0, si es aluminio pon 1: "))
    # Solicita un valor al usuario
    #Calculos
    ##resitencia total del condcutor
    R = AV/inominal
    ##reistencia por metro
    Rm = R/L
    ## sección
    a = None
    if m == 1:
     seccion = (p_cobre*L*inominal)/(V*Rm)
     redondeo = round(seccion, 3)
     a = redondeo
     print(f"La sección del conductor es:  {redondeo} milimetros cuadrados")
    elif m == 0:
        seccion = (p_alum*L*inominal)/(V*Rm)
        redondeo = round(seccion, 3)
        a = redondeo
        print(f"La sección del conductor es:  {redondeo} milimetros cuadrados")
    def extraer_x(array):
        return [coord[0] for coord in array]

    # Ejemplo de uso

    array_x = extraer_x(matriz)
    



    def buscar_valor(lista, valor):
        if valor in lista:
            return valor, None
        else:
            lista.append(valor)
            lista.sort()
            indice = lista.index(valor)
            if indice == 0:
                return None, lista[indice + 1]
            elif indice == len(lista) - 1:
                return lista[indice - 1], None
            else:
                return lista[indice + 1], lista[indice - 1]

    # Ejemplo de uso:

    x1, x2 = buscar_valor(array_x, a)
    print("Valor inferiro:", x1)
    print("Valor superior:", x2)

    def buscar_imprimir_pareja(pares, valor_x):
        for x, y in pares:
            if x == valor_x:
                print(f"Para el valor de inferior {valor_x}: ({x}, calibre AWG {y})")
                return
            elif y == valor_x:
                print(f"Para el valor superiror {valor_x}: ({y}, cakibre AWG {x})")
                return
       

    # Ejemplo de uso:




    if x2 is None:
        buscar_imprimir_pareja(matriz, x1)
        
    else:
        buscar_imprimir_pareja(matriz, x1)
        buscar_imprimir_pareja(matriz, x2)











while True:
  respuesta = input("¿Desea realizar un cálculo ? (si/no): ")

  # Si la respuesta es "s", realizar otra suma
  if respuesta.lower() == "si":
    suma()

  # Si la respuesta es "n", salir del bucle
  elif respuesta.lower() == "no":
    break
  # Si la respuesta no es válida, mostrar un mensaje de error
  else:
    print("Respuesta no válida. Introduzca 'si' o 'no'.")
