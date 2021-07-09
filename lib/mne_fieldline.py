import lib.mne_fieldline_lib as fl_lib

def connect():
    fl_lib.init_fieldline_connection()
    fl_lib.init_fieldtrip_connection()
    fl_lib.init_sensors()

def start_measurement():
    if fl_lib.are_sensors_ready():
        fl_lib.init_acquisition()
    else:
        print("Sensors are not initialized")

def stop_measurement():
    fl_lib.stop_measurement()

def disconnect():
    fl_lib.stop_service()

def tune_sensors():
    fl_lib.init_sensors()

def stop_tune_sensors():
    pass

def phantom_on():
    pass

def phantom_off():
    pass

class main_runner:
    def __init__(self):
        connect()
        fl_lib.init_sensors()
        pass

    def __del__(self):
        print("Destructor called") 
        stop_measurement()
        disconnect()

