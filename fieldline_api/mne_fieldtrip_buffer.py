import FieldTrip

class Buffer:
    def __init__(self, config):
        self.buffer = FieldTrip.Client()
        self.ip = config.ft_IP
        self.port = config.ft_port
        self.num_sensors = config.num_sensors
        self.sampling_frequency = config.sampling_frequency

        self.data_type = FieldTrip.DATATYPE_FLOAT32

        self.connect()

    def __del__(self):
        pass

    def connect(self):
        self.buffer.connect(self.ip, self.port)
        if self.is_connected():
            print("FieldTrip buffer connected.")

    def init_header(self):
        if self.is_connected():
            self.buffer.putHeader(self.num_sensors, self.sampling_frequency, self.data_type)
            self.header = self.buffer.getHeader()

    def putData(self, data):
        if self.is_connected():
            self.buffer.putData(data)

    def is_connected(self):
        return self.buffer.isConnected
    

