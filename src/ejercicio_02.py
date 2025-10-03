from data import get_dataframe

def ejercicio_02():
    df = get_dataframe()

    mayores_40 = df.loc[df['edad'] > 40]
    it_empleados = df.loc[df['departamento'] == 'IT']
    salario_mayor_80000 = df.loc[df['salario'] > 80000]

    print(f"Empleados mayores de 40 años: {len(mayores_40)}")
    print(mayores_40)

    print(f"\nEmpleados del departamento IT: {len(it_empleados)}")
    print(it_empleados)

    print(f"\nEmpleados con salario mayor a 80,000: {len(salario_mayor_80000)}")
    print(salario_mayor_80000)

if __name__ == "__main__":
    ejercicio_02()
