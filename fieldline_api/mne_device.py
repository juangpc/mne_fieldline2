import mne_config_file_parser
import mne_fieldline_device
import mne_fieldtrip_buffer

mne_fieldline_config_file = ".mne_fieldline_config.py"

class Device:
    def __init__(self):
        self.config = mne_config_file_parser.parse_config_file(mne_fieldline_config_file)
        self.buffer = mne_fieldtrip_buffer.Buffer(self.config)

    def __del__(self):
        self.stop()
 
    def start(self):
        self.config = mne_config_file_parser.parse_config_file(mne_fieldline_config_file)

        # self.device = mne_fieldline_device.Device(self.config)
        self.device.start()

    def stop(self):
        self.device.stop()

    def setVerboseMode(self, v):
        self.verboseMode = v

    def verboseMode(self):
        return self.verboseMode

    def setDataMultiplier(self, m):
        self.dataMultiplier = m

    def dataMultplier(self):
        return self.dataMultiplier



# import queue
# import threading
# import numpy
           
