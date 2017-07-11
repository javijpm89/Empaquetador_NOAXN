#!/home/javi/Util/anaconda/bin/python
import os
import Configurator
import socket
from termcolor import colored


def printMenu(projects):
    print "Empaquetador Python"
    print "============ ======"
    print " Proyectos No Axon "
    print " --------- -- ---- "
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

        pathIni = config.basePath + config.getpathproject(project)
        pathFin = config.repositoryBase + config.getrepopath(project)

        if (os.path.exists(pathIni) and os.path.exists(pathFin)):
            print colored('[OK] - Proyecto ' + project + ' comprobado','green')
            projectsok.append(project)
        else:
            print colored('[ERROR] - Error en el proyecto ' + project,'red')

    return projectsok


def main():

    # Sacamos toda la configuracion
    config = Configurator.Configurator()

    projectschecked = checkconfigparameters(config)

    printMenu(projectschecked)

    # Obtenemos la opcion del usuario y el proyecto que desea versionar
    idoption = int(raw_input('Introduzca Id de proyecto a versionar >> '))

    proyectoseleccionado = projectschecked[idoption-1]

    print proyectoseleccionado


main()

