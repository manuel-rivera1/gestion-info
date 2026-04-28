import pandas as pd
from file import load_data


def export_to_csv():
    """z
    Exporta los registros a CSV usando pandas
    """

    try:

        data = load_data()

        if not data:
            print("No hay registros")
            return

        df = pd.DataFrame(data)

        df.to_csv("data/reporte.csv", index=False)

        print("Reporte exportado correctamente")

    except Exception as e:

        print("Error:", e)


def generate_report(*args, **kwargs):
    """
    Función simple usando *args y **kwargs
    """

    try:

        data = load_data()

        if not data:
            print("No hay datos")
            return

        df = pd.DataFrame(data)

        # FILTRAR con kwargs
        for key, value in kwargs.items():

            if key in df.columns:

                df = df[df[key] == value]

        # ORDENAR con args
        if args:

            df = df.sort_values(by=list(args))

        print(df)

    except Exception as e:

        print("Error:", e)