import queue
import time
import threading
import numpy

import mne_fieldline_config as config
import FieldTrip


class FieldlineDevice:
    def __init__(self):
        self.connect()
        self.init_sensors()
        self.verboseMode = False
        self.dataMultiplier = 1

    def __del__(self):
        self.stop_measurement()
        self.disconnect()

    def connect(self):
        lib.init_fieldline_connection()
        lib.init_fieldtrip_connection()
        lib.init_sensors()

    def start_measurement(self):
        if lib.are_sensors_ready():
            lib.init_acquisition()
        else:
            print("Sensors are not initialized")
        
    def stop_measurement(self):
        lib.stop_measurement()

    def disconnect(self):
        lib.stop_service()

    def setVerboseMode(self, v):
        self.verboseMode = v

    def verboseMode(self):
        return self.verboseMode