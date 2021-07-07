import queue
import time
import threading
import numpy
import imp
import os

import mne_fieldline_config as configFile
from fieldline_connector import FieldLineConnector
from fieldline_api.fieldline_service import FieldLineService

import FieldTrip

mneFieldlineConfigFile = ".mne_fieldline_config.py"
class FieldlineDevice:
    def __init__(self):
        self.verboseMode = False
        self.dataMultiplier = 1
        
        self.defaultSamplingFrequency
        self.workingChassis
        self.brokenSensors
        self.workingSensors
        self.ipList
        self.channelKeyList

        self.connector
        self.service

        self.ftBuffer

        self.__parseConfigFile()

        self.__connectToFieldLine()
        self.__connectToFtBuffer()
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

    def __connectToFtBuffer(self):
        pass        

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

    def __parseConfigFile(self):

        currentDirectory = os.getcwd()
        configFile = os.path.join(currentDirectory, mneFieldlineConfigFile)
        config = imp.load_source(configFile)

        self.ip_list = config.ip_list
        self.self.workingChassis = config.self.workingChassis
        self.brokenSensors = config.broken_sensors
        self.workingSensors = config.working_sensors
        self.defaultSamplingFrequency = config.sampling_frequency

        self.ftIP = config.ft_IP
        self.ftPort = config.ft_port

    def __configFieldtripBuffer(self):
        pass

    def __printIfVerbose(self, str):
        if self.verboseMode() is True:
            print(str)
    