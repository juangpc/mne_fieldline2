import configparser
import ast

class Parser_Output:
    def __str__(self):
        out_str = ""
        for section in vars(self).items():
            out_str += "\n" + section[0] + ":" + str(section[1]) + "\n"
        return out_str
     
class Parser_Section:
    def __str__(self):
        out_str = ""
        for opt in vars(self).items():
            out_str += "\n\t" + opt[0] + " = " + str(opt[1])
        return out_str
class Parser:
    def __init__(self, config_file = None):
        self.parser = configparser.ConfigParser()
        if config_file is not None:
            self.config_file = config_file

    def set_file(self, config_file):
        self.config_file = config_file

    def read(self, config_file = None):
        if config_file is not None:
            self.config_file = config_file
            self.read()
        elif self.config_file is not None:
            self.parser.read(self.config_file)
        return self.__parse_config_file()
    
    def parse(self):
        return self.read()

    def __parse_config_file(self):
        self.config = Parser_Output()
        for section in self.parser.sections():
            sect = Parser_Section()
            for option in self.parser.options(section):
                setattr(sect, option, ast.literal_eval(self.parser[section][option]))
            setattr(self.config, section, sect)
            # for option in self.parser.options(section):
            #     delattr(sect, option)
        return self.config


def parse_file(file):
    parser = Parser(file)
    return parser.read()