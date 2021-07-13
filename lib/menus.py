

class IncorrectInstallationMenu:
    def __init__(self, app):
        self.menu_list = [('Incorrect FieldLine install. Please re-install and try again.', app.exit)]
        self.app = app

class InitialMenu:
    def __init__(self):
        self.menu_list = [('Install Fieldline api', self.func1),
                          ('Change state to Menu2', self.func2),
                          ('Exit', self.app.exit) ]
    
    def __del__(self):
        with open('bli14.txt','a') as file_out:
            file_out.write('bybye!!!\n')

    def func1(self):
        with open('bli1.txt','w') as file_out:
            file_out.write('blablabla')
            file_out.write('\n\nfunc1 in Menu1')
    
    def func2(self):
        self.app.set_gui_menu(Menu2(self.app)) 

class Menu2:
    def __init__(self):
        self.menu_list = [('func1 - Menu2', self.func1),
                          ('Exit', self.app.exit) ]

    def func1(self):
        with open('bli2.txt','w') as file_out:
            file_out.write('blobloblo')
            file_out.write('\n\nfunc1 in Menu2')
