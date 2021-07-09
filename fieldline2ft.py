import lib.mne_ini_file_parser
import lib.fieldline2ft_gui

config_file = 'fieldline2ft.ini'

def start():
    pass
    
def stop():
    pass

def void():
    pass

      
gui = lib.fieldline2ft_gui.GUI()
gui.set_menu(['START', 'STOP', 'RESTART', 'EXIT'])
gui.set_callbacks([start, stop, void, gui.exit])

gui.start()
