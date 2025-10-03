from data import get_dataframe
from datetime import datetime, timedelta
import pandas as pd


def ejercicio_07():
    df = get_dataframe()
    df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])

    # Filtrar empleados que ingresaron en 2022
    ingresaron_2022 = df.loc[df['fecha_ingreso'].dt.year == 2022]

    # Filtrar empleados que ingresaron en últimos 2 años (desde hoy)
    fecha_limite = datetime.now() - timedelta(days=365*2)
    ingresaron_ult_2_anios = df.loc[df['fecha_ingreso'] >= fecha_limite]

    # Filtrar empleados que ingresaron en primer trimestre
    primer_trimestre = df.loc[df['fecha_ingreso'].dt.month.isin([1, 2, 3])]

    # Calcular antigüedad promedio
    def antiguedad_promedio(grupo):
        return (datetime.now() - grupo['fecha_ingreso']).dt.days.mean() / 365

    print("Empleados que ingresaron en 2022:")
    print(ingresaron_2022.describe())
    print("Antigüedad promedio:", antiguedad_promedio(ingresaron_2022))

    print("\nEmpleados que ingresaron en últimos 2 años:")
    print(ingresaron_ult_2_anios.describe())
    print("Antigüedad promedio:", antiguedad_promedio(ingresaron_ult_2_anios))

    print("\nEmpleados que ingresaron en primer trimestre:")
    print(primer_trimestre.describe())
    print("Antigüedad promedio:", antiguedad_promedio(primer_trimestre))


if __name__ == "__main__":
    ejercicio_07()