# -*- coding: utf-8 -*-
import zipfile
import os


class Zipper:
    def __init__(self, pathtozip, zipfile):
        self.path = pathtozip
        self.file = zipfile

    def zipContent(self):
        print "[INFO] - Obteniendo ficheros a comprimir " + self.path
        os.chdir(self.path)
        finalfile = zipfile.ZipFile(self.file, 'w', zipfile.ZIP_DEFLATED)
        print "[INFO] - Comprimiendo directorios"
        try:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    finalfile.write(os.path.join(root, file))
                    #print "Adding to ZIP" + str(finalfile.filename) + os.path.join(root, file)
        except Exception, exc:
            print "Fallo al generar el fichero " + self.file + "%s" % str(exc)
        finally:
            finalfile.close()

        try:
            print "INFO - Generando fichero MD5 de comprobación"
            md5ofzip = str(os.popen("md5sum " + finalfile.filename + " | awk {'print $1'}").read())
            md5zipfile = open(finalfile.filename + '.md5', 'w')
            md5zipfile.write(md5ofzip)
        except Exception, exc:
            print "Error al generar el fichero md5 " + "%s" % str(exc)
        finally:
            md5zipfile.close()

