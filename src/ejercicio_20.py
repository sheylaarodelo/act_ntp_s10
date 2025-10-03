from data import get_dataframe
import numpy as np
import pandas as pd

def ejercicio_20():
    df = get_dataframe()

    vistas = {
        'primeras_10': df.iloc[:10],
        'ultimas_10': df.iloc[-10:],
        'pares': df.iloc[::2],
        'terceras': df.iloc[::3]
    }

    aleatorias = df.iloc[np.random.choice(df.index.size, 10, replace=False)]

    print("Resumen muestras por vista:")
    for key, vista in vistas.items():
        print(f"\n{key}:")
        print(vista.describe())

    print("\nMuestra aleatoria (10 filas):")
    print(aleatorias.describe())

if __name__ == "__main__":
    ejercicio_20()