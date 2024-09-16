def calculations(cursor, commerce, selected_month, selected_year, iva, table_name):
    """
    Ejecuta una consulta SQL basada en un archivo de reglas de negocio y devuelve el resultado.

    Args:
        cursor: Objeto de cursor de base de datos que permite ejecutar la consulta SQL.
        commerce (str): Nombre del comercio para determinar el archivo de reglas de negocio a utilizar.
        selected_month (int): Mes seleccionado para la consulta.
        selected_year (int): Año seleccionado para la consulta.
        iva (float): Valor del IVA a ser utilizado en la consulta.
        table_name (str): Nombre de la tabla que será formateado en la consulta SQL.

    Returns:
        ResultSet: El resultado de la ejecución de la consulta SQL.

    """
    with open(f'sql_files/business_rules/{commerce}.sql', 'r') as business_rule:
        query = business_rule.read()
    query = query.format(table_name)
    result = cursor.execute(query, (iva, selected_month, selected_year))
    return result
