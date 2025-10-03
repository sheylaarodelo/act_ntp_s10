from data import get_dataframe

def ejercicio_11():
    df = get_dataframe()

    primera_fila = df.iloc[0]
    primeras_5_filas = df.iloc[:5]
    ultima_fila = df.iloc[-1]
    filas_especificas = df.iloc[[0, 3, 5, 10]]  # ejemplo

    print("Primera fila:")
    print(primera_fila)
    print("\nPrimeras 5 filas:")
    print(primeras_5_filas)
    print("\nÚltima fila:")
    print(ultima_fila)
    print("\nFilas específicas 0,3,5,10:")
    print(filas_especificas)

if __name__ == "__main__":
    ejercicio_11()