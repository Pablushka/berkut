import smtplib  # simple mail transfer protocol
import ssl  # secure socket layer

# MIME is Multipurpose Internet Mail Extensions
from email.mime.text import MIMEText
# MIMEMultipart is a container for MIME messages
from email.mime.multipart import MIMEMultipart
from config import settings


def send_registration_email(receiver: str, name: str, qr: str, token: str, user_id: int):

    sender_email = "pablo@nomades.com.ar"
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["Subject"] = "Bievenido a Berkut"

    text = "Por favor abra este email en un software de correo que soporte HTML"
    html = f"""\
    <html>
      <body>
        <p>Hola {name}</p>
        <p>Gracias por su registración</p>
        <p>Por favor siga las instrucciones para completar su registro</p>
        
        <h1>Paso 1</h1>
        <p>Escanee el código qr con la app de autenticación de su celular. Si no posee ninguna, aquí recomendamos alguna: </p>
        <p> <a href="https://keeweb.info/">KeeWeb</a> </p>
        <p> <a href="https://freeotp.github.io/">freeOTP</a> </p>
        <img src="data:image/png;base64, {qr}" alt="QR Code" width="300" height="300">
        <p>Su token secreto es: {token}</p>
        <h3>MANTENGALO SEGURO</h3>
        
        <h1>Paso 2</h1>
        <p>Popr favor siga el siguiente link e ingrese el código generado por su app de autentication.</p>
        <p> <a href="http://localhost:5000/users/verify/{user_id}"> Click aquí </a> </p>
      </body>
    </html>
    """

    print("Enviando email a " + html)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.fastmail.com", 465, context=context) as server:
        server.login("pablo@nomades.com.ar",
                     (settings["SMTP_MAIL_PASSWORD"] or ""))
        server.sendmail(
            sender_email, receiver, message.as_string()
        )

    message = None
