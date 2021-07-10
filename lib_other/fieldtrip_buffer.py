import FieldTrip
import numpy

class FieldTripBuffer:
    def __init__(self):
        pass

    


ft_client = FieldTrip.Client()
ft_IP = config.ft_IP
ft_port = config.ft_port
ft_data_type = FieldTrip.DATATYPE_FLOAT32

data_stream_multiplier = 1

def connect_to_fieldtrip_buffer():
    ft_client.connect(ft_IP, ft_port)
    if ft_client.isConnected:
        print("Fieldtrip Client connected")

def init_ft_header():
    if ft_client.isConnected:
        ft_client.putHeader(num_working_sensors(), default_sample_freq, ft_data_type)
        header = ft_client.getHeader()
        if header.nChannels == num_working_sensors():
            print("Fieldtrip header initialized")

def test_data_to_ft():
    arr_data = nunmpy.zeros((200,num_working_sensors()), dtype=numpy.single)
    ft_client.putData(arr_data)
    
def init_fieldtrip_connection():
    connect_to_fieldtrip_buffer()
    init_ft_header()                