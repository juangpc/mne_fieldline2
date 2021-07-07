import mne_config_file_parser as parser
import mne_fieldline_device as fieldline_device

import queue

import threading
import numpy


import FieldTrip

mne_fieldline_config_file = ".mne_fieldline_config.py"

class Device:
    def __init__(self):
        self.verboseMode = False

        self.config = parser.parse_config_file(mne_fieldline_config_file)

        self.opm = fieldline_device.Device()

        # self.__configFtBuffer(config)
        # self.__init_sensors()
        # self.__configFieldtripBuffer()

    def __del__(self):
        self.stop()
        self.exit()
 
    def start(self):
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

    def __printIfVerbose(self, str):
        if self.verboseMode() is True:
            print(str)

    def __numWorkingSensors():

       def __configFtBuffer(self):
        self.ftBuffer.client = FieldTrip.Client()
        self.ftBuffer.ip = self.config.ft_IP
        self.ftBuffer.port = self.config.ft_port
        self.ftBuffer.client.connect(self.ftBuffer.ip, self.ftBuffer.port)
        if self.ftBuffer.client.isConnected:
            self.__printIfVerbose("Fieldtrip Client connected")

        dataType = FieldTrip.DATATYPE_FLOAT32
        if self.ftBuffer.client.isConnected:
            self.ftBuffer.client.putHeader(num_working_sensors(), default_sample_freq, dataType)
        self.ftBuffer.header = self.ftBuffer.client.getHeader()
        if self.ftBuffer.header.nChannels == num_working_sensors():
            self.__printIfVerbose("Fieldtrip header initialized")            
