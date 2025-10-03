from data import get_dataframe

def ejercicio_09():
    df = get_dataframe()

    filtro_1 = df.loc[(df['activo']) &
                      (df['departamento'].isin(['IT', 'Finanzas'])) &
                      (df['salario'] > 60000) &
                      (df['edad'] < 45)]

    ciudades_especificas = ['Bogotá', 'Medellín']
    filtro_2 = df.loc[(df['ciudad'].isin(ciudades_especificas)) &
                      (df['experiencia_años'] > 10)]

    print("Filtro empleados activos, IT o Finanzas, salario>60000, edad<45:")
    print(filtro_1.describe())

    print("\nFiltro empleados de ciudades específicas con experiencia > 10 años:")
    print(filtro_2.describe())

if __name__ == "__main__":
    ejercicio_09()