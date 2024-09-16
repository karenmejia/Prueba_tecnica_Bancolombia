import pandas as pd

def generate_excel(df, commerce):
    """
    Exporta un DataFrame a un archivo Excel en una ruta específica.

    Args:
        df (pd.DataFrame): El DataFrame que se exportará a un archivo Excel.
        commerce (str): Nombre del comercio, utilizado para definir el directorio en el que se guardará el archivo.

    Returns:
        None
    """
    df.to_excel(f'Utils/Summary_Invoices/{commerce}/Summary.xlsx', index=False)
