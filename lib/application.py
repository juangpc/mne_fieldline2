import time
import lib.ini_file_parser
import lib.gui

class App:
    def __init__(self, config_file = None):
        self.exit_application = False
        self.time_step = 0.01
        self.config_file = config_file
        self.__setup_gui()

    def __del__(self):
        pass

    def start(self):
        self.__loop()

    def exit(self):
        self.gui.exit_loop()
        self.exit_application = True

    def __loop(self):
        while not self.exit_application:
            self.gui.update(self.gui_model)
            time.sleep(self.time_step)

    def __setup_gui(self):
        menus = ['Connect to Fieldline', 
                 'Restart Fieldline Sensors', 
                 'Start sending Fieldline data',
                 'Exit']
        callbacks = [self.add1_to_second, 
                     self.add1_to_third,
                     self.add1_to_fourth,
                     self.exit]
        self.gui = lib.gui.Gui()
        self.gui_model = lib.gui.Model(menu_items=menus, callback_list=callbacks)
        
    def add1_to_second(self):
        self.gui_model.menu_items[1] = self.gui_model.menu_items[1] + "bla"
    
    def add1_to_third(self):
        self.gui_model.menu_items[2] = self.gui_model.menu_items[2] + "bla"
    
    def add1_to_fourth(self):
        self.gui_model.menu_items[3] = self.gui_model.menu_items[3] + "bla"
