from data import get_dataframe

def ejercicio_12():
    df = get_dataframe()

    filas_10_a_20 = df.iloc[10:21]
    ultimas_10_filas = df.iloc[-10:]
    filas_pares = df.iloc[::2]
    cada_tercera = df.iloc[::3]

    print("Filas del 10 al 20:")
    print(filas_10_a_20)
    print("\nÚltimas 10 filas:")
    print(ultimas_10_filas)
    print("\nFilas pares:")
    print(filas_pares)
    print("\nCada tercera fila:")
    print(cada_tercera)

if __name__ == "__main__":
    ejercicio_12()