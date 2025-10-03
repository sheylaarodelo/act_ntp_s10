from data import get_dataframe

def ejercicio_16():
    df = get_dataframe()

    cada_segunda_fila = df.iloc[::2]
    filas_orden_inverso = df.iloc[::-1]
    cada_quinta_desde_3 = df.iloc[2::5]

    combinacion = df.iloc[::3, ::2]

    print("Cada segunda fila:")
    print(cada_segunda_fila.head())
    print("\nFilas en orden inverso:")
    print(filas_orden_inverso.head())
    print("\nCada quinta fila empezando en posición 3:")
    print(cada_quinta_desde_3.head())
    print("\nCombinación pasos filas y columnas:")
    print(combinacion.head())

if __name__ == "__main__":
    ejercicio_16()