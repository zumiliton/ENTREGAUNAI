import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(mensaje,destinatario,asunto):
    try:
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587
        usuario_smtp = 'sanburger92@gmail.com'
        contraseña_smtp = 'ffov vkdg iasw fild'

        mensaje_correo = MIMEMultipart()
        mensaje_correo['From'] = usuario_smtp
        mensaje_correo['To'] = 'tate14651@gmail.com'
        mensaje_correo['Subject'] = asunto

        mensaje_correo.attach(MIMEText(mensaje, 'plain'))

        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()

            servidor.login(usuario_smtp, contraseña_smtp)

            servidor.sendmail(usuario_smtp, destinatario, mensaje_correo.as_string())
        return True
    except Exception as e:
        print(str(e))
        return False


