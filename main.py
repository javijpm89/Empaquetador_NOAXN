import versioncontroller
import zipper
import Configurator
import sys
import mailer
import os



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


def checkconfigparameters(config):

    projectstatus = {}

    print 'INFO - Cargando configuracion'
    print 'INFO - Comprobando resolucion de servidor de mail'
    resulmailserver = os.system("telnet "+config.mailserver + " ; echo $?")
    if (resulmailserver == 0):
        print '[OK] - Resolucion de nombre correcta'
    else:
        print '[ERROR] - Resolucion incorrecta'

    print 'INFO - Comprobando directorios de todos los proyectos'

    for project in config.projects.split(','):
        projectstatus='KO'
        pathIni = config.basePath + config.getpathproject(project)
        pathFin = config.repositoryBase + config.getrepopath(project)

        if (os.path.exists(pathIni) and os.path.exists(pathFin)):
            print '[OK] - Proyecto ' + project + ' comprobado'
            projectstatus = 'OK'
        else:
            print '[ERROR] - Error en el proyecto ' + project
            projectstatus = 'KO'

        projectstatus.update({project:projectstatus})

    return projectstatus


def main():

    # Sacamos toda la configuracion
    config = Configurator.Configurator()
    projects = config.projects.split(',')
    printMenu(projects)

    # Obtenemos la opcion del usuario y el proyecto que desea versionar
    idoption = raw_input('Introduzca Id de proyecto a versionar >> ')

    proyectoseleccionado = projects[idoption-1]


main()


