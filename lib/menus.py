import logging

log = logging.getLogger('menus')

__global_app = None

def global_app(*vargs):
    global __global_app
    if len(vargs) == 0:
        return __global_app
    else:
        __global_app = vargs[0]

def global_exit():
    global __global_app
    return __global_app.exit

class BaseMenu:
    def switch_to_menu(new_menu):
        global_app().set_gui_menu(new_menu)

class IncorrectInstallationMenu:
    def __init__(self):
        self.menu_list = [('Incorrect FieldLine installation. Please re-install and try again.', global_exit())]


class InitialMenu(BaseMenu):
    def __init__(self):
        self.menu_list = [('Install Fieldline api', self.func1),
                          ('Change state to Menu2', self.func2),
                          ('Exit', global_exit()) ]
    
    def __del__(self):
        with open('bli14.txt','w') as file_out:
            file_out.write('bybye!!!\n')

    def func1(self):
        with open('bli1.txt','w') as file_out:
            file_out.write('blablabla')
            file_out.write('\n\nfunc1 in Menu1')
    
    def func2(self):
        log.debug("Switching to Menu2")
        self.switch_to_menu(Menu2())

class Menu2(BaseMenu):
    def __init__(self, app = []):
        self.app = app
        self.menu_list = [('func1 - Menu2', self.func1),
                          ('Switch to menu 1', self.func2),
                          ('Exit', global_exit()) ]

    def func1(self):
        with open('bli2.txt','w') as file_out:
            file_out.write('blobloblo')
            file_out.write('\n\nfunc1 in Menu2')
    def func2(self):
        log.debug("Switch back to menu 1")
        self.switch_to_menu(InitialMenu())