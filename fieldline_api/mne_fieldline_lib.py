import queue
import time
import threading
import numpy
import imp
import os

from fieldline_connector import FieldLineConnector
from fieldline_api.fieldline_service import FieldLineService
import FieldTrip

mneFieldlineConfigFile = ".mne_fieldline_config.py"

def parseConfigFile(file):
    
    currentDirectory = os.getcwd()
    configFile = os.path.join(currentDirectory, file)
    config = imp.load_source(configFile)
    
    return config
class FieldlineDevice:
    def __init__(self):
        self.verboseMode = False
        self.dataMultiplier = 1

        self.connector
        self.service

        self.ftBuffer

        self.config = self.parseConfigFile(mneFieldlineConfigFile)

        self.__connectToFieldLine()
        self.__configFtBuffer()
        # self.__init_sensors()
        # self.__configFieldtripBuffer()

    def __del__(self):
        self.stop()
        self.exit()

    def __connectToFieldLine(self):
        self.connector = FieldLineConnector()
        self.service = FieldLineService(self.connector, prefix = "")
        time.sleep(.5)
        self.service.start()
        self.service.connect(self.ipList)
        while self.service.get_sensor_state(0,1) is None:
            time.sleep(.5)
        self.__printIfVerbose ("Fieldline service connected.")
        for chassis in self.workingChassis:
            version = self.service.get_version(chassis)
            self.__printIfVerbose("Connection with chassis: " + str(chassis) + "... OK")
            self.__printIfVerbose("Chassis " + str(version))
        self.__printIfVerbose("---")

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
        header = self.ftBuffer.client.getHeader()
        if header.nChannels == num_working_sensors():
            print("Fieldtrip header initialized")            

    # def start(self):
    #     if lib.are_sensors_ready():
    #         lib.init_acquisition()
    #     else:
    #         print("Sensors are not initialized")
        
    # def stop(self):
    #     lib.stop()

    # def exit(self):
    #     lib.stop_service()

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
    