from data import get_dataframe
import numpy as np

def ejercicio_18():
    df = get_dataframe()

    # Posiciones con salario mayor a 90000
    pos_may_salario = df.index[df['salario'] > 90000].tolist()

    # Uso percentiles para seleccionar filas
    percentil_90 = df['salario'].quantile(0.90)
    filas_percentil = df.loc[df['salario'] >= percentil_90]

    # Listas dinámicas de índices
    seleccion_dinamica = df.iloc[pos_may_salario]

    print("Posiciones con salario mayor a 90000:")
    print(pos_may_salario)
    print("\nFilas en percentil 90 o superior salario:")
    print(filas_percentil)
    print("\nSeleccion dinámica basada en posiciones mayores a 90000:")
    print(seleccion_dinamica)

if __name__ == "__main__":
    ejercicio_18()