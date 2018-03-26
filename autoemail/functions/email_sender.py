import smtplib
from email.mime.text import MIMEText

__all__ = (
    'Email_Sender',
)




class Email_Sender():

    def send(self, email_id, password, recipients, subject, message):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_id, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['To'] = ", ".join(recipients)
        smtp.sendmail(email_id, recipients, msg.as_string())
        smtp.quit()
