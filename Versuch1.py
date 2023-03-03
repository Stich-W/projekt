

recipient_email = input("Geben Sie die E-Mail-Adresse des Empfängers ein: ")
email_text = input("Geben Sie den Text der E-Mail ein: ")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Konfigurieren Sie die SMTP-Server-Informationen für den E-Mail-Anbieter, den Sie verwenden möchten.
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"

# Erstellen Sie eine Instanz der SMTP-Klasse und stellen Sie eine Verbindung zum SMTP-Server her.
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Erstellen Sie eine MIMEText-Nachricht, die den Textinhalt der E-Mail enthält.
email_message = MIMEText("Hello, World!")

# Konfigurieren Sie die E-Mail-Header-Informationen.
email_message["From"] = "sender_email_address"
email_message["To"] = "recipient_email_address"
email_message["Subject"] = "Test Email"

# Senden Sie die E-Mail über die SMTP-Verbindung.
smtp_connection.sendmail(email_message["From"], email_message["To"], email_message.as_string())

# Schließen Sie die SMTP-Verbindung.
smtp_connection.quit()
