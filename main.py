from soluciones.salario_semanal import calcularSalario, leerDatos, mostrarSalario
from soluciones.ejercicio1 import calcularRaizCuadrada, leerDatos1, mostrarRaizCuadrada
from soluciones.ejercicio2 import calcularFactorial, leerDatos2, mostrarFactorial

def main():
  while True:
    print("menu")
    print("1. Calcular salario semanal")
    print("2: Raíz cuadrada de (b-a**2)/c")
    print("3. n factorial")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
      horas, pago = leerDatos()
      salario = calcularSalario(horas, pago)
      mostrarSalario(salario)
    elif opcion == "2":
      a, b, c = leerDatos1()
      raiz_cuadrada = calcularRaizCuadrada(a, b, c)
      mostrarRaizCuadrada(raiz_cuadrada)
    elif opcion == "3":
      n = leerDatos2()
      factorial = calcularFactorial(n)
      mostrarFactorial(factorial)
    elif opcion == "4":
      break
    else:
      print("Opción no válida")

if __name__ == "__main__":
    main()

