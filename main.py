from Helper.helper import Helper
from Utils.commission_calculation import calculations
from Utils.generate_df import generate_df
from Utils.generate_excel import generate_excel
from Utils.send_email import send_email

def main():
    """
    Este script principal gestiona el flujo de cálculo de comisiones, generación de informes y envío de correos electrónicos.

    1. **Inicialización:** Se establece una conexión con la base de datos y se define el comercio.
    2. **Cálculo y Generación de Datos:**
       - Solicita al usuario el mes y el año para el cálculo de comisiones.
       - Ejecuta la función `calculations` para procesar los datos de comisiones.
       - Genera un DataFrame con la función `generate_df`.
       - Crea y carga datos en la tabla de la base de datos utilizando la función `helper`.
    3. **Exportación a Excel:** Exporta los datos a un archivo Excel con la función `generate_excel`.
    4. **Ingreso de Destinatarios:** Solicita al usuario los destinatarios adicionales para el correo electrónico.
    5. **Envío de Correo Electrónico:** Envía un correo electrónico con el archivo Excel adjunto utilizando la función `send_email`, además
    de poner el dataframe en el cuerpo del correo.

    Returns:
        None
    """
    helper = Helper() # Se instancia el helper
    cursor = helper.cursor() # Se crea objeto cursor
    conexion = helper.connection() # Se crea objeto conexion
    commerce = 'FusionWave_Enterprises' # Recibe el nombre del negocio al cual se le desea enviar la información
    answer = 1
    helper.drop_table('commission_table')

    while answer == 1:
        selected_month = input('Ingrese el mes con formato MM (ejemplo -> agosto -> 08): ')
        selected_year = input('Ingrese el mes con formato YYYY (ejemplo -> 2024): ')
        iva = 1.19
        table_name = commerce+'_' + selected_year + selected_month
        fields = ('Fecha_Mes', 'Nombre', 'Nit', 'Valor_comision', 'Valor_iva', 'Valor_Total', 'Correo')
        calculations(cursor, commerce, selected_month, selected_year, iva, table_name)
        final_df = generate_df(conexion, table_name)

        helper.create_table('commission_table', 'Fecha_Mes INT, Nombre VARCHAR(255), Nit BIGINT, Valor_comision BIGINT, Valor_iva INT, Valor_Total BIGINT, Correo VARCHAR(255)')
        helper.data_insert(final_df, 'commission_table', fields)
        answer = int(input('¿Desea ingresar otra fecha?, escriba 1 si desea ingresar otra fecha o 0 si desea generar los resultados: '))

    df_to_excel = helper.read('commission_table')
    generate_excel(df_to_excel, commerce)

    destinatario_adicional = []     

    option = int(input('¿Desea ingresar un destinario adicional?, escriba 1 para "SI" o 0 para "NO": '))
    if option == 1:
        while option == 1:
            nuevo_email = input('Ingrese el destinatario adicional: ')
            destinatario_adicional.append(nuevo_email)
            option = int(input('¿Desea ingresar un destinario adicional?, escriba 1 para "SI" o 0 para "NO": '))

    if final_df.empty:
        print('El comercio se encuentra inactivo')
    else:
        sender_email = input('Ingrese el email de origen de Outlook: ')
        password = input('Ingrese la contraseña: ')
        send_email(df_to_excel, sender_email, password, destinatario_adicional)

main()