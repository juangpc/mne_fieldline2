from logging import error
import threading
from lib.fieldline_connector import FieldLineConnector
from fieldline_api.fieldline_service import FieldLineService

import time
import datetime
import numpy
class FieldLineDevice:
    def __init__(self, conf):
        self.connector = FieldLineConnector()
        self.service = FieldLineService(self.connector, prefix = "")
        self.__time_sleep_minor_secs = .4
        self.__time_out_secs = 20
        self.__init_configuration(conf)
        self.measuring_data = False
        self.measuring_data_lock = threading.Lock()

        self.data_callback_lock = threading.Lock()
        self.data_callback = print

    def __del__(self):
        self.stop()
        self.service.stop()

    def __init_configuration(self, conf = None):
        self.ip_list = conf.ip_list
        self.working_chassis = conf.working_chassis
        self.working_sensors = conf.working_sensors
        self.broken_sensors = conf.broken_sensors
        self.channel_key_list = self.__create_channel_key_list()

    def is_connected(self):
        time_start = datetime.datetime.now()
        waiting_time_seconds = (datetime.datetime.now() - time_start).total_seconds
        ch = self.working_chassis[0]
        sens = self.working_sensors[ch][0]
        service_output = self.service.get_sensor_state(ch, sens)

        while service_output is None and waiting_time_seconds < self.__time_out_secs:
            time.sleep(self.__time_sleep_minor_secs)
            service_output = self.service.get_sensor_state(ch, sens)
            waiting_time_seconds = (datetime.datetime.now() - time_start).total_seconds

        if service_output is not None:
            return True
        else:
            return False

    def chassis_version(self):
        version_output = []
        for ch in self.working_chassis:
            version_output.append(self.service.get_version(ch))
        return version_output

    def connect(self):
        if not self.service.is_service_running():
            self.service.start()
            time.sleep(self.__time_sleep_minor_secs)
            if self.is_connected():
                return True
            else:
                return False
        else:
            return False
            
    def init_sensors(self):
        self.__turn_off_all_broken_sensors()
        self.__restart_all_working_sensors()
        self.__coarse_zero_all_working_sensors()
        self.__fine_zero_all_working_sensors()

    def num_working_sensors(self):
        num_sensors = 0
        for ch in self.working_chassis:
            num_sensors += len(self.working_sensors[ch])
        return num_sensors

    def num_fine_zeroed_sensoros(self):
        num_sensors = 0
        if self.connector.fine_zero_sensors:
            for sensors_in_chassis in self.connector.fine_zero_sensors.values():
                num_sensors += len(sensors_in_chassis)
        return num_sensors

    def num_coarse_zeroed_sensors(self):
        num_sensors = 0
        if self.connector.coarse_zero_sensors:
            for sensors_in_chassis in self.connector.coarse_zero_sensors.values():
                num_sensors += len(sensors_in_chassis)
        return num_sensors

    def num_restarted_sensors(self):
        num_sensors = 0
        if self.connector.restarted_sensors:
            for sensors_in_chassis in self.connector.restarted_sensors.values():
                num_sensors += len(sensors_in_chassis)
        return num_sensors

    def start(self):
        if self.service.is_service_running():
            if not self.measuring_data():
                self.service.start_data()
                self.measuring_data(True)
                time.sleep(self.__time_sleep_minor_secs)
                self.acquisition_thread = threading.Thread(target = self.__data_retreiver_thread, daemon = True)
                self.acquisition_thread.start()

    def stop(self):
        if self.measuring_data():
            self.measuring_data(False)
            self.service.stop_data()

    def measuring_data(self, *argv):
        if len(argv) == 0:
            self.measuring_data_lock.acquire()
            out_value = self.measuring_data
            self.measuring_data_lock.release()
        else:
            self.measuring_data_lock.acquire()
            self.measuring_data = argv[0]
            self.measuring_data_lock.release()
        return self.measuring_data()

    def __wait_for_restart_to_finish(self):
        while (self.num_restarted_sensors() < self.num_working_sensors()):
            time.sleep(self.__time_sleep_minor_secs)

    def __wait_for_coarse_zero_to_finish(self):
        while (self.num_coarse_zeroed_sensors() < self.num_working_sensors()):
            time.sleep(self.__time_sleep_minor_secs)

    def __wait_for_fine_zero_to_finish(self):
        while (self.num_fine_zeroed_sensors() < self.num_working_sensors()):
            time.sleep(self.__time_sleep_minor_secs)            

    def __turn_off_all_broken_sensors(self):
        for ch in self.working_chassis:
            for si in self.broken_sensors[ch]:
                self.service.turn_off_sensor(ch, si)

    def __restart_all_working_sensors(self):
        for ch in self.working_chassis:
            for s in self.working_sensors:
                self.service.restart_sensor(ch, s)
                time.sleep(self.__time_sleep_minor_secs)
        self.__wait_for_restart_to_finish()
        
    def __coarse_zero_all_working_sensors(self):
        for ch in self.working_chassis:
            for s in self.working_sensors:
                self.service.coarse_zero_sensor(ch, s)
                time.sleep(self.__time_sleep_minor_secs)
        self.__wait_for_coarse_zero_to_finish()

    def __fine_zero_all_working_sensors(self):
        for ch in self.working_chassis:
            for s in self.working_sensors:
                self.service.fine_zero_sensor(ch, s)
                time.sleep(self.__time_sleep_minor_secs)
        self.__wait_for_fine_zero_to_finish

    def __data_retreiver_thread(self):
        while self.measuring_data():
            data = self.connector.data_q.get()
            self.__parse_data(data)
            self.connector.data_q.task_done()

    def __create_channel_key_list(self):
        channel_key_list = []
        for ch in self.working_chassis:
            for s in self.working_sensors[ch]:
                key = str(ch).zfill(2) + ':' + str(s).zfill(2) + ':' + str(28).zfill(2)
                channel_key_list.append(key)
        return channel_key_list

    def set_data_callback(self, callback):
        self.data_callback_lock.acquire()
        self.data_callback = callback
        self.data_callback_lock.release()

    def __parse_data(self, data):
        chunk = numpy.zeros(len(data), self.num_working_sensors(), dtype=numpy.single)
        for sample_i in range(len(data)):
            for ch_i, channel in enumerate(self.channel_key_list):
                chunk[sample_i, ch_i] = data[0][channel]["data"] * data[0][channel]["calibration"]
        self.data_callback(chunk)


