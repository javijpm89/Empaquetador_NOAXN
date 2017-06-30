import xml.etree.ElementTree as ET


class VersionController():

    def __init__(self,path):
        self.pathtoproject=path

    def getVersion(self):
        tree = ET.parse(self.pathtoproject+"version.xml")
        nodoppal = tree.getroot()
        if (nodoppal.tag == 'version'):
            return nodoppal.text


    def setNewVersion(self,version):
        ver = str.split(version,'.')
        subver = int(ver[2])
        subver = subver+1
        newver = str(str(ver[0])+'.'+str(ver[1])+'.'+str(subver))
        return newver

    def updateVersionValue(self,newversion):
        tree = ET.parse(self.pathtoproject+"version.xml")
        node = tree.getroot()
        if (node.tag == 'version'):
            node.text = newversion
            try:
                tree.write(self.pathtoproject+"version.xml",'UTF-8')
                return True
            except:
                print "Error al escribir la nueva version"
                return False
