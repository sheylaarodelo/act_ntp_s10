from data import get_dataframe

def ejercicio_01():
    df = get_dataframe()

    empleado_10 = df.loc[10]
    empleados_lista = df.loc[[1, 2, 30, 50]]
    empleados_rango = df.loc[20:30]

    print("Empleado con ID 10:")
    print(empleado_10)
    print("\nEmpleados con IDs 1, 2, 30, 50:")
    print(empleados_lista)
    print("\nEmpleados con IDs del 20 al 30:")
    print(empleados_rango)

if __name__ == "__main__":
    ejercicio_01()