import lib.fieldline
import lib.log
import lib.application
import lib.ini_file_parser
import lib.FieldTrip

import logging
import time

log = logging.getLogger('main')

class IncorrectInstallationMenu:
    def __init__(self):
        self.menu_list = [('Incorrect FieldLine installation. Please re-install and try again.', app.exit)]

class ConnectToFieldline:
    def __init__(self):
        self.menu_list = [('Connect to Fieldline', self.connect_to_fieldline),
                          ('Exit', app.exit) ]
    
    def connect_to_fieldline(self):
        log.info("connecting to new state: ConnectedState")
        app.set_gui_menu(ConnectedState())
    
class ConnectedState:
    def __init__(self):
        self.menu_list = [('Disconnect from FieldLine', self.disconnect_from_fieldline),
                          ('Tune sensors', self.tune_sensors),
                          ('Start data acquisition', self.start_acquisition),
                          ('Exit', app.exit) ]

    def disconnect_from_fieldline(self):
        app.set_gui_menu(ConnectToFieldline())

    def tune_sensors(self):
        app.set_gui_menu(TunningSensorsState())

    def start_acquisition(self):
        app.set_gui_menu(AcquisitionState())


class TunningSensorsState:
    def __init__(self):
        self.menu_list = [('Tunning sensors...', void),
                          ('Go Back', self.go_back),
                          ('Exit', app.exit)]
        
    def go_back(self):
        app.set_gui_menu(ConnectedState())

class AcquisitionState:
    def __init__(self):
        self.menu_list = [('Stop data acquisition', self.stop_acquisition),
                          ('Exit', app.exit)]
    def stop_acquisition(self):
        app.set_gui_menu(ConnectedState())

def void():
    pass

## ###############################################################################

log.info("Starting fieldline2ft application.")
log.info("Creating main app.")
app = lib.application.App()

log.info("Parsing input file.")
config = lib.ini_file_parser.parse_file('fieldline2ft.ini')
log.debug(config)

if lib.fieldline.fieldline_correctly_installed():
    app.set_gui_menu(ConnectToFieldline())
else:
    app.set_gui_menu(IncorrectInstallationMenu(app))

fieldline = lib.fieldline.FieldLineDevice(config.fieldline)

ft_buffer_client = lib.FieldTrip.Client()

def connect_to_fieldtrip_buffer():
    log.info("Attempting to connect to Fieldtrip Buffer")
    ft_buffer_client.connect(config.fieldtrip.ft_IP, config.fieldtrip.ft_port)
    if ft_buffer_client.isConnected():
        log.info("Connection with FT Buffer successful.")
    else:
        log.info("Connection with FT Buffer failed.")
        log.debug(ft_buffer_client)
     
def init_ft_header():
    if ft_buffer_client.isConnected:
        ft_buffer_client.putHeader(fieldline.num_working_sensors(), config.dieldtrip.sampling_frequency, lib.FieldTrip.DATATYPE_FLOAT32)
        header = ft_buffer_client.getHeader()
        if header.nChannels == fieldline.num_working_sensors():
            log.info("Fieldtrip header initialized")
        else:
            log.info("Fieldtrip header NOT initialized")

# def test_data_to_ft():
#     arr_data = nunmpy.zeros((200,num_working_sensors()), dtype=numpy.single)
#     ft_client.putData(arr_data)
    
# def init_fieldtrip_connection():
#     connect_to_fieldtrip_buffer()
#     init_ft_header()                


# def exit():
#     mne.disconnect
#     app.exit

app.start()