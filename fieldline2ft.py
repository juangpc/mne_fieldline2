import mne_cpp.ini_file_parser
import mne_cpp.gui

config_file = 'fieldline2ft.ini'

def start():
    pass
    
def stop():
    pass

def void():
    pass

      
gui = mne_cpp.gui.GUI()
gui.set_menu(['START', 'STOP', 'RESTART', 'EXIT'])
gui.set_callbacks([start, stop, void, gui.exit])

gui.start()
