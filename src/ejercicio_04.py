from data import get_dataframe

def ejercicio_04():
    df = get_dataframe()

    solo_nombre_salario = df.loc[:, ['nombre', 'salario']]
    rango_columnas = df.loc[:, 'nombre':'departamento']
    mayores_50_cols = df.loc[df['edad'] > 50, 'nombre':'departamento']

    print("Nombre y salario:")
    print(solo_nombre_salario.head(10))

    print("\nRango columnas nombre a departamento:")
    print(rango_columnas.head(10))

    print("\nEmpleados mayores de 50 años - nombre a departamento:")
    print(mayores_50_cols.head(10))

if __name__ == "__main__":
    ejercicio_04()