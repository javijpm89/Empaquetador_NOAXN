import versioncontroller
import zipper
import Configurator
import sys
from mailer import Mailer

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



def main():


    mail = Mailer.Mailer()


    config = Configurator.Configurator()
    projects = config.projects.split('\n')
    print projects
    printMenu(projects)

    raw_input('Introduzca Id de proyecto a versionar >> ')
    print projects


main()


