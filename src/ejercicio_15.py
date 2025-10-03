from data import get_dataframe

def ejercicio_15():
    df = get_dataframe().copy()

    print("Antes de modificar:")
    print(df.iloc[0:3, 3:5])

    # Modificar valores en posiciones específicas
    df.iloc[0, 3] = 99999  # salario primer empleado
    df.iloc[1:3, 4] = ['Bogotá', 'Cali']  # cambiar ciudad empleados 2 y 3

    # Modificar múltiples columnas a la vez
    df.iloc[3:5, [2,5]] = [[45, 88000], [50, 90000]]  # edad y salario

    print("Después de modificar:")
    print(df.iloc[0:5, 3:6])

if __name__ == "__main__":
    ejercicio_15()