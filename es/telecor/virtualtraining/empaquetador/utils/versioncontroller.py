# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


class VersionController():

    def __init__(self,path):
        self.pathtoproject=path

    def getVersion(self):
        try:
            tree = ET.parse(self.pathtoproject+"version.xml")
            nodoppal = tree.getroot()
            if (nodoppal.tag == 'version'):
                return nodoppal.text
        except IOError as error:
            print error.message
            return None

    def setNewVersion(self,version):
        ver = str.split(version,'.')
        subver = int(ver[2])
        subver = subver+1
        newver = str(str(ver[0])+'.'+str(ver[1])+'.'+str(subver))
        return newver

    def writenewversion(self, newversion):

        root = ET.Element("version")
        root.text = newversion

        tree = ET.ElementTree(root)
        try:
            tree.write(self.pathtoproject+"version.xml")
            return True
        except Exception as ex:
            print ex.message
            return False
