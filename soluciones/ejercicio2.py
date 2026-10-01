'''
PANTEAMIENTO DEL PROBLEMA

Calcular n! = math.sqrt(2 * math.pi) * math.e**(-n) * n**(n + 1/2)
'''

# PROBLEMA: Calcular n!
# ENTRADAS: n
# SALIDA: factorial
# ALGORITMO
# 1. Leer n
# 2. Calcular factorial
# 3. Mostrar resultado

#CONTARTO DE FUNCIONES
#leerDatos()
#Entrada: ninguna
#Salida: n
#Responsabilidad: pedir 
#datos al usuario

#calcularFactorial(n)
#Entrada: n
#Salida: factorial
#Responsabilidad: 
#Calcular, no imprimir

#mostrarFactorial(factorial)
#Entrada: factorial
#Salida: ninguna
#Responsabilidad: 
#mostrar resultado

#CASOS DE PRUEBA
# Caso 1: n = 5
#Entrada: 5
#Salida: 118.019168
# Caso 2: n = 3
#Entrada: 3
#Salida: 10.88888888888889
#
# Caso 3: n = 4
#Entrada: 4
#Salida: 24.0
#
#Restricciones:
#- no imprimir dentro de la función calcularFactorial
#- devolver el resultado
#- no usar bibliotecas externas
#- no usar variables globales
#- no realices llamadas a funciones dentro de este archivo
def leerDatos2():
    n = int(input("Ingrese el valor de n: "))
    return n

def calcularFactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        
    return factorial

def mostrarFactorial(factorial):
    print("El factorial es:", factorial)