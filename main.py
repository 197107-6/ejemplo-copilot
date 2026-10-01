from soluciones.salario_semanal import calcularSalario, leerDatos, mostrarSalario

def main():
    horas, pago = leerDatos()
    salario = calcularSalario(horas, pago)
    mostrarSalario(salario)

if __name__ == "__main__":
    main()

