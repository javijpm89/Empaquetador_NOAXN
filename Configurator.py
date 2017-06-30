from ConfigParser import SafeConfigParser


class Configurator:

    pathProject = None
    repoPath = None

    basePath = None
    repositoryBase = None

    server = None
    userMail = None
    passMail = None
    destMail = None

    def __init__(self,project):

        configuration = SafeConfigParser()
        configuration.read('config.ini')

        self.pathProject = self.configuration.get(project,'path')
        self.repoPath = self.configuration.get(project,'repository')

        # Configuracion base
        self.basePath = configuration.get('main_config', 'basePath')
        self.repositoryBase = configuration.get('main_config', 'repositoryBasePath')

        # Configuracion de mailing
        self.server = configuration.get('mailing', 'mailserver')
        self.userMail = configuration.get('mailing', 'userMail')
        self.passMail = configuration.get('mailing', 'passMail')
        self.destMail = configuration.get('mailing', 'dstmail')

    @classmethod
    def getpathproject(self):
        return self.pathProject

    @classmethod
    def getrepopath(self):
        return self.repoPath

    @classmethod
    def getbasepath(self):
        return self.basePath

    @classmethod
    def getrepositorybase(self):
        return self.basePath

    @classmethod
    def getserver(self):
        return self.server

    @classmethod
    def getusermail(self):
        return self.userMail

    @classmethod
    def getpassmail(self):
        return self.passMail

    @classmethod
    def getdestmail(self):
        return self.destMail