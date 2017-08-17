# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import ssl
import urllib2
import xmltodict


class VersionController():

    def __init__(self,path):
        self.pathtoproject=path

    def getversion(self):
        try:
            tree = ET.parse(self.pathtoproject+"version.xml")
            nodoppal = tree.getroot()
            if nodoppal.tag == 'version':
                return nodoppal.text
        except IOError as error:
            print error.message
            return None

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

    def setnewversion(self, version):

        ver = str.split(version,'.')
        subver3 = int(ver[2])
        subver2 = int(ver[1])
        subver1 = int(ver[0])

        if subver3 == 999:
            if subver2 == 999:
                subver1 = subver1 + 1
                subver2 = 0
                subver3 = 0
            subver2 = subver2 + 1
            subver3 = 0

        subver3 = subver3 + 1
        newver = str(str(subver1) + '.' + str(subver2) + '.' + str(subver3))
        return newver

    def getversionfromweb(self,url):

        context = ssl._create_unverified_context(ssl.PROTOCOL_TLSv1)

        file = urllib2.urlopen(url+'/version.xml', context=context)
        data = file.read()
        file.close()

        data = xmltodict.parse(data)

        return data['version']