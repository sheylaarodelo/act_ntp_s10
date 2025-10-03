from data import get_dataframe
import pandas as pd

def ejercicio_10():
    df = get_dataframe()

    # Vistas
    activos = df.loc[df['activo']]
    nuevos = df.loc[df['fecha_ingreso'] > pd.Timestamp.now() - pd.DateOffset(years=1)]
    altos_salarios = df.loc[df['salario'] > df['salario'].quantile(0.9)]

    # Métricas
    por_departamento = df.groupby('departamento').agg({
        'salario': ['mean', 'max', 'min'],
        'edad': ['mean', 'max', 'min'],
        'empleado_id': 'count'
    })

    por_ciudad = df.groupby('ciudad').agg({
        'salario': ['mean', 'max', 'min'],
        'edad': ['mean', 'max', 'min'],
        'empleado_id': 'count'
    })

    # Top performers ejemplo (salario + experiencia)
    df['score'] = df['salario'] / df['salario'].max() + df['experiencia_años'] / df['experiencia_años'].max()
    top_performers = df.nlargest(10, 'score')

    print("Métricas por departamento:")
    print(por_departamento)

    print("\nMétricas por ciudad:")
    print(por_ciudad)

    print("\nTop performers:")
    print(top_performers[['nombre', 'departamento', 'salario', 'experiencia_años', 'score']])

if __name__ == "__main__":
    ejercicio_10()