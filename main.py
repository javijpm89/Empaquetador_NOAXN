# -*- coding: utf-8 -*-
import os
import socket
import time
from termcolor import colored

from es.telecor.virtualtraining.empaquetador.utils import Configurator
from es.telecor.virtualtraining.empaquetador.utils import zipper
from es.telecor.virtualtraining.empaquetador.utils import versioncontroller
from es.telecor.virtualtraining.empaquetador.utils import mailer

version = "0.9.6_Alpha"


def printmenu(projects):

    print "Empaquetador Python"
    print "============ ======"
    print " Proyectos No Axon "
    print " --------- -- ---- "
    print "Version -> " + version
    print "Listado de proyectos registrados"
    id_proyecto=1
    for project in projects:
        print str(id_proyecto) + ' - ' + str(project)
        id_proyecto=id_proyecto+1


def conectamail():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('vtpostman',25))
    msg = str(sock.recv(512))
    response=False
    if msg.startswith('220'):
        response = True
    sock.close()
    return response


def checkconfigparameters(config):

    projectsok = []

    print 'INFO - Cargando configuracion'
    print 'INFO - Comprobando resolucion de servidor de mail'

    if (conectamail()):
        print colored('[OK] - El servidor de correo responde','green')
    else:
        print ('[ERROR] - Fallo al conectar con el servidor de correo','red')

    print 'INFO - Comprobando directorios de todos los proyectos'

    for project in config.projects.split(','):

        path_ini = config.basePath + config.getpathproject(project)
        path_fin = config.repositoryBase + config.getrepopath(project)

        if os.path.exists(path_ini) and os.path.exists(path_fin):
            print colored('[OK] - Proyecto ' + project + ' comprobado','green')
            projectsok.append(project)
        else:
            print colored('[ERROR] - Error en el proyecto ' + project,'red')

        time.sleep(1)

    return projectsok


def main():

    # Cargamos la configuracion
    config = Configurator.Configurator()

    projectschecked = checkconfigparameters(config)

    printmenu(projectschecked)

    # Obtenemos la opcion del usuario y el proyecto que desea versionar
    idoption = int(raw_input('Introduzca Id de proyecto a versionar >> '))

    proyectoseleccionado = projectschecked[idoption-1]

    basepath = config.basePath

    pathproject = basepath + config.getpathproject(proyectoseleccionado)
    pathrepo = config.repositoryBase + config.getrepopath(proyectoseleccionado)

    today = time.strftime("%Y%m%d")

    print "[INFO] - Obteniendo versión a generar"

    vcontroller = versioncontroller.VersionController(pathproject)
    currentversion=vcontroller.getversion()

    if currentversion is None:
        print colored("[ERROR] - Error al obtener la versión del proyecto " + proyectoseleccionado, "red")
        print colored("[INFO] - Obteniendo version.xml desde la URL")
        currentversion = vcontroller.getversionfromweb()
    else:
        print colored("[OK] - Version a generar -> " + str(currentversion), "green")

    # Generamos el paquete con version y fecha
    packagename = proyectoseleccionado+'_'+today+'_'+currentversion+'.zip'
    zipgen = zipper.Zipper(pathproject, pathrepo + packagename)
    zipgen.zipcontent()

    # Aumentamos el numero de version en el fichero version.xml
    newver = vcontroller.setnewversion(currentversion)


    # Notificamos via correo que se ha generado un paquete nuevo

    mail = mailer.Mailer(config.mailserver,config.userMail,config.passMail,config.userMail,config.destMail,proyectoseleccionado,currentversion)
    rcmailer=mail.sendmail()

    if rcmailer is True:
        print colored("[OK] - Correo enviado a "+config.destMail,'green')
    else:
        print colored("[ERROR] - Fallo en el envío del correo")

    # Borramos ahora todos los ficheros y dejamos la parte de subidas limpia (a excepcion del version.xml)
    print "INFO - Borrando los ficheros ya empaquetados"
    os.system("rm -R " + pathproject +"*")

    resultupdatever = vcontroller.writenewversion(newver)

    if resultupdatever is True:
        print colored("[OK] - Nueva version " + str(newver) + " fijada en version.xml", 'green')
    else:
        print colored("[ERROR] - No se ha podido actualizar el fichero de version", 'red')

main()

