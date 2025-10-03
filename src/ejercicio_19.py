from data import get_dataframe
import numpy as np
import pandas as pd

def ejercicio_19():
    df = get_dataframe()

    vista_1 = df.iloc[:10]
    vista_2 = df.iloc[-10:]
    vista_3 = df.iloc[np.random.choice(df.index.size, 5, replace=False)]

    sistematica = df.iloc[::5]

    mezcla = pd.concat([vista_3, sistematica])

    print("Vista 1 (primeras 10 filas):")
    print(vista_1)
    print("\nVista 2 (últimas 10 filas):")
    print(vista_2)
    print("\nVista 3 (5 filas aleatorias):")
    print(vista_3)
    print("\nSistema (cada 5 filas):")
    print(sistematica)
    print("\nMezcla de muestras:")
    print(mezcla)

if __name__ == "__main__":
    ejercicio_19()