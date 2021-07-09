import mne_cpp.gui

class App:
    def __init__(self):
        self.gui = mne_cpp.gui.Gui()
        self.exit_application = False

    def __del__(self):
        pass

    def start(self):
        self.gui.start()

    def set_menu(self, items_list):
        self.gui.set_menu_items(items_list)

    def exit(self):
        self.gui.exit_loop()

    def set_callbacks(self, func_list):
        self.gui.set_callbacks(func_list)


