# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import os


class Configurator:

    configuration = None

    pathProject = None
    repoPath = None

    basePath = None
    repositoryBase = None
    url = None

    mailserver = None
    userMail = None
    passMail = None
    destMail = None

    projects = None

    def __init__(self):

        currentPath = os.getcwd()
        self.configuration = SafeConfigParser()
        self.configuration.read(currentPath + '/es/telecor/virtualtraining/empaquetador/config/' + 'config.ini')

        self.projects = self.configuration.get('projects','projectList')

        # Configuracion base
        self.basePath = self.configuration.get('main_config', 'basePath')
        self.repositoryBase = self.configuration.get('main_config', 'repositoryBasePath')

        # Configuracion de mailing
        self.mailserver = self.configuration.get('mailing', 'mailserver')
        self.userMail = self.configuration.get('mailing', 'userMail')
        self.passMail = self.configuration.get('mailing', 'passMail')
        self.destMail = self.configuration.get('mailing', 'dstmail')

    def getpathproject(self,project):
        return self.configuration.get(project,'path')

    def getrepopath(self,project):
        return self.configuration.get(project,'repository')

    def geturl(self,project):
        return self.configuration.get(project,'url')

    def getbasepath(self):
        return self.basePath

    def getrepositorybase(self):
        return self.basePath

    def getserver(self):
        return self.mailserver

    def getusermail(self):
        return self.userMail

    def getpassmail(self):
        return self.passMail

    def getdestmail(self):
        return self.destMail

    def getprojects(self):
        return self.projects