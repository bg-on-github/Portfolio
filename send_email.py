import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user = "biprajitghoshal@gmail.com"

    pwd = 'magrrmzjlxwepnnh'
    receiver = "biprajitghoshal@gmail.com"

    contx = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=contx) as server:
        server.login(user, pwd)
        server.sendmail(user, receiver, message)
