import imp
import os

def parse_config_file(file):
    
    current_directory = os.getcwd()
    config_file = os.path.join(current_directory, file)
    config = imp.load_source(config_file)
    
    return config
