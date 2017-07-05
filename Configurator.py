from ConfigParser import SafeConfigParser


class Configurator:

    pathProject = None
    repoPath = None

    basePath = None
    repositoryBase = None

    mailserver = None
    userMail = None
    passMail = None
    destMail = None

    projects = None

    def __init__(self):

        self.configuration = SafeConfigParser()
        self.configuration.read('config.ini')

        self.projects = self.configuration.get('projects','projectList')

        # Configuracion base
        self.basePath = self.configuration.get('main_config', 'basePath')
        self.repositoryBase = self.configuration.get('main_config', 'repositoryBasePath')

        # Configuracion de mailing
        self.mailserver = self.configuration.get('mailing', 'mailserver')
        self.userMail = self.configuration.get('mailing', 'userMail')
        self.passMail = self.configuration.get('mailing', 'passMail')
        self.destMail = self.configuration.get('mailing', 'dstmail')

    @classmethod
    def getpathproject(self,project):
        return self.configuration.get(project,'path')

    @classmethod
    def getrepopath(self,project):
        return self.configuration.get(project,'repository')

    @classmethod
    def getbasepath(self):
        return self.basePath

    @classmethod
    def getrepositorybase(self):
        return self.basePath

    @classmethod
    def getserver(self):
        return self.mailserver

    @classmethod
    def getusermail(self):
        return self.userMail

    @classmethod
    def getpassmail(self):
        return self.passMail

    @classmethod
    def getdestmail(self):
        return self.destMail

    @classmethod
    def getprojects(self):
        return self.projects