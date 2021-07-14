import lib.globals as globals
import logging

log = logging.getLogger('menus')

class IncorrectInstallationMenu:
    def __init__(self):
        self.menu_list = [('Incorrect FieldLine installation. Please re-install and try again.', globals.app.exit)]

class InitialMenu:
    def __init__(self):
        self.menu_list = [('Install Fieldline api', self.func1),
                          ('Change state to Menu2', self.func2),
                          ('Exit', globals.app.exit) ]
    
    def __del__(self):
        with open('bli14.txt','w') as file_out:
            file_out.write('bybye!!!\n')

    def func1(self):
        with open('bli1.txt','w') as file_out:
            file_out.write('blablabla')
            file_out.write('\n\nfunc1 in Menu1')
    
    def func2(self):
        log.debug("Switching to Menu2")
        globals.app.set_gui_menu(Menu2())

class Menu2:
    def __init__(self):
        self.menu_list = [('func1 - Menu2', self.func1),
                          ('Switch to menu 1', self.func2),
                          ('Exit', globals.app.exit) ]

    def func1(self):
        with open('bli2.txt','w') as file_out:
            file_out.write('blobloblo')
            file_out.write('\n\nfunc1 in Menu2')
    def func2(self):
        log.debug("Switch back to menu 1")
        globals.app.switch_to_menu(InitialMenu())

