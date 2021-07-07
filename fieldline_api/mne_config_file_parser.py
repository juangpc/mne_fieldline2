import imp
import os

def parseConfigFile(file):
    
    currentDirectory = os.getcwd()
    configFile = os.path.join(currentDirectory, file)
    config = imp.load_source(configFile)
    
    return config
