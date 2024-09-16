import pandas as pd

def generate_df(conexion, table_name):
    """
    Genera un DataFrame a partir de una consulta SQL ejecutada en una conexión de base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos utilizado para ejecutar la consulta SQL.
        table_name (str): Nombre de la tabla que será formateado en la consulta SQL.

    Returns:
        pd.DataFrame: DataFrame que contiene los resultados de la consulta SQL.
    """
    with open(f'sql_files/results_table/final_df.sql', 'r') as final_df:
        query = final_df.read()
    query = query.format(table_name)
    result = pd.read_sql_query(query, conexion)

    return result
