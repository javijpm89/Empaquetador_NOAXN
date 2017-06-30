import versioncontroller
import zipper
import Configurator
import sys

def printMenu(projects):
    print "Empaquetador Python"
    print "============ ======"
    print " Proyectos No Axon "
    print " --------- -- ---- "
    print "Listado de proyectos registrados"
    id_proyecto=1
    for project in projects:
        print str(id_proyecto) + str(project)
        id_proyecto=id_proyecto+1



def main():

    config = Configurator.Configurator()
    projects = config.getprojects()
    printMenu(projects)


main()


