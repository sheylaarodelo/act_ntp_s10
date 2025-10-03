from data import get_dataframe

def ejercicio_05():
    df = get_dataframe().copy()
    
    print("Antes de cambios IT salario:")
    print(df.loc[df['departamento']=='IT', 'salario'].head())

    # Aumentar salario 10% a IT
    df.loc[df['departamento']=='IT', 'salario'] *= 1.1

    # Cambiar estado a inactivo para mayores de 60
    df.loc[df['edad'] > 60, 'activo'] = False

    # Actualizar ciudad a Bogotá para RRHH
    df.loc[df['departamento']=='RRHH', 'ciudad'] = 'Bogotá'

    print("Después de cambios IT salario:")
    print(df.loc[df['departamento']=='IT', 'salario'].head())
    print("\nEmpleados mayores de 60 (estado actualizado):")
    print(df.loc[df['edad']>60, ['edad', 'activo']])
    print("\nEmpleados RRHH con ciudad actualizada:")
    print(df.loc[df['departamento']=='RRHH', ['departamento', 'ciudad']])

if __name__ == "__main__":
    ejercicio_05()
