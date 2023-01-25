import os
import smtplib
import ssl


def send_email(message):
    username = f"{os.getenv('USERNAME')}@gmail.com"
    password = os.getenv("PASSWORD")
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    receiver = username

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)

        server.sendmail(username, receiver, message)
