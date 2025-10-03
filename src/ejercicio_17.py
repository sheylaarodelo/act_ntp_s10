from data import get_dataframe
import numpy as np

def ejercicio_17():
    df = get_dataframe()

    subconjunto = df.iloc[5:15]
    bool_array = np.array([True if x % 2 == 0 else False for x in range(len(df))])
    seleccion_bool = df.iloc[bool_array]

    vista_agregada = subconjunto[['salario', 'edad']].mean()

    print("Subconjunto filas 5 a 14:")
    print(subconjunto)
    print("\nSelección con array booleano filtrando incluso filas:")
    print(seleccion_bool.head())
    print("\nMedia salario y edad en subconjunto:")
    print(vista_agregada)

if __name__ == "__main__":
    ejercicio_17()