from data import get_dataframe
import pandas as pd

def clasificar_salario(salario):
    if salario < 50000:
        return 'bajo'
    elif salario < 90000:
        return 'medio'
    else:
        return 'alto'

def ejercicio_08():
    df = get_dataframe().copy()
    df['categoria_salario'] = df['salario'].apply(clasificar_salario)

    promedio_salario = df['salario'].mean()
    filtrar_superior_promedio = df.loc[df['salario'] > promedio_salario]

    percentil_75 = df['salario'].quantile(0.75)
    filtrar_percentil_75 = df.loc[df['salario'] >= percentil_75]

    print("Distribución categorías salario:")
    print(df['categoria_salario'].value_counts())

    print("\nEmpleados con salario superior al promedio:")
    print(filtrar_superior_promedio.describe())

    print("\nEmpleados en percentil 75 o superior:")
    print(filtrar_percentil_75.describe())

if __name__ == "__main__":
    ejercicio_08()