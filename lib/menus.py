import logging

log = logging.getLogger('menus')

__exit_fcn = None

def global_exit(*vargs):
    global __exit_fcn
    if len(vargs) == 0:
        return __exit_fcn
    else:
        __exit_fcn = vargs[0]

class IncorrectInstallationMenu:
    def __init__(self, app = []):
        self.app = app
        self.menu_list = [('Incorrect FieldLine installation. Please re-install and try again.', global_exit())]

class InitialMenu:
    def __init__(self, app = []):
        self.app = app
        self.menu_list = [('Install Fieldline api', self.func1),
                          ('Change state to Menu2', self.func2),
                          ('Exit', global_exit()) ]
    
    def __del__(self):
        with open('bli14.txt','a') as file_out:
            file_out.write('bybye!!!\n')

    def func1(self):
        with open('bli1.txt','w') as file_out:
            file_out.write('blablabla')
            file_out.write('\n\nfunc1 in Menu1')
    
    def func2(self):
        self.app.set_gui_menu(Menu2()) 

class Menu2:
    def __init__(self, app = []):
        self.app = app
        self.menu_list = [('func1 - Menu2', self.func1),
                          ('Exit', global_exit()) ]

    def func1(self):
        with open('bli2.txt','w') as file_out:
            file_out.write('blobloblo')
            file_out.write('\n\nfunc1 in Menu2')
