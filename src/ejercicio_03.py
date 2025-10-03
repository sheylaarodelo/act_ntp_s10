from data import get_dataframe

def ejercicio_03():
    df = get_dataframe()

    it_salario_alto = df.loc[(df['departamento'] == 'IT') & (df['salario'] > 70000)]
    ventas_marketing = df.loc[df['departamento'].isin(['Ventas', 'Marketing'])]
    activos_experiencia = df.loc[(df['activo'] == True) & (df['experiencia_años'] > 5)]

    print("Empleados IT con salario mayor a 70000:")
    print(it_salario_alto.describe())

    print("\nEmpleados de Ventas o Marketing:")
    print(ventas_marketing.describe())

    print("\nEmpleados activos con más de 5 años de experiencia:")
    print(activos_experiencia.describe())

if __name__ == "__main__":
    ejercicio_03()