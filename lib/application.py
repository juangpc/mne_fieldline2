import time
import lib.ini_file_parser
import lib.gui

class App:
    def __init__(self):
        self.exit_application = False
        self.time_step = 0.01
        self.__init_gui()

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

    def __init_gui(self):
        menu = [lib.gui.MenuItem('Exit', self.exit)]
        self.gui = lib.gui.Gui()
        self.gui_model = lib.gui.Model(menu_items=menu)
