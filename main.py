import versioncontroller
import zipper
from ConfigParser import SafeConfigParser


configuration = SafeConfigParser()
configuration.read('config.ini')

base = configuration.get('main_config','pathBase')
finalbasedir=configuration.get('main_config','repositoryBasePath')

project = configuration.get('houseon_public_web','path')
finalprojectdir = configuration.get('houseon_public_web','repositoryHouseOnWeb')


