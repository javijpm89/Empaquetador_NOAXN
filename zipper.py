import zipfile
import os
import versioncontroller


class Zipper:

    def __init__(self,pathtozip,zipfile):
        self.path=pathtozip
        self.file = zipfile

    def zipContent(self):
        os.chdir(self.path)
        finalfile = zipfile.ZipFile(self.file,'w',zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk('.'):
            for file in files:
                self.finalfile.write(os.path.join(root, file))
                print "Adding to ZIP" + finalfile + os.path.join(root, file)
        finalfile.close()