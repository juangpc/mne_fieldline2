import mne_cpp.ini_file_parser
import mne_cpp.application

config_file = 'fieldline2ft.ini'

def start():
    pass
    
def stop():
    pass

def void():
    pass

      
app = mne_cpp.application.App()
app.set_menu(['START', 'STOP', 'RESTART', 'EXIT'])
app.set_callbacks([start, stop, void, app.exit])

app.start()
