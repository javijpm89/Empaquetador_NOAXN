# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import sys


class Mailer:

    def __init__(self, server,usermail,password,mailfrom,mailto,project,version):

        self.server=server
        self.usermail=usermail
        self.password=password
        self.mailfrom=mailfrom
        self.mailto=mailto
        self.project=project
        self.version=version

    def sendmail(self):
        try:
            print "INFO - Preparando correo"

            conection = smtplib.SMTP(self.server, 25)
            conection.set_debuglevel(False)
            conection.login(self.usermail,self.password)

            message = MIMEText("Se ha generado la version " + self.version + " del proyecto " + self.project)
            message['Subject'] = "Notificacion de nueva version de " + self.project
            message['From'] = self.mailfrom
            message['To'] = self.mailto

            try:
                conection.sendmail(self.mailfrom,self.mailto,message.as_string())
                return True
            except Exception as e:
                print e.message
                return False
            finally:
                conection.close()
        except Exception, exc:
            print ("Fallo al enviar el correo %s" % str(exc))
            return False
