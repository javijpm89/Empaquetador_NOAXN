import smtplib
from email.mime.text import MIMEText


class Mailer:

    def __init__(self,server,password,mailfrom,mailto,project,version):
        self.server=server
        self.password=password
        self.mailfrom=mailfrom
        self.mailto=mailto
        self.project=project
        self.version=version


    def sendmail(self):

        message="Se ha generado la version " + self.version + "del proyecto" + self.project
        message['Subject'] = "Notificacion de nueva versión de " + self.project
        message['From'] = self.mailfrom
        message['To'] = self.mailto

        sender = smtplib.SMTP(self.server)
        sender.sendmail(self.mailfrom,self.mailto,message)
        sender.close()
