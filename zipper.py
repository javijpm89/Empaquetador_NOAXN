import zipfile
import os


class Zipper:

    def __init__(self, pathtozip, zipfile):
        self.path=pathtozip
        self.file = zipfile

    def zipContent(self):
        os.chdir(self.path)
        finalfile = zipfile.ZipFile(self.file, 'w', zipfile.ZIP_DEFLATED)
        try:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    self.finalfile.write(os.path.join(root, file))
                    print "Adding to ZIP" + finalfile + os.path.join(root, file)
        except Exception, exc:
            print "Fallo al generar el fichero " + self.file + "%s" %str(exc)
        finally:
            finalfile.close()