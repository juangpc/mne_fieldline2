import lib.globals as globals
import logging
import time

log = logging.getLogger(__name__)

class IncorrectInstallationMenu:
    def __init__(self):
        self.menu_list = [('Incorrect FieldLine installation. Please re-install and try again.', globals.exit)]

class ConnectToFieldline:
    def __init__(self):
        self.menu_list = [('Connect to Fieldline', self.connect_to_fieldline),
                          ('Exit', globals.exit) ]
    
    def connect_to_fieldline(self):
        log.info("connecting to new state: ConnectedState")
        globals.app.set_gui_menu(ConnectedState())
    
class ConnectedState:
    def __init__(self):
        self.menu_list = [('Disconnect from FieldLine', self.disconnect_from_fieldline),
                          ('Tune sensors', self.tune_sensors),
                          ('Start data acquisition', self.start_acquisition)
                          ('Exit', globals.exit) ]

    def disconnect_from_fieldline(self):
        globals.switch_to_menu(ConnectToFieldline())

    def tune_sensors(self):
        globals.switch_to_menu(TunningSensorsState())

    def start_acquisition(self):
        globals.switch_to_menu(AcquisitionState())

class TunningSensorsState:
    def __init__(self):
        self.menu_list = [('Exit', globals.exit)]
        time.sleep(4)
        globals.switch_to_menu(ConnectedState)

class AcquisitionState:
    def __init__(self):
        self.menu_list = [('Stop data acquisition', self.stop_acquisition),
                          ('Exit', globals.exit)]
    def stop_acquisition(self):
        globals.switch_to_menu(ConnectedState())


