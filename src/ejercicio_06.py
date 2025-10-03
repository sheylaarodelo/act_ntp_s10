from data import get_dataframe

def ejercicio_06():
    df = get_dataframe()

    nombre_contiene_1 = df.loc[df['nombre'].str.contains('1')]
    apellido_termina_5 = df.loc[df['apellido'].str.endswith('5')]
    ciudad_empieza_B = df.loc[df['ciudad'].str.startswith('B')]

    print("Empleados cuyo nombre contiene '1':")
    print(nombre_contiene_1.describe())

    print("\nEmpleados cuyo apellido termina con '5':")
    print(apellido_termina_5.describe())

    print("\nEmpleados de ciudades que empiezan con 'B':")
    print(ciudad_empieza_B.describe())

if __name__ == "__main__":
    ejercicio_06()