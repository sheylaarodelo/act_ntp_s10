from data import get_dataframe

def ejercicio_14():
    df = get_dataframe()

    primeras_3_cols = df.iloc[:, :3]
    cols_especificas = df.iloc[:, [0, 2, 4]]
    ultima_columna = df.iloc[:, -1]
    filas_columnas_combinadas = df.iloc[5:10, 1:4]

    print("Primeras 3 columnas:")
    print(primeras_3_cols.head())
    print("\nColumnas específicas 0, 2, 4:")
    print(cols_especificas.head())
    print("\nÚltima columna:")
    print(ultima_columna.head())
    print("\nFilas 5 a 9, columnas 1 a 3:")
    print(filas_columnas_combinadas)

if __name__ == "__main__":
    ejercicio_14()