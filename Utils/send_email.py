import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import re

def send_email(df, sender_email, password, lista_destinatarios):
    """
    Envía un correo electrónico con un archivo adjunto y el contenido de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que contiene la información a incluir en el cuerpo del correo.
        sender_email (str): Dirección de correo electrónico del remitente.
        password (str): Contraseña del correo electrónico del remitente.
        lista_destinatarios (list of str): Lista de direcciones de correo electrónico de los destinatarios.

    Returns:
        None
    """
    table = df
    destino = table.iloc[0][6]
    lista_destinatarios.append(destino)
    subject = 'Summary Invoices - Batsej Open Finance S.A'
    body = f'Cordial saludo, Batsej Open Finance S.A se permite informarle el resultado de los valores totales a cobrar para los meses de julio y agosto de 2024:\n {table} \n Quedamos atentos.'    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(lista_destinatarios)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    file_path = r'Utils\Summary_Invoices\FusionWave_Enterprises\Summary.xlsx'  
    attachment = open(file_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= {os.path.basename(file_path)}',
    )

    msg.attach(part)

    attachment.close()

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls() 
        server.login(sender_email, password)

        server.sendmail(sender_email, ', '.join(lista_destinatarios), msg.as_string())

        print('Correo enviado exitosamente')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')
    finally:
        server.quit()