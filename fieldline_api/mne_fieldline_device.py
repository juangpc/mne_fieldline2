from fieldline_connector import FieldLineConnector
from fieldline_api.fieldline_service import FieldLineService
import time

class Device():
    def __init__(self, config):
        self.__parse_config_values(config)

        self.connector = FieldLineConnector()
        self.service = FieldLineService(self.connector, prefix = "")
        time.sleep(.5)

    def __del__(self):
        pass

    def __parse_config_values(self, config):
        self.config.ip_list = config.ip_list
        self.working_chassis = config.working_chassis
        self.broken_sensors =  config.broken_sensors 
        self.working_sensors = config.working_sensors
        self.sampling_frequency = config.sampling_frequency



    def connect(self):
        self.service.start()
        self.connector(self.config.ipList)
        while self.fieldlineService.get_sensor_state(0,1) is None:
            time.sleep(.5)
        self.__printIfVerbose ("Fieldline service connected.")
        for chassis in self.config.workingChassis:
            version = self.fieldlineService.get_version(chassis)
            self.__printIfVerbose("Connection with chassis: " + str(chassis) + "... OK")
            self.__printIfVerbose("Chassis " + str(version))
        self.__printIfVerbose("---")

    def start(self):
        pass

        #     if lib.are_sensors_ready():
        #     lib.init_acquisition()
        # else:
        #     print("Sensors are not initialized")