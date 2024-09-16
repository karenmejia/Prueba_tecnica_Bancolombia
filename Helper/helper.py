import sqlite3
import pandas as pd

class Helper:
    """
    Clase para interactuar con una base de datos SQLite.

    Atributos:
        path (str): Ruta al archivo de la base de datos SQLite.

    Métodos:
        __init__(): Conecta a la base de datos SQLite.
        read(table_name): Lee datos de una tabla y los devuelve como DataFrame de pandas.
        cursor(): Devuelve un objeto cursor para ejecutar comandos SQL.
        connection(): Devuelve el objeto de conexión a SQLite.
        create_table(table_name, fields): Crea una nueva tabla en la base de datos.
        drop_table(table_name): Elimina la tabla especificada.
        data_insert(df, table_name, fields): Inserta datos de un DataFrame en la tabla.
    """

    path = 'Helper\BD\database.sqlite'

    def __init__(self):
        """
        Inicializa la clase y conecta a la base de datos.
        """
        self.conexion = sqlite3.connect(self.path)

    def read(self, table_name):
        """
        Lee todos los datos de la tabla especificada.

        Args:
            table_name (str): Nombre de la tabla.

        Returns:
            pandas.DataFrame: Datos de la tabla.
        """
        query_data = f"SELECT * FROM {table_name};"
        return pd.read_sql_query(query_data, self.conexion)

    def cursor(self):
        """
        Devuelve un cursor para ejecutar comandos SQL.

        Returns:
            sqlite3.Cursor: Objeto cursor.
        """
        return self.conexion.cursor()

    def connection(self):
        """
        Devuelve el objeto de conexión a SQLite.

        Returns:
            sqlite3.Connection: Objeto de conexión.
        """
        return self.conexion

    def create_table(self, table_name, fields):
        """
        Crea una nueva tabla si no existe.

        Args:
            table_name (str): Nombre de la tabla.
            fields (str): Campos y tipos de datos.
        """
        self.conexion.cursor().execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({fields})')
        print(f'Tabla "{table_name}" creada correctamente')

    def drop_table(self, table_name):
        """
        Elimina la tabla especificada si existe.

        Args:
            table_name (str): Nombre de la tabla.
        """
        self.conexion.cursor().execute(f'DROP TABLE IF EXISTS {table_name}')
        print(f'Tabla "{table_name}" borrada correctamente')

    def data_insert(self, df, table_name, fields):
        """
        Inserta datos de un DataFrame en la tabla especificada.

        Args:
            df (pandas.DataFrame): Datos a insertar.
            table_name (str): Nombre de la tabla.
            fields (str): Campos en la tabla.
        """
        df = df.fillna(999999)
        for _, row in df.iterrows():
            values = tuple(row)
            self.conexion.cursor().execute(f'INSERT INTO {table_name} {fields} VALUES {values}')
            self.conexion.cursor().fetchall()
            self.conexion.commit()
