import time
import threading
import lib.gui

class App:
    def __init__(self):
        self.time_step = 0.01
        self.__exit_app = False
        self.__exit_app_lock = threading.Lock()
        self.__init_gui()

    def __del__(self):
        pass

    def start(self):
        self.__loop()

    def exit(self):
        self.gui.exit_loop()
        self.__exit_application(True)

    def __exit_application(self, *argv):
        if len(argv) == 0:
            self.__exit_app_lock.acquire()
            out_state = self.__exit_app
            self.__exit_app_lock.release()
        elif len(argv) == 1 and type(argv[0]) is bool:
            self.__exit_app_lock.acquire()
            self.__exit_app = argv[0]
            self.__exit_app_lock.release()
            out_state = argv[0]
        return out_state

    def __loop(self):
        while not self.__exit_application():
            self.gui.update(self.gui_model)
            time.sleep(self.time_step)

    def __init_gui(self):
        menu = [lib.gui.MenuItem('Exit', self.exit)]
        self.gui = lib.gui.Gui()
        self.gui_model = lib.gui.Model(menu_items=menu)


