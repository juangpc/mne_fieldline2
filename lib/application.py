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

    def __init_gui(self):
        self.gui = lib.gui.Gui()
        self.__gui_menu = None
        self.__gui_menu_lock = threading.Lock()
        self.gui_menu([('Exit', self.exit)])

    def set_gui_menu(self, menu):
        self.gui_menu(menu.menu_list)

    def start(self):
        self.__loop_thread = threading.Thread(target = self.__loop)
        self.__loop_thread.start()

    def exit(self):
        self.gui.exit_loop()
        self.__exit_application(True)

    def gui_menu(self, *argv):
        if len(argv) == 0:
            self.__gui_menu_lock.acquire()
            out_menu = self.__gui_menu
            self.__gui_menu_lock.release()
        else: 
            self.__gui_menu_lock.acquire()
            self.__gui_menu = argv[0]
            self.__gui_menu_lock.release()
            out_menu = self.gui_menu()
        return out_menu
        
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
            self.gui.update(self.gui_menu())
            time.sleep(self.time_step)




