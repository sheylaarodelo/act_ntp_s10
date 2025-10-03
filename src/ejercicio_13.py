from data import get_dataframe
import numpy as np
import pandas as pd


def ejercicio_13():
    df = get_dataframe()

    posiciones = [0, 5, 10, 15]
    filas_seleccionadas = df.iloc[posiciones]

    np.random.seed(42)
    filas_aleatorias = df.iloc[np.random.choice(df.index.size, 5, replace=False)]

    combinadas = pd.concat([filas_seleccionadas, filas_aleatorias])

    print("Filas seleccionadas por posiciones específicas:")
    print(filas_seleccionadas)
    print("\nFilas aleatorias:")
    print(filas_aleatorias)
    print("\nCombinación de ambas:")
    print(combinadas)

    print("Estadísticas de filas seleccionadas:")
    print(combinadas.describe())

if __name__ == "__main__":
    ejercicio_13()