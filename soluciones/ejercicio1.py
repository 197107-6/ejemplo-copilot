'''
PANTEAMIENTO DEL PROBLEMA

Calcular la raiz cuadrada de math.sqrt(b-a**2)/c.
doble
'''

# PROBLEMA: Calcular la raiz cuadrada de math.sqrt(b-a**2)/c.
# ENTRADAS: a, b, c
# SALIDA: raiz_cuadrada
# ALGORITMO
# 1. Leer a, b, c
# 2. Calcular raiz cuadrada
# 3. Mostrar resultado

#CONTARTO DE FUNCIONES
#leerDatos()
#Entrada: ninguna
#Salida: a, b, c
#Responsabilidad: pedir 
#datos al usuario

#calcularRaizCuadrada(a, b, c)
#Entrada: a, b, c
#Salida: raiz_cuadrada
#Responsabilidad: 
#Calcular, no imprimir

#mostrarRaizCuadrada(raiz_cuadrada)
#Entrada: raiz_cuadrada
#Salida: ninguna
#Responsabilidad: 
#mostrar resultado

#CASOS DE PRUEBA
# Caso 1: a = 2, b = 20, c = 5
#Entrada: 2, 20, 5
#Salida: 2.8284271247461903
#
# Caso 2: a = 3, b = 30, c = 6
#Entrada: 3, 30, 6
#Salida: 3.4641016151377544
#
# Caso 3: a = 4, b = 40, c = 7
#Entrada: 4, 40, 7
#Salida: 4.0
#
#Restricciones:
#- no imprimir dentro de la función calcularRaizCuadrada
#- devolver el resultado
#- no usar bibliotecas externas
#- no usar variables globales
#- no realices llamadas a funciones dentro de este archivo
def leerDatos1():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c

def calcularRaizCuadrada(a, b, c):
    return (b - a**2) / c

def mostrarRaizCuadrada(raiz_cuadrada):
    print("La raíz cuadrada es:", raiz_cuadrada)